{
    " (vmax_u8_dsl ; vmaxq_s8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t1\n )+ (typed:signed-vec-max ; typed:signed-vec-max_p8_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+64+vmax_s8+typed:signed-vec-max_p8_s64_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64)",
                "output_size": 64,
                "original_src_expr": " (vmax_u8_dsl ; vmaxq_s8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-max ; typed:signed-vec-max_p8_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vmax_s8",
                "dst_ctx": "typed:signed-vec-max_p8_s64_signed_1"
            }
        }
    ],
    " (vmax_u8_dsl ; vmaxq_s8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t1\n )+ (typed:signed-vec-max ; typed:signed-vec-max_p8_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+128+vmaxq_s8+typed:signed-vec-max_p8_s128_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 1)",
                "dst": "(typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (vmax_u8_dsl ; vmaxq_s8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-max ; typed:signed-vec-max_p8_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vmaxq_s8",
                "dst_ctx": "typed:signed-vec-max_p8_s128_signed_1"
            }
        }
    ],
    " (vmax_u8_dsl ; vmaxq_s8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t1\n )+ (typed:signed-vec-max ; typed:signed-vec-max_p8_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+64+vmax_s32+typed:signed-vec-max_p32_s64_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vmax_u8_dsl ; vmaxq_s8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-max ; typed:signed-vec-max_p8_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vmax_s32",
                "dst_ctx": "typed:signed-vec-max_p32_s64_signed_1"
            }
        }
    ],
    " (vmax_u8_dsl ; vmaxq_s8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t1\n )+ (typed:signed-vec-max ; typed:signed-vec-max_p8_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+64+vmax_s16+typed:signed-vec-max_p16_s64_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64)",
                "output_size": 64,
                "original_src_expr": " (vmax_u8_dsl ; vmaxq_s8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-max ; typed:signed-vec-max_p8_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vmax_s16",
                "dst_ctx": "typed:signed-vec-max_p16_s64_signed_1"
            }
        }
    ],
    " (vmax_u8_dsl ; vmaxq_s8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t1\n )+ (typed:signed-vec-max ; typed:signed-vec-max_p8_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+128+vmaxq_s16+typed:signed-vec-max_p16_s128_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1)",
                "dst": "(typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128)",
                "output_size": 128,
                "original_src_expr": " (vmax_u8_dsl ; vmaxq_s8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-max ; typed:signed-vec-max_p8_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vmaxq_s16",
                "dst_ctx": "typed:signed-vec-max_p16_s128_signed_1"
            }
        }
    ],
    " (vmax_u8_dsl ; vmaxq_s8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t1\n )+ (typed:signed-vec-max ; typed:signed-vec-max_p8_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+128+vmaxq_s32+typed:signed-vec-max_p32_s128_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 1)",
                "dst": "(typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vmax_u8_dsl ; vmaxq_s8\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-max ; typed:signed-vec-max_p8_s128_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "vmaxq_s32",
                "dst_ctx": "typed:signed-vec-max_p32_s128_signed_1"
            }
        }
    ],
    " (vmax_u8_dsl ; vmaxq_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )+ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+64+vmax_u8+typed:unsigned-vec-max_p8_s64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 0)",
                "dst": "(typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64)",
                "output_size": 64,
                "original_src_expr": " (vmax_u8_dsl ; vmaxq_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vmax_u8",
                "dst_ctx": "typed:unsigned-vec-max_p8_s64_signed_0"
            }
        }
    ],
    " (vmax_u8_dsl ; vmaxq_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )+ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+128+vmaxq_u16+typed:unsigned-vec-max_p16_s128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128)",
                "output_size": 128,
                "original_src_expr": " (vmax_u8_dsl ; vmaxq_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vmaxq_u16",
                "dst_ctx": "typed:unsigned-vec-max_p16_s128_signed_0"
            }
        }
    ],
    " (vmax_u8_dsl ; vmaxq_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )+ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+128+vmaxq_u8+typed:unsigned-vec-max_p8_s128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (vmax_u8_dsl ; vmaxq_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vmaxq_u8",
                "dst_ctx": "typed:unsigned-vec-max_p8_s128_signed_0"
            }
        }
    ],
    " (vmax_u8_dsl ; vmaxq_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )+ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+64+vmax_u16+typed:unsigned-vec-max_p16_s64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 0)",
                "dst": "(typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64)",
                "output_size": 64,
                "original_src_expr": " (vmax_u8_dsl ; vmaxq_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vmax_u16",
                "dst_ctx": "typed:unsigned-vec-max_p16_s64_signed_0"
            }
        }
    ],
    " (vmax_u8_dsl ; vmaxq_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )+ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+128+vmaxq_u32+typed:unsigned-vec-max_p32_s128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vmax_u8_dsl ; vmaxq_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vmaxq_u32",
                "dst_ctx": "typed:unsigned-vec-max_p32_s128_signed_0"
            }
        }
    ],
    " (vmax_u8_dsl ; vmaxq_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )+ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+64+vmax_u32+typed:unsigned-vec-max_p32_s64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 0 0)",
                "dst": "(typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vmax_u8_dsl ; vmaxq_u32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vmax_u32",
                "dst_ctx": "typed:unsigned-vec-max_p32_s64_signed_0"
            }
        }
    ],
    " (vmin_u32_dsl ; vminq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n )+ (typed:signed-vec-min ; typed:signed-vec-min_p32_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+128+vminq_s32+typed:signed-vec-min_p32_s128_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 1)",
                "dst": "(typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vmin_u32_dsl ; vminq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-min ; typed:signed-vec-min_p32_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vminq_s32",
                "dst_ctx": "typed:signed-vec-min_p32_s128_signed_1"
            }
        }
    ],
    " (vmin_u32_dsl ; vminq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n )+ (typed:signed-vec-min ; typed:signed-vec-min_p32_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+64+vmin_s8+typed:signed-vec-min_p8_s64_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)",
                "output_size": 64,
                "original_src_expr": " (vmin_u32_dsl ; vminq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-min ; typed:signed-vec-min_p32_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vmin_s8",
                "dst_ctx": "typed:signed-vec-min_p8_s64_signed_1"
            }
        }
    ],
    " (vmin_u32_dsl ; vminq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n )+ (typed:signed-vec-min ; typed:signed-vec-min_p32_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+128+vminq_s8+typed:signed-vec-min_p8_s128_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 1)",
                "dst": "(typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (vmin_u32_dsl ; vminq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-min ; typed:signed-vec-min_p32_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vminq_s8",
                "dst_ctx": "typed:signed-vec-min_p8_s128_signed_1"
            }
        }
    ],
    " (vmin_u32_dsl ; vminq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n )+ (typed:signed-vec-min ; typed:signed-vec-min_p32_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+128+vminq_s16+typed:signed-vec-min_p16_s128_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1)",
                "dst": "(typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128)",
                "output_size": 128,
                "original_src_expr": " (vmin_u32_dsl ; vminq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-min ; typed:signed-vec-min_p32_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vminq_s16",
                "dst_ctx": "typed:signed-vec-min_p16_s128_signed_1"
            }
        }
    ],
    " (vmin_u32_dsl ; vminq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n )+ (typed:signed-vec-min ; typed:signed-vec-min_p32_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+64+vmin_s16+typed:signed-vec-min_p16_s64_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64)",
                "output_size": 64,
                "original_src_expr": " (vmin_u32_dsl ; vminq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-min ; typed:signed-vec-min_p32_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vmin_s16",
                "dst_ctx": "typed:signed-vec-min_p16_s64_signed_1"
            }
        }
    ],
    " (vmin_u32_dsl ; vminq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n )+ (typed:signed-vec-min ; typed:signed-vec-min_p32_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+64+vmin_s32+typed:signed-vec-min_p32_s64_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vmin_u32_dsl ; vminq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n )",
                "original_dst_expr": " (typed:signed-vec-min ; typed:signed-vec-min_p32_s128_signed_1\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vmin_s32",
                "dst_ctx": "typed:signed-vec-min_p32_s64_signed_1"
            }
        }
    ],
    " (vmin_u32_dsl ; vminq_u16\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+64+vmin_u32+typed:unsigned-vec-min_p32_s64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vmin_u32_dsl ; vminq_u16\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vmin_u32",
                "dst_ctx": "typed:unsigned-vec-min_p32_s64_signed_0"
            }
        }
    ],
    " (vmin_u32_dsl ; vminq_u16\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+128+vminq_u8+typed:unsigned-vec-min_p8_s128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (vmin_u32_dsl ; vminq_u16\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vminq_u8",
                "dst_ctx": "typed:unsigned-vec-min_p8_s128_signed_0"
            }
        }
    ],
    " (vmin_u32_dsl ; vminq_u16\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+128+vminq_u16+typed:unsigned-vec-min_p16_s128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128)",
                "output_size": 128,
                "original_src_expr": " (vmin_u32_dsl ; vminq_u16\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vminq_u16",
                "dst_ctx": "typed:unsigned-vec-min_p16_s128_signed_0"
            }
        }
    ],
    " (vmin_u32_dsl ; vminq_u16\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+128+vminq_u32+typed:unsigned-vec-min_p32_s128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vmin_u32_dsl ; vminq_u16\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vminq_u32",
                "dst_ctx": "typed:unsigned-vec-min_p32_s128_signed_0"
            }
        }
    ],
    " (vmin_u32_dsl ; vminq_u16\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+64+vmin_u16+typed:unsigned-vec-min_p16_s64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64)",
                "output_size": 64,
                "original_src_expr": " (vmin_u32_dsl ; vminq_u16\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vmin_u16",
                "dst_ctx": "typed:unsigned-vec-min_p16_s64_signed_0"
            }
        }
    ],
    " (vmin_u32_dsl ; vminq_u16\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )+64+vmin_u8+typed:unsigned-vec-min_p8_s64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)",
                "output_size": 64,
                "original_src_expr": " (vmin_u32_dsl ; vminq_u16\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s128_signed_0\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t16\n\t128\n )",
                "src_ctx": "vmin_u8",
                "dst_ctx": "typed:unsigned-vec-min_p8_s64_signed_0"
            }
        }
    ]
}