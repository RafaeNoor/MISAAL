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
;;                                Hydride Scale Expression 
;; ================================================================================
(define (repair:scale-expr prog scale-factor)
 (destruct prog
	[(reg id) (reg id) ]
	[(lit v) (lit (apply concat (for/list ([i (range scale-factor)]) v) ) )]
	[ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(
		vector-two-input-swizzle_dsl
		(repair:scale-expr v0 scale-factor)
		(repair:scale-expr v1 scale-factor)
		num_2
		prec_i_o
		num_4
		num_5
		num_6
		num_7
		num_8
		)
	]
	[ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(
		interleave-vectors_dsl
		(repair:scale-expr v0 scale-factor)
		(repair:scale-expr v1 scale-factor)
		(* scale-factor size_i_o)
		prec_i_o
		)
	]
	[ (interleave-vector_dsl v0 size_i_o prec_i_o)
		(
		interleave-vector_dsl
		(repair:scale-expr v0 scale-factor)
		(* scale-factor size_i_o)
		prec_i_o
		)
	]
	[ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(
		deinterleave-vector_dsl
		(repair:scale-expr v0 scale-factor)
		(* scale-factor size_i_o)
		prec_i_o
		)
	]
	[ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(
		llvm_shuffle_vectors_dsl
		(repair:scale-expr v0 scale-factor)
		(repair:scale-expr v1 scale-factor)
		num_2
		prec_i_o
		(repair:scale-expr v4 scale-factor)
		num_5
		)
	]
	[ (llvm-zext_dsl v0 size_i size_o)
		(
		llvm-zext_dsl
		(repair:scale-expr v0 scale-factor)
		(* scale-factor size_i)
		(* scale-factor size_o)
		)
	]
	[ (scalar_splat_dsl v0 size_i size_o)
		(
		scalar_splat_dsl
		(repair:scale-expr v0 scale-factor)
		(* scale-factor size_i)
		(* scale-factor size_o)
		)
	]
	[ (repair-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-add_p16_s128_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-add_p16_s256_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-add_p16_s32_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-add_p16_s64_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-add_p32_s128_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-add_p32_s256_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-add_p32_s32_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-add_p32_s64_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-add_p64_s128_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-add_p64_s256_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-add_p64_s64_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-add_p8_s128_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-add_p8_s256_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-add_p8_s32_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-add_p8_s64_signed_None")
(repair-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-bwand_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-bwand_p16_s128_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-bwand_p16_s256_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-bwand_p16_s32_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-bwand_p16_s64_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-bwand_p32_s128_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-bwand_p32_s256_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-bwand_p32_s32_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-bwand_p32_s64_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-bwand_p64_s128_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-bwand_p64_s256_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-bwand_p64_s64_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-bwand_p8_s128_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-bwand_p8_s256_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-bwand_p8_s32_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-bwand_p8_s64_signed_None")
(repair-bwand_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-bwnot_dsl v0 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-bwnot_p16_s128_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-bwnot_p16_s256_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-bwnot_p16_s32_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-bwnot_p16_s64_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-bwnot_p32_s128_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-bwnot_p32_s256_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-bwnot_p32_s32_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-bwnot_p32_s64_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-bwnot_p64_s128_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-bwnot_p64_s256_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-bwnot_p64_s64_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-bwnot_p8_s128_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-bwnot_p8_s256_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-bwnot_p8_s32_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-bwnot_p8_s64_signed_None")
(repair-bwnot_dsl
(repair:scale-expr v0 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-bwor_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-bwor_p16_s128_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-bwor_p16_s256_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-bwor_p16_s32_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-bwor_p16_s64_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-bwor_p32_s128_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-bwor_p32_s256_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-bwor_p32_s32_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-bwor_p32_s64_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-bwor_p64_s128_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-bwor_p64_s256_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-bwor_p64_s64_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-bwor_p8_s128_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-bwor_p8_s256_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-bwor_p8_s32_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-bwor_p8_s64_signed_None")
(repair-bwor_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-sabsd_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-sabsd_p16_s128_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-sabsd_p16_s256_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-sabsd_p16_s32_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-sabsd_p16_s64_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-sabsd_p32_s128_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-sabsd_p32_s256_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-sabsd_p32_s32_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-sabsd_p32_s64_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-sabsd_p64_s128_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-sabsd_p64_s256_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-sabsd_p64_s64_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-sabsd_p8_s128_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-sabsd_p8_s256_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-sabsd_p8_s32_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-sabsd_p8_s64_signed_1")
(repair-sabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-sdiv_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-sdiv_p16_s128_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-sdiv_p16_s256_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-sdiv_p16_s32_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-sdiv_p16_s64_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-sdiv_p32_s128_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-sdiv_p32_s256_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-sdiv_p32_s32_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-sdiv_p32_s64_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-sdiv_p64_s128_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-sdiv_p64_s256_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-sdiv_p64_s64_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-sdiv_p8_s128_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-sdiv_p8_s256_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-sdiv_p8_s32_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-sdiv_p8_s64_signed_1")
(repair-sdiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-shl_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-shl_p16_s128_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-shl_p16_s256_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-shl_p16_s32_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-shl_p16_s64_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-shl_p32_s128_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-shl_p32_s256_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-shl_p32_s32_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-shl_p32_s64_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-shl_p64_s128_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-shl_p64_s256_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-shl_p64_s64_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-shl_p8_s128_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-shl_p8_s256_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-shl_p8_s32_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-shl_p8_s64_signed_None")
(repair-shl_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-smax_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-smax_p16_s128_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-smax_p16_s256_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-smax_p16_s32_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-smax_p16_s64_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-smax_p32_s128_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-smax_p32_s256_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-smax_p32_s32_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-smax_p32_s64_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-smax_p64_s128_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-smax_p64_s256_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-smax_p64_s64_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-smax_p8_s128_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-smax_p8_s256_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-smax_p8_s32_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-smax_p8_s64_signed_1")
(repair-smax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-smin_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-smin_p16_s128_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-smin_p16_s256_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-smin_p16_s32_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-smin_p16_s64_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-smin_p32_s128_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-smin_p32_s256_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-smin_p32_s32_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-smin_p32_s64_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-smin_p64_s128_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-smin_p64_s256_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-smin_p64_s64_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-smin_p8_s128_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-smin_p8_s256_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-smin_p8_s32_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-smin_p8_s64_signed_1")
(repair-smin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-smod_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-smod_p16_s128_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-smod_p16_s256_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-smod_p16_s32_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-smod_p16_s64_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-smod_p32_s128_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-smod_p32_s256_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-smod_p32_s32_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-smod_p32_s64_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-smod_p64_s128_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-smod_p64_s256_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-smod_p64_s64_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-smod_p8_s128_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-smod_p8_s256_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-smod_p8_s32_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-smod_p8_s64_signed_1")
(repair-smod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-smul_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-smul_p16_s128_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-smul_p16_s256_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-smul_p16_s32_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-smul_p16_s64_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-smul_p32_s128_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-smul_p32_s256_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-smul_p32_s32_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-smul_p32_s64_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-smul_p64_s128_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-smul_p64_s256_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-smul_p64_s64_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-smul_p8_s128_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-smul_p8_s256_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-smul_p8_s32_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-smul_p8_s64_signed_1")
(repair-smul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-ssat-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-ssat-add_p16_s128_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-ssat-add_p16_s256_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-ssat-add_p16_s32_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-ssat-add_p16_s64_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-ssat-add_p32_s128_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-ssat-add_p32_s256_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-ssat-add_p32_s32_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-ssat-add_p32_s64_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-ssat-add_p64_s128_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-ssat-add_p64_s256_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-ssat-add_p64_s64_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-ssat-add_p8_s128_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-ssat-add_p8_s256_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-ssat-add_p8_s32_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-ssat-add_p8_s64_signed_1")
(repair-ssat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-ssat-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-ssat-sub_p16_s128_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-ssat-sub_p16_s256_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-ssat-sub_p16_s32_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-ssat-sub_p16_s64_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-ssat-sub_p32_s128_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-ssat-sub_p32_s256_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-ssat-sub_p32_s32_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-ssat-sub_p32_s64_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-ssat-sub_p64_s128_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-ssat-sub_p64_s256_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-ssat-sub_p64_s64_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-ssat-sub_p8_s128_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-ssat-sub_p8_s256_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-ssat-sub_p8_s32_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-ssat-sub_p8_s64_signed_1")
(repair-ssat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-sshr_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-sshr_p16_s128_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-sshr_p16_s256_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-sshr_p16_s32_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-sshr_p16_s64_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-sshr_p32_s128_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-sshr_p32_s256_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-sshr_p32_s32_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-sshr_p32_s64_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-sshr_p64_s128_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-sshr_p64_s256_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-sshr_p64_s64_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-sshr_p8_s128_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-sshr_p8_s256_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-sshr_p8_s32_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-sshr_p8_s64_signed_1")
(repair-sshr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-sub_p16_s128_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-sub_p16_s256_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-sub_p16_s32_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-sub_p16_s64_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-sub_p32_s128_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-sub_p32_s256_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-sub_p32_s32_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-sub_p32_s64_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-sub_p64_s128_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-sub_p64_s256_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-sub_p64_s64_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-sub_p8_s128_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-sub_p8_s256_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-sub_p8_s32_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-sub_p8_s64_signed_None")
(repair-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-uabsd_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-uabsd_p16_s128_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-uabsd_p16_s256_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-uabsd_p16_s32_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-uabsd_p16_s64_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-uabsd_p32_s128_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-uabsd_p32_s256_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-uabsd_p32_s32_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-uabsd_p32_s64_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-uabsd_p64_s128_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-uabsd_p64_s256_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-uabsd_p64_s64_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-uabsd_p8_s128_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-uabsd_p8_s256_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-uabsd_p8_s32_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-uabsd_p8_s64_signed_0")
(repair-uabsd_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-udiv_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-udiv_p16_s128_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-udiv_p16_s256_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-udiv_p16_s32_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-udiv_p16_s64_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-udiv_p32_s128_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-udiv_p32_s256_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-udiv_p32_s32_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-udiv_p32_s64_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-udiv_p64_s128_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-udiv_p64_s256_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-udiv_p64_s64_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-udiv_p8_s128_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-udiv_p8_s256_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-udiv_p8_s32_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-udiv_p8_s64_signed_0")
(repair-udiv_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-umax_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-umax_p16_s128_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-umax_p16_s256_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-umax_p16_s32_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-umax_p16_s64_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-umax_p32_s128_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-umax_p32_s256_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-umax_p32_s32_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-umax_p32_s64_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-umax_p64_s128_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-umax_p64_s256_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-umax_p64_s64_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-umax_p8_s128_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-umax_p8_s256_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-umax_p8_s32_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-umax_p8_s64_signed_0")
(repair-umax_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-umin_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-umin_p16_s128_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-umin_p16_s256_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-umin_p16_s32_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-umin_p16_s64_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-umin_p32_s128_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-umin_p32_s256_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-umin_p32_s32_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-umin_p32_s64_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-umin_p64_s128_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-umin_p64_s256_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-umin_p64_s64_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-umin_p8_s128_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-umin_p8_s256_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-umin_p8_s32_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-umin_p8_s64_signed_0")
(repair-umin_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-umod_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-umod_p16_s128_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-umod_p16_s256_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-umod_p16_s32_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-umod_p16_s64_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-umod_p32_s128_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-umod_p32_s256_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-umod_p32_s32_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-umod_p32_s64_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-umod_p64_s128_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-umod_p64_s256_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-umod_p64_s64_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-umod_p8_s128_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-umod_p8_s256_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-umod_p8_s32_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-umod_p8_s64_signed_0")
(repair-umod_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-umul_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-umul_p16_s128_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-umul_p16_s256_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-umul_p16_s32_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-umul_p16_s64_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-umul_p32_s128_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-umul_p32_s256_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-umul_p32_s32_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-umul_p32_s64_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-umul_p64_s128_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-umul_p64_s256_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-umul_p64_s64_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-umul_p8_s128_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-umul_p8_s256_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-umul_p8_s32_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-umul_p8_s64_signed_0")
(repair-umul_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-usat-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-usat-add_p16_s128_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-usat-add_p16_s256_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-usat-add_p16_s32_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-usat-add_p16_s64_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-usat-add_p32_s128_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-usat-add_p32_s256_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-usat-add_p32_s32_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-usat-add_p32_s64_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-usat-add_p64_s128_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-usat-add_p64_s256_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-usat-add_p64_s64_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-usat-add_p8_s128_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-usat-add_p8_s256_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-usat-add_p8_s32_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-usat-add_p8_s64_signed_0")
(repair-usat-add_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-usat-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-usat-sub_p16_s128_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-usat-sub_p16_s256_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-usat-sub_p16_s32_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-usat-sub_p16_s64_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-usat-sub_p32_s128_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-usat-sub_p32_s256_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-usat-sub_p32_s32_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-usat-sub_p32_s64_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-usat-sub_p64_s128_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-usat-sub_p64_s256_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-usat-sub_p64_s64_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-usat-sub_p8_s128_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-usat-sub_p8_s256_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-usat-sub_p8_s32_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-usat-sub_p8_s64_signed_0")
(repair-usat-sub_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-ushr_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4))
(displayln "Scaling case for repair-ushr_p16_s128_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 8))
(displayln "Scaling case for repair-ushr_p16_s256_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1))
(displayln "Scaling case for repair-ushr_p16_s32_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2))
(displayln "Scaling case for repair-ushr_p16_s64_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4))
(displayln "Scaling case for repair-ushr_p32_s128_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 8))
(displayln "Scaling case for repair-ushr_p32_s256_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1))
(displayln "Scaling case for repair-ushr_p32_s32_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2))
(displayln "Scaling case for repair-ushr_p32_s64_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4))
(displayln "Scaling case for repair-ushr_p64_s128_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 8))
(displayln "Scaling case for repair-ushr_p64_s256_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2))
(displayln "Scaling case for repair-ushr_p64_s64_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4))
(displayln "Scaling case for repair-ushr_p8_s128_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8))
(displayln "Scaling case for repair-ushr_p8_s256_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1))
(displayln "Scaling case for repair-ushr_p8_s32_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2))
(displayln "Scaling case for repair-ushr_p8_s64_signed_0")
(repair-ushr_dsl
(repair:scale-expr v0 scale-factor)
(repair:scale-expr v1 scale-factor)
prec_i_o
(* scale-factor size_i_o)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[ (repair-vector-reduce-add_dsl num_0 v1 size_o size_i)
		(cond 
		[(and  (equal? num_0 2) (equal? size_o 0) (equal? size_i 1))
(displayln "Scaling case for repair-vector-reduce-add_p16_s32_signed_None")
(repair-vector-reduce-add_dsl
num_0
(repair:scale-expr v1 scale-factor)
(* scale-factor size_o)
(* scale-factor size_i)
)
]
		[(and  (equal? num_0 4) (equal? size_o 0) (equal? size_i 2))
(displayln "Scaling case for repair-vector-reduce-add_p16_s64_signed_None")
(repair-vector-reduce-add_dsl
num_0
(repair:scale-expr v1 scale-factor)
(* scale-factor size_o)
(* scale-factor size_i)
)
]
		[(and  (equal? num_0 4) (equal? size_o 1) (equal? size_i 4))
(displayln "Scaling case for repair-vector-reduce-add_p32_s128_signed_None")
(repair-vector-reduce-add_dsl
num_0
(repair:scale-expr v1 scale-factor)
(* scale-factor size_o)
(* scale-factor size_i)
)
]
		[(and  (equal? num_0 2) (equal? size_o 1) (equal? size_i 2))
(displayln "Scaling case for repair-vector-reduce-add_p32_s64_signed_None")
(repair-vector-reduce-add_dsl
num_0
(repair:scale-expr v1 scale-factor)
(* scale-factor size_o)
(* scale-factor size_i)
)
]
		[(and  (equal? num_0 2) (equal? size_o 2) (equal? size_i 4))
(displayln "Scaling case for repair-vector-reduce-add_p64_s128_signed_None")
(repair-vector-reduce-add_dsl
num_0
(repair:scale-expr v1 scale-factor)
(* scale-factor size_o)
(* scale-factor size_i)
)
]
		[(and  (equal? num_0 4) (equal? size_o 2) (equal? size_i 8))
(displayln "Scaling case for repair-vector-reduce-add_p64_s256_signed_None")
(repair-vector-reduce-add_dsl
num_0
(repair:scale-expr v1 scale-factor)
(* scale-factor size_o)
(* scale-factor size_i)
)
]
		[(and  (equal? num_0 4) (equal? size_o 0) (equal? size_i 1))
(displayln "Scaling case for repair-vector-reduce-add_p8_s32_signed_None")
(repair-vector-reduce-add_dsl
num_0
(repair:scale-expr v1 scale-factor)
(* scale-factor size_o)
(* scale-factor size_i)
)
]
		[else (error "Unable to identify how to scale up " prog)]
		)
	]
	[_ (error "Unrecognized expression")]
 )
)
;; ================================================================================

