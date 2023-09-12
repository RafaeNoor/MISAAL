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
;;                                DSL Get Length
;; ================================================================================



(define (typed:halide:get-length prog env)
 (destruct prog
	[(dim-x id) 1]
	[(dim-y id) 1]
	[(idx-i id) 1]
	[(idx-j id) 1]
	[(reg id) (bvlength (vector-ref-bv env id))]
	[(lit v) (bvlength v)]
	[(nop v1) (typed:halide:get-length v1 env)]
    [(buffer-index index elemT buffSize) buffSize]
    [(typed:int-imm data prec signed?) prec]
	[(idx-add i1 i2) 1]
	[(idx-mul i1 i2) 1]
	[(vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8) (* (max 1 (/ num_2 num_5)) (+ num_4 (* 2 num_6)) prec_i_o)]
	[(interleave-vectors_dsl v0 v1 size_i_o prec_i_o) (* 2 size_i_o)]
	[(interleave-vector_dsl v0 size_i_o prec_i_o) size_i_o]
	[(deinterleave-vector_dsl v0 size_i_o prec_i_o) size_i_o]
	[(llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5) (* num_5 prec_i_o) ]
	[(llvm-vect-add_dsl v0 v1 num_2 prec_i_o) (* num_2 prec_i_o) ]
	[(llvm-vect-sub_dsl v0 v1 num_2 prec_i_o) (* num_2 prec_i_o) ]
	[(llvm-vect-mul_dsl v0 v1 num_2 prec_i_o) (* num_2 prec_i_o) ]
	[(llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o) (* num_2 prec_i_o) ]
	[(llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o) (* num_2 prec_i_o) ]
	[(typed:cast-int v0 prec_i num_2 num_3 prec_o)
		(cond 
		[(and  (equal? prec_i 16) (equal? num_2 #f) (equal? num_3 64) (equal? prec_o 32)) 2048]
		[(and  (equal? prec_i 16) (equal? num_2 #f) (equal? num_3 128) (equal? prec_o 8)) 1024]
		[(and  (equal? prec_i 32) (equal? num_2 #f) (equal? num_3 64) (equal? prec_o 16)) 1024]
		[(and  (equal? prec_i 8) (equal? num_2 #f) (equal? num_3 128) (equal? prec_o 16)) 2048]
		[(and  (equal? prec_i 16) (equal? num_2 #t) (equal? num_3 64) (equal? prec_o 32)) 2048]
		[(and  (equal? prec_i 16) (equal? num_2 #t) (equal? num_3 128) (equal? prec_o 8)) 1024]
		[(and  (equal? prec_i 32) (equal? num_2 #t) (equal? num_3 64) (equal? prec_o 16)) 1024]
		[(and  (equal? prec_i 8) (equal? num_2 #t) (equal? num_3 128) (equal? prec_o 16)) 2048]
		[else (error "Unable to infer length for typed:cast-int: "  prog)]
)

	]
	[(typed:cast-uint v0 prec_i num_2 num_3 prec_o)
		(cond 
		[(and  (equal? prec_i 16) (equal? num_2 #f) (equal? num_3 64) (equal? prec_o 32)) 2048]
		[(and  (equal? prec_i 16) (equal? num_2 #f) (equal? num_3 128) (equal? prec_o 8)) 1024]
		[(and  (equal? prec_i 32) (equal? num_2 #f) (equal? num_3 64) (equal? prec_o 16)) 1024]
		[(and  (equal? prec_i 8) (equal? num_2 #f) (equal? num_3 128) (equal? prec_o 16)) 2048]
		[(and  (equal? prec_i 16) (equal? num_2 #t) (equal? num_3 64) (equal? prec_o 32)) 2048]
		[(and  (equal? prec_i 16) (equal? num_2 #t) (equal? num_3 128) (equal? prec_o 8)) 1024]
		[(and  (equal? prec_i 32) (equal? num_2 #t) (equal? num_3 64) (equal? prec_o 16)) 1024]
		[(and  (equal? prec_i 8) (equal? num_2 #t) (equal? num_3 128) (equal? prec_o 16)) 2048]
		[else (error "Unable to infer length for typed:cast-uint: "  prog)]
)

	]
	[(typed:concat_vectors v0 v1 prec_i_o size_i)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i 1024)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i 1024)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i 1024)) 2048]
		[else (error "Unable to infer length for typed:concat_vectors: "  prog)]
)

	]
	[(typed:signed-vec-abs v0 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-abs: "  prog)]
)

	]
	[(typed:signed-vec-absd v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-absd: "  prog)]
)

	]
	[(typed:signed-vec-div v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-div: "  prog)]
)

	]
	[(typed:signed-vec-halving_add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-halving_add: "  prog)]
)

	]
	[(typed:signed-vec-max v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-max: "  prog)]
)

	]
	[(typed:signed-vec-min v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-min: "  prog)]
)

	]
	[(typed:signed-vec-mod v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-mod: "  prog)]
)

	]
	[(typed:signed-vec-mul v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-mul: "  prog)]
)

	]
	[(typed:signed-vec-rounding_halving_add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-rounding_halving_add: "  prog)]
)

	]
	[(typed:signed-vec-rounding_mul_shift_right v0 v1 v2 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-rounding_mul_shift_right: "  prog)]
)

	]
	[(typed:signed-vec-rounding_shift_right v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-rounding_shift_right: "  prog)]
)

	]
	[(typed:signed-vec-sat-add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-sat-add: "  prog)]
)

	]
	[(typed:signed-vec-sat-sub v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-sat-sub: "  prog)]
)

	]
	[(typed:signed-vec-shr v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-shr: "  prog)]
)

	]
	[(typed:signed-vec-widen-mul v0 v1 prec_i_o size_i)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i 1024)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i 1024)) 2048]
		[else (error "Unable to infer length for typed:signed-vec-widen-mul: "  prog)]
)

	]
	[(typed:slice_vectors v0 num_1 num_2 num_3 prec_i_o size_i)
		(cond 
		[(and  (equal? num_1 0) (equal? num_2 1) (equal? num_3 64) (equal? prec_i_o 16) (equal? size_i 2048)) 1024]
		[(and  (equal? num_1 64) (equal? num_2 1) (equal? num_3 64) (equal? prec_i_o 16) (equal? size_i 2048)) 1024]
		[(and  (equal? num_1 0) (equal? num_2 1) (equal? num_3 32) (equal? prec_i_o 32) (equal? size_i 2048)) 1024]
		[(and  (equal? num_1 32) (equal? num_2 1) (equal? num_3 32) (equal? prec_i_o 32) (equal? size_i 2048)) 1024]
		[(and  (equal? num_1 0) (equal? num_2 1) (equal? num_3 128) (equal? prec_i_o 8) (equal? size_i 2048)) 1024]
		[(and  (equal? num_1 128) (equal? num_2 1) (equal? num_3 128) (equal? prec_i_o 8) (equal? size_i 2048)) 1024]
		[else (error "Unable to infer length for typed:slice_vectors: "  prog)]
)

	]
	[(typed:unsigned-vec-absd v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-absd: "  prog)]
)

	]
	[(typed:unsigned-vec-div v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-div: "  prog)]
)

	]
	[(typed:unsigned-vec-halving_add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-halving_add: "  prog)]
)

	]
	[(typed:unsigned-vec-max v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-max: "  prog)]
)

	]
	[(typed:unsigned-vec-min v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-min: "  prog)]
)

	]
	[(typed:unsigned-vec-mod v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-mod: "  prog)]
)

	]
	[(typed:unsigned-vec-mul v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-mul: "  prog)]
)

	]
	[(typed:unsigned-vec-rounding_halving_add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-rounding_halving_add: "  prog)]
)

	]
	[(typed:unsigned-vec-rounding_mul_shift_right v0 v1 v2 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-rounding_mul_shift_right: "  prog)]
)

	]
	[(typed:unsigned-vec-rounding_shift_right v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-rounding_shift_right: "  prog)]
)

	]
	[(typed:unsigned-vec-sat-add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-sat-add: "  prog)]
)

	]
	[(typed:unsigned-vec-sat-sub v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-sat-sub: "  prog)]
)

	]
	[(typed:unsigned-vec-shr v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-shr: "  prog)]
)

	]
	[(typed:unsigned-vec-widen-mul v0 v1 prec_i_o size_i)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i 1024)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i 1024)) 2048]
		[else (error "Unable to infer length for typed:unsigned-vec-widen-mul: "  prog)]
)

	]
	[(typed:vec-add v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:vec-add: "  prog)]
)

	]
	[(typed:vec-bwand v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:vec-bwand: "  prog)]
)

	]
	[(typed:vec-bwnot v0 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:vec-bwnot: "  prog)]
)

	]
	[(typed:vec-saturate v0 prec_i num_2 num_3 prec_o bool_5)
		(cond 
		[(and  (equal? prec_i 16) (equal? num_2 #f) (equal? num_3 128) (equal? prec_o 8)) 1024]
		[(and  (equal? prec_i 16) (equal? num_2 #f) (equal? num_3 128) (equal? prec_o 8)) 1024]
		[(and  (equal? prec_i 32) (equal? num_2 #f) (equal? num_3 64) (equal? prec_o 16)) 1024]
		[(and  (equal? prec_i 32) (equal? num_2 #f) (equal? num_3 64) (equal? prec_o 16)) 1024]
		[(and  (equal? prec_i 16) (equal? num_2 #t) (equal? num_3 128) (equal? prec_o 8)) 1024]
		[(and  (equal? prec_i 16) (equal? num_2 #t) (equal? num_3 128) (equal? prec_o 8)) 1024]
		[(and  (equal? prec_i 32) (equal? num_2 #t) (equal? num_3 64) (equal? prec_o 16)) 1024]
		[(and  (equal? prec_i 32) (equal? num_2 #t) (equal? num_3 64) (equal? prec_o 16)) 1024]
		[else (error "Unable to infer length for typed:vec-saturate: "  prog)]
)

	]
	[(typed:vec-shl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:vec-shl: "  prog)]
)

	]
	[(typed:vec-sub v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[else (error "Unable to infer length for typed:vec-sub: "  prog)]
)

	]
	[(typed:xBroadcast v0 size_i prec_i_o num_3)
		(cond 
		[(and  (equal? size_i 32) (equal? prec_i_o 32) (equal? num_3 32)) 1024]
		[(and  (equal? size_i 32) (equal? prec_i_o 32) (equal? num_3 64)) 2048]
		[else (error "Unable to infer length for typed:xBroadcast: "  prog)]
)

	]
 )
)

;; ================================================================================
