#lang rosette/safe

(require
  (only-in racket/struct make-constructor-style-printer)
  (only-in racket/base error)
  rosette/lib/destruct)

(require hydride/halide)
(require hydride/ir/hydride/definition)

(provide (all-defined-out))
         
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Define Halide's IR extended with explicit type information


;; Generalized Broadcast
(struct typed:xBroadcast (sca prec size factor) #:transparent #:mutable)
(struct typed:int-imm (data prec signed?) #:transparent #:mutable)

(struct typed:ramp (base stride len) #:transparent)

;; Generalized Cast
(struct typed:cast-int  (vec iprec  isigned? olane oprec ) #:transparent #:mutable)
(struct typed:cast-uint (vec iprec  isigned?  olane oprec) #:transparent #:mutable)

;; Shuffles
(struct typed:vec-broadcast (n vec iprec isize) #:transparent #:mutable)
(struct typed:slice_vectors (vec base stride len iprec isize) #:transparent #:mutable)
(struct typed:concat_vectors (v1 v2 iprec isize) #:transparent #:mutable)

;; Generalized Saturation
(struct typed:vec-saturate  (vec  iprec isigned? olane oprec signed?) #:transparent #:mutable)


(struct typed:vec-if (v1 v2 v3 iprec isize) #:transparent #:mutable )
(struct typed:vec-eq (v1 v2 iprec isize) #:transparent #:mutable )
(struct typed:vec-clz (v1 iprec isize) #:transparent #:mutable )
(struct typed:vec-bwand (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:vec-bwnot (v1 iprec isize) #:transparent #:mutable)

(struct typed:vec-add (v1  v2 iprec isize) #:transparent #:mutable)
(struct typed:vec-sub (v1  v2 iprec isize) #:transparent #:mutable)
(struct typed:vec-shl (v1 v2 iprec isize) #:transparent #:mutable )

;; Operations are split based of signed and unsigned

(struct typed:signed-vec-absd (v1 v2 iprec isize) #:transparent #:mutable )
(struct typed:signed-vec-abs (v1 iprec isize) #:transparent #:mutable)
(struct typed:signed-vec-sat-add (v1 v2  iprec isize) #:transparent #:mutable)
(struct typed:signed-vec-sat-sub (v1 v2  iprec isize) #:transparent #:mutable )
(struct typed:signed-vec-mul (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:signed-vec-widen-mul (v1 v2 iprec isize) #:transparent #:mutable )
(struct typed:signed-vec-div (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:signed-vec-mod (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:signed-vec-max (v1 v2 iprec isize) #:transparent #:mutable )
(struct typed:signed-vec-min (v1 v2 iprec isize) #:transparent #:mutable )
(struct typed:signed-vec-lt (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:signed-vec-le (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:signed-vec-shr (v1 v2 iprec isize) #:transparent #:mutable )
(struct typed:signed-vec-rounding_mul_shift_right (v1 v2 v3 iprec isize) #:transparent #:mutable)
(struct typed:signed-vec-mul_shift_right (v1 v2 v3 iprec isize) #:transparent #:mutable )
(struct typed:signed-vec-rounding_shift_right (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:signed-vec-rounding_halving_add (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:signed-vec-halving_add (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:signed-vector_reduce (op width vec iprec isize) #:transparent #:mutable)




;; Unsigned variants


(struct typed:unsigned-vec-absd (v1 v2 iprec isize) #:transparent #:mutable )
(struct typed:unsigned-vec-sat-add (v1 v2  iprec isize) #:transparent #:mutable)
(struct typed:unsigned-vec-sat-sub (v1 v2  iprec isize) #:transparent #:mutable )
(struct typed:unsigned-vec-mul (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:unsigned-vec-widen-mul (v1 v2 iprec isize) #:transparent #:mutable )
(struct typed:unsigned-vec-div (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:unsigned-vec-mod (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:unsigned-vec-max (v1 v2 iprec isize) #:transparent #:mutable )
(struct typed:unsigned-vec-min (v1 v2 iprec isize) #:transparent #:mutable )
(struct typed:unsigned-vec-lt (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:unsigned-vec-le (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:unsigned-vec-shr (v1 v2 iprec isize) #:transparent #:mutable )
(struct typed:unsigned-vec-rounding_mul_shift_right (v1 v2 v3 iprec isize) #:transparent #:mutable)
(struct typed:unsigned-vec-mul_shift_right (v1 v2 v3 iprec isize) #:transparent #:mutable )
(struct typed:unsigned-vec-rounding_shift_right (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:unsigned-vec-rounding_halving_add (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:unsigned-vec-halving_add (v1 v2 iprec isize) #:transparent #:mutable)
(struct typed:unsigned-vector_reduce (op width vec iprec isize) #:transparent #:mutable)
