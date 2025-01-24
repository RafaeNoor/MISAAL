{
    " (vrshrd_n_s64_dsl ; vrshrd_n_s64\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 128)))\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t128\n\t-1\n\t0\n\t-1\n\t1\n )+ (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s64_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t64\n\t64\n )+64+vrshrd_n_s64+typed:signed-vec-shr_p64_s64_signed_1": [
        {
            "property_name": "EnumeratePatternarm_missing_ashr",
            "property": {
                "src": "(vrshrd_n_s64_dsl (lit (bv #x0000000000000000 64)) (lit (bv #x00000000000000000000000000000001 128)) (lit (bv #x00000000000000000000000000000001 128)) (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 64 -1 0 128 -1 0 -1 1)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64)",
                "output_size": 64,
                "original_src_expr": " (vrshrd_n_s64_dsl ; vrshrd_n_s64\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 128)))\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t128\n\t-1\n\t0\n\t-1\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s64_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t64\n\t64\n )",
                "src_ctx": "vrshrd_n_s64",
                "dst_ctx": "typed:signed-vec-shr_p64_s64_signed_1"
            }
        }
    ],
    " (vrshrd_n_s64_dsl ; vrshrd_n_s64\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 128)))\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t128\n\t-1\n\t0\n\t-1\n\t1\n )+ (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s64_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t64\n\t64\n )+128+vrshrq_n_s64+typed:signed-vec-shr_p64_s128_signed_1": [
        {
            "property_name": "EnumeratePatternarm_missing_ashr",
            "property": {
                "src": "(vrshrd_n_s64_dsl (lit (bv #x0000000000000000 64)) (lit (bv #x00000000000000000000000000000001 128)) (lit (bv #x00000000000000000000000000000001 128)) (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 128 128 0 128 64 -1 0 128 -1 0 -1 1)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 64 128)",
                "output_size": 128,
                "original_src_expr": " (vrshrd_n_s64_dsl ; vrshrd_n_s64\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 128)))\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t128\n\t-1\n\t0\n\t-1\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s64_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t64\n\t64\n )",
                "src_ctx": "vrshrq_n_s64",
                "dst_ctx": "typed:signed-vec-shr_p64_s128_signed_1"
            }
        }
    ],
    " (vrshr_n_s32_dsl ; vrshr_n_s32\n\t(lit (bv #x00000000 (bitvector 32)))\n\t(lit (bv #x0000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000001 (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n\t-1\n\t1\n\t64\n )+ (typed:signed-vec-shr ; typed:signed-vec-shr_p32_s64_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t32\n\t64\n )+64+vrshr_n_s32+typed:signed-vec-shr_p32_s64_signed_1": [
        {
            "property_name": "EnumeratePatternarm_missing_ashr",
            "property": {
                "src": "(vrshr_n_s32_dsl (lit (bv #x00000000 32)) (lit (bv #x0000000000000001 64)) (lit (bv #x0000000000000001 64)) (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 0 64 32 -1 -1 0 -1 1 64)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vrshr_n_s32_dsl ; vrshr_n_s32\n\t(lit (bv #x00000000 (bitvector 32)))\n\t(lit (bv #x0000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000001 (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n\t-1\n\t1\n\t64\n )",
                "original_dst_expr": " (typed:signed-vec-shr ; typed:signed-vec-shr_p32_s64_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t32\n\t64\n )",
                "src_ctx": "vrshr_n_s32",
                "dst_ctx": "typed:signed-vec-shr_p32_s64_signed_1"
            }
        }
    ],
    " (vrshr_n_s32_dsl ; vrshr_n_s32\n\t(lit (bv #x00000000 (bitvector 32)))\n\t(lit (bv #x0000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000001 (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n\t-1\n\t1\n\t64\n )+ (typed:signed-vec-shr ; typed:signed-vec-shr_p32_s64_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t32\n\t64\n )+128+vrshrq_n_s32+typed:signed-vec-shr_p32_s128_signed_1": [
        {
            "property_name": "EnumeratePatternarm_missing_ashr",
            "property": {
                "src": "(vrshr_n_s32_dsl (lit (bv #x00000000 32)) (lit (bv #x0000000000000001 64)) (lit (bv #x0000000000000001 64)) (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 128 128 0 128 32 -1 -1 0 -1 1 64)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vrshr_n_s32_dsl ; vrshr_n_s32\n\t(lit (bv #x00000000 (bitvector 32)))\n\t(lit (bv #x0000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000001 (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n\t-1\n\t1\n\t64\n )",
                "original_dst_expr": " (typed:signed-vec-shr ; typed:signed-vec-shr_p32_s64_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t32\n\t64\n )",
                "src_ctx": "vrshrq_n_s32",
                "dst_ctx": "typed:signed-vec-shr_p32_s128_signed_1"
            }
        }
    ]
}