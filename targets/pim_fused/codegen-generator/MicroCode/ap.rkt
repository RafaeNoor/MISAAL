#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)
(require "./types.rkt")
(require "./utils.rkt")
(require "./interpreter.rkt")

(custodian-limit-memory (current-custodian) (* 10000 1024 1024))
(current-bitwidth 16)


(define num-registers 2)



(define bitwidth 2)


(define num-inputs 3)


(define program
  (program-hole 
    'ap  ; target micro-op set possible choices {'nand-only , 'drisa-nor , 'drisa-mixed, 'ap , 'flex  }
    num-registers  ; Number of bit registers
    num-inputs ; Number of inputs
    8 ; Output program length
    )
  )

(define (spec-fn env)
  (bvadd (bvadd (vector-ref env 0) (vector-ref env 1) ) (vector-ref env 2))
  )

(define-values (satisfiable? synth-sol)
               (concrete-iterative-synthesis program micro:interpret num-registers num-inputs bitwidth spec-fn)
               )

