{
    "_mm256_dpbusd_epi32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-vector-reduce-add_dsl 4 (reg (bv #x06 8)) 32 128) (reg (bv #x00 8)) 32 32 -1)",
                "synth_expression": "(_mm256_dpbusd_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 256 32 0 32 8 -1 1 1 16 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0)))\n(define %9.ab0 (concat \n\n(bvsizeext (extract 255 248 b) 16 1)\n(bvsizeext (extract 247 240 b) 16 1)\n(bvsizeext (extract 239 232 b) 16 1)\n(bvsizeext (extract 231 224 b) 16 1)))\n(define %10 (concat \n\n(bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1))\n(bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1))\n(bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1))\n(bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1))))\n(define %11.ab0 (concat \n\n(bvsizeext (bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1)) 32 1))) \n (vector reg_0 reg_1 reg_2 %4.ab0 %9.ab0 %10 %11.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64,
                    128
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-vector-reduce-add_dsl 4 (reg (bv #x06 8)) 32 128) (repair-cast-int_dsl (reg (bv #x00 8)) 16 16 32) 32 32 -1)",
                "synth_expression": "(_mm256_dpbusd_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 256 32 0 32 8 -1 1 1 16 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0)))\n(define %9.ab0 (concat \n\n(bvsizeext (extract 255 248 b) 16 1)\n(bvsizeext (extract 247 240 b) 16 1)\n(bvsizeext (extract 239 232 b) 16 1)\n(bvsizeext (extract 231 224 b) 16 1)))\n(define %10 (concat \n\n(bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1))\n(bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1))\n(bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1))\n(bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1))))\n(define %11.ab0 (concat \n\n(bvsizeext (bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1)) 32 1))) \n (vector reg_0 reg_1 reg_2 %4.ab0 %9.ab0 %10 %11.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64,
                    128
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32 1) (repair-vector-reduce-add_dsl 4 (reg (bv #x06 8)) 32 128) 32 32)",
                "synth_expression": "(_mm256_dpbusd_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 256 32 0 32 8 -1 1 1 16 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0)))\n(define %9.ab0 (concat \n\n(bvsizeext (extract 255 248 b) 16 1)\n(bvsizeext (extract 247 240 b) 16 1)\n(bvsizeext (extract 239 232 b) 16 1)\n(bvsizeext (extract 231 224 b) 16 1)))\n(define %10 (concat \n\n(bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1))\n(bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1))\n(bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1))\n(bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1))))\n(define %11.ab0 (concat \n\n(bvsizeext (bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1)) 32 1))) \n (vector reg_0 reg_1 reg_2 %4.ab0 %9.ab0 %10 %11.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64,
                    128
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-add_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32 0) (repair-vector-reduce-add_dsl 4 (reg (bv #x06 8)) 32 128) 32 32)",
                "synth_expression": "(_mm256_dpbusd_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 256 32 0 32 8 1 1 1 16 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0)))\n(define %9.ab0 (concat \n\n(bvsizeext (extract 255 248 b) 16 1)\n(bvsizeext (extract 247 240 b) 16 1)\n(bvsizeext (extract 239 232 b) 16 1)\n(bvsizeext (extract 231 224 b) 16 1)))\n(define %10 (concat \n\n(bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1))\n(bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1))\n(bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1))\n(bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1))))\n(define %11.ab0 (concat \n\n(bvsizeext (bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1)) 32 1))) \n (vector reg_0 reg_1 reg_2 %4.ab0 %9.ab0 %10 %11.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64,
                    128
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32 0) (repair-vector-reduce-add_dsl 4 (reg (bv #x06 8)) 32 128) 32 32)",
                "synth_expression": "(_mm256_dpbusd_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 256 32 0 32 8 -1 1 1 16 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0)))\n(define %9.ab0 (concat \n\n(bvsizeext (extract 255 248 b) 16 1)\n(bvsizeext (extract 247 240 b) 16 1)\n(bvsizeext (extract 239 232 b) 16 1)\n(bvsizeext (extract 231 224 b) 16 1)))\n(define %10 (concat \n\n(bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1))\n(bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1))\n(bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1))\n(bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1))))\n(define %11.ab0 (concat \n\n(bvsizeext (bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1)) 32 1))) \n (vector reg_0 reg_1 reg_2 %4.ab0 %9.ab0 %10 %11.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64,
                    128
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-ssat-add_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32 1) (repair-vector-reduce-add_dsl 4 (reg (bv #x06 8)) 32 128) 32 32)",
                "synth_expression": "(_mm256_dpbusd_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 256 32 0 32 8 1 1 1 16 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0)))\n(define %9.ab0 (concat \n\n(bvsizeext (extract 255 248 b) 16 1)\n(bvsizeext (extract 247 240 b) 16 1)\n(bvsizeext (extract 239 232 b) 16 1)\n(bvsizeext (extract 231 224 b) 16 1)))\n(define %10 (concat \n\n(bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1))\n(bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1))\n(bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1))\n(bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1))))\n(define %11.ab0 (concat \n\n(bvsizeext (bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1)) 32 1))) \n (vector reg_0 reg_1 reg_2 %4.ab0 %9.ab0 %10 %11.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64,
                    128
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-add_dsl (repair-vector-reduce-add_dsl 4 (reg (bv #x06 8)) 32 128) (typed-folded:broadcast_dsl (reg (bv #x00 8)) 32 1) 32 32)",
                "synth_expression": "(_mm256_dpbusd_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 256 32 0 32 8 -1 1 1 16 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0)))\n(define %9.ab0 (concat \n\n(bvsizeext (extract 255 248 b) 16 1)\n(bvsizeext (extract 247 240 b) 16 1)\n(bvsizeext (extract 239 232 b) 16 1)\n(bvsizeext (extract 231 224 b) 16 1)))\n(define %10 (concat \n\n(bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1))\n(bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1))\n(bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1))\n(bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1))))\n(define %11.ab0 (concat \n\n(bvsizeext (bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1)) 32 1))) \n (vector reg_0 reg_1 reg_2 %4.ab0 %9.ab0 %10 %11.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64,
                    128
                ],
                "src_env_sizes": [
                    256,
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_dpbusd_epi32",
                "output_expression": "(repair-add_dsl (repair-vector-reduce-add_dsl 4 (reg (bv #x06 8)) 32 128) (typed-folded:broadcast_dsl (reg (bv #x00 8)) 32 1) 32 32)",
                "synth_expression": "(_mm256_dpbusd_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 256 32 0 32 8 -1 1 1 16 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define src (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 255 224 src)))\n(define reg_1 (concat \n\n(extract 255 248 a)\n(extract 247 240 a)\n(extract 239 232 a)\n(extract 231 224 a)))\n(define reg_2 (concat \n\n(extract 255 248 b)\n(extract 247 240 b)\n(extract 239 232 b)\n(extract 231 224 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 255 248 a) 16 0)\n(bvsizeext (extract 247 240 a) 16 0)\n(bvsizeext (extract 239 232 a) 16 0)\n(bvsizeext (extract 231 224 a) 16 0)))\n(define %9.ab0 (concat \n\n(bvsizeext (extract 255 248 b) 16 1)\n(bvsizeext (extract 247 240 b) 16 1)\n(bvsizeext (extract 239 232 b) 16 1)\n(bvsizeext (extract 231 224 b) 16 1)))\n(define %10 (concat \n\n(bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1))\n(bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1))\n(bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1))\n(bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1))))\n(define %11.ab0 (concat \n\n(bvsizeext (bvmul (bvsizeext (extract 255 248 a) 16 0) (bvsizeext (extract 255 248 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 247 240 a) 16 0) (bvsizeext (extract 247 240 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 239 232 a) 16 0) (bvsizeext (extract 239 232 b) 16 1)) 32 1)\n(bvsizeext (bvmul (bvsizeext (extract 231 224 a) 16 0) (bvsizeext (extract 231 224 b) 16 1)) 32 1))) \n (vector reg_0 reg_1 reg_2 %4.ab0 %9.ab0 %10 %11.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
                    64,
                    128
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(typed-folded:vec-add_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 32 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) 32 32 -1)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 127 112 b) 32 1)\n(bvsizeext (extract 111 96 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 127 112 a) 32 1) (bvsizeext (extract 127 112 b) 32 1))\n(bvmul (bvsizeext (extract 111 96 a) 32 1) (bvsizeext (extract 111 96 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(typed-folded:vec-add_dsl (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) (reg (bv #x00 8)) 32 32 1)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 32 0 32 16 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 127 112 b) 32 1)\n(bvsizeext (extract 111 96 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 127 112 a) 32 1) (bvsizeext (extract 127 112 b) 32 1))\n(bvmul (bvsizeext (extract 111 96 a) 32 1) (bvsizeext (extract 111 96 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(typed-folded:vec-add_dsl (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) (repair-cast-int_dsl (reg (bv #x00 8)) 16 16 32) 32 32 -1)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 127 112 b) 32 1)\n(bvsizeext (extract 111 96 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 127 112 a) 32 1) (bvsizeext (extract 127 112 b) 32 1))\n(bvmul (bvsizeext (extract 111 96 a) 32 1) (bvsizeext (extract 111 96 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32 0) (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512))))\n(define reg_1 (concat \n\n(extract 511 496 a)\n(extract 495 480 a)))\n(define reg_2 (concat \n\n(extract 511 496 b)\n(extract 495 480 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 511 496 a) 32 1)\n(bvsizeext (extract 495 480 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 511 496 b) 32 1)\n(bvsizeext (extract 495 480 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 511 496 a) 32 1) (bvsizeext (extract 511 496 b) 32 1))\n(bvmul (bvsizeext (extract 495 480 a) 32 1) (bvsizeext (extract 495 480 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
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
                    512
                ]
            }
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32 -1) (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) 8 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512))))\n(define reg_1 (concat \n\n(extract 511 496 a)\n(extract 495 480 a)))\n(define reg_2 (concat \n\n(extract 511 496 b)\n(extract 495 480 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 511 496 a) 32 1)\n(bvsizeext (extract 495 480 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 511 496 b) 32 1)\n(bvsizeext (extract 495 480 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 511 496 a) 32 1) (bvsizeext (extract 511 496 b) 32 1))\n(bvmul (bvsizeext (extract 495 480 a) 32 1) (bvsizeext (extract 495 480 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
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
                    512
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-ssat-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 32 -1) (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) 8 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512))))\n(define reg_1 (concat \n\n(extract 511 496 a)\n(extract 495 480 a)))\n(define reg_2 (concat \n\n(extract 511 496 b)\n(extract 495 480 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 511 496 a) 32 1)\n(bvsizeext (extract 495 480 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 511 496 b) 32 1)\n(bvsizeext (extract 495 480 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 511 496 a) 32 1) (bvsizeext (extract 511 496 b) 32 1))\n(bvmul (bvsizeext (extract 495 480 a) 32 1) (bvsizeext (extract 495 480 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
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
                    512
                ]
            }
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-smul_dsl (typed-folded:vec-div_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 32 1) (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512))))\n(define reg_1 (concat \n\n(extract 511 496 a)\n(extract 495 480 a)))\n(define reg_2 (concat \n\n(extract 511 496 b)\n(extract 495 480 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 511 496 a) 32 1)\n(bvsizeext (extract 495 480 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 511 496 b) 32 1)\n(bvsizeext (extract 495 480 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 511 496 a) 32 1) (bvsizeext (extract 511 496 b) 32 1))\n(bvmul (bvsizeext (extract 495 480 a) 32 1) (bvsizeext (extract 495 480 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
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
                    512
                ]
            }
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0) (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) 16 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512))))\n(define reg_1 (concat \n\n(extract 511 496 a)\n(extract 495 480 a)))\n(define reg_2 (concat \n\n(extract 511 496 b)\n(extract 495 480 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 511 496 a) 32 1)\n(bvsizeext (extract 495 480 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 511 496 b) 32 1)\n(bvsizeext (extract 495 480 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 511 496 a) 32 1) (bvsizeext (extract 511 496 b) 32 1))\n(bvmul (bvsizeext (extract 495 480 a) 32 1) (bvsizeext (extract 495 480 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
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
                    512
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-ssat-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 32 0) (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512))))\n(define reg_1 (concat \n\n(extract 511 496 a)\n(extract 495 480 a)))\n(define reg_2 (concat \n\n(extract 511 496 b)\n(extract 495 480 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 511 496 a) 32 1)\n(bvsizeext (extract 495 480 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 511 496 b) 32 1)\n(bvsizeext (extract 495 480 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 511 496 a) 32 1) (bvsizeext (extract 511 496 b) 32 1))\n(bvmul (bvsizeext (extract 495 480 a) 32 1) (bvsizeext (extract 495 480 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
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
                    512
                ]
            }
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32 0) (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 127 112 b) 32 1)\n(bvsizeext (extract 111 96 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 127 112 a) 32 1) (bvsizeext (extract 127 112 b) 32 1))\n(bvmul (bvsizeext (extract 111 96 a) 32 1) (bvsizeext (extract 111 96 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-ssat-add_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32 1) (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 32 0 32 16 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 127 112 b) 32 1)\n(bvsizeext (extract 111 96 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 127 112 a) 32 1) (bvsizeext (extract 127 112 b) 32 1))\n(bvmul (bvsizeext (extract 111 96 a) 32 1) (bvsizeext (extract 111 96 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
    "_mm256_maddubs_epi16+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32 1) (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 127 112 b) 32 1)\n(bvsizeext (extract 111 96 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 127 112 a) 32 1) (bvsizeext (extract 127 112 b) 32 1))\n(bvmul (bvsizeext (extract 111 96 a) 32 1) (bvsizeext (extract 111 96 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-ssat-add_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32 0) (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 32 0 32 16 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 127 112 b) 32 1)\n(bvsizeext (extract 111 96 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 127 112 a) 32 1) (bvsizeext (extract 127 112 b) 32 1))\n(bvmul (bvsizeext (extract 111 96 a) 32 1) (bvsizeext (extract 111 96 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
    "_mm256_maddubs_epi16+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 127 112 b) 32 1)\n(bvsizeext (extract 111 96 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 127 112 a) 32 1) (bvsizeext (extract 127 112 b) 32 1))\n(bvmul (bvsizeext (extract 111 96 a) 32 1) (bvsizeext (extract 111 96 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-ssat-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 32 0 32 16 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 127 112 b) 32 1)\n(bvsizeext (extract 111 96 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 127 112 a) 32 1) (bvsizeext (extract 127 112 b) 32 1))\n(bvmul (bvsizeext (extract 111 96 a) 32 1) (bvsizeext (extract 111 96 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
    "_mm256_maddubs_epi16+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) (lit (bv #x00000000 32)) 8 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512))))\n(define reg_1 (concat \n\n(extract 511 496 a)\n(extract 495 480 a)))\n(define reg_2 (concat \n\n(extract 511 496 b)\n(extract 495 480 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 511 496 a) 32 1)\n(bvsizeext (extract 495 480 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 511 496 b) 32 1)\n(bvsizeext (extract 495 480 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 511 496 a) 32 1) (bvsizeext (extract 511 496 b) 32 1))\n(bvmul (bvsizeext (extract 495 480 a) 32 1) (bvsizeext (extract 495 480 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
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
                    512
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-ssat-add_dsl (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) (lit (bv #x00000000 32)) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 32 0 32 16 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512))))\n(define reg_1 (concat \n\n(extract 511 496 a)\n(extract 495 480 a)))\n(define reg_2 (concat \n\n(extract 511 496 b)\n(extract 495 480 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 511 496 a) 32 1)\n(bvsizeext (extract 495 480 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 511 496 b) 32 1)\n(bvsizeext (extract 495 480 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 511 496 a) 32 1) (bvsizeext (extract 511 496 b) 32 1))\n(bvmul (bvsizeext (extract 495 480 a) 32 1) (bvsizeext (extract 495 480 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
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
                    512
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-ssat-sub_dsl (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) (lit (bv #x00000000 32)) 8 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512))))\n(define reg_1 (concat \n\n(extract 511 496 a)\n(extract 495 480 a)))\n(define reg_2 (concat \n\n(extract 511 496 b)\n(extract 495 480 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 511 496 a) 32 1)\n(bvsizeext (extract 495 480 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 511 496 b) 32 1)\n(bvsizeext (extract 495 480 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 511 496 a) 32 1) (bvsizeext (extract 511 496 b) 32 1))\n(bvmul (bvsizeext (extract 495 480 a) 32 1) (bvsizeext (extract 495 480 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
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
                    512
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-vector-reduce-add_dsl 4 (typed-folded:cast-extend_dsl (reg (bv #x05 8)) 64 64 128 0) 32 128)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 511 480 (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512))))\n(define reg_1 (concat \n\n(extract 511 496 a)\n(extract 495 480 a)))\n(define reg_2 (concat \n\n(extract 511 496 b)\n(extract 495 480 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 511 496 a) 32 1)\n(bvsizeext (extract 495 480 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 511 496 b) 32 1)\n(bvsizeext (extract 495 480 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 511 496 a) 32 1) (bvsizeext (extract 511 496 b) 32 1))\n(bvmul (bvsizeext (extract 495 480 a) 32 1) (bvsizeext (extract 495 480 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
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
                    512
                ]
            }
        }
    ],
    "_mm256_maddubs_epi16+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) (typed-folded:broadcast_dsl (reg (bv #x00 8)) 32 1) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 127 112 b) 32 1)\n(bvsizeext (extract 111 96 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 127 112 a) 32 1) (bvsizeext (extract 127 112 b) 32 1))\n(bvmul (bvsizeext (extract 111 96 a) 32 1) (bvsizeext (extract 111 96 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-add_dsl (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) (typed-folded:broadcast_dsl (reg (bv #x00 8)) 16 2) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 32 0 32 16 -1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 127 112 b) 32 1)\n(bvsizeext (extract 111 96 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 127 112 a) 32 1) (bvsizeext (extract 127 112 b) 32 1))\n(bvmul (bvsizeext (extract 111 96 a) 32 1) (bvsizeext (extract 111 96 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-ssat-add_dsl (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) (typed-folded:broadcast_dsl (reg (bv #x00 8)) 16 2) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 32 0 32 16 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 127 112 b) 32 1)\n(bvsizeext (extract 111 96 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 127 112 a) 32 1) (bvsizeext (extract 127 112 b) 32 1))\n(bvmul (bvsizeext (extract 111 96 a) 32 1) (bvsizeext (extract 111 96 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "output_expression": "(repair-ssat-add_dsl (repair-vector-reduce-add_dsl 2 (reg (bv #x05 8)) 32 64) (typed-folded:broadcast_dsl (reg (bv #x00 8)) 32 1) 32 32)",
                "synth_expression": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 32 0 32 16 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define %arg0 (vector-ref env 0))\n(define a (vector-ref env 1))\n(define b (vector-ref env 2)) \n (define reg_0 (concat \n\n(extract 127 96 %arg0)))\n(define reg_1 (concat \n\n(extract 127 112 a)\n(extract 111 96 a)))\n(define reg_2 (concat \n\n(extract 127 112 b)\n(extract 111 96 b)))\n(define %14.ab0 (concat \n\n(bvsizeext (extract 127 112 a) 32 1)\n(bvsizeext (extract 111 96 a) 32 1)))\n(define %15.ab0 (concat \n\n(bvsizeext (extract 127 112 b) 32 1)\n(bvsizeext (extract 111 96 b) 32 1)))\n(define %16 (concat \n\n(bvmul (bvsizeext (extract 127 112 a) 32 1) (bvsizeext (extract 127 112 b) 32 1))\n(bvmul (bvsizeext (extract 111 96 a) 32 1) (bvsizeext (extract 111 96 b) 32 1)))) \n (vector reg_0 reg_1 reg_2 %14.ab0 %15.ab0 %16)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    32,
                    64,
                    64,
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
    "_mm256_madd52hi_epu64+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-add_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64 -1) (repair-usat-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 64 64) 16 64)",
                "synth_expression": "(_mm256_madd52hi_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 208 52 64 -1 0 52 52 0 128 0 52 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-usat-add_dsl (typed-folded:vec-add_dsl (reg (bv #x02 8)) (reg (bv #x07 8)) 64 64 -1) (repair-usat-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-usat-sub_dsl (typed-folded:vec-add_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64 -1) (repair-usat-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64) 32 64)",
                "synth_expression": "(_mm256_madd52hi_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 208 52 64 -1 0 52 52 0 128 0 52 0)",
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
    "_mm256_madd52hi_epu64+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 -1) (repair-add_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64) 32 64)",
                "synth_expression": "(_mm256_madd52hi_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 208 52 64 -1 0 52 52 0 128 0 52 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-usat-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x07 8)) (reg (bv #x07 8)) 8 64 0) (repair-add_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64) 64 64)",
                "synth_expression": "(_mm256_madd52hi_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 208 52 64 -1 0 52 52 0 128 0 52 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x02 8)) (reg (bv #x07 8)) 64 64 -1) (repair-usat-add_dsl (reg (bv #x07 8)) (reg (bv #x07 8)) 64 64) 64 64)",
                "synth_expression": "(_mm256_madd52hi_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 208 52 64 -1 0 52 52 0 128 0 52 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-usat-sub_dsl (repair-add_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64 -1) 16 64)",
                "synth_expression": "(_mm256_madd52hi_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 208 52 64 -1 0 52 52 0 128 0 52 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-add_dsl (reg (bv #x02 8)) (reg (bv #x07 8)) 64 64) (repair-usat-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64) 16 64 1)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-add_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-sub_dsl (reg (bv #x07 8)) (reg (bv #x07 8)) 16 64 1) 64 64 -1)",
                "synth_expression": "(_mm256_madd52hi_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 208 52 64 -1 0 52 52 0 128 0 52 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-usat-add_dsl (reg (bv #x07 8)) (reg (bv #x07 8)) 64 64) (typed-folded:vec-sub_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64 -1) 64 64 -1)",
                "synth_expression": "(_mm256_madd52hi_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 208 52 64 -1 0 52 52 0 128 0 52 0)",
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
    "_mm256_madd52hi_epu64+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x07 8)) (reg (bv #x07 8)) 32 64 0) (repair-add_dsl (reg (bv #x02 8)) (reg (bv #x07 8)) 64 64) 16 64)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-usat-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x07 8)) (reg (bv #x07 8)) 64 64 0) (repair-add_dsl (reg (bv #x02 8)) (reg (bv #x07 8)) 64 64) 64 64)",
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
    "_mm256_madd52hi_epu64+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64 0) (typed-folded:vec-min_dsl (reg (bv #x07 8)) (reg (bv #x07 8)) 64 64 1) 64 64)",
                "synth_expression": "(_mm256_madd52hi_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 208 52 64 -1 0 52 52 0 128 0 52 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64 0) (reg (bv #x07 8)) 64 64)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(typed-folded:vec-min_dsl (repair-add_dsl (reg (bv #x02 8)) (reg (bv #x07 8)) 64 64) (repair-add_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64) 8 64 1)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(typed-folded:vec-min_dsl (repair-usat-add_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64) (repair-add_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64) 16 64 0)",
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
    "_mm256_madd52hi_epu64+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 1) (reg (bv #x07 8)) 64 64)",
                "synth_expression": "(_mm256_madd52hi_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 208 52 64 -1 0 52 52 0 128 0 52 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64 0) (typed-folded:vec-max_dsl (reg (bv #x07 8)) (reg (bv #x07 8)) 16 64 0) 64 64)",
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
    "_mm256_madd52hi_epu64+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x07 8)) (reg (bv #x07 8)) 64 64) (reg (bv #x02 8)) 64 64)",
                "synth_expression": "(_mm256_madd52hi_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 208 52 64 -1 0 52 52 0 128 0 52 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x07 8)) (reg (bv #x07 8)) 64 64) (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 64 64) 64 64)",
                "synth_expression": "(_mm256_madd52hi_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 208 52 64 -1 0 52 52 0 128 0 52 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-add_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64) (repair-add_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64) 8 64)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-usat-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64) (repair-add_dsl (reg (bv #x07 8)) (reg (bv #x02 8)) 64 64) 16 64)",
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
    "_mm256_madd52hi_epu64+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x02 8)) (reg (bv #x07 8)) 64 64) (lit (bv #x0000000000000000 64)) 64 64)",
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
    "_mm256_madd52hi_epu64+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-add_dsl (typed-folded:broadcast_dsl (reg (bv #x02 8)) 64 1) (reg (bv #x07 8)) 64 64)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "output_expression": "(repair-add_dsl (typed-folded:broadcast_dsl (reg (bv #x02 8)) 16 4) (typed-folded:broadcast_dsl (reg (bv #x07 8)) 32 2) 64 64)",
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
    "_mm256_mul_epi32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-ssat-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 64) (repair-smul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) 8 64 0)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm256_mul_epi32+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-ssat-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64 -1) (repair-smul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) 8 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-ssat-sub_dsl (repair-smul_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64) (typed-folded:vec-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 0) 32 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-smul_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64) (repair-ssat-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 64) 64 64 1)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-smul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 64 1) 64 64 0)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm256_mul_epi32+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed-folded:vec-div_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 64 64 1) (repair-smul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm256_mul_epi32+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-ssat-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 1) (repair-smul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-ssat-sub_dsl (repair-smul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-mod_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 64 1) 16 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-smul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) (repair-ssat-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 64) 8 64 1)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-smul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-mod_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 64 1) 8 64 0)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm256_mul_epi32+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64 1) (reg (bv #x03 8)) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 64 1) (repair-cast-int_dsl (reg (bv #x02 8)) 16 16 64) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm256_mul_epi32+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64 0) (reg (bv #x03 8)) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 1) (repair-cast-int_dsl (reg (bv #x03 8)) 16 16 64) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 1) (typed-folded:vec-max_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 64 1) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed-folded:vec-max_dsl (repair-ssat-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64) (repair-smul_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64) 64 64 0)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed-folded:vec-max_dsl (repair-smul_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64) (repair-smul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) 8 64 1)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm256_mul_epi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 64) (reg (bv #x02 8)) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64) (repair-cast-int_dsl (reg (bv #x03 8)) 32 32 64) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64) (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 64) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm256_mul_epi32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (repair-cast-int_dsl (reg (bv #x03 8)) 16 16 64) (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 32 64 1) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm256_mul_epi32+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (repair-cast-int_dsl (reg (bv #x02 8)) 16 16 64) (typed-folded:broadcast_dsl (reg (bv #x03 8)) 16 4) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed-folded:broadcast_dsl (reg (bv #x02 8)) 16 4) (reg (bv #x03 8)) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    256,
                    256
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed-folded:broadcast_dsl (reg (bv #x02 8)) 32 2) (typed-folded:broadcast_dsl (reg (bv #x03 8)) 16 4) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 223 192 a)))\n(define reg_1 (concat \n\n(extract 223 192 b)))\n(define %4.ab0 (concat \n\n(bvsizeext (extract 223 192 a) 64 1)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 223 192 b) 64 1))) \n (vector reg_0 reg_1 %4.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm512_mulhi_epu16+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:vec-add_dsl (repair-usat-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 32 64 1)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
    "_mm512_mulhi_epu16+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 -1) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64 -1)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64 0) 64 64 -1)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
    "_mm512_mulhi_epu16+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:vec-div_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64 1) 32 64 1)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
    "_mm512_mulhi_epu16+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64 1) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 1) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64 0)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 0) 32 64 1)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
    "_mm512_mulhi_epu16+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 0) (reg (bv #x00 8)) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 1) (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 1) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:vec-min_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 8 64 0)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
    "_mm512_mulhi_epu16+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0) (reg (bv #x00 8)) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 0) (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 0) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:vec-max_dsl (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64 0)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:vec-max_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 64 64 0)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
    "_mm512_mulhi_epu16+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (reg (bv #x01 8)) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-usat-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
    "_mm512_mulhi_epu16+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x0000000000000000 64)) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x0000000000000000 64)) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
    "_mm512_mulhi_epu16+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed-folded:broadcast_dsl (reg (bv #x01 8)) 64 1) (reg (bv #x00 8)) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 8 8) (typed-folded:broadcast_dsl (reg (bv #x01 8)) 16 4) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 64 a)))\n(define reg_1 (concat \n\n(extract 127 64 b)))\n(define %6.ab0 (concat \n\n(bvsizeext (extract 127 64 a) 128 0)))\n(define %7.ab0 (concat \n\n(bvsizeext (extract 127 64 b) 128 0)))\n(define %8 (concat \n\n(bvmul (bvsizeext (extract 127 64 a) 128 0) (bvsizeext (extract 127 64 b) 128 0)))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0 %8)\n)",
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
    "_mm_mul_su32+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-add_dsl (repair-usat-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64) (repair-umul_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64) 64 64 1)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm_mul_su32+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 1) (repair-umul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) (typed-folded:vec-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 64 -1) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm_mul_su32+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-div_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 64 0) (repair-umul_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm_mul_su32+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 0) (repair-umul_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64) (typed-folded:vec-mod_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 1) 8 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-umul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) (repair-usat-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 64) 32 64 0)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-umul_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64) (typed-folded:vec-mod_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64 1) 8 64 1)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm_mul_su32+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 64 1) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 64 1) (reg (bv #x02 8)) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm_mul_su32+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-max_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 64 1) (reg (bv #x02 8)) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64 0) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 64 32) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-max_dsl (repair-umul_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 32 64) (repair-umul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) 64 64 0)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed-folded:vec-max_dsl (repair-usat-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 64) (repair-umul_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) 64 64 0)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm_mul_su32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 64) (reg (bv #x02 8)) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 64) (repair-cast-uint_dsl (reg (bv #x02 8)) 16 16 64) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 64) (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm_mul_su32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 32 32 64 0) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm_mul_su32+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x02 8)) 32 32 64) (typed-folded:broadcast_dsl (reg (bv #x03 8)) 16 4) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (typed-folded:broadcast_dsl (reg (bv #x02 8)) 32 2) (reg (bv #x03 8)) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
                    64,
                    64
                ],
                "src_env_sizes": [
                    64,
                    64
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (typed-folded:broadcast_dsl (reg (bv #x02 8)) 8 8) (typed-folded:broadcast_dsl (reg (bv #x03 8)) 64 1) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 31 0 a)))\n(define reg_1 (concat \n\n(extract 31 0 b)))\n(define %2.ab0 (concat \n\n(bvsizeext (extract 31 0 a) 64 0)))\n(define %3.ab0 (concat \n\n(bvsizeext (extract 31 0 b) 64 0))) \n (vector reg_0 reg_1 %2.ab0 %3.ab0)\n)",
                "target_input_sizes": [
                    32,
                    32,
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
    "_mm_avg_epu8+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-ushr_dsl (reg (bv #x03 8)) (typed-folded:vec-sub_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 16 0) 16 16)",
                "synth_expression": "(_mm_avg_epu8_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 -1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 112 a)))\n(define reg_1 (concat \n\n(extract 127 112 b)))\n(define %6.ab0 (concat \n\n(bvaddnw (extract 127 112 a) (extract 127 112 b) 16 -1)))\n(define %7.ab0 (concat \n\n(bvaddnw (bvaddnw (extract 127 112 a) (extract 127 112 b) 16 -1) (bv #x0000000000000001 16) 16 -1))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    16,
                    16,
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
    "_mm_avg_epu8+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-ushr_dsl (reg (bv #x03 8)) (typed-folded:vec-div_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 16 1) 16 16)",
                "synth_expression": "(_mm_avg_epu8_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 -1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 112 a)))\n(define reg_1 (concat \n\n(extract 127 112 b)))\n(define %6.ab0 (concat \n\n(bvaddnw (extract 127 112 a) (extract 127 112 b) 16 -1)))\n(define %7.ab0 (concat \n\n(bvaddnw (bvaddnw (extract 127 112 a) (extract 127 112 b) 16 -1) (bv #x0000000000000001 16) 16 -1))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    16,
                    16,
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-ushr_dsl (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 16 1) (repair-usat-sub_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 16) 16 16)",
                "synth_expression": "(_mm_avg_epu8_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 -1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 112 a)))\n(define reg_1 (concat \n\n(extract 127 112 b)))\n(define %6.ab0 (concat \n\n(bvaddnw (extract 127 112 a) (extract 127 112 b) 16 -1)))\n(define %7.ab0 (concat \n\n(bvaddnw (bvaddnw (extract 127 112 a) (extract 127 112 b) 16 -1) (bv #x0000000000000001 16) 16 -1))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    16,
                    16,
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-ushr_dsl (typed-folded:vec-max_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 16 1) (repair-usat-sub_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 16) 16 16)",
                "synth_expression": "(_mm_avg_epu8_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 -1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 112 a)))\n(define reg_1 (concat \n\n(extract 127 112 b)))\n(define %6.ab0 (concat \n\n(bvaddnw (extract 127 112 a) (extract 127 112 b) 16 -1)))\n(define %7.ab0 (concat \n\n(bvaddnw (bvaddnw (extract 127 112 a) (extract 127 112 b) 16 -1) (bv #x0000000000000001 16) 16 -1))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    16,
                    16,
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-ushr_dsl (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 16) (repair-usat-sub_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 16) 16 16)",
                "synth_expression": "(_mm_avg_epu8_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 -1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 112 a)))\n(define reg_1 (concat \n\n(extract 127 112 b)))\n(define %6.ab0 (concat \n\n(bvaddnw (extract 127 112 a) (extract 127 112 b) 16 -1)))\n(define %7.ab0 (concat \n\n(bvaddnw (bvaddnw (extract 127 112 a) (extract 127 112 b) 16 -1) (bv #x0000000000000001 16) 16 -1))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    16,
                    16,
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
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_avg_epu8",
                "output_expression": "(repair-ushr_dsl (typed-folded:broadcast_dsl (reg (bv #x03 8)) 16 1) (repair-usat-sub_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 16) 16 16)",
                "synth_expression": "(_mm_avg_epu8_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 -1 0)",
                "env-func": "(define (prepare-env env) \n\n(define a (vector-ref env 0))\n(define b (vector-ref env 1)) \n (define reg_0 (concat \n\n(extract 127 112 a)))\n(define reg_1 (concat \n\n(extract 127 112 b)))\n(define %6.ab0 (concat \n\n(bvaddnw (extract 127 112 a) (extract 127 112 b) 16 -1)))\n(define %7.ab0 (concat \n\n(bvaddnw (bvaddnw (extract 127 112 a) (extract 127 112 b) 16 -1) (bv #x0000000000000001 16) 16 -1))) \n (vector reg_0 reg_1 %6.ab0 %7.ab0)\n)",
                "target_input_sizes": [
                    16,
                    16,
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
    "_mm_add_si64+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 1) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 -1) 64 64 0)",
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
    "_mm_add_si64+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 1) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 1) 32 64 1)",
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
    "_mm_add_si64+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64 0) (reg (bv #x00 8)) 64 64)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 0) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0) 64 64)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed-folded:vec-min_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64 1)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)",
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
    "_mm_add_si64+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64 0) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 0) (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 0) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed-folded:vec-max_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64 1)",
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
    "_mm_add_si64+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (reg (bv #x00 8)) 64 64)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 64 64)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
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
    "_mm_add_si64+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (lit (bv #x0000000000000000 64)) 32 64)",
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
    "_mm_add_si64+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed-folded:broadcast_dsl (reg (bv #x01 8)) 64 1) (reg (bv #x00 8)) 64 64)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed-folded:broadcast_dsl (reg (bv #x01 8)) 32 2) (typed-folded:broadcast_dsl (reg (bv #x00 8)) 8 8) 64 64)",
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
    "_mm_hadd_pi16+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32 1) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 16 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32 1) 32 32 0)",
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
    "_mm_hadd_pi16+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32 1) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 1) 16 32 0)",
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
    "_mm_hadd_pi16+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32 1) (reg (bv #x00 8)) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32 1) (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 1) 32 32)",
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
    "_mm_hadd_pi16+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32 1) (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32 1) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32 0) (reg (bv #x01 8)) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed-folded:vec-max_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 8 32 0)",
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
    "_mm_hadd_pi16+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (reg (bv #x00 8)) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 16 32)",
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
    "_mm_hadd_pi16+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (lit (bv #x00000000 32)) 16 32)",
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
    "_mm_hadd_pi16+typed-folded:cast-truncate": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (lit (bv #x00000000 32)) 16 32)",
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
    "_mm_hadd_pi16+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed-folded:broadcast_dsl (reg (bv #x01 8)) 32 1) (reg (bv #x00 8)) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 32 1) (typed-folded:broadcast_dsl (reg (bv #x01 8)) 32 1) 32 32)",
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
    "_mm_broadcastmb_epi64+typed-folded:vec-add": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x00000000 32)) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x00000000 32)) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 8 32 1)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 8 32 1)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 8 32 1)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 8 32 1)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x00000000 32)) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x00000000 32)) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 32 32 1)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 32 32 1)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 32 32 1)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 32 32 1)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0) 16 32 16)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0) 16 32 16)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x00000000 32)) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed-folded:vec-max_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32 1)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x00000000 32)) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 8 32 0)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x00000000 32)) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 16 32 0)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x00000000 32)) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32 0)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed-folded:vec-max_dsl (lit (bv #x00000000 32)) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 8 32 0)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 32 16)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (lit (bv #x00000000 32)) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 16 32 0) 32 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed-folded:cast-truncate": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-cast-uint_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 16 1) 16 32 16)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed-folded:ramp": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00000000 32)) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)",
                "env-func": "(define (prepare-env env) \n\n(define k (vector-ref env 0)) \n (define reg_0 (concat \n\n(extract 15 0 k))) \n (vector reg_0)\n)",
                "target_input_sizes": [
                    16
                ],
                "src_env_sizes": [
                    16
                ]
            }
        }
    ],
    "_mm_hadd_pi32+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x04 8)) (reg (bv #x00 8)) 8 32 -1) (reg (bv #x00 8)) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 32 0) (repair-add_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 32 32) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x04 8)) (reg (bv #x01 8)) 16 32 -1) (typed-folded:vec-sub_dsl (reg (bv #x04 8)) (reg (bv #x00 8)) 32 32 -1) 16 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-sub_dsl (reg (bv #x04 8)) (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32 -1) 32 32 -1)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-add_dsl (reg (bv #x04 8)) (reg (bv #x03 8)) 8 32) (reg (bv #x03 8)) 8 32 -1)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-add_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 8 32) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 8 32 -1)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (typed-folded:vec-sub_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 32 1) 32 32 -1)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-sub_dsl (typed-folded:vec-sub_dsl (reg (bv #x04 8)) (reg (bv #x00 8)) 32 32 -1) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x04 8)) 16 32 -1) 16 32 -1)",
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
    "_mm_hadd_pi32+typed-folded:vec-div": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-div_dsl (reg (bv #x04 8)) (typed-folded:vec-div_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 32 32 1) 32 32 1)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-div_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (typed-folded:vec-div_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 32 32 1) 32 32 0)",
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
    "_mm_hadd_pi32+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 32 1) (reg (bv #x04 8)) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 0) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-mod_dsl (reg (bv #x04 8)) (typed-folded:vec-mod_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 32 0) 16 32 0)",
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
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 32 1) (reg (bv #x03 8)) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-min_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (reg (bv #x04 8)) 32 32 1)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 32 0) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 32 1) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-min_dsl (typed-folded:vec-min_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 8 32 0) (reg (bv #x04 8)) 8 32 1)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-min_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 32 32 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-min_dsl (typed-folded:vec-min_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 8 32 0) (typed-folded:vec-min_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 16 32 0) 32 32 1)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-min_dsl (typed-folded:vec-min_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 8 32 1) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 32 32 0)",
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
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32 0) (reg (bv #x01 8)) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 1) (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32 0) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-max_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (reg (bv #x04 8)) 8 32 1)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-max_dsl (typed-folded:vec-max_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 16 32 1) (reg (bv #x04 8)) 8 32 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-max_dsl (typed-folded:vec-max_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 32 32 0) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 16 32 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-max_dsl (typed-folded:vec-max_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 32 32 0) (typed-folded:vec-max_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 32 32 0) 16 32 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-max_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 32 32 0)",
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
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32) (reg (bv #x01 8)) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (reg (bv #x04 8)) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (typed-folded:vec-bwor_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 8 32) 16 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-bwor_dsl (typed-folded:vec-bwor_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 8 32) (reg (bv #x04 8)) 16 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed-folded:vec-bwor_dsl (typed-folded:vec-bwor_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 16 32) (typed-folded:vec-bwor_dsl (reg (bv #x04 8)) (reg (bv #x04 8)) 8 32) 16 32)",
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
    "_mm_hadd_pi32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (lit (bv #x00000000 32)) (reg (bv #x04 8)) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (lit (bv #x00000000 32)) 32 32)",
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
    "_mm_hadd_pi32+typed-folded:cast-truncate": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (lit (bv #x00000000 32)) (reg (bv #x04 8)) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (lit (bv #x00000000 32)) 8 32)",
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
    "_mm_hadd_pi32+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed-folded:broadcast_dsl (reg (bv #x01 8)) 32 1) (reg (bv #x00 8)) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 8 4) (typed-folded:broadcast_dsl (reg (bv #x01 8)) 16 2) 32 32)",
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
    "_mm_add_pi8+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64 1) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)",
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
    "_mm_add_pi8+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 1) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 1) 32 64 0)",
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
    "_mm_add_pi8+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 1) (reg (bv #x00 8)) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed-folded:vec-min_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 8 64 1)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
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
    "_mm_add_pi8+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 0) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 1) (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64 0) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed-folded:vec-max_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 16 64 1)",
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
    "_mm_add_pi8+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)",
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
    "_mm_add_pi8+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x0000000000000000 64)) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
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
    "_mm_add_pi8+typed-folded:broadcast": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 32 2) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (typed-folded:broadcast_dsl (reg (bv #x00 8)) 64 1) (typed-folded:broadcast_dsl (reg (bv #x01 8)) 64 1) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
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
                "output_expression": "(repair-ssat-sub_dsl (typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64 0) (repair-ssat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0 32 0 32 0)",
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
    "_mm256_hadd_epi32+typed-folded:vec-sub": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32 1) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed-folded:vec-sub_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32 0) 32 32 0)",
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
    "_mm256_hadd_epi32+typed-folded:vec-mod": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32 0) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 16 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed-folded:vec-mod_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32 1) 32 32 1)",
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
    "_mm256_hadd_epi32+typed-folded:vec-min": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32 1) (reg (bv #x01 8)) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32 0) (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32 0) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed-folded:vec-min_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 8 32 1)",
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
    "_mm256_hadd_epi32+typed-folded:vec-max": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 1) (reg (bv #x00 8)) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32 0) (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32 0) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed-folded:vec-max_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 16 32 0)",
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
    "_mm256_hadd_epi32+typed-folded:vec-bwor": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (reg (bv #x00 8)) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32) (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed-folded:vec-bwor_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 32 32)",
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
    "_mm256_hadd_epi32+typed-folded:cast-extend": [
        {
            "property_name": "RepairRelavanceV4",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (lit (bv #x00000000 32)) 32 32)",
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
    ]
}