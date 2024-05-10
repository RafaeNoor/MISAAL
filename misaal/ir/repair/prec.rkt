;#============================== misaal File =================================
;#
;# Part of the misaal Compiler Infrastructure.
;# <Placeholder for license information>
;#
;#=============================================================================
;#
;# Do NOT modify this file. It is automatically generated.
;#
;#=============================================================================

#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)
(require rosette/solver/smt/boolector)

(require hydride/utils/bvops)
(require hydride/utils/misc)

(require hydride/ir/hydride/definition)
(require misaal/ir/repair/definition)


(provide (all-defined-out))
;; ================================================================================
;;                                DSL Get Output Precision
;; ================================================================================
(define (repair:get-prec prog env)
 (destruct prog
	[(dim-x id) 1]
	[(dim-y id) 1]
	[(idx-i id) 1]
	[(idx-j id) 1]
	[(reg id) (bvlength (vector-ref-bv env id))] ;; FIX-ME NOTE: DO NOT USE THIS METHOD FOR PREC
	[(lit v) (bvlength v)]
	[(nop v1) (repair:get-prec v1 env)]
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
	[(repair-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-add")]
)

	]
	[(repair-bwand_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-bwand")]
)

	]
	[(repair-bwnot_dsl v0 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-bwnot")]
)

	]
	[(repair-bwor_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-bwor")]
)

	]
	[(repair-cast-int_dsl v0 prec_i prec_o size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 128)) 32]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 16)) 32]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 32)) 32]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)) 8]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 32)) 64]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 64)) 64]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)) 32]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)) 32]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 128)) 16]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 16)) 16]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 64)) 16]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 8)) 16]
		[else (error "Unable to infer prec for repair-cast-int")]
)

	]
	[(repair-cast-uint_dsl v0 prec_i prec_o size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 128)) 32]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 16)) 32]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 32)) 32]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)) 8]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 32)) 64]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 64)) 64]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)) 32]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)) 32]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 128)) 16]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 16)) 16]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 64)) 16]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 8)) 16]
		[else (error "Unable to infer prec for repair-cast-uint")]
)

	]
	[(repair-sabsd_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-sabsd")]
)

	]
	[(repair-saturate_dsl v0 prec_i prec_o size_i bool_4)
		(cond 
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)) 8]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)) 16]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)) 32]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)) 32]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)) 32]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)) 32]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)) 32]
		[else (error "Unable to infer prec for repair-saturate")]
)

	]
	[(repair-sdiv_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-sdiv")]
)

	]
	[(repair-shl_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-shl")]
)

	]
	[(repair-smax_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-smax")]
)

	]
	[(repair-smin_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-smin")]
)

	]
	[(repair-smod_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-smod")]
)

	]
	[(repair-smul_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-smul")]
)

	]
	[(repair-ssat-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-ssat-add")]
)

	]
	[(repair-ssat-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-ssat-sub")]
)

	]
	[(repair-sshr_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-sshr")]
)

	]
	[(repair-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-sub")]
)

	]
	[(repair-uabsd_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-uabsd")]
)

	]
	[(repair-udiv_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-udiv")]
)

	]
	[(repair-umax_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-umax")]
)

	]
	[(repair-umin_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-umin")]
)

	]
	[(repair-umod_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-umod")]
)

	]
	[(repair-umul_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-umul")]
)

	]
	[(repair-usat-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-usat-add")]
)

	]
	[(repair-usat-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-usat-sub")]
)

	]
	[(repair-ushr_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for repair-ushr")]
)

	]
	[(repair-vector-reduce-add_dsl num_0 v1 size_o size_i)
		(cond 
		[(and  (equal? num_0 2) (equal? size_o 16) (equal? size_i 32)) 16]
		[(and  (equal? num_0 4) (equal? size_o 16) (equal? size_i 64)) 16]
		[(and  (equal? num_0 4) (equal? size_o 32) (equal? size_i 128)) 32]
		[(and  (equal? num_0 2) (equal? size_o 32) (equal? size_i 64)) 32]
		[(and  (equal? num_0 2) (equal? size_o 64) (equal? size_i 128)) 64]
		[(and  (equal? num_0 4) (equal? size_o 64) (equal? size_i 256)) 64]
		[(and  (equal? num_0 2) (equal? size_o 8) (equal? size_i 16)) 8]
		[(and  (equal? num_0 4) (equal? size_o 8) (equal? size_i 32)) 8]
		[else (error "Unable to infer prec for repair-vector-reduce-add")]
)

	]
	
[
v
 
1
]
 )
)
;; ================================================================================

