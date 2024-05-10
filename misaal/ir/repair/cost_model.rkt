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
(require misaal/ir/repair/definition)


(provide (all-defined-out))
;; ================================================================================
;;                                DSL Cost Model
;; ================================================================================
(define cost_repair-add_dsl 1)
(define cost_repair-bwand_dsl 1)
(define cost_repair-bwnot_dsl 1)
(define cost_repair-bwor_dsl 1)
(define cost_repair-cast-int_dsl 1)
(define cost_repair-cast-uint_dsl 1)
(define cost_repair-sabsd_dsl 1)
(define cost_repair-saturate_dsl 1)
(define cost_repair-sdiv_dsl 1)
(define cost_repair-shl_dsl 1)
(define cost_repair-smax_dsl 1)
(define cost_repair-smin_dsl 1)
(define cost_repair-smod_dsl 1)
(define cost_repair-smul_dsl 1)
(define cost_repair-ssat-add_dsl 1)
(define cost_repair-ssat-sub_dsl 1)
(define cost_repair-sshr_dsl 1)
(define cost_repair-sub_dsl 1)
(define cost_repair-uabsd_dsl 1)
(define cost_repair-udiv_dsl 1)
(define cost_repair-umax_dsl 1)
(define cost_repair-umin_dsl 1)
(define cost_repair-umod_dsl 1)
(define cost_repair-umul_dsl 1)
(define cost_repair-usat-add_dsl 1)
(define cost_repair-usat-sub_dsl 1)
(define cost_repair-ushr_dsl 1)
(define cost_repair-vector-reduce-add_dsl 1)

(define (repair:cost prog)
 (destruct prog
	[(reg id) 1]
	[(lit v) 1 ]
		[ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(+ 4 (repair:cost  v0)  (repair:cost  v1)  
		 
		)
	]
		[ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(+ 4 (repair:cost  v0)  (repair:cost  v1)  
		)
	]
		[ (interleave-vector_dsl v0 size_i_o prec_i_o)
		(+ 3 (repair:cost  v0) )
	]
		[ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(+ 3 (repair:cost  v0) )
	]
		[ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(+ 5 (repair:cost  v0)  (repair:cost  v1)  
		 (repair:cost  v4) )
	]
		[ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (repair:cost  v0)  (repair:cost  v1)  
		)
	]
		[ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (repair:cost  v0)  (repair:cost  v1)  
		)
	]
		[ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (repair:cost  v0)  (repair:cost  v1)  
		)
	]
		[ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (repair:cost  v0)  (repair:cost  v1)  
		)
	]
		[ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (repair:cost  v0)  (repair:cost  v1)  
		)
	]
		[ (llvm-zext_dsl v0 size_i size_o)
		(+ 1 (repair:cost  v0) )
	]
		[ (scalar_splat_dsl v0 size_i size_o)
		(+ 1 (repair:cost  v0) )
	]
	[ (repair-add_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-add_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-bwand_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-bwand_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-bwnot_dsl v0 prec_i_o size_i_o)
		(+ cost_repair-bwnot_dsl (repair:cost  v0) )
	]
	[ (repair-bwor_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-bwor_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-cast-int_dsl v0 prec_i prec_o size_i)
		(+ cost_repair-cast-int_dsl (repair:cost  v0)  
		)
	]
	[ (repair-cast-uint_dsl v0 prec_i prec_o size_i)
		(+ cost_repair-cast-uint_dsl (repair:cost  v0)  
		)
	]
	[ (repair-sabsd_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-sabsd_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-saturate_dsl v0 prec_i prec_o size_i bool_4)
		(+ cost_repair-saturate_dsl (repair:cost  v0)  
		)
	]
	[ (repair-sdiv_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-sdiv_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-shl_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-shl_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-smax_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-smax_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-smin_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-smin_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-smod_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-smod_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-smul_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-smul_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-ssat-add_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-ssat-add_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-ssat-sub_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-ssat-sub_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-sshr_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-sshr_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-sub_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-sub_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-uabsd_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-uabsd_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-udiv_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-udiv_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-umax_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-umax_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-umin_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-umin_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-umod_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-umod_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-umul_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-umul_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-usat-add_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-usat-add_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-usat-sub_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-usat-sub_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-ushr_dsl v0 v1 prec_i_o size_i_o)
		(+ cost_repair-ushr_dsl (repair:cost  v0)  (repair:cost  v1)  
		)
	]
	[ (repair-vector-reduce-add_dsl num_0 v1 size_o size_i)
		(+ cost_repair-vector-reduce-add_dsl (repair:cost  v1)  
		)
	]
	[v  (error "Unrecognized Term in cost model" v)]
 )
)
;; ================================================================================

