#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)
(require "./types.rkt")
(require "./cost.rkt")

(provide (all-defined-out))

(define (print-state env)
  (define-values (inputs registers sense-amp output)
                 (values 
                   (STATE-inputs env)
                   (STATE-registers env)
                   (STATE-SA env)
                   (STATE-output env)
                   )
                 )

  (printf "====================\n")
  (printf "Inputs:\n")
  (printf "~a\n" inputs)

  (printf "Registers:\n")
  (printf "~a\n" registers)

  (printf "Sense Amplifer:\n")
  (printf "~a\n" sense-amp)

  (printf "Output:\n")
  (printf "~a\n" output)

  (printf "====================\n")

  )
; a is input 0
; b is input 1
; CR is register 0
; PR is register 1

(define A 0)
(define B 1)
(define CR (Reg 0))
(define PR (Reg 1))



(define (full-inst* num-registers num-inputs)

  (define operand-list
    (append
      (list (SA))
      (for/list ([i (range num-registers)])  (Reg i))
      )
    
    )
  (define (operand) 
    (apply choose* 
           operand-list
      )
    )

  (define (read-inputs)  (apply choose* (for/list ([i (range num-inputs)]) (ReadSA i))))



  (define stmt
    (choose* 
      (read-inputs)
      (AND (operand) (operand) (operand))
      (XOR (operand) (operand) (operand))
      (XNOR (operand) (operand) (operand))
      (OR (operand) (operand) (operand))
      (NOR (operand) (operand) (operand))
      (NOT (operand) (operand))
      (NAND (operand) (operand) (operand))
      (SEL (operand) (operand) (operand) (operand))
      (WriteOut (SA))
      )
    )
  stmt


  )


(define (nand-only-inst* num-registers num-inputs)

  (define operand-list
    (append
      (list (SA))
      (for/list ([i (range num-registers)])  (Reg i))
      )
    
    )
  (define (operand) 
    (apply choose* 
           operand-list
      )
    )

  (define (read-inputs)  (apply choose* (for/list ([i (range num-inputs)]) (ReadSA i))))



  (define stmt
    (choose* 
      (read-inputs)
      (NAND (operand) (operand) (operand))
      (NOP)
      (WriteOut (SA))
      )
    )
  stmt


  )

;(and/or/nor)
(define (drisa-nor-inst* num-registers num-inputs)


  (define operand-list
    (append
      (list (SA))
      (for/list ([i (range num-registers)])  (Reg i))
      )
    
    )
  (define (operand) 
    (apply choose* 
           operand-list
      )
    )

  (define (read-inputs)  (apply choose* (for/list ([i (range num-inputs)]) (ReadSA i))))



  (define stmt
    (choose* 
      (read-inputs)
      (AND (operand) (operand) (operand))
      (OR (operand) (operand) (operand))
      (NOR (operand) (operand) (operand))
      (WriteOut (SA))
      (NOP)
      )
    )
  stmt


  )


; (and/or/not/nand/nor/xnor)
(define (drisa-mixed-inst* num-registers num-inputs)

  (define operand-list
    (append
      (list (SA))
      (for/list ([i (range num-registers)])  (Reg i))
      )
    
    )
  (define (operand) 
    (apply choose* 
           operand-list
      )
    )

  (define (read-inputs)  (apply choose* (for/list ([i (range num-inputs)]) (ReadSA i))))



  (define stmt
    (choose* 
      (read-inputs)
      (AND (operand) (operand) (operand))
      (OR (operand) (operand) (operand))
      (NOR (operand) (operand) (operand))
      (XNOR (operand) (operand) (operand))
      (NAND (operand) (operand) (operand))
      (NOT (operand) (operand))
      (WriteOut (SA))
      )
    )
  stmt


  )



;(and/xnor/sel)
(define (ap-inst* num-registers num-inputs)
  (define operand-list
    (append
      (list (SA))
      (for/list ([i (range num-registers)])  (Reg i))
      )
    
    )
  (define (operand) 
    (apply choose* 
           operand-list
      )
    )

  (define (read-inputs)  (apply choose* (for/list ([i (range num-inputs)]) (ReadSA i))))

  (define stmt
    (choose* 
      ;(ReadSA A)
      ;(ReadSA B)
      (read-inputs)
      (AND (operand) (operand) (operand))
      (XNOR (operand) (operand) (operand))
      (SEL (operand) (operand) (operand) (operand))
      (WriteOut (SA))
      (NOP)
      )
    )
  stmt
  )



; (not/and/or/xor/sel):
(define (flex-inst* num-registers num-inputs)

  (define operand-list
    (append
      (list (SA))
      (for/list ([i (range num-registers)])  (Reg i))
      )
    
    )
  (define (operand) 
    (apply choose* 
           operand-list
      )
    )

  (define (read-inputs)  (apply choose* (for/list ([i (range num-inputs)]) (ReadSA i))))



  (define stmt
    (choose* 
      (read-inputs)
      (AND (operand) (operand) (operand))
      (XOR (operand) (operand) (operand))
      (OR (operand) (operand) (operand))
      (NOT (operand) (operand))
      (SEL (operand) (operand) (operand) (operand))
      (WriteOut (SA))
      )
    )
  stmt
  )


(define (program-hole target num-registers num-inputs len)
  (define grammar-select 
    (cond
      [(equal? target 'full)
       full-inst*
       ]

      [(equal? target 'nand-only)
       nand-only-inst*
       ]

      [(equal? target 'drisa-nor)
       drisa-nor-inst*
       ]

      [(equal? target 'drisa-mixed)
       drisa-mixed-inst*
       ]

      [(equal? target 'ap)
       ap-inst*
       ]

      [(equal? target 'flex)
       flex-inst*
       ]
      [else
        (error "Unrecognized target in grammar")
        ]
      )
    )

  (for/list ([i (range len)]) (grammar-select num-registers num-inputs))
  )


(define (create-state inputs num-registers bitwidth)
  (define (get-zero i) (bv 0 1))
  (STATE 
    ;; Inputs
    inputs
    ;; Registers
    (build-vector num-registers get-zero)
    ;; Sense AMP
    (bv 0 1)

    ;; Ouput
    (bv 0 bitwidth)
    )
  )





(define (concrete-micro-op-synth grammar interpret-fn num-registers num-inputs bitwidth spec-fn cexs)
  (clear-vc!)

  (define optimize? #t)

  (define model 
    (cond
      [optimize?
        (optimize
          #:minimize (list (dram-cost grammar))
          #:guarantee 
          (begin
            (for/list ([cex cexs])
                      (assert 
                        (equal?
                          (spec-fn cex)
                          (STATE-output (interpret-fn grammar (create-state cex num-registers bitwidth) bitwidth))
                          )
                        )
                      )
            )

          )
        
        
        ]
      [else
        (synthesize
          #:forall (list )
          #:guarantee 
          (begin
            (for/list ([cex cexs])
                      (assert 
                        (equal?
                          (spec-fn cex)
                          (STATE-output (interpret-fn grammar (create-state cex num-registers bitwidth) bitwidth))
                          )
                        )
                      )
            )

          )

        ]
      
      
      
      
      )
    
    )



  (cond
    [(unsat? model)
     (values #f  '())
     ]
    [else
      (values #t (evaluate grammar model))
      ]

    )


  )

(define (verify-micro-op-synth prog interpreter-fn num-registers num-inputs bitwidth spec-fn)
  (clear-vc!)

  (define (get-sym i) 
    (define-symbolic* val (bitvector bitwidth))
    val
    )
  (define symbolic-env (build-vector num-inputs get-sym))
  (define cex
    (verify 
      (assert 
        (equal?
          (spec-fn symbolic-env)
          (STATE-output (interpreter-fn prog (create-state symbolic-env num-registers bitwidth) bitwidth))
          )
        )

      )
    )

  (cond
    [(unsat? cex)
     ;; Proven equivalent
     (values #t '())
     ]
    [else
      (define new-cex (evaluate symbolic-env cex))
      (values #f new-cex)
      ]
    
    
    )


  )



(define (concrete-iterative-synthesis-helper grammar interpreter-fn num-registers num-inputs bitwidth spec-fn cex-ls)

  (define cexs
    (cond
      [(equal? cex-ls '())
       (define (get-zero i) (bv 0 bitwidth))
       (define (get-one i) (bv 1 bitwidth))
       (list (build-vector num-inputs get-zero) (build-vector num-inputs get-one) )
       ]
      [else
        cex-ls
        ]
      )
    )

  (printf "Counter examples: ~a\n" cexs)

  (define-values (sat? prog)
                 (concrete-micro-op-synth grammar interpreter-fn num-registers num-inputs bitwidth spec-fn cexs)
                 )

  (cond 

    [sat? 

      (displayln "Concrete synthesis found possible program:")
      (pretty-print prog)

      ;; Verify correctness
      (define-values (verified? verify-cex) (verify-micro-op-synth prog interpreter-fn num-registers num-inputs bitwidth spec-fn))

      (cond
        [verified? 
          ;; Found solution returning!
          (displayln "Verification passed!")
          (values verified? prog)

          ]
        [else
          ; Next iteration of synthesis
          (concrete-iterative-synthesis-helper grammar interpreter-fn num-registers num-inputs bitwidth spec-fn (append cexs (list verify-cex)))
          ]
        )
      ]
    [else
      ;; Unable to synthesize -> exit
      (displayln "Unsatisfiable")
      (values #f '())
      ]
    )


  )


(define (concrete-iterative-synthesis grammar interpreter-fn num-registers num-inputs bitwidth spec-fn)
  (displayln "Concrete Iterative Synthesis ")

  (define-values (sat? program) 
                (concrete-iterative-synthesis-helper grammar interpreter-fn num-registers num-inputs bitwidth spec-fn '())
                 
                 )
  
  (values sat? program)
  
  
  
  )
