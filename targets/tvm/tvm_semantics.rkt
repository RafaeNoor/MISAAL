#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)
(require hydride)

(define (typed:vec-add v1 v2 iprec isize sign)
  (define dst
    (apply 
      concat
           (for/list ([%iter (reverse (range 0 isize iprec))])
                     (define %lastidx1 (- iprec 1))
                     (define %high (+ %lastidx1 %iter))
                     (define slice_v1 (extract %high %iter v1))
                     (define %lastidx2 (- iprec 1))
                     (define %high2 (+ %lastidx2 %iter))
                     (define slice_v2 (extract %high2 %iter v2))
                     (define %result (bvaddnw slice_v1 slice_v2 sign))
                     %result
                     )
           )
    )
  dst
  )

(define (typed:vec-sub v1 v2 iprec isize sign)
  (define dst
    (apply 
      concat
           (for/list ([%iter (reverse (range 0 isize iprec))])
                     (define %lastidx1 (- iprec 1))
                     (define %high (+ %lastidx1 %iter))
                     (define slice_v1 (extract %high %iter v1))
                     (define %lastidx2 (- iprec 1))
                     (define %high2 (+ %lastidx2 %iter))
                     (define slice_v2 (extract %high2 %iter v2))
                     (define %result (bvsubnw slice_v1 slice_v2 sign))
                     %result
                     )
           )
    )
  dst
  )

(define (typed:vec-mul v1 v2 iprec widenprec isize sign)
  (define dst
    (apply 
      concat
           (for/list ([%iter (reverse (range 0 isize iprec))])
                     (define %lastidx1 (- iprec 1))
                     (define %high (+ %lastidx1 %iter))
                     (define slice_v1 (extract %high %iter v1))
                     (define %widen_slice_v1 (bvsizeext slice_v1 widenprec sign))
                     (define %lastidx2 (- iprec 1))
                     (define %high2 (+ %lastidx2 %iter))
                     (define slice_v2 (extract %high2 %iter v2))
                     (define %widen_slice_v2 (bvsizeext slice_v2 widenprec sign))
                     (define prod (bvmul %widen_slice_v1 %widen_slice_v1))
                     (define %narrow (extract %lastidx1 0 prod))
                     %narrow
                     )
           )
    )
  dst
  )