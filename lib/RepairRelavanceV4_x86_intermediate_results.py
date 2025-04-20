{
    "_mm256_madd52hi_epu64+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(typed-folded:vec-add_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64 -1)",
                "synth_expression": "(_mm256_madd52hi_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 208 52 64 -1 0 52 52 0 128 0 52 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1))\n(define c (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 243 192 b)))\n(define reg_1 (concat \n\n(extract 243 192 c)))\n(define reg_2 (concat \n\n(extract 255 192 a)))\n(define reg_3 (concat \n\n(extract 103 52 (bvmul (bvsizeext (extract 243 192 b) 128 0) (bvsizeext (extract 243 192 c) 128 0)))))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 243 192 b) 128 0)))\n(define %8.ab0 (concat \n\n(bvsizeext (extract 243 192 c) 128 0)))\n(define %9 (concat \n\n(bvmul (bvsizeext (extract 243 192 b) 128 0) (bvsizeext (extract 243 192 c) 128 0))))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 103 52 (bvmul (bvsizeext (extract 243 192 b) 128 0) (bvsizeext (extract 243 192 c) 128 0))) 64 0))) \n (vector reg_0 reg_1 reg_2 reg_3 %7.ab0 %8.ab0 %9 %15.ab0)\n)",
                "target_input_sizes": [
                    52,
                    52,
                    64,
                    52,
                    128,
                    128,
                    128,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        }
    ],
    "_mm_add_si64+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 -1)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 a)))\n(define reg_1 (concat \n\n(extract 63 0 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_mm_hadd_pi16+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 -1)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 96 b)))\n(define reg_1 (concat \n\n(extract 95 64 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    32,
                    32
                ],
                "src_env_sizes": [
                    128,
                    128
                ]
            }
        }
    ],
    "_mm_hadd_pi32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 -1)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 32 a)))\n(define reg_1 (concat \n\n(extract 31 0 a)))\n(define reg_2 (concat \n\n(extract 63 32 b)))\n(define reg_3 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvaddnw (extract 63 32 a) (extract 31 0 a) 32 -1))) \n (vector reg_0 reg_1 reg_2 reg_3 %2.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm_hadd_pi32+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-min_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 32 32 1)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 32 a)))\n(define reg_1 (concat \n\n(extract 31 0 a)))\n(define reg_2 (concat \n\n(extract 63 32 b)))\n(define reg_3 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvaddnw (extract 63 32 a) (extract 31 0 a) 32 -1))) \n (vector reg_0 reg_1 reg_2 reg_3 %2.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm_hadd_pi32+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-max_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 8 32 0)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 32 a)))\n(define reg_1 (concat \n\n(extract 31 0 a)))\n(define reg_2 (concat \n\n(extract 63 32 b)))\n(define reg_3 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvaddnw (extract 63 32 a) (extract 31 0 a) 32 -1))) \n (vector reg_0 reg_1 reg_2 reg_3 %2.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm_hadd_pi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-bwor_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 16 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 32 a)))\n(define reg_1 (concat \n\n(extract 31 0 a)))\n(define reg_2 (concat \n\n(extract 63 32 b)))\n(define reg_3 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvaddnw (extract 63 32 a) (extract 31 0 a) 32 -1))) \n (vector reg_0 reg_1 reg_2 reg_3 %2.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm_add_pi8+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64 -1)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    64,
                    64
                ],
                "src_env_sizes": [
                    512,
                    512
                ]
            }
        }
    ],
    "_mm_div_epi64+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_div_epi64",
                "output_expression": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64 1)",
                "synth_expression": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 16 1 16 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %5.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 1)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 1)))\n(define %7.ab0 (concat \n\n(bvdiv (bvsizeext (extract 127 64 a) 128 1) (bvsizeext (extract 127 64 b) 128 1) 1))) \n (vector reg_0 reg_1 %5.ab0 %6.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    64,
                    64,
                    128,
                    128,
                    128
                ],
                "src_env_sizes": [
                    128,
                    128
                ]
            }
        }
    ],
    "_mm256_hadd_epi32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 -1)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 255 224 b)))\n(define reg_1 (concat \n\n(extract 223 192 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    32,
                    32
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        }
    ],
    "_m_pslld+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 0)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvshl (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_m_pslld+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 -1)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvshl (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_m_pslld+typed-folded:vec-lt": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(lit (bv #x00000000 32))",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvshl (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_m_pslld+typed-folded:vec-le": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(lit (bv #x00000000 32))",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvshl (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_m_pslld+typed-folded:vec-eq": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(lit (bv #x00000000 32))",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvshl (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_m_pslld+typed-folded:vec-gt": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(lit (bv #x00000000 32))",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvshl (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_m_pslld+typed-folded:vec-ge": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(lit (bv #x00000000 32))",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvshl (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_mm256_rol_epi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(typed-folded:vec-bwor_dsl (reg (bv #x04 8)) (reg (bv #x07 8)) 64 64)",
                "synth_expression": "(_mm256_rol_epi32_dsl (lit (bv #x40 8)) (lit (bv #x40 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 16 8 64 1 0 -1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8))))\n(define %1.site0.ab0 (concat \n\n(bvsizeext (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 64 0)))\n(define %2.site0 (concat \n\n(bvshl (extract 127 64 a) (bvsizeext (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 64 0))))\n(define %3.site0.ab0 (concat \n\n(bvsubnw (bv #x00000040 8) (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 8 -1)))\n(define %4.site0.ab0 (concat \n\n(bvsizeext (bvsubnw (bv #x00000040 8) (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 8 -1) 64 0)))\n(define %5.site0 (concat \n\n(bvashr (extract 127 64 a) (bvsizeext (bvsubnw (bv #x00000040 8) (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 8 -1) 64 0)))) \n (vector reg_0 reg_1 %0.site0 %1.site0.ab0 %2.site0 %3.site0.ab0 %4.site0.ab0 %5.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8,
                    64,
                    64,
                    8,
                    64,
                    64
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        }
    ],
    "_m_psrld+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 -1)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvlshr (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_m_psrld+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 0)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvlshr (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_m_psrld+typed-folded:vec-lt": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(lit (bv #x00000000 32))",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvlshr (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_m_psrld+typed-folded:vec-le": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(lit (bv #x00000000 32))",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvlshr (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_m_psrld+typed-folded:vec-gt": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(lit (bv #x00000000 32))",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvlshr (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_m_psrld+typed-folded:vec-eq": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(lit (bv #x00000000 32))",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvlshr (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_m_psrld+typed-folded:vec-ge": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(lit (bv #x00000000 32))",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define count.norm (vector-ref env 0))\n(define a.norm (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 count.norm)))\n(define reg_2 (concat \n\n(extract 63 32 a.norm)))\n(define reg_3 (concat \n\n(extract 63 0 count.norm)))\n(define %8.ab0.norm (concat \n\n(bvsizeext (extract 63 32 a.norm) 64 0)))\n(define %9.norm (concat \n\n(bvlshr (bvsizeext (extract 63 32 a.norm) 64 0) (extract 63 0 count.norm)))) \n (vector reg_0 reg_2 reg_3 %8.ab0.norm %9.norm)\n)",
                "target_input_sizes": [
                    64,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_mm256_ror_epi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(typed-folded:vec-bwor_dsl (reg (bv #x04 8)) (reg (bv #x07 8)) 8 64)",
                "synth_expression": "(_mm256_ror_epi32_dsl (lit (bv #x40 8)) (lit (bv #x40 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 64 8 64 1 0 -1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8))))\n(define %1.site0.ab0 (concat \n\n(bvsizeext (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 64 0)))\n(define %2.site0 (concat \n\n(bvashr (extract 511 448 a) (bvsizeext (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 64 0))))\n(define %3.site0.ab0 (concat \n\n(bvsubnw (bv #x00000040 8) (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 8 -1)))\n(define %4.site0.ab0 (concat \n\n(bvsizeext (bvsubnw (bv #x00000040 8) (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 8 -1) 64 0)))\n(define %5.site0 (concat \n\n(bvshl (extract 511 448 a) (bvsizeext (bvsubnw (bv #x00000040 8) (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 8 -1) 64 0)))) \n (vector reg_0 reg_1 %0.site0 %1.site0.ab0 %2.site0 %3.site0.ab0 %4.site0.ab0 %5.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8,
                    64,
                    64,
                    8,
                    64,
                    64
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        }
    ],
    "_mm512_rem_epu32+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64 1)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 255 192 a)))\n(define reg_1 (concat \n\n(extract 255 192 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        }
    ],
    "_mm512_or_epi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    64,
                    64
                ],
                "src_env_sizes": [
                    512,
                    512
                ]
            }
        }
    ],
    "_mm_rolv_epi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x05 8)) 64 64)",
                "synth_expression": "(_mm_rolv_epi32_dsl (lit (bv #x0000000000000040 64)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64))))\n(define %1.site0 (concat \n\n(bvshl (extract 511 448 a) (bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))))\n(define %2.site0.ab0 (concat \n\n(bvsubnw (bv #x0000000000000000000000000000000000000000000000000000000000000040 64) (bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)) 64 -1)))\n(define %3.site0 (concat \n\n(bvashr (extract 511 448 a) (bvsubnw (bv #x0000000000000000000000000000000000000000000000000000000000000040 64) (bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)) 64 -1)))) \n (vector reg_0 reg_1 %0.site0 %1.site0 %2.site0.ab0 %3.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
                    64,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    512,
                    512
                ]
            }
        }
    ],
    "_mm256_max_epu64+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 1)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 255 192 a)))\n(define reg_1 (concat \n\n(extract 255 192 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        }
    ],
    "_mm_rorv_epi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x05 8)) 16 64)",
                "synth_expression": "(_mm_rorv_epi32_dsl (lit (bv #x0000000000000040 64)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 -1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64))))\n(define %1.site0 (concat \n\n(bvashr (extract 127 64 a) (bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))))\n(define %2.site0.ab0 (concat \n\n(bvsubnw (bv #x0000000000000000000000000000000000000000000000000000000000000040 64) (bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)) 64 -1)))\n(define %3.site0 (concat \n\n(bvshl (extract 127 64 a) (bvsubnw (bv #x0000000000000000000000000000000000000000000000000000000000000040 64) (bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)) 64 -1)))) \n (vector reg_0 reg_1 %0.site0 %1.site0 %2.site0.ab0 %3.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
                    64,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    128,
                    128
                ]
            }
        }
    ],
    "_mm_hsub_pi32+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hsub_pi32",
                "output_expression": "(typed-folded:vec-sub_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 32 32 -1)",
                "synth_expression": "(_mm_hsub_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 32 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 63 32 a)))\n(define reg_2 (concat \n\n(extract 31 0 b)))\n(define reg_3 (concat \n\n(extract 63 32 b)))\n(define %2.ab0 (concat \n\n(bvsubnw (extract 31 0 a) (extract 63 32 a) 32 -1))) \n (vector reg_0 reg_1 reg_2 reg_3 %2.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm_hsub_pi32+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hsub_pi32",
                "output_expression": "(typed-folded:vec-min_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 8 32 0)",
                "synth_expression": "(_mm_hsub_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 32 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 63 32 a)))\n(define reg_2 (concat \n\n(extract 31 0 b)))\n(define reg_3 (concat \n\n(extract 63 32 b)))\n(define %2.ab0 (concat \n\n(bvsubnw (extract 31 0 a) (extract 63 32 a) 32 -1))) \n (vector reg_0 reg_1 reg_2 reg_3 %2.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm_hsub_pi32+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hsub_pi32",
                "output_expression": "(typed-folded:vec-max_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 8 32 1)",
                "synth_expression": "(_mm_hsub_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 32 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 63 32 a)))\n(define reg_2 (concat \n\n(extract 31 0 b)))\n(define reg_3 (concat \n\n(extract 63 32 b)))\n(define %2.ab0 (concat \n\n(bvsubnw (extract 31 0 a) (extract 63 32 a) 32 -1))) \n (vector reg_0 reg_1 reg_2 reg_3 %2.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm_hsub_pi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hsub_pi32",
                "output_expression": "(typed-folded:vec-bwor_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 16 32)",
                "synth_expression": "(_mm_hsub_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 32 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 63 32 a)))\n(define reg_2 (concat \n\n(extract 31 0 b)))\n(define reg_3 (concat \n\n(extract 63 32 b)))\n(define %2.ab0 (concat \n\n(bvsubnw (extract 31 0 a) (extract 63 32 a) 32 -1))) \n (vector reg_0 reg_1 reg_2 reg_3 %2.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm_sub_si64+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 -1)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 63 0 a)))\n(define reg_1 (concat \n\n(extract 63 0 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        }
    ],
    "_mm_min_epu16+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64 0)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 255 192 a)))\n(define reg_1 (concat \n\n(extract 255 192 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        }
    ],
    "_mm512_subs_epi8+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64 0)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    64,
                    64
                ],
                "src_env_sizes": [
                    512,
                    512
                ]
            }
        }
    ],
    "_m_por+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_m_por",
                "output_expression": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512)",
                "synth_expression": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 512 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 0 a)))\n(define reg_1 (concat \n\n(extract 511 0 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    512,
                    512
                ],
                "src_env_sizes": [
                    512,
                    512
                ]
            }
        }
    ],
    "_mm256_hsub_epi32+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hsub_epi32",
                "output_expression": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 -1)",
                "synth_expression": "(_mm256_hsub_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 96 128 2 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 b)))\n(define reg_1 (concat \n\n(extract 255 224 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    32,
                    32
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        }
    ],
    "_mm_hsub_epi16+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hsub_epi16",
                "output_expression": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 -1)",
                "synth_expression": "(_mm_hsub_epi16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 32 64 128 32 -1 32 2 -1 96 128 2 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 95 64 b)))\n(define reg_1 (concat \n\n(extract 127 96 b))) \n (vector reg_0 reg_1)\n)",
                "target_input_sizes": [
                    32,
                    32
                ],
                "src_env_sizes": [
                    128,
                    128
                ]
            }
        }
    ]
}