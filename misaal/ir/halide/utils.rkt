#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require rosette/lib/destruct)

(require hydride/utils/bvops)
(require hydride/utils/misc)


(require hydride/ir/hydride/definition)
(require misaal/ir/halide/types)
(require misaal/ir/halide/length)
(require misaal/ir/halide/prec)

(require hydride/halide)

(require 
  (only-in racket/base error)
  )


(provide (all-defined-out))

(define (is-halide-expr-signed? expr)
  (define elemT (typed-get-elemT expr))

  (cond 
    [(equal? elemT 'int1) #t]
    [(equal? elemT 'int8) #t]
    [(equal? elemT 'int16) #t]
    [(equal? elemT 'int32) #t]
    [(equal? elemT 'int64) #t]
    [(equal? elemT 'uint1) #t]
    [(equal? elemT 'uint8) #f]
    [(equal? elemT 'uint16) #f]
    [(equal? elemT 'uint32) #f]
    [(equal? elemT 'uint64) #f]
    [else
      (error "Unrecognized elemtT ~a" elemT)
      ]
    )
  )


(define (typed-get-elemT expr)
  (destruct expr 
            [(buffer-index index elemT buffSize) elemT]
            [(typed:int-imm data prec signed?) (halide:size-to-elemT-signed (bvlength data) signed?) ]
            [ (typed:cast-int v0 prec_i isigned? num_3 prec_o)
             (halide:size-to-elemT-signed prec_o #t)
             ]
            [ (typed:cast-uint v0 prec_i isigned? num_3 prec_o)
             (halide:size-to-elemT-signed prec_o #f)
             ]
            [ (typed:concat_vectors v0 v1 prec_i_o size_i)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-abs v0 num_1 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-absd v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-div v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-halving_add v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-max v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-min v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-mod v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-mul v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-rounding_halving_add v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-rounding_mul_shift_right v0 v1 v2 num_3 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-rounding_shift_right v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-sat-add v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-sat-sub v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-shr v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:signed-vec-widen-mul v0 v1 prec_i_o size_i)
             (typed-get-elemT v0)
             ]
            [ (typed:slice_vectors v0 num_1 num_2 num_3 prec_i_o size_i)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-absd v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-div v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-halving_add v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-max v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-min v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-mod v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-mul v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-rounding_halving_add v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-rounding_mul_shift_right v0 v1 v2 num_3 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-rounding_shift_right v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-sat-add v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-sat-sub v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-shr v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:unsigned-vec-widen-mul v0 v1 prec_i_o size_i)
             (typed-get-elemT v0)
             ]
            [ (typed:vec-add v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:vec-bwand v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:vec-bwnot v0 num_1 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:vec-saturate v0 prec_i num_2 num_3 prec_o bool_5)
             (typed-get-elemT v0)
             ]
            [ (typed:vec-shl v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:vec-sub v0 v1 num_2 prec_i_o)
             (typed-get-elemT v0)
             ]
            [ (typed:xBroadcast v0 size_i prec_i_o num_3)
             (typed-get-elemT v0)
             ]
            [_ 
              (println expr)
              (error "Unrecognized expression in visitor ~a" expr)
              ]
            )

  )

(define empty-vector (vector))

;; Map halide expressions to typed halide expressions
(define (convert-halide-to-typed-halide halide-expr id-map)
  (define expr-map (make-hash))

  (define (reference expr)
    (hash-ref! expr-map expr -1)
    )

  (define (visitor-fn expr)
    (define mapped-expr
        (destruct expr
                  [(xBroadcast sca factor)
                   (typed:xBroadcast sca (typed:halide:get-prec sca empty-vector) (typed:halide:get-length sca empty-vector) factor)
                   ]

                  [(int-imm data signed?)
                   (typed:int-imm data (bvlength data) signed?)
                   ]

                  [(ramp base stride len)
                   (typed:ramp base stride len)
                   ]

                  [(buffer data elemT buffsize)
                   (define index (hash-ref! id-map expr -1))
                   (buffer-index (bitvector->integer index) elemT buffsize)
                   ]

                  [(cast-int vec olane oprec)
                   (define isigned? (is-halide-expr-signed? vec))
                   (typed:cast-int vec (typed:halide:get-prec vec empty-vector) isigned? olane oprec)
                   ]

                  [(cast-uint vec olane oprec)
                   (define isigned? (is-halide-expr-signed? vec))
                   (typed:cast-uint vec (typed:halide:get-prec vec empty-vector) isigned? olane oprec)
                   ]

                  [(vec-saturate vec olane oprec signed?)
                   (define isigned? (is-halide-expr-signed? vec))
                   (typed:vec-saturate vec (typed:halide:get-prec vec empty-vector) isigned? olane oprec signed?)
                   ]
                  [(vec-add v1 v2)
                   (typed:vec-add v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector))
                   ]

                  [(vec-sub v1 v2)
                   (typed:vec-sub v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector))
                   ]

                  [(vec-shl v1 v2)
                   (typed:vec-shl v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector))
                   ]

                  [(vec-sat-add v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-sat-add v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-sat-add v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                  [(vec-sat-sub v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-sat-sub v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-sat-sub v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]
                [(vec-mul v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-mul v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-mul v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]
                [(vec-widen-mul v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-widen-mul v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-widen-mul v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vec-rounding_shift_right v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-rounding_shift_right v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-rounding_shift_right v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vec-rounding_mul_shift_right v1 v2 v3)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-rounding_mul_shift_right v1 v2 v3 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-rounding_mul_shift_right v1 v2 v3 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vec-rounding_halving_add v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-rounding_halving_add v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-rounding_halving_add v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vec-halving_add v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-halving_add v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-halving_add v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vec-div v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-div v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-div v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vec-mod v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-mod v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-mod v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vec-min v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-min v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-min v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vec-max v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-max v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-max v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vec-shr v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-shr v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-shr v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vec-absd v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-absd v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-absd v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vec-abs v1 )
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-abs v1  (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (error "Abs only applicable to signed values")
                        ]
                      )
                   ]

                [(vec-clz v1 )
                 (typed:vec-clz v1 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector))
                 ]

                [(vec-eq v1 v2)
                 (typed:vec-eq v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector))
                 ]

                [(vec-if v1 v2 v3 )
                 (typed:vec-if v1 v2 v3 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector))
                 ]

                [(vec-bwnot v1 )
                 (typed:vec-bwnot v1  (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector))
                 ]

                [(vec-broadcast n v1)
                 (typed:vec-broadcast n v1  (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector))
                 ]

                [(slice_vectors vec base stride len )
                 (typed:slice_vectors vec base stride len  (typed:halide:get-prec vec empty-vector) (typed:halide:get-length vec empty-vector))
                 ]

                [(concat_vectors v1 v2 )
                 (typed:concat_vectors v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector))
                 ]


                [(vec-lt v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-lt v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-lt v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vec-le v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:signed-vec-le v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:unsigned-vec-le v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vec-bwand v1 v2)
                    (define isigned? (is-halide-expr-signed? v1))
                    (cond 
                      [isigned?
                        (typed:vec-bwand v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]

                      [else
                        (typed:vec-bwand v1 v2 (typed:halide:get-prec v1 empty-vector) (typed:halide:get-length v1 empty-vector) )
                        ]
                      )
                   ]

                [(vector_reduce op width vec)
                    (define isigned? (is-halide-expr-signed? vec))
                    (cond 
                      [isigned?
                        (typed:signed-vector_reduce_add  width vec (typed:halide:get-prec vec empty-vector) (typed:halide:get-length vec empty-vector) )
                        ]

                      [else

                        (typed:unsigned-vector_reduce_add  width vec (typed:halide:get-prec vec empty-vector) (typed:halide:get-length vec empty-vector) )
                        ]
                      )
                   ]
                [_ expr]
                  )
        )
    (hash-set! expr-map mapped-expr expr)
    mapped-expr

    )
  (halide:visit halide-expr visitor-fn)
  
  )

;; EggLog Utils

(define (emit-integer-to-egglog val)
  ;(string-append "(INT " (~s val) ")")
  (string-append "" (~s val) "")
  )

(define (emit-bool-to-egglog val)
  (cond
    [val
        ;(string-append "(INT " (~s 1) ")")
        (string-append " " (~s 1) "")
      ]
    [else

        ;(string-append "(INT " (~s 0) ")")
        (string-append " " (~s 0) "")
      
      ]
    
    )
  )

(define (emit-expr-to-egglog expr)
(destruct expr 
            [(buffer-index index elemT buffSize) (string-append "reg_" (~s index) "\n")]

            [(typed:int-imm data prec signed?) (string-append "(LIT " (~s (bitvector->integer data)) " " (~s prec) ")\n") ]
            [ (typed:cast-int v0 prec_i isigned? num_3 prec_o)
             (string-append "\n(typed-cast-int " (emit-expr-to-egglog v0) " "  (emit-integer-to-egglog prec_i) " " (emit-bool-to-egglog isigned?) " " (emit-integer-to-egglog num_3) " " 
                            (emit-integer-to-egglog prec_o) ")\n")
             ]
            [ (typed:cast-uint v0 prec_i isigned? num_3 prec_o)
             (string-append "\n(typed-cast-uint " (emit-expr-to-egglog v0) " "  (emit-integer-to-egglog prec_i) " " (emit-bool-to-egglog isigned?) " " (emit-integer-to-egglog num_3) " " 
                            (emit-integer-to-egglog prec_o) ")\n")
             ]
            [ (typed:concat_vectors v0 v1 prec_i_o size_i)
             (string-append "\n(typed-concat_vectors " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog prec_i_o) " " (emit-integer-to-egglog size_i) ")\n")
             ]
            [ (typed:signed-vec-abs v0 num_1 prec_i_o)
             (string-append "\n(typed-signed-vec-abs " (emit-expr-to-egglog v0) " "  (emit-integer-to-egglog num_1) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:signed-vec-absd v0 v1 num_2 prec_i_o)

             (string-append "\n(typed-signed-vec-absd " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:signed-vec-div v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-signed-vec-div " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:signed-vec-halving_add v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-signed-vec-halving_add " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:signed-vec-max v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-signed-vec-max " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:signed-vec-min v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-signed-vec-min " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:signed-vec-mod v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-signed-vec-mod " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:signed-vec-mul v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-signed-vec-mul " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:signed-vec-rounding_halving_add v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-signed-vec-rounding_halving_add " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:signed-vec-rounding_mul_shift_right v0 v1 v2 num_3 prec_i_o)
             (string-append "\n(typed-signed-vec-rounding_mul_shift_right " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-expr-to-egglog v2) " " (emit-integer-to-egglog num_3) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:signed-vec-rounding_shift_right v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-signed-vec-rounding_shift_right " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:signed-vec-sat-add v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-signed-vec-sat-add " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]

            [ (typed:signed-vec-sat-sub v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-signed-vec-sat-sub " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:signed-vec-shr v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-signed-vec-shr " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:signed-vec-widen-mul v0 v1 prec_i_o size_i)
             (string-append "\n(typed-signed-vec-widen-mul " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog prec_i_o) " " (emit-integer-to-egglog size_i) ")\n")
             ]
            [ (typed:slice_vectors v0 num_1 num_2 num_3 prec_i_o size_i)
             (string-append "\n(typed-slice_vectors " (emit-expr-to-egglog v0)  " " (emit-integer-to-egglog num_1) " " (emit-integer-to-egglog num_2)  " " (emit-integer-to-egglog num_3)  " " (emit-integer-to-egglog prec_i_o)  " "   (emit-integer-to-egglog size_i)")\n")
             ]
            [ (typed:unsigned-vec-absd v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-unsigned-vec-absd " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:unsigned-vec-div v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-unsigned-vec-div " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:unsigned-vec-halving_add v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-unsigned-vec-halving_add " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:unsigned-vec-max v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-unsigned-vec-max " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:unsigned-vec-min v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-unsigned-vec-min " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:unsigned-vec-mod v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-unsigned-vec-mod " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:unsigned-vec-mul v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-unsigned-vec-mul " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:unsigned-vec-rounding_halving_add v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-unsigned-vec-rounding_halving_add " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:unsigned-vec-rounding_mul_shift_right v0 v1 v2 num_3 prec_i_o)
             (string-append "\n(typed-unsigned-vec-rounding_mul_shift_right" (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-expr-to-egglog v2) " " (emit-integer-to-egglog num_3) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:unsigned-vec-rounding_shift_right v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-unsigned-vec-rounding_shift_right " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:unsigned-vec-sat-add v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-unsigned-vec-sat-add " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:unsigned-vec-sat-sub v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-unsigned-vec-sat-sub " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:unsigned-vec-shr v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-unsigned-vec-shr " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:unsigned-vec-widen-mul v0 v1 prec_i_o size_i)
             (string-append "\n(typed-unsigned-vec-widen-mul " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog prec_i_o) " " (emit-integer-to-egglog size_i) ")\n")
             ]
            [ (typed:vec-add v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-vec-add " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:vec-bwand v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-vec-bwand " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:vec-bwnot v0 num_1 prec_i_o)
             (string-append "\n(typed-vec-bwnot " (emit-expr-to-egglog v0) " "  (emit-integer-to-egglog num_1) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:vec-saturate v0 prec_i num_2 num_3 prec_o bool_5)
             (string-append "\n(typed-vec-saturate " (emit-expr-to-egglog v0) " "  (emit-integer-to-egglog prec_i) " " (emit-bool-to-egglog num_2) " " (emit-integer-to-egglog num_3) " "  
                            (emit-integer-to-egglog prec_o) " "
                            (emit-bool-to-egglog bool_5) " "
                            ")\n")
             ]
            [ (typed:vec-shl v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-vec-shl " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:vec-sub v0 v1 num_2 prec_i_o)
             (string-append "\n(typed-vec-sub " (emit-expr-to-egglog v0) " " (emit-expr-to-egglog v1) " " (emit-integer-to-egglog num_2) " " (emit-integer-to-egglog prec_i_o) ")\n")
             ]
            [ (typed:xBroadcast v0 size_i prec_i_o num_3)

             (string-append "\n(typed-xBroadcast " (emit-expr-to-egglog v0)  " " (emit-integer-to-egglog size_i) " " (emit-integer-to-egglog prec_i_o) " " (emit-integer-to-egglog num_3)  ")\n")
             ]
            [_ 
              (println expr)
              (error "Unrecognized expression in visitor ~a" expr)
              ]
            )
  )
