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
;;                                DSL Get Ops
;; ================================================================================
(define (repair:get-bv-ops prog)
 (destruct prog
	[(reg id) '()]
	[(lit v) '()]
		[(vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(remove-duplicates (append (list  'if) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))
	]
		[(interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(remove-duplicates (append (list  ) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))
	]
		[(interleave-vector_dsl v0 size_i_o prec_i_o)
		(remove-duplicates (append (list  'cond) (repair:get-bv-ops v0)))
	]
		[(deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(remove-duplicates (append (list  'cond) (repair:get-bv-ops v0)))
	]
		[(llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(remove-duplicates (append (list  'if 'bitvector->integer) (repair:get-bv-ops v0) (repair:get-bv-ops v1) (repair:get-bv-ops v4)))
	]
		[(llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvadd) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))
	]
		[(llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvsub) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))
	]
		[(llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvmul) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))
	]
		[(llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvsdiv) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))
	]
		[(llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvudiv) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))
	]
		[(llvm-zext_dsl v0 size_i size_o)
		(remove-duplicates (append (list  'zero-extend) (repair:get-bv-ops v0)))
	]
		[(scalar_splat_dsl v0 size_i size_o)
		(remove-duplicates (append (list  'zero-extend) (repair:get-bv-ops v0)))
	]
	[(repair-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-add_p16_s128_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-add_p16_s16_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-add_p16_s256_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-add_p16_s32_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-add_p16_s64_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-add_p32_s128_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-add_p32_s256_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-add_p32_s32_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-add_p32_s64_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-add_p64_s128_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-add_p64_s256_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-add_p64_s64_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-add_p8_s128_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-add_p8_s16_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-add_p8_s256_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-add_p8_s32_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-add_p8_s64_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-add_p8_s8_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-add")]
)

	]
	[(repair-bwand_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-bwand_p16_s128_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-bwand_p16_s16_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-bwand_p16_s256_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-bwand_p16_s32_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-bwand_p16_s64_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-bwand_p32_s128_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-bwand_p32_s256_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-bwand_p32_s32_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-bwand_p32_s64_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-bwand_p64_s128_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-bwand_p64_s256_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-bwand_p64_s64_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-bwand_p8_s128_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-bwand_p8_s16_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-bwand_p8_s256_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-bwand_p8_s32_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-bwand_p8_s64_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-bwand_p8_s8_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-bwand")]
)

	]
	[(repair-bwnot_dsl v0 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-bwnot_p16_s128_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-bwnot_p16_s16_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-bwnot_p16_s256_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-bwnot_p16_s32_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-bwnot_p16_s64_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-bwnot_p32_s128_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-bwnot_p32_s256_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-bwnot_p32_s32_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-bwnot_p32_s64_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-bwnot_p64_s128_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-bwnot_p64_s256_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-bwnot_p64_s64_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-bwnot_p8_s128_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-bwnot_p8_s16_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-bwnot_p8_s256_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-bwnot_p8_s32_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-bwnot_p8_s64_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-bwnot_p8_s8_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (repair:get-bv-ops v0)))]
		[else (error "Unable to get ops  for repair-bwnot")]
)

	]
	[(repair-bwor_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-bwor_p16_s128_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-bwor_p16_s16_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-bwor_p16_s256_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-bwor_p16_s32_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-bwor_p16_s64_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-bwor_p32_s128_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-bwor_p32_s256_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-bwor_p32_s32_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-bwor_p32_s64_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-bwor_p64_s128_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-bwor_p64_s256_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-bwor_p64_s64_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-bwor_p8_s128_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-bwor_p8_s16_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-bwor_p8_s256_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-bwor_p8_s32_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-bwor_p8_s64_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-bwor_p8_s8_signed_None
 
  (remove-duplicates (append (list  'bvor 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-bwor")]
)

	]
	[(repair-cast-int_dsl v0 prec_i prec_o size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 128)); repair-cast-int_ip16_is128_op32_os256_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)); repair-cast-int_ip16_is128_op8_os64_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 16)); repair-cast-int_ip16_is16_op32_os32_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)); repair-cast-int_ip16_is16_op8_os8_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)); repair-cast-int_ip16_is256_op8_os128_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 32)); repair-cast-int_ip16_is32_op32_os64_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)); repair-cast-int_ip16_is32_op8_os16_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 64)); repair-cast-int_ip16_is64_op32_os128_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)); repair-cast-int_ip16_is64_op8_os32_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)); repair-cast-int_ip32_is128_op16_os64_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 128)); repair-cast-int_ip32_is128_op64_os256_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)); repair-cast-int_ip32_is256_op16_os128_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)); repair-cast-int_ip32_is32_op16_os16_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 32)); repair-cast-int_ip32_is32_op64_os64_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)); repair-cast-int_ip32_is64_op16_os32_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 64)); repair-cast-int_ip32_is64_op64_os128_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)); repair-cast-int_ip64_is128_op32_os64_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)); repair-cast-int_ip64_is256_op32_os128_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)); repair-cast-int_ip64_is64_op32_os32_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 128)); repair-cast-int_ip8_is128_op16_os256_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 16)); repair-cast-int_ip8_is16_op16_os32_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 32)); repair-cast-int_ip8_is32_op16_os64_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 64)); repair-cast-int_ip8_is64_op16_os128_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 8)); repair-cast-int_ip8_is8_op16_os16_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (repair:get-bv-ops v0)))]
		[else (error "Unable to get ops  for repair-cast-int")]
)

	]
	[(repair-cast-uint_dsl v0 prec_i prec_o size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 128)); repair-cast-uint_ip16_is128_op32_os256_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)); repair-cast-uint_ip16_is128_op8_os64_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 16)); repair-cast-uint_ip16_is16_op32_os32_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)); repair-cast-uint_ip16_is16_op8_os8_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)); repair-cast-uint_ip16_is256_op8_os128_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 32)); repair-cast-uint_ip16_is32_op32_os64_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)); repair-cast-uint_ip16_is32_op8_os16_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 64)); repair-cast-uint_ip16_is64_op32_os128_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)); repair-cast-uint_ip16_is64_op8_os32_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)); repair-cast-uint_ip32_is128_op16_os64_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 128)); repair-cast-uint_ip32_is128_op64_os256_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)); repair-cast-uint_ip32_is256_op16_os128_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)); repair-cast-uint_ip32_is32_op16_os16_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 32)); repair-cast-uint_ip32_is32_op64_os64_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)); repair-cast-uint_ip32_is64_op16_os32_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 64)); repair-cast-uint_ip32_is64_op64_os128_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)); repair-cast-uint_ip64_is128_op32_os64_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)); repair-cast-uint_ip64_is256_op32_os128_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)); repair-cast-uint_ip64_is64_op32_os32_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 128)); repair-cast-uint_ip8_is128_op16_os256_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 16)); repair-cast-uint_ip8_is16_op16_os32_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 32)); repair-cast-uint_ip8_is32_op16_os64_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 64)); repair-cast-uint_ip8_is64_op16_os128_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 8)); repair-cast-uint_ip8_is8_op16_os16_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (repair:get-bv-ops v0)))]
		[else (error "Unable to get ops  for repair-cast-uint")]
)

	]
	[(repair-sabsd_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-sabsd_p16_s128_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-sabsd_p16_s16_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-sabsd_p16_s256_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-sabsd_p16_s32_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-sabsd_p16_s64_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-sabsd_p32_s128_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-sabsd_p32_s256_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-sabsd_p32_s32_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-sabsd_p32_s64_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-sabsd_p64_s128_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-sabsd_p64_s256_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-sabsd_p64_s64_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-sabsd_p8_s128_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-sabsd_p8_s16_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-sabsd_p8_s256_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-sabsd_p8_s32_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-sabsd_p8_s64_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-sabsd_p8_s8_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-sabsd")]
)

	]
	[(repair-saturate_dsl v0 prec_i prec_o size_i bool_4)
		(cond 
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)); repair-saturate_ip16_is128_op8_os64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)); repair-saturate_ip16_is128_op8_os64_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)); repair-saturate_ip16_is16_op8_os8_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)); repair-saturate_ip16_is16_op8_os8_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)); repair-saturate_ip16_is256_op8_os128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)); repair-saturate_ip16_is256_op8_os128_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)); repair-saturate_ip16_is32_op8_os16_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)); repair-saturate_ip16_is32_op8_os16_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)); repair-saturate_ip16_is64_op8_os32_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)); repair-saturate_ip16_is64_op8_os32_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)); repair-saturate_ip32_is128_op16_os64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)); repair-saturate_ip32_is128_op16_os64_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)); repair-saturate_ip32_is256_op16_os128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)); repair-saturate_ip32_is256_op16_os128_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)); repair-saturate_ip32_is32_op16_os16_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)); repair-saturate_ip32_is32_op16_os16_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)); repair-saturate_ip32_is64_op16_os32_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)); repair-saturate_ip32_is64_op16_os32_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)); repair-saturate_ip64_is128_op32_os64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)); repair-saturate_ip64_is128_op32_os64_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)); repair-saturate_ip64_is256_op32_os128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)); repair-saturate_ip64_is256_op32_os128_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)); repair-saturate_ip64_is64_op32_os32_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (repair:get-bv-ops v0)))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)); repair-saturate_ip64_is64_op32_os32_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (repair:get-bv-ops v0)))]
		[else (error "Unable to get ops  for repair-saturate")]
)

	]
	[(repair-sdiv_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-sdiv_p16_s128_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-sdiv_p16_s16_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-sdiv_p16_s256_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-sdiv_p16_s32_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-sdiv_p16_s64_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-sdiv_p32_s128_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-sdiv_p32_s256_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-sdiv_p32_s32_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-sdiv_p32_s64_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-sdiv_p64_s128_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-sdiv_p64_s256_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-sdiv_p64_s64_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-sdiv_p8_s128_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-sdiv_p8_s16_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-sdiv_p8_s256_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-sdiv_p8_s32_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-sdiv_p8_s64_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-sdiv_p8_s8_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-sdiv")]
)

	]
	[(repair-shl_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-shl_p16_s128_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-shl_p16_s16_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-shl_p16_s256_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-shl_p16_s32_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-shl_p16_s64_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-shl_p32_s128_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-shl_p32_s256_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-shl_p32_s32_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-shl_p32_s64_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-shl_p64_s128_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-shl_p64_s256_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-shl_p64_s64_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-shl_p8_s128_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-shl_p8_s16_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-shl_p8_s256_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-shl_p8_s32_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-shl_p8_s64_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-shl_p8_s8_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-shl")]
)

	]
	[(repair-smax_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-smax_p16_s128_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-smax_p16_s16_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-smax_p16_s256_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-smax_p16_s32_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-smax_p16_s64_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-smax_p32_s128_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-smax_p32_s256_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-smax_p32_s32_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-smax_p32_s64_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-smax_p64_s128_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-smax_p64_s256_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-smax_p64_s64_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-smax_p8_s128_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-smax_p8_s16_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-smax_p8_s256_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-smax_p8_s32_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-smax_p8_s64_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-smax_p8_s8_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-smax")]
)

	]
	[(repair-smin_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-smin_p16_s128_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-smin_p16_s16_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-smin_p16_s256_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-smin_p16_s32_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-smin_p16_s64_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-smin_p32_s128_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-smin_p32_s256_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-smin_p32_s32_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-smin_p32_s64_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-smin_p64_s128_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-smin_p64_s256_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-smin_p64_s64_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-smin_p8_s128_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-smin_p8_s16_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-smin_p8_s256_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-smin_p8_s32_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-smin_p8_s64_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-smin_p8_s8_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-smin")]
)

	]
	[(repair-smod_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-smod_p16_s128_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-smod_p16_s16_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-smod_p16_s256_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-smod_p16_s32_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-smod_p16_s64_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-smod_p32_s128_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-smod_p32_s256_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-smod_p32_s32_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-smod_p32_s64_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-smod_p64_s128_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-smod_p64_s256_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-smod_p64_s64_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-smod_p8_s128_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-smod_p8_s16_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-smod_p8_s256_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-smod_p8_s32_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-smod_p8_s64_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-smod_p8_s8_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-smod")]
)

	]
	[(repair-smul_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-smul_p16_s128_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-smul_p16_s16_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-smul_p16_s256_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-smul_p16_s32_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-smul_p16_s64_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-smul_p32_s128_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-smul_p32_s256_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-smul_p32_s32_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-smul_p32_s64_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-smul_p64_s128_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-smul_p64_s256_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-smul_p64_s64_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-smul_p8_s128_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-smul_p8_s16_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-smul_p8_s256_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-smul_p8_s32_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-smul_p8_s64_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-smul_p8_s8_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-smul")]
)

	]
	[(repair-ssat-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-ssat-add_p16_s128_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-ssat-add_p16_s16_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-ssat-add_p16_s256_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-ssat-add_p16_s32_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-ssat-add_p16_s64_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-ssat-add_p32_s128_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-ssat-add_p32_s256_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-ssat-add_p32_s32_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-ssat-add_p32_s64_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-ssat-add_p64_s128_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-ssat-add_p64_s256_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-ssat-add_p64_s64_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-ssat-add_p8_s128_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-ssat-add_p8_s16_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-ssat-add_p8_s256_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-ssat-add_p8_s32_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-ssat-add_p8_s64_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-ssat-add_p8_s8_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-ssat-add")]
)

	]
	[(repair-ssat-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-ssat-sub_p16_s128_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-ssat-sub_p16_s16_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-ssat-sub_p16_s256_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-ssat-sub_p16_s32_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-ssat-sub_p16_s64_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-ssat-sub_p32_s128_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-ssat-sub_p32_s256_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-ssat-sub_p32_s32_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-ssat-sub_p32_s64_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-ssat-sub_p64_s128_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-ssat-sub_p64_s256_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-ssat-sub_p64_s64_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-ssat-sub_p8_s128_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-ssat-sub_p8_s16_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-ssat-sub_p8_s256_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-ssat-sub_p8_s32_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-ssat-sub_p8_s64_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-ssat-sub_p8_s8_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-ssat-sub")]
)

	]
	[(repair-sshr_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-sshr_p16_s128_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-sshr_p16_s16_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-sshr_p16_s256_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-sshr_p16_s32_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-sshr_p16_s64_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-sshr_p32_s128_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-sshr_p32_s256_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-sshr_p32_s32_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-sshr_p32_s64_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-sshr_p64_s128_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-sshr_p64_s256_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-sshr_p64_s64_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-sshr_p8_s128_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-sshr_p8_s16_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-sshr_p8_s256_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-sshr_p8_s32_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-sshr_p8_s64_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-sshr_p8_s8_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-sshr")]
)

	]
	[(repair-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-sub_p16_s128_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-sub_p16_s16_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-sub_p16_s256_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-sub_p16_s32_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-sub_p16_s64_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-sub_p32_s128_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-sub_p32_s256_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-sub_p32_s32_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-sub_p32_s64_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-sub_p64_s128_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-sub_p64_s256_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-sub_p64_s64_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-sub_p8_s128_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-sub_p8_s16_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-sub_p8_s256_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-sub_p8_s32_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-sub_p8_s64_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-sub_p8_s8_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-sub")]
)

	]
	[(repair-uabsd_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-uabsd_p16_s128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-uabsd_p16_s16_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-uabsd_p16_s256_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-uabsd_p16_s32_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-uabsd_p16_s64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-uabsd_p32_s128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-uabsd_p32_s256_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-uabsd_p32_s32_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-uabsd_p32_s64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-uabsd_p64_s128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-uabsd_p64_s256_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-uabsd_p64_s64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-uabsd_p8_s128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-uabsd_p8_s16_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-uabsd_p8_s256_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-uabsd_p8_s32_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-uabsd_p8_s64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-uabsd_p8_s8_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-uabsd")]
)

	]
	[(repair-udiv_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-udiv_p16_s128_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-udiv_p16_s16_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-udiv_p16_s256_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-udiv_p16_s32_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-udiv_p16_s64_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-udiv_p32_s128_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-udiv_p32_s256_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-udiv_p32_s32_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-udiv_p32_s64_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-udiv_p64_s128_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-udiv_p64_s256_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-udiv_p64_s64_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-udiv_p8_s128_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-udiv_p8_s16_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-udiv_p8_s256_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-udiv_p8_s32_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-udiv_p8_s64_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-udiv_p8_s8_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-udiv")]
)

	]
	[(repair-umax_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-umax_p16_s128_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-umax_p16_s16_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-umax_p16_s256_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-umax_p16_s32_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-umax_p16_s64_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-umax_p32_s128_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-umax_p32_s256_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-umax_p32_s32_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-umax_p32_s64_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-umax_p64_s128_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-umax_p64_s256_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-umax_p64_s64_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-umax_p8_s128_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-umax_p8_s16_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-umax_p8_s256_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-umax_p8_s32_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-umax_p8_s64_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-umax_p8_s8_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-umax")]
)

	]
	[(repair-umin_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-umin_p16_s128_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-umin_p16_s16_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-umin_p16_s256_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-umin_p16_s32_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-umin_p16_s64_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-umin_p32_s128_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-umin_p32_s256_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-umin_p32_s32_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-umin_p32_s64_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-umin_p64_s128_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-umin_p64_s256_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-umin_p64_s64_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-umin_p8_s128_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-umin_p8_s16_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-umin_p8_s256_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-umin_p8_s32_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-umin_p8_s64_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-umin_p8_s8_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-umin")]
)

	]
	[(repair-umod_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-umod_p16_s128_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-umod_p16_s16_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-umod_p16_s256_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-umod_p16_s32_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-umod_p16_s64_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-umod_p32_s128_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-umod_p32_s256_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-umod_p32_s32_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-umod_p32_s64_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-umod_p64_s128_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-umod_p64_s256_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-umod_p64_s64_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-umod_p8_s128_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-umod_p8_s16_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-umod_p8_s256_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-umod_p8_s32_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-umod_p8_s64_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-umod_p8_s8_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-umod")]
)

	]
	[(repair-umul_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-umul_p16_s128_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-umul_p16_s16_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-umul_p16_s256_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-umul_p16_s32_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-umul_p16_s64_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-umul_p32_s128_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-umul_p32_s256_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-umul_p32_s32_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-umul_p32_s64_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-umul_p64_s128_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-umul_p64_s256_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-umul_p64_s64_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-umul_p8_s128_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-umul_p8_s16_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-umul_p8_s256_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-umul_p8_s32_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-umul_p8_s64_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-umul_p8_s8_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-umul")]
)

	]
	[(repair-usat-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-usat-add_p16_s128_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-usat-add_p16_s16_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-usat-add_p16_s256_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-usat-add_p16_s32_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-usat-add_p16_s64_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-usat-add_p32_s128_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-usat-add_p32_s256_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-usat-add_p32_s32_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-usat-add_p32_s64_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-usat-add_p64_s128_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-usat-add_p64_s256_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-usat-add_p64_s64_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-usat-add_p8_s128_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-usat-add_p8_s16_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-usat-add_p8_s256_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-usat-add_p8_s32_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-usat-add_p8_s64_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-usat-add_p8_s8_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-usat-add")]
)

	]
	[(repair-usat-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-usat-sub_p16_s128_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-usat-sub_p16_s16_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-usat-sub_p16_s256_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-usat-sub_p16_s32_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-usat-sub_p16_s64_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-usat-sub_p32_s128_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-usat-sub_p32_s256_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-usat-sub_p32_s32_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-usat-sub_p32_s64_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-usat-sub_p64_s128_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-usat-sub_p64_s256_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-usat-sub_p64_s64_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-usat-sub_p8_s128_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-usat-sub_p8_s16_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-usat-sub_p8_s256_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-usat-sub_p8_s32_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-usat-sub_p8_s64_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-usat-sub_p8_s8_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-usat-sub")]
)

	]
	[(repair-ushr_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); repair-ushr_p16_s128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); repair-ushr_p16_s16_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); repair-ushr_p16_s256_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); repair-ushr_p16_s32_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); repair-ushr_p16_s64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); repair-ushr_p32_s128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); repair-ushr_p32_s256_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); repair-ushr_p32_s32_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); repair-ushr_p32_s64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); repair-ushr_p64_s128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); repair-ushr_p64_s256_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); repair-ushr_p64_s64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); repair-ushr_p8_s128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); repair-ushr_p8_s16_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); repair-ushr_p8_s256_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); repair-ushr_p8_s32_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); repair-ushr_p8_s64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); repair-ushr_p8_s8_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (repair:get-bv-ops v0) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-ushr")]
)

	]
	[(repair-vector-reduce-add_dsl num_0 v1 size_o size_i)
		(cond 
		[(and  (equal? num_0 2) (equal? size_o 16) (equal? size_i 32)); repair-vector-reduce-add_p16_s32_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v1)))]
		[(and  (equal? num_0 4) (equal? size_o 16) (equal? size_i 64)); repair-vector-reduce-add_p16_s64_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v1)))]
		[(and  (equal? num_0 4) (equal? size_o 32) (equal? size_i 128)); repair-vector-reduce-add_p32_s128_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v1)))]
		[(and  (equal? num_0 2) (equal? size_o 32) (equal? size_i 64)); repair-vector-reduce-add_p32_s64_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v1)))]
		[(and  (equal? num_0 2) (equal? size_o 64) (equal? size_i 128)); repair-vector-reduce-add_p64_s128_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v1)))]
		[(and  (equal? num_0 4) (equal? size_o 64) (equal? size_i 256)); repair-vector-reduce-add_p64_s256_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v1)))]
		[(and  (equal? num_0 2) (equal? size_o 8) (equal? size_i 16)); repair-vector-reduce-add_p8_s16_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v1)))]
		[(and  (equal? num_0 4) (equal? size_o 8) (equal? size_i 32)); repair-vector-reduce-add_p8_s32_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (repair:get-bv-ops v1)))]
		[else (error "Unable to get ops  for repair-vector-reduce-add")]
)

	]
 )
)
;; ================================================================================

