#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require rosette/lib/destruct)
(require hydride)
(require misaal)


(provide  (all-defined-out))

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

(define (repair-sat-add v1 v2 prec size)
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

(define (repair-reduce-add red-factor v1  prec size)
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

(define (repair-bvor v1 v2 prec size)
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

(define (repair-bvand v1 v2 prec size)
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

(define (repair-bvmod v1 v2 prec size)
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


(define (repair-max v1 v2 prec size)
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

(define (repair-min v1 v2 prec size)
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
(define (repair-sat-sub v1 v2 prec size)
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

(define (repair-mul v1 v2 prec size)
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


(define (repair-sext v1 input-prec output-prec size)
  (define result
    (apply concat
           (for/list ([i (reverse (range 0 size input-prec))])
                     (define low i)
                     (define high (+ low (- input-prec 1)))
                     (define v1.i (extract high low v1))
                     (define v1.i.sext (sign-extend v1.i (bitvector output-prec)))
                     v1.i.sext
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
