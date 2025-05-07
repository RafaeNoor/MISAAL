{
    "_mm256_dpbusd_epi32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-ssat-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 64) (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) 8 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm256_dpbusd_epi32+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 64 -1) (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 64 -1) (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) (typed-folded:vec-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 64 -1) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm256_dpbusd_epi32+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-smul_dsl (typed-folded:vec-div_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 32 64 0) (repair-smul_dsl (reg (bv #x04 8)) (reg (bv #x03 8)) 16 64) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0)))\n(define %9.ab0 (concat \n\n(bvsizeext (extract 255 248 b) 16 1)\n(bvsizeext (extract 247 240 b) 16 1)\n(bvsizeext (extract 239 232 b) 16 1)\n(bvsizeext (extract 231 224 b) 16 1))) \n (vector reg_0 reg_1 reg_2 %4.ab0 %9.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
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
    "_mm256_dpbusd_epi32+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 64 0) (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 64 0) (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) 8 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) (typed-folded:vec-mod_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 64 0) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm256_dpbusd_epi32+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-cast-int_dsl (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 32 1) 8 16 32)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(typed-folded:vec-min_dsl (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) 16 64 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm256_dpbusd_epi32+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-cast-int_dsl (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 32 0) 8 16 32)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(typed-folded:vec-max_dsl (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) 8 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(typed-folded:vec-max_dsl (repair-ssat-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 64) (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) 8 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm256_dpbusd_epi32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-cast-int_dsl (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0) 16 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0) 8 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-sub_dsl (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0) (lit (bv #x0000000000000000 64)) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-sub_dsl (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0) (lit (bv #x0000000000000000 64)) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-sub_dsl (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0) (lit (bv #x0000000000000000 64)) 64 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-sub_dsl (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 32 16 0) (lit (bv #x0000000000000000 64)) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(typed-folded:cast-extend_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 16 32) 8 32 16 0)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-add_dsl (repair-ssat-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 64) (typed-folded:cast-extend_dsl (reg (bv #x02 8)) 8 32 16 1) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-cast-int_dsl (typed-folded:cast-extend_dsl (reg (bv #x02 8)) 8 32 16 1) 16 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-add_dsl (repair-ssat-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 64) (typed-folded:cast-extend_dsl (reg (bv #x02 8)) 8 32 16 1) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm256_dpbusd_epi32+typed-folded:cast-truncate": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-add_dsl (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) (lit (bv #x0000000000000000 64)) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-add_dsl (repair-cast-int_dsl (reg (bv #x02 8)) 8 16 32) (lit (bv #x0000000000000000 64)) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm256_dpbusd_epi32+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-cast-int_dsl (typed-folded:broadcast_dsl (reg (bv #x02 8)) 32 1) 8 16 32)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0))) \n (vector reg_0 reg_1 reg_2 %4.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
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
    "_mm256_dpbusd_epi32+typed-folded:ramp": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-add_dsl (repair-cast-int_dsl (reg (bv #x05 8)) 16 32 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0)))\n(define %9.ab0 (concat \n\n(bvsizeext (extract 255 248 b) 16 1)\n(bvsizeext (extract 247 240 b) 16 1)\n(bvsizeext (extract 239 232 b) 16 1)\n(bvsizeext (extract 231 224 b) 16 1)))\n(define %10 (concat \n\n(bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1))\n(bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1))\n(bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1))\n(bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1)))) \n (vector reg_0 reg_1 reg_2 %4.ab0 %9.ab0 %10)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-add_dsl (repair-cast-int_dsl (reg (bv #x05 8)) 16 32 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0)))\n(define %9.ab0 (concat \n\n(bvsizeext (extract 255 248 b) 16 1)\n(bvsizeext (extract 247 240 b) 16 1)\n(bvsizeext (extract 239 232 b) 16 1)\n(bvsizeext (extract 231 224 b) 16 1)))\n(define %10 (concat \n\n(bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1))\n(bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1))\n(bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1))\n(bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1)))) \n (vector reg_0 reg_1 reg_2 %4.ab0 %9.ab0 %10)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x05 8)) 16 32 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0)))\n(define %9.ab0 (concat \n\n(bvsizeext (extract 255 248 b) 16 1)\n(bvsizeext (extract 247 240 b) 16 1)\n(bvsizeext (extract 239 232 b) 16 1)\n(bvsizeext (extract 231 224 b) 16 1)))\n(define %10 (concat \n\n(bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1))\n(bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1))\n(bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1))\n(bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1)))) \n (vector reg_0 reg_1 reg_2 %4.ab0 %9.ab0 %10)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
    "_mm256_maddubs_epi16+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 16 64)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(typed-folded:vec-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 8 64 0)",
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
                "output_expression": "(typed-folded:vec-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 32 64 0)",
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
                "output_expression": "(typed-folded:vec-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 32 64 0)",
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
                "output_expression": "(typed-folded:vec-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 64 64 -1)",
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
                "output_expression": "(typed-folded:vec-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 16 64 -1)",
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
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 16 64)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 8 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 64 64)",
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
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 8 64 0)",
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
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 64 64 0)",
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
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 8 64 0)",
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
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64 1)",
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
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 8 64 0)",
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
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 64 64)",
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
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 16 64)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 8 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 64 64)",
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
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 8 64 1)",
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
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 8 64 0)",
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
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 8 64 0)",
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
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 8 64 0)",
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
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 64 64 1)",
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
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 16 64)",
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
                "output_expression": "(repair-cast-int_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 0) 16 32 32)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 64 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 64 64)",
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
                "output_expression": "(typed-folded:vec-min_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 32 64 0)",
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
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 32 64)",
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
                "output_expression": "(repair-cast-int_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32 1) 16 32 32)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 64 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 8 64 0)",
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
                "output_expression": "(typed-folded:vec-max_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 8 64 0)",
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
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 16 64 0)",
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
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 64 64 0)",
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
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 16 64 0)",
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
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 8 64 0)",
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
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-cast-int_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 16 32 32)",
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
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 32 64)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(typed-folded:vec-bwor_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 16 64)",
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
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 32 64)",
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
                "output_expression": "(typed-folded:vec-bwor_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 16 64)",
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
                "output_expression": "(typed-folded:vec-bwor_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 16 64)",
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
                "output_expression": "(typed-folded:vec-bwor_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 16 64)",
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
                "output_expression": "(typed-folded:vec-bwor_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 16 64)",
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
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1) 32 64)",
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
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1) 8 64)",
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
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1) 32 64)",
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
                "output_expression": "(repair-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1) 32 64)",
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
                "output_expression": "(repair-cast-int_dsl (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1) 32 32 64)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1) 32 64)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1) 32 64)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1) 16 64)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 32 32 1) (lit (bv #x0000000000000000 64)) 16 64)",
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
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:cast-truncate": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 16 64)",
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
                "output_expression": "(repair-ssat-add_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-add_dsl (repair-cast-int_dsl (reg (bv #x02 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-ssat-add_dsl (repair-cast-int_dsl (reg (bv #x02 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x02 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 16 64)",
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
                "output_expression": "(repair-add_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 16 64)",
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
                "output_expression": "(repair-cast-int_dsl (typed-folded:broadcast_dsl (reg (bv #x01 8)) 32 1) 16 32 32)",
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
                "output_expression": "(repair-cast-int_dsl (typed-folded:broadcast_dsl (reg (bv #x01 8)) 32 1) 16 32 32)",
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
                "output_expression": "(repair-ssat-add_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-ssat-add_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 8 64)",
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
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:ramp": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-add_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-ssat-add_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 8 64)",
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
                "output_expression": "(repair-ssat-add_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 16 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
        }
    ],
    "_mm256_mul_epi32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 64 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 16 64)",
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
                "output_expression": "(typed-folded:vec-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 8 64 0)",
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
                "output_expression": "(typed-folded:vec-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 8 64 1)",
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
                "output_expression": "(typed-folded:vec-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 16 64 -1)",
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
                "output_expression": "(typed-folded:vec-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 16 64 0)",
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
        }
    ],
    "_mm256_mul_epi32+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 64 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 8 64 -1)",
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
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64 -1)",
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
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 64 64 1)",
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
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 8 64 0)",
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
        }
    ],
    "_mm256_mul_epi32+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
        }
    ],
    "_mm256_mul_epi32+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64 1)",
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
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 8 64 0)",
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
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 8 64 1)",
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
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64 0)",
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
        }
    ],
    "_mm256_mul_epi32+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-cast-int_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32 1) 32 64 32)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 16 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(typed-folded:vec-min_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 16 64 0)",
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
                "output_expression": "(repair-cast-int_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 1) 32 64 32)",
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
    "_mm256_mul_epi32+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-cast-int_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32 1) 32 64 32)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(typed-folded:vec-max_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 8 64 0)",
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
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 64 64 0)",
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
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 8 64 0)",
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
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 8 64 0)",
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
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 8 64 0)",
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
                "output_expression": "(repair-cast-int_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 0) 32 64 32)",
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
    "_mm256_mul_epi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-cast-int_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32) 32 64 32)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 16 64)",
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
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 64 64)",
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
                "output_expression": "(typed-folded:vec-bwor_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
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
                "output_expression": "(typed-folded:vec-bwor_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 8 64)",
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
                "output_expression": "(typed-folded:vec-bwor_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
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
                "output_expression": "(typed-folded:vec-bwor_dsl (lit (bv #x0000000000000000 64)) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 16 64)",
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
                "output_expression": "(repair-cast-int_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 64 32)",
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
    "_mm256_mul_epi32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-cast-int_dsl (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 32 64 1) 32 32 64)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 32 64 1) 32 64)",
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
                "output_expression": "(repair-ssat-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 32 64 1) 32 64)",
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
        }
    ],
    "_mm256_mul_epi32+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-cast-int_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 32 1) 32 64 32)",
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
                "output_expression": "(repair-ssat-add_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-cast-int_dsl (typed-folded:broadcast_dsl (reg (bv #x01 8)) 32 1) 32 64 32)",
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
    "_mm256_mul_epi32+typed-folded:ramp": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-ssat-add_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 8 64)",
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
                "output_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 8 64)",
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
        }
    ],
    "_mm_mul_su32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 8 64 0)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 32 64 -1)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 16 64 -1)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 16 64 0)",
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
    "_mm_mul_su32+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 64 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 8 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 8 64 0)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64 -1)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64 -1)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 16 64 1)",
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
    "_mm_mul_su32+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 16 64)",
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
    "_mm_mul_su32+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64 0)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 8 64 0)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 8 64 0)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 8 64 1)",
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
    "_mm_mul_su32+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32 0) 32 64 32)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 8 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-min_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 64 64 1)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 0) 32 64 32)",
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
        }
    ],
    "_mm_mul_su32+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32 1) 32 64 32)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-max_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 8 64 1)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 32 64 0)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 32 64 0)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 64 64 1)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 16 64 0)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32 0) 32 64 32)",
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
        }
    ],
    "_mm_mul_su32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32) 32 64 32)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-bwor_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-bwor_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-bwor_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-bwor_dsl (lit (bv #x0000000000000000 64)) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 32 64 32)",
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
        }
    ],
    "_mm_mul_su32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 32 64 0) 32 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 32 64 0) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x0000000000000000 64)) (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 32 64 0) 8 64)",
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
    "_mm_mul_su32+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 16 2) 32 64 32)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-add_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 8 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:broadcast_dsl (reg (bv #x01 8)) 32 1) 32 64 32)",
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
        }
    ],
    "_mm_mul_su32+typed-folded:ramp": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-add_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 64 64)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (lit (bv #x0000000000000000 64)) 32 64)",
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
                "output_expression": "(repair-add_dsl (typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16 -1) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16) 8 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16 -1) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16) 8 16)",
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
    "_mm_avg_epu8+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 16 0) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) 8 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-usat-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 16 0) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 8 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-usat-sub_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 16 0) 8 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-ushr_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 0) 8 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16) 8 16 1)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16) 8 16 -1)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 1) 16 16 1)",
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
    "_mm_avg_epu8+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 0) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 8 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-usat-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16 0) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-usat-sub_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 1) 8 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-ushr_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0) 8 16)",
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
    "_mm_avg_epu8+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 0) (reg (bv #x00 8)) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16 1) (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 1) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(typed-folded:vec-min_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 8 16 0)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(typed-folded:vec-min_dsl (repair-usat-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 16 0)",
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
    "_mm_avg_epu8+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0) (reg (bv #x01 8)) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 1) (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(typed-folded:vec-max_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16) 16 16 0)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(typed-folded:vec-max_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 16 1)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(typed-folded:vec-max_dsl (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 16) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 8 16 0)",
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
    "_mm_avg_epu8+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) (reg (bv #x01 8)) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 16) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 16)",
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
    "_mm_avg_epu8+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (lit (bv #x0000 16)) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-usat-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (lit (bv #x0000 16)) 8 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-usat-sub_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (lit (bv #x0000 16)) 8 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-ushr_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (lit (bv #x0000 16)) 16 16)",
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
    "_mm_avg_epu8+typed-folded:cast-truncate": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (lit (bv #x0000 16)) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-usat-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (lit (bv #x0000 16)) 8 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-usat-sub_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (lit (bv #x0000 16)) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-ushr_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (lit (bv #x0000 16)) 16 16)",
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
    "_mm_avg_epu8+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-add_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 16 1) (typed-folded:broadcast_dsl (reg (bv #x01 8)) 16 1) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-add_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 16 1) (reg (bv #x01 8)) 16 16)",
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
    "_m_pslld+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed-folded:cast-extend_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32 64 0)",
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
    "_mm256_rol_epi32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 8 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 8 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-usat-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 32 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        }
    ],
    "_mm256_rol_epi32+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-bwor_dsl (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 -1) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 -1) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-sub_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 -1) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-uabsd_dsl (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 -1) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        }
    ],
    "_mm256_rol_epi32+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 1) (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 64 64) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8))))\n(define %1.site0.ab0 (concat \n\n(bvsizeext (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 64 0))) \n (vector reg_0 reg_1 %0.site0 %1.site0.ab0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8,
                    64
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        }
    ],
    "_mm256_rol_epi32+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-bwor_dsl (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-sub_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-uabsd_dsl (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        }
    ],
    "_mm256_rol_epi32+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 8 8 0) 8 64 8)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        }
    ],
    "_mm256_rol_epi32+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 8 1) 8 64 8)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        }
    ],
    "_mm256_rol_epi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 8) 8 64 8)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        }
    ],
    "_mm256_rol_epi32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-bwor_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (lit (bv #x0000000000000000 64)) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:cast-extend_dsl (reg (bv #x02 8)) 8 8 16 1) 8 32 16)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (lit (bv #x0000000000000000 64)) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-sub_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (lit (bv #x0000000000000000 64)) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-uabsd_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (lit (bv #x0000000000000000 64)) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        }
    ],
    "_mm256_rol_epi32+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_rol_epi32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:broadcast_dsl (reg (bv #x02 8)) 8 1) 8 64 8)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    128,
                    8
                ]
            }
        }
    ],
    "_m_psrld+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed-folded:cast-extend_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32 64 0)",
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
    "_mm256_ror_epi32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 8 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 16 64 -1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-usat-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 8 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        }
    ],
    "_mm256_ror_epi32+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-bwor_dsl (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 -1) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 -1) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-sub_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 -1) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-uabsd_dsl (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 -1) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        }
    ],
    "_mm256_ror_epi32+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-shl_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x06 8)) 64 64) (typed-folded:vec-div_dsl (reg (bv #x06 8)) (reg (bv #x03 8)) 64 64 1) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8))))\n(define %1.site0.ab0 (concat \n\n(bvsizeext (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 64 0)))\n(define %2.site0 (concat \n\n(bvashr (extract 511 448 a) (bvsizeext (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 64 0))))\n(define %3.site0.ab0 (concat \n\n(bvsubnw (bv #x00000040 8) (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 8 -1)))\n(define %4.site0.ab0 (concat \n\n(bvsizeext (bvsubnw (bv #x00000040 8) (bvsmod (extract 7 0 imm8) (bv #x00000040 8)) 8 -1) 64 0))) \n (vector reg_0 reg_1 %0.site0 %1.site0.ab0 %2.site0 %3.site0.ab0 %4.site0.ab0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8,
                    64,
                    64,
                    8,
                    64
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        }
    ],
    "_mm256_ror_epi32+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-bwor_dsl (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-sub_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-uabsd_dsl (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0) (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        }
    ],
    "_mm256_ror_epi32+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 8 8 0) 8 64 8)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        }
    ],
    "_mm256_ror_epi32+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 8 1) 8 64 8)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        }
    ],
    "_mm256_ror_epi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 8) 8 64 8)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        }
    ],
    "_mm256_ror_epi32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-bwor_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (lit (bv #x0000000000000000 64)) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:cast-extend_dsl (reg (bv #x02 8)) 8 8 16 1) 8 32 16)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (lit (bv #x0000000000000000 64)) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-sub_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (lit (bv #x0000000000000000 64)) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        },
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-uabsd_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 8 64 8) (lit (bv #x0000000000000000 64)) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        }
    ],
    "_mm256_ror_epi32+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm256_ror_epi32",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:broadcast_dsl (reg (bv #x02 8)) 8 1) 8 64 8)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define imm8 (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 7 0 imm8)))\n(define %0.site0 (concat \n\n(bvsmod (extract 7 0 imm8) (bv #x00000040 8)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    8,
                    8
                ],
                "src_env_sizes": [
                    512,
                    8
                ]
            }
        }
    ],
    "_mm_rolv_epi32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (repair-sabsd_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 64 64) 64 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (repair-sshr_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64) 8 64 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 8 64 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (repair-uabsd_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64) 64 64 -1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) 64 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rolv_epi32+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-bwor_dsl (typed-folded:vec-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 1) (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64 -1) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-sshr_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 1) 8 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-sub_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 0) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rolv_epi32+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(typed-folded:vec-div_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0) 64 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rolv_epi32+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-bwor_dsl (typed-folded:vec-mod_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 64 64 1) (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64 0) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-sshr_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64 1) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-sub_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 1) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rolv_epi32+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (reg (bv #x00 8)) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 64 64 1) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 64 64 0) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rolv_epi32+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (reg (bv #x00 8)) (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64 0) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64 0) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rolv_epi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (reg (bv #x00 8)) (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x02 8)) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 64 64) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rolv_epi32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-bwor_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (lit (bv #x0000000000000000 64)) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (lit (bv #x0000000000000000 64)) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rolv_epi32+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (reg (bv #x00 8)) (typed-folded:broadcast_dsl (reg (bv #x02 8)) 16 4) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (typed-folded:broadcast_dsl (reg (bv #x02 8)) 64 1) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 64 1) (reg (bv #x02 8)) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 64 1) (repair-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
                    64,
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
                "candidate": "_mm_rolv_epi32",
                "output_expression": "(repair-shl_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 32 2) (typed-folded:broadcast_dsl (reg (bv #x02 8)) 8 8) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 448 a)))\n(define reg_1 (concat \n\n(extract 511 448 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 511 448 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rorv_epi32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) 64 64 -1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (repair-sshr_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 32 64) 32 64 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) 32 64 1)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-uabsd_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) 64 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rorv_epi32+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-bwor_dsl (typed-folded:vec-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64 1) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-shl_dsl (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-sub_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0) 8 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64 1) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sub_dsl (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 0) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rorv_epi32+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-div_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 1) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-shl_dsl (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-div_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rorv_epi32+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-bwor_dsl (typed-folded:vec-mod_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64 0) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) 8 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-shl_dsl (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-mod_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64 1) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0) 8 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sub_dsl (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-mod_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 64 64 1) 16 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rorv_epi32+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 0) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (reg (bv #x00 8)) (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 8 64 0) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 0) (reg (bv #x02 8)) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 1) (repair-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 0) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 64 0) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rorv_epi32+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 1) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (reg (bv #x00 8)) (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64 0) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 1) (reg (bv #x02 8)) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 8 64 0) (repair-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 8 64 0) (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 0) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(typed-folded:vec-max_dsl (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) 64 64 0)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rorv_epi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (reg (bv #x00 8)) (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 32 64) (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 16 64) (reg (bv #x02 8)) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 16 64) (repair-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rorv_epi32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-bwor_dsl (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (lit (bv #x0000000000000000 64)) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-shl_dsl (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (lit (bv #x0000000000000000 64)) 32 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    "_mm_rorv_epi32+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceIntermediates",
            "property": {
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (reg (bv #x00 8)) (typed-folded:broadcast_dsl (reg (bv #x02 8)) 64 1) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 8 64) (typed-folded:broadcast_dsl (reg (bv #x02 8)) 8 8) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 32 2) (reg (bv #x02 8)) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 32 2) (repair-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 64 64) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
                    64,
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
                "candidate": "_mm_rorv_epi32",
                "output_expression": "(repair-sshr_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 32 2) (typed-folded:broadcast_dsl (reg (bv #x02 8)) 64 1) 64 64)",
                "synth_expression": "'()",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %0.site0 (concat \n\n(bvsmod (extract 127 64 b) (bv #x0000000000000000000000000000000000000000000000000000000000000040 64)))) \n (vector reg_0 reg_1 %0.site0)\n)",
                "target_input_sizes": [
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
    ]
}