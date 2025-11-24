#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)
(require "./types.rkt")
(require "./interpreter.rkt")
(require "./cost.rkt")





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


(register-cost program)




(list
 (ReadSA 0)
 (XNOR (SA) (Reg 0) (SA))
 (SEL (Reg 0) (Reg 0) (Reg 0) (SA))
 (WriteOut (SA))
 )
