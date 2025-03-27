#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)
(require hydride)

; Missing [vec-mod, vec-gt, vec-ge, vec-eq, vec-bwor] semantics in this file but shouldn't matter


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

(define (typed:vec-div v1 v2 iprec isize sign)
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
                     (define %result (bvdiv slice_v1 slice_v2 sign))
                     %result
                     )
           )
    )
  dst
  )

(define (typed:vec-min v1 v2 iprec isize sign)
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
                     (define min-v1-v2 (bvmin slice_v1 slice_v2 sign))
                     min-v1-v2
                     )
           )
    )
  dst
  )

(define (typed:vec-max v1 v2 iprec isize sign)
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
                     (define max-v1-v2 (bvmax slice_v1 slice_v2 sign))
                     max-v1-v2
                     )
           )
    )
  dst
  )

(define (typed:vec-lt v1 v2 iprec isize sign)
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
                     (define result (bvlt slice_v1 slice_v2 sign))
                     result
                     )
           )
    )
  dst
  )

(define (typed:vec-le v1 v2 iprec isize sign)
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
                     (define result (bvle slice_v1 slice_v2 sign))
                     result
                     )
           )
    )
  dst
  )

  (define (typed:vec-bwand v1 v2 iprec isize)
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
                      (define %result (bvand slice_v1 slice_v2))
                      %result
                      )
            )
    )
  dst
  )