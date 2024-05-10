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
(require rosette/lib/destruct)

(require hydride/utils/bvops)
(require hydride/utils/misc)


(require hydride/ir/hydride/definition)
(require misaal/ir/repair/definition)


(provide (all-defined-out))
;; ================================================================================
;;                                DSL Get Length
;; ================================================================================
(define (repair:get-length prog env)
 (destruct prog
	[(dim-x id) 1]
	[(dim-y id) 1]
	[(idx-i id) 1]
	[(idx-j id) 1]
	[(reg id) (bvlength (vector-ref-bv env id))]
	[(lit v) (bvlength v)]
	[(nop v1) (repair:get-length v1 env)]
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
	[(repair-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-add: "  prog)]
)

	]
	[(repair-bwand_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-bwand: "  prog)]
)

	]
	[(repair-bwnot_dsl v0 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-bwnot: "  prog)]
)

	]
	[(repair-bwor_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-bwor: "  prog)]
)

	]
	[(repair-cast-int_dsl v0 prec_i prec_o size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 128)) 256]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 16)) 32]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)) 128]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 32)) 64]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 64)) 128]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 128)) 256]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)) 128]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 32)) 64]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 64)) 128]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)) 128]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 128)) 256]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 16)) 32]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 32)) 64]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 64)) 128]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 8)) 16]
		[else (error "Unable to infer length for repair-cast-int: "  prog)]
)

	]
	[(repair-cast-uint_dsl v0 prec_i prec_o size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 128)) 256]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 16)) 32]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)) 128]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 32)) 64]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 64)) 128]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 128)) 256]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)) 128]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 32)) 64]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 64)) 128]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)) 128]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 128)) 256]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 16)) 32]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 32)) 64]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 64)) 128]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 8)) 16]
		[else (error "Unable to infer length for repair-cast-uint: "  prog)]
)

	]
	[(repair-sabsd_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-sabsd: "  prog)]
)

	]
	[(repair-saturate_dsl v0 prec_i prec_o size_i bool_4)
		(cond 
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)) 8]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)) 128]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)) 128]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)) 128]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)) 128]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)) 16]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)) 64]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)) 128]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)) 128]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)) 32]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)) 32]
		[else (error "Unable to infer length for repair-saturate: "  prog)]
)

	]
	[(repair-sdiv_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-sdiv: "  prog)]
)

	]
	[(repair-shl_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-shl: "  prog)]
)

	]
	[(repair-smax_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-smax: "  prog)]
)

	]
	[(repair-smin_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-smin: "  prog)]
)

	]
	[(repair-smod_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-smod: "  prog)]
)

	]
	[(repair-smul_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-smul: "  prog)]
)

	]
	[(repair-ssat-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-ssat-add: "  prog)]
)

	]
	[(repair-ssat-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-ssat-sub: "  prog)]
)

	]
	[(repair-sshr_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-sshr: "  prog)]
)

	]
	[(repair-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-sub: "  prog)]
)

	]
	[(repair-uabsd_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-uabsd: "  prog)]
)

	]
	[(repair-udiv_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-udiv: "  prog)]
)

	]
	[(repair-umax_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-umax: "  prog)]
)

	]
	[(repair-umin_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-umin: "  prog)]
)

	]
	[(repair-umod_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-umod: "  prog)]
)

	]
	[(repair-umul_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-umul: "  prog)]
)

	]
	[(repair-usat-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-usat-add: "  prog)]
)

	]
	[(repair-usat-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-usat-sub: "  prog)]
)

	]
	[(repair-ushr_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for repair-ushr: "  prog)]
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
		[else (error "Unable to infer length for repair-vector-reduce-add: "  prog)]
)

	]
 )
)
;; ================================================================================

