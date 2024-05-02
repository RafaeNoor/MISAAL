#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require rosette/lib/destruct)
(require hydride)
(require misaal)
(require "./semantics.rkt")
(require "./definition.rkt")
(require "./interpreter.rkt")
(require "./cost.rkt")


(define (spec-expr env)
  (hexagon_V6_vrmpybv_128B (bv 0 1024) (vector-ref env 0) (vector-ref env 1)
                           1024 32 0 32 8 -1 1 1 16 1 0
                           )
  )


(define v1 (create-tensor 1 128 8))
(define v2 (create-tensor 1 128 8))

;(set! v2 (create-splat 5 128 8))

(set! v1 (?? (bitvector 1024)))
(set! v2 (?? (bitvector 1024)))

(set! v1 (create-concrete-bv 1024))
(set! v2 (create-concrete-bv 1024))

(define vfull (concat v1 v2))

(define (extract-fn i)
  (define low (* i 8))
  (define high (+ low 7))
  (extract high low vfull)
  )

(define env (build-vector 256 extract-fn))



(define spec-env (vector v1 v2))

(define-grammar 
  (test-grammar)
  [expr_start 
    (choose 
      (repair-reduce-add_dsl
        4
        (expr-4-32b-vec)
        32
        128

        )
      )
    ]


  [expr-4-32b-vec
    (choose 
      (repair-max_dsl (expr-4-32b-vec) (expr-4-32b-vec) 32 128)
      (repair-min_dsl (expr-4-32b-vec) (expr-4-32b-vec) 32 128)
      (repair-add_dsl (expr-4-32b-vec) (expr-4-32b-vec) 32 128)
      (repair-sub_dsl (expr-4-32b-vec) (expr-4-32b-vec) 32 128)
      (repair-sat-add_dsl (expr-4-32b-vec) (expr-4-32b-vec) 32 128)
      (repair-sat-sub_dsl (expr-4-32b-vec) (expr-4-32b-vec) 32 128)
      (repair-mul_dsl (expr-4-32b-vec) (expr-4-32b-vec) 32 128)
      (repair-widen-mul_dsl (expr-4-8b-vec) (expr-4-8b-vec) 8 32 32)
      (repair-widen-mul_dsl (expr-4-16b-vec) (expr-4-16b-vec) 16 32 64)
      (repair-sext_dsl (expr-4-8b-vec)  8 32 32)
      (repair-sext_dsl (expr-4-16b-vec)  16 32 64)
      )
    ]


  [expr-4-16b-vec
    (choose 
      (repair-max_dsl (expr-4-16b-vec) (expr-4-16b-vec) 16 64)
      (repair-min_dsl (expr-4-16b-vec) (expr-4-16b-vec) 16 64)
      (repair-add_dsl (expr-4-16b-vec) (expr-4-16b-vec) 16 64)
      (repair-sub_dsl (expr-4-16b-vec) (expr-4-16b-vec) 16 64)
      (repair-sat-add_dsl (expr-4-16b-vec) (expr-4-16b-vec) 16 64)
      (repair-sat-sub_dsl (expr-4-16b-vec) (expr-4-16b-vec) 16 64)
      (repair-mul_dsl (expr-4-16b-vec) (expr-4-16b-vec) 16 64)
      (repair-widen-mul_dsl (expr-4-8b-vec) (expr-4-8b-vec) 8 16 32)
      (repair-sext_dsl (expr-4-8b-vec)  8 16 32)
      )
    ]

  [expr-4-8b-vec
    (choose 
      (repair-max_dsl (expr-4-8b-vec) (expr-4-8b-vec) 8 64)
      (repair-min_dsl (expr-4-8b-vec) (expr-4-8b-vec) 8 64)
      (repair-add_dsl (expr-4-8b-vec) (expr-4-8b-vec) 8 64)
      (repair-sub_dsl (expr-4-8b-vec) (expr-4-8b-vec) 8 64)
      (repair-sat-add_dsl (expr-4-8b-vec) (expr-4-8b-vec) 8 64)
      (repair-sat-sub_dsl (expr-4-8b-vec) (expr-4-8b-vec) 8 64)
      (repair-mul_dsl (expr-4-8b-vec) (expr-4-8b-vec) 8 64)
      (repair-build-vector_dsl 4 (list 252 253 254 255))
      (repair-build-vector_dsl 4 (list 124 125 126 127))
      )
    ]
  )



(define (test-grammar-depth k) (test-grammar  #:depth k #:start expr_start))
(define repair-synth (test-grammar-depth 3))

(define synth-result (repair:interpret repair-synth env))

(define spec-result-full (spec-expr spec-env))

(define i 0)
(define adjusted_i (- 31 i))
(define result.i.low (* adjusted_i 32))
(define result.i.high (+ result.i.low 31))
(define result.i (extract result.i.high result.i.low spec-result-full))
(printf "Result i ~a\n" (bitvector->integer result.i))

(define test-expr 
  (repair-build-vector_dsl 4 (list 252 253 254 255))
  )
(define test-check (repair:interpret test-expr env))
(print-mat test-check 1 4 8)

(define test-expr-2 
  (repair-build-vector_dsl 4 (list 124 125 126 127))
  )

(define test-check-2 (repair:interpret test-expr-2 env))
(print-mat test-check-2 1 4 8)

(displayln "Launching synthesis")
(define start (current-seconds))
(define optimize? #t)
(define sol?
  (cond
    [optimize?
      (optimize #:minimize (list (repair:cost repair-synth ))
                  #:guarantee (begin
                                (assert (equal? synth-result result.i))
                                )
                  )
     ]
    [else 

      (synthesize #:forall (list env)
                  #:guarantee (begin
                                (assert (equal? synth-result result.i))
                                )
                  )
      ]

    )
  )

(define end (current-seconds))
(printf "Synthesis took ~a seconds ...\n" (- end start))


(define synth-expr (evaluate repair-synth sol?))
(pretty-print synth-expr)
(println (repair:cost synth-expr))
