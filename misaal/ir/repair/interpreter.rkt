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
(require hydride/utils/llvm_impl)


(require hydride/ir/hydride/definition)


(require misaal/ir/repair/semantics)
(require misaal/ir/repair/definition)
(require misaal/ir/repair/length)


(provide (all-defined-out))
;; ================================================================================
;;                                DSL Interpreter
;; ================================================================================
(define (repair:interpret prog env)
 (destruct prog
	[(reg id) (vector-ref-bv env id)]
	[(lit v) v]
	[ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(vector-two-input-swizzle (repair:interpret v0 env) (repair:interpret v1 env) num_2 
		 prec_i_o num_4 num_5 
		 num_6 num_7 num_8)
	]
	[ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(interleave-vectors (repair:interpret v0 env) (repair:interpret v1 env) size_i_o 
		 prec_i_o)
	]
	[ (interleave-vector_dsl v0 size_i_o prec_i_o)
		(interleave-vector (repair:interpret v0 env) size_i_o prec_i_o)
	]
	[ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(deinterleave-vector (repair:interpret v0 env) size_i_o prec_i_o)
	]
	[ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(llvm_shuffle_vectors (repair:interpret v0 env) (repair:interpret v1 env) num_2 
		 prec_i_o (repair:interpret v4 env) num_5)
	]
	[ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-add (repair:interpret v0 env) (repair:interpret v1 env) num_2 
		 prec_i_o)
	]
	[ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-sub (repair:interpret v0 env) (repair:interpret v1 env) num_2 
		 prec_i_o)
	]
	[ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-mul (repair:interpret v0 env) (repair:interpret v1 env) num_2 
		 prec_i_o)
	]
	[ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-sdiv (repair:interpret v0 env) (repair:interpret v1 env) num_2 
		 prec_i_o)
	]
	[ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-udiv (repair:interpret v0 env) (repair:interpret v1 env) num_2 
		 prec_i_o)
	]
	[ (llvm-zext_dsl v0 size_i size_o)
		(llvm-zext (repair:interpret v0 env) size_i size_o)
	]
	[ (scalar_splat_dsl v0 size_i size_o)
		(scalar_splat (repair:interpret v0 env) size_i size_o)
	]
	[ (repair-add_dsl v0 v1 prec_i_o size_i_o)
		(repair-add (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-bwand_dsl v0 v1 prec_i_o size_i_o)
		(repair-bwand (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-bwnot_dsl v0 prec_i_o size_i_o)
		(repair-bwnot (repair:interpret v0 env) prec_i_o size_i_o)
	]
	[ (repair-bwor_dsl v0 v1 prec_i_o size_i_o)
		(repair-bwor (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-cast-int_dsl v0 prec_i prec_o size_i)
		(repair-cast-int (repair:interpret v0 env) prec_i prec_o 
		 size_i)
	]
	[ (repair-cast-uint_dsl v0 prec_i prec_o size_i)
		(repair-cast-uint (repair:interpret v0 env) prec_i prec_o 
		 size_i)
	]
	[ (repair-sabsd_dsl v0 v1 prec_i_o size_i_o)
		(repair-sabsd (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-saturate_dsl v0 prec_i prec_o size_i bool_4)
		(repair-saturate (repair:interpret v0 env) prec_i prec_o 
		 size_i bool_4)
	]
	[ (repair-sdiv_dsl v0 v1 prec_i_o size_i_o)
		(repair-sdiv (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-shl_dsl v0 v1 prec_i_o size_i_o)
		(repair-shl (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-smax_dsl v0 v1 prec_i_o size_i_o)
		(repair-smax (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-smin_dsl v0 v1 prec_i_o size_i_o)
		(repair-smin (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-smod_dsl v0 v1 prec_i_o size_i_o)
		(repair-smod (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-smul_dsl v0 v1 prec_i_o size_i_o)
		(repair-smul (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-ssat-add_dsl v0 v1 prec_i_o size_i_o)
		(repair-ssat-add (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-ssat-sub_dsl v0 v1 prec_i_o size_i_o)
		(repair-ssat-sub (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-sshr_dsl v0 v1 prec_i_o size_i_o)
		(repair-sshr (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-sub_dsl v0 v1 prec_i_o size_i_o)
		(repair-sub (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-uabsd_dsl v0 v1 prec_i_o size_i_o)
		(repair-uabsd (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-udiv_dsl v0 v1 prec_i_o size_i_o)
		(repair-udiv (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-umax_dsl v0 v1 prec_i_o size_i_o)
		(repair-umax (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-umin_dsl v0 v1 prec_i_o size_i_o)
		(repair-umin (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-umod_dsl v0 v1 prec_i_o size_i_o)
		(repair-umod (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-umul_dsl v0 v1 prec_i_o size_i_o)
		(repair-umul (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-usat-add_dsl v0 v1 prec_i_o size_i_o)
		(repair-usat-add (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-usat-sub_dsl v0 v1 prec_i_o size_i_o)
		(repair-usat-sub (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-ushr_dsl v0 v1 prec_i_o size_i_o)
		(repair-ushr (repair:interpret v0 env) (repair:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (repair-vector-reduce-add_dsl num_0 v1 size_o size_i)
		(repair-vector-reduce-add num_0 (repair:interpret v1 env) size_o 
		 size_i)
	]
	[v (error "Unrecognized Term in Interpreter" v)]
 )
)
;; ================================================================================

