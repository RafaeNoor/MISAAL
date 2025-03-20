#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)
(require hydride)
;['typed:cast-int-extend', 'typed:cast-int-truncate', 'typed:cast-uint-extend', 'typed:cast-uint-truncate', 'typed:concat_vectors', 'typed:signed-vec-abs', 'typed:signed-vec-absd', 'typed:signed-vec-div', 'typed:signed-vec-halving_add', 'typed:signed-vec-le', 'typed:signed-vec-lt', 'typed:signed-vec-max', 'typed:signed-vec-min', 'typed:signed-vec-mod', 'typed:signed-vec-mul', 'typed:signed-vec-rounding_halving_add', 'typed:signed-vec-rounding_mul_shift_right', 'typed:signed-vec-rounding_shift_right', 'typed:signed-vec-sat-add', 'typed:signed-vec-sat-sub', 'typed:signed-vec-shr', 'typed:signed-vec-widen-mul', 'typed:signed-vector_reduce_add', 'typed:slice_vectors', 'typed:unsigned-vec-absd', 'typed:unsigned-vec-div', 'typed:unsigned-vec-halving_add', 'typed:unsigned-vec-le', 'typed:unsigned-vec-lt', 'typed:unsigned-vec-max', 'typed:unsigned-vec-min', 'typed:unsigned-vec-mod', 'typed:unsigned-vec-mul', 'typed:unsigned-vec-rounding_halving_add', 'typed:unsigned-vec-rounding_mul_shift_right', 'typed:unsigned-vec-rounding_shift_right', 'typed:unsigned-vec-sat-add', 'typed:unsigned-vec-sat-sub', 'typed:unsigned-vec-shr', 'typed:unsigned-vec-widen-mul', 'typed:vec-add', 'typed:vec-bwand', 'typed:vec-bwnot', 'typed:vec-eq', 'typed:vec-saturate', 'typed:vec-shl', 'typed:vec-sub', 'typed:xBroadcast']




(define (typed:cast-extend vec iprec isize oprec sign)
  (define dst
    (apply 
      concat
      (for/list ([%iter (reverse (range 0 isize iprec))])
                (define %lastidx1 (- iprec 1))
                (define %high (+ %lastidx1 %iter))
                (define slice (extract %high %iter vec))
                (define %sext (bvsizeext slice oprec sign))
                %sext
                )
      )
    )
  dst
  )



(define (typed:cast-truncate vec iprec isize oprec)
  (define dst
    (apply 
      concat
           (for/list ([%iter (reverse (range 0 isize iprec))])
                     (define %lastidx1 (- iprec 1))
                     (define %high (+ %lastidx1 %iter))
                     (define slice (extract %high %iter vec))
                     (define %offset (- oprec 1))
                     (define %trunc (extract %offset 0 slice))
                     %trunc
                     )
           )
    )
  dst
  )




(define (typed-folded:vec-saturate vec iprec isize oprec sign)
  (define dst
    (apply 
      concat
           (for/list ([%iter (reverse (range 0 isize iprec))])
                     (define %lastidx1 (- iprec 1))
                     (define %high (+ %lastidx1 %iter))
                     (define slice (extract %high %iter vec))
                     (define %trunc (bvsaturate slice iprec oprec sign))
                     %trunc
                     )
           )
    )
  dst
  )





(define (typed:concat_vectors v1 v2 iprec isize)
  (define dst (concat v1 v2))
  dst
  )

(define (typed:signed-vec-abs vec iprec isize)
  (define dst
    (apply 
      concat
           (for/list ([%iter (reverse (range 0 isize iprec))])
                     (define %lastidx1 (- iprec 1))
                     (define %high (+ %lastidx1 %iter))
                     (define slice (extract %high %iter vec))
                     (define integ (bitvector->integer slice))
                     (define val (abs integ))
                     (define %updated-val (integer->bitvector val (bitvector iprec)))
                     %updated-val
                     )
           )
    )
  dst
  )

(define (typed:vec-absd v1 v2 iprec isize sign)
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
                     (define min-v1-v2 (bvmin slice_v1 slice_v2 sign))
                     (define %diff (bvsub max-v1-v2 min-v1-v2))
                     %diff
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

(define (typed-folded:vec-reduce_add reduce-factor v1 iprec isize )
  (define dst
    (apply 
      concat 
      (for/list ([%outer (reverse (range 0 isize (* iprec reduce-factor)))])
                (apply 
                  bvadd 
                  (for/list ([%iter (reverse (range 0 reduce-factor 1))])
                            (define %step (* iprec %iter))
                            (define %low-offset (+ %outer %step))
                            (define %lastidx (- iprec 1))
                            (define %high-idx (+ %low-offset %lastidx))
                            (define %slice (extract %high-idx %low-offset v1))
                            %slice
                            )
                  )
                )
      )
    )
  dst
  )

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





(define (typed:vec-halving_add v1 v2 iprec widenprec isize sign)
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
                     (define sum (bvadd %widen_slice_v1 %widen_slice_v1))
                     (define avg (bvdiv sum (bv 2 (bitvector widenprec))  bvdiv))
                     (define %narrow (extract %lastidx1 0 avg))
                     %narrow
                     )
           )
    )
  dst
  )


(define (typed:vec-rounding_halving_add v1 v2 iprec widenprec isize sign)
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
                     (define sum (bvadd %widen_slice_v1 %widen_slice_v1))
                     (define rounded_sum (bvadd sum (bv 1 (bitvector widenprec))))
                     (define avg (bvdiv rounded_sum (bv 2 (bitvector widenprec))  sign))
                     (define %narrow (extract %lastidx1 0 avg))
                     %narrow
                     )
           )
    )
  dst
  )



(define (typed-folded:vec-rounding_shift_right v1 v2 iprec widenprec isize sign) 
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
                (define %max-b-0 (bvmax slice_v2 (bv 0 (bitvector iprec)) sign)) 
                (define %lshift (bvshl (bv 1 (bitvector iprec)) %max-b-0 )) 
                (define %half (bvdiv %lshift (bv 2 (bitvector iprec)) sign)) 
                (define %widen_half_v2 (bvsizeext %half widenprec sign)) 
                (define %sum (bvadd %widen_slice_v1 %widen_half_v2)) 
                (define %rshift (bvshr %sum %widen_slice_v2 sign)) 
                (define %narrow (bvsaturate %rshift widenprec iprec sign)) 
                %narrow 

                ) 
      ) 
    ) 
  dst 
  ) 

; Compute saturating_narrow(rounding_shift_right(widening_mul(a, b), q))

(define (typed-folded:vec-rounding_mul_shift_right v1 v2 v3 iprec widenprec isize sign) 
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
                (define %lastidx3 (- iprec 1)) 
                (define %high3 (+ %lastidx3 %iter)) 
                (define slice_v3 (extract %high3 %iter v3)) 
                (define %widen_slice_v3 (bvsizeext slice_v3 widenprec sign)) 
                (define %widen-mul-a-b (bvmul %widen_slice_v1 %widen_slice_v2))
                
                ;; saturating_narrow(widening_add(a, (1 << max(b, 0)) / 2) >> b).
                (define %max-q-0 (bvmax %widen_slice_v3 (bv 0 (bitvector widenprec)) sign)) 
                (define %lshift (bvshl (bv 1 (bitvector widenprec)) %max-q-0 )) 
                (define %half (bvdiv %lshift (bv 2 (bitvector widenprec)) sign)) 
                (define %widen_half_v3 (bvsizeext %half (* widenprec 2) sign)) 
                (define %double-widen-mul-a-b (bvsizeext %widen-mul-a-b (* widenprec 2) sign)) 
                (define %sum (bvadd %double-widen-mul-a-b %widen_half_v3)) 
                (define %double-widen-v3 (bvsizeext %widen_slice_v3 (* widenprec 2) sign)) 
                (define %rshift (bvshr %sum %double-widen-v3 sign)) 
                (define %narrow (bvsaturate %rshift (* widenprec 2) widenprec sign)) 
                (define %double-narrow (bvsaturate %narrow widenprec iprec sign)) 
                %double-narrow
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

(define (typed:vec-widen-mul v1 v2 iprec widenprec isize sign)
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
                     (define %prod (bvmul %widen_slice_v1 %widen_slice_v1))
                     %prod
                     )
           )
    )
  dst
  )

(define (typed-folded:broadcast %v1 iprec factor)
  (define dst
    (apply 
      concat
           (for/list ([%iter (reverse (range 0 factor 1))])
                     %v1
                     )
           )
    )
  dst
  )


(define (typed-folded:slice_vectors %v1 iprec %isize base stride len)
  (define dst
    (apply 
      concat
           (for/list ([%iter (reverse (range 0 len 1))])
                     (define %offset-from-base (* iprec stride))
                     (define %elem-idx (+ base %iter))
                     (define %offset-to-base (* %elem-idx iprec))
                     (define %offset (+ %offset-to-base %offset-from-base))
                     (define %lastidx (- iprec 1))
                     (define %high (+ %offset %lastidx))
                     (define %slice (extract %high %offset %v1))
                     %slice
                     )
           )
    )
  dst
  )


(define test-vec (create-tensor 1 64 16))
(println test-vec)
(typed-folded:slice_vectors test-vec 8 1024 0 1 64)
;(typed:vec-rounding_shift_right test-vec test-vec 16 32 1024 1)
