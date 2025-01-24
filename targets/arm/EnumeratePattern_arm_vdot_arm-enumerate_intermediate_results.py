{
    " (vdotq_s32_dsl ; vdotq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n )+ (typed:vec-add ; typed:vec-add_p32_s128_signed_None\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s512_signed_None_reduce_4\n\t\t4\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is256_op32_os512_signed_1\n\t\t\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s128_signed_1\n\t\t\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t\t\t(buffer-index  2 'uint8 128) ; < 16 x i8> False\n\t\t\t\t8\n\t\t\t\t128\n\t\t\t )\n\t\t\t16\n\t\t\t1\n\t\t\t16\n\t\t\t32\n\t\t )\n\t\t32\n\t\t512\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+64+vdot_s32+typed:vec-add_p32_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_vdot",
            "property": {
                "src": "(vdotq_s32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 64 32 0 32 8 -1 1 1)",
                "dst": "(typed:vec-add (typed:signed-vector_reduce_add 4 (typed:cast-int-extend (typed:signed-vec-widen-mul (reg (bv #x02 8)) (reg (bv #x00 8)) 8 64) 16 1 8 32) 32 256) (reg (bv #x01 8)) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vdotq_s32_dsl ; vdotq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s128_signed_None\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s512_signed_None_reduce_4\n\t\t4\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is256_op32_os512_signed_1\n\t\t\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s128_signed_1\n\t\t\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t\t\t(buffer-index  2 'uint8 128) ; < 16 x i8> False\n\t\t\t\t8\n\t\t\t\t128\n\t\t\t )\n\t\t\t16\n\t\t\t1\n\t\t\t16\n\t\t\t32\n\t\t )\n\t\t32\n\t\t512\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vdot_s32",
                "dst_ctx": "typed:vec-add_p32_s64_signed_None"
            }
        }
    ],
    " (vdotq_s32_dsl ; vdotq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n )+ (typed:vec-add ; typed:vec-add_p32_s128_signed_None\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s512_signed_None_reduce_4\n\t\t4\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is256_op32_os512_signed_1\n\t\t\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s128_signed_1\n\t\t\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t\t\t(buffer-index  2 'uint8 128) ; < 16 x i8> False\n\t\t\t\t8\n\t\t\t\t128\n\t\t\t )\n\t\t\t16\n\t\t\t1\n\t\t\t16\n\t\t\t32\n\t\t )\n\t\t32\n\t\t512\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+128+vdotq_s32+typed:vec-add_p32_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_vdot",
            "property": {
                "src": "(vdotq_s32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 32 0 32 8 -1 1 1)",
                "dst": "(typed:vec-add (typed:signed-vector_reduce_add 4 (typed:cast-int-extend (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) 16 1 16 32) 32 512) (reg (bv #x02 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vdotq_s32_dsl ; vdotq_s32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s128_signed_None\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s512_signed_None_reduce_4\n\t\t4\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is256_op32_os512_signed_1\n\t\t\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s128_signed_1\n\t\t\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t\t\t(buffer-index  2 'uint8 128) ; < 16 x i8> False\n\t\t\t\t8\n\t\t\t\t128\n\t\t\t )\n\t\t\t16\n\t\t\t1\n\t\t\t16\n\t\t\t32\n\t\t )\n\t\t32\n\t\t512\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vdotq_s32",
                "dst_ctx": "typed:vec-add_p32_s128_signed_None"
            }
        }
    ],
    " (vdotq_s32_dsl ; vdotq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t0\n\t0\n )+ (typed:vec-add ; typed:vec-add_p32_s128_signed_None\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s512_signed_None_reduce_4\n\t\t4\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p8_s128_signed_0\n\t\t\t\t(buffer-index  2 'uint8 128) ; < 16 x i8> False\n\t\t\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t\t\t8\n\t\t\t\t128\n\t\t\t )\n\t\t\t16\n\t\t\t1\n\t\t\t16\n\t\t\t32\n\t\t )\n\t\t32\n\t\t512\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+128+vdotq_u32+typed:vec-add_p32_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_vdot",
            "property": {
                "src": "(vdotq_s32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 32 0 32 8 -1 0 0)",
                "dst": "(typed:vec-add (typed:signed-vector_reduce_add 4 (typed:cast-uint-extend (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x02 8)) 8 128) 16 1 16 32) 32 512) (reg (bv #x00 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (vdotq_s32_dsl ; vdotq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s128_signed_None\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s512_signed_None_reduce_4\n\t\t4\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p8_s128_signed_0\n\t\t\t\t(buffer-index  2 'uint8 128) ; < 16 x i8> False\n\t\t\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t\t\t8\n\t\t\t\t128\n\t\t\t )\n\t\t\t16\n\t\t\t1\n\t\t\t16\n\t\t\t32\n\t\t )\n\t\t32\n\t\t512\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vdotq_u32",
                "dst_ctx": "typed:vec-add_p32_s128_signed_None"
            }
        }
    ],
    " (vdotq_s32_dsl ; vdotq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t0\n\t0\n )+ (typed:vec-add ; typed:vec-add_p32_s128_signed_None\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s512_signed_None_reduce_4\n\t\t4\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p8_s128_signed_0\n\t\t\t\t(buffer-index  2 'uint8 128) ; < 16 x i8> False\n\t\t\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t\t\t8\n\t\t\t\t128\n\t\t\t )\n\t\t\t16\n\t\t\t1\n\t\t\t16\n\t\t\t32\n\t\t )\n\t\t32\n\t\t512\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )+64+vdot_u32+typed:vec-add_p32_s64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_vdot",
            "property": {
                "src": "(vdotq_s32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 64 32 0 32 8 -1 0 0)",
                "dst": "(typed:vec-add (typed:signed-vector_reduce_add 4 (typed:cast-uint-extend (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x02 8)) 8 64) 16 1 8 32) 32 256) (reg (bv #x01 8)) 32 64)",
                "output_size": 64,
                "original_src_expr": " (vdotq_s32_dsl ; vdotq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s128_signed_None\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s512_signed_None_reduce_4\n\t\t4\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p8_s128_signed_0\n\t\t\t\t(buffer-index  2 'uint8 128) ; < 16 x i8> False\n\t\t\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t\t\t8\n\t\t\t\t128\n\t\t\t )\n\t\t\t16\n\t\t\t1\n\t\t\t16\n\t\t\t32\n\t\t )\n\t\t32\n\t\t512\n\t )\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t32\n\t128\n )",
                "src_ctx": "vdot_u32",
                "dst_ctx": "typed:vec-add_p32_s64_signed_None"
            }
        }
    ]
}