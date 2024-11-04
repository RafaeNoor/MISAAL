
        #lang rosette
        (require rosette/lib/synthax)
        (require rosette/lib/angelic)
        (require racket/pretty)
        (require rosette/lib/destruct)
        (require hydride)
        (require misaal)

        ;; Uncomment the line below to enable verbose logging
        (enable-debug)
        (custodian-limit-memory (current-custodian) (* 10000 1024 1024))
        (current-bitwidth 16)
        
(define (hexagon_V6_vlsrwv_128B  VvV.norm %arg0.norm VuV.norm %vectsize0.norm %outerlanesize0.norm %innerlaneoffset0.norm %innerlanesize0.norm %elemsize0.norm %arg1.norm %arg2.norm )
(define VdV.norm
(apply
concat
(for/list ([%outer.it.norm (reverse (range 0 %vectsize0.norm %outerlanesize0.norm))])
 (apply
 concat
 (for/list ([i.new0.norm (reverse (range %innerlaneoffset0.norm %innerlanesize0.norm %elemsize0.norm))])
  (define %lastidx0.norm (-  %elemsize0.norm  1))
  (define %1.norm (+  i.new0.norm  %lastidx0.norm))
  (define %2.norm (extract  %1.norm i.new0.norm VvV.norm))
  (define %3.ab0.norm (bvgt %2.norm %arg0.norm %arg1.norm ))
  (define %6.norm (extract  %1.norm i.new0.norm VuV.norm))
  (define %10.norm (bvlshr  %6.norm  %2.norm))
  (define %17.norm (bvshl  %6.norm  %2.norm))
  (define %18.norm (if (equal? %3.ab0.norm #t) %10.norm %17.norm))
  %18.norm
 )
 )
)
)
)
(bvpadhighbits  VdV.norm %arg2.norm)
)

;; ================================================================================
;;                                Struct Definitions
;; ================================================================================
(struct typed:unsigned-vec-shr (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct typed:unsigned-vec-div (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct hexagon_V6_vlsrwv_128B_dsl (v0 vc_1 v2 size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9) #:transparent #:mutable)
;; ================================================================================

;; ================================================================================
;;                                DSL Cost Model
;; ================================================================================
(define cost_typed:unsigned-vec-shr 1)
(define cost_typed:unsigned-vec-div 1)
(define cost_hexagon_V6_vlsrwv_128B_dsl 1)

(define (double_target_:cost prog)
 (destruct prog
	[(reg id) 1]
	[(buffer-index id ty size) 1]
	[(lit v) 1 ]
		[ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(+ 4 (double_target_:cost  v0)  (double_target_:cost  v1)  
		 
		)
	]
		[ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(+ 4 (double_target_:cost  v0)  (double_target_:cost  v1)  
		)
	]
		[ (interleave-vector_dsl v0 size_i_o prec_i_o)
		(+ 3 (double_target_:cost  v0) )
	]
		[ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(+ 3 (double_target_:cost  v0) )
	]
		[ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(+ 5 (double_target_:cost  v0)  (double_target_:cost  v1)  
		 (double_target_:cost  v4) )
	]
		[ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (double_target_:cost  v0)  (double_target_:cost  v1)  
		)
	]
		[ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (double_target_:cost  v0)  (double_target_:cost  v1)  
		)
	]
		[ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (double_target_:cost  v0)  (double_target_:cost  v1)  
		)
	]
		[ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (double_target_:cost  v0)  (double_target_:cost  v1)  
		)
	]
		[ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(+ 2 (double_target_:cost  v0)  (double_target_:cost  v1)  
		)
	]
		[ (llvm-zext_dsl v0 size_i size_o)
		(+ 1 (double_target_:cost  v0) )
	]
		[ (scalar_splat_dsl v0 size_i size_o)
		(+ 1 (double_target_:cost  v0) )
	]
	[ (typed:unsigned-vec-shr v0 v1 prec_i_o size_i_o)
		(+ cost_typed:unsigned-vec-shr (double_target_:cost  v0)  (double_target_:cost  v1)  
		)
	]
	[ (typed:unsigned-vec-div v0 v1 prec_i_o size_i_o)
		(+ cost_typed:unsigned-vec-div (double_target_:cost  v0)  (double_target_:cost  v1)  
		)
	]
	[ (hexagon_V6_vlsrwv_128B_dsl v0 vc_1 v2 size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9)
		(+ cost_hexagon_V6_vlsrwv_128B_dsl (double_target_:cost  v0)  (double_target_:cost  vc_1)  (double_target_:cost  v2)  
		 
		 
		)
	]
	[v  (error "Unrecognized Term in cost model" v)]
 )
)
;; ================================================================================

;; ================================================================================
;;                                DSL Interpreter
;; ================================================================================
(define (double_target_:interpret prog env)
 (destruct prog
	[(reg id) (vector-ref-bv env id)]
	[(buffer-index id ty size) (vector-ref env id)]
	[(lit v) v]
	[ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(vector-two-input-swizzle (double_target_:interpret v0 env) (double_target_:interpret v1 env) num_2 
		 prec_i_o num_4 num_5 
		 num_6 num_7 num_8)
	]
	[ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(interleave-vectors (double_target_:interpret v0 env) (double_target_:interpret v1 env) size_i_o 
		 prec_i_o)
	]
	[ (interleave-vector_dsl v0 size_i_o prec_i_o)
		(interleave-vector (double_target_:interpret v0 env) size_i_o prec_i_o)
	]
	[ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(deinterleave-vector (double_target_:interpret v0 env) size_i_o prec_i_o)
	]
	[ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(llvm_shuffle_vectors (double_target_:interpret v0 env) (double_target_:interpret v1 env) num_2 
		 prec_i_o (double_target_:interpret v4 env) num_5)
	]
	[ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-add (double_target_:interpret v0 env) (double_target_:interpret v1 env) num_2 
		 prec_i_o)
	]
	[ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-sub (double_target_:interpret v0 env) (double_target_:interpret v1 env) num_2 
		 prec_i_o)
	]
	[ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-mul (double_target_:interpret v0 env) (double_target_:interpret v1 env) num_2 
		 prec_i_o)
	]
	[ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-sdiv (double_target_:interpret v0 env) (double_target_:interpret v1 env) num_2 
		 prec_i_o)
	]
	[ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-udiv (double_target_:interpret v0 env) (double_target_:interpret v1 env) num_2 
		 prec_i_o)
	]
	[ (llvm-zext_dsl v0 size_i size_o)
		(llvm-zext (double_target_:interpret v0 env) size_i size_o)
	]
	[ (scalar_splat_dsl v0 size_i size_o)
		(scalar_splat (double_target_:interpret v0 env) size_i size_o)
	]
	[ (typed:unsigned-vec-shr v0 v1 prec_i_o size_i_o)
		(do-typed:unsigned-shr (double_target_:interpret v0 env) (double_target_:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (typed:unsigned-vec-div v0 v1 prec_i_o size_i_o)
		(do-typed:unsigned-div (double_target_:interpret v0 env) (double_target_:interpret v1 env) prec_i_o 
		 size_i_o)
	]
	[ (hexagon_V6_vlsrwv_128B_dsl v0 vc_1 v2 size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9)
		(hexagon_V6_vlsrwv_128B (double_target_:interpret v0 env) (double_target_:interpret vc_1 env) (double_target_:interpret v2 env) 
		 size_i_o num_4 num_5 
		 num_6 prec_i_o num_8 
		 num_9)
	]
	[v (error "Unrecognized Term in Interpreter" v)]
 )
)
;; ================================================================================

;; ================================================================================
;;                                DSL Get Length
;; ================================================================================
(define (double_target_:get-length prog env)
 (destruct prog
	[(dim-x id) 1]
	[(dim-y id) 1]
	[(idx-i id) 1]
	[(idx-j id) 1]
	[(reg id) (bvlength (vector-ref-bv env id))]
	[(lit v) (bvlength v)]
	[(nop v1) (double_target_:get-length v1 env)]
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
	[(typed:unsigned-vec-shr v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4096)) 4096]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 512)) 512]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4096)) 4096]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 512)) 512]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4096)) 4096]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 512)) 512]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4096)) 4096]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 512)) 512]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for typed:unsigned-vec-shr: "  prog)]
)

	]
	[(typed:unsigned-vec-div v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4096)) 4096]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 512)) 512]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4096)) 4096]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 512)) 512]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4096)) 4096]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 512)) 512]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 1024]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 128]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 2048]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 256]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4096)) 4096]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 512)) 512]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer length for typed:unsigned-vec-div: "  prog)]
)

	]
	[(hexagon_V6_vlsrwv_128B_dsl v0 vc_1 v2 size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9)
		(cond 
		[(and  (equal? size_i_o 1024) (equal? num_4 1024) (equal? num_5 0) (equal? num_6 1024) (equal? prec_i_o 32) (equal? num_8 1) (equal? num_9 0)) 1024]
		[(and  (equal? size_i_o 1024) (equal? num_4 1024) (equal? num_5 0) (equal? num_6 1024) (equal? prec_i_o 16) (equal? num_8 1) (equal? num_9 0)) 1024]
		[else (error "Unable to infer length for hexagon_V6_vlsrwv_128B: "  prog)]
)

	]
 )
)
;; ================================================================================

;; ================================================================================
;;                                DSL Get Output Precision
;; ================================================================================
(define (double_target_:get-prec prog env)
 (destruct prog
	[(dim-x id) 1]
	[(dim-y id) 1]
	[(idx-i id) 1]
	[(idx-j id) 1]
	[(reg id) (bvlength (vector-ref-bv env id))] ;; FIX-ME NOTE: DO NOT USE THIS METHOD FOR PREC
	[(lit v) (bvlength v)]
	[(nop v1) (double_target_:get-prec v1 env)]
	[(idx-add i1 i2) 1]
	[(idx-mul i1 i2) 1]
	[(vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8) num_2]
	[(interleave-vectors_dsl v0 v1 size_i_o prec_i_o) prec_i_o]
	[(interleave-vector_dsl v0 size_i_o prec_i_o) prec_i_o]
	[(deinterleave-vector_dsl v0 size_i_o prec_i_o) prec_i_o]
	[(llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5) prec_i_o]
	[(llvm-vect-add_dsl v0 v1 num_2 prec_i_o) prec_i_o ]
	[(llvm-vect-sub_dsl v0 v1 num_2 prec_i_o) prec_i_o ]
	[(llvm-vect-mul_dsl v0 v1 num_2 prec_i_o) prec_i_o ]
	[(llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o) prec_i_o ]
	[(llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o) prec_i_o ]
	[(typed:unsigned-vec-shr v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4096)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 512)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4096)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 512)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 1024)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2048)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4096)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 512)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4096)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 512)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-shr")]
)

	]
	[(typed:unsigned-vec-div v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4096)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 512)) 16]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)) 16]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4096)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 512)) 32]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)) 32]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 1024)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2048)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4096)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 512)) 64]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)) 64]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4096)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 512)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)) 8]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)) 8]
		[else (error "Unable to infer prec for typed:unsigned-vec-div")]
)

	]
	[(hexagon_V6_vlsrwv_128B_dsl v0 vc_1 v2 size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9)
		(cond 
		[(and  (equal? size_i_o 1024) (equal? num_4 1024) (equal? num_5 0) (equal? num_6 1024) (equal? prec_i_o 32) (equal? num_8 1) (equal? num_9 0)) 32]
		[(and  (equal? size_i_o 1024) (equal? num_4 1024) (equal? num_5 0) (equal? num_6 1024) (equal? prec_i_o 16) (equal? num_8 1) (equal? num_9 0)) 16]
		[else (error "Unable to infer prec for hexagon_V6_vlsrwv_128B")]
)

	]
	
[
v
 
1
]
 )
)
;; ================================================================================

;; ================================================================================
;;                                DSL Custom Printer
;; ================================================================================
(define (double_target_:hydride-printer  prog)
 (destruct prog
	[(dim-x id) (string-append "\n"  "(dim-x " (~s id) ")")]
	[(dim-y id) (string-append "\n" "(dim-y " (~s id) ")")]
	[(idx-i id) (string-append "\n" "(idx-i " (~s id) ")")]
	[(idx-j id) (string-append "\n" "(idx-j " (~s id) ")")]
	[(reg id) (string-append  "\n" "(reg " (~s  (bitvector->natural id)) ")")]
	[(lit v) (string-append   "(lit " (~s v) ")")]
	[(nop v1) (string-append "\n" "(nop " (double_target_:hydride-printer v1) ")")]
	[(idx-add i1 i2) (string-append "\n" "(idx-add " (~s i1) (~s i2) ")" )]
	[(idx-mul i1 i2) (string-append "\n" "(idx-mul " (~s i1) (~s i2) ")" )]
	[(vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8) 
	(string-append "\n" 
	(string-append "(vector-two-input-swizzle_dsl " (if (lit? v0) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v0 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v0 (vector 0)) (double_target_:get-prec v0 (vector 0))) (/ (double_target_:get-prec v0 (vector 0))) )] [else (values (/ (double_target_:get-length v0 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v0) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v0)) " " " " (if (lit? v1) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v1 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v1 (vector 0)) (double_target_:get-prec v1 (vector 0))) (/ (double_target_:get-prec v1 (vector 0))) )] [else (values (/ (double_target_:get-length v1 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v1) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v1)) " " " " (if (lit? num_2) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_2 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_2 (vector 0)) (double_target_:get-prec num_2 (vector 0))) (/ (double_target_:get-prec num_2 (vector 0))) )] [else (values (/ (double_target_:get-length num_2 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_2) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_2)) " " " " (if (lit? prec_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length prec_i_o (vector 0)) (double_target_:get-prec prec_i_o (vector 0))) (/ (double_target_:get-prec prec_i_o (vector 0))) )] [else (values (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer prec_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer prec_i_o)) " " " " (if (lit? num_4) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_4 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_4 (vector 0)) (double_target_:get-prec num_4 (vector 0))) (/ (double_target_:get-prec num_4 (vector 0))) )] [else (values (/ (double_target_:get-length num_4 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_4) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_4)) " " " " (if (lit? num_5) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_5 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_5 (vector 0)) (double_target_:get-prec num_5 (vector 0))) (/ (double_target_:get-prec num_5 (vector 0))) )] [else (values (/ (double_target_:get-length num_5 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_5) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_5)) " " " " (if (lit? num_6) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_6 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_6 (vector 0)) (double_target_:get-prec num_6 (vector 0))) (/ (double_target_:get-prec num_6 (vector 0))) )] [else (values (/ (double_target_:get-length num_6 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_6) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_6)) " " " " (if (lit? num_7) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_7 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_7 (vector 0)) (double_target_:get-prec num_7 (vector 0))) (/ (double_target_:get-prec num_7 (vector 0))) )] [else (values (/ (double_target_:get-length num_7 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_7) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_7)) " " " " (if (lit? num_8) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_8 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_8 (vector 0)) (double_target_:get-prec num_8 (vector 0))) (/ (double_target_:get-prec num_8 (vector 0))) )] [else (values (/ (double_target_:get-length num_8 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_8) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_8)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
	[(interleave-vectors_dsl v0 v1 size_i_o prec_i_o) 
	(string-append "\n" 
	(string-append "(interleave-vectors_dsl " (if (lit? v0) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v0 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v0 (vector 0)) (double_target_:get-prec v0 (vector 0))) (/ (double_target_:get-prec v0 (vector 0))) )] [else (values (/ (double_target_:get-length v0 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v0) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v0)) " " " " (if (lit? v1) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v1 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v1 (vector 0)) (double_target_:get-prec v1 (vector 0))) (/ (double_target_:get-prec v1 (vector 0))) )] [else (values (/ (double_target_:get-length v1 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v1) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v1)) " " " " (if (lit? size_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length size_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length size_i_o (vector 0)) (double_target_:get-prec size_i_o (vector 0))) (/ (double_target_:get-prec size_i_o (vector 0))) )] [else (values (/ (double_target_:get-length size_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer size_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer size_i_o)) " " " " (if (lit? prec_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length prec_i_o (vector 0)) (double_target_:get-prec prec_i_o (vector 0))) (/ (double_target_:get-prec prec_i_o (vector 0))) )] [else (values (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer prec_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer prec_i_o)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
	[(interleave-vector_dsl v0 size_i_o prec_i_o) 
	(string-append "\n" 
	(string-append "(interleave-vector_dsl " (if (lit? v0) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v0 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v0 (vector 0)) (double_target_:get-prec v0 (vector 0))) (/ (double_target_:get-prec v0 (vector 0))) )] [else (values (/ (double_target_:get-length v0 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v0) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v0)) " " " " (if (lit? size_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length size_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length size_i_o (vector 0)) (double_target_:get-prec size_i_o (vector 0))) (/ (double_target_:get-prec size_i_o (vector 0))) )] [else (values (/ (double_target_:get-length size_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer size_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer size_i_o)) " " " " (if (lit? prec_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length prec_i_o (vector 0)) (double_target_:get-prec prec_i_o (vector 0))) (/ (double_target_:get-prec prec_i_o (vector 0))) )] [else (values (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer prec_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer prec_i_o)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
	[(deinterleave-vector_dsl v0 size_i_o prec_i_o) 
	(string-append "\n" 
	(string-append "(deinterleave-vector_dsl " (if (lit? v0) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v0 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v0 (vector 0)) (double_target_:get-prec v0 (vector 0))) (/ (double_target_:get-prec v0 (vector 0))) )] [else (values (/ (double_target_:get-length v0 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v0) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v0)) " " " " (if (lit? size_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length size_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length size_i_o (vector 0)) (double_target_:get-prec size_i_o (vector 0))) (/ (double_target_:get-prec size_i_o (vector 0))) )] [else (values (/ (double_target_:get-length size_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer size_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer size_i_o)) " " " " (if (lit? prec_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length prec_i_o (vector 0)) (double_target_:get-prec prec_i_o (vector 0))) (/ (double_target_:get-prec prec_i_o (vector 0))) )] [else (values (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer prec_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer prec_i_o)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
	[(llvm-vect-add_dsl v0 v1 num_2 prec_i_o) 
	(string-append "\n" 
	(string-append "(llvm-vect-add_dsl " (if (lit? v0) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v0 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v0 (vector 0)) (double_target_:get-prec v0 (vector 0))) (/ (double_target_:get-prec v0 (vector 0))) )] [else (values (/ (double_target_:get-length v0 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v0) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v0)) " " " " (if (lit? v1) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v1 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v1 (vector 0)) (double_target_:get-prec v1 (vector 0))) (/ (double_target_:get-prec v1 (vector 0))) )] [else (values (/ (double_target_:get-length v1 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v1) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v1)) " " " " (if (lit? num_2) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_2 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_2 (vector 0)) (double_target_:get-prec num_2 (vector 0))) (/ (double_target_:get-prec num_2 (vector 0))) )] [else (values (/ (double_target_:get-length num_2 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_2) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_2)) " " " " (if (lit? prec_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length prec_i_o (vector 0)) (double_target_:get-prec prec_i_o (vector 0))) (/ (double_target_:get-prec prec_i_o (vector 0))) )] [else (values (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer prec_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer prec_i_o)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
	[(llvm-vect-sub_dsl v0 v1 num_2 prec_i_o) 
	(string-append "\n" 
	(string-append "(llvm-vect-sub_dsl " (if (lit? v0) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v0 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v0 (vector 0)) (double_target_:get-prec v0 (vector 0))) (/ (double_target_:get-prec v0 (vector 0))) )] [else (values (/ (double_target_:get-length v0 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v0) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v0)) " " " " (if (lit? v1) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v1 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v1 (vector 0)) (double_target_:get-prec v1 (vector 0))) (/ (double_target_:get-prec v1 (vector 0))) )] [else (values (/ (double_target_:get-length v1 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v1) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v1)) " " " " (if (lit? num_2) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_2 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_2 (vector 0)) (double_target_:get-prec num_2 (vector 0))) (/ (double_target_:get-prec num_2 (vector 0))) )] [else (values (/ (double_target_:get-length num_2 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_2) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_2)) " " " " (if (lit? prec_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length prec_i_o (vector 0)) (double_target_:get-prec prec_i_o (vector 0))) (/ (double_target_:get-prec prec_i_o (vector 0))) )] [else (values (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer prec_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer prec_i_o)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
	[(llvm-vect-mul_dsl v0 v1 num_2 prec_i_o) 
	(string-append "\n" 
	(string-append "(llvm-vect-mul_dsl " (if (lit? v0) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v0 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v0 (vector 0)) (double_target_:get-prec v0 (vector 0))) (/ (double_target_:get-prec v0 (vector 0))) )] [else (values (/ (double_target_:get-length v0 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v0) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v0)) " " " " (if (lit? v1) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v1 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v1 (vector 0)) (double_target_:get-prec v1 (vector 0))) (/ (double_target_:get-prec v1 (vector 0))) )] [else (values (/ (double_target_:get-length v1 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v1) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v1)) " " " " (if (lit? num_2) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_2 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_2 (vector 0)) (double_target_:get-prec num_2 (vector 0))) (/ (double_target_:get-prec num_2 (vector 0))) )] [else (values (/ (double_target_:get-length num_2 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_2) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_2)) " " " " (if (lit? prec_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length prec_i_o (vector 0)) (double_target_:get-prec prec_i_o (vector 0))) (/ (double_target_:get-prec prec_i_o (vector 0))) )] [else (values (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer prec_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer prec_i_o)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
	[(llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o) 
	(string-append "\n" 
	(string-append "(llvm-vect-sdiv_dsl " (if (lit? v0) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v0 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v0 (vector 0)) (double_target_:get-prec v0 (vector 0))) (/ (double_target_:get-prec v0 (vector 0))) )] [else (values (/ (double_target_:get-length v0 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v0) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v0)) " " " " (if (lit? v1) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v1 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v1 (vector 0)) (double_target_:get-prec v1 (vector 0))) (/ (double_target_:get-prec v1 (vector 0))) )] [else (values (/ (double_target_:get-length v1 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v1) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v1)) " " " " (if (lit? num_2) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_2 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_2 (vector 0)) (double_target_:get-prec num_2 (vector 0))) (/ (double_target_:get-prec num_2 (vector 0))) )] [else (values (/ (double_target_:get-length num_2 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_2) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_2)) " " " " (if (lit? prec_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length prec_i_o (vector 0)) (double_target_:get-prec prec_i_o (vector 0))) (/ (double_target_:get-prec prec_i_o (vector 0))) )] [else (values (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer prec_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer prec_i_o)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
	[(llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o) 
	(string-append "\n" 
	(string-append "(llvm-vect-udiv_dsl " (if (lit? v0) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v0 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v0 (vector 0)) (double_target_:get-prec v0 (vector 0))) (/ (double_target_:get-prec v0 (vector 0))) )] [else (values (/ (double_target_:get-length v0 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v0) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v0)) " " " " (if (lit? v1) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v1 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v1 (vector 0)) (double_target_:get-prec v1 (vector 0))) (/ (double_target_:get-prec v1 (vector 0))) )] [else (values (/ (double_target_:get-length v1 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v1) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v1)) " " " " (if (lit? num_2) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_2 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_2 (vector 0)) (double_target_:get-prec num_2 (vector 0))) (/ (double_target_:get-prec num_2 (vector 0))) )] [else (values (/ (double_target_:get-length num_2 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_2) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_2)) " " " " (if (lit? prec_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length prec_i_o (vector 0)) (double_target_:get-prec prec_i_o (vector 0))) (/ (double_target_:get-prec prec_i_o (vector 0))) )] [else (values (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer prec_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer prec_i_o)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
	[(llvm-zext_dsl v0 size_i size_o) 
	(string-append "\n" 
	(string-append "(llvm-zext_dsl " (if (lit? v0) (double_target_:hydride-printer v0) (double_target_:hydride-printer v0)) " " " " (if (lit? size_i) (double_target_:hydride-printer size_i) (double_target_:hydride-printer size_i)) " " " " (if (lit? size_o) (double_target_:hydride-printer size_o) (double_target_:hydride-printer size_o)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
	[(scalar_splat_dsl v0 size_i size_o) 
	(string-append "\n" 
	(string-append "(scalar_splat_dsl " (if (lit? v0) (double_target_:hydride-printer v0) (double_target_:hydride-printer v0)) " " " " (if (lit? size_i) (double_target_:hydride-printer size_i) (double_target_:hydride-printer size_i)) " " " " (if (lit? size_o) (double_target_:hydride-printer size_o) (double_target_:hydride-printer size_o)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
[(typed:unsigned-vec-shr v0 v1 prec_i_o size_i_o) 
	(string-append "\n" 
	(string-append "(typed:unsigned-vec-shr " (if (lit? v0) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v0 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v0 (vector 0)) (double_target_:get-prec v0 (vector 0))) (/ (double_target_:get-prec v0 (vector 0))) )] [else (values (/ (double_target_:get-length v0 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v0) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v0)) " " " " (if (lit? v1) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v1 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v1 (vector 0)) (double_target_:get-prec v1 (vector 0))) (/ (double_target_:get-prec v1 (vector 0))) )] [else (values (/ (double_target_:get-length v1 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v1) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v1)) " " " " (if (lit? prec_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length prec_i_o (vector 0)) (double_target_:get-prec prec_i_o (vector 0))) (/ (double_target_:get-prec prec_i_o (vector 0))) )] [else (values (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer prec_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer prec_i_o)) " " " " (if (lit? size_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length size_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length size_i_o (vector 0)) (double_target_:get-prec size_i_o (vector 0))) (/ (double_target_:get-prec size_i_o (vector 0))) )] [else (values (/ (double_target_:get-length size_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer size_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer size_i_o)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
[(typed:unsigned-vec-div v0 v1 prec_i_o size_i_o) 
	(string-append "\n" 
	(string-append "(typed:unsigned-vec-div " (if (lit? v0) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v0 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v0 (vector 0)) (double_target_:get-prec v0 (vector 0))) (/ (double_target_:get-prec v0 (vector 0))) )] [else (values (/ (double_target_:get-length v0 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v0) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v0)) " " " " (if (lit? v1) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v1 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v1 (vector 0)) (double_target_:get-prec v1 (vector 0))) (/ (double_target_:get-prec v1 (vector 0))) )] [else (values (/ (double_target_:get-length v1 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v1) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v1)) " " " " (if (lit? prec_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length prec_i_o (vector 0)) (double_target_:get-prec prec_i_o (vector 0))) (/ (double_target_:get-prec prec_i_o (vector 0))) )] [else (values (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer prec_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer prec_i_o)) " " " " (if (lit? size_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length size_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length size_i_o (vector 0)) (double_target_:get-prec size_i_o (vector 0))) (/ (double_target_:get-prec size_i_o (vector 0))) )] [else (values (/ (double_target_:get-length size_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer size_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer size_i_o)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
[(hexagon_V6_vlsrwv_128B_dsl v0 vc_1 v2 size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9) 
	(string-append "\n" 
	(string-append "(hexagon_V6_vlsrwv_128B_dsl " (if (lit? v0) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v0 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v0 (vector 0)) (double_target_:get-prec v0 (vector 0))) (/ (double_target_:get-prec v0 (vector 0))) )] [else (values (/ (double_target_:get-length v0 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v0) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v0)) " " " " (if (lit? vc_1) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length vc_1 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length vc_1 (vector 0)) (double_target_:get-prec vc_1 (vector 0))) (/ (double_target_:get-prec vc_1 (vector 0))) )] [else (values (/ (double_target_:get-length vc_1 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer vc_1) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer vc_1)) " " " " (if (lit? v2) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length v2 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length v2 (vector 0)) (double_target_:get-prec v2 (vector 0))) (/ (double_target_:get-prec v2 (vector 0))) )] [else (values (/ (double_target_:get-length v2 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer v2) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer v2)) " " " " (if (lit? size_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length size_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length size_i_o (vector 0)) (double_target_:get-prec size_i_o (vector 0))) (/ (double_target_:get-prec size_i_o (vector 0))) )] [else (values (/ (double_target_:get-length size_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer size_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer size_i_o)) " " " " (if (lit? num_4) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_4 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_4 (vector 0)) (double_target_:get-prec num_4 (vector 0))) (/ (double_target_:get-prec num_4 (vector 0))) )] [else (values (/ (double_target_:get-length num_4 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_4) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_4)) " " " " (if (lit? num_5) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_5 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_5 (vector 0)) (double_target_:get-prec num_5 (vector 0))) (/ (double_target_:get-prec num_5 (vector 0))) )] [else (values (/ (double_target_:get-length num_5 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_5) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_5)) " " " " (if (lit? num_6) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_6 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_6 (vector 0)) (double_target_:get-prec num_6 (vector 0))) (/ (double_target_:get-prec num_6 (vector 0))) )] [else (values (/ (double_target_:get-length num_6 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_6) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_6)) " " " " (if (lit? prec_i_o) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length prec_i_o (vector 0)) (double_target_:get-prec prec_i_o (vector 0))) (/ (double_target_:get-prec prec_i_o (vector 0))) )] [else (values (/ (double_target_:get-length prec_i_o (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer prec_i_o) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer prec_i_o)) " " " " (if (lit? num_8) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_8 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_8 (vector 0)) (double_target_:get-prec num_8 (vector 0))) (/ (double_target_:get-prec num_8 (vector 0))) )] [else (values (/ (double_target_:get-length num_8 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_8) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_8)) " " " " (if (lit? num_9) (begin (define-values (num_elem arg_prec) (cond [(< (/ (double_target_:get-length num_9 (vector 0)) prec_i_o) 1)  (values  (/ (double_target_:get-length num_9 (vector 0)) (double_target_:get-prec num_9 (vector 0))) (/ (double_target_:get-prec num_9 (vector 0))) )] [else (values (/ (double_target_:get-length num_9 (vector 0)) prec_i_o) prec_i_o)]))(string-append (double_target_:hydride-printer num_9) " ; " "<" (~s num_elem) " x i" (~s arg_prec) ">" "\n" )) (double_target_:hydride-printer num_9)) " " " " ")")
	(string-append ";" "<" (~s (/ (double_target_:get-length prog (vector 0)) (double_target_:get-prec prog (vector 0))) ) " x " "i" (~s (double_target_:get-prec prog (vector 0))) ">") "\n")]
	[v (pretty-format v)]
 )
)
;; ================================================================================

;; ================================================================================
;;                                DSL Binder
;; ================================================================================
(define (double_target_:bind-expr prog env)
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
		(vector-two-input-swizzle_dsl (double_target_:bind-expr v0 env) (double_target_:bind-expr v1 env) (double_target_:bind-expr num_2 env) 
		 (double_target_:bind-expr prec_i_o env) (double_target_:bind-expr num_4 env) (double_target_:bind-expr num_5 env) 
		 (double_target_:bind-expr num_6 env) (double_target_:bind-expr num_7 env) (double_target_:bind-expr num_8 env))
	]
	[ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(interleave-vectors_dsl (double_target_:bind-expr v0 env) (double_target_:bind-expr v1 env) (double_target_:bind-expr size_i_o env) 
		 (double_target_:bind-expr prec_i_o env))
	]
	[ (interleave-vector_dsl v0 size_i_o prec_i_o)
		(interleave-vector_dsl (double_target_:bind-expr v0 env) (double_target_:bind-expr size_i_o env) (double_target_:bind-expr prec_i_o env))
	]
	[ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(deinterleave-vector_dsl (double_target_:bind-expr v0 env) (double_target_:bind-expr size_i_o env) (double_target_:bind-expr prec_i_o env))
	]
	[ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(llvm_shuffle_vectors_dsl (double_target_:bind-expr v0 env) (double_target_:bind-expr v1 env) (double_target_:bind-expr num_2 env) 
		 (double_target_:bind-expr prec_i_o env) (double_target_:bind-expr v4 env) (double_target_:bind-expr num_5 env))
	]
	[ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-add_dsl (double_target_:bind-expr v0 env) (double_target_:bind-expr v1 env) (double_target_:bind-expr num_2 env) 
		 (double_target_:bind-expr prec_i_o env))
	]
	[ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-sub_dsl (double_target_:bind-expr v0 env) (double_target_:bind-expr v1 env) (double_target_:bind-expr num_2 env) 
		 (double_target_:bind-expr prec_i_o env))
	]
	[ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-mul_dsl (double_target_:bind-expr v0 env) (double_target_:bind-expr v1 env) (double_target_:bind-expr num_2 env) 
		 (double_target_:bind-expr prec_i_o env))
	]
	[ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-sdiv_dsl (double_target_:bind-expr v0 env) (double_target_:bind-expr v1 env) (double_target_:bind-expr num_2 env) 
		 (double_target_:bind-expr prec_i_o env))
	]
	[ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(llvm-vect-udiv_dsl (double_target_:bind-expr v0 env) (double_target_:bind-expr v1 env) (double_target_:bind-expr num_2 env) 
		 (double_target_:bind-expr prec_i_o env))
	]
	[ (llvm-zext_dsl v0 size_i size_o)
		(llvm-zext_dsl (double_target_:bind-expr v0 env) (double_target_:bind-expr size_i env) (double_target_:bind-expr size_o env))
	]
	[ (scalar_splat_dsl v0 size_i size_o)
		(scalar_splat_dsl (double_target_:bind-expr v0 env) (double_target_:bind-expr size_i env) (double_target_:bind-expr size_o env))
	]
	[ (typed:unsigned-vec-shr v0 v1 prec_i_o size_i_o)
		(typed:unsigned-vec-shr (double_target_:bind-expr v0 env) (double_target_:bind-expr v1 env) (double_target_:bind-expr prec_i_o env) 
		 (double_target_:bind-expr size_i_o env))
	]
	[ (typed:unsigned-vec-div v0 v1 prec_i_o size_i_o)
		(typed:unsigned-vec-div (double_target_:bind-expr v0 env) (double_target_:bind-expr v1 env) (double_target_:bind-expr prec_i_o env) 
		 (double_target_:bind-expr size_i_o env))
	]
	[ (hexagon_V6_vlsrwv_128B_dsl v0 vc_1 v2 size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9)
		(hexagon_V6_vlsrwv_128B_dsl (double_target_:bind-expr v0 env) (double_target_:bind-expr vc_1 env) (double_target_:bind-expr v2 env) 
		 (double_target_:bind-expr size_i_o env) (double_target_:bind-expr num_4 env) (double_target_:bind-expr num_5 env) 
		 (double_target_:bind-expr num_6 env) (double_target_:bind-expr prec_i_o env) (double_target_:bind-expr num_8 env) 
		 (double_target_:bind-expr num_9 env))
	]
	[v v]
 )
)
;; ================================================================================

;; ================================================================================
;;                                Hydride Visitor 
;; ================================================================================
(define (double_target_:visitor prog fn)
 (destruct prog
	[(dim-x id) (fn prog)]
	[(dim-y id) (fn prog)]
	[(idx-i id) (fn prog)]
	[(idx-j id) (fn prog)]
	[(reg id) (fn prog) ]
	[(buffer-index id type size) (fn prog) ]
	[(lit v) (fn prog)]
	[(nop v1) (double_target_:visitor v1 fn)]
	[(idx-add i1 i2) (fn prog) ]
	[(idx-mul i1 i2) (fn prog) ]
	[ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(define v0-visited (double_target_:visitor v0 fn))
		(define v1-visited (double_target_:visitor v1 fn))
		(fn ( vector-two-input-swizzle_dsl v0-visited v1-visited num_2 prec_i_o num_4 num_5 num_6 num_7 num_8 ))
	]
	[ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(define v0-visited (double_target_:visitor v0 fn))
		(define v1-visited (double_target_:visitor v1 fn))
		(fn ( interleave-vectors_dsl v0-visited v1-visited size_i_o prec_i_o ))
	]
	[ (interleave-vector_dsl v0 size_i_o prec_i_o)
		(define v0-visited (double_target_:visitor v0 fn))
		(fn ( interleave-vector_dsl v0-visited size_i_o prec_i_o ))
	]
	[ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(define v0-visited (double_target_:visitor v0 fn))
		(fn ( deinterleave-vector_dsl v0-visited size_i_o prec_i_o ))
	]
	[ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(define v0-visited (double_target_:visitor v0 fn))
		(define v1-visited (double_target_:visitor v1 fn))
		(define v4-visited (double_target_:visitor v4 fn))
		(fn ( llvm_shuffle_vectors_dsl v0-visited v1-visited num_2 prec_i_o v4-visited num_5 ))
	]
	[ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(define v0-visited (double_target_:visitor v0 fn))
		(define v1-visited (double_target_:visitor v1 fn))
		(fn ( llvm-vect-add_dsl v0-visited v1-visited num_2 prec_i_o ))
	]
	[ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(define v0-visited (double_target_:visitor v0 fn))
		(define v1-visited (double_target_:visitor v1 fn))
		(fn ( llvm-vect-sub_dsl v0-visited v1-visited num_2 prec_i_o ))
	]
	[ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(define v0-visited (double_target_:visitor v0 fn))
		(define v1-visited (double_target_:visitor v1 fn))
		(fn ( llvm-vect-mul_dsl v0-visited v1-visited num_2 prec_i_o ))
	]
	[ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(define v0-visited (double_target_:visitor v0 fn))
		(define v1-visited (double_target_:visitor v1 fn))
		(fn ( llvm-vect-sdiv_dsl v0-visited v1-visited num_2 prec_i_o ))
	]
	[ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(define v0-visited (double_target_:visitor v0 fn))
		(define v1-visited (double_target_:visitor v1 fn))
		(fn ( llvm-vect-udiv_dsl v0-visited v1-visited num_2 prec_i_o ))
	]
	[ (llvm-zext_dsl v0 size_i size_o)
		(define v0-visited (double_target_:visitor v0 fn))
		(fn ( llvm-zext_dsl v0-visited size_i size_o ))
	]
	[ (scalar_splat_dsl v0 size_i size_o)
		(define v0-visited (double_target_:visitor v0 fn))
		(fn ( scalar_splat_dsl v0-visited size_i size_o ))
	]
	[ (typed:unsigned-vec-shr v0 v1 prec_i_o size_i_o)
		(define v0-visited (double_target_:visitor v0 fn))
		(define v1-visited (double_target_:visitor v1 fn))
		(fn ( typed:unsigned-vec-shr v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (typed:unsigned-vec-div v0 v1 prec_i_o size_i_o)
		(define v0-visited (double_target_:visitor v0 fn))
		(define v1-visited (double_target_:visitor v1 fn))
		(fn ( typed:unsigned-vec-div v0-visited v1-visited prec_i_o size_i_o ))
	]
	[ (hexagon_V6_vlsrwv_128B_dsl v0 vc_1 v2 size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9)
		(define v0-visited (double_target_:visitor v0 fn))
		(define vc_1-visited (double_target_:visitor vc_1 fn))
		(define v2-visited (double_target_:visitor v2 fn))
		(fn ( hexagon_V6_vlsrwv_128B_dsl v0-visited vc_1-visited v2-visited size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9 ))
	]
	[_ (error "Unrecognized expression in visitor")]
 )
)
;; ================================================================================

;; ================================================================================
;;                                DSL Get Ops
;; ================================================================================
(define (double_target_:get-bv-ops prog)
 (destruct prog
	[(reg id) '()]
	[(buffer-index id type size) '()]
	[(lit v) '()]
		[(vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(remove-duplicates (append (list  'if) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))
	]
		[(interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(remove-duplicates (append (list  ) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))
	]
		[(interleave-vector_dsl v0 size_i_o prec_i_o)
		(remove-duplicates (append (list  'cond) (double_target_:get-bv-ops v0)))
	]
		[(deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(remove-duplicates (append (list  'cond) (double_target_:get-bv-ops v0)))
	]
		[(llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(remove-duplicates (append (list  'bitvector->integer 'if) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1) (double_target_:get-bv-ops v4)))
	]
		[(llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvadd) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))
	]
		[(llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvsub) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))
	]
		[(llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvmul) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))
	]
		[(llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvsdiv) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))
	]
		[(llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(remove-duplicates (append (list  'bvudiv) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))
	]
		[(llvm-zext_dsl v0 size_i size_o)
		(remove-duplicates (append (list  'zero-extend) (double_target_:get-bv-ops v0)))
	]
		[(scalar_splat_dsl v0 size_i size_o)
		(remove-duplicates (append (list  'zero-extend) (double_target_:get-bv-ops v0)))
	]
	[(typed:unsigned-vec-shr v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)); typed:unsigned-vec-shr_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); typed:unsigned-vec-shr_p16_s128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); typed:unsigned-vec-shr_p16_s16_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)); typed:unsigned-vec-shr_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); typed:unsigned-vec-shr_p16_s256_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); typed:unsigned-vec-shr_p16_s32_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4096)); typed:unsigned-vec-shr_p16_s4096_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 512)); typed:unsigned-vec-shr_p16_s512_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); typed:unsigned-vec-shr_p16_s64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)); typed:unsigned-vec-shr_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); typed:unsigned-vec-shr_p32_s128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)); typed:unsigned-vec-shr_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); typed:unsigned-vec-shr_p32_s256_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); typed:unsigned-vec-shr_p32_s32_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4096)); typed:unsigned-vec-shr_p32_s4096_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 512)); typed:unsigned-vec-shr_p32_s512_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); typed:unsigned-vec-shr_p32_s64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 1024)); typed:unsigned-vec-shr_p64_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); typed:unsigned-vec-shr_p64_s128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2048)); typed:unsigned-vec-shr_p64_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); typed:unsigned-vec-shr_p64_s256_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4096)); typed:unsigned-vec-shr_p64_s4096_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 512)); typed:unsigned-vec-shr_p64_s512_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); typed:unsigned-vec-shr_p64_s64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)); typed:unsigned-vec-shr_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); typed:unsigned-vec-shr_p8_s128_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); typed:unsigned-vec-shr_p8_s16_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)); typed:unsigned-vec-shr_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); typed:unsigned-vec-shr_p8_s256_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); typed:unsigned-vec-shr_p8_s32_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4096)); typed:unsigned-vec-shr_p8_s4096_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 512)); typed:unsigned-vec-shr_p8_s512_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); typed:unsigned-vec-shr_p8_s64_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); typed:unsigned-vec-shr_p8_s8_signed_0
 
  (remove-duplicates (append (list  'extract 'bvlshr) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-shr")]
)

	]
	[(typed:unsigned-vec-div v0 v1 prec_i_o size_i_o)
		(cond 
		[(and  (equal? prec_i_o 16) (equal? size_i_o 1024)); typed:unsigned-vec-div_p16_s1024_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 128)); typed:unsigned-vec-div_p16_s128_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 16)); typed:unsigned-vec-div_p16_s16_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 2048)); typed:unsigned-vec-div_p16_s2048_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 256)); typed:unsigned-vec-div_p16_s256_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 32)); typed:unsigned-vec-div_p16_s32_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 4096)); typed:unsigned-vec-div_p16_s4096_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 512)); typed:unsigned-vec-div_p16_s512_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 16) (equal? size_i_o 64)); typed:unsigned-vec-div_p16_s64_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 1024)); typed:unsigned-vec-div_p32_s1024_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 128)); typed:unsigned-vec-div_p32_s128_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 2048)); typed:unsigned-vec-div_p32_s2048_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 256)); typed:unsigned-vec-div_p32_s256_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 32)); typed:unsigned-vec-div_p32_s32_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 4096)); typed:unsigned-vec-div_p32_s4096_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 512)); typed:unsigned-vec-div_p32_s512_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 32) (equal? size_i_o 64)); typed:unsigned-vec-div_p32_s64_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 1024)); typed:unsigned-vec-div_p64_s1024_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 128)); typed:unsigned-vec-div_p64_s128_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 2048)); typed:unsigned-vec-div_p64_s2048_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 256)); typed:unsigned-vec-div_p64_s256_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 4096)); typed:unsigned-vec-div_p64_s4096_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 512)); typed:unsigned-vec-div_p64_s512_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 64) (equal? size_i_o 64)); typed:unsigned-vec-div_p64_s64_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 1024)); typed:unsigned-vec-div_p8_s1024_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 128)); typed:unsigned-vec-div_p8_s128_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 16)); typed:unsigned-vec-div_p8_s16_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 2048)); typed:unsigned-vec-div_p8_s2048_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 256)); typed:unsigned-vec-div_p8_s256_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 32)); typed:unsigned-vec-div_p8_s32_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 4096)); typed:unsigned-vec-div_p8_s4096_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 512)); typed:unsigned-vec-div_p8_s512_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 64)); typed:unsigned-vec-div_p8_s64_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[(and  (equal? prec_i_o 8) (equal? size_i_o 8)); typed:unsigned-vec-div_p8_s8_signed_0
 
  (remove-duplicates (append (list  'bvudiv 'extract 'zero-extend) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v1)))]
		[else (error "Unable to get ops  for typed:unsigned-vec-div")]
)

	]
	[(hexagon_V6_vlsrwv_128B_dsl v0 vc_1 v2 size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9)
		(cond 
		[(and  (equal? size_i_o 1024) (equal? num_4 1024) (equal? num_5 0) (equal? num_6 1024) (equal? prec_i_o 32) (equal? num_8 1) (equal? num_9 0)); hexagon_V6_vlsrwv_128B
 
  (remove-duplicates (append (list  'bvshl 'bvlshr 'bvsgt 'if) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v2)))]
		[(and  (equal? size_i_o 1024) (equal? num_4 1024) (equal? num_5 0) (equal? num_6 1024) (equal? prec_i_o 16) (equal? num_8 1) (equal? num_9 0)); hexagon_V6_vlsrhv_128B
 
  (remove-duplicates (append (list  'bvshl 'bvlshr 'bvsgt 'if) (double_target_:get-bv-ops v0) (double_target_:get-bv-ops v2)))]
		[else (error "Unable to get ops  for hexagon_V6_vlsrwv_128B")]
)

	]
 )
)
;; ================================================================================

;; ================================================================================
;;                                DSL Constant Fold Expression
;; ================================================================================
(define (double_target_:const-fold prog )
 (destruct prog
	[(dim-x id) (dim-x id)]
	[(dim-y id) (dim-y id)]
	[(idx-i id) (idx-i id)]
	[(idx-j id) (idx-j id)]
	[(reg id) (reg id) ]
	[(buffer-index id type size) (buffer-index id type size) ]
	[(lit v) (lit v)]
	[(nop v1) (double_target_:const-fold v1)]
	[(idx-add i1 i2)(idx-add i1 i2) ]
	[(idx-mul i1 i2) (idx-mul i1 i2) ]
	[ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(define v0-folded (double_target_:const-fold v0))
		(define v1-folded (double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( vector-two-input-swizzle_dsl v0-folded v1-folded num_2 prec_i_o num_4 num_5 num_6 num_7 num_8 ) (vector)))
]
		[else ( vector-two-input-swizzle_dsl v0-folded v1-folded num_2 prec_i_o num_4 num_5 num_6 num_7 num_8 )]
		)
	]
	[ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(define v0-folded (double_target_:const-fold v0))
		(define v1-folded (double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( interleave-vectors_dsl v0-folded v1-folded size_i_o prec_i_o ) (vector)))
]
		[else ( interleave-vectors_dsl v0-folded v1-folded size_i_o prec_i_o )]
		)
	]
	[ (interleave-vector_dsl v0 size_i_o prec_i_o)
		(define v0-folded (double_target_:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (double_target_:interpret ( interleave-vector_dsl v0-folded size_i_o prec_i_o ) (vector)))
]
		[else ( interleave-vector_dsl v0-folded size_i_o prec_i_o )]
		)
	]
	[ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(define v0-folded (double_target_:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (double_target_:interpret ( deinterleave-vector_dsl v0-folded size_i_o prec_i_o ) (vector)))
]
		[else ( deinterleave-vector_dsl v0-folded size_i_o prec_i_o )]
		)
	]
	[ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(define v0-folded (double_target_:const-fold v0))
		(define v1-folded (double_target_:const-fold v1))
		(define v4-folded (double_target_:const-fold v4))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded) (lit? v4-folded))
(lit (double_target_:interpret ( llvm_shuffle_vectors_dsl v0-folded v1-folded num_2 prec_i_o v4-folded num_5 ) (vector)))
]
		[else ( llvm_shuffle_vectors_dsl v0-folded v1-folded num_2 prec_i_o v4-folded num_5 )]
		)
	]
	[ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (double_target_:const-fold v0))
		(define v1-folded (double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( llvm-vect-add_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-add_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (double_target_:const-fold v0))
		(define v1-folded (double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( llvm-vect-sub_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-sub_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (double_target_:const-fold v0))
		(define v1-folded (double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( llvm-vect-mul_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-mul_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (double_target_:const-fold v0))
		(define v1-folded (double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( llvm-vect-sdiv_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-sdiv_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (double_target_:const-fold v0))
		(define v1-folded (double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( llvm-vect-udiv_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-udiv_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-zext_dsl v0 size_i size_o)
		(define v0-folded (double_target_:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (double_target_:interpret ( llvm-zext_dsl v0-folded size_i size_o ) (vector)))
]
		[else ( llvm-zext_dsl v0-folded size_i size_o )]
		)
	]
	[ (scalar_splat_dsl v0 size_i size_o)
		(define v0-folded (double_target_:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (double_target_:interpret ( scalar_splat_dsl v0-folded size_i size_o ) (vector)))
]
		[else ( scalar_splat_dsl v0-folded size_i size_o )]
		)
	]
	[ (typed:unsigned-vec-shr v0 v1 prec_i_o size_i_o)
		(define v0-folded (double_target_:const-fold v0))
		(define v1-folded (double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( typed:unsigned-vec-shr v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( typed:unsigned-vec-shr v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (typed:unsigned-vec-div v0 v1 prec_i_o size_i_o)
		(define v0-folded (double_target_:const-fold v0))
		(define v1-folded (double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( typed:unsigned-vec-div v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[else ( typed:unsigned-vec-div v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (hexagon_V6_vlsrwv_128B_dsl v0 vc_1 v2 size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9)
		(define v0-folded (double_target_:const-fold v0))
		(define vc_1-folded (double_target_:const-fold vc_1))
		(define v2-folded (double_target_:const-fold v2))
		(cond
		[(and (lit? v0-folded) (lit? vc_1-folded) (lit? v2-folded))
(lit (double_target_:interpret ( hexagon_V6_vlsrwv_128B_dsl v0-folded vc_1-folded v2-folded size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9 ) (vector)))
]
		[else ( hexagon_V6_vlsrwv_128B_dsl v0-folded vc_1-folded v2-folded size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9 )]
		)
	]
	[v (error "Unrecognized expression" v)]
 )
)
;; ================================================================================

;; ================================================================================
;;                                DSL Constant Fold Expression
;; ================================================================================
(define (aggressive-double_target_:const-fold prog )
 (destruct prog
	[(dim-x id) (dim-x id)]
	[(dim-y id) (dim-y id)]
	[(idx-i id) (idx-i id)]
	[(idx-j id) (idx-j id)]
	[(reg id) (reg id) ]
	[(buffer-index id type size) (buffer-index id type size) ]
	[(lit v) (lit v)]
	[(nop v1) (aggressive-double_target_:const-fold v1)]
	[(idx-add i1 i2)(idx-add i1 i2) ]
	[(idx-mul i1 i2) (idx-mul i1 i2) ]
	[ (vector-two-input-swizzle_dsl v0 v1 num_2 prec_i_o num_4 num_5 num_6 num_7 num_8)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(define v1-folded (aggressive-double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( vector-two-input-swizzle_dsl v0-folded v1-folded num_2 prec_i_o num_4 num_5 num_6 num_7 num_8 ) (vector)))
]
		[else ( vector-two-input-swizzle_dsl v0-folded v1-folded num_2 prec_i_o num_4 num_5 num_6 num_7 num_8 )]
		)
	]
	[ (interleave-vectors_dsl v0 v1 size_i_o prec_i_o)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(define v1-folded (aggressive-double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( interleave-vectors_dsl v0-folded v1-folded size_i_o prec_i_o ) (vector)))
]
		[(lit? v0-folded)
(define test-env (vector (?? (bitvector size_i_o))))
(define test-expr (interleave-vectors_dsl v0-folded (reg (bv 0 4)) size_i_o prec_i_o))
(define test-result (double_target_:interpret test-expr test-env))
(cond [(concrete? test-result) (lit test-result)]
[(equal? test-result (vector-ref test-env 0))  v1-folded]
[else ( interleave-vectors_dsl v0-folded v1-folded size_i_o prec_i_o )])
]
		[(lit? v1-folded)
(define test-env (vector (?? (bitvector size_i_o))))
(define test-expr (interleave-vectors_dsl (reg (bv 0 4)) v1-folded size_i_o prec_i_o))
(define test-result (double_target_:interpret test-expr test-env))
(cond [(concrete? test-result) (lit test-result)]
[(equal? test-result (vector-ref test-env 0))  v0-folded]
[else ( interleave-vectors_dsl v0-folded v1-folded size_i_o prec_i_o )])
]
		[else ( interleave-vectors_dsl v0-folded v1-folded size_i_o prec_i_o )]
		)
	]
	[ (interleave-vector_dsl v0 size_i_o prec_i_o)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (double_target_:interpret ( interleave-vector_dsl v0-folded size_i_o prec_i_o ) (vector)))
]
		[(lit? v0-folded)
(define test-env (vector ))
(define test-expr (interleave-vector_dsl v0-folded size_i_o prec_i_o))
(define test-result (double_target_:interpret test-expr test-env))
(cond [(concrete? test-result) (lit test-result)]
[else ( interleave-vector_dsl v0-folded size_i_o prec_i_o )])
]
		[else ( interleave-vector_dsl v0-folded size_i_o prec_i_o )]
		)
	]
	[ (deinterleave-vector_dsl v0 size_i_o prec_i_o)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (double_target_:interpret ( deinterleave-vector_dsl v0-folded size_i_o prec_i_o ) (vector)))
]
		[(lit? v0-folded)
(define test-env (vector ))
(define test-expr (deinterleave-vector_dsl v0-folded size_i_o prec_i_o))
(define test-result (double_target_:interpret test-expr test-env))
(cond [(concrete? test-result) (lit test-result)]
[else ( deinterleave-vector_dsl v0-folded size_i_o prec_i_o )])
]
		[else ( deinterleave-vector_dsl v0-folded size_i_o prec_i_o )]
		)
	]
	[ (llvm_shuffle_vectors_dsl v0 v1 num_2 prec_i_o v4 num_5)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(define v1-folded (aggressive-double_target_:const-fold v1))
		(define v4-folded (aggressive-double_target_:const-fold v4))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded) (lit? v4-folded))
(lit (double_target_:interpret ( llvm_shuffle_vectors_dsl v0-folded v1-folded num_2 prec_i_o v4-folded num_5 ) (vector)))
]
		[else ( llvm_shuffle_vectors_dsl v0-folded v1-folded num_2 prec_i_o v4-folded num_5 )]
		)
	]
	[ (llvm-vect-add_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(define v1-folded (aggressive-double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( llvm-vect-add_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-add_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-vect-sub_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(define v1-folded (aggressive-double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( llvm-vect-sub_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-sub_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-vect-mul_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(define v1-folded (aggressive-double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( llvm-vect-mul_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-mul_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-vect-sdiv_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(define v1-folded (aggressive-double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( llvm-vect-sdiv_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-sdiv_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-vect-udiv_dsl v0 v1 num_2 prec_i_o)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(define v1-folded (aggressive-double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( llvm-vect-udiv_dsl v0-folded v1-folded num_2 prec_i_o ) (vector)))
]
		[else ( llvm-vect-udiv_dsl v0-folded v1-folded num_2 prec_i_o )]
		)
	]
	[ (llvm-zext_dsl v0 size_i size_o)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (double_target_:interpret ( llvm-zext_dsl v0-folded size_i size_o ) (vector)))
]
		[(lit? v0-folded)
(define test-env (vector ))
(define test-expr (llvm-zext_dsl v0-folded size_i size_o))
(define test-result (double_target_:interpret test-expr test-env))
(cond [(concrete? test-result) (lit test-result)]
[else ( llvm-zext_dsl v0-folded size_i size_o )])
]
		[else ( llvm-zext_dsl v0-folded size_i size_o )]
		)
	]
	[ (scalar_splat_dsl v0 size_i size_o)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(cond
		[(and (lit? v0-folded))
(lit (double_target_:interpret ( scalar_splat_dsl v0-folded size_i size_o ) (vector)))
]
		[(lit? v0-folded)
(define test-env (vector ))
(define test-expr (scalar_splat_dsl v0-folded size_i size_o))
(define test-result (double_target_:interpret test-expr test-env))
(cond [(concrete? test-result) (lit test-result)]
[else ( scalar_splat_dsl v0-folded size_i size_o )])
]
		[else ( scalar_splat_dsl v0-folded size_i size_o )]
		)
	]
	[ (typed:unsigned-vec-shr v0 v1 prec_i_o size_i_o)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(define v1-folded (aggressive-double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( typed:unsigned-vec-shr v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[(lit? v0-folded)
(define test-env (vector (?? (bitvector size_i_o))))
(define test-expr (typed:unsigned-vec-shr v0-folded (reg (bv 0 4)) prec_i_o size_i_o))
(define test-result (double_target_:interpret test-expr test-env))
(cond [(concrete? test-result) (lit test-result)]
[(equal? test-result (vector-ref test-env 0))  v1-folded]
[else ( typed:unsigned-vec-shr v0-folded v1-folded prec_i_o size_i_o )])
]
		[(lit? v1-folded)
(define test-env (vector (?? (bitvector size_i_o))))
(define test-expr (typed:unsigned-vec-shr (reg (bv 0 4)) v1-folded prec_i_o size_i_o))
(define test-result (double_target_:interpret test-expr test-env))
(cond [(concrete? test-result) (lit test-result)]
[(equal? test-result (vector-ref test-env 0))  v0-folded]
[else ( typed:unsigned-vec-shr v0-folded v1-folded prec_i_o size_i_o )])
]
		[else ( typed:unsigned-vec-shr v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (typed:unsigned-vec-div v0 v1 prec_i_o size_i_o)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(define v1-folded (aggressive-double_target_:const-fold v1))
		(cond
		[(and (lit? v0-folded) (lit? v1-folded))
(lit (double_target_:interpret ( typed:unsigned-vec-div v0-folded v1-folded prec_i_o size_i_o ) (vector)))
]
		[(lit? v0-folded)
(define test-env (vector (?? (bitvector size_i_o))))
(define test-expr (typed:unsigned-vec-div v0-folded (reg (bv 0 4)) prec_i_o size_i_o))
(define test-result (double_target_:interpret test-expr test-env))
(cond [(concrete? test-result) (lit test-result)]
[(equal? test-result (vector-ref test-env 0))  v1-folded]
[else ( typed:unsigned-vec-div v0-folded v1-folded prec_i_o size_i_o )])
]
		[(lit? v1-folded)
(define test-env (vector (?? (bitvector size_i_o))))
(define test-expr (typed:unsigned-vec-div (reg (bv 0 4)) v1-folded prec_i_o size_i_o))
(define test-result (double_target_:interpret test-expr test-env))
(cond [(concrete? test-result) (lit test-result)]
[(equal? test-result (vector-ref test-env 0))  v0-folded]
[else ( typed:unsigned-vec-div v0-folded v1-folded prec_i_o size_i_o )])
]
		[else ( typed:unsigned-vec-div v0-folded v1-folded prec_i_o size_i_o )]
		)
	]
	[ (hexagon_V6_vlsrwv_128B_dsl v0 vc_1 v2 size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9)
		(define v0-folded (aggressive-double_target_:const-fold v0))
		(define vc_1-folded (aggressive-double_target_:const-fold vc_1))
		(define v2-folded (aggressive-double_target_:const-fold v2))
		(cond
		[(and (lit? v0-folded) (lit? vc_1-folded) (lit? v2-folded))
(lit (double_target_:interpret ( hexagon_V6_vlsrwv_128B_dsl v0-folded vc_1-folded v2-folded size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9 ) (vector)))
]
		[(lit? v0-folded)
(define test-env (vector (?? (bitvector size_i_o)) (?? (bitvector size_i_o))))
(define test-expr (hexagon_V6_vlsrwv_128B_dsl v0-folded (reg (bv 0 4)) (reg (bv 1 4)) size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9))
(define test-result (double_target_:interpret test-expr test-env))
(cond [(concrete? test-result) (lit test-result)]
[(equal? test-result (vector-ref test-env 0))  vc_1-folded]
[(equal? test-result (vector-ref test-env 1))  v2-folded]
[else ( hexagon_V6_vlsrwv_128B_dsl v0-folded vc_1-folded v2-folded size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9 )])
]
		[(lit? vc_1-folded)
(define test-env (vector (?? (bitvector size_i_o)) (?? (bitvector size_i_o))))
(define test-expr (hexagon_V6_vlsrwv_128B_dsl (reg (bv 0 4)) vc_1-folded (reg (bv 1 4)) size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9))
(define test-result (double_target_:interpret test-expr test-env))
(cond [(concrete? test-result) (lit test-result)]
[(equal? test-result (vector-ref test-env 0))  v0-folded]
[(equal? test-result (vector-ref test-env 1))  v2-folded]
[else ( hexagon_V6_vlsrwv_128B_dsl v0-folded vc_1-folded v2-folded size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9 )])
]
		[(lit? v2-folded)
(define test-env (vector (?? (bitvector size_i_o)) (?? (bitvector size_i_o))))
(define test-expr (hexagon_V6_vlsrwv_128B_dsl (reg (bv 0 4)) (reg (bv 1 4)) v2-folded size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9))
(define test-result (double_target_:interpret test-expr test-env))
(cond [(concrete? test-result) (lit test-result)]
[(equal? test-result (vector-ref test-env 0))  v0-folded]
[(equal? test-result (vector-ref test-env 1))  vc_1-folded]
[else ( hexagon_V6_vlsrwv_128B_dsl v0-folded vc_1-folded v2-folded size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9 )])
]
		[else ( hexagon_V6_vlsrwv_128B_dsl v0-folded vc_1-folded v2-folded size_i_o num_4 num_5 num_6 prec_i_o num_8 num_9 )]
		)
	]
	[v (error "Unrecognized expression" v)]
 )
)
;; ================================================================================

(define (src_output_hexagon_V6_vlsrwv_128B_layer_0_bv_1024) 
(choose* 
(hexagon_V6_vlsrwv_128B_dsl	;hexagon_V6_vlsrwv_128B
(choose* (reg  (bv 0 (bitvector 8))))
(lit (bv #x00000000000000000000000000000000 (bitvector 32)))				;; 32-bit Constant Bitvector operand
(choose* (reg  (bv 0 (bitvector 8))))
1024				;; Integer Operand 
1024				;; Integer Operand 
0				;; Integer Operand 
1024				;; Integer Operand 
32				;; Precision Operand 
1				;; Integer Operand 
0				;; Integer Operand 
)
(hexagon_V6_vlsrwv_128B_dsl	;hexagon_V6_vlsrhv_128B
(choose* (reg  (bv 0 (bitvector 8))))
(lit (bv #x0000000000000000 (bitvector 16)))				;; 16-bit Constant Bitvector operand
(choose* (reg  (bv 0 (bitvector 8))))
1024				;; Integer Operand 
1024				;; Integer Operand 
0				;; Integer Operand 
1024				;; Integer Operand 
16				;; Precision Operand 
1				;; Integer Operand 
0				;; Integer Operand 
)
)
)
(define src-expr
 (src_output_hexagon_V6_vlsrwv_128B_layer_0_bv_1024)
)
(define (dst_output_typed:unsigned-vec-shr_layer_0_bv_1024) 
(choose* 
(typed:unsigned-vec-shr	;typed:unsigned-vec-shr_p16_s1024_signed_0
(choose* (reg  (bv 0 (bitvector 8))))
(dst_dst_output_typed:unsigned-vec-shr_layer_0_bv_1024_arg_1_typed:unsigned-vec-div_layer_1_bv_1024)
16				;; Precision Operand 
1024				;; Integer Operand 
)
(typed:unsigned-vec-shr	;typed:unsigned-vec-shr_p32_s1024_signed_0
(choose* (reg  (bv 0 (bitvector 8))))
(dst_dst_output_typed:unsigned-vec-shr_layer_0_bv_1024_arg_1_typed:unsigned-vec-div_layer_1_bv_1024)
32				;; Precision Operand 
1024				;; Integer Operand 
)
(typed:unsigned-vec-shr	;typed:unsigned-vec-shr_p64_s1024_signed_0
(choose* (reg  (bv 0 (bitvector 8))))
(dst_dst_output_typed:unsigned-vec-shr_layer_0_bv_1024_arg_1_typed:unsigned-vec-div_layer_1_bv_1024)
64				;; Precision Operand 
1024				;; Integer Operand 
)
(typed:unsigned-vec-shr	;typed:unsigned-vec-shr_p8_s1024_signed_0
(choose* (reg  (bv 0 (bitvector 8))))
(dst_dst_output_typed:unsigned-vec-shr_layer_0_bv_1024_arg_1_typed:unsigned-vec-div_layer_1_bv_1024)
8				;; Precision Operand 
1024				;; Integer Operand 
)
)
)
(define (dst_dst_output_typed:unsigned-vec-shr_layer_0_bv_1024_arg_1_typed:unsigned-vec-div_layer_1_bv_1024) 
(choose* 
(typed:unsigned-vec-div	;typed:unsigned-vec-div_p16_s1024_signed_0
(choose* (reg  (bv 0 (bitvector 8))))
(choose* (reg  (bv 0 (bitvector 8))))
16				;; Precision Operand 
1024				;; Integer Operand 
)
(typed:unsigned-vec-div	;typed:unsigned-vec-div_p32_s1024_signed_0
(choose* (reg  (bv 0 (bitvector 8))))
(choose* (reg  (bv 0 (bitvector 8))))
32				;; Precision Operand 
1024				;; Integer Operand 
)
(typed:unsigned-vec-div	;typed:unsigned-vec-div_p64_s1024_signed_0
(choose* (reg  (bv 0 (bitvector 8))))
(choose* (reg  (bv 0 (bitvector 8))))
64				;; Precision Operand 
1024				;; Integer Operand 
)
(typed:unsigned-vec-div	;typed:unsigned-vec-div_p8_s1024_signed_0
(choose* (reg  (bv 0 (bitvector 8))))
(choose* (reg  (bv 0 (bitvector 8))))
8				;; Precision Operand 
1024				;; Integer Operand 
)
)
)
(define (invoke-spec src-expr  env)
 
(double_target_:interpret src-expr env))
(define (invoke-spec-lane src-expr lane-idx env)
 
(define low (* 32 lane-idx))
(define high (+ low (- 32 1)))
(define slice (extract high low (double_target_:interpret src-expr env)))
slice)
(define optimize? #t)
(define symbolic? #f)
(define interpreter double_target_:interpret)
(define cost-model double_target_:cost)
(define leaves-sizes (list 1024))
(define-values (satisfiable? mat-src mat-dst)  (expanded-grammar-synthesize invoke-spec invoke-spec-lane src-expr (dst_output_typed:unsigned-vec-shr_layer_0_bv_1024) leaves-sizes optimize? interpreter cost-model  symbolic? 30 'z3))
(cond [satisfiable? (write-str-to-file (~v mat-src) "g_wgw9xa.src.log.rkt")
(write-str-to-file (~v mat-dst) "g_wgw9xa.dst.log.rkt")
(exit 0)] [else (exit 1)])
