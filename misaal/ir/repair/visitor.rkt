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



(require hydride/ir/hydride/definition)
(require misaal/ir/repair/definition)


(provide (all-defined-out))
;; ================================================================================
;;                                Hydride Visitor 
;; ================================================================================
(define (repair:visitor prog fn)
 (destruct prog
	[(dim-x id) (fn prog)]
	[(dim-y id) (fn prog)]
	[(idx-i id) (fn prog)]
	[(idx-j id) (fn prog)]
	[(reg id) (fn prog) ]
	[(lit v) (fn prog)]
	[(nop v1) (repair:visitor v1 fn)]
	[(idx-add i1 i2) (fn prog) ]
	[(idx-mul i1 i2) (fn prog) ]
	[ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( vector-two-input-swizzle_dsl v0-visited v1-visited num_2 prec_i_o num_4 num_5 num_6 num_7 num_8 ))
	]
	[ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( interleave-vectors_dsl v0-visited v1-visited size_i_o prec_i_o ))
	]
	[ (interleave-vector_dsl v0 size_i_o prec_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(fn ( interleave-vector_dsl v0-visited size_i_o prec_i_o ))
	]
	[ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(fn ( deinterleave-vector_dsl v0-visited size_i_o prec_i_o ))
	]
	[ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(define v4-visited (repair:visitor v4 fn))
		(fn ( llvm_shuffle_vectors_dsl v0-visited v1-visited num_2 prec_i_o v4-visited num_5 ))
	]
	[ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( llvm-vect-add_dsl v0-visited v1-visited num_2 prec_i_o ))
	]
	[ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( llvm-vect-sub_dsl v0-visited v1-visited num_2 prec_i_o ))
	]
	[ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( llvm-vect-mul_dsl v0-visited v1-visited num_2 prec_i_o ))
	]
	[ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( llvm-vect-sdiv_dsl v0-visited v1-visited num_2 prec_i_o ))
	]
	[ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( llvm-vect-udiv_dsl v0-visited v1-visited num_2 prec_i_o ))
	]
	[ (llvm-zext_dsl v0 size_i size_o)
		(define v0-visited (repair:visitor v0 fn))
		(fn ( llvm-zext_dsl v0-visited size_i size_o ))
	]
	[ (scalar_splat_dsl v0 size_i size_o)
		(define v0-visited (repair:visitor v0 fn))
		(fn ( scalar_splat_dsl v0-visited size_i size_o ))
	]
	[ (repair-add_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-add_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-bwand_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-bwand_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-bwnot_dsl v0 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(fn ( repair-bwnot_dsl v0-visited prec_i_o size_i_o ))
	]
	[ (repair-bwor_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-bwor_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-cast-int_dsl v0 prec_i prec_o size_i)
		(define v0-visited (repair:visitor v0 fn))
		(fn ( repair-cast-int_dsl v0-visited prec_i prec_o size_i ))
	]
	[ (repair-cast-uint_dsl v0 prec_i prec_o size_i)
		(define v0-visited (repair:visitor v0 fn))
		(fn ( repair-cast-uint_dsl v0-visited prec_i prec_o size_i ))
	]
	[ (repair-sabsd_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-sabsd_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-saturate_dsl v0 prec_i prec_o size_i bool_4)
		(define v0-visited (repair:visitor v0 fn))
		(fn ( repair-saturate_dsl v0-visited prec_i prec_o size_i bool_4 ))
	]
	[ (repair-sdiv_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-sdiv_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-shl_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-shl_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-smax_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-smax_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-smin_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-smin_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-smod_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-smod_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-smul_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-smul_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-ssat-add_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-ssat-add_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-ssat-sub_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-ssat-sub_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-sshr_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-sshr_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-sub_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-sub_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-uabsd_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-uabsd_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-udiv_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-udiv_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-umax_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-umax_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-umin_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-umin_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-umod_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-umod_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-umul_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-umul_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-usat-add_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-usat-add_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-usat-sub_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-usat-sub_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-ushr_dsl v0 v1 prec_i_o size_i_o)
		(define v0-visited (repair:visitor v0 fn))
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-ushr_dsl v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (repair-vector-reduce-add_dsl num_0 v1 size_o size_i)
		(define v1-visited (repair:visitor v1 fn))
		(fn ( repair-vector-reduce-add_dsl num_0 v1-visited size_o size_i ))
	]
	[_ (error "Unrecognized expression in visitor")]
 )
)
;; ================================================================================

