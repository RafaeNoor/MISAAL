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
(require rosette/solver/smt/boolector)

(require hydride/utils/bvops)
(require hydride/utils/misc)


(require hydride/ir/hydride/definition)

(require misaal/ir/repair/semantics)
(require misaal/ir/repair/definition)
(require misaal/ir/repair/length)


(provide (all-defined-out))
;; ================================================================================
;;                                DSL Binder
;; ================================================================================
(define (repair:bind-expr prog env)
 (destruct prog
	[(dim-x id) (dim-x id)]
	[(dim-y id) (dim-y id)]
	[(idx-i id) (idx-i id)]
	[(idx-j id) (idx-j id)]
	[(reg id) (vector-ref-bv env id)]
	[(lit v) (lit v)]
	[(idx-add i1 i2) (idx-add i1 i2)]
	[(idx-mul i1 i2) (idx-mul i1 i2)]
	[ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(vector-two-input-swizzle_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr num_2 env) 
		 (repair:bind-expr prec_i_o env) (repair:bind-expr num_4 env) (repair:bind-expr num_5 env) 
		 (repair:bind-expr num_6 env) (repair:bind-expr num_7 env) (repair:bind-expr num_8 env))
	]
	[ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(interleave-vectors_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr size_i_o env) 
		 (repair:bind-expr prec_i_o env))
	]
	[ (interleave-vector_dsl v0 size_i_o prec_i_o)
		(interleave-vector_dsl (repair:bind-expr v0 env) (repair:bind-expr size_i_o env) (repair:bind-expr prec_i_o env))
	]
	[ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(deinterleave-vector_dsl (repair:bind-expr v0 env) (repair:bind-expr size_i_o env) (repair:bind-expr prec_i_o env))
	]
	[ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(llvm_shuffle_vectors_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr num_2 env) 
		 (repair:bind-expr prec_i_o env) (repair:bind-expr v4 env) (repair:bind-expr num_5 env))
	]
	[ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-add_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr num_2 env) 
		 (repair:bind-expr prec_i_o env))
	]
	[ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-sub_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr num_2 env) 
		 (repair:bind-expr prec_i_o env))
	]
	[ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-mul_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr num_2 env) 
		 (repair:bind-expr prec_i_o env))
	]
	[ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-sdiv_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr num_2 env) 
		 (repair:bind-expr prec_i_o env))
	]
	[ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-udiv_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr num_2 env) 
		 (repair:bind-expr prec_i_o env))
	]
	[ (llvm-zext_dsl v0 size_i size_o)
		(llvm-zext_dsl (repair:bind-expr v0 env) (repair:bind-expr size_i env) (repair:bind-expr size_o env))
	]
	[ (scalar_splat_dsl v0 size_i size_o)
		(scalar_splat_dsl (repair:bind-expr v0 env) (repair:bind-expr size_i env) (repair:bind-expr size_o env))
	]
	[ (repair-add_dsl v0 v1 prec_i_o size_i_o)
		(repair-add_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-bwand_dsl v0 v1 prec_i_o size_i_o)
		(repair-bwand_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-bwnot_dsl v0 prec_i_o size_i_o)
		(repair-bwnot_dsl (repair:bind-expr v0 env) (repair:bind-expr prec_i_o env) (repair:bind-expr size_i_o env))
	]
	[ (repair-bwor_dsl v0 v1 prec_i_o size_i_o)
		(repair-bwor_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-cast-int_dsl v0 prec_i prec_o size_i)
		(repair-cast-int_dsl (repair:bind-expr v0 env) (repair:bind-expr prec_i env) (repair:bind-expr prec_o env) 
		 (repair:bind-expr size_i env))
	]
	[ (repair-cast-uint_dsl v0 prec_i prec_o size_i)
		(repair-cast-uint_dsl (repair:bind-expr v0 env) (repair:bind-expr prec_i env) (repair:bind-expr prec_o env) 
		 (repair:bind-expr size_i env))
	]
	[ (repair-sabsd_dsl v0 v1 prec_i_o size_i_o)
		(repair-sabsd_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-saturate_dsl v0 prec_i prec_o size_i bool_4)
		(repair-saturate_dsl (repair:bind-expr v0 env) (repair:bind-expr prec_i env) (repair:bind-expr prec_o env) 
		 (repair:bind-expr size_i env) (repair:bind-expr bool_4 env))
	]
	[ (repair-sdiv_dsl v0 v1 prec_i_o size_i_o)
		(repair-sdiv_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-shl_dsl v0 v1 prec_i_o size_i_o)
		(repair-shl_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-smax_dsl v0 v1 prec_i_o size_i_o)
		(repair-smax_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-smin_dsl v0 v1 prec_i_o size_i_o)
		(repair-smin_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-smod_dsl v0 v1 prec_i_o size_i_o)
		(repair-smod_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-smul_dsl v0 v1 prec_i_o size_i_o)
		(repair-smul_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-ssat-add_dsl v0 v1 prec_i_o size_i_o)
		(repair-ssat-add_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-ssat-sub_dsl v0 v1 prec_i_o size_i_o)
		(repair-ssat-sub_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-sshr_dsl v0 v1 prec_i_o size_i_o)
		(repair-sshr_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-sub_dsl v0 v1 prec_i_o size_i_o)
		(repair-sub_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-uabsd_dsl v0 v1 prec_i_o size_i_o)
		(repair-uabsd_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-udiv_dsl v0 v1 prec_i_o size_i_o)
		(repair-udiv_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-umax_dsl v0 v1 prec_i_o size_i_o)
		(repair-umax_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-umin_dsl v0 v1 prec_i_o size_i_o)
		(repair-umin_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-umod_dsl v0 v1 prec_i_o size_i_o)
		(repair-umod_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-umul_dsl v0 v1 prec_i_o size_i_o)
		(repair-umul_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-usat-add_dsl v0 v1 prec_i_o size_i_o)
		(repair-usat-add_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-usat-sub_dsl v0 v1 prec_i_o size_i_o)
		(repair-usat-sub_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-ushr_dsl v0 v1 prec_i_o size_i_o)
		(repair-ushr_dsl (repair:bind-expr v0 env) (repair:bind-expr v1 env) (repair:bind-expr prec_i_o env) 
		 (repair:bind-expr size_i_o env))
	]
	[ (repair-vector-reduce-add_dsl num_0 v1 size_o size_i)
		(repair-vector-reduce-add_dsl (repair:bind-expr num_0 env) (repair:bind-expr v1 env) (repair:bind-expr size_o env) 
		 (repair:bind-expr size_i env))
	]
	[v v]
 )
)
;; ================================================================================

