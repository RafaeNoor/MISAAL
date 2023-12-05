#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require rosette/lib/destruct)

(require hydride/utils/bvops)
(require hydride/utils/misc)


(require hydride/ir/hydride/definition)
(require misaal/ir/halide/types)

(require hydride/halide)

(require 
  (only-in racket/base error)
  )


(provide (all-defined-out))
;; ================================================================================
;;                                Hydride Visitor 
;; ================================================================================
(define (typed:halide:visitor prog fn)
  (destruct prog
            [(dim-x id) (fn prog)]
            [(dim-y id) (fn prog)]
            [(idx-i id) (fn prog)]
            [(idx-j id) (fn prog)]
            [(reg id) (fn prog) ]
            [(buffer-index index elemT buffSize) (fn prog)]
            [(typed:int-imm data prec signed?) (fn prog)]
            [(lit v) (fn prog)]
            [(nop v1) (typed:halide:visitor v1 fn)]
            [(idx-add i1 i2) (fn prog) ]
            [(idx-mul i1 i2) (fn prog) ]
            [ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( vector-two-input-swizzle_dsl v0-visited v1-visited num_2 prec_i_o num_4 num_5 num_6 num_7 num_8 ))
             ]
            [ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( interleave-vectors_dsl v0-visited v1-visited size_i_o prec_i_o ))
             ]
            [ (interleave-vector_dsl v0 size_i_o prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (fn ( interleave-vector_dsl v0-visited size_i_o prec_i_o ))
             ]
            [ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (fn ( deinterleave-vector_dsl v0-visited size_i_o prec_i_o ))
             ]
            [ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (define v4-visited (typed:halide:visitor v4 fn))
             (fn ( llvm_shuffle_vectors_dsl v0-visited v1-visited num_2 prec_i_o v4-visited num_5 ))
             ]
            [ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( llvm-vect-add_dsl v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( llvm-vect-sub_dsl v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( llvm-vect-mul_dsl v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( llvm-vect-sdiv_dsl v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( llvm-vect-udiv_dsl v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (llvm-zext_dsl v0 size_i size_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (fn ( llvm-zext_dsl v0-visited size_i size_o ))
             ]
            [ (scalar_splat_dsl v0 size_i size_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (fn ( scalar_splat_dsl v0-visited size_i size_o ))
             ]
            [ (typed:cast-int v0 prec_i num_2 num_3 prec_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (fn ( typed:cast-int v0-visited prec_i num_2 num_3 prec_o ))
             ]
            [ (typed:cast-uint v0 prec_i num_2 num_3 prec_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (fn ( typed:cast-uint v0-visited prec_i num_2 num_3 prec_o ))
             ]
            [ (typed:concat_vectors v0 v1 prec_i_o size_i)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:concat_vectors v0-visited v1-visited prec_i_o size_i ))
             ]
            [ (typed:signed-vec-abs v0 num_1 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (fn ( typed:signed-vec-abs v0-visited num_1 prec_i_o ))
             ]
            [ (typed:signed-vec-absd v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-absd v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:signed-vec-div v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-div v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:signed-vec-halving_add v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-halving_add v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:signed-vec-max v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-max v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:signed-vec-min v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-min v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:signed-vec-mod v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-mod v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:signed-vec-mul v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-mul v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:signed-vec-rounding_halving_add v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-rounding_halving_add v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:signed-vec-rounding_mul_shift_right v0 v1 v2 num_3 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (define v2-visited (typed:halide:visitor v2 fn))
             (fn ( typed:signed-vec-rounding_mul_shift_right v0-visited v1-visited v2-visited num_3 prec_i_o ))
             ]
            [ (typed:signed-vec-rounding_shift_right v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-rounding_shift_right v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:signed-vec-sat-add v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-sat-add v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:signed-vec-sat-sub v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-sat-sub v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:signed-vec-shr v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-shr v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:signed-vec-widen-mul v0 v1 prec_i_o size_i)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-widen-mul v0-visited v1-visited prec_i_o size_i ))
             ]
            [ (typed:slice_vectors v0 num_1 num_2 num_3 prec_i_o size_i)
             (define v0-visited (typed:halide:visitor v0 fn))
             (fn ( typed:slice_vectors v0-visited num_1 num_2 num_3 prec_i_o size_i ))
             ]
            [ (typed:unsigned-vec-absd v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-absd v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:unsigned-vec-div v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-div v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:unsigned-vec-halving_add v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-halving_add v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:unsigned-vec-max v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-max v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:unsigned-vec-min v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-min v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:unsigned-vec-mod v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-mod v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:unsigned-vec-mul v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-mul v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:unsigned-vec-rounding_halving_add v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-rounding_halving_add v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:unsigned-vec-rounding_mul_shift_right v0 v1 v2 num_3 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (define v2-visited (typed:halide:visitor v2 fn))
             (fn ( typed:unsigned-vec-rounding_mul_shift_right v0-visited v1-visited v2-visited num_3 prec_i_o ))
             ]
            [ (typed:unsigned-vec-rounding_shift_right v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-rounding_shift_right v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:unsigned-vec-sat-add v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-sat-add v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:unsigned-vec-sat-sub v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-sat-sub v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:unsigned-vec-shr v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-shr v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:unsigned-vec-widen-mul v0 v1 prec_i_o size_i)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-widen-mul v0-visited v1-visited prec_i_o size_i ))
             ]
            [ (typed:vec-add v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:vec-add v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:vec-bwand v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:vec-bwand v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:vec-bwnot v0 num_1 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (fn ( typed:vec-bwnot v0-visited num_1 prec_i_o ))
             ]
            [ (typed:vec-saturate v0 prec_i num_2 num_3 prec_o bool_5)
             (define v0-visited (typed:halide:visitor v0 fn))
             (fn ( typed:vec-saturate v0-visited prec_i num_2 num_3 prec_o bool_5 ))
             ]
            [ (typed:vec-shl v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:vec-shl v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:vec-sub v0 v1 num_2 prec_i_o)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:vec-sub v0-visited v1-visited num_2 prec_i_o ))
             ]
            [ (typed:xBroadcast v0 size_i prec_i_o num_3)
             (define v0-visited (typed:halide:visitor v0 fn))
             (fn ( typed:xBroadcast v0-visited size_i prec_i_o num_3 ))
             ]

            [ (typed:signed-vec-le v0 v1 prec_i size_i)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-le v0-visited v1-visited prec_i size_i ))
             ]
            [ (typed:signed-vec-lt v0 v1 prec_i size_i)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:signed-vec-lt v0-visited v1-visited prec_i size_i ))
             ]

            [ (typed:unsigned-vec-le v0 v1 prec_i size_i)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-le v0-visited v1-visited prec_i size_i ))
             ]
            [ (typed:unsigned-vec-lt v0 v1 prec_i size_i)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:unsigned-vec-lt v0-visited v1-visited prec_i size_i ))
             ]

            [ (typed:vec-eq v0 v1 prec_i size_i)
             (define v0-visited (typed:halide:visitor v0 fn))
             (define v1-visited (typed:halide:visitor v1 fn))
             (fn ( typed:vec-eq v0-visited v1-visited prec_i size_i ))
             ]

	[ (typed:signed-vector_reduce_add width vec iprec isize)
             (define vec-visited (typed:halide:visitor vec fn))
             (fn ( typed:signed-vector_reduce_add width vec-visited iprec isize))
	]

	[ (typed:unsigned-vector_reduce_add width vec iprec isize)
             (define vec-visited (typed:halide:visitor vec fn))
             (fn ( typed:unsigned-vector_reduce_add width vec-visited iprec isize))
	]

            [_ (error "Unrecognized expression in typed:halide:visitor" prog)]
            )
  )
;; ================================================================================

