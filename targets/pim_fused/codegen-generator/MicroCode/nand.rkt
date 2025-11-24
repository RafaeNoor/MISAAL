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


(define num-registers 4)



(define bitwidth 2)


(define num-inputs 2)


(define program
  (program-hole 
    'nand-only  ; target micro-op set possible choices {'nand-only , 'drisa-nor , 'drisa-mixed, 'ap , 'flex  }
    num-registers  ; Number of bit registers
    num-inputs ; Number of inputs
    12 ; Output program length
    )
  )

(define (spec-fn env)
  (bvadd (vector-ref env 0) (vector-ref env 1) )
  )

(define-values (satisfiable? synth-sol)
               (concrete-iterative-synthesis program micro:interpret num-registers num-inputs bitwidth spec-fn)
               )

