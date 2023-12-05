#lang rosette

(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require rosette/lib/destruct)
(require
  rosette/lib/destruct
  hydride/cpp
  hydride/utils/bvops

  (only-in racket/base error)
  hydride/ir/halide/types)

(require hydride/halide)
(require hydride/cpp)
(require hydride/utils/misc)
(require hydride/utils/llvm_impl)
(require hydride/utils/bvops)

(require hydride/ir/hydride/definition)
(require misaal/ir/halide/types)
(require misaal/ir/halide/length)
(require misaal/ir/halide/prec)

(provide  (all-defined-out))
;; ================================================================================
;;                               Halide Semantics Implementation
;; ================================================================================


(define (do-typed:xBroadcast sca prec size factor)
  ;(printf "bvlength broadcast input ~a\n" (bvlength sca))
  (define vals 
    (for/list ([i (range factor)])
              sca
              )
    )
  (define result
    (apply concat (reverse vals))
    )
  ;(printf "Broadcast result size: ~a\n" (bvlength result))
  result
  )


(define (do-typed:ramp base stride len)
  (define vals 
    (for/list ([i (range len)])
              (define addend (* i stride))
              (bvadd base (bv addend (bitvector (bvlength base))))
              )
    )

  ( apply concat (reverse vals))
  )



(define (do-typed:cast-int vec iprec isigned? olane oprec)

  ;(printf "bvlength cast-int input ~a\n" (bvlength vec))
  (define vals 
    (for/list ([i (range olane)])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define slice (extract high low vec))

              (cond 
                [(>= oprec iprec)
                    (sign-extend slice (bitvector oprec))
                 ]
                [else
                  (extract (- oprec 1) 0 slice)
                  ]
                )
              )
    )
  (define result ( apply concat (reverse vals)))

  ;(printf "Cast-int result size: ~a\n" (bvlength result))
  result
  )



(define (do-typed:cast-uint vec iprec isigned? olane oprec)
  ;(printf "bvlength cast-uint input ~a\n" (bvlength vec))
  (define vals 
    (for/list ([i (range olane)])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define slice (extract high low vec))

              (cond 
                [(>= oprec iprec)
                    (zero-extend slice (bitvector oprec))
                 ]
                [else
                  (extract (- oprec 1) 0 slice)
                  ]
                )
              )
    )


  (define result ( apply concat (reverse vals)))

  ;(printf "Cast-uint result size: ~a\n" (bvlength result))
  result

  )

(define (do-typed:vec-broadcast n vec iprec isize)

  (define vals 
    (for/list ([i (range n)])
              vec
              )
    )
  ( apply concat (reverse vals))
  )


(define (do-typed:slice_vectors vec base stride len iprec isize)
  ;(printf "bvlength slice_vectors input ~a\n" (bvlength vec))
  (define vals 
    (for/list ([i (range len)])
              (define slice_index (+ base (* stride i)))
              (define low (* slice_index iprec))
              (define high (+ low (- iprec 1)))
              (extract high low vec)
              )
    )

  (define result ( apply concat (reverse vals)))

  ;(printf "Slice vectors result size: ~a\n" (bvlength result))
  result
  )


(define (do-typed:concat_vectors v1 v2 iprec isize)
  ;(printf "bvlength concat input ~a ~a\n" (bvlength v1) (bvlength v2))
  (concat v1 v2)
  )

(define (do-typed:saturate vec  iprec isigned? olane oprec signed?)
  ;(printf "bvlength saturate input ~a\n" (bvlength vec))
  (define vals 
    (for/list ([i (range olane)])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define slice (extract high low vec))
              (cond 
                [signed?
                  (bvssat slice iprec oprec)
                  ]
                [else
                  (bvusat slice iprec oprec)
                  ]
                
                )
              )
    )

  (define result ( apply concat (reverse vals)))
  ;(printf "saturate result size: ~a\n" (bvlength result))
  result
  )


(define (do-typed:if v1 v2 v3 iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v2_slice (extract high low v2))
              (define v3_slice (extract high low v3))
              (define v1_slice (extract i i v1))
              (cond 
                [(bveq v1_slice (bv 1 1))
                 v2_slice
                  ]
                [else
                  v3_slice
                  ]
                
                )
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:eq v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (cond 
                [(bveq v1_slice v2_slice)
                 (bv 1 1)
                  ]
                [else
                 (bv 0 1)
                  ]
                
                )
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:add v1 v2  iprec isize)
  ;(printf "bvlength add input ~a ~a\n" (bvlength v1) (bvlength v2))
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvadd v1_slice v2_slice)
              )
    )

  (define result ( apply concat (reverse vals)))
  ;(printf "add result size: ~a\n" (bvlength result))
  result
  )


(define (do-typed:sub v1 v2  iprec isize)
  ;(printf "bvlength sub input ~a ~a\n" (bvlength v1) (bvlength v2))
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvsub v1_slice v2_slice)
              )
    )

  (define result ( apply concat (reverse vals)))
  ;(printf "sub result size: ~a\n" (bvlength result))
  result
  )

(define (do-typed:shl v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvshl v1_slice v2_slice)
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:vec-bwand v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvand v1_slice v2_slice)
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:vec-bwnot v1   iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (bvnot v1_slice)
              )
    )
  ( apply concat (reverse vals))
  )


(define (do-typed:signed-widen-add v1 v2  iprec isize)
  (define widen-v1 (do-typed:cast-int v1 iprec #t (/ isize iprec) (* 2 iprec)))
  (define widen-v2 (do-typed:cast-int v2 iprec #t (/ isize iprec) (* 2 iprec)))
  (do-typed:add widen-v1 widen-v2 (* iprec 2) (* isize 2))
  )

;narrow((widen(a) + widen(b) + 1) / 2)

(define (do-typed:signed-rounding-halving-add v1 v2  iprec isize)
  (define widen-v1 (do-typed:cast-int v1 iprec #t (/ isize iprec) (* 2 iprec)))
  (define widen-v2 (do-typed:cast-int v2 iprec #t (/ isize iprec) (* 2 iprec)))
  (define addend (create-splat-bv (bv 1 (* 2 iprec))  (/ isize iprec)))
  (define sum-a-b (do-typed:add widen-v1 widen-v2 (* iprec 2) (* isize 2)))
  (define sum-addened (do-typed:add sum-a-b addend (* iprec 2) (* isize 2)))
  (define  two (create-splat-bv (bv 2 (* 2 iprec))  (/ isize iprec)))
  (define divided (do-typed:signed-div sum-addened two (* iprec 2) (* isize 2)))
  (do-typed:cast-int divided (* iprec 2) #t (/ isize iprec) iprec)
  )

;narrow((widen(a) + widen(b) + 0) / 2)

(define (do-typed:signed-halving-add v1 v2  iprec isize)
  (define widen-v1 (do-typed:cast-int v1 iprec #t (/ isize iprec) (* 2 iprec)))
  (define widen-v2 (do-typed:cast-int v2 iprec #t (/ isize iprec) (* 2 iprec)))
  (define addend (create-splat-bv (bv 0 (* 2 iprec))  (/ isize iprec)))
  (define sum-a-b (do-typed:add widen-v1 widen-v2 (* iprec 2) (* isize 2)))
  (define sum-addened (do-typed:add sum-a-b addend (* iprec 2) (* isize 2)))
  (define  two (create-splat-bv (bv 2 (* 2 iprec))  (/ isize iprec)))
  (define divided (do-typed:signed-div sum-addened two (* iprec 2) (* isize 2)))
  (do-typed:cast-int divided (* iprec 2) #t (/ isize iprec) iprec)
  )

(define (do-typed:signed-widen-sub v1 v2  iprec isize)
  (define widen-v1 (do-typed:cast-int v1 iprec #t (/ isize iprec) (* 2 iprec)))
  (define widen-v2 (do-typed:cast-int v2 iprec #t (/ isize iprec) (* 2 iprec)))
  (do-typed:sub widen-v1 widen-v2 (* iprec 2) (* isize 2))
  )

(define (do-typed:signed-vec-absd v1 v2  iprec isize)
  (define max_operands (do-typed:signed-max v1 v2 iprec isize))
  (define min_operands (do-typed:signed-min v1 v2 iprec isize))
  (do-typed:sub max_operands min_operands iprec isize)
  )

(define (do-typed:signed-vec-abs v1   iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define abs-int (abs (bitvector->integer v1_slice)))
              (integer->bitvector abs-int (bitvector iprec))
              )
    )
  ( apply concat (reverse vals))
  )
(define (do-typed:signed-sat-add v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvaddnsw v1_slice v2_slice iprec)
              )
    )
  ( apply concat (reverse vals))
  )
(define (do-typed:signed-sat-sub v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvsubnsw v1_slice v2_slice iprec)
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:signed-mul v1 v2  iprec isize)
  ;(printf "bvlength mul input ~a ~a\n" (bvlength v1) (bvlength v2))
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (define widened-v1 (sign-extend v1_slice (bitvector (* iprec 2))))
              (define widened-v2 (sign-extend v2_slice (bitvector (* iprec 2))))
              (define product (bvmul widened-v1 widened-v2))
              (extract (- iprec 1) 0 product)
              )
    )

  (define result ( apply concat (reverse vals)))
  ;(printf "signed-mul result size: ~a\n" (bvlength result))
  result
  )
(define (do-typed:signed-widen-mul v1 v2  iprec isize)

  ;(printf "bvlength mul input ~a ~a\n" (bvlength v1) (bvlength v2))
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (define widened-v1 (sign-extend v1_slice (bitvector (* iprec 2))))
              (define widened-v2 (sign-extend v2_slice (bitvector (* iprec 2))))
              (define product (bvmul widened-v1 widened-v2))
              product
              )
    )
  (define result ( apply concat (reverse vals)))
  ;(printf "signed-widen-mul result size: ~a\n" (bvlength result))
  result
  )

(define (do-typed:signed-div v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvsdiv v1_slice v2_slice)
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:signed-mod v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvsrem v1_slice v2_slice)
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:signed-max v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvsmax v1_slice v2_slice)
              )
    )
  ( apply concat (reverse vals))
  )
(define (do-typed:signed-min v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvsmin v1_slice v2_slice)
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:signed-lt v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (cond 
                [(bvslt v1_slice v2_slice)
                 (bv 1 1)
                  ]
                [else
                 (bv 0 1)
                  ]
                
                )
              )
    )
  ( apply concat (reverse vals))
  )
(define (do-typed:signed-le v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (cond 
                [(bvsle v1_slice v2_slice)
                 (bv 1 1)
                  ]
                [else
                 (bv 0 1)
                  ]
                
                )
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:signed-shr v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvashr v1_slice v2_slice)
              )
    )
  ( apply concat (reverse vals))
  )

; Compute saturating_narrow(rounding_shift_right(widening_mul(a, b), q))
(define (do-typed:signed-rounding_mul_shift_right v1 v2 v3  iprec isize)
  (define widened-product (do-typed:signed-widen-mul v1 v2 iprec isize))
  (define sext-q (do-typed:cast-int v3 iprec #t (/ isize iprec) (* iprec 2)))
  (define rounding-shr (do-typed:signed-rounding_shift_right widened-product sext-q (* iprec 2) (* isize 2) ))
  (do-typed:saturate rounding-shr (* iprec 2) (* isize 2) #t (/ isize iprec) iprec #t)
  )


;; saturating_narrow(widening_add(a, (1 << max(b, 0)) / 2) >> b).
(define (do-typed:signed-rounding_shift_right v1 v2  iprec isize)
  (define zero (bv 0 isize))
  (define max-b-0 (do-typed:signed-max zero v2 iprec isize))
  (define one (create-splat-bv (bv 1 iprec) (/ isize iprec)))
  (define one-shifted (do-typed:shl one max-b-0 iprec isize))

  (define two (create-splat-bv (bv 2 iprec) (/ isize iprec)))
  (define shifted-div-two (do-typed:signed-div one-shifted two iprec isize))
  (define widened-add (do-typed:signed-widen-add v1 shifted-div-two iprec isize))
  (define widen-b (do-typed:cast-int v2 iprec #t (/ isize iprec) (* 2 iprec)))
  (define shift-right (do-typed:signed-shr widened-add widen-b (* 2 iprec) (* isize 2)))
  (do-typed:saturate shift-right (* iprec 2) (* isize 2) #t (/ isize iprec) iprec #t)
  )

(define (do-typed:signed-vector-reduce-add width v1 iprec isize)
  (define vals 
    (for/list ([i (range 0 (/ isize iprec) width)])
              (apply bvadd 
                     (for/list ([k (range width)])
                               (define low (* (+ i k) iprec))
                               (define high (+ low (- iprec 1)))
                               (define vec_slice (extract high low v1))
                               vec_slice
                               )
                     )
              )
    )
  ( apply concat (reverse vals))
  )

;; UNSIGNED OPERATIONS




(define (do-typed:unsigned-widen-add v1 v2  iprec isize)
  (define widen-v1 (do-typed:cast-uint v1 iprec #f (/ isize iprec) (* 2 iprec)))
  (define widen-v2 (do-typed:cast-uint v2 iprec #f (/ isize iprec) (* 2 iprec)))
  (do-typed:add widen-v1 widen-v2 (* iprec 2) (* isize 2))
  )

;narrow((widen(a) + widen(b) + 1) / 2)
(define (do-typed:unsigned-rounding-halving-add v1 v2  iprec isize)
  (define widen-v1 (do-typed:cast-uint v1 iprec #f (/ isize iprec) (* 2 iprec)))
  (define widen-v2 (do-typed:cast-uint v2 iprec #f (/ isize iprec) (* 2 iprec)))
  (define addend (create-splat-bv (bv 1 (* 2 iprec))  (/ isize iprec)))
  (define sum-a-b (do-typed:add widen-v1 widen-v2 (* iprec 2) (* isize 2)))
  (define sum-addened (do-typed:add sum-a-b addend (* iprec 2) (* isize 2)))
  (define  two (create-splat-bv (bv 2 (* 2 iprec))  (/ isize iprec)))
  (define divided (do-typed:unsigned-div sum-addened two (* iprec 2) (* isize 2)))
  (do-typed:cast-uint divided (* iprec 2) #f (/ isize iprec) iprec)
  )

;narrow((widen(a) + widen(b) + 0) / 2)
(define (do-typed:unsigned-halving-add v1 v2  iprec isize)
  (define widen-v1 (do-typed:cast-uint v1 iprec #f (/ isize iprec) (* 2 iprec)))
  (define widen-v2 (do-typed:cast-uint v2 iprec #f (/ isize iprec) (* 2 iprec)))
  (define addend (create-splat-bv (bv 0 (* 2 iprec))  (/ isize iprec)))
  (define sum-a-b (do-typed:add widen-v1 widen-v2 (* iprec 2) (* isize 2)))
  (define sum-addened (do-typed:add sum-a-b addend (* iprec 2) (* isize 2)))
  (define  two (create-splat-bv (bv 2 (* 2 iprec))  (/ isize iprec)))
  (define divided (do-typed:unsigned-div sum-addened two (* iprec 2) (* isize 2)))
  (do-typed:cast-uint divided (* iprec 2) #f (/ isize iprec) iprec)
  )

(define (do-typed:unsigned-widen-sub v1 v2  iprec isize)
  (define widen-v1 (do-typed:cast-uint v1 iprec #f (/ isize iprec) (* 2 iprec)))
  (define widen-v2 (do-typed:cast-uint v2 iprec #f (/ isize iprec) (* 2 iprec)))
  (do-typed:sub widen-v1 widen-v2 (* iprec 2) (* isize 2))
  )

(define (do-typed:unsigned-vec-absd v1 v2  iprec isize)
  (define max_operands (do-typed:unsigned-max v1 v2 iprec isize))
  (define min_operands (do-typed:unsigned-min v1 v2 iprec isize))
  (do-typed:sub max_operands min_operands iprec isize)
  )

(define (do-typed:unsigned-sat-add v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvaddnuw v1_slice v2_slice iprec)
              )
    )
  ( apply concat (reverse vals))
  )
(define (do-typed:unsigned-sat-sub v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvsubnuw v1_slice v2_slice iprec)
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:unsigned-mul v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (define widened-v1 (zero-extend v1_slice (bitvector (* iprec 2))))
              (define widened-v2 (zero-extend v2_slice (bitvector (* iprec 2))))
              (define product (bvmul widened-v1 widened-v2))
              (extract (- iprec 1) 0 product)
              )
    )
  ( apply concat (reverse vals))
  )
(define (do-typed:unsigned-widen-mul v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (define widened-v1 (zero-extend v1_slice (bitvector (* iprec 2))))
              (define widened-v2 (zero-extend v2_slice (bitvector (* iprec 2))))
              (define product (bvmul widened-v1 widened-v2))
              product
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:unsigned-div v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvudiv v1_slice v2_slice)
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:unsigned-mod v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvurem v1_slice v2_slice)
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:unsigned-max v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvumax v1_slice v2_slice)
              )
    )
  ( apply concat (reverse vals))
  )
(define (do-typed:unsigned-min v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvumin v1_slice v2_slice)
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:unsigned-lt v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (cond 
                [(bvult v1_slice v2_slice)
                 (bv 1 1)
                  ]
                [else
                 (bv 0 1)
                  ]
                
                )
              )
    )
  ( apply concat (reverse vals))
  )
(define (do-typed:unsigned-le v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (cond 
                [(bvule v1_slice v2_slice)
                 (bv 1 1)
                  ]
                [else
                 (bv 0 1)
                  ]
                
                )
              )
    )
  ( apply concat (reverse vals))
  )

(define (do-typed:unsigned-shr v1 v2  iprec isize)
  (define vals 
    (for/list ([i (range (/ isize iprec))])
              (define low (* i iprec))
              (define high (+ low (- iprec 1)))
              (define v1_slice (extract high low v1))
              (define v2_slice (extract high low v2))
              (bvlshr v1_slice v2_slice)
              )
    )
  ( apply concat (reverse vals))
  )

; Compute saturating_narrow(rounding_shift_right(widening_mul(a, b), q))
(define (do-typed:unsigned-rounding_mul_shift_right v1 v2 v3  iprec isize)
  (define widened-product (do-typed:unsigned-widen-mul v1 v2 iprec isize))
  (define sext-q (do-typed:cast-uint v3 iprec #f (/ isize iprec) (* iprec 2)))
  (define rounding-shr (do-typed:unsigned-rounding_shift_right widened-product sext-q (* iprec 2) (* isize 2) ))
  (do-typed:saturate rounding-shr (* iprec 2) (* isize 2) #f (/ isize iprec) iprec #f)
  )


;; saturating_narrow(widening_add(a, (1 << max(b, 0)) / 2) >> b).
(define (do-typed:unsigned-rounding_shift_right v1 v2  iprec isize)
  (define zero (bv 0 isize))
  (define max-b-0 (do-typed:unsigned-max zero v2 iprec isize))
  (define one (create-splat-bv (bv 1 iprec) (/ isize iprec)))
  (define one-shifted (do-typed:shl one max-b-0 iprec isize))

  (define two (create-splat-bv (bv 2 iprec) (/ isize iprec)))
  (define shifted-div-two (do-typed:unsigned-div one-shifted two iprec isize))
  (define widened-add (do-typed:unsigned-widen-add v1 shifted-div-two iprec isize))
  (define widen-b (do-typed:cast-uint v2 iprec #f (/ isize iprec) (* 2 iprec)))
  (define shift-right (do-typed:unsigned-shr widened-add widen-b (* 2 iprec) (* isize 2)))
  (do-typed:saturate shift-right (* iprec 2) (* isize 2) #f (/ isize iprec) iprec #f)
  )

