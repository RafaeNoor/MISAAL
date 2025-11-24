#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)
(require "./types.rkt")

(provide (all-defined-out))


(define (inst-cost program)
  (define 
    stmt-costs 
    (for/list 
      ([stmt program])

      (destruct stmt
                [(NOP) 0]
                [_ 1]
                )
      
      )
    )
  (apply + stmt-costs)
  
  )

(define (get-stmt-registers stmt) 
  (define (is-reg a)
    (destruct a
              [(Reg id) #t]
              [_ #f]
              )
    )
  (destruct stmt
            [(AND dst opA opB)
             (filter is-reg (list dst opA opB))
             ]

            [(NOP)
             (list)
             ]

            [(XOR dst opA opB)
             (filter is-reg (list dst opA opB))
             ]

            [(XNOR dst opA opB)
             (filter is-reg (list dst opA opB))
             ]

            [(OR dst opA opB)
             (filter is-reg (list dst opA opB))
             ]

            [(NOR dst opA opB)
             (filter is-reg (list dst opA opB))
             ]

            [(NAND dst opA opB)
             (filter is-reg (list dst opA opB))
             ]

            [(NOT dst opA )
             (filter is-reg (list dst opA))
             ]

            [(WriteOut src )
             (list)
             ]

            [(SEL dst pred opA opB)
             (filter is-reg (list dst pred opA opB))
             ]
            [_ (list)]
            )
  )

(define (get-stmt-dst-registers stmt) 
  (destruct stmt
            [(AND dst opA opB)
             (destruct dst
                       [(Reg id) id]
                       [else 0]
                       )
             ]

            [(NOP)
             0



             ]

            [(XOR dst opA opB)

             (destruct dst
                       [(Reg id) id]
                       [else 0]
                       )
             ]

            [(XNOR dst opA opB)
             (destruct dst
                       [(Reg id) id]
                       [else 0]
                       )
             ]

            [(OR dst opA opB)
             (destruct dst
                       [(Reg id) id]
                       [else 0]
                       )
             ]

            [(NOR dst opA opB)

             (destruct dst
                       [(Reg id) id]
                       [else 0]
                       )
             ]

            [(NAND dst opA opB)

             (destruct dst
                       [(Reg id) id]
                       [else 0]
                       )
             ]

            [(NOT dst opA )
             (destruct dst
                       [(Reg id) id]
                       [else 0]
                       )
             ]

            [(WriteOut src )
             0

             ]

            [(SEL dst pred opA opB)
             (destruct dst
                       [(Reg id) id]
                       [else 0]
                       )
             ]
            [_ 0]
            )
  )


;; Cost for minimizing the number of
;; register used
(define (register-cost program)
  (define 
    stmt-costs 
    (for/list 
      ([stmt program])
      (define registers (get-stmt-dst-registers stmt))

      ;(printf "Registers: ~a\n" registers)
      (define reg-ids 
        ;(for/list ([reg registers])(Reg-reg-id reg))
        registers
        )

     reg-ids 


      )
    )
  (apply max stmt-costs)
  
  )

;; DRAM Cost is a combination of register cost and inst cost
(define (dram-cost prog)
  (+ (register-cost prog) (inst-cost prog) )
  )
