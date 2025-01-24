{
    " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+64+vabd_u8+typed:unsigned-vec-absd_p8_s64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_absd",
            "property": {
                "src": "(vabdq_s32_dsl (lit (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)",
                "output_size": 64,
                "original_src_expr": " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vabd_u8",
                "dst_ctx": "typed:unsigned-vec-absd_p8_s64_signed_0"
            }
        }
    ],
    " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+128+vabdq_u8+typed:unsigned-vec-absd_p8_s128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_absd",
            "property": {
                "src": "(vabdq_s32_dsl (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vabdq_u8",
                "dst_ctx": "typed:unsigned-vec-absd_p8_s128_signed_0"
            }
        }
    ],
    " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )+64+vabd_u8+typed:unsigned-vec-absd_p16_s64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_absd",
            "property": {
                "src": "(vabdq_s32_dsl (lit (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "output_size": 64,
                "original_src_expr": " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )",
                "src_ctx": "vabd_u8",
                "dst_ctx": "typed:unsigned-vec-absd_p16_s64_signed_0"
            }
        }
    ],
    " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )+64+vabd_u8+typed:unsigned-vec-absd_p32_s64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_absd",
            "property": {
                "src": "(vabdq_s32_dsl (lit (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )",
                "src_ctx": "vabd_u8",
                "dst_ctx": "typed:unsigned-vec-absd_p32_s64_signed_0"
            }
        }
    ],
    " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )+64+vabd_u8+typed:unsigned-vec-absd_p64_s64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_absd",
            "property": {
                "src": "(vabdq_s32_dsl (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "output_size": 64,
                "original_src_expr": " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )",
                "src_ctx": "vabd_u8",
                "dst_ctx": "typed:unsigned-vec-absd_p64_s64_signed_0"
            }
        }
    ],
    " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )+64+vabd_u8+typed:unsigned-vec-absd_p8_s64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_absd",
            "property": {
                "src": "(vabdq_s32_dsl (lit (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "output_size": 64,
                "original_src_expr": " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )",
                "src_ctx": "vabd_u8",
                "dst_ctx": "typed:unsigned-vec-absd_p8_s64_signed_0"
            }
        }
    ],
    " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )+128+vabdq_u8+typed:unsigned-vec-absd_p16_s128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_absd",
            "property": {
                "src": "(vabdq_s32_dsl (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) 16 128)",
                "output_size": 128,
                "original_src_expr": " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )",
                "src_ctx": "vabdq_u8",
                "dst_ctx": "typed:unsigned-vec-absd_p16_s128_signed_0"
            }
        }
    ],
    " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )+128+vabdq_u8+typed:unsigned-vec-absd_p32_s128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_absd",
            "property": {
                "src": "(vabdq_s32_dsl (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )",
                "src_ctx": "vabdq_u8",
                "dst_ctx": "typed:unsigned-vec-absd_p32_s128_signed_0"
            }
        }
    ],
    " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )+128+vabdq_u8+typed:unsigned-vec-absd_p64_s128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_absd",
            "property": {
                "src": "(vabdq_s32_dsl (lit (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) 64 128)",
                "output_size": 128,
                "original_src_expr": " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )",
                "src_ctx": "vabdq_u8",
                "dst_ctx": "typed:unsigned-vec-absd_p64_s128_signed_0"
            }
        }
    ],
    " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )+128+vabdq_u8+typed:unsigned-vec-absd_p8_s128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_absd",
            "property": {
                "src": "(vabdq_s32_dsl (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) 8 128)",
                "output_size": 128,
                "original_src_expr": " (vabdq_s32_dsl ; vabdq_u8\n\t(lit (bv #x00 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s128_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t16\n\t128\n )",
                "src_ctx": "vabdq_u8",
                "dst_ctx": "typed:unsigned-vec-absd_p8_s128_signed_0"
            }
        }
    ],
    " (vaba_u8_dsl ; vabaq_u8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  2 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+64+vaba_u8+typed:vec-add_p8_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_absd",
            "property": {
                "src": "(vaba_u8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:vec-add (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x02 8)) 8 64) (reg (bv #x01 8)) 8 64)",
                "output_size": 64,
                "original_src_expr": " (vaba_u8_dsl ; vabaq_u8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  2 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vaba_u8",
                "dst_ctx": "typed:vec-add_p8_s64_signed_None"
            }
        }
    ],
    " (vaba_u8_dsl ; vabaq_u8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  2 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+128+vabaq_u8+typed:vec-add_p8_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_absd",
            "property": {
                "src": "(vaba_u8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:vec-add (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x02 8)) 8 128) (reg (bv #x01 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (vaba_u8_dsl ; vabaq_u8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p8_s128_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s128_signed_0\n\t\t(buffer-index  2 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vabaq_u8",
                "dst_ctx": "typed:vec-add_p8_s128_signed_None"
            }
        }
    ]
}
