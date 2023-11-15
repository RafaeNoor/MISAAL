#lang rosette/safe


(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require rosette/lib/destruct)
(require
  rosette/lib/destruct
  hydride/utils/debug
  (only-in racket/base error)
  )

(require hydride/ir/hydride/definition)
(require hydride/halide)
(require misaal/ir/halide/types)




(provide (all-defined-out))
;; ================================================================================
;;                                DSL Get Ops
;; ================================================================================
(define (typed:halide:get-bv-ops prog)
 (destruct prog
	[(reg id) '()]
	[(lit v) '()]
		[(vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(remove-duplicates (append (list  'if) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))
	]
		[(interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(remove-duplicates (append (list  ) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))
	]
		[(interleave-vector_dsl v0 size_i_o prec_i_o)
		(remove-duplicates (append (list  'cond) (typed:halide:get-bv-ops v0)))
	]
		[(deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(remove-duplicates (append (list  'cond) (typed:halide:get-bv-ops v0)))
	]
		[(llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(remove-duplicates (append (list  'bitvector->integer 'if) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1) (typed:halide:get-bv-ops v4)))
	]
		[(llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvadd) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))
	]
		[(llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvsub) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))
	]
		[(llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvmul) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))
	]
		[(llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvsdiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))
	]
		[(llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvudiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))
	]
		[(llvm-zext_dsl v0 size_i size_o)
		(remove-duplicates (append (list  'zero-extend) (typed:halide:get-bv-ops v0)))
	]
		[(scalar_splat_dsl v0 size_i size_o)
		(remove-duplicates (append (list  'zero-extend) (typed:halide:get-bv-ops v0)))
	]
	[(typed:cast-int v0 prec_i num_2 num_3 prec_o)
		(cond 
		[(and  (equal? prec_i 16) (equal? num_2 0) (equal? num_3 64) (equal? prec_o 32)); typed:cast-int_0_ip16_is1024_op32_os2048_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? num_2 0) (equal? num_3 128) (equal? prec_o 8)); typed:cast-int_0_ip16_is2048_op8_os1024_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? num_2 0) (equal? num_3 64) (equal? prec_o 16)); typed:cast-int_0_ip32_is2048_op16_os1024_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? num_2 0) (equal? num_3 128) (equal? prec_o 16)); typed:cast-int_0_ip8_is1024_op16_os2048_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? num_2 1) (equal? num_3 64) (equal? prec_o 32)); typed:cast-int_1_ip16_is1024_op32_os2048_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? num_2 1) (equal? num_3 128) (equal? prec_o 8)); typed:cast-int_1_ip16_is2048_op8_os1024_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? num_2 1) (equal? num_3 64) (equal? prec_o 16)); typed:cast-int_1_ip32_is2048_op16_os1024_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? num_2 1) (equal? num_3 128) (equal? prec_o 16)); typed:cast-int_1_ip8_is1024_op16_os2048_signed_1
 
  (remove-duplicates (append (list  'extract 'sign-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[else (error "Unable to get ops  for typed:cast-int")]
)

	]
	[(typed:cast-uint v0 prec_i num_2 num_3 prec_o)
		(cond 
		[(and  (equal? prec_i 16) (equal? num_2 0) (equal? num_3 64) (equal? prec_o 32)); typed:cast-uint_0_ip16_is1024_op32_os2048_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? num_2 0) (equal? num_3 128) (equal? prec_o 8)); typed:cast-uint_0_ip16_is2048_op8_os1024_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? num_2 0) (equal? num_3 64) (equal? prec_o 16)); typed:cast-uint_0_ip32_is2048_op16_os1024_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? num_2 0) (equal? num_3 128) (equal? prec_o 16)); typed:cast-uint_0_ip8_is1024_op16_os2048_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? num_2 1) (equal? num_3 64) (equal? prec_o 32)); typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? num_2 1) (equal? num_3 128) (equal? prec_o 8)); typed:cast-uint_1_ip16_is2048_op8_os1024_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? num_2 1) (equal? num_3 64) (equal? prec_o 16)); typed:cast-uint_1_ip32_is2048_op16_os1024_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 8) (equal? num_2 1) (equal? num_3 128) (equal? prec_o 16)); typed:cast-uint_1_ip8_is1024_op16_os2048_signed_0
 
  (remove-duplicates (append (list  'extract 'zero-extend 'concat) (typed:halide:get-bv-ops v0)))]
		[else (error "Unable to get ops  for typed:cast-uint")]
)

	]
	[(typed:concat_vectors v0 v1 prec_i_o size_i)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i 1024)); typed:concat_vectors_ip16_is1024_op16_os2048_signed_None
 
  (remove-duplicates (append (list  'extract 'concat) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i 1024)); typed:concat_vectors_ip32_is1024_op32_os2048_signed_None
 
  (remove-duplicates (append (list  'extract 'concat) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i 1024)); typed:concat_vectors_ip8_is1024_op8_os2048_signed_None
 
  (remove-duplicates (append (list  'extract 'concat) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:concat_vectors")]
)

	]
	[(typed:signed-vec-abs v0 num_1 prec_i_o)
		(cond 
		[(and  (equal? num_1 16) (equal? prec_i_o 1024)); typed:signed-vec-abs_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'abs 'extract 'sign-extend 'bitvector->integer) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 16) (equal? prec_i_o 2048)); typed:signed-vec-abs_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'abs 'extract 'sign-extend 'bitvector->integer) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 32) (equal? prec_i_o 1024)); typed:signed-vec-abs_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'abs 'extract 'sign-extend 'bitvector->integer) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 32) (equal? prec_i_o 2048)); typed:signed-vec-abs_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'abs 'extract 'sign-extend 'bitvector->integer) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 8) (equal? prec_i_o 1024)); typed:signed-vec-abs_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'abs 'extract 'sign-extend 'bitvector->integer) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 8) (equal? prec_i_o 2048)); typed:signed-vec-abs_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'abs 'extract 'sign-extend 'bitvector->integer) (typed:halide:get-bv-ops v0)))]
		[else (error "Unable to get ops  for typed:signed-vec-abs")]
)

	]
	[(typed:signed-vec-absd v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:signed-vec-absd_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:signed-vec-absd_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:signed-vec-absd_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:signed-vec-absd_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:signed-vec-absd_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:signed-vec-absd_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvsmax 'bvsmin) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-absd")]
)

	]
	[(typed:signed-vec-div v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:signed-vec-div_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:signed-vec-div_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:signed-vec-div_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:signed-vec-div_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:signed-vec-div_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:signed-vec-div_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsdiv 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-div")]
)

	]
	[(typed:signed-vec-halving_add v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:signed-vec-halving_add_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvadd 'sign-extend 'bvsdiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:signed-vec-halving_add_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'extract 'bvadd 'sign-extend 'bvsdiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:signed-vec-halving_add_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvadd 'sign-extend 'bvsdiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:signed-vec-halving_add_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'extract 'bvadd 'sign-extend 'bvsdiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:signed-vec-halving_add_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvadd 'sign-extend 'bvsdiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:signed-vec-halving_add_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'extract 'bvadd 'sign-extend 'bvsdiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-halving_add")]
)

	]
	[(typed:signed-vec-max v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:signed-vec-max_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:signed-vec-max_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:signed-vec-max_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:signed-vec-max_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:signed-vec-max_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:signed-vec-max_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsmax 'bvsgt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-max")]
)

	]
	[(typed:signed-vec-min v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:signed-vec-min_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:signed-vec-min_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:signed-vec-min_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:signed-vec-min_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:signed-vec-min_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:signed-vec-min_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsmin 'bvslt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-min")]
)

	]
	[(typed:signed-vec-mod v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:signed-vec-mod_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:signed-vec-mod_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:signed-vec-mod_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:signed-vec-mod_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:signed-vec-mod_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:signed-vec-mod_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsrem 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-mod")]
)

	]
	[(typed:signed-vec-mul v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:signed-vec-mul_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:signed-vec-mul_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:signed-vec-mul_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:signed-vec-mul_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:signed-vec-mul_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:signed-vec-mul_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-mul")]
)

	]
	[(typed:signed-vec-rounding_halving_add v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:signed-vec-rounding_halving_add_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvadd 'sign-extend 'bvsdiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:signed-vec-rounding_halving_add_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'extract 'bvadd 'sign-extend 'bvsdiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:signed-vec-rounding_halving_add_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvadd 'sign-extend 'bvsdiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:signed-vec-rounding_halving_add_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'extract 'bvadd 'sign-extend 'bvsdiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:signed-vec-rounding_halving_add_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvadd 'sign-extend 'bvsdiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:signed-vec-rounding_halving_add_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'extract 'bvadd 'sign-extend 'bvsdiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-rounding_halving_add")]
)

	]
	[(typed:signed-vec-rounding_mul_shift_right v0 v1 v2 num_3 prec_i_o)
		(cond 
		[(and  (equal? num_3 16) (equal? prec_i_o 1024)); typed:signed-vec-rounding_mul_shift_right_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'bvshl 'bvashr 'bvssat 'bvsdiv 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1) (typed:halide:get-bv-ops v2)))]
		[(and  (equal? num_3 16) (equal? prec_i_o 2048)); typed:signed-vec-rounding_mul_shift_right_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'bvshl 'bvashr 'bvssat 'bvsdiv 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1) (typed:halide:get-bv-ops v2)))]
		[(and  (equal? num_3 32) (equal? prec_i_o 1024)); typed:signed-vec-rounding_mul_shift_right_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'bvshl 'bvashr 'bvssat 'bvsdiv 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1) (typed:halide:get-bv-ops v2)))]
		[(and  (equal? num_3 32) (equal? prec_i_o 2048)); typed:signed-vec-rounding_mul_shift_right_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'bvshl 'bvashr 'bvssat 'bvsdiv 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1) (typed:halide:get-bv-ops v2)))]
		[(and  (equal? num_3 8) (equal? prec_i_o 1024)); typed:signed-vec-rounding_mul_shift_right_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'bvshl 'bvashr 'bvssat 'bvsdiv 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1) (typed:halide:get-bv-ops v2)))]
		[(and  (equal? num_3 8) (equal? prec_i_o 2048)); typed:signed-vec-rounding_mul_shift_right_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'bvshl 'bvashr 'bvssat 'bvsdiv 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1) (typed:halide:get-bv-ops v2)))]
		[else (error "Unable to get ops  for typed:signed-vec-rounding_mul_shift_right")]
)

	]
	[(typed:signed-vec-rounding_shift_right v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:signed-vec-rounding_shift_right_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'bvshl 'bvashr 'bvssat 'bvsdiv 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:signed-vec-rounding_shift_right_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'bvshl 'bvashr 'bvssat 'bvsdiv 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:signed-vec-rounding_shift_right_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'bvshl 'bvashr 'bvssat 'bvsdiv 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:signed-vec-rounding_shift_right_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'bvshl 'bvashr 'bvssat 'bvsdiv 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:signed-vec-rounding_shift_right_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'bvshl 'bvashr 'bvssat 'bvsdiv 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:signed-vec-rounding_shift_right_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'bvshl 'bvashr 'bvssat 'bvsdiv 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-rounding_shift_right")]
)

	]
	[(typed:signed-vec-sat-add v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:signed-vec-sat-add_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:signed-vec-sat-add_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:signed-vec-sat-add_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:signed-vec-sat-add_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:signed-vec-sat-add_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:signed-vec-sat-add_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'bvaddnsw 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-sat-add")]
)

	]
	[(typed:signed-vec-sat-sub v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:signed-vec-sat-sub_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:signed-vec-sat-sub_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:signed-vec-sat-sub_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:signed-vec-sat-sub_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:signed-vec-sat-sub_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:signed-vec-sat-sub_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'bvsubnsw 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-sat-sub")]
)

	]
	[(typed:signed-vec-shr v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:signed-vec-shr_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:signed-vec-shr_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:signed-vec-shr_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:signed-vec-shr_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:signed-vec-shr_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:signed-vec-shr_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'extract 'bvashr) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-shr")]
)

	]
	[(typed:signed-vec-widen-mul v0 v1 prec_i_o size_i)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i 1024)); typed:signed-vec-widen-mul_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i 1024)); typed:signed-vec-widen-mul_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'bvmul 'extract 'sign-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-widen-mul")]
)

	]
	[(typed:slice_vectors v0 num_1 num_2 num_3 prec_i_o size_i)
		(cond 
		[(and  (equal? num_1 0) (equal? num_2 1) (equal? num_3 64) (equal? prec_i_o 16) (equal? size_i 2048)); typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_0_1_64
 
  (remove-duplicates (append (list  'extract 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 64) (equal? num_2 1) (equal? num_3 64) (equal? prec_i_o 16) (equal? size_i 2048)); typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_64_1_64
 
  (remove-duplicates (append (list  'extract 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 0) (equal? num_2 1) (equal? num_3 32) (equal? prec_i_o 32) (equal? size_i 2048)); typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_0_1_32
 
  (remove-duplicates (append (list  'extract 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 32) (equal? num_2 1) (equal? num_3 32) (equal? prec_i_o 32) (equal? size_i 2048)); typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_32_1_32
 
  (remove-duplicates (append (list  'extract 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 0) (equal? num_2 1) (equal? num_3 128) (equal? prec_i_o 8) (equal? size_i 2048)); typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_0_1_128
 
  (remove-duplicates (append (list  'extract 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 128) (equal? num_2 1) (equal? num_3 128) (equal? prec_i_o 8) (equal? size_i 2048)); typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_128_1_128
 
  (remove-duplicates (append (list  'extract 'concat) (typed:halide:get-bv-ops v0)))]
		[else (error "Unable to get ops  for typed:slice_vectors")]
)

	]
	[(typed:unsigned-vec-absd v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:unsigned-vec-absd_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:unsigned-vec-absd_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:unsigned-vec-absd_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:unsigned-vec-absd_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:unsigned-vec-absd_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:unsigned-vec-absd_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvsub 'bvumax 'bvumin) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-absd")]
)

	]
	[(typed:unsigned-vec-div v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:unsigned-vec-div_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:unsigned-vec-div_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:unsigned-vec-div_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:unsigned-vec-div_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:unsigned-vec-div_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:unsigned-vec-div_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-div")]
)

	]
	[(typed:unsigned-vec-halving_add v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:unsigned-vec-halving_add_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvadd 'zero-extend 'bvudiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:unsigned-vec-halving_add_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvadd 'zero-extend 'bvudiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:unsigned-vec-halving_add_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvadd 'zero-extend 'bvudiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:unsigned-vec-halving_add_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvadd 'zero-extend 'bvudiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:unsigned-vec-halving_add_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvadd 'zero-extend 'bvudiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:unsigned-vec-halving_add_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvadd 'zero-extend 'bvudiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-halving_add")]
)

	]
	[(typed:unsigned-vec-max v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:unsigned-vec-max_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:unsigned-vec-max_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:unsigned-vec-max_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:unsigned-vec-max_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:unsigned-vec-max_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:unsigned-vec-max_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'bvumax 'bvugt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-max")]
)

	]
	[(typed:unsigned-vec-min v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:unsigned-vec-min_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:unsigned-vec-min_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:unsigned-vec-min_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:unsigned-vec-min_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:unsigned-vec-min_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:unsigned-vec-min_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'bvumin 'bvult 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-min")]
)

	]
	[(typed:unsigned-vec-mod v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:unsigned-vec-mod_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:unsigned-vec-mod_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:unsigned-vec-mod_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:unsigned-vec-mod_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:unsigned-vec-mod_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:unsigned-vec-mod_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'bvurem 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-mod")]
)

	]
	[(typed:unsigned-vec-mul v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:unsigned-vec-mul_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:unsigned-vec-mul_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:unsigned-vec-mul_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:unsigned-vec-mul_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:unsigned-vec-mul_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:unsigned-vec-mul_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-mul")]
)

	]
	[(typed:unsigned-vec-rounding_halving_add v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvadd 'zero-extend 'bvudiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:unsigned-vec-rounding_halving_add_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvadd 'zero-extend 'bvudiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:unsigned-vec-rounding_halving_add_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvadd 'zero-extend 'bvudiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:unsigned-vec-rounding_halving_add_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvadd 'zero-extend 'bvudiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:unsigned-vec-rounding_halving_add_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvadd 'zero-extend 'bvudiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:unsigned-vec-rounding_halving_add_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvadd 'zero-extend 'bvudiv) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-rounding_halving_add")]
)

	]
	[(typed:unsigned-vec-rounding_mul_shift_right v0 v1 v2 num_3 prec_i_o)
		(cond 
		[(and  (equal? num_3 16) (equal? prec_i_o 1024)); typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'bvmul 'bvshl 'bvlshr 'bvusat 'bvudiv 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1) (typed:halide:get-bv-ops v2)))]
		[(and  (equal? num_3 16) (equal? prec_i_o 2048)); typed:unsigned-vec-rounding_mul_shift_right_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'bvmul 'bvshl 'bvlshr 'bvusat 'bvudiv 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1) (typed:halide:get-bv-ops v2)))]
		[(and  (equal? num_3 32) (equal? prec_i_o 1024)); typed:unsigned-vec-rounding_mul_shift_right_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'bvmul 'bvshl 'bvlshr 'bvusat 'bvudiv 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1) (typed:halide:get-bv-ops v2)))]
		[(and  (equal? num_3 32) (equal? prec_i_o 2048)); typed:unsigned-vec-rounding_mul_shift_right_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'bvmul 'bvshl 'bvlshr 'bvusat 'bvudiv 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1) (typed:halide:get-bv-ops v2)))]
		[(and  (equal? num_3 8) (equal? prec_i_o 1024)); typed:unsigned-vec-rounding_mul_shift_right_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'bvmul 'bvshl 'bvlshr 'bvusat 'bvudiv 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1) (typed:halide:get-bv-ops v2)))]
		[(and  (equal? num_3 8) (equal? prec_i_o 2048)); typed:unsigned-vec-rounding_mul_shift_right_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'bvmul 'bvshl 'bvlshr 'bvusat 'bvudiv 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1) (typed:halide:get-bv-ops v2)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-rounding_mul_shift_right")]
)

	]
	[(typed:unsigned-vec-rounding_shift_right v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:unsigned-vec-rounding_shift_right_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'bvshl 'bvlshr 'bvusat 'bvudiv 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:unsigned-vec-rounding_shift_right_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'bvshl 'bvlshr 'bvusat 'bvudiv 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:unsigned-vec-rounding_shift_right_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'bvshl 'bvlshr 'bvusat 'bvudiv 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:unsigned-vec-rounding_shift_right_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'bvshl 'bvlshr 'bvusat 'bvudiv 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:unsigned-vec-rounding_shift_right_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'bvshl 'bvlshr 'bvusat 'bvudiv 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:unsigned-vec-rounding_shift_right_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'bvshl 'bvlshr 'bvusat 'bvudiv 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-rounding_shift_right")]
)

	]
	[(typed:unsigned-vec-sat-add v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:unsigned-vec-sat-add_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:unsigned-vec-sat-add_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:unsigned-vec-sat-add_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:unsigned-vec-sat-add_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:unsigned-vec-sat-add_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:unsigned-vec-sat-add_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'bvaddnuw 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-sat-add")]
)

	]
	[(typed:unsigned-vec-sat-sub v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:unsigned-vec-sat-sub_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:unsigned-vec-sat-sub_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:unsigned-vec-sat-sub_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:unsigned-vec-sat-sub_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:unsigned-vec-sat-sub_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:unsigned-vec-sat-sub_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'bvsubnuw 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-sat-sub")]
)

	]
	[(typed:unsigned-vec-shr v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:unsigned-vec-shr_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:unsigned-vec-shr_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:unsigned-vec-shr_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:unsigned-vec-shr_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:unsigned-vec-shr_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:unsigned-vec-shr_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-shr")]
)

	]
	[(typed:unsigned-vec-widen-mul v0 v1 prec_i_o size_i)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i 1024)); typed:unsigned-vec-widen-mul_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i 1024)); typed:unsigned-vec-widen-mul_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'bvmul 'extract 'zero-extend) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-widen-mul")]
)

	]
	[(typed:vec-add v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:vec-add_p16_s1024_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:vec-add_p16_s2048_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:vec-add_p32_s1024_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:vec-add_p32_s2048_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:vec-add_p8_s1024_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:vec-add_p8_s2048_signed_None
 
  (remove-duplicates (append (list  'bvadd 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:vec-add")]
)

	]
	[(typed:vec-bwand v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:vec-bwand_p16_s1024_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:vec-bwand_p16_s2048_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:vec-bwand_p32_s1024_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:vec-bwand_p32_s2048_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:vec-bwand_p8_s1024_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:vec-bwand_p8_s2048_signed_None
 
  (remove-duplicates (append (list  'bvand 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:vec-bwand")]
)

	]
	[(typed:vec-bwnot v0 num_1 prec_i_o)
		(cond 
		[(and  (equal? num_1 16) (equal? prec_i_o 1024)); typed:vec-bwnot_p16_s1024_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 16) (equal? prec_i_o 2048)); typed:vec-bwnot_p16_s2048_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 32) (equal? prec_i_o 1024)); typed:vec-bwnot_p32_s1024_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 32) (equal? prec_i_o 2048)); typed:vec-bwnot_p32_s2048_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 8) (equal? prec_i_o 1024)); typed:vec-bwnot_p8_s1024_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? num_1 8) (equal? prec_i_o 2048)); typed:vec-bwnot_p8_s2048_signed_None
 
  (remove-duplicates (append (list  'bvnot 'extract) (typed:halide:get-bv-ops v0)))]
		[else (error "Unable to get ops  for typed:vec-bwnot")]
)

	]
	[(typed:vec-saturate v0 prec_i num_2 num_3 prec_o bool_5)
		(cond 
		[(and  (equal? prec_i 16) (equal? num_2 0) (equal? num_3 128) (equal? prec_o 8)); typed:vec-saturate_0_ip16_is2048_op8_os1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? num_2 0) (equal? num_3 128) (equal? prec_o 8)); typed:vec-saturate_0_ip16_is2048_op8_os1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? num_2 0) (equal? num_3 64) (equal? prec_o 16)); typed:vec-saturate_0_ip32_is2048_op16_os1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? num_2 0) (equal? num_3 64) (equal? prec_o 16)); typed:vec-saturate_0_ip32_is2048_op16_os1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? num_2 1) (equal? num_3 128) (equal? prec_o 8)); typed:vec-saturate_1_ip16_is2048_op8_os1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 16) (equal? num_2 1) (equal? num_3 128) (equal? prec_o 8)); typed:vec-saturate_1_ip16_is2048_op8_os1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? num_2 1) (equal? num_3 64) (equal? prec_o 16)); typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvusat 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? prec_i 32) (equal? num_2 1) (equal? num_3 64) (equal? prec_o 16)); typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_1
 
  (remove-duplicates (append (list  'extract 'bvssat 'concat) (typed:halide:get-bv-ops v0)))]
		[else (error "Unable to get ops  for typed:vec-saturate")]
)

	]
	[(typed:vec-shl v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:vec-shl_p16_s1024_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:vec-shl_p16_s2048_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:vec-shl_p32_s1024_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:vec-shl_p32_s2048_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:vec-shl_p8_s1024_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:vec-shl_p8_s2048_signed_None
 
  (remove-duplicates (append (list  'extract 'bvshl) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:vec-shl")]
)

	]
	[(typed:vec-sub v0 v1 num_2 prec_i_o)
		(cond 
		[(and  (equal? num_2 16) (equal? prec_i_o 1024)); typed:vec-sub_p16_s1024_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 16) (equal? prec_i_o 2048)); typed:vec-sub_p16_s2048_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 1024)); typed:vec-sub_p32_s1024_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 32) (equal? prec_i_o 2048)); typed:vec-sub_p32_s2048_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 1024)); typed:vec-sub_p8_s1024_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? num_2 8) (equal? prec_i_o 2048)); typed:vec-sub_p8_s2048_signed_None
 
  (remove-duplicates (append (list  'bvsub 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:vec-sub")]
)

	]
	[(typed:xBroadcast v0 size_i prec_i_o num_3)
		(cond 
		[(and  (equal? size_i 32) (equal? prec_i_o 32) (equal? num_3 32)); typed:xBroadcast_is32_os1024_signed_None
 
  (remove-duplicates (append (list  'extract 'concat) (typed:halide:get-bv-ops v0)))]
		[(and  (equal? size_i 32) (equal? prec_i_o 32) (equal? num_3 64)); typed:xBroadcast_is32_os2048_signed_None
 
  (remove-duplicates (append (list  'extract 'concat) (typed:halide:get-bv-ops v0)))]
		[else (error "Unable to get ops  for typed:xBroadcast")]
)

	]
[(typed:vec-eq v0 v1 prec_i size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? size_i 1024)); typed:vec-eq_p16_s1024_signed_None
 
  (remove-duplicates (append (list  'if 'extract 'bveq 'eq) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 16) (equal? size_i 2048)); typed:vec-eq_p16_s2048_signed_None
 
  (remove-duplicates (append (list  'if 'extract 'bveq 'eq) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 32) (equal? size_i 1024)); typed:vec-eq_p32_s1024_signed_None
 
  (remove-duplicates (append (list  'if 'extract 'bveq 'eq) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 32) (equal? size_i 2048)); typed:vec-eq_p32_s2048_signed_None
 
  (remove-duplicates (append (list  'if 'extract 'bveq 'eq) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 8) (equal? size_i 1024)); typed:vec-eq_p8_s1024_signed_None
 
  (remove-duplicates (append (list  'if 'extract 'bveq 'eq) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 8) (equal? size_i 2048)); typed:vec-eq_p8_s2048_signed_None
 
  (remove-duplicates (append (list  'if 'extract 'bveq 'eq) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:vec-eq")]
)

	]

	[(typed:signed-vec-le v0 v1 prec_i size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? size_i 1024)); typed:signed-vec-le_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'bvslt 'bvsle 'bveq 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 16) (equal? size_i 2048)); typed:signed-vec-le_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'bvslt 'bvsle 'bveq 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 32) (equal? size_i 1024)); typed:signed-vec-le_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'bvslt 'bvsle 'bveq 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 32) (equal? size_i 2048)); typed:signed-vec-le_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'bvslt 'bvsle 'bveq 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 8) (equal? size_i 1024)); typed:signed-vec-le_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'bvslt 'bvsle 'bveq 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 8) (equal? size_i 2048)); typed:signed-vec-le_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'bvslt 'bvsle 'bveq 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-le")]
)

	]
	[(typed:signed-vec-lt v0 v1 prec_i size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? size_i 1024)); typed:signed-vec-lt_p16_s1024_signed_1
 
  (remove-duplicates (append (list  'bvslt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 16) (equal? size_i 2048)); typed:signed-vec-lt_p16_s2048_signed_1
 
  (remove-duplicates (append (list  'bvslt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 32) (equal? size_i 1024)); typed:signed-vec-lt_p32_s1024_signed_1
 
  (remove-duplicates (append (list  'bvslt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 32) (equal? size_i 2048)); typed:signed-vec-lt_p32_s2048_signed_1
 
  (remove-duplicates (append (list  'bvslt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 8) (equal? size_i 1024)); typed:signed-vec-lt_p8_s1024_signed_1
 
  (remove-duplicates (append (list  'bvslt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 8) (equal? size_i 2048)); typed:signed-vec-lt_p8_s2048_signed_1
 
  (remove-duplicates (append (list  'bvslt 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:signed-vec-lt")]
)

	]

	[(typed:unsigned-vec-le v0 v1 prec_i size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? size_i 1024)); typed:unsigned-vec-le_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'bvult 'bvule 'bveq 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 16) (equal? size_i 2048)); typed:unsigned-vec-le_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'bvult 'bvule 'bveq 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 32) (equal? size_i 1024)); typed:unsigned-vec-le_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'bvult 'bvule 'bveq 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 32) (equal? size_i 2048)); typed:unsigned-vec-le_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'bvult 'bvule 'bveq 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 8) (equal? size_i 1024)); typed:unsigned-vec-le_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'bvult 'bvule 'bveq 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 8) (equal? size_i 2048)); typed:unsigned-vec-le_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'bvult 'bvule 'bveq 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-le")]
)

	]
	[(typed:unsigned-vec-lt v0 v1 prec_i size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? size_i 1024)); typed:unsigned-vec-lt_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'bvult 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 16) (equal? size_i 2048)); typed:unsigned-vec-lt_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'bvult 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 32) (equal? size_i 1024)); typed:unsigned-vec-lt_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'bvult 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 32) (equal? size_i 2048)); typed:unsigned-vec-lt_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'bvult 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 8) (equal? size_i 1024)); typed:unsigned-vec-lt_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'bvult 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 8) (equal? size_i 2048)); typed:unsigned-vec-lt_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'bvult 'extract) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-lt")]
)

	]
[(typed:vec-eq v0 v1 prec_i size_i)
		(cond 
		[(and  (equal? prec_i 16) (equal? size_i 1024)); typed:vec-eq_p16_s1024_signed_None
 
  (remove-duplicates (append (list  'if 'extract 'bveq 'eq) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 16) (equal? size_i 2048)); typed:vec-eq_p16_s2048_signed_None
 
  (remove-duplicates (append (list  'if 'extract 'bveq 'eq) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 32) (equal? size_i 1024)); typed:vec-eq_p32_s1024_signed_None
 
  (remove-duplicates (append (list  'if 'extract 'bveq 'eq) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 32) (equal? size_i 2048)); typed:vec-eq_p32_s2048_signed_None
 
  (remove-duplicates (append (list  'if 'extract 'bveq 'eq) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 8) (equal? size_i 1024)); typed:vec-eq_p8_s1024_signed_None
 
  (remove-duplicates (append (list  'if 'extract 'bveq 'eq) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[(and  (equal? prec_i 8) (equal? size_i 2048)); typed:vec-eq_p8_s2048_signed_None
 
  (remove-duplicates (append (list  'if 'extract 'bveq 'eq) (typed:halide:get-bv-ops v0) (typed:halide:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:vec-eq")]
)

	]

    [_ (list)]
 )
)
;; ================================================================================
