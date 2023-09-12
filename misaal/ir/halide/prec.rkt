#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require rosette/lib/destruct)

(require hydride/utils/bvops)
(require hydride/utils/misc)

(require 
  (only-in racket/base error)
  )

(require hydride/halide)

(require hydride/ir/hydride/definition)
(require misaal/ir/halide/types)


(provide (all-defined-out))
;; ================================================================================
;;                                DSL Get Output Precision
;; ================================================================================






(define (typed:halide:get-prec prog env)
 (destruct prog
	[(dim-x id) 1]
	[(dim-y id) 1]
	[(idx-i id) 1]
	[(idx-j id) 1]
	[(reg id) (bvlength (vector-ref-bv env id))] ;; FIX-ME NOTE: DO NOT USE THIS METHOD FOR PREC
	[(lit v) (bvlength v)]
	[(nop v1) (typed:halide:get-prec v1 env)]
    [(buffer-index index elemT buffSize) (halide:intr-elemT-size elemT)]
    [(typed:int-imm data prec signed?) prec]
	[(idx-add i1 i2) 1]
	[(idx-mul i1 i2) 1]
	[(vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8) num_2]
	[(interleave-vectors_dsl v0 v1 size_i_o prec_i_o) prec_i_o]
	[(interleave-vector_dsl v0 size_i_o prec_i_o) prec_i_o]
	[(deinterleave-vector_dsl v0 size_i_o prec_i_o) prec_i_o]
	[(llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5) prec_i_o]
	[(llvm-vect-add_dsl v0 v1 num_2 prec_i_o) prec_i_o ]
	[(llvm-vect-sub_dsl v0 v1 num_2 prec_i_o) prec_i_o ]
	[(llvm-vect-mul_dsl v0 v1 num_2 prec_i_o) prec_i_o ]
	[(llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o) prec_i_o ]
	[(llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o) prec_i_o ]
	[(typed:cast-int v0 prec_i num_2 num_3 prec_o)
		(cond 
		[(and  (equal? prec_i 16) (equal? num_2 #f) (equal? num_3 64) (equal? prec_o 32)) 32]
		[(and  (equal? prec_i 16) (equal? num_2 #f) (equal? num_3 128) (equal? prec_o 8)) 8]
		[(and  (equal? prec_i 32) (equal? num_2 #f) (equal? num_3 64) (equal? prec_o 16)) 16]
		[(and  (equal? prec_i 8) (equal? num_2 #f) (equal? num_3 128) (equal? prec_o 16)) 16]
		[(and  (equal? prec_i 16) (equal? num_2 #t) (equal? num_3 64) (equal? prec_o 32)) 32]
		[(and  (equal? prec_i 16) (equal? num_2 #t) (equal? num_3 128) (equal? prec_o 8)) 8]
		[(and  (equal? prec_i 32) (equal? num_2 #t) (equal? num_3 64) (equal? prec_o 16)) 16]
		[(and  (equal? prec_i 8) (equal? num_2 #t) (equal? num_3 128) (equal? prec_o 16)) 16]
		[else (error "Unable to infer prec for typed:cast-int")]
)

	]
	[(typed:cast-uint v0 prec_i num_2 num_3 prec_o)
		(cond 
		[(and  (equal? prec_i 16) (equal? num_2 #f) (equal? num_3 64) (equal? prec_o 32)) 32]
		[(and  (equal? prec_i 16) (equal? num_2 #f) (equal? num_3 128) (equal? prec_o 8)) 8]
		[(and  (equal? prec_i 32) (equal? num_2 #f) (equal? num_3 64) (equal? prec_o 16)) 16]
		[(and  (equal? prec_i 8) (equal? num_2 #f) (equal? num_3 128) (equal? prec_o 16)) 16]
		[(and  (equal? prec_i 16) (equal? num_2 #t) (equal? num_3 64) (equal? prec_o 32)) 32]
		[(and  (equal? prec_i 16) (equal? num_2 #t) (equal? num_3 128) (equal? prec_o 8)) 8]
		[(and  (equal? prec_i 32) (equal? num_2 #t) (equal? num_3 64) (equal? prec_o 16)) 16]
		[(and  (equal? prec_i 8) (equal? num_2 #t) (equal? num_3 128) (equal? prec_o 16)) 16]
		[else (error "Unable to infer prec for typed:cast-uint")]
)

	]
	[(typed:concat_vectors v0 v1 prec_i_o size_i)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i 1024)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i 1024)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i 1024)) 8]
		[else (error "Unable to infer prec for typed:concat_vectors")]
)

	]
	[(typed:signed-vec-abs v0 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-abs")]
)

	]
	[(typed:signed-vec-absd v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-absd")]
)

	]
	[(typed:signed-vec-div v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-div")]
)

	]
	[(typed:signed-vec-halving_add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-halving_add")]
)

	]
	[(typed:signed-vec-max v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-max")]
)

	]
	[(typed:signed-vec-min v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-min")]
)

	]
	[(typed:signed-vec-mod v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-mod")]
)

	]
	[(typed:signed-vec-mul v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-mul")]
)

	]
	[(typed:signed-vec-rounding_halving_add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-rounding_halving_add")]
)

	]
	[(typed:signed-vec-rounding_mul_shift_right v0 v1 v2 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-rounding_mul_shift_right")]
)

	]
	[(typed:signed-vec-rounding_shift_right v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-rounding_shift_right")]
)

	]
	[(typed:signed-vec-sat-add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-sat-add")]
)

	]
	[(typed:signed-vec-sat-sub v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-sat-sub")]
)

	]
	[(typed:signed-vec-shr v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:signed-vec-shr")]
)

	]
	[(typed:signed-vec-widen-mul v0 v1 prec_i_o size_i)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i 1024)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i 1024)) 16]
		[else (error "Unable to infer prec for typed:signed-vec-widen-mul")]
)

	]
	[(typed:slice_vectors v0 num_1 num_2 num_3 prec_i_o size_i)
		(cond 
		[(and  (equal? num_1 0) (equal? num_2 1) (equal? num_3 64) (equal? prec_i_o 16) (equal? size_i 2048)) 16]
		[(and  (equal? num_1 64) (equal? num_2 1) (equal? num_3 64) (equal? prec_i_o 16) (equal? size_i 2048)) 16]
		[(and  (equal? num_1 0) (equal? num_2 1) (equal? num_3 32) (equal? prec_i_o 32) (equal? size_i 2048)) 32]
		[(and  (equal? num_1 32) (equal? num_2 1) (equal? num_3 32) (equal? prec_i_o 32) (equal? size_i 2048)) 32]
		[(and  (equal? num_1 0) (equal? num_2 1) (equal? num_3 128) (equal? prec_i_o 8) (equal? size_i 2048)) 8]
		[(and  (equal? num_1 128) (equal? num_2 1) (equal? num_3 128) (equal? prec_i_o 8) (equal? size_i 2048)) 8]
		[else (error "Unable to infer prec for typed:slice_vectors")]
)

	]
	[(typed:unsigned-vec-absd v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-absd")]
)

	]
	[(typed:unsigned-vec-div v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-div")]
)

	]
	[(typed:unsigned-vec-halving_add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-halving_add")]
)

	]
	[(typed:unsigned-vec-max v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-max")]
)

	]
	[(typed:unsigned-vec-min v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-min")]
)

	]
	[(typed:unsigned-vec-mod v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-mod")]
)

	]
	[(typed:unsigned-vec-mul v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-mul")]
)

	]
	[(typed:unsigned-vec-rounding_halving_add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-rounding_halving_add")]
)

	]
	[(typed:unsigned-vec-rounding_mul_shift_right v0 v1 v2 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-rounding_mul_shift_right")]
)

	]
	[(typed:unsigned-vec-rounding_shift_right v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-rounding_shift_right")]
)

	]
	[(typed:unsigned-vec-sat-add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-sat-add")]
)

	]
	[(typed:unsigned-vec-sat-sub v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-sat-sub")]
)

	]
	[(typed:unsigned-vec-shr v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-shr")]
)

	]
	[(typed:unsigned-vec-widen-mul v0 v1 prec_i_o size_i)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i 1024)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i 1024)) 16]
		[else (error "Unable to infer prec for typed:unsigned-vec-widen-mul")]
)

	]
	[(typed:vec-add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:vec-add")]
)

	]
	[(typed:vec-bwand v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:vec-bwand")]
)

	]
	[(typed:vec-bwnot v0 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:vec-bwnot")]
)

	]
	[(typed:vec-saturate v0 prec_i num_2 num_3 prec_o bool_5)
		(cond 
		[(and  (equal? prec_i 16) (equal? num_2 #f) (equal? num_3 128) (equal? prec_o 8)) 8]
		[(and  (equal? prec_i 16) (equal? num_2 #f) (equal? num_3 128) (equal? prec_o 8)) 8]
		[(and  (equal? prec_i 32) (equal? num_2 #f) (equal? num_3 64) (equal? prec_o 16)) 16]
		[(and  (equal? prec_i 32) (equal? num_2 #f) (equal? num_3 64) (equal? prec_o 16)) 16]
		[(and  (equal? prec_i 16) (equal? num_2 #t) (equal? num_3 128) (equal? prec_o 8)) 8]
		[(and  (equal? prec_i 16) (equal? num_2 #t) (equal? num_3 128) (equal? prec_o 8)) 8]
		[(and  (equal? prec_i 32) (equal? num_2 #t) (equal? num_3 64) (equal? prec_o 16)) 16]
		[(and  (equal? prec_i 32) (equal? num_2 #t) (equal? num_3 64) (equal? prec_o 16)) 16]
		[else (error "Unable to infer prec for typed:vec-saturate")]
)

	]
	[(typed:vec-shl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[else (error "Unable to infer prec for typed:vec-shl")]
)

	]
	[(typed:vec-sub v0 v1 prec_i_o size_i_o)

		(cond 
		;[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		;[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		;[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		;[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		;[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		;[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
        [else prec_i_o]
		;[else (error "Unable to infer prec for typed:vec-sub")]

)
        prec_i_o

	]
	[(typed:xBroadcast v0 size_i prec_i_o num_3)
		(cond 
		[(and  (equal? size_i 32) (equal? prec_i_o 32) (equal? num_3 32)) 32]
		[(and  (equal? size_i 32) (equal? prec_i_o 32) (equal? num_3 64)) 32]
		[else (error "Unable to infer prec for typed:xBroadcast")]
)

	]
	
[
v
 
1
]
 )
)
;; ================================================================================
