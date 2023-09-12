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
;;                                DSL Interpreter
;; ================================================================================
(define (typed:halide:interpret prog env)
  (destruct prog
            [(reg id) (vector-ref-bv env id)]
            [(typed:int-imm data prec signed?)
            (lambda (i) (halide:imm-ref data signed?) )
             ]
            [(buffer-index index elemT buffsize) (lambda (i) (halide:buffer-ref (halide:create-buffer (vector-ref env index) elemT) i))]
            [(lit v) v]
            [ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
             (vector-two-input-swizzle (typed:halide:interpret v0 env) (typed:halide:interpret v1 env) num_2 
                                       prec_i_o num_4 num_5 
                                       num_6 num_7 num_8)
             ]
            [ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
             (interleave-vectors (typed:halide:interpret v0 env) (typed:halide:interpret v1 env) size_i_o 
                                 prec_i_o)
             ]
            [ (interleave-vector_dsl v0 size_i_o prec_i_o)
             (interleave-vector (typed:halide:interpret v0 env) size_i_o prec_i_o)
             ]
            [ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
             (deinterleave-vector (typed:halide:interpret v0 env) size_i_o prec_i_o)
             ]
            [ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
             (llvm_shuffle_vectors (typed:halide:interpret v0 env) (typed:halide:interpret v1 env) num_2 
                                   prec_i_o (typed:halide:interpret v4 env) num_5)
             ]
            [ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
             (llvm-vect-add (typed:halide:interpret v0 env) (typed:halide:interpret v1 env) num_2 
                            prec_i_o)
             ]
            [ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
             (llvm-vect-sub (typed:halide:interpret v0 env) (typed:halide:interpret v1 env) num_2 
                            prec_i_o)
             ]
            [ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
             (llvm-vect-mul (typed:halide:interpret v0 env) (typed:halide:interpret v1 env) num_2 
                            prec_i_o)
             ]
            [ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
             (llvm-vect-sdiv (typed:halide:interpret v0 env) (typed:halide:interpret v1 env) num_2 
                             prec_i_o)
             ]
            [ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
             (llvm-vect-udiv (typed:halide:interpret v0 env) (typed:halide:interpret v1 env) num_2 
                             prec_i_o)
             ]
            [ (llvm-zext_dsl v0 size_i size_o)
             (llvm-zext (typed:halide:interpret v0 env) size_i size_o)
             ]
            [ (scalar_splat_dsl v0 size_i size_o)
             (scalar_splat (typed:halide:interpret v0 env) size_i size_o)
             ]
            [ (typed:cast-int v0 prec_i num_2 num_3 prec_o)
             (lambda (i) (cpp:cast ((typed:halide:interpret v0 env) i) 
                                   (cond
                                     [(eq? prec_o 8)  'int8]
                                     [(eq? prec_o 16)  'int16]
                                     [(eq? prec_o 32)  'int32]
                                     [(eq?  prec_o 64)  'int64]
                                     [else (error "typed_halide/interpreter.rkt: Unexpected buffer type in size-to-elemT-signed" prec_o )]
                                     )
                                   ))


             ]
            [ (typed:cast-uint v0 prec_i num_2 num_3 prec_o)
             (lambda (i) (cpp:cast ((typed:halide:interpret v0 env) i) 
                                   (cond
                                     [(eq? prec_o 8)  'int8]
                                     [(eq? prec_o 16)  'int16]
                                     [(eq? prec_o 32)  'int32]
                                     [(eq? prec_o 64)  'int64]
                                     [else (error "halide/interpreter.rkt: Unexpected buffer type in size-to-elemT-signed" prec_o )]
                                     )
                                   ))
             ]
            [ (typed:concat_vectors v0 v1 prec_i_o size_i)
             (define input_len (/ size_i prec_i_o))
             (lambda (i) (if (< i input_len) ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) (- i input_len))))
             ]
            [ (typed:signed-vec-abs v0 num_1 prec_i_o)
             (lambda (i) (halide:do-abs ((typed:halide:interpret v0 env) i)))

             ]
            [ (typed:signed-vec-absd v0 v1 num_2 prec_i_o)
             (lambda (i) 
               (halide:do-absd ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i))
               )
             ]
            [ (typed:signed-vec-div v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-div ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:signed-vec-halving_add v0 v1 num_2 prec_i_o)

             (lambda (i) (halide:do-rounding-halving-add ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i) #f))

             ]
            [ (typed:signed-vec-max v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-max ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:signed-vec-min v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-min ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:signed-vec-mod v0 v1 num_2 prec_i_o)

             (lambda (i) (halide:do-mod ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:signed-vec-mul v0 v1 num_2 prec_i_o)

             (lambda (i) (halide:do-mul ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:signed-vec-rounding_halving_add v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-rounding-halving-add ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i) #t))
             ]
            [ (typed:signed-vec-rounding_mul_shift_right v0 v1 v2 num_3 prec_i_o)
             (lambda (i) (halide:do-rounding-mul-shift-right ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i) ((typed:halide:interpret v2 env) i) ))
             ]
            [ (typed:signed-vec-rounding_shift_right v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-rounding-shift-right ((typed:halide:interpret env v0 env) i) ((typed:halide:interpret v1 env) i)))

             ]
            [ (typed:signed-vec-sat-add v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-sat-add ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))

             ]
            [ (typed:signed-vec-sat-sub v0 v1 num_2 prec_i_o)

             (lambda (i) (halide:do-sat-sub ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:signed-vec-shr v0 v1 num_2 prec_i_o)

             (lambda (i) (halide:do-shr ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))

             ]
            [ (typed:signed-vec-widen-mul v0 v1 prec_i_o size_i)
             (lambda (i) (halide:do-widened-mul ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:slice_vectors v0 num_1 num_2 num_3 prec_i_o size_i)
             (lambda (i) ((typed:halide:interpret v0 env) (+ num_1 (* i num_2))))
             ]
            [ (typed:unsigned-vec-absd v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-absd ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:unsigned-vec-div v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-div ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:unsigned-vec-halving_add v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-rounding-halving-add ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i) #f))
             ]
            [ (typed:unsigned-vec-max v0 v1 num_2 prec_i_o)
(lambda (i) (halide:do-max ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:unsigned-vec-min v0 v1 num_2 prec_i_o)

(lambda (i) (halide:do-min ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:unsigned-vec-mod v0 v1 num_2 prec_i_o)

(lambda (i) (halide:do-mod ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:unsigned-vec-mul v0 v1 num_2 prec_i_o)

(lambda (i) (halide:do-mul ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:unsigned-vec-rounding_halving_add v0 v1 num_2 prec_i_o)
(lambda (i) (halide:do-rounding-halving-add ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i) #t))
             ]
            [ (typed:unsigned-vec-rounding_mul_shift_right v0 v1 v2 num_3 prec_i_o)

             (lambda (i) (halide:do-rounding-mul-shift-right ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i) ((typed:halide:interpret v2 env) i) ))
             ]
            [ (typed:unsigned-vec-rounding_shift_right v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-rounding-shift-right ((typed:halide:interpret env v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:unsigned-vec-sat-add v0 v1 num_2 prec_i_o)

             (lambda (i) (halide:do-sat-add ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:unsigned-vec-sat-sub v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-sat-sub ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:unsigned-vec-shr v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-shr ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:unsigned-vec-widen-mul v0 v1 prec_i_o size_i)

             (lambda (i) (halide:do-widened-mul ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:vec-add v0 v1 num_2 prec_i_o)

             (lambda (i) (halide:do-add ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:vec-bwand v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-bwand ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:vec-bwnot v0 num_1 prec_i_o)
             (lambda (i) (halide:do-bwnot ((typed:halide:interpret v0 env) i) ))
             ]
            [ (typed:vec-saturate v0 prec_i num_2 num_3 oprec signed?)
             (lambda (i) 
               (define input-val (cpp:eval ((typed:halide:interpret v0) i)))
               (cond
                 [(and signed? (eq? oprec 8))  (int8_t (bvssat input-val (bvlength input-val) 8))]
                 [(and signed? (eq? oprec 16))  (int16_t (bvssat input-val (bvlength input-val) 16))]
                 [(and signed? (eq? oprec 32))  (int32_t (bvssat input-val (bvlength input-val) 32))]
                 [(and signed? (eq? oprec 64))  (int64_t (bvssat input-val (bvlength input-val) 64))]
                 [(and  (eq? oprec 8))  (uint8_t (bvusat input-val (bvlength input-val) 8))]
                 [(and  (eq? oprec 16))  (uint16_t (bvusat input-val (bvlength input-val) 16))]
                 [(and  (eq? oprec 32))  (uint32_t (bvusat input-val (bvlength input-val) 32))]
                 [(and  (eq? oprec 64))  (uint64_t (bvusat input-val (bvlength input-val) 64))]
                 [else (error "halide/interpreter.rkt: Unexpected buffer type in vec-saturate" oprec )]
                 )
               )

             ]
            [ (typed:vec-shl v0 v1 num_2 prec_i_o)
             (lambda (i) (halide:do-shl ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:vec-sub v0 v1 num_2 prec_i_o)
             (println (typed:halide:get-prec v0 (vector)))
             (assert (equal? (typed:halide:get-prec v0 (vector)) num_2))
             (assert (equal? (typed:halide:get-prec v1 (vector)) num_2))
             (lambda (i) (halide:do-sub ((typed:halide:interpret v0 env) i) ((typed:halide:interpret v1 env) i)))
             ]
            [ (typed:xBroadcast v0 size_i prec_i_o num_3)
                (lambda (i) ((typed:halide:interpret v0 env) 0))
             ]
            [v (error "Unrecognized Term in Interpreter" v)]
            )
  )


(define (typed:halide:interpret-hydride expr env)
  (printf "vec-size ~a\n" (typed:halide:get-length expr env)  )
  (printf "vec-prec ~a\n" (typed:halide:get-prec expr env)  )
  (define vec-len (/ (typed:halide:get-length expr env) (typed:halide:get-prec expr env)))
  (printf "vec-len ~a\n" vec-len)
  (halide:assemble-bitvector (typed:halide:interpret expr env) vec-len)
  )

;; ================================================================================
