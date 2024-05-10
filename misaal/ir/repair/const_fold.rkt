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

(require misaal/ir/repair/interpreter)


(provide (all-defined-out))
;; ================================================================================
;;                                DSL Constant Fold Expression
;; ================================================================================
(define (repair:const-fold prog )
 (destruct prog
	[(dim-x id) (dim-x id)]
	[(dim-y id) (dim-y id)]
	[(idx-i id) (idx-i id)]
	[(idx-j id) (idx-j id)]
	[(reg id) (reg id) ]
	[(lit v) (lit v)]
	[(nop v1) (repair:const-fold v1)]
	[(idx-add i1 i2)(idx-add i1 i2) ]
	[(idx-mul i1 i2) (idx-mul i1 i2) ]
	[ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( vector-two-input-swizzle_dsl v0-folded v1-folded num_2 prec_i_o num_4 num_5 num_6 num_7 num_8 ) (vector)))
]
		[else ( vector-two-input-swizzle_dsl v0-folded v1-folded num_2 prec_i_o num_4 num_5 num_6 num_7 num_8 )]
		)
	]
	[ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( interleave-vectors_dsl v0-folded v1-folded size_i_o prec_i_o ) (vector)))
]
		[else ( interleave-vectors_dsl v0-folded v1-folded size_i_o prec_i_o )]
		)
	]
	[ (interleave-vector_dsl v0 size_i_o prec_i_o)
		(define v0-folded (repair:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (repair:interpret ( interleave-vector_dsl v0-folded size_i_o prec_i_o ) (vector)))
]
		[else ( interleave-vector_dsl v0-folded size_i_o prec_i_o )]
		)
	]
	[ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(define v0-folded (repair:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (repair:interpret ( deinterleave-vector_dsl v0-folded size_i_o prec_i_o ) (vector)))
]
		[else ( deinterleave-vector_dsl v0-folded size_i_o prec_i_o )]
		)
	]
	[ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(define v4-folded (repair:const-fold v4))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded) (lit? v4-folded))
(lit (repair:interpret ( llvm_shuffle_vectors_dsl v0-folded v1-folded num_2 prec_i_o v4-folded num_5 ) (vector)))
]
		[else ( llvm_shuffle_vectors_dsl v0-folded v1-folded num_2 prec_i_o v4-folded num_5 )]
		)
	]
	[ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( llvm-vect-add_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-add_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( llvm-vect-sub_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-sub_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( llvm-vect-mul_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-mul_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( llvm-vect-sdiv_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-sdiv_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( llvm-vect-udiv_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-udiv_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-zext_dsl v0 size_i size_o)
		(define v0-folded (repair:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (repair:interpret ( llvm-zext_dsl v0-folded size_i size_o ) (vector)))
]
		[else ( llvm-zext_dsl v0-folded size_i size_o )]
		)
	]
	[ (scalar_splat_dsl v0 size_i size_o)
		(define v0-folded (repair:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (repair:interpret ( scalar_splat_dsl v0-folded size_i size_o ) (vector)))
]
		[else ( scalar_splat_dsl v0-folded size_i size_o )]
		)
	]
	[ (repair-add_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-add_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-add_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-bwand_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-bwand_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-bwand_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-bwnot_dsl v0 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (repair:interpret ( repair-bwnot_dsl v0-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-bwnot_dsl v0-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-bwor_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-bwor_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-bwor_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-cast-int_dsl v0 prec_i prec_o size_i)
		(define v0-folded (repair:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (repair:interpret ( repair-cast-int_dsl v0-folded prec_i prec_o size_i ) (vector)))
]
		[else ( repair-cast-int_dsl v0-folded prec_i prec_o size_i )]
		)
	]
	[ (repair-cast-uint_dsl v0 prec_i prec_o size_i)
		(define v0-folded (repair:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (repair:interpret ( repair-cast-uint_dsl v0-folded prec_i prec_o size_i ) (vector)))
]
		[else ( repair-cast-uint_dsl v0-folded prec_i prec_o size_i )]
		)
	]
	[ (repair-sabsd_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-sabsd_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-sabsd_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-saturate_dsl v0 prec_i prec_o size_i bool_4)
		(define v0-folded (repair:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (repair:interpret ( repair-saturate_dsl v0-folded prec_i prec_o size_i bool_4 ) (vector)))
]
		[else ( repair-saturate_dsl v0-folded prec_i prec_o size_i bool_4 )]
		)
	]
	[ (repair-sdiv_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-sdiv_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-sdiv_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-shl_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-shl_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-shl_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-smax_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-smax_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-smax_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-smin_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-smin_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-smin_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-smod_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-smod_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-smod_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-smul_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-smul_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-smul_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-ssat-add_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-ssat-add_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-ssat-add_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-ssat-sub_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-ssat-sub_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-ssat-sub_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-sshr_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-sshr_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-sshr_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-sub_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-sub_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-sub_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-uabsd_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-uabsd_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-uabsd_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-udiv_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-udiv_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-udiv_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-umax_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-umax_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-umax_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-umin_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-umin_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-umin_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-umod_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-umod_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-umod_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-umul_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-umul_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-umul_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-usat-add_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-usat-add_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-usat-add_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-usat-sub_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-usat-sub_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-usat-sub_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-ushr_dsl v0 v1 prec_i_o size_i_o)
		(define v0-folded (repair:const-fold v0))
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (repair:interpret ( repair-ushr_dsl v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( repair-ushr_dsl v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (repair-vector-reduce-add_dsl num_0 v1 size_o size_i)
		(define v1-folded (repair:const-fold v1))
		(cond
		[(and (lit? v1-folded))
(lit (repair:interpret ( repair-vector-reduce-add_dsl num_0 v1-folded size_o size_i ) (vector)))
]
		[else ( repair-vector-reduce-add_dsl num_0 v1-folded size_o size_i )]
		)
	]
	[v (error "Unrecognized expression" v)]
 )
)
;; ================================================================================

