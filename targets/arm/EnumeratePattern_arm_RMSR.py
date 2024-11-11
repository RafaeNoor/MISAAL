{
    " (vqrdmulh_s32_dsl ; vqrdmulhq_s32\n\t(lit (bv #x00000000000000000000000040000000 (bitvector 128)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n\t64\n\t-1\n\t1\n\t128\n\t1\n )+ (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p32_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t\t(lit (bv #x0000001f (bitvector 32)))\n\t\t32\n\t\t32\n\t\t4\n\t )\n\t32\n\t128\n )": [
        {
            "property_name": "EnumeratePattern_arm_RMSR",
            "property": {
                "src": " (vqrdmulh_s32_dsl ; vqrdmulhq_s32\n\t(lit (bv #x00000000000000000000000040000000 (bitvector 128)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n\t64\n\t-1\n\t1\n\t128\n\t1\n )",
                "dst": " (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p32_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t\t(lit (bv #x0000001f (bitvector 32)))\n\t\t32\n\t\t32\n\t\t4\n\t )\n\t32\n\t128\n )",
                "src_ctx": "vqrdmulhq_s32",
                "dst_ctx": "typed:signed-vec-rounding_mul_shift_right_p32_s128_signed_1",
                "output_size": 128
            }
        }
    ],
    " (vqrdmulhq_s16_dsl ; vqrdmulhq_s16\n\t(lit (bv #x0000000000004000 (bitvector 64)))\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t1\n\t32\n\t-1\n\t1\n\t64\n\t1\n )+ (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p16_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(lit (bv #x000f (bitvector 16)))\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t16\n\t128\n )": [
        {
            "property_name": "EnumeratePattern_arm_RMSR",
            "property": {
                "src": " (vqrdmulhq_s16_dsl ; vqrdmulhq_s16\n\t(lit (bv #x0000000000004000 (bitvector 64)))\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t1\n\t32\n\t-1\n\t1\n\t64\n\t1\n )",
                "dst": " (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p16_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(lit (bv #x000f (bitvector 16)))\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t16\n\t128\n )",
                "src_ctx": "vqrdmulhq_s16",
                "dst_ctx": "typed:signed-vec-rounding_mul_shift_right_p16_s128_signed_1",
                "output_size": 128
            }
        }
    ],
    " (vqrdmulhq_s16_dsl ; vqrdmulh_s16\n\t(lit (bv #x0000000000004000 (bitvector 64)))\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t1\n\t32\n\t-1\n\t1\n\t64\n\t1\n )+ (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p16_s64_signed_1\n\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(lit (bv #x000f (bitvector 16)))\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t16\n\t64\n )": [
        {
            "property_name": "EnumeratePattern_arm_RMSR",
            "property": {
                "src": " (vqrdmulhq_s16_dsl ; vqrdmulh_s16\n\t(lit (bv #x0000000000004000 (bitvector 64)))\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t1\n\t32\n\t-1\n\t1\n\t64\n\t1\n )",
                "dst": " (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p16_s64_signed_1\n\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t\t(lit (bv #x000f (bitvector 16)))\n\t\t16\n\t\t16\n\t\t4\n\t )\n\t16\n\t64\n )",
                "src_ctx": "vqrdmulh_s16",
                "dst_ctx": "typed:signed-vec-rounding_mul_shift_right_p16_s64_signed_1",
                "output_size": 64
            }
        }
    ],
    " (vqrdmulhq_s16_dsl ; vqrdmulhh_s16\n\t(lit (bv #x0000000000004000 (bitvector 64)))\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t16\n\t16\n\t0\n\t1\n\t32\n\t-1\n\t1\n\t64\n\t1\n )+ (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p16_s16_signed_1\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t(lit (bv #x000f (bitvector 16)))\n\t16\n\t16\n )": [
        {
            "property_name": "EnumeratePattern_arm_RMSR",
            "property": {
                "src": " (vqrdmulhq_s16_dsl ; vqrdmulhh_s16\n\t(lit (bv #x0000000000004000 (bitvector 64)))\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t16\n\t16\n\t0\n\t1\n\t32\n\t-1\n\t1\n\t64\n\t1\n )",
                "dst": " (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p16_s16_signed_1\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t(buffer-index  1 'uint8 16) ; < 2 x i8> False\n\t(lit (bv #x000f (bitvector 16)))\n\t16\n\t16\n )",
                "src_ctx": "vqrdmulhh_s16",
                "dst_ctx": "typed:signed-vec-rounding_mul_shift_right_p16_s16_signed_1",
                "output_size": 16
            }
        }
    ],
    " (vqrdmulh_s32_dsl ; vqrdmulh_s32\n\t(lit (bv #x00000000000000000000000040000000 (bitvector 128)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t1\n\t64\n\t-1\n\t1\n\t128\n\t1\n )+ (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p32_s64_signed_1\n\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t\t(lit (bv #x0000001f (bitvector 32)))\n\t\t32\n\t\t32\n\t\t2\n\t )\n\t32\n\t64\n )": [
        {
            "property_name": "EnumeratePattern_arm_RMSR",
            "property": {
                "src": " (vqrdmulh_s32_dsl ; vqrdmulh_s32\n\t(lit (bv #x00000000000000000000000040000000 (bitvector 128)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t1\n\t64\n\t-1\n\t1\n\t128\n\t1\n )",
                "dst": " (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p32_s64_signed_1\n\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t\t(lit (bv #x0000001f (bitvector 32)))\n\t\t32\n\t\t32\n\t\t2\n\t )\n\t32\n\t64\n )",
                "src_ctx": "vqrdmulh_s32",
                "dst_ctx": "typed:signed-vec-rounding_mul_shift_right_p32_s64_signed_1",
                "output_size": 64
            }
        }
    ],
    " (vqrdmulh_s32_dsl ; vqrdmulhs_s32\n\t(lit (bv #x00000000000000000000000040000000 (bitvector 128)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t1\n\t64\n\t-1\n\t1\n\t128\n\t1\n )+ (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p32_s32_signed_1\n\t(buffer-index  1 'uint8 32) ; < 4 x i8> False\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t(lit (bv #x0000001f (bitvector 32)))\n\t32\n\t32\n )": [
        {
            "property_name": "EnumeratePattern_arm_RMSR",
            "property": {
                "src": " (vqrdmulh_s32_dsl ; vqrdmulhs_s32\n\t(lit (bv #x00000000000000000000000040000000 (bitvector 128)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t1\n\t64\n\t-1\n\t1\n\t128\n\t1\n )",
                "dst": " (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p32_s32_signed_1\n\t(buffer-index  1 'uint8 32) ; < 4 x i8> False\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t(lit (bv #x0000001f (bitvector 32)))\n\t32\n\t32\n )",
                "src_ctx": "vqrdmulhs_s32",
                "dst_ctx": "typed:signed-vec-rounding_mul_shift_right_p32_s32_signed_1",
                "output_size": 32
            }
        }
    ]
}
