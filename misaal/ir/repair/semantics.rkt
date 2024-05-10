;#============================== Hydride File =================================
;#
;# Part of the Hydride Compiler Infrastructure.
;# <Placeholder for license information>
;#
;#=============================================================================
;#
;# Do NOT modify this file. It is automatically generated.
;#
;#=============================================================================

#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)
(require rosette/solver/smt/boolector)

(require hydride/utils/bvops)
(require hydride/utils/misc)


(provide (all-defined-out))
;; ================================================================================
;;                                DSL Semantics
;; ================================================================================

(define (repair-add v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvadd v1.i v2.i)


                     )
           )
    )
  result
  )


(define (repair-sshr v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvashr v1.i v2.i)
                     )
           )
    )
  result
  )

(define (repair-ushr v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvlshr v1.i v2.i)
                     )
           )
    )
  result
  )


(define (repair-sabsd v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (define max.i (bvsmax v1.i v2.i))
                     (define min.i (bvsmin v1.i v2.i))
                     (bvsub max.i min.i)
                     )
           )
    )
  result
  )

(define (repair-uabsd v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (define max.i (bvumax v1.i v2.i))
                     (define min.i (bvumin v1.i v2.i))
                     (bvsub max.i min.i)
                     )
           )
    )
  result
  )


(define (repair-ssat-add v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvaddnsw v1.i v2.i prec)


                     )
           )
    )
  result
  )


(define (repair-usat-add v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvaddnuw v1.i v2.i prec)
                     )
           )
    )
  result
  )

(define (repair-vector-reduce-add red-factor v1  prec size)
  (define result
    (apply concat
           (for/list ([outer.i (reverse (range 0 size (* prec red-factor)))])
                     (apply bvadd
                            (for/list ([inner.i (range 0 red-factor)])
                                      (define low.inner.i (* inner.i prec))
                                      (define low.outer.i (+ low.inner.i outer.i))
                                      (define high.outer.i (+ low.outer.i (- prec 1)))
                                      (extract high.outer.i low.outer.i v1)
                                      )
                            )
                     )
           )
    )
  result
  )



(define (repair-sdiv v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvsdiv v1.i v2.i)
                     )
           )
    )
  result
  )


(define (repair-shl v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvshl v1.i v2.i)
                     )
           )
    )
  result
  )

(define (repair-udiv v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvsdiv v1.i v2.i)
                     )
           )
    )
  result
  )

(define (repair-bwor v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvor v1.i v2.i)
                     )
           )
    )
  result
  )

(define (repair-bwand v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvand v1.i v2.i)
                     )
           )
    )
  result
  )

(define (repair-bwnot v1  prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (bvnot v1.i)
                     )
           )
    )
  result
  )

(define (repair-smod v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvsmod v1.i v2.i)
                     )
           )
    )
  result
  )

(define (repair-umod v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvurem v1.i v2.i)
                     )
           )
    )
  result
  )


(define (repair-smax v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvsmax v1.i v2.i)
                     )
           )
    )
  result
  )

(define (repair-umax v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvumax v1.i v2.i)
                     )
           )
    )
  result
  )

(define (repair-smin v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvsmin v1.i v2.i)
                     )
           )
    )
  result
  )

(define (repair-umin v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvsmin v1.i v2.i)
                     )
           )
    )
  result
  )


(define (repair-sub v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvsub v1.i v2.i)
                     )
           )
    )
  result
  )
(define (repair-ssat-sub v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvsubnsw v1.i v2.i prec)
                     )
           )
    )
  result
  )

(define (repair-usat-sub v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (bvsubnuw v1.i v2.i prec)
                     )
           )
    )
  result
  )

(define (repair-smul v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (define v1.i.sext (sign-extend v1.i (bitvector (* 2 prec))))
                     (define v2.i.sext (sign-extend v2.i (bitvector (* 2 prec))))
                     (define product (bvmul v1.i.sext v2.i.sext))
                     (extract (- prec 1) 0 product)
                     )
           )
    )
  result
  )

(define (repair-umul v1 v2 prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size prec))])
                     (define low i)
                     (define high (+ low (- prec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (define v1.i.zext (zero-extend v1.i (bitvector (* 2 prec))))
                     (define v2.i.zext (zero-extend v2.i (bitvector (* 2 prec))))
                     (define product (bvmul v1.i.zext v2.i.zext))
                     (extract (- prec 1) 0 product)
                     )
           )
    )
  result
  )


(define (repair-cast-int v1 input-prec output-prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size input-prec))])
                     (define low i)
                     (define high (+ low (- input-prec 1)))
                     (define v1.i (extract high low v1))
                     (cond 
                       [(> output-prec input-prec)
                        (define v1.i.sext (sign-extend v1.i (bitvector output-prec)))
                        v1.i.sext

                        ]
                       [else
                         (extract (- output-prec 1) 0 v1.i)
                        ]
                       )
                     )
           )
    )
  result
  )




(define (repair-cast-uint v1 input-prec output-prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size input-prec))])
                     (define low i)
                     (define high (+ low (- input-prec 1)))
                     (define v1.i (extract high low v1))
                     (cond 
                       [(> output-prec input-prec)
                        (define v1.i.zext (zero-extend v1.i (bitvector output-prec)))
                        v1.i.zext

                        ]
                       [else
                         (extract (- output-prec 1) 0 v1.i)
                        ]
                       )
                     )
           )
    )
  result
  )

(define (repair-saturate v1 input-prec output-prec size signed?)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size input-prec))])
                     (define low i)
                     (define high (+ low (- input-prec 1)))
                     (define v1.i (extract high low v1))
                     (cond 
                       [signed? 
                         (bvssat v1.i input-prec output-prec)
                         ]
                       [else
                         (bvusat v1.i input-prec output-prec)
                        ]
                       )
                     )
           )
    )
  result
  )


(define (repair-widen-mul v1 v2 iprec oprec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size iprec))])
                     (define low i)
                     (define high (+ low (- iprec 1)))
                     (define v1.i (extract high low v1))
                     (define v2.i (extract high low v2))
                     (define v1.i.sext (sign-extend v1.i (bitvector oprec)))
                     (define v2.i.sext (sign-extend v2.i (bitvector oprec)))
                     (define product (bvmul v1.i.sext v2.i.sext))
                     product
                     )
           )
    )
  result
  )

(define (repair-extract-index v1 prec size index)
  (define max-index (- (/ size prec) 1))
  (define adjusted-index (- max-index index))
  (define low (* adjusted-index prec))
  (define high (+ (- prec 1) low))
  (extract high low v1)
  )

(define (repair-build-vector num-elements indices env)
  (define result
    (apply concat
           (for/list ([i (reverse indices)])
                     (vector-ref env i)
                     )
           )
    )
  result
  )
;; ================================================================================

