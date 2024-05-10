;#============================== Hydride File =================================
;#
;# Part of the Hydride Compiler Infrastructure.
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
;;                                DSL Get Names
;; ================================================================================
(define (repair:get-target-name prog)
 (destruct prog
	[(reg id) '()]
	[(lit v) '()]
		[(vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		 (append (list  "two_input_swizzle_N6_T8_LO0_L3_G3_D1_R0") (repair:get-target-name v0) (repair:get-target-name v1))
	]
		[(interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		 (append (list  "interleave-vectors-128-16") (repair:get-target-name v0) (repair:get-target-name v1))
	]
		[(interleave-vector_dsl v0 size_i_o prec_i_o)
		 (append (list  "interleave-vector-128-16") (repair:get-target-name v0))
	]
		[(deinterleave-vector_dsl v0 size_i_o prec_i_o)
		 (append (list  "deinterleave-vector-128-16") (repair:get-target-name v0))
	]
		[(llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		 (append (list  "shuffle-vector-128-16-128") (repair:get-target-name v0) (repair:get-target-name v1) (repair:get-target-name v4))
	]
		[(llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		 (append (list  "llvm-vect-add-128-16") (repair:get-target-name v0) (repair:get-target-name v1))
	]
		[(llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		 (append (list  "llvm-vect-sub-128-16") (repair:get-target-name v0) (repair:get-target-name v1))
	]
		[(llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		 (append (list  "llvm-vect-mul-128-16") (repair:get-target-name v0) (repair:get-target-name v1))
	]
		[(llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		 (append (list  "llvm-vect-sdiv-128-16") (repair:get-target-name v0) (repair:get-target-name v1))
	]
		[(llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		 (append (list  "llvm-vect-udiv-128-16") (repair:get-target-name v0) (repair:get-target-name v1))
	]
		[(llvm-zext_dsl v0 size_i size_o)
		 (append (list  "llvm-zext-8-32") (repair:get-target-name v0))
	]
		[(scalar_splat_dsl v0 size_i size_o)
		 (append (list  "llvm-splat-8-32") (repair:get-target-name v0))
	]
	[(repair-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-add_p16_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-add_p16_s16_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-add_p16_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-add_p16_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-add_p16_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-add_p32_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-add_p32_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-add_p32_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-add_p32_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-add_p64_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-add_p64_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-add_p64_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-add_p8_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-add_p8_s16_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-add_p8_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-add_p8_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-add_p8_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-add_p8_s8_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-add")]
)

	]
	[(repair-bwand_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-bwand_p16_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-bwand_p16_s16_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-bwand_p16_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-bwand_p16_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-bwand_p16_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-bwand_p32_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-bwand_p32_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-bwand_p32_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-bwand_p32_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-bwand_p64_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-bwand_p64_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-bwand_p64_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-bwand_p8_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-bwand_p8_s16_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-bwand_p8_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-bwand_p8_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-bwand_p8_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-bwand_p8_s8_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-bwand")]
)

	]
	[(repair-bwnot_dsl v0 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-bwnot_p16_s128_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-bwnot_p16_s16_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-bwnot_p16_s256_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-bwnot_p16_s32_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-bwnot_p16_s64_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-bwnot_p32_s128_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-bwnot_p32_s256_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-bwnot_p32_s32_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-bwnot_p32_s64_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-bwnot_p64_s128_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-bwnot_p64_s256_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-bwnot_p64_s64_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-bwnot_p8_s128_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-bwnot_p8_s16_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-bwnot_p8_s256_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-bwnot_p8_s32_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-bwnot_p8_s64_signed_None") (repair:get-target-name v0))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-bwnot_p8_s8_signed_None") (repair:get-target-name v0))]
		[else (error "Unable to get name  for repair-bwnot")]
)

	]
	[(repair-bwor_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-bwor_p16_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-bwor_p16_s16_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-bwor_p16_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-bwor_p16_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-bwor_p16_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-bwor_p32_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-bwor_p32_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-bwor_p32_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-bwor_p32_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-bwor_p64_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-bwor_p64_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-bwor_p64_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-bwor_p8_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-bwor_p8_s16_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-bwor_p8_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-bwor_p8_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-bwor_p8_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-bwor_p8_s8_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-bwor")]
)

	]
	[(repair-cast-int_dsl v0 prec_i prec_o size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 128)) 
   (append (list  "repair-cast-int_ip16_is128_op32_os256_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)) 
   (append (list  "repair-cast-int_ip16_is128_op8_os64_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 16)) 
   (append (list  "repair-cast-int_ip16_is16_op32_os32_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)) 
   (append (list  "repair-cast-int_ip16_is16_op8_os8_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)) 
   (append (list  "repair-cast-int_ip16_is256_op8_os128_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 32)) 
   (append (list  "repair-cast-int_ip16_is32_op32_os64_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)) 
   (append (list  "repair-cast-int_ip16_is32_op8_os16_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 64)) 
   (append (list  "repair-cast-int_ip16_is64_op32_os128_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)) 
   (append (list  "repair-cast-int_ip16_is64_op8_os32_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)) 
   (append (list  "repair-cast-int_ip32_is128_op16_os64_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 128)) 
   (append (list  "repair-cast-int_ip32_is128_op64_os256_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)) 
   (append (list  "repair-cast-int_ip32_is256_op16_os128_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)) 
   (append (list  "repair-cast-int_ip32_is32_op16_os16_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 32)) 
   (append (list  "repair-cast-int_ip32_is32_op64_os64_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)) 
   (append (list  "repair-cast-int_ip32_is64_op16_os32_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 64)) 
   (append (list  "repair-cast-int_ip32_is64_op64_os128_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)) 
   (append (list  "repair-cast-int_ip64_is128_op32_os64_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)) 
   (append (list  "repair-cast-int_ip64_is256_op32_os128_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)) 
   (append (list  "repair-cast-int_ip64_is64_op32_os32_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 128)) 
   (append (list  "repair-cast-int_ip8_is128_op16_os256_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 16)) 
   (append (list  "repair-cast-int_ip8_is16_op16_os32_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 32)) 
   (append (list  "repair-cast-int_ip8_is32_op16_os64_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 64)) 
   (append (list  "repair-cast-int_ip8_is64_op16_os128_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 8)) 
   (append (list  "repair-cast-int_ip8_is8_op16_os16_signed_1") (repair:get-target-name v0))]
		[else (error "Unable to get name  for repair-cast-int")]
)

	]
	[(repair-cast-uint_dsl v0 prec_i prec_o size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 128)) 
   (append (list  "repair-cast-uint_ip16_is128_op32_os256_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)) 
   (append (list  "repair-cast-uint_ip16_is128_op8_os64_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 16)) 
   (append (list  "repair-cast-uint_ip16_is16_op32_os32_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)) 
   (append (list  "repair-cast-uint_ip16_is16_op8_os8_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)) 
   (append (list  "repair-cast-uint_ip16_is256_op8_os128_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 32)) 
   (append (list  "repair-cast-uint_ip16_is32_op32_os64_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)) 
   (append (list  "repair-cast-uint_ip16_is32_op8_os16_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 32) (equal? size_i 64)) 
   (append (list  "repair-cast-uint_ip16_is64_op32_os128_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)) 
   (append (list  "repair-cast-uint_ip16_is64_op8_os32_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)) 
   (append (list  "repair-cast-uint_ip32_is128_op16_os64_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 128)) 
   (append (list  "repair-cast-uint_ip32_is128_op64_os256_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)) 
   (append (list  "repair-cast-uint_ip32_is256_op16_os128_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)) 
   (append (list  "repair-cast-uint_ip32_is32_op16_os16_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 32)) 
   (append (list  "repair-cast-uint_ip32_is32_op64_os64_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)) 
   (append (list  "repair-cast-uint_ip32_is64_op16_os32_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 64) (equal? size_i 64)) 
   (append (list  "repair-cast-uint_ip32_is64_op64_os128_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)) 
   (append (list  "repair-cast-uint_ip64_is128_op32_os64_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)) 
   (append (list  "repair-cast-uint_ip64_is256_op32_os128_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)) 
   (append (list  "repair-cast-uint_ip64_is64_op32_os32_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 128)) 
   (append (list  "repair-cast-uint_ip8_is128_op16_os256_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 16)) 
   (append (list  "repair-cast-uint_ip8_is16_op16_os32_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 32)) 
   (append (list  "repair-cast-uint_ip8_is32_op16_os64_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 64)) 
   (append (list  "repair-cast-uint_ip8_is64_op16_os128_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 8) (equal? prec_o 16) (equal? size_i 8)) 
   (append (list  "repair-cast-uint_ip8_is8_op16_os16_signed_0") (repair:get-target-name v0))]
		[else (error "Unable to get name  for repair-cast-uint")]
)

	]
	[(repair-sabsd_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-sabsd_p16_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-sabsd_p16_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-sabsd_p16_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-sabsd_p16_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-sabsd_p16_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-sabsd_p32_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-sabsd_p32_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-sabsd_p32_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-sabsd_p32_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-sabsd_p64_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-sabsd_p64_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-sabsd_p64_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-sabsd_p8_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-sabsd_p8_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-sabsd_p8_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-sabsd_p8_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-sabsd_p8_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-sabsd_p8_s8_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-sabsd")]
)

	]
	[(repair-saturate_dsl v0 prec_i prec_o size_i bool_4)
		(cond 
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)) 
   (append (list  "repair-saturate_ip16_is128_op8_os64_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 128)) 
   (append (list  "repair-saturate_ip16_is128_op8_os64_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)) 
   (append (list  "repair-saturate_ip16_is16_op8_os8_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 16)) 
   (append (list  "repair-saturate_ip16_is16_op8_os8_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)) 
   (append (list  "repair-saturate_ip16_is256_op8_os128_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 256)) 
   (append (list  "repair-saturate_ip16_is256_op8_os128_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)) 
   (append (list  "repair-saturate_ip16_is32_op8_os16_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 32)) 
   (append (list  "repair-saturate_ip16_is32_op8_os16_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)) 
   (append (list  "repair-saturate_ip16_is64_op8_os32_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 16) (equal? prec_o 8) (equal? size_i 64)) 
   (append (list  "repair-saturate_ip16_is64_op8_os32_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)) 
   (append (list  "repair-saturate_ip32_is128_op16_os64_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 128)) 
   (append (list  "repair-saturate_ip32_is128_op16_os64_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)) 
   (append (list  "repair-saturate_ip32_is256_op16_os128_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 256)) 
   (append (list  "repair-saturate_ip32_is256_op16_os128_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)) 
   (append (list  "repair-saturate_ip32_is32_op16_os16_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 32)) 
   (append (list  "repair-saturate_ip32_is32_op16_os16_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)) 
   (append (list  "repair-saturate_ip32_is64_op16_os32_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 32) (equal? prec_o 16) (equal? size_i 64)) 
   (append (list  "repair-saturate_ip32_is64_op16_os32_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)) 
   (append (list  "repair-saturate_ip64_is128_op32_os64_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 128)) 
   (append (list  "repair-saturate_ip64_is128_op32_os64_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)) 
   (append (list  "repair-saturate_ip64_is256_op32_os128_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 256)) 
   (append (list  "repair-saturate_ip64_is256_op32_os128_signed_1") (repair:get-target-name v0))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)) 
   (append (list  "repair-saturate_ip64_is64_op32_os32_signed_0") (repair:get-target-name v0))]
		[(and  (equal? prec_i 64) (equal? prec_o 32) (equal? size_i 64)) 
   (append (list  "repair-saturate_ip64_is64_op32_os32_signed_1") (repair:get-target-name v0))]
		[else (error "Unable to get name  for repair-saturate")]
)

	]
	[(repair-sdiv_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-sdiv_p16_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-sdiv_p16_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-sdiv_p16_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-sdiv_p16_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-sdiv_p16_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-sdiv_p32_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-sdiv_p32_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-sdiv_p32_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-sdiv_p32_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-sdiv_p64_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-sdiv_p64_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-sdiv_p64_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-sdiv_p8_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-sdiv_p8_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-sdiv_p8_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-sdiv_p8_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-sdiv_p8_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-sdiv_p8_s8_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-sdiv")]
)

	]
	[(repair-shl_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-shl_p16_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-shl_p16_s16_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-shl_p16_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-shl_p16_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-shl_p16_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-shl_p32_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-shl_p32_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-shl_p32_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-shl_p32_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-shl_p64_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-shl_p64_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-shl_p64_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-shl_p8_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-shl_p8_s16_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-shl_p8_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-shl_p8_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-shl_p8_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-shl_p8_s8_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-shl")]
)

	]
	[(repair-smax_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-smax_p16_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-smax_p16_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-smax_p16_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-smax_p16_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-smax_p16_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-smax_p32_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-smax_p32_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-smax_p32_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-smax_p32_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-smax_p64_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-smax_p64_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-smax_p64_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-smax_p8_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-smax_p8_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-smax_p8_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-smax_p8_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-smax_p8_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-smax_p8_s8_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-smax")]
)

	]
	[(repair-smin_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-smin_p16_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-smin_p16_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-smin_p16_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-smin_p16_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-smin_p16_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-smin_p32_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-smin_p32_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-smin_p32_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-smin_p32_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-smin_p64_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-smin_p64_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-smin_p64_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-smin_p8_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-smin_p8_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-smin_p8_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-smin_p8_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-smin_p8_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-smin_p8_s8_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-smin")]
)

	]
	[(repair-smod_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-smod_p16_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-smod_p16_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-smod_p16_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-smod_p16_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-smod_p16_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-smod_p32_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-smod_p32_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-smod_p32_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-smod_p32_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-smod_p64_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-smod_p64_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-smod_p64_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-smod_p8_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-smod_p8_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-smod_p8_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-smod_p8_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-smod_p8_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-smod_p8_s8_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-smod")]
)

	]
	[(repair-smul_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-smul_p16_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-smul_p16_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-smul_p16_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-smul_p16_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-smul_p16_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-smul_p32_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-smul_p32_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-smul_p32_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-smul_p32_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-smul_p64_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-smul_p64_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-smul_p64_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-smul_p8_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-smul_p8_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-smul_p8_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-smul_p8_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-smul_p8_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-smul_p8_s8_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-smul")]
)

	]
	[(repair-ssat-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-ssat-add_p16_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-ssat-add_p16_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-ssat-add_p16_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-ssat-add_p16_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-ssat-add_p16_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-ssat-add_p32_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-ssat-add_p32_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-ssat-add_p32_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-ssat-add_p32_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-ssat-add_p64_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-ssat-add_p64_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-ssat-add_p64_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-ssat-add_p8_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-ssat-add_p8_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-ssat-add_p8_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-ssat-add_p8_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-ssat-add_p8_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-ssat-add_p8_s8_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-ssat-add")]
)

	]
	[(repair-ssat-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-ssat-sub_p16_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-ssat-sub_p16_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-ssat-sub_p16_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-ssat-sub_p16_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-ssat-sub_p16_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-ssat-sub_p32_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-ssat-sub_p32_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-ssat-sub_p32_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-ssat-sub_p32_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-ssat-sub_p64_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-ssat-sub_p64_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-ssat-sub_p64_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-ssat-sub_p8_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-ssat-sub_p8_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-ssat-sub_p8_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-ssat-sub_p8_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-ssat-sub_p8_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-ssat-sub_p8_s8_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-ssat-sub")]
)

	]
	[(repair-sshr_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-sshr_p16_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-sshr_p16_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-sshr_p16_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-sshr_p16_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-sshr_p16_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-sshr_p32_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-sshr_p32_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-sshr_p32_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-sshr_p32_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-sshr_p64_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-sshr_p64_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-sshr_p64_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-sshr_p8_s128_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-sshr_p8_s16_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-sshr_p8_s256_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-sshr_p8_s32_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-sshr_p8_s64_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-sshr_p8_s8_signed_1") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-sshr")]
)

	]
	[(repair-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-sub_p16_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-sub_p16_s16_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-sub_p16_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-sub_p16_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-sub_p16_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-sub_p32_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-sub_p32_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-sub_p32_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-sub_p32_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-sub_p64_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-sub_p64_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-sub_p64_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-sub_p8_s128_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-sub_p8_s16_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-sub_p8_s256_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-sub_p8_s32_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-sub_p8_s64_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-sub_p8_s8_signed_None") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-sub")]
)

	]
	[(repair-uabsd_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-uabsd_p16_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-uabsd_p16_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-uabsd_p16_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-uabsd_p16_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-uabsd_p16_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-uabsd_p32_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-uabsd_p32_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-uabsd_p32_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-uabsd_p32_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-uabsd_p64_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-uabsd_p64_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-uabsd_p64_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-uabsd_p8_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-uabsd_p8_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-uabsd_p8_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-uabsd_p8_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-uabsd_p8_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-uabsd_p8_s8_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-uabsd")]
)

	]
	[(repair-udiv_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-udiv_p16_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-udiv_p16_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-udiv_p16_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-udiv_p16_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-udiv_p16_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-udiv_p32_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-udiv_p32_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-udiv_p32_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-udiv_p32_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-udiv_p64_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-udiv_p64_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-udiv_p64_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-udiv_p8_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-udiv_p8_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-udiv_p8_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-udiv_p8_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-udiv_p8_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-udiv_p8_s8_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-udiv")]
)

	]
	[(repair-umax_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-umax_p16_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-umax_p16_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-umax_p16_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-umax_p16_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-umax_p16_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-umax_p32_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-umax_p32_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-umax_p32_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-umax_p32_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-umax_p64_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-umax_p64_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-umax_p64_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-umax_p8_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-umax_p8_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-umax_p8_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-umax_p8_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-umax_p8_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-umax_p8_s8_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-umax")]
)

	]
	[(repair-umin_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-umin_p16_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-umin_p16_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-umin_p16_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-umin_p16_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-umin_p16_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-umin_p32_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-umin_p32_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-umin_p32_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-umin_p32_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-umin_p64_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-umin_p64_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-umin_p64_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-umin_p8_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-umin_p8_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-umin_p8_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-umin_p8_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-umin_p8_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-umin_p8_s8_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-umin")]
)

	]
	[(repair-umod_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-umod_p16_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-umod_p16_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-umod_p16_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-umod_p16_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-umod_p16_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-umod_p32_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-umod_p32_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-umod_p32_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-umod_p32_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-umod_p64_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-umod_p64_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-umod_p64_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-umod_p8_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-umod_p8_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-umod_p8_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-umod_p8_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-umod_p8_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-umod_p8_s8_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-umod")]
)

	]
	[(repair-umul_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-umul_p16_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-umul_p16_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-umul_p16_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-umul_p16_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-umul_p16_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-umul_p32_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-umul_p32_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-umul_p32_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-umul_p32_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-umul_p64_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-umul_p64_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-umul_p64_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-umul_p8_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-umul_p8_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-umul_p8_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-umul_p8_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-umul_p8_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-umul_p8_s8_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-umul")]
)

	]
	[(repair-usat-add_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-usat-add_p16_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-usat-add_p16_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-usat-add_p16_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-usat-add_p16_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-usat-add_p16_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-usat-add_p32_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-usat-add_p32_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-usat-add_p32_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-usat-add_p32_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-usat-add_p64_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-usat-add_p64_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-usat-add_p64_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-usat-add_p8_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-usat-add_p8_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-usat-add_p8_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-usat-add_p8_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-usat-add_p8_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-usat-add_p8_s8_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-usat-add")]
)

	]
	[(repair-usat-sub_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-usat-sub_p16_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-usat-sub_p16_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-usat-sub_p16_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-usat-sub_p16_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-usat-sub_p16_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-usat-sub_p32_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-usat-sub_p32_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-usat-sub_p32_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-usat-sub_p32_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-usat-sub_p64_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-usat-sub_p64_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-usat-sub_p64_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-usat-sub_p8_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-usat-sub_p8_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-usat-sub_p8_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-usat-sub_p8_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-usat-sub_p8_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-usat-sub_p8_s8_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-usat-sub")]
)

	]
	[(repair-ushr_dsl v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 
   (append (list  "repair-ushr_p16_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 
   (append (list  "repair-ushr_p16_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 
   (append (list  "repair-ushr_p16_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 
   (append (list  "repair-ushr_p16_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 
   (append (list  "repair-ushr_p16_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 
   (append (list  "repair-ushr_p32_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 
   (append (list  "repair-ushr_p32_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 
   (append (list  "repair-ushr_p32_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 
   (append (list  "repair-ushr_p32_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 
   (append (list  "repair-ushr_p64_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 
   (append (list  "repair-ushr_p64_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 
   (append (list  "repair-ushr_p64_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 
   (append (list  "repair-ushr_p8_s128_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 
   (append (list  "repair-ushr_p8_s16_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 
   (append (list  "repair-ushr_p8_s256_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 
   (append (list  "repair-ushr_p8_s32_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 
   (append (list  "repair-ushr_p8_s64_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 
   (append (list  "repair-ushr_p8_s8_signed_0") (repair:get-target-name v0) (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-ushr")]
)

	]
	[(repair-vector-reduce-add_dsl num_0 v1 size_o size_i)
		(cond 
		[(and  (equal? num_0 2) (equal? size_o 16) (equal? size_i 32)) 
   (append (list  "repair-vector-reduce-add_p16_s32_signed_None") (repair:get-target-name v1))]
		[(and  (equal? num_0 4) (equal? size_o 16) (equal? size_i 64)) 
   (append (list  "repair-vector-reduce-add_p16_s64_signed_None") (repair:get-target-name v1))]
		[(and  (equal? num_0 4) (equal? size_o 32) (equal? size_i 128)) 
   (append (list  "repair-vector-reduce-add_p32_s128_signed_None") (repair:get-target-name v1))]
		[(and  (equal? num_0 2) (equal? size_o 32) (equal? size_i 64)) 
   (append (list  "repair-vector-reduce-add_p32_s64_signed_None") (repair:get-target-name v1))]
		[(and  (equal? num_0 2) (equal? size_o 64) (equal? size_i 128)) 
   (append (list  "repair-vector-reduce-add_p64_s128_signed_None") (repair:get-target-name v1))]
		[(and  (equal? num_0 4) (equal? size_o 64) (equal? size_i 256)) 
   (append (list  "repair-vector-reduce-add_p64_s256_signed_None") (repair:get-target-name v1))]
		[(and  (equal? num_0 2) (equal? size_o 8) (equal? size_i 16)) 
   (append (list  "repair-vector-reduce-add_p8_s16_signed_None") (repair:get-target-name v1))]
		[(and  (equal? num_0 4) (equal? size_o 8) (equal? size_i 32)) 
   (append (list  "repair-vector-reduce-add_p8_s32_signed_None") (repair:get-target-name v1))]
		[else (error "Unable to get name  for repair-vector-reduce-add")]
)

	]
 )
)
;; ================================================================================

