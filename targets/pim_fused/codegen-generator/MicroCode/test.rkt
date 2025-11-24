#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)
(require "./types.rkt")
(require "./interpreter.rkt")





; a is input 0
; b is input 1
; CR is register 0
; PR is register 1

(define A 0)
(define B 1)
(define CR (Reg 0))
(define PR (Reg 1))

(define program
  (list
    ; SA = mem_row_read(a)
    (ReadSA A)
    ;PR = XOR(SA, CR)
    (XOR PR (SA) CR)

    ;SA = mem_row_read(b)
    (ReadSA B)

    ;CR = SEL(PR, SA, CR)
    (SEL CR PR (SA) CR)
    ;SA = XOR(PR, SA)
    (XOR (SA) PR (SA))

    ;mem_row_write(s, SA)
    (WriteOut (SA))
    )

  )



(set! program

  (list
 (ReadSA 0)
 (NAND (Reg 0) (SA) (Reg 1))
 (NAND (SA) (Reg 0) (SA))
 (NAND (Reg 0) (Reg 0) (Reg 1))
 (NAND (Reg 0) (SA) (Reg 0))
 (ReadSA 1)
 (NAND (Reg 1) (SA) (Reg 0))
 (NAND (SA) (Reg 1) (SA))
 (NAND (Reg 0) (Reg 1) (Reg 0))
 (NAND (SA) (SA) (Reg 0))
 (WriteOut (SA))
 (NAND (Reg 1) (Reg 1) (Reg 1)))
  )

(define bitwidth 3)
(define zero (bv 0 bitwidth))

;(define a (bv 14 bitwidth))
;(define b (bv 15 bitwidth))

(define-symbolic a (bitvector bitwidth))
(define-symbolic b (bitvector bitwidth))
;(assert (bvsge a zero))
;(assert (bvsge b zero))

(define expected-result (bvadd a b))
(printf "Expected result ~a\n" expected-result)
(define (execute-micro-op-program a b)

  (define carry (bv 0 1))
  (define pr (bv 0 1))


  (define starting-state (STATE
                           (vector a b)
                           (vector carry pr)
                           (bv 0 1)
                           (bv 0 bitwidth)
                           ))


  (define result-state (micro:interpret program starting-state bitwidth))


  (println result-state)

  (define result (STATE-output result-state))

  (printf "Result of computation is ~a (~a)\n" result (bitvector->integer result))
  result
  )

(define result (execute-micro-op-program a b))


(define cex
  (verify
    (assert (equal? result expected-result))
    )
  )
(cond
  [(unsat? cex)
   (printf "Implementation is equivalent!\n")
   (exit 0)
   ]
  )
(println cex)

(define cex-a (evaluate a cex ))
(define cex-b (evaluate b cex ))

(displayln "Counter example operands")
(println cex-a)
(println cex-b)

(bitvector->integer cex-a)
(bitvector->integer cex-b)

(define cex-result (bvadd cex-a cex-b))

(displayln "Counter example expected result")
(println cex-result)
(bitvector->integer cex-result)


(define micro-result (execute-micro-op-program cex-a cex-b))

(displayln "Counter example actual result")
(println micro-result)
(bitvector->integer micro-result)
