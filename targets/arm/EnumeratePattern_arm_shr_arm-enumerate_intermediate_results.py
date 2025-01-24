{
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+64+vshl_s64+typed:vec-shl_p64_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 64 0 1 128 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshl_s64",
                "dst_ctx": "typed:vec-shl_p64_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+128+vshlq_s16+typed:vec-shl_p16_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 128 128 0 128 16 0 1 32 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 16 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshlq_s16",
                "dst_ctx": "typed:vec-shl_p16_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+64+vshld_u64+typed:vec-shl_p32_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 64 0 0 128 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshld_u64",
                "dst_ctx": "typed:vec-shl_p32_s64_signed_None"
            }
        }
    ],
    " (vshrq_n_u8_dsl ; vshrq_n_u32\n\t(lit (bv #x00000000 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is32_op16_os64_signed_0\n\t\t(buffer-index  1 'uint8 32) ; < 4 x i8> False\n\t\t8\n\t\t1\n\t\t4\n\t\t16\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n\t64\n )+ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t\t(buffer-index  1 'uint8 32) ; < 4 x i8> False\n\t\t32\n\t\t32\n\t\t4\n\t )\n\t32\n\t128\n )+128+vshrq_n_u32+typed:unsigned-vec-shr_p32_s128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshrq_n_u8_dsl (lit (bv #x00000000 32)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 4 16) 128 128 0 128 32 -1 0 0 64)",
                "dst": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 32 32 4) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vshrq_n_u8_dsl ; vshrq_n_u32\n\t(lit (bv #x00000000 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is32_op16_os64_signed_0\n\t\t(buffer-index  1 'uint8 32) ; < 4 x i8> False\n\t\t8\n\t\t1\n\t\t4\n\t\t16\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n\t64\n )",
                "original_dst_expr": " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t\t(buffer-index  1 'uint8 32) ; < 4 x i8> False\n\t\t32\n\t\t32\n\t\t4\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshrq_n_u32",
                "dst_ctx": "typed:unsigned-vec-shr_p32_s128_signed_0"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+128+vshlq_s8+typed:vec-shl_p8_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 128 128 0 128 8 0 1 16 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 8 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshlq_s8",
                "dst_ctx": "typed:vec-shl_p8_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+64+vshl_s64+typed:vec-shl_p32_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 64 0 1 128 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshl_s64",
                "dst_ctx": "typed:vec-shl_p32_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+128+vshlq_u32+typed:vec-shl_p32_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 128 128 0 128 32 0 0 64 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshlq_u32",
                "dst_ctx": "typed:vec-shl_p32_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+128+vshlq_u16+typed:vec-shl_p16_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 128 128 0 128 16 0 0 32 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 16 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshlq_u16",
                "dst_ctx": "typed:vec-shl_p16_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+128+vshlq_u64+typed:vec-shl_p64_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 128 128 0 128 64 0 0 128 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 64 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshlq_u64",
                "dst_ctx": "typed:vec-shl_p64_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+64+vshl_s32+typed:vec-shl_p64_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 32 0 1 64 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshl_s32",
                "dst_ctx": "typed:vec-shl_p64_s64_signed_None"
            }
        }
    ],
    " (vshrq_n_u8_dsl ; vshrq_n_u32\n\t(lit (bv #x00000000 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is32_op16_os64_signed_0\n\t\t(buffer-index  1 'uint8 32) ; < 4 x i8> False\n\t\t8\n\t\t1\n\t\t4\n\t\t16\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n\t64\n )+ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t\t(buffer-index  1 'uint8 32) ; < 4 x i8> False\n\t\t32\n\t\t32\n\t\t4\n\t )\n\t32\n\t128\n )+64+vshr_n_u32+typed:unsigned-vec-shr_p32_s64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshrq_n_u8_dsl (lit (bv #x00000000 32)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 4 16) 64 64 0 64 32 -1 0 0 64)",
                "dst": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 32 32 2) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vshrq_n_u8_dsl ; vshrq_n_u32\n\t(lit (bv #x00000000 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is32_op16_os64_signed_0\n\t\t(buffer-index  1 'uint8 32) ; < 4 x i8> False\n\t\t8\n\t\t1\n\t\t4\n\t\t16\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n\t64\n )",
                "original_dst_expr": " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t\t(buffer-index  1 'uint8 32) ; < 4 x i8> False\n\t\t32\n\t\t32\n\t\t4\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshr_n_u32",
                "dst_ctx": "typed:unsigned-vec-shr_p32_s64_signed_0"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+64+vshl_s8+typed:vec-shl_p8_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 8 0 1 16 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 8 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshl_s8",
                "dst_ctx": "typed:vec-shl_p8_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+64+vshld_u64+typed:vec-shl_p64_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 64 0 0 128 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshld_u64",
                "dst_ctx": "typed:vec-shl_p64_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+64+vshl_s32+typed:vec-shl_p32_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 32 0 1 64 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshl_s32",
                "dst_ctx": "typed:vec-shl_p32_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+128+vshlq_u32+typed:vec-shl_p64_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 128 128 0 128 32 0 0 64 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 64 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshlq_u32",
                "dst_ctx": "typed:vec-shl_p64_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+128+vshlq_u64+typed:vec-shl_p32_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 128 128 0 128 64 0 0 128 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshlq_u64",
                "dst_ctx": "typed:vec-shl_p32_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+128+vshlq_u8+typed:vec-shl_p8_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 128 128 0 128 8 0 0 16 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 8 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshlq_u8",
                "dst_ctx": "typed:vec-shl_p8_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+64+vshl_u16+typed:vec-shl_p16_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 16 0 0 32 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 16 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshl_u16",
                "dst_ctx": "typed:vec-shl_p16_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+64+vshl_u32+typed:vec-shl_p32_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 32 0 0 64 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshl_u32",
                "dst_ctx": "typed:vec-shl_p32_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+128+vshlq_s32+typed:vec-shl_p32_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 128 128 0 128 32 0 1 64 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshlq_s32",
                "dst_ctx": "typed:vec-shl_p32_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+128+vshlq_s32+typed:vec-shl_p64_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 128 128 0 128 32 0 1 64 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 64 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshlq_s32",
                "dst_ctx": "typed:vec-shl_p64_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+64+vshl_u8+typed:vec-shl_p8_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 8 0 0 16 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 8 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshl_u8",
                "dst_ctx": "typed:vec-shl_p8_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+128+vshlq_s8+typed:vec-shl_p8_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 128 128 0 128 8 0 1 16 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshlq_s8",
                "dst_ctx": "typed:vec-shl_p8_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+64+vshl_u32+typed:vec-shl_p64_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 32 0 0 64 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshl_u32",
                "dst_ctx": "typed:vec-shl_p64_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+64+vshl_s32+typed:vec-shl_p32_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 64 64 0 64 32 0 1 64 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshl_s32",
                "dst_ctx": "typed:vec-shl_p32_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+128+vshlq_u64+typed:vec-shl_p64_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 64 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshlq_u64",
                "dst_ctx": "typed:vec-shl_p64_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+64+vshl_s16+typed:vec-shl_p16_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 16 0 1 32 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 16 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshl_s16",
                "dst_ctx": "typed:vec-shl_p16_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+64+vshl_s64+typed:vec-shl_p64_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 64 64 0 64 64 0 1 128 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 64 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshl_s64",
                "dst_ctx": "typed:vec-shl_p64_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+128+vshlq_s64+typed:vec-shl_p64_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 128 128 0 128 64 0 1 128 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 64 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshlq_s64",
                "dst_ctx": "typed:vec-shl_p64_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )+128+vshlq_s64+typed:vec-shl_p32_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 128 128 0 128 64 0 1 128 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n\t128\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p32_s128_signed_None\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vshlq_s64",
                "dst_ctx": "typed:vec-shl_p32_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+64+vshl_s8+typed:vec-shl_p8_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 64 64 0 64 8 0 1 16 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 8 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshl_s8",
                "dst_ctx": "typed:vec-shl_p8_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+128+vshlq_u32+typed:vec-shl_p32_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshlq_u32",
                "dst_ctx": "typed:vec-shl_p32_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+64+vshld_u64+typed:vec-shl_p64_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 64 64 0 64 64 0 0 128 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 64 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshld_u64",
                "dst_ctx": "typed:vec-shl_p64_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+128+vshlq_u16+typed:vec-shl_p16_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 128 128 0 128 16 0 0 32 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 16 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshlq_u16",
                "dst_ctx": "typed:vec-shl_p16_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+128+vshlq_s16+typed:vec-shl_p16_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 16 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshlq_s16",
                "dst_ctx": "typed:vec-shl_p16_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+128+vshlq_u8+typed:vec-shl_p8_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 128 128 0 128 8 0 0 16 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshlq_u8",
                "dst_ctx": "typed:vec-shl_p8_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+64+vshl_u16+typed:vec-shl_p16_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 64 64 0 64 16 0 0 32 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 16 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshl_u16",
                "dst_ctx": "typed:vec-shl_p16_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+64+vshl_u8+typed:vec-shl_p8_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 64 64 0 64 8 0 0 16 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 8 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshl_u8",
                "dst_ctx": "typed:vec-shl_p8_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+128+vshlq_s32+typed:vec-shl_p32_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 128 128 0 128 32 0 1 64 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshlq_s32",
                "dst_ctx": "typed:vec-shl_p32_s128_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+64+vshl_s16+typed:vec-shl_p16_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 64 64 0 64 16 0 1 32 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 16 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshl_s16",
                "dst_ctx": "typed:vec-shl_p16_s64_signed_None"
            }
        }
    ],
    " (vsraq_n_u8_dsl ; vsraq_n_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is32_op16_os64_signed_0\n\t\t(buffer-index  2 'uint8 32) ; < 4 x i8> False\n\t\t8\n\t\t1\n\t\t4\n\t\t16\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n\t64\n )+ (typed:vec-add ; typed:vec-add_p32_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 32) ; < 4 x i8> False\n\t\t\t32\n\t\t\t32\n\t\t\t4\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+64+vsra_n_u32+typed:vec-add_p32_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vsraq_n_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x02 8)) 8 1 4 16) 64 64 0 64 32 -1 0 0 64)",
                "dst": "(typed:vec-add (typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 32 32 2) 32 64) (reg (bv #x01 8)) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vsraq_n_u8_dsl ; vsraq_n_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is32_op16_os64_signed_0\n\t\t(buffer-index  2 'uint8 32) ; < 4 x i8> False\n\t\t8\n\t\t1\n\t\t4\n\t\t16\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n\t64\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 32) ; < 4 x i8> False\n\t\t\t32\n\t\t\t32\n\t\t\t4\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vsra_n_u32",
                "dst_ctx": "typed:vec-add_p32_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+64+vshl_u32+typed:vec-shl_p32_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 64 64 0 64 32 0 0 64 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) (reg (bv #x01 8)) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshl_u32",
                "dst_ctx": "typed:vec-shl_p32_s64_signed_None"
            }
        }
    ],
    " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )+ (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+128+vshlq_s64+typed:vec-shl_p64_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 128 128 0 128 64 0 1 128 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 64 128)",
                "output_size": 128,
                "original_src_expr": " (vshl_s8_dsl ; vshlq_u16\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t1\n )",
                "original_dst_expr": " (typed:vec-shl ; typed:vec-shl_p16_s128_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vshlq_s64",
                "dst_ctx": "typed:vec-shl_p64_s128_signed_None"
            }
        }
    ],
    " (vsraq_n_u8_dsl ; vsraq_n_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is32_op16_os64_signed_0\n\t\t(buffer-index  2 'uint8 32) ; < 4 x i8> False\n\t\t8\n\t\t1\n\t\t4\n\t\t16\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n\t64\n )+ (typed:vec-add ; typed:vec-add_p32_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 32) ; < 4 x i8> False\n\t\t\t32\n\t\t\t32\n\t\t\t4\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+128+vsraq_n_u32+typed:vec-add_p32_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vsraq_n_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x02 8)) 8 1 4 16) 128 128 0 128 32 -1 0 0 64)",
                "dst": "(typed:vec-add (typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 32 32 4) 32 128) (reg (bv #x01 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vsraq_n_u8_dsl ; vsraq_n_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is32_op16_os64_signed_0\n\t\t(buffer-index  2 'uint8 32) ; < 4 x i8> False\n\t\t8\n\t\t1\n\t\t4\n\t\t16\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n\t64\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 32) ; < 4 x i8> False\n\t\t\t32\n\t\t\t32\n\t\t\t4\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vsraq_n_u32",
                "dst_ctx": "typed:vec-add_p32_s128_signed_None"
            }
        }
    ],
    " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )+ (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t8\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+64+vsra_n_u32+typed:vec-add_p32_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vsraq_n_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 4) 64 64 0 64 32 -1 0 0 64)",
                "dst": "(typed:vec-add (typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 4) 32 64) (reg (bv #x01 8)) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t8\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vsra_n_u32",
                "dst_ctx": "typed:vec-add_p32_s64_signed_None"
            }
        }
    ],
    " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )+ (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t8\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+64+vsra_n_u16+typed:vec-add_p16_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vsraq_n_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 4) 64 64 0 64 16 -1 0 0 64)",
                "dst": "(typed:vec-add (typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 4) 32 64) (reg (bv #x01 8)) 16 64)",
                "output_size": 64,
                "original_src_expr": " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t8\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vsra_n_u16",
                "dst_ctx": "typed:vec-add_p16_s64_signed_None"
            }
        }
    ],
    " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )+ (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t8\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+128+vsraq_n_u8+typed:vec-add_p8_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vsraq_n_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 4) 128 128 0 128 8 -1 0 0 64)",
                "dst": "(typed:vec-add (typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 8) 32 128) (reg (bv #x01 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t8\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vsraq_n_u8",
                "dst_ctx": "typed:vec-add_p8_s128_signed_None"
            }
        }
    ],
    " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )+ (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t8\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+128+vsraq_n_u32+typed:vec-add_p32_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vsraq_n_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 4) 128 128 0 128 32 -1 0 0 64)",
                "dst": "(typed:vec-add (typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 8) 32 128) (reg (bv #x01 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t8\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vsraq_n_u32",
                "dst_ctx": "typed:vec-add_p32_s128_signed_None"
            }
        }
    ],
    " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )+ (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t8\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+128+vsraq_n_u16+typed:vec-add_p16_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vsraq_n_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 4) 128 128 0 128 16 -1 0 0 64)",
                "dst": "(typed:vec-add (typed:unsigned-vec-shr (reg (bv #x01 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 8) 64 128) (reg (bv #x00 8)) 16 128)",
                "output_size": 128,
                "original_src_expr": " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t8\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vsraq_n_u16",
                "dst_ctx": "typed:vec-add_p16_s128_signed_None"
            }
        }
    ],
    " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )+ (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t8\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+64+vsra_n_u8+typed:vec-add_p8_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_shr",
            "property": {
                "src": "(vsraq_n_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 4) 64 64 0 64 8 -1 0 0 64)",
                "dst": "(typed:vec-add (typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 4) 64 64) (reg (bv #x01 8)) 8 64)",
                "output_size": 64,
                "original_src_expr": " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t8\n\t\t )\n\t\t32\n\t\t128\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vsra_n_u8",
                "dst_ctx": "typed:vec-add_p8_s64_signed_None"
            }
        }
    ]
}