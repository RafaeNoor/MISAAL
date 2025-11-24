#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)
(require "./types.rkt")
(require "./utils.rkt")



(provide (all-defined-out))


(define (copy-vector vec)
  (define num-elems (vector-length vec))

  (define (index-fn i)
    (vector-ref vec i)
    )

  (build-vector num-elems index-fn)
  
  )


;; Create a new bitvector by extracting relavent slices 
(define (set-bit src bit-index value src-bitwidth)
  (cond
    [(equal? bit-index 0)
      (define high-slice (extract (- src-bitwidth 1) (+ 1 bit-index) src))
      (concat high-slice value )
     
     ]
    [(equal? bit-index (- src-bitwidth 1))
      (define low-slice (extract (- bit-index 1) 0 src))
      (concat  value low-slice)
     ]
    [else
      (define low-slice (extract (- bit-index 1)  0 src))
      (define high-slice (extract (- src-bitwidth 1) (+ 1 bit-index) src))
      (concat high-slice value low-slice)
      ]
    )
  
  )


(define (micro:interpret-index stmt env index row-size)
  (define-values (inputs registers sense-amp output)
                 (values 
                   (STATE-inputs env)
                   (STATE-registers env)
                   (STATE-SA env)
                   (STATE-output env)
                   )
                 )
  (define (get-operand op)
    (destruct op
              [(Reg id)
               ;; Registers are explicitly 1 bit
                (vector-ref registers id)
               ]
              [(SA) 
               sense-amp
               ]
              [_ (error "Unrecognized operand")]
              )
    )

  (define (set-dst dst value)
    (destruct dst 
              [(Reg id)
               ;(vector-set! registers id value)
               ;(STATE inputs registers sense-amp output)

               ; alt
               (define registers-copy (copy-vector registers))
               (vector-set! registers-copy id value)
               (STATE inputs registers-copy sense-amp output)
               ]
              [(SA)
               (STATE inputs registers value output)
               ]
              [_ (error "Unrecognized destination register")]
              )
    )
  (destruct stmt
            [(ReadSA idx)
             (define input-value (vector-ref inputs idx))
             (define input-bit (bit index input-value))
             (STATE inputs registers input-bit output)
             ]

            [(AND dst opA opB)
             (define opA-Value (get-operand opA))
             (define opB-Value (get-operand opB))
             (define result (bvand opA-Value opB-Value))
             (set-dst dst result)
             ]

            [(NOP)
             env
             ]

            [(XOR dst opA opB)
             (define opA-Value (get-operand opA))
             (define opB-Value (get-operand opB))
             (define result (bvxor opA-Value opB-Value))
             (set-dst dst result)
             ]

            [(XNOR dst opA opB)
             (define opA-Value (get-operand opA))
             (define opB-Value (get-operand opB))
             (define result (bvnot (bvxor opA-Value opB-Value)))
             (set-dst dst result)
             ]

            [(OR dst opA opB)
             (define opA-Value (get-operand opA))
             (define opB-Value (get-operand opB))
             (define result (bvor opA-Value opB-Value))
             (set-dst dst result)
             ]

            [(NOR dst opA opB)
             (define opA-Value (get-operand opA))
             (define opB-Value (get-operand opB))
             (define result (bvnot (bvor opA-Value opB-Value)))
             (set-dst dst result)
             ]

            [(NAND dst opA opB)
             (define opA-Value (get-operand opA))
             (define opB-Value (get-operand opB))
             (define result (bvnot (bvand opA-Value opB-Value)))
             (set-dst dst result)
             ]

            [(NOT dst opA )
             (define opA-Value (get-operand opA))
             (define result (bvnot opA-Value))
             (set-dst dst result)
             ]

            [(WriteOut src )
             (define opA-Value (get-operand src))
             (define updated-output-value (set-bit output index opA-Value row-size))
             (STATE inputs registers sense-amp updated-output-value)
             ]

            [(SEL dst pred opA opB)
             (define pred-Value (get-operand pred))
             (define opA-Value (get-operand opA))
             (define opB-Value (get-operand opB))
             ;(define result
             ;  (apply
             ;    concat
             ;    (for/list ([i (range row-size)])
             ;              (define mask (bit i pred-Value))
             ;              (if
             ;                (bvzero? mask)
             ;                ; If bit is 0 then select opB-value bit i
             ;                (bit i opB-Value)
             ;                (bit i opA-Value)
             ;                )
             ;              )
             ;    )
             ;  )
             (define result
               (if
                 (bvzero? pred-Value)
                 opB-Value
                 opA-Value
                 )
               
               )

             (set-dst dst result)
             ]
            )
  )


(define (micro:interpret stmts env bvsize)
  (define current-state env)

  (for/list ([i (range bvsize)])
            (for/list ([stmt stmts])
                      (define result-state (micro:interpret-index stmt current-state i bvsize))
                      (set! current-state result-state)
                      )

            ;(printf "Iteration ~a\n" i)
            ;(print-state current-state)
            )
  current-state
  )
