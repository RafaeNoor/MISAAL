{
    "_mm512_fmadd_epi32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm512_fmadd_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (reg (bv #x06 8)) (reg (bv #x05 8)) 64 64 -1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1))\n(define c (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b)))\n(define reg_2 (concat \n\n(extract 511 480 c)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 511 480 a) 64 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 511 480 b) 64 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 511 480 a) 64 0) (bvsizeext (extract 511 480 b) 64 0))))\n(define %11.ab0 (concat \n\n(bvsizeext (extract 511 480 c) 64 0))) \n (vector reg_0 reg_1 reg_2 %6.ab0 %7.ab0 %8 %11.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    512,
                    512,
                    512
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm512_fmadd_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (reg (bv #x06 8)) (reg (bv #x05 8)) 64 64 -1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1))\n(define c (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b)))\n(define reg_2 (concat \n\n(extract 511 480 c)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 511 480 a) 64 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 511 480 b) 64 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 511 480 a) 64 0) (bvsizeext (extract 511 480 b) 64 0))))\n(define %11.ab0 (concat \n\n(bvsizeext (extract 511 480 c) 64 0))) \n (vector reg_0 reg_1 reg_2 %6.ab0 %7.ab0 %8 %11.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    512,
                    512,
                    512
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm512_fmadd_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (reg (bv #x05 8)) (reg (bv #x06 8)) 64 64 -1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1))\n(define c (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b)))\n(define reg_2 (concat \n\n(extract 511 480 c)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 511 480 a) 64 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 511 480 b) 64 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 511 480 a) 64 0) (bvsizeext (extract 511 480 b) 64 0))))\n(define %11.ab0 (concat \n\n(bvsizeext (extract 511 480 c) 64 0))) \n (vector reg_0 reg_1 reg_2 %6.ab0 %7.ab0 %8 %11.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    512,
                    512,
                    512
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm512_fmadd_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (reg (bv #x06 8)) (reg (bv #x05 8)) 64 64 -1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1))\n(define c (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b)))\n(define reg_2 (concat \n\n(extract 511 480 c)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 511 480 a) 64 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 511 480 b) 64 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 511 480 a) 64 0) (bvsizeext (extract 511 480 b) 64 0))))\n(define %11.ab0 (concat \n\n(bvsizeext (extract 511 480 c) 64 0))) \n (vector reg_0 reg_1 reg_2 %6.ab0 %7.ab0 %8 %11.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    512,
                    512,
                    512
                ]
            }
        }
    ],
    "_mm_avg_epu8+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16 -1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 112 a)))\n(define reg_1 (concat \n\n(extract 127 112 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    16,
                    16
                ],
                "src_env_sizes": [
                    128,
                    128
                ]
            }
        }
    ]
}