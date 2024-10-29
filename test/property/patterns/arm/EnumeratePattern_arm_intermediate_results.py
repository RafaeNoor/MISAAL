{
    " (vadd_u16_dsl ; vadd_u8\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n )+ (typed:vec-add ; typed:vec-add_p8_s64_signed_None\n\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t64\n )+128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(vadd_u16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1)",
                "dst": "(typed:vec-add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (vadd_u16_dsl ; vadd_u8\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p8_s64_signed_None\n\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t64\n )"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u8\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n )+ (typed:vec-add ; typed:vec-add_p8_s64_signed_None\n\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t64\n )+64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 -1)",
                "dst": "(typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64)",
                "output_size": 64,
                "original_src_expr": " (vadd_u16_dsl ; vadd_u8\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p8_s64_signed_None\n\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t64\n )"
            }
        }
    ],
    " (vhsub_u16_dsl ; vhsub_u8\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:vec-sub ; typed:vec-sub_p8_s64_signed_None\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p64_s64_signed_0\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t )\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p8_s64_signed_0\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t8\n\t\t64\n\t )\n\t8\n\t64\n )+64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(vhsub_u16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 1 -1 0 16 0 16)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "output_size": 64,
                "original_src_expr": " (vhsub_u16_dsl ; vhsub_u8\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s64_signed_None\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p64_s64_signed_0\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t )\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p8_s64_signed_0\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t8\n\t\t64\n\t )\n\t8\n\t64\n )"
            }
        }
    ],
    " (vhsub_u16_dsl ; vhsub_u8\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t-1\n\t0\n\t16\n\t0\n\t16\n )+ (typed:vec-sub ; typed:vec-sub_p8_s64_signed_None\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p64_s64_signed_0\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t )\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p8_s64_signed_0\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t8\n\t\t64\n\t )\n\t8\n\t64\n )+128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(vhsub_u16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 -1 0 32 0 32)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) 16 128)",
                "output_size": 128,
                "original_src_expr": " (vhsub_u16_dsl ; vhsub_u8\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t-1\n\t0\n\t16\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s64_signed_None\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p64_s64_signed_0\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t )\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p8_s64_signed_0\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t8\n\t\t64\n\t )\n\t8\n\t64\n )"
            }
        }
    ],
    " (vqdmull_s16_dsl ; vqdmull_s16\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t32\n\t2\n\t1\n\t1\n )+ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s128_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s64_signed_1\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s64_signed_1\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t16\n\t\t64\n\t )\n\t32\n\t128\n )+32": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(vqdmull_s16_dsl (lit (bv #x00000002 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16 0 16 16 32 2 1 1)",
                "dst": "(typed:signed-vec-sat-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 32 32)",
                "output_size": 32,
                "original_src_expr": " (vqdmull_s16_dsl ; vqdmull_s16\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t32\n\t2\n\t1\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s128_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s64_signed_1\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s64_signed_1\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t16\n\t\t64\n\t )\n\t32\n\t128\n )"
            }
        }
    ],
    " (vqdmull_s16_dsl ; vqdmull_s16\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t32\n\t2\n\t1\n\t1\n )+ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s128_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s64_signed_1\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s64_signed_1\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t16\n\t\t64\n\t )\n\t32\n\t128\n )+128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(vqdmull_s16_dsl (lit (bv #x00000002 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 2 1 1)",
                "dst": "(typed:signed-vec-sat-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vqdmull_s16_dsl ; vqdmull_s16\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t32\n\t2\n\t1\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s128_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s64_signed_1\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s64_signed_1\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t16\n\t\t64\n\t )\n\t32\n\t128\n )"
            }
        }
    ],
    " (vqdmull_s16_dsl ; vqdmull_s16\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t32\n\t2\n\t1\n\t1\n )+ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s128_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s64_signed_1\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s64_signed_1\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t16\n\t\t64\n\t )\n\t32\n\t128\n )+64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(vqdmull_s16_dsl (lit (bv #x0000000000000002 64)) (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 2 1 1)",
                "dst": "(typed:signed-vec-sat-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 64 64)",
                "output_size": 64,
                "original_src_expr": " (vqdmull_s16_dsl ; vqdmull_s16\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t32\n\t2\n\t1\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s128_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s64_signed_1\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s64_signed_1\n\t\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t\t(buffer-index  1 'uint8 64) ; < 8 x i8> False\n\t\t16\n\t\t64\n\t )\n\t32\n\t128\n )"
            }
        }
    ]
}