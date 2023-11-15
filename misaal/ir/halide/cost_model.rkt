#lang rosette/safe


(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require rosette/lib/destruct)
(require
  rosette/lib/destruct
  hydride/utils/debug
  (only-in racket/base error)
  )

(require hydride/ir/hydride/definition)
(require hydride/halide)
(require misaal/ir/halide/types)




(provide (all-defined-out))
;; ================================================================================
;;                                DSL Cost Model
;; ================================================================================
(define cost_typed:cast-int 1)
(define cost_typed:cast-uint 1)
(define cost_typed:concat_vectors 1)
(define cost_typed:signed-vec-abs 1)
(define cost_typed:signed-vec-absd 1)
(define cost_typed:signed-vec-div 1)
(define cost_typed:signed-vec-halving_add 1)
(define cost_typed:signed-vec-max 1)
(define cost_typed:signed-vec-min 1)
(define cost_typed:signed-vec-mod 1)
(define cost_typed:signed-vec-mul 1)
(define cost_typed:signed-vec-rounding_halving_add 1)
(define cost_typed:signed-vec-rounding_mul_shift_right 1)
(define cost_typed:signed-vec-rounding_shift_right 1)
(define cost_typed:signed-vec-sat-add 1)
(define cost_typed:signed-vec-sat-sub 1)
(define cost_typed:signed-vec-shr 1)
(define cost_typed:signed-vec-widen-mul 1)
(define cost_typed:slice_vectors 1)
(define cost_typed:unsigned-vec-absd 1)
(define cost_typed:unsigned-vec-div 1)
(define cost_typed:unsigned-vec-halving_add 1)
(define cost_typed:unsigned-vec-max 1)
(define cost_typed:unsigned-vec-min 1)
(define cost_typed:unsigned-vec-mod 1)
(define cost_typed:unsigned-vec-mul 1)
(define cost_typed:unsigned-vec-rounding_halving_add 1)
(define cost_typed:unsigned-vec-rounding_mul_shift_right 1)
(define cost_typed:unsigned-vec-rounding_shift_right 1)
(define cost_typed:unsigned-vec-sat-add 1)
(define cost_typed:unsigned-vec-sat-sub 1)
(define cost_typed:unsigned-vec-shr 1)
(define cost_typed:unsigned-vec-widen-mul 1)
(define cost_typed:vec-add 1)
(define cost_typed:vec-bwand 1)
(define cost_typed:vec-bwnot 1)
(define cost_typed:vec-saturate 1)
(define cost_typed:vec-shl 1)
(define cost_typed:vec-sub 1)
(define cost_typed:xBroadcast 1)
(define cost_typed:vec-eq 1)
(define cost_typed:unsigned-vec-le 1)
(define cost_typed:unsigned-vec-lt 1)
(define cost_typed:signed-vec-le 1)
(define cost_typed:signed-vec-lt 1)

(define (typed:halide:cost prog)
 (destruct prog
	[(reg id) 1]
	[(lit v) 1 ]
	[(typed:int-imm  data prec signed?) 1 ]
	[(buffer-index index elemT buffSize) 1]
		[ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(+ 4 (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		 
		)
	]
		[ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(+ 3 (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
		[ (interleave-vector_dsl v0 size_i_o prec_i_o)
		(+ 1 (typed:halide:cost  v0) )
	]
		[ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(+ 1 (typed:halide:cost  v0) )
	]
		[ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(+ 5 (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		 (typed:halide:cost  v4) )
	]
		[ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
		[ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
		[ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
		[ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
		[ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
		[ (llvm-zext_dsl v0 size_i size_o)
		(+ 1 (typed:halide:cost  v0) )
	]
		[ (scalar_splat_dsl v0 size_i size_o)
		(+ 1 (typed:halide:cost  v0) )
	]
	[ (typed:cast-int v0 prec_i num_2 num_3 prec_o)
		(+ cost_typed:cast-int (typed:halide:cost  v0)  
		)
	]
	[ (typed:cast-uint v0 prec_i num_2 num_3 prec_o)
		(+ cost_typed:cast-uint (typed:halide:cost  v0)  
		)
	]
	[ (typed:concat_vectors v0 v1 prec_i_o size_i)
		(+ cost_typed:concat_vectors (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-abs v0 num_1 prec_i_o)
		(+ cost_typed:signed-vec-abs (typed:halide:cost  v0) )
	]
	[ (typed:signed-vec-absd v0 v1 num_2 prec_i_o)
		(+ cost_typed:signed-vec-absd (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-div v0 v1 num_2 prec_i_o)
		(+ cost_typed:signed-vec-div (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-halving_add v0 v1 num_2 prec_i_o)
		(+ cost_typed:signed-vec-halving_add (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-max v0 v1 num_2 prec_i_o)
		(+ cost_typed:signed-vec-max (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-min v0 v1 num_2 prec_i_o)
		(+ cost_typed:signed-vec-min (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-mod v0 v1 num_2 prec_i_o)
		(+ cost_typed:signed-vec-mod (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-mul v0 v1 num_2 prec_i_o)
		(+ cost_typed:signed-vec-mul (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-rounding_halving_add v0 v1 num_2 prec_i_o)
		(+ cost_typed:signed-vec-rounding_halving_add (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-rounding_mul_shift_right v0 v1 v2 num_3 prec_i_o)
		(+ cost_typed:signed-vec-rounding_mul_shift_right (typed:halide:cost  v0)  (typed:halide:cost  v1)  (typed:halide:cost  v2)  
		)
	]
	[ (typed:signed-vec-rounding_shift_right v0 v1 num_2 prec_i_o)
		(+ cost_typed:signed-vec-rounding_shift_right (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-sat-add v0 v1 num_2 prec_i_o)
		(+ cost_typed:signed-vec-sat-add (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-sat-sub v0 v1 num_2 prec_i_o)
		(+ cost_typed:signed-vec-sat-sub (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-shr v0 v1 num_2 prec_i_o)
		(+ cost_typed:signed-vec-shr (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-widen-mul v0 v1 prec_i_o size_i)
		(+ cost_typed:signed-vec-widen-mul (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:slice_vectors v0 num_1 num_2 num_3 prec_i_o size_i)
		(+ cost_typed:slice_vectors (typed:halide:cost  v0)  
		)
	]
	[ (typed:unsigned-vec-absd v0 v1 num_2 prec_i_o)
		(+ cost_typed:unsigned-vec-absd (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-div v0 v1 num_2 prec_i_o)
		(+ cost_typed:unsigned-vec-div (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-halving_add v0 v1 num_2 prec_i_o)
		(+ cost_typed:unsigned-vec-halving_add (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-max v0 v1 num_2 prec_i_o)
		(+ cost_typed:unsigned-vec-max (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-min v0 v1 num_2 prec_i_o)
		(+ cost_typed:unsigned-vec-min (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-mod v0 v1 num_2 prec_i_o)
		(+ cost_typed:unsigned-vec-mod (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-mul v0 v1 num_2 prec_i_o)
		(+ cost_typed:unsigned-vec-mul (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-rounding_halving_add v0 v1 num_2 prec_i_o)
		(+ cost_typed:unsigned-vec-rounding_halving_add (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-rounding_mul_shift_right v0 v1 v2 num_3 prec_i_o)
		(+ cost_typed:unsigned-vec-rounding_mul_shift_right (typed:halide:cost  v0)  (typed:halide:cost  v1)  (typed:halide:cost  v2)  
		)
	]
	[ (typed:unsigned-vec-rounding_shift_right v0 v1 num_2 prec_i_o)
		(+ cost_typed:unsigned-vec-rounding_shift_right (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-sat-add v0 v1 num_2 prec_i_o)
		(+ cost_typed:unsigned-vec-sat-add (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-sat-sub v0 v1 num_2 prec_i_o)
		(+ cost_typed:unsigned-vec-sat-sub (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-shr v0 v1 num_2 prec_i_o)
		(+ cost_typed:unsigned-vec-shr (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-widen-mul v0 v1 prec_i_o size_i)
		(+ cost_typed:unsigned-vec-widen-mul (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:vec-add v0 v1 num_2 prec_i_o)
		(+ cost_typed:vec-add (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:vec-bwand v0 v1 num_2 prec_i_o)
		(+ cost_typed:vec-bwand (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:vec-bwnot v0 num_1 prec_i_o)
		(+ cost_typed:vec-bwnot (typed:halide:cost  v0) )
	]
	[ (typed:vec-saturate v0 prec_i num_2 num_3 prec_o bool_5)
		(+ cost_typed:vec-saturate (typed:halide:cost  v0)  
		)
	]
	[ (typed:vec-shl v0 v1 num_2 prec_i_o)
		(+ cost_typed:vec-shl (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:vec-sub v0 v1 num_2 prec_i_o)
		(+ cost_typed:vec-sub (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:xBroadcast v0 size_i prec_i_o num_3)
		(+ cost_typed:xBroadcast (typed:halide:cost  v0)  
		)
	]

	[ (typed:vec-eq v0 v1 prec_i size_i)
		(+ cost_typed:vec-eq (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]

	[ (typed:unsigned-vec-le v0 v1 prec_i size_i)
		(+ cost_typed:unsigned-vec-le (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-lt v0 v1 prec_i size_i)
		(+ cost_typed:unsigned-vec-lt (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]

	[ (typed:signed-vec-le v0 v1 prec_i size_i)
		(+ cost_typed:signed-vec-le (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[ (typed:signed-vec-lt v0 v1 prec_i size_i)
		(+ cost_typed:signed-vec-lt (typed:halide:cost  v0)  (typed:halide:cost  v1)  
		)
	]
	[v  (error "Unrecognized Term in cost model" v)]
 )
)
;; ================================================================================
