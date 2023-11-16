#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require rosette/lib/destruct)
(require rosette/solver/smt/boolector)
(require rosette/solver/smt/z3)
(require hydride/utils/bvops)
(require hydride/utils/debug)
(require hydride/utils/misc)
(require hydride/synthesis/iterative_synthesis)
(require hydride/synthesis/synth_main)
(require hydride/synthesis/python)



(require misaal/synthesis/target_desc)
(require misaal/synthesis/grammar_utils)




(require hydride/halide)


(provide (all-defined-out))

(define (misaal-rewrite-ir spec-expr  starting-depth depth-limit  optimize? symbolic? solver input-sizes input-precs scale-factor src-language-desc target-language-desc cost-model-type target-symbol)
  (debug-log (format "Invoked step-wise-synthesis!\n"))

  (define step-limit 5)

  (define solved? #f)

  (define-values 
    (src-interpreter src-cost-fn src-visitor src-length-fn src-prec-fn src-get-ops)
    (cond
      [#t ;(equal? (vector-length src-language-desc) 6)
       ;(values (vector-ref src-language-desc 0) (vector-ref src-language-desc 1)  (vector-ref src-language-desc 2) (vector-ref src-language-desc 3) (vector-ref src-language-desc 4) (vector-ref src-language-desc 5))
       (values (target-desc-interpreter src-language-desc)  
               (target-desc-cost-fn src-language-desc)
               (target-desc-visitor src-language-desc)
               (target-desc-length-fn src-language-desc)
               (target-desc-prec-fn src-language-desc)
               (target-desc-get-ops-fn src-language-desc)
               )
       ]
      [else
        (error "Unsupported src language in misaal-rewrite-ir" src-language-desc)
        ]
      )
    )


  (define-values 
    (target-interpreter target-cost-fn target-visitor target-length-fn target-prec-fn target-get-ops)
    (cond
      [#t ;(equal? (vector-length target-language-desc) 6)
       ;(values (vector-ref target-language-desc 0) (vector-ref target-language-desc 1)  (vector-ref target-language-desc 2) (vector-ref target-language-desc 3) (vector-ref target-language-desc 4) (vector-ref target-language-desc 5))

       (values (target-desc-interpreter target-language-desc)  
               (target-desc-cost-fn target-language-desc)
               (target-desc-visitor target-language-desc)
               (target-desc-length-fn target-language-desc)
               (target-desc-prec-fn target-language-desc)
               (target-desc-get-ops-fn target-language-desc)
               )
       ]
      [else
        (error "Unsupported target language in misaal-rewrite-ir" target-language-desc)
        ]
      )
    )


  (define spec-expr-output-size (src-length-fn spec-expr (vector)))
  (define spec-expr-output-prec (src-prec-fn spec-expr (vector)))
  (define expr-VF (/ spec-expr-output-size spec-expr-output-prec))


  (define leaves-sizes input-sizes)
  (define cost-bound 30)


  (define (invoke-spec-lane lane-idx env-lane)
    (debug-log (format "Invoked spec lane with src language ~a, env ~a and lane-idx ~a\n" src-language-desc env-lane lane-idx))
    (define spec-result (src-interpreter spec-expr env-lane))
    (define low (* spec-expr-output-prec lane-idx))
    (define high (+ low (- spec-expr-output-prec 1)))

    (define spec-result-slice (extract high low spec-result))
    (debug-log (format "Src Language Spec produced: ~a\n" spec-result-slice))
    spec-result-slice
    )


  (define (invoke-spec env-lane)
    (debug-log (format "Invoked spec full with src language ~a, env ~a \n" src-language-desc env-lane))
    (define spec-result (src-interpreter spec-expr env-lane))
    (debug-log (format "Src Language Spec produced: ~a\n" spec-result))
    spec-result
    )


  (define sol '())

  ;; Set timeout for overall time spent trying the synthesize any one query
  (set-start-time-global-timeout)
  (set-global-timeout #t)


  (define start-time (current-seconds))
  (define solutions 
    ;; Traversal order first searchs the breadth of grammars
    ;; at the depth d before incrementing d.
    (for/list ([d (range starting-depth depth-limit)])
              (debug-log (format "=====================\nSTARTING SYNTHESIS FOR DEPTH ~a\n=====================\n" d))
              (define steps-per-depth
                (cond
                  [(<= d 2) 2]
                  [(equal? d 4) 
                    step-limit
                   ]
                  [else
                    step-limit
                    ]
                  )

                )

              (define NUM_THREADS 
                (cond 
                  [(<= d 2) 1]
                  [else
                    2
                    ]
                  )
                )

              (for/list ([s (range 0 steps-per-depth NUM_THREADS)])
                        (cond 
                          [solved? 
                            ;; Already solved, no need to launch parallel threads
                            ;; avoid overheads
                            '()
                            ]
                          [else
                            (define step-low s)
                            (define step-high (min (+ step-low NUM_THREADS) steps-per-depth))

                            ;; If even one of the threads finds a valid solution,
                            ;; we can kill all other threads. Use THREADS-REF variable
                            ;; to 'hack' circular definition.
                            (define THREADS-REF '())
                            (define (kill-other-threads exclude-idx)
                              (debug-log (format "Killing all other threads except ~a!, num threads currently executing: ~a\n" exclude-idx (length THREADS-REF)))
                              (for/list ([t-idx (range (length THREADS-REF))])
                                        (define actual-thread-idx (+ step-low t-idx))
                                        (cond
                                          [(equal? actual-thread-idx exclude-idx)
                                           '()
                                           ]
                                          [else
                                            (debug-log (format "Killing thread at relative index ~a\n" t-idx))
                                            (kill-thread (list-ref THREADS-REF t-idx))
                                            ]
                                          )
                                        )
                              )

                            (define thds  
                              (for/list ([t (range step-low step-high )])
                                        ;; Reset context for next synthesis
                                        (set-optimize-bound-found #f)
                                        (parameterize 
                                          ([current-solver (if (equal? solver 'z3) (z3) (boolector))] 
                                           [current-bitwidth 16]
                                           )

                                          ;; Removing Threading
                                          (thread 
                                            (thunk
                                                    (clear-vc!)
                                                    (clear-terms!)
                                                    (collect-garbage)

                                                    ;; if solution already found in previous
                                                    ;; iteration, do nothing.
                                                    (cond
                                                      [(not solved?)
                                                       (define base_name (string-append "base_" (~s (random 10000)) "_s" (~s t) "_d" (~s d)))

                                                       ;; get-grammar step-i, depth d
                                                       ;; get-interpreter step-i, depth d
                                                       ;; get-cost-model step-i, depth d
                                                       (define-values (grammar interpreter cost-model) 
                                                                      (cond
                                                                        [(equal? target-symbol 'halide)
                                                                                (debug-log "Target is Halide IR")
                                                                                (debug-log target-symbol)
                                                                                (define-values (inter-grammar inter-interpreter inter-cost-model)
                                                                                               (get-expr-grammar-step-hydride spec-expr base_name src-get-ops src-visitor src-length-fn src-prec-fn input-precs input-sizes (list) expr-VF t d scale-factor))
                                                                                (values inter-grammar target-interpreter target-cost-fn )
                                                                                ]
                                                                        [else
                                                                          (debug-log "Running custom grammar importer")
                                                                          (get-expr-grammar-step-misaal spec-expr base_name src-get-ops src-visitor src-length-fn src-prec-fn input-precs input-sizes (list) expr-VF t d scale-factor target-language-desc)
                                                                          ]
                                                                        )
                                                                      )

                                                       (define (grammar-fn i)
                                                         (grammar i)
                                                         )
                                                       (debug-log (format "Specification: ~a\n" spec-expr ))

                                                       ;; perform synthesis
                                                       (define-values (sat? mat el) 
                                                                      (synthesize-sol-with-depth 
                                                                        d 
                                                                        d invoke-spec invoke-spec-lane grammar-fn leaves-sizes 
                                                                        optimize? interpreter cost-model  symbolic? cost-bound solver) 
                                                                      )
                                                       ;; if sat set solution? to be true
                                                       (if sat?
                                                         (begin
                                                           (set! solved? #t)
                                                           (set! sol mat)
                                                           ;(kill-other-threads t)
                                                           )
                                                         '()
                                                         )
                                                       ]
                                                      )
                                                    ) ;(thunk
                                                  ) ; (thread 
                                          ) ;; paramterize 
                                        ) ;; threads list
                              ) ;; thds

                            (set! THREADS-REF thds)

                            (debug-log (format "Waiting on parallel threads range ~a to ~a for synthesis depth ~a \n" step-low step-high d))
                            (for/list ([thd thds])
                                      (thread-wait thd)
                                      )
                            ]
                          )
                        ) 
              )
    )


  (define end-time (current-seconds))

  ;; Reset context for next synthesis
  (set-optimize-bound-found #f)
  (set-global-timeout #f)

  (debug-log "Stepwise synthesis completed!")


  (if (not solved?)
    (begin
      (debug-log "Synthesis failed!")
      (values #f sol (- end-time start-time))
      )
    (values solved? sol (- end-time start-time))
    )
  )
