{
    "_mm256_dpbusd_epi32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b))) \n (vector reg_0 reg_1 reg_2)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b))) \n (vector reg_0 reg_1 reg_2)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32
                ],
                "src_env_sizes": [
                    128,
                    128,
                    128
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x02 8)) 16 32 32 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1))) \n (vector reg_0 reg_1 reg_2 %14.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    128,
                    128,
                    128
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x02 8)) 16 32 32 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1))) \n (vector reg_0 reg_1 reg_2 %14.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    128,
                    128,
                    128
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x02 8)) 16 32 32 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512))))\n(define reg_1 (concat \n\n(extract 511 496 a)\n(extract 495 480 a)))\n(define reg_2 (concat \n\n(extract 511 496 b)\n(extract 495 480 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 511 496 a) 32 1)\n(bvsizeext (extract 495 480 a) 32 1))) \n (vector reg_0 reg_1 reg_2 %14.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    512,
                    512
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512))))\n(define reg_1 (concat \n\n(extract 511 496 a)\n(extract 495 480 a)))\n(define reg_2 (concat \n\n(extract 511 496 b)\n(extract 495 480 b))) \n (vector reg_0 reg_1 reg_2)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32
                ],
                "src_env_sizes": [
                    512,
                    512
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x02 8)) 16 32 32 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512))))\n(define reg_1 (concat \n\n(extract 511 496 a)\n(extract 495 480 a)))\n(define reg_2 (concat \n\n(extract 511 496 b)\n(extract 495 480 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 511 496 a) 32 1)\n(bvsizeext (extract 495 480 a) 32 1))) \n (vector reg_0 reg_1 reg_2 %14.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    512,
                    512
                ]
            }
        }
    ],
    "_mm256_mulhrs_epi16+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mulhrs_epi16",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 16 32 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 255 240 a)))\n(define reg_1 (concat \n\n(extract 255 240 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    16,
                    16
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mulhrs_epi16",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 16 32 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 255 240 a)))\n(define reg_1 (concat \n\n(extract 255 240 b)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 255 240 a) 32 1))) \n (vector reg_0 reg_1 %3.ab0)\n)",
                "target_input_sizes": [
                    16,
                    16,
                    32
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        }
    ],
    "_mm512_fmadd_epi32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm512_fmadd_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (reg (bv #x05 8)) (reg (bv #x06 8)) 64 64 0)",
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
        }
    ],
    "_mm512_fmadd_epi32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm512_fmadd_epi32",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1))\n(define c (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b)))\n(define reg_2 (concat \n\n(extract 511 480 c))) \n (vector reg_0 reg_1 reg_2)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32
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
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1))\n(define c (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b)))\n(define reg_2 (concat \n\n(extract 511 480 c)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 511 480 a) 64 0))) \n (vector reg_0 reg_1 reg_2 %6.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x02 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1))\n(define c (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b)))\n(define reg_2 (concat \n\n(extract 511 480 c)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 511 480 a) 64 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 511 480 b) 64 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 511 480 a) 64 0) (bvsizeext (extract 511 480 b) 64 0)))) \n (vector reg_0 reg_1 reg_2 %6.ab0 %7.ab0 %8)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1))\n(define c (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b)))\n(define reg_2 (concat \n\n(extract 511 480 c)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 511 480 a) 64 0))) \n (vector reg_0 reg_1 reg_2 %6.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x02 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1))\n(define c (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b)))\n(define reg_2 (concat \n\n(extract 511 480 c)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 511 480 a) 64 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 511 480 b) 64 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 511 480 a) 64 0) (bvsizeext (extract 511 480 b) 64 0)))) \n (vector reg_0 reg_1 reg_2 %6.ab0 %7.ab0 %8)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x02 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1))\n(define c (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b)))\n(define reg_2 (concat \n\n(extract 511 480 c)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 511 480 a) 64 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 511 480 b) 64 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 511 480 a) 64 0) (bvsizeext (extract 511 480 b) 64 0)))) \n (vector reg_0 reg_1 reg_2 %6.ab0 %7.ab0 %8)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x02 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1))\n(define c (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b)))\n(define reg_2 (concat \n\n(extract 511 480 c)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 511 480 a) 64 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 511 480 b) 64 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 511 480 a) 64 0) (bvsizeext (extract 511 480 b) 64 0)))) \n (vector reg_0 reg_1 reg_2 %6.ab0 %7.ab0 %8)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm256_mul_epi32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 32 64 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    32,
                    32
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 32 32 64 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1))) \n (vector reg_0 reg_1 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        }
    ],
    "_mm512_mulhi_epu16+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 64 64 128 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    64,
                    64
                ],
                "src_env_sizes": [
                    128,
                    128
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 64 64 128 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0))) \n (vector reg_0 reg_1 %6.ab0)\n)",
                "target_input_sizes": [
                    64,
                    64,
                    128
                ],
                "src_env_sizes": [
                    128,
                    128
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 64 64 128 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0))) \n (vector reg_0 reg_1 %6.ab0)\n)",
                "target_input_sizes": [
                    64,
                    64,
                    128
                ],
                "src_env_sizes": [
                    128,
                    128
                ]
            }
        }
    ],
    "_mm_mul_su32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0))) \n (vector reg_0 reg_1 %2.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    32,
                    32
                ],
                "src_env_sizes": [
                    64,
                    64
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
    ],
    "_mm512_mulhi_epu32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm512_mulhi_epu32",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    32,
                    32
                ],
                "src_env_sizes": [
                    512,
                    512
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm512_mulhi_epu32",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 511 480 a) 64 0))) \n (vector reg_0 reg_1 %6.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    512,
                    512
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm512_mulhi_epu32",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 a)))\n(define reg_1 (concat \n\n(extract 511 480 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 511 480 a) 64 0))) \n (vector reg_0 reg_1 %6.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    512,
                    512
                ]
            }
        }
    ],
    "_mm_div_epi64+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_div_epi64",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 64 64 128 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %5.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 1))) \n (vector reg_0 reg_1 %5.ab0)\n)",
                "target_input_sizes": [
                    64,
                    64,
                    128
                ],
                "src_env_sizes": [
                    128,
                    128
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_div_epi64",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 64 64 128 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    64,
                    64
                ],
                "src_env_sizes": [
                    128,
                    128
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_div_epi64",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 64 64 128 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %5.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 1))) \n (vector reg_0 reg_1 %5.ab0)\n)",
                "target_input_sizes": [
                    64,
                    64,
                    128
                ],
                "src_env_sizes": [
                    128,
                    128
                ]
            }
        }
    ],
    "_m_pslld+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm))) \n (vector reg_0 reg_2 reg_3)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_m_psrld+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed-folded:cast-extend_dsl (reg (bv #x01 8)) 32 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm))) \n (vector reg_0 reg_2 reg_3)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ]
}