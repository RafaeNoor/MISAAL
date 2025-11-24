#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)



(provide (all-defined-out))


;; MICRO-OP Description
;; Read operands into Sense Amplifer. 
(struct ReadSA (id) #:transparent )

;; Write result of register / SA to output
(struct WriteOut (src) #:transparent )

;; Registers are 1 bit registers
(struct Reg (reg-id) #:transparent #:mutable)

(struct SA () #:transparent )

;; NO OP
(struct NOP () #:transparent )

;; Logical Operations, must explicitly 
;; provide destination address / register
(struct AND (dst opA opB) #:transparent )
(struct XOR (dst opA opB) #:transparent )
(struct OR (dst opA opB) #:transparent )
(struct NOR (dst opA opB) #:transparent )
(struct XNOR (dst opA opB) #:transparent )
(struct NAND (dst opA opB) #:transparent )
(struct SEL (dst PRED opA opB) #:transparent )
(struct NOT (dst opA) #:transparent )

(struct STATE 
        (inputs registers SA output) #:transparent )




