#lang rosette




(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require racket/sandbox)
(require data/bit-vector)
(require rosette/lib/destruct)
(require rosette/solver/smt/boolector)
(require rosette/solver/smt/z3)
(require hydride/utils/bvops)
(require hydride/utils/debug)
(require hydride/utils/target)
(require hydride/utils/misc)
(require hydride/ir/hydride/interpreter)
(require hydride/ir/hydride/visitor)

(require hydride/ir/hvx/interpreter)
(require hydride/ir/hvx/const_fold)
(require hydride/ir/hvx/visitor)

(require hydride/ir/arm/interpreter)
(require hydride/ir/arm/const_fold)
(require hydride/ir/arm/visitor)

(require hydride/ir/hydride/const_fold)
(require hydride/ir/hydride/length)
(require hydride/synthesis/symbolic_synthesis)
(require hydride/synthesis/iterative_synthesis)




(require hydride/halide)


(provide (all-defined-out))

(define (synthesize-sol-iterative-constraints invoke_ref
                                  invoke_ref_lane
                                  grammar
                                  bitwidth-list
                                  optimize?
                                  interpreter-fn
                                  cost-fn
                                  cexs
                                  failing-lanes
                                  cost-bound
                                  solver
                                  failed-sols
                                  constraint-fn
                                  )
  (debug-log "synthesize-sol-iterative-constraints")

  (cond
    [(and optimize? (not iterative-optimize) optimize-bound-found)
     (debug-log "Escaping early as other thread found optimize bound solution")
     (values #f '() -1)]
    [(and global-timeout? (>= (- (current-seconds) start-time) GLOBAL_TIMEOUT))
     (debug-log "Global Timeout exceeded: exiting ...")
     (values #f '() -1)]
    [(>= (length cexs) 15)
     (debug-log "Escaping early as exceeded quota for number of cex allowed")
     (values #f '() -1)]
    [else
     ;; Clear the verification condition up till this point
     (clear-vc!)

     ;(gc-terms!)

     (collect-garbage)
     (debug-log "Garbage collected")
     ;; If the cexs is empty
     ;; create a random set of concrete inputs
     ;; else use the concrete inputs accumulated
     ;; so far
     (define cex-ls
       (if (equal? (length cexs) 0)
           (list (create-concrete-bvs bitwidth-list) (create-concrete-bvs bitwidth-list))
           cexs))

     (define output-size (bvlength (invoke_ref (list-ref cex-ls 0))))
     (define lane-sol (invoke_ref_lane 0 (list-ref cex-ls 0)))
     (define word-size (bvlength lane-sol))
     (define num-lanes (/ output-size word-size))

     (define failing-ls (if (equal? (length failing-lanes) 0) (list 0 (- num-lanes 1)) failing-lanes))

     (debug-log "Concrete counter examples:")
     (debug-log cex-ls)

     (debug-log "Failing lanes examples:")
     (debug-log failing-ls)

     ;; Sythesizing keeping only a single lane
     ;; in the assertion. We'll verify over all
     ;; lanes
     (define (assert-query-synth-fn env random-idx)
       (debug-log "Interpreting on single lane")

       (define full-interpret-res (interpreter-fn grammar env))
       (debug-log full-interpret-res)
       (debug-log "Lane Index for grammar")
       (debug-log random-idx)

       (define low (* word-size random-idx))
       (define high (+ low (- word-size 1)))


       (define halide-res (invoke_ref_lane (+ random-idx 0) env))

       (debug-log "Spec Produced:")
       (debug-log halide-res)

        (debug-log "Spec Produced (full):")
        (define full-spec-res (invoke_ref env))
        (debug-log full-spec-res)

       (if synthesize-by-lane
           (debug-log "Synthesize by lane...")
           (debug-log "Synthesize by entire vector size..."))


       (debug-log "Full-interpret-res")
       (debug-log full-interpret-res)

       (debug-log (equal? full-spec-res full-interpret-res) )
       (define condition
         (if synthesize-by-lane
             (equal? halide-res (extract high low full-interpret-res) )
             (equal? full-spec-res full-interpret-res)
             
             ))

       (println (bvlength full-interpret-res))
       (println (bvlength full-spec-res))


       (debug-log "Condition")
       (debug-log condition)


       ;; Additional constraints
       (define add-constraints (constraint-fn grammar env))
       ;(assert (and condition add-constraints))
       (assert condition)
       (assert add-constraints)
       )

     (define start_time (current-seconds))
     (define sol?
       (iterative-synth-query-constraints assert-query-synth-fn
                              grammar
                              cex-ls
                              failing-ls
                              optimize?
                              cost-fn
                              cost-bound
                              solver
                              failed-sols))

     (define end_time (current-seconds))
     (define elapsed_time (- end_time start_time))

     (define satisfiable? (sat? sol?))

     (debug-log satisfiable?)

     (define materialize
       (if satisfiable?
           (evaluate grammar sol?)

           '()))

     (define iterative-opt-case
       (and optimize?
            ;(equal? solver 'boolector)
            iterative-optimize))

     (debug-log (format "Is this iterative optimization case ~a ?\n" iterative-opt-case))

     (define visitor-functor
       (cond
         [(equal? target 'x86) hydride:visitor]
         [(equal? target 'arm) arm:visitor]
         [(equal? target 'hvx) hvx:visitor]))

     (define is-union (not (concrete? materialize)))

     ;(set! materialize
     ;  (cond
     ;    [is-union
     ;      (set! is-union #f)
     ;      (de-union-expression materialize visitor-functor)
     ;      ]
     ;    [else
     ;      materialize
     ;      ]
     ;    )
     ;  )

     (cond
       [(and satisfiable? (not is-union))

        ;; If satisfiable, verify current solution and check
        ;; if it's true over ALL inputs
        (begin

          (debug-log "Unchecked solution:")
          (debug-log materialize)

          (debug-log (format "Is concrete? ~a\n" (concrete? materialize)))

          (debug-log (format "Is solution a union? ~a\n" is-union))

          (define (invoke_sol_lane lane-idx env)
            (define intermediate-result (interpreter-fn materialize env))
            (define low (* word-size lane-idx))
            (define high (+ low (- word-size 1)))
            (extract high low intermediate-result))

          (define-values (verified? new-cex)
            (cond
              [synthesize-by-lane
               ;; For operations involving division the solver
               ;; often get's stuck when verifying a correct
               ;; solution. Hence we first do a quick verification
               ;; across lanes individually and only execute full verification
               ;; when there exists some lane which failed.
               (begin
                 (define verify-individual-lanes
                   (verify-across-lanes bitwidth-list
                                        invoke_ref_lane
                                        invoke_sol_lane
                                        solver
                                        word-size
                                        output-size))
                 (if verify-individual-lanes
                     (values #t '())
                     (verify-synth-sol materialize bitwidth-list invoke_ref solver interpreter-fn)))]
              [else (verify-synth-sol materialize bitwidth-list invoke_ref solver interpreter-fn)]))

          (define const-fold
            (cond
              [(equal? target 'x86) hydride:const-fold]
              [(equal? target 'arm) arm:const-fold]
              [(equal? target 'hvx) hvx:const-fold]))

          (if verified? ;; If solution is found to be correct for all possible inputs

              ;; Check if optimizations is enabled and the current solver is boolector
              (if iterative-opt-case

                  ;; If true, then attempt synthesizing a solution with a tighter cost bound
                  (begin
                    (debug-log "Iteartive optimization, refine search")
                    (define simplify (const-fold materialize))
                    (debug-log (format "Searching for better solution with cost < ~a \n"
                                       (cost-fn simplify)))
                    (define-values (tighter-sol-sat? tighter-sol-materialize tighter-sol-elapsed-time)
                      (synthesize-sol-iterative-constraints invoke_ref
                                                invoke_ref_lane
                                                grammar
                                                bitwidth-list
                                                optimize?
                                                interpreter-fn
                                                cost-fn
                                                cex-ls
                                                failing-ls
                                                (cost-fn simplify) ;; Use tighter cost bound
                                                solver
                                                failed-sols
                                                constraint-fn
                                                ))

                    ;; If a tighter solution exists then return that, else return current found solution
                    (if tighter-sol-sat?
                        (values tighter-sol-sat? tighter-sol-materialize tighter-sol-elapsed-time)
                        (values satisfiable? simplify elapsed_time)))

                  ;; If not doing optimizaiton and boolector then return current verified solution directly
                  (begin
                    (if (and optimize? (not iterative-opt-case))

                        (begin

                          (set-optimize-bound-found #t)
                          (values satisfiable? materialize elapsed_time))

                        (values satisfiable? materialize elapsed_time))))

              ;; If not verified then attempt synthesizing with appended counter example
              (begin
                (define new-failing-cex
                  (if (member new-cex cex-ls)
                      (begin
                        (debug-log
                         "Returned a counter example which was previously seen, generating different cex")
                        (create-concrete-bvs bitwidth-list))
                      new-cex))
                (define new-failing-lane
                  (get-failing-lanes invoke_ref
                                     materialize
                                     (list new-failing-cex)
                                     word-size
                                     interpreter-fn))

                (synthesize-sol-iterative-constraints
                 invoke_ref
                 invoke_ref_lane
                 grammar
                 bitwidth-list
                 optimize?
                 interpreter-fn
                 cost-fn
                 (append cex-ls (list new-failing-cex)) ;; Append new cex into accumulated inputs
                 (append failing-ls new-failing-lane)
                 cost-bound
                 solver
                 (append failed-sols (list materialize))
                 constraint-fn
                 
                 
                 ))))]

       ;; Found a solution, but it contains a symbolic
       ;; union term as one of the sub-trees. Add another
       ;; counter example and re-attempt synthesis.
       [(and satisfiable? (<= (length cex-ls) 15))
        (begin
          (debug-log "Contains symbolic union, retry synthesis")
          (debug-log "Union solution:")
          (debug-log materialize)
          (synthesize-sol-iterative-constraints
           invoke_ref
           invoke_ref_lane
           grammar
           bitwidth-list
           optimize?
           interpreter-fn
           cost-fn
           (append cex-ls
                   (list (create-concrete-bvs
                          bitwidth-list))) ;; Append new cex into accumulated inputs
           (append failing-ls (list (random num-lanes)))
           cost-bound
           solver
           (append failed-sols (list materialize))
           constraint-fn
           ))]
       ;; Found union-solutions and exceed number of CEXs
       ;; , return failure
       [satisfiable? (values #f materialize elapsed_time)]
       [else
        (values satisfiable? materialize elapsed_time) ;; If not satisfiable just return current state
        ])]))



(define (iterative-synth-query-constraints assert-query-fn
                               grammar
                               cex-ls
                               failing-ls
                               optimize?
                               cost-fn
                               cost-bound
                               solver
                               failed-sols)

  (cond
    [(and optimize? (equal? solver 'boolector))
     (boolector-optimize-constraints assert-query-fn grammar cex-ls failing-ls cost-fn cost-bound failed-sols)]
    [(and optimize? (equal? solver 'z3) iterative-optimize)
     (z3-optimize-iterative-constraints assert-query-fn grammar cex-ls failing-ls cost-fn cost-bound failed-sols)]
    [(and optimize? (equal? solver 'z3))
     (z3-optimize-constraints assert-query-fn grammar cex-ls failing-ls cost-fn cost-bound failed-sols)]
    [else
     (regular-concrete-synthesis-constraints assert-query-fn
                                 grammar
                                 cex-ls
                                 failing-ls
                                 cost-fn
                                 cost-bound
                                 failed-sols)]))


(define (boolector-optimize-constraints assert-query-fn grammar cex-ls failing-ls cost-fn cost-bound failed-sols)
  (begin
    (debug-log (format "Boolector optimize with cost-bound ~a ...\n" cost-bound))
    (debug-log "Synthesizing...\n")
    ;(current-solver (boolector))
    ;(current-bitwidth 16)
    ;(custodian-limit-memory (current-custodian) (* 20000 1024 1024))

    (define sol?
      (synthesize #:forall (list cex-ls)
                  #:guarantee (begin
                                ;; loop over inputs and add asserts
                                (get-concrete-asserts assert-query-fn cex-ls failing-ls)
                                (assert (< (cost-fn grammar) cost-bound)))))

    (define satisfiable? (sat? sol?))

    (define materialize (if satisfiable? (evaluate grammar sol?) '()))

    (if satisfiable? (debug-log materialize) '())

    sol?))

(define (z3-optimize-iterative-constraints assert-query-fn
                               grammar
                               cex-ls
                               failing-ls
                               cost-fn
                               cost-bound
                               failed-sols)
  (begin
    (debug-log (format "z3-optimize iterative with cost-bound ~a ...\n" cost-bound))
    (debug-log "Synthesizing...\n")

    (define sol?
      (synthesize #:forall (list cex-ls)
                  #:guarantee (begin
                                ;; loop over inputs and add asserts
                                (get-concrete-asserts assert-query-fn cex-ls failing-ls)
                                (assert (< (cost-fn grammar) cost-bound)))))

    (define satisfiable? (sat? sol?))

    (define materialize (if satisfiable? (evaluate grammar sol?) '()))

    (if satisfiable? (debug-log materialize) '())

    sol?))


(define (z3-optimize-constraints assert-query-fn grammar cex-ls failing-ls cost-fn cost-bound failed-sols)
  (begin
    (debug-log "*********** z3-optimize *****************")
    (define synthesis-timeout? #f)
    (define sol?
      (cond
        [synthesis-timeout?
         (with-handlers ([exn:fail? (lambda (exn)
                                      (begin
                                        (debug-log "Synthesis timed-out ...")
                                        (unsat)))])
           (with-deep-time-limit 10000 ; 2 hours timeout
                                 (optimize #:minimize (list (cost-fn grammar))
                                           #:guarantee
                                           ;; loop over inputs and add asserts
                                           (begin
                                             (get-concrete-asserts assert-query-fn cex-ls failing-ls)
                                             ;(assert (< (cost-fn grammar) cost-bound))
                                             ))))]
        [else

         (optimize #:minimize (list (cost-fn grammar))
                   #:guarantee
                   ;; loop over inputs and add asserts
                   (begin
                     (get-concrete-asserts assert-query-fn cex-ls failing-ls)
                     ;(assert (< (cost-fn grammar) cost-bound))
                     ))]))
    (if (sat? sol?)
        (begin
          (define mat (evaluate grammar sol?))
          (debug-log "Z3 Synthesized Solution")
          (debug-log mat))
        '())
    sol?))


(define (regular-concrete-synthesis-constraints assert-query-fn
                                    grammar
                                    cex-ls
                                    failing-ls
                                    cost-fn
                                    cost-bound
                                    failed-sols)
  (begin
    (debug-log "*** regular-concrete-synthesis ***")
    (synthesize #:forall (list cex-ls)
                #:guarantee (begin
                              ;; loop over inputs and add asserts
                              (get-concrete-asserts assert-query-fn cex-ls failing-ls)
                              ;(assert (< (cost-fn grammar) cost-bound))
                              ))))
