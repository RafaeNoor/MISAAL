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

(define (expanded-grammar-synthesize 
                                   invoke_ref ; expr -> env -> bv
                                   invoke_ref_lane ; expr -> lane-idx -> env -> bv
                                   grammar-fn-src
                                   grammar-fn-dst
                                   bitwidth-list
                                   optimize?
                                   interpreter-fn
                                   cost-fn
                                   symbolic?
                                   cost-bound
                                   solver)

  (if (equal? solver 'boolector) (current-solver (boolector)) (current-solver (z3)))

  (cond
    [symbolic?
     (error "expanded-grammar-synthesize symbolic synthesis not yet supported")
     ]
    [else

        (define-values (satisfiable? materialize-src  materialize-dst )
                       (expanded-grammar-synthesize-iterative
                                                 invoke_ref
                                                 invoke_ref_lane
                                                 grammar-fn-src
                                                 grammar-fn-dst
                                                 bitwidth-list
                                                 optimize?
                                                 interpreter-fn
                                                 cost-fn
                                                 '()
                                                 '()
                                                 cost-bound
                                                 solver
                                                 '())

                       )
        (values satisfiable?  materialize-src  materialize-dst )
      ]
    )
  )


(define (expanded-grammar-synthesize-iterative 
                                  invoke_ref
                                  invoke_ref_lane
                                  grammar-fn-src
                                  grammar-fn-dst
                                  bitwidth-list
                                  optimize?
                                  interpreter-fn
                                  cost-fn
                                  cexs
                                  failing-lanes
                                  cost-bound
                                  solver
                                  failed-sols)
  (debug-log "expanded-grammar-synthesize-iterative")

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

      (define output-size (bvlength (invoke_ref grammar-fn-src (list-ref cex-ls 0))))
      (define lane-sol (invoke_ref_lane grammar-fn-src 0 (list-ref cex-ls 0)))
      (define word-size (bvlength lane-sol))
      (define num-lanes (/ output-size word-size))

      (define failing-ls (if (equal? (length failing-lanes) 0) (list 0 0) failing-lanes))

      (debug-log "Concrete counter examples:")
      (debug-log cex-ls)

      (debug-log "Failing lanes examples:")
      (debug-log failing-ls)

      ;; Sythesizing keeping only a single lane
      ;; in the assertion. We'll verify over all
      ;; lanes
      (define (assert-query-synth-fn env random-idx)
        (debug-log "Interpreting on single lane")

        (define full-interpret-res (interpreter-fn grammar-fn-dst env))
        (debug-log full-interpret-res)
        (debug-log "Lane Index for grammar")
        (debug-log random-idx)

        (define low (* word-size random-idx))
        (define high (+ low (- word-size 1)))


        (define halide-res (invoke_ref_lane grammar-fn-src (+ random-idx 0) env))

        (debug-log "Spec Produced:")
        (debug-log halide-res)
        (debug-log (bvlength halide-res))

        (debug-log "Spec Produced (full):")
        (define full-spec-res (invoke_ref grammar-fn-src  env))
        (debug-log full-spec-res)
        (debug-log (bvlength full-spec-res))

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
        (assert condition)
        )

      (define start_time (current-seconds))
      (define sol?
        (iterative-synth-query assert-query-synth-fn
                               grammar-fn-dst
                               cex-ls
                               failing-ls
                               optimize?
                               cost-fn
                               cost-bound
                               solver
                               failed-sols))

      (define end_time (current-seconds))

      (define satisfiable? (sat? sol?))

      (debug-log satisfiable?)

      (define complete-sol? 
        (if satisfiable?
          (complete-solution sol? (append (symbolics grammar-fn-dst) (symbolics grammar-fn-src)))
          sol?
          )
        )


      (define materialize-dst
        (if satisfiable?
          (evaluate grammar-fn-dst complete-sol?)
          '()))

      (define materialize-src
        (if satisfiable?
          (evaluate grammar-fn-src complete-sol?)
          '()))

      (debug-log "Materialized expressions")
      (debug-log "src")
      (debug-log materialize-src)


      (debug-log (evaluate materialize-src sol?))

      (debug-log "dst")
      (debug-log materialize-dst)

      (define iterative-opt-case
        (and optimize?
             ;(equal? solver 'boolector)
             iterative-optimize))

      (debug-log (format "Is this iterative optimization case ~a ?\n" iterative-opt-case))


      (define is-union (or (not (concrete? materialize-src)) (not (concrete? materialize-dst))   ))


      (cond
        [(and satisfiable? (not is-union))

         ;; If satisfiable, verify current solution and check
         ;; if it's true over ALL inputs
         (begin

           (debug-log "Unchecked solution:")
           (debug-log materialize-src)
           (debug-log materialize-dst)

           (debug-log (format "Is concrete? ~a\n" (concrete? materialize-dst)))

           (debug-log (format "Is solution a union? ~a\n" is-union))

           (define (invoke_sol_verify_lane lane-idx env)
             (define intermediate-result (interpreter-fn materialize-dst env))
             (define low (* word-size lane-idx))
             (define high (+ low (- word-size 1)))
             (extract high low intermediate-result))

           (define (invoke_ref_verify_lane lane-idx env)
             (invoke_ref_lane materialize-src lane-idx env)
             )

           (define (invoke_ref_verify env)
             (invoke_ref materialize-src  env)
             )

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
                                                       invoke_ref_verify_lane
                                                       invoke_sol_verify_lane
                                                       solver
                                                       word-size
                                                       output-size))
                                (if verify-individual-lanes
                                  (values #t '())
                                  (verify-synth-sol materialize-dst bitwidth-list invoke_ref_verify solver interpreter-fn)
                                  )
                                )]
                            [else 
                              (verify-synth-sol materialize-dst bitwidth-list invoke_ref_verify solver interpreter-fn)
                              ]
                            )
                          )


           (if verified? ;; If solution is found to be correct for all possible inputs

             ;; Check if optimizations is enabled and the current solver is boolector
             (if iterative-opt-case

               ;; If true, then attempt synthesizing a solution with a tighter cost bound
               (begin
                 (debug-log "Iterative optimization, refine search")
                 (define simplify  materialize-dst)
                 (debug-log (format "Searching for better solution with cost < ~a \n"
                                    (cost-fn simplify)))
                 (define-values (tighter-sol-sat? tighter-sol-materialize-src tighter-sol-materialize-dst )
                                (expanded-grammar-synthesize-iterative invoke_ref
                                                          invoke_ref_lane
                                                          grammar-fn-src
                                                          grammar-fn-dst
                                                          bitwidth-list
                                                          optimize?
                                                          interpreter-fn
                                                          cost-fn
                                                          cex-ls
                                                          failing-ls
                                                          (cost-fn simplify) ;; Use tighter cost bound
                                                          solver
                                                          failed-sols))

                 ;; If a tighter solution exists then return that, else return current found solution
                 (if tighter-sol-sat?
                   (values tighter-sol-sat? tighter-sol-materialize-src  tighter-sol-materialize-dst )
                   (values satisfiable? tighter-sol-materialize-src simplify )))

               ;; If not doing optimizaiton and boolector then return current verified solution directly
               (begin
                 (if (and optimize? (not iterative-opt-case))

                   (begin

                     (set-optimize-bound-found #t)
                     (values satisfiable? materialize-src materialize-dst ))

                   (values satisfiable? materialize-src materialize-dst ))))

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
                 (get-failing-lanes invoke_ref_verify
                                    materialize-dst
                                    (list new-failing-cex)
                                    word-size
                                    interpreter-fn))

               (expanded-grammar-synthesize-iterative
                 invoke_ref
                 invoke_ref_lane
                 grammar-fn-src
                 grammar-fn-dst
                 bitwidth-list
                 optimize?
                 interpreter-fn
                 cost-fn
                 (append cex-ls (list new-failing-cex)) ;; Append new cex into accumulated inputs
                 (append failing-ls new-failing-lane)
                 cost-bound
                 solver
                 (append failed-sols (list materialize-dst))))))]

        ;; Found a solution, but it contains a symbolic
        ;; union term as one of the sub-trees. Add another
        ;; counter example and re-attempt synthesis.
        [(and satisfiable? (<= (length cex-ls) 15))
         (begin
           (debug-log "Contains symbolic union, retry synthesis")
           (debug-log "Union solution:")
           (debug-log materialize-dst)
           (expanded-grammar-synthesize-iterative
             invoke_ref
             invoke_ref_lane
             grammar-fn-src
             grammar-fn-dst
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
             (append failed-sols (list materialize-dst))))]
        ;; Found union-solutions and exceed number of CEXs
        ;; , return failure
        [satisfiable? (values #f materialize-src materialize-dst )]
        [else
          (values satisfiable? materialize-src materialize-dst ) ;; If not satisfiable just return current state
          ])])
  )

