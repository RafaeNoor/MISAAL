{
    " (vmvn_s16_dsl ; vmvn_s16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n )_ (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmvn_s16_dsl (reg (bv #x00 8)) 64 64 0 64 8)",
                "dst": "(typed:vec-bwnot (reg (bv #x00 8)) 8 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 -1)",
                "dst": "(typed:vec-add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0)",
                "dst": "(typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 1)",
                "dst": "(typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64)"
            }
        }
    ],
    " (vqmovn_u64_dsl ; vqmovn_u64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t128\n\t64\n\t2\n )_ (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1\n\t64\n\t8\n\t#f\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vqmovn_u64_dsl (reg (bv #x00 8)) 64 64 0 64 8 1 1 32 16 2)",
                "dst": "(typed:vec-saturate (reg (bv #x00 8)) 16 1 8 8 #t)"
            }
        }
    ],
    " (vhadd_s32_dsl ; vhadd_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vhadd_s32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 1 -1 0 32 0 32)",
                "dst": "(typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64)"
            }
        }
    ],
    " (vshl_s8_dsl ; vshl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t1\n\t16\n\t1\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 0 32 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64)"
            }
        }
    ],
    " (vrhadd_s16_dsl ; vrhadd_s16\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t-1\n\t-1\n\t1\n\t32\n\t1\n\t32\n )_ (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrhadd_s16_dsl (lit (bv #x00000001 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 1 -1 -1 0 32 0 32)",
                "dst": "(typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64)"
            }
        }
    ],
    " (vrshld_s64_dsl ; vrshld_s64\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t-1\n\t1\n\t128\n\t-1\n\t1\n\t128\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrshld_s64_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 -1 0 16 -1 1 16)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32)",
                "dst": "(typed:cast-uint (reg (bv #x00 8)) 16 1 4 32)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16)",
                "dst": "(typed:cast-int (reg (bv #x00 8)) 8 1 8 16)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1)",
                "dst": "(typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 1)",
                "dst": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0 16 0)",
                "dst": "(typed:unsigned-vec-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0 16 0)",
                "dst": "(typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64)"
            }
        }
    ],
    " (vhadd_s32_dsl ; vhadd_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vhadd_s32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 1 -1 0 64 0 64)",
                "dst": "(typed:vec-add (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x0000000000000000 64)) 8 64)"
            }
        }
    ],
    " (vhadd_s32_dsl ; vhadd_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vhadd_s32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 1 -1 0 64 0 64)",
                "dst": "(typed:unsigned-vec-halving_add (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x00 8)) 32 64)"
            }
        }
    ],
    " (vhadd_s32_dsl ; vhadd_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vhadd_s32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 1 -1 0 64 0 64)",
                "dst": "(typed:unsigned-vec-halving_add (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)"
            }
        }
    ],
    " (vhadd_s32_dsl ; vhadd_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vhadd_s32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 -1 0 16 0 16)",
                "dst": "(typed:signed-vec-sat-add (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x0000000000000000 64)) 8 64)"
            }
        }
    ],
    " (vshl_s8_dsl ; vshl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t1\n\t16\n\t1\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p16_s1024_signed_None_reduce_2\n\t\t2\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 1 64 1)",
                "dst": "(typed:vec-shl (typed:vec-shl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x0000000000000000 64)) 8 64)"
            }
        }
    ],
    " (vshl_s8_dsl ; vshl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t1\n\t16\n\t1\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 0 16 1)",
                "dst": "(typed:vec-shl (typed:vec-shl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x0000000000000000 64)) 64 64)"
            }
        }
    ],
    " (vshl_s8_dsl ; vshl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t1\n\t16\n\t1\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 0 64 1)",
                "dst": "(typed:vec-shl (typed:vec-shl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)"
            }
        }
    ],
    " (vshl_s8_dsl ; vshl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t1\n\t16\n\t1\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p16_s1024_signed_None_reduce_2\n\t\t2\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 1 16 1)",
                "dst": "(typed:signed-vec-shr (typed:vec-shl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x0000000000000000 64)) 32 64)"
            }
        }
    ],
    " (vshl_s8_dsl ; vshl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t1\n\t16\n\t1\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 1 16 1)",
                "dst": "(typed:signed-vec-shr (typed:vec-shl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x0000000000000000 64)) 16 64)"
            }
        }
    ],
    " (vshl_s8_dsl ; vshl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t1\n\t16\n\t1\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 0 0 128 1)",
                "dst": "(typed:signed-vec-shr (typed:vec-shl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)"
            }
        }
    ],
    " (vhsub_u16_dsl ; vhsub_u16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t-1\n\t0\n\t32\n\t0\n\t32\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vhsub_u16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 1 -1 0 64 0 64)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 32 64)"
            }
        }
    ],
    " (vhsub_u16_dsl ; vhsub_u16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t-1\n\t0\n\t32\n\t0\n\t32\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vhsub_u16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 1 -1 0 16 0 16)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (reg (bv #x01 8)) 8 64)"
            }
        }
    ],
    " (vhsub_u16_dsl ; vhsub_u16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t-1\n\t0\n\t32\n\t0\n\t32\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vhsub_u16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 -1 0 16 0 16)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)"
            }
        }
    ],
    " (vhsub_u16_dsl ; vhsub_u16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t-1\n\t0\n\t32\n\t0\n\t32\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vhsub_u16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 -1 0 16 0 16)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 8 64)"
            }
        }
    ],
    " (vrhadd_s16_dsl ; vrhadd_s16\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t-1\n\t-1\n\t1\n\t32\n\t1\n\t32\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrhadd_s16_dsl (lit (bv #x0001 16)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 -1 -1 0 16 0 16)",
                "dst": "(typed:vec-add (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x0000000000000000 64)) 16 64)"
            }
        }
    ],
    " (vrhadd_s16_dsl ; vrhadd_s16\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t-1\n\t-1\n\t1\n\t32\n\t1\n\t32\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrhadd_s16_dsl (lit (bv #x0000000000000001 64)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 1 -1 -1 0 64 0 64)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x0000000000000000 64)) 8 64)"
            }
        }
    ],
    " (vrhadd_s16_dsl ; vrhadd_s16\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t-1\n\t-1\n\t1\n\t32\n\t1\n\t32\n )_ (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrhadd_s16_dsl (lit (bv #x0000000000000001 64)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 1 -1 -1 0 64 0 64)",
                "dst": "(typed:unsigned-vec-rounding_halving_add (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 32 64)"
            }
        }
    ],
    " (vrhadd_s16_dsl ; vrhadd_s16\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t-1\n\t-1\n\t1\n\t32\n\t1\n\t32\n )_ (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrhadd_s16_dsl (lit (bv #x0001 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 1 -1 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-rounding_halving_add (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 64 64)"
            }
        }
    ],
    " (vrhadd_s16_dsl ; vrhadd_s16\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t-1\n\t-1\n\t1\n\t32\n\t1\n\t32\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrhadd_s16_dsl (lit (bv #x0001 16)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 -1 -1 0 16 0 16)",
                "dst": "(typed:signed-vec-sat-add (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x0000000000000000 64)) 64 64)"
            }
        }
    ],
    " (vaddw_u8_dsl ; vaddw_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t-1\n\t0\n\t32\n\t0\n\t32\n\t2\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vaddw_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 -1 0 64 0 64 2)",
                "dst": "(typed:vec-add (typed:cast-uint (reg (bv #x01 8)) 16 1 4 32) (reg (bv #x00 8)) 32 128)"
            }
        }
    ],
    " (vaddw_u8_dsl ; vaddw_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t-1\n\t0\n\t32\n\t0\n\t32\n\t2\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vaddw_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 -1 1 32 1 32 2)",
                "dst": "(typed:vec-add (typed:cast-int (reg (bv #x01 8)) 8 1 8 16) (reg (bv #x00 8)) 16 128)"
            }
        }
    ],
    " (vrshld_s64_dsl ; vrshld_s64\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t-1\n\t1\n\t128\n\t-1\n\t1\n\t128\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrshld_s64_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 -1 0 16 -1 1 16)",
                "dst": "(typed:vec-shl (typed:vec-shl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x0000000000000000 64)) 16 64)"
            }
        }
    ],
    " (vrshld_s64_dsl ; vrshld_s64\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t-1\n\t1\n\t128\n\t-1\n\t1\n\t128\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p16_s1024_signed_None_reduce_2\n\t\t2\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrshld_s64_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 -1 1 16 -1 1 16)",
                "dst": "(typed:vec-shl (typed:vec-shl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x0000000000000000 64)) 8 64)"
            }
        }
    ],
    " (vrshld_s64_dsl ; vrshld_s64\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t-1\n\t1\n\t128\n\t-1\n\t1\n\t128\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrshld_s64_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 -1 1 16 -1 1 16)",
                "dst": "(typed:vec-shl (typed:vec-shl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)"
            }
        }
    ],
    " (vrshld_s64_dsl ; vrshld_s64\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t-1\n\t1\n\t128\n\t-1\n\t1\n\t128\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrshld_s64_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 -1 1 16 -1 1 16)",
                "dst": "(typed:vec-shl (typed:vec-shl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x0000000000000000 64)) 8 64)"
            }
        }
    ],
    " (vrshld_s64_dsl ; vrshld_s64\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t-1\n\t1\n\t128\n\t-1\n\t1\n\t128\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrshld_s64_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 -1 1 16 -1 1 16)",
                "dst": "(typed:signed-vec-shr (typed:vec-shl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x0000000000000000 64)) 8 64)"
            }
        }
    ],
    " (vrshld_s64_dsl ; vrshld_s64\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t-1\n\t1\n\t128\n\t-1\n\t1\n\t128\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p16_s1024_signed_None_reduce_2\n\t\t2\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrshld_s64_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 -1 0 16 -1 1 16)",
                "dst": "(typed:signed-vec-shr (typed:vec-shl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x0000000000000000 64)) 64 64)"
            }
        }
    ],
    " (vrshld_s64_dsl ; vrshld_s64\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t-1\n\t1\n\t128\n\t-1\n\t1\n\t128\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrshld_s64_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 -1 0 16 -1 1 16)",
                "dst": "(typed:signed-vec-shr (typed:vec-shl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)"
            }
        }
    ],
    " (vrshld_s64_dsl ; vrshld_s64\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t-1\n\t1\n\t128\n\t-1\n\t1\n\t128\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrshld_s64_dsl (lit (bv #x00000001 32)) (lit (bv #x00000001 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 -1 1 32 -1 1 32)",
                "dst": "(typed:signed-vec-shr (typed:vec-shl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x0000000000000000 64)) 32 64)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64)",
                "dst": "(typed:vec-sub (typed:cast-uint (reg (bv #x00 8)) 32 1 2 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16)",
                "dst": "(typed:vec-sub (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16)",
                "dst": "(typed:vec-sub (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64)",
                "dst": "(typed:vec-sub (typed:cast-uint (reg (bv #x00 8)) 32 1 2 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32)",
                "dst": "(typed:vec-sub (typed:cast-uint (reg (bv #x00 8)) 16 1 4 32) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32)",
                "dst": "(typed:vec-sub (typed:cast-int (reg (bv #x00 8)) 16 1 4 32) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16)",
                "dst": "(typed:vec-sub (typed:cast-int (reg (bv #x00 8)) 8 1 8 16) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32)",
                "dst": "(typed:vec-sub (typed:cast-int (reg (bv #x00 8)) 16 1 4 32) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32)",
                "dst": "(typed:vec-sub (typed:cast-int (reg (bv #x00 8)) 16 1 4 32) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64)",
                "dst": "(typed:vec-sub (typed:cast-int (reg (bv #x00 8)) 32 1 2 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) 64 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-int (reg (bv #x00 8)) 16 1 4 32) 8 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-uint (reg (bv #x00 8)) 32 1 2 64) 64 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-int (reg (bv #x00 8)) 8 1 8 16) 16 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) 8 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-int (reg (bv #x00 8)) 8 1 8 16) 32 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-uint (reg (bv #x00 8)) 16 1 4 32) 16 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-int (reg (bv #x00 8)) 16 1 4 32) 32 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-int (reg (bv #x00 8)) 16 1 4 32) 32 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-uint (reg (bv #x00 8)) 16 1 4 32) 16 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16)",
                "dst": "(typed:signed-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) 8 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16)",
                "dst": "(typed:signed-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-int (reg (bv #x00 8)) 8 1 8 16) 8 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64)",
                "dst": "(typed:signed-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-uint (reg (bv #x00 8)) 32 1 2 64) 64 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16)",
                "dst": "(typed:signed-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-int (reg (bv #x00 8)) 8 1 8 16) 32 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16)",
                "dst": "(typed:signed-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) 16 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16)",
                "dst": "(typed:signed-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-int (reg (bv #x00 8)) 8 1 8 16) 64 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16)",
                "dst": "(typed:signed-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) 32 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16)",
                "dst": "(typed:signed-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-int (reg (bv #x00 8)) 8 1 8 16) 32 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64)",
                "dst": "(typed:signed-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-uint (reg (bv #x00 8)) 32 1 2 64) 32 128)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64)",
                "dst": "(typed:signed-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:cast-int (reg (bv #x00 8)) 32 1 2 64) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 -1)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 -1)",
                "dst": "(typed:vec-sub (typed:vec-bwnot (reg (bv #x01 8)) 8 128) (typed:vec-bwnot (reg (bv #x00 8)) 32 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 -1)",
                "dst": "(typed:vec-sub (typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:vec-add (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) (reg (bv #x00 8)) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) (reg (bv #x00 8)) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1)",
                "dst": "(typed:vec-add (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 1)",
                "dst": "(typed:vec-add (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1)",
                "dst": "(typed:vec-add (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 -1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-bwnot (reg (bv #x00 8)) 32 128) (typed:vec-bwnot (reg (bv #x01 8)) 64 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 -1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) (reg (bv #x01 8)) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) (reg (bv #x01 8)) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1)",
                "dst": "(typed:unsigned-vec-min (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) (reg (bv #x00 8)) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) (typed:vec-bwnot (reg (bv #x01 8)) 16 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1)",
                "dst": "(typed:unsigned-vec-min (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 -1)",
                "dst": "(typed:unsigned-vec-max (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 1)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 -1)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 -1)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-bwnot (reg (bv #x00 8)) 64 128) (typed:vec-bwnot (reg (bv #x01 8)) 8 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) (reg (bv #x01 8)) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) (reg (bv #x00 8)) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 -1)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) 8 128)"
            }
        }
    ],
    " (vqdmull_s16_dsl ; vqdmull_s16\n\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t32\n\t2\n\t1\n\t1\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vqdmull_s16_dsl (lit (bv #x00000002 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 2 1 1)",
                "dst": "(typed:signed-vec-sat-add (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 32 128)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 8 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 8 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (reg (bv #x00 8)) 32 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 16 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:vec-add (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 16 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:vec-add (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 8 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 16 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (reg (bv #x00 8)) 32 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 8 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 32 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:unsigned-vec-mod (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:unsigned-vec-mod (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 8 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:signed-vec-max (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x00 8)) 8 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:signed-vec-max (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:unsigned-vec-mod (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 8 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 64 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x0000000000000000 64)) 8 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x0000000000000000 64)) 64 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 16 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 8 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x0000000000000000 64)) 64 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x0000000000000000 64)) 64 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:unsigned-vec-absd (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 32 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (reg (bv #x01 8)) 16 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 16 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 16 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x0000000000000000 64)) 64 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x0000000000000000 64)) 64 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x0000000000000000 64)) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 64 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x0000000000000000 64)) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 16 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (reg (bv #x00 8)) 32 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 1)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 16 64)"
            }
        }
    ],
    " (vsubl_s8_dsl ; vsubl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t-1\n\t1\n\t16\n\t1\n\t16\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubl_s8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 -1 0 32 0 32)",
                "dst": "(typed:vec-sub (typed:cast-uint (reg (bv #x00 8)) 16 1 4 32) (typed:cast-uint (reg (bv #x01 8)) 16 1 4 32) 32 128)"
            }
        }
    ],
    " (vsubl_s8_dsl ; vsubl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t-1\n\t1\n\t16\n\t1\n\t16\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubl_s8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 -1 1 32 1 32)",
                "dst": "(typed:vec-sub (typed:cast-int (reg (bv #x00 8)) 16 1 4 32) (typed:cast-int (reg (bv #x01 8)) 16 1 4 32) 32 128)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 8 64)"
            }
        }
    ],
    " (vsubl_s8_dsl ; vsubl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t-1\n\t1\n\t16\n\t1\n\t16\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubl_s8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 -1 0 16 0 16)",
                "dst": "(typed:signed-vec-sat-sub (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) (typed:cast-uint (reg (bv #x01 8)) 8 1 8 16) 16 128)"
            }
        }
    ],
    " (vsubl_s8_dsl ; vsubl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t-1\n\t1\n\t16\n\t1\n\t16\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubl_s8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 -1 1 32 1 32)",
                "dst": "(typed:signed-vec-sat-sub (typed:cast-int (reg (bv #x01 8)) 16 1 4 32) (typed:cast-int (reg (bv #x00 8)) 16 1 4 32) 32 128)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 0 0 64 0)",
                "dst": "(typed:cast-uint (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 64 1 2 32)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 0 0 64 0)",
                "dst": "(typed:cast-int (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 64 1 2 32)"
            }
        }
    ],
    " (vaddl_s32_dsl ; vaddl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vaddl_s32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 -1 0 32 0 32)",
                "dst": "(typed:vec-add (typed:cast-uint (reg (bv #x01 8)) 16 1 4 32) (typed:cast-uint (reg (bv #x00 8)) 16 1 4 32) 64 128)"
            }
        }
    ],
    " (vaddl_s32_dsl ; vaddl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vaddl_s32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 -1 1 32 1 32)",
                "dst": "(typed:vec-add (typed:cast-int (reg (bv #x01 8)) 16 1 4 32) (typed:cast-int (reg (bv #x00 8)) 16 1 4 32) 32 128)"
            }
        }
    ],
    " (vaddl_s32_dsl ; vaddl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vaddl_s32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 -1 0 64 0 64)",
                "dst": "(typed:signed-vec-sat-add (typed:cast-uint (reg (bv #x00 8)) 32 1 2 64) (typed:cast-uint (reg (bv #x01 8)) 32 1 2 64) 64 128)"
            }
        }
    ],
    " (vaddl_s32_dsl ; vaddl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vaddl_s32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 -1 1 16 1 16)",
                "dst": "(typed:signed-vec-sat-add (typed:cast-int (reg (bv #x01 8)) 8 1 8 16) (typed:cast-int (reg (bv #x00 8)) 8 1 8 16) 16 128)"
            }
        }
    ],
    " (vmull_high_s16_dsl ; vmull_high_s16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n\t32\n\t16\n\t1\n\t2\n )_ (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_high_s16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 32 16 0 2)",
                "dst": "(typed:unsigned-vec-widen-mul (typed:slice_vectors (reg (bv #x01 8)) 4 1 4 16 128) (typed:slice_vectors (reg (bv #x00 8)) 1 1 1 64 128) 16 64)"
            }
        }
    ],
    " (vmull_high_s16_dsl ; vmull_high_s16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n\t32\n\t16\n\t1\n\t2\n )_ (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t0\n\t1\n\t32\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_high_s16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0 16 8 0 2)",
                "dst": "(typed:slice_vectors (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) 2 1 2 64 256)"
            }
        }
    ],
    " (vmull_high_s16_dsl ; vmull_high_s16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n\t32\n\t16\n\t1\n\t2\n )_ (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t0\n\t1\n\t32\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_high_s16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 1 32 16 1 2)",
                "dst": "(typed:slice_vectors (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) 8 1 8 16 256)"
            }
        }
    ],
    " (vmull_high_s16_dsl ; vmull_high_s16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t1\n\t32\n\t16\n\t1\n\t2\n )_ (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_high_s16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 1 64 32 1 2)",
                "dst": "(typed:signed-vec-widen-mul (typed:slice_vectors (reg (bv #x01 8)) 2 1 2 32 128) (typed:slice_vectors (reg (bv #x00 8)) 2 1 2 32 128) 32 64)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:vec-sub (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:vec-add (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:unsigned-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-sat-add (lit (bv #x00000000000000000000000000000000 128)) (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-rounding_mul_shift_right (typed:cast-uint (reg (bv #x01 8)) 32 1 2 64) (typed:cast-uint (reg (bv #x00 8)) 32 1 2 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-rounding_mul_shift_right (typed:cast-uint (reg (bv #x01 8)) 8 1 8 16) (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:unsigned-vec-rounding_mul_shift_right (typed:cast-uint (reg (bv #x01 8)) 16 1 4 32) (typed:cast-uint (reg (bv #x00 8)) 16 1 4 32) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-rounding_mul_shift_right (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) (typed:cast-uint (reg (bv #x01 8)) 8 1 8 16) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-rounding_mul_shift_right (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) (typed:cast-uint (reg (bv #x01 8)) 8 1 8 16) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-rounding_mul_shift_right (typed:cast-uint (reg (bv #x00 8)) 32 1 2 64) (typed:cast-uint (reg (bv #x01 8)) 32 1 2 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-rounding_mul_shift_right (typed:cast-uint (reg (bv #x00 8)) 32 1 2 64) (typed:cast-uint (reg (bv #x01 8)) 32 1 2 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-rounding_mul_shift_right (typed:cast-uint (reg (bv #x01 8)) 32 1 2 64) (typed:cast-uint (reg (bv #x00 8)) 32 1 2 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-rounding_mul_shift_right (typed:cast-uint (reg (bv #x01 8)) 8 1 8 16) (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-rounding_mul_shift_right (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) (typed:cast-uint (reg (bv #x01 8)) 8 1 8 16) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-mul (typed:cast-uint (reg (bv #x00 8)) 8 1 8 16) (typed:cast-uint (reg (bv #x01 8)) 8 1 8 16) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-mul (typed:cast-int (reg (bv #x00 8)) 32 1 2 64) (typed:cast-int (reg (bv #x01 8)) 32 1 2 64) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:unsigned-vec-absd (lit (bv #x00000000000000000000000000000000 128)) (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:signed-vec-shr (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 0 16 0)",
                "dst": "(typed:signed-vec-shr (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:signed-vec-shr (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:signed-vec-shr (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:signed-vec-shr (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:signed-vec-shr (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:signed-vec-shr (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:signed-vec-shr (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:signed-vec-shr (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 0 64 0)",
                "dst": "(typed:signed-vec-shr (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:signed-vec-shr (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:signed-vec-shr (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:signed-vec-shr (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:signed-vec-shr (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 64 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 64 0 2 1 64 1)",
                "dst": "(typed:signed-vec-shr (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:signed-vec-shr (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 8 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:signed-vec-shr (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:signed-vec-shr (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:signed-vec-shr (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:signed-vec-shr (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (lit (bv #x00000000000000000000000000000000 128)) 16 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32 0)",
                "dst": "(typed:signed-vec-mul (typed:cast-uint (reg (bv #x00 8)) 16 1 4 32) (typed:cast-uint (reg (bv #x01 8)) 16 1 4 32) 32 128)"
            }
        }
    ],
    " (vmull_u32_dsl ; vmull_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmull_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16 1)",
                "dst": "(typed:signed-vec-mul (typed:cast-int (reg (bv #x00 8)) 8 1 8 16) (typed:cast-int (reg (bv #x01 8)) 8 1 8 16) 16 128)"
            }
        }
    ],
    " (vnegq_s64_dsl ; vnegq_s64\n\t (vnegq_s64_dsl ; vnegq_s64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t64\n\t\t0\n\t\t1\n\t\t128\n\t )\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t1\n\t128\n )_Reg": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vnegq_s64_dsl (vnegq_s64_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 1 128) 128 128 0 128 64 0 1 128)",
                "dst": "(reg (bv #x00 8))"
            }
        }
    ],
    " (vmvn_s16_dsl ; vmvn_s16\n\t (vmvn_s16_dsl ; vmvn_s16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n )_Reg": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmvn_s16_dsl (vmvn_s16_dsl (reg (bv #x00 8)) 64 64 0 64 8) 64 64 0 64 8)",
                "dst": "(reg (bv #x00 8))"
            }
        }
    ],
    " (vmvn_s16_dsl ; vmvn_s16\n\t (vmvn_s16_dsl ; vmvn_s16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n )_ (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmvn_s16_dsl (vmvn_s16_dsl (reg (bv #x00 8)) 64 64 0 64 8) 64 64 0 64 8)",
                "dst": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 8 64) 8 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 0) (reg (bv #x02 8)) 64 64 0 64 64 -1)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (reg (bv #x02 8)) 64 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 32 0) (reg (bv #x01 8)) 64 64 0 64 8 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x02 8)) (reg (bv #x00 8)) 32 64) (reg (bv #x01 8)) 8 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 8 1) (reg (bv #x00 8)) 64 64 0 64 32 -1)",
                "dst": "(typed:vec-add (typed:signed-vec-sat-add (reg (bv #x02 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 32 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 16 -1) (reg (bv #x00 8)) 64 64 0 64 32 -1)",
                "dst": "(typed:vec-add (typed:vec-add (reg (bv #x02 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x00 8)) 32 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1) (reg (bv #x02 8)) 64 64 0 64 32 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:vec-add (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x02 8)) 32 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0) (reg (bv #x02 8)) 64 64 0 64 8 1)",
                "dst": "(typed:signed-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x02 8)) 8 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 16 -1) (reg (bv #x00 8)) 64 64 0 64 64 1)",
                "dst": "(typed:signed-vec-sat-add (typed:vec-add (reg (bv #x01 8)) (reg (bv #x02 8)) 16 64) (reg (bv #x00 8)) 64 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 8 1) (reg (bv #x01 8)) 64 64 0 64 32 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-sat-add (reg (bv #x02 8)) (reg (bv #x00 8)) 8 64) (reg (bv #x01 8)) 32 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 8 1) (reg (bv #x00 8)) 64 64 0 64 32 1)",
                "dst": "(typed:signed-vec-sat-add (typed:signed-vec-sat-add (reg (bv #x02 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 32 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 64 64 0 64 16 0) (vadd_u16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 16 1) 64 64 0 64 32 -1)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x03 8)) 16 64) (typed:signed-vec-sat-add (reg (bv #x02 8)) (reg (bv #x00 8)) 16 64) 32 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 -1) (vadd_u16_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64 0 64 16 -1) 64 64 0 64 16 -1)",
                "dst": "(typed:vec-add (typed:vec-add (reg (bv #x03 8)) (reg (bv #x01 8)) 16 64) (typed:vec-add (reg (bv #x00 8)) (reg (bv #x02 8)) 16 64) 16 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 64 64 0 64 8 1) (vadd_u16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 64 1) 64 64 0 64 16 -1)",
                "dst": "(typed:vec-add (typed:signed-vec-sat-add (reg (bv #x03 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-sat-add (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64) 16 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 64 1) (vadd_u16_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 64 64 0 64 8 -1) 64 64 0 64 64 -1)",
                "dst": "(typed:vec-add (typed:signed-vec-sat-add (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64) (typed:vec-add (reg (bv #x03 8)) (reg (bv #x01 8)) 8 64) 64 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 32 0) (vadd_u16_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 64 64 0 64 32 -1) 64 64 0 64 64 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x02 8)) 32 64) (typed:vec-add (reg (bv #x03 8)) (reg (bv #x00 8)) 32 64) 64 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64 0 64 64 0) (vadd_u16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 0) 64 64 0 64 32 -1)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-sat-add (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64) 32 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 64 64 0 64 64 0) (vadd_u16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 32 1) 64 64 0 64 16 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x03 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-sat-add (reg (bv #x02 8)) (reg (bv #x00 8)) 32 64) 16 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 64 64 0 64 32 1) (vadd_u16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 32 1) 64 64 0 64 32 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-sat-add (reg (bv #x00 8)) (reg (bv #x02 8)) 32 64) (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x03 8)) 32 64) 32 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 64 64 0 64 16 0) (vadd_u16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 8 0) 64 64 0 64 16 1)",
                "dst": "(typed:signed-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x02 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-sat-add (reg (bv #x03 8)) (reg (bv #x01 8)) 16 64) 16 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 32 1) (vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 64 64 0 64 64 0) 64 64 0 64 16 1)",
                "dst": "(typed:signed-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x03 8)) 64 64) (typed:signed-vec-sat-add (reg (bv #x02 8)) (reg (bv #x00 8)) 32 64) 16 64)"
            }
        }
    ],
    " (vhadd_s32_dsl ; vhadd_s32\n\t (vhadd_s32_dsl ; vhadd_s32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vhadd_s32_dsl (vhadd_s32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 -1 0 16 0 16) (reg (bv #x02 8)) 64 64 0 64 16 1 -1 0 32 0 32)",
                "dst": "(typed:unsigned-vec-halving_add (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-halving_add (reg (bv #x02 8)) (reg (bv #x02 8)) 8 64) 16 64)"
            }
        }
    ],
    " (vhadd_s32_dsl ; vhadd_s32\n\t (vhadd_s32_dsl ; vhadd_s32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vhadd_s32_dsl (vhadd_s32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 1 -1 0 32 0 32) (reg (bv #x02 8)) 64 64 0 64 8 1 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-halving_add (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x02 8)) 8 64)"
            }
        }
    ],
    " (vadd_u16_dsl ; vadd_u16\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t (vadd_u16_dsl ; vadd_u16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t-1\n\t )\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vadd_u16_dsl (vadd_u16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 16 -1) (vadd_u16_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 64 64 0 64 32 1) 64 64 0 64 64 1)",
                "dst": "(typed:signed-vec-sat-add (typed:signed-vec-sat-add (reg (bv #x00 8)) (reg (bv #x03 8)) 32 64) (typed:vec-add (reg (bv #x02 8)) (reg (bv #x01 8)) 16 64) 64 64)"
            }
        }
    ],
    " (vhadd_s32_dsl ; vhadd_s32\n\t (vhadd_s32_dsl ; vhadd_s32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t )\n\t (vhadd_s32_dsl ; vhadd_s32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vhadd_s32_dsl (vhadd_s32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 1 -1 0 32 0 32) (vhadd_s32_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64 0 64 8 1 -1 0 16 0 16) 64 64 0 64 8 1 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-halving_add (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-halving_add (reg (bv #x03 8)) (reg (bv #x02 8)) 8 64) 8 64)"
            }
        }
    ],
    " (vshl_s8_dsl ; vshl_s8\n\t (vshl_s8_dsl ; vshl_s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t0\n\t\t1\n\t\t16\n\t\t1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t1\n\t16\n\t1\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vshl_s8_dsl (vshl_s8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 0 32 1) (reg (bv #x00 8)) 64 64 0 64 8 0 1 16 1)",
                "dst": "(typed:vec-shl (typed:vec-shl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x00 8)) 8 64)"
            }
        }
    ],
    " (vshl_s8_dsl ; vshl_s8\n\t (vshl_s8_dsl ; vshl_s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t0\n\t\t1\n\t\t16\n\t\t1\n\t )\n\t (vshl_s8_dsl ; vshl_s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t0\n\t\t1\n\t\t16\n\t\t1\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t1\n\t16\n\t1\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vshl_s8_dsl (vshl_s8_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 1 16 1) (vshl_s8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 16 0 0 32 1) 64 64 0 64 8 0 1 16 1)",
                "dst": "(typed:vec-shl (typed:vec-shl (reg (bv #x03 8)) (reg (bv #x01 8)) 8 64) (typed:vec-shl (reg (bv #x00 8)) (reg (bv #x02 8)) 16 64) 8 64)"
            }
        }
    ],
    " (vrhadd_s16_dsl ; vrhadd_s16\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t (vrhadd_s16_dsl ; vrhadd_s16\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t-1\n\t-1\n\t1\n\t32\n\t1\n\t32\n )_ (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrhadd_s16_dsl (lit (bv #x0001 16)) (vrhadd_s16_dsl (lit (bv #x0001 16)) (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 -1 -1 0 16 0 16) (reg (bv #x01 8)) 64 64 0 64 8 1 -1 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-rounding_halving_add (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x02 8)) 8 64) (reg (bv #x01 8)) 8 64)"
            }
        }
    ],
    " (vrhadd_s16_dsl ; vrhadd_s16\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t (vrhadd_s16_dsl ; vrhadd_s16\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t-1\n\t-1\n\t1\n\t32\n\t1\n\t32\n )_ (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrhadd_s16_dsl (lit (bv #x0000000000000001 64)) (vrhadd_s16_dsl (lit (bv #x00000001 32)) (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 16 1 -1 -1 0 32 0 32) (reg (bv #x00 8)) 64 64 0 64 32 1 -1 -1 0 64 0 64)",
                "dst": "(typed:unsigned-vec-rounding_halving_add (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x02 8)) 16 64) 32 64)"
            }
        }
    ],
    " (vrhadd_s16_dsl ; vrhadd_s16\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t (vrhadd_s16_dsl ; vrhadd_s16\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t )\n\t (vrhadd_s16_dsl ; vrhadd_s16\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t-1\n\t-1\n\t1\n\t32\n\t1\n\t32\n )_ (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrhadd_s16_dsl (lit (bv #x0000000000000001 64)) (vrhadd_s16_dsl (lit (bv #x0001 16)) (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64 0 64 8 1 -1 -1 0 16 0 16) (vrhadd_s16_dsl (lit (bv #x0001 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 1 -1 -1 0 16 0 16) 64 64 0 64 32 1 -1 -1 0 64 0 64)",
                "dst": "(typed:unsigned-vec-rounding_halving_add (typed:unsigned-vec-rounding_halving_add (reg (bv #x02 8)) (reg (bv #x03 8)) 8 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 32 64)"
            }
        }
    ],
    " (vrshld_s64_dsl ; vrshld_s64\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t (vrshld_s64_dsl ; vrshld_s64\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t-1\n\t\t1\n\t\t128\n\t\t-1\n\t\t1\n\t\t128\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t-1\n\t1\n\t128\n\t-1\n\t1\n\t128\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrshld_s64_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (vrshld_s64_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 8 0 -1 1 16 -1 1 16) (reg (bv #x00 8)) 64 64 0 64 8 0 -1 0 16 -1 1 16)",
                "dst": "(typed:vec-shl (typed:vec-shl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (reg (bv #x02 8)) 8 64)"
            }
        }
    ],
    " (vrshld_s64_dsl ; vrshld_s64\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t (vrshld_s64_dsl ; vrshld_s64\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t-1\n\t\t1\n\t\t128\n\t\t-1\n\t\t1\n\t\t128\n\t )\n\t (vrshld_s64_dsl ; vrshld_s64\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 (bitvector 128)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t-1\n\t\t1\n\t\t128\n\t\t-1\n\t\t1\n\t\t128\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t-1\n\t1\n\t128\n\t-1\n\t1\n\t128\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vrshld_s64_dsl (lit (bv #x0000000000000001 64)) (lit (bv #x0000000000000001 64)) (vrshld_s64_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 8 0 -1 1 16 -1 1 16) (vrshld_s64_dsl (lit (bv #x0000000000000001 64)) (lit (bv #x0000000000000001 64)) (reg (bv #x03 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 -1 1 64 -1 1 64) 64 64 0 64 32 0 -1 0 64 -1 1 64)",
                "dst": "(typed:vec-shl (typed:vec-shl (reg (bv #x01 8)) (reg (bv #x02 8)) 8 64) (typed:vec-shl (reg (bv #x03 8)) (reg (bv #x00 8)) 32 64) 32 64)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 16 -1) (reg (bv #x00 8)) 128 128 0 128 32 -1)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x02 8)) 16 128) (reg (bv #x00 8)) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1) (reg (bv #x02 8)) 128 128 0 128 16 -1)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x02 8)) 16 128) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 0) (reg (bv #x01 8)) 128 128 0 128 32 -1)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 8 128) (reg (bv #x01 8)) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1) (reg (bv #x00 8)) 128 128 0 128 16 -1)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 8 128) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 32 0) (reg (bv #x01 8)) 128 128 0 128 16 -1)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x02 8)) 32 128) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0) (reg (bv #x02 8)) 128 128 0 128 16 -1)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x02 8)) 16 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1) (reg (bv #x02 8)) 128 128 0 128 32 -1)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) (typed:vec-add (reg (bv #x01 8)) (reg (bv #x02 8)) 32 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0) (reg (bv #x02 8)) 128 128 0 128 32 -1)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) (typed:vec-add (reg (bv #x01 8)) (reg (bv #x02 8)) 32 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 64 1) (reg (bv #x00 8)) 128 128 0 128 32 -1)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x02 8)) 64 128) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 64 1) (reg (bv #x00 8)) 128 128 0 128 32 -1)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x02 8)) 64 128) (reg (bv #x00 8)) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 64 1) (reg (bv #x00 8)) 128 128 0 128 64 -1)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x02 8)) 64 128) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1) (reg (bv #x02 8)) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) (reg (bv #x02 8)) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1) (reg (bv #x02 8)) 128 128 0 128 64 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x02 8)) 32 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1) (reg (bv #x02 8)) 128 128 0 128 16 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 8 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 8 0) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x02 8)) 8 128) (reg (bv #x01 8)) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0) (reg (bv #x02 8)) 128 128 0 128 16 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 32 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 16 0) (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x02 8)) 16 128) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 64 1) (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 64 128) (reg (bv #x00 8)) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 1) (reg (bv #x01 8)) 128 128 0 128 16 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 8 128) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1) (reg (bv #x02 8)) 128 128 0 128 64 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 64 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 -1) (reg (bv #x02 8)) 128 128 0 128 64 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (reg (bv #x02 8)) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1) (reg (bv #x02 8)) 128 128 0 128 32 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 8 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1) (reg (bv #x01 8)) 128 128 0 128 64 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 16 128) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0) (reg (bv #x02 8)) 128 128 0 128 16 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) (reg (bv #x02 8)) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 64 0) (reg (bv #x01 8)) 128 128 0 128 64 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 64 128) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 64 0) (reg (bv #x01 8)) 128 128 0 128 8 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x02 8)) 64 128) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1) (reg (bv #x02 8)) 128 128 0 128 64 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) (reg (bv #x02 8)) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 1) (reg (bv #x02 8)) 128 128 0 128 8 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 32 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 1) (reg (bv #x02 8)) 128 128 0 128 8 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x02 8)) 8 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 32 0) (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 128 32 0) 128 128 0 128 8 -1)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x02 8)) 32 128) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x03 8)) 32 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 8 0) (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 8 1) 128 128 0 128 64 -1)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 8 128) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x03 8)) 8 128) 64 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 32 1) (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0) 128 128 0 128 16 -1)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x03 8)) (reg (bv #x02 8)) 32 128) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 16 1) (vsubq_u32_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1) 128 128 0 128 16 -1)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x02 8)) 16 128) (typed:vec-sub (reg (bv #x03 8)) (reg (bv #x00 8)) 16 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 64 1) (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 8 1) 128 128 0 128 8 -1)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x03 8)) 64 128) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x02 8)) 8 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 0) (vsubq_u32_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1) 128 128 0 128 16 -1)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 8 128) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x03 8)) 16 128) 16 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 8 -1) (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x03 8)) 8 128) (typed:vec-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 16 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 128 8 -1) (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 8 0) 128 128 0 128 32 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x03 8)) 8 128) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x02 8)) 8 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 64 -1) (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 8 1) 128 128 0 128 32 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x03 8)) (reg (bv #x01 8)) 64 128) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x02 8)) 8 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 0) (vsubq_u32_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 64 0) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 8 128) (typed:unsigned-vec-sat-sub (reg (bv #x03 8)) (reg (bv #x01 8)) 64 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 32 0) (vsubq_u32_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 8 1) 128 128 0 128 8 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 32 128) (typed:signed-vec-sat-sub (reg (bv #x03 8)) (reg (bv #x00 8)) 8 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 32 1) (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1) 128 128 0 128 32 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x03 8)) (reg (bv #x00 8)) 32 128) (typed:vec-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 16 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 32 1) (vsubq_u32_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 8 1) 128 128 0 128 32 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 32 128) (typed:signed-vec-sat-sub (reg (bv #x03 8)) (reg (bv #x01 8)) 8 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 64 0) (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1) 128 128 0 128 32 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x03 8)) (reg (bv #x02 8)) 64 128) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 8 1) (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1) 128 128 0 128 32 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x03 8)) (reg (bv #x02 8)) 8 128) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) 32 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 8 1) (vsubq_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1) 128 128 0 128 8 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x03 8)) 8 128) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) 8 128)"
            }
        }
    ],
    " (vsubq_u32_dsl ; vsubq_u32\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t (vsubq_u32_dsl ; vsubq_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t-1\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vsubq_u32_dsl (vsubq_u32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 8 1) (vsubq_u32_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 32 0) 128 128 0 128 8 1)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 8 128) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x03 8)) 32 128) 8 128)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t (vmax_u8_dsl ; vmax_u8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (vmax_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 1) (reg (bv #x02 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:signed-vec-max (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (reg (bv #x02 8)) 32 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t (vmax_u8_dsl ; vmax_u8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (vmax_u8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 1) (reg (bv #x01 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:signed-vec-max (typed:signed-vec-max (reg (bv #x02 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t (vmax_u8_dsl ; vmax_u8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t0\n\t\t0\n\t )\n\t (vmax_u8_dsl ; vmax_u8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmax_u8_dsl (vmax_u8_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 1) (vmax_u8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 1) 64 64 0 64 16 0 1)",
                "dst": "(typed:signed-vec-max (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x02 8)) 32 64) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x03 8)) 8 64) 16 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t (vmin_u32_dsl ; vmin_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (vmin_u32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 1) (reg (bv #x00 8)) 64 64 0 64 8 0 1)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x02 8)) 16 64) (reg (bv #x00 8)) 8 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t (vmin_u32_dsl ; vmin_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (vmin_u32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 1) (reg (bv #x01 8)) 64 64 0 64 32 0 1)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x02 8)) (reg (bv #x00 8)) 8 64) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t (vmin_u32_dsl ; vmin_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (vmin_u32_dsl ; vmin_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmin_u32_dsl (vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 1) (vmin_u32_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64 0 64 32 0 1) 64 64 0 64 8 0 1)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-min (reg (bv #x02 8)) (reg (bv #x03 8)) 32 64) 8 64)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (vmul_u32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 32 0 0 64 0) (reg (bv #x01 8)) 64 64 0 64 32 0 0 64 0)",
                "dst": "(typed:unsigned-vec-mul (typed:unsigned-vec-mul (reg (bv #x00 8)) (reg (bv #x02 8)) 32 64) (reg (bv #x01 8)) 32 64)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (vmul_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 0 16 0) (reg (bv #x02 8)) 64 64 0 64 32 0 0 64 0)",
                "dst": "(typed:unsigned-vec-mul (typed:signed-vec-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x02 8)) 32 64)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (vmul_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0 16 0) (reg (bv #x02 8)) 64 64 0 64 16 0 0 32 0)",
                "dst": "(typed:signed-vec-mul (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (reg (bv #x02 8)) 16 64)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (vmul_u32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 8 0 0 16 0) (reg (bv #x01 8)) 64 64 0 64 16 0 0 32 0)",
                "dst": "(typed:signed-vec-mul (typed:signed-vec-mul (reg (bv #x00 8)) (reg (bv #x02 8)) 8 64) (reg (bv #x01 8)) 16 64)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (vmul_u32_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 0 64 0) (vmul_u32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 0 32 0) 64 64 0 64 16 0 0 32 0)",
                "dst": "(typed:unsigned-vec-mul (typed:unsigned-vec-mul (reg (bv #x02 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-mul (reg (bv #x03 8)) (reg (bv #x00 8)) 32 64) 16 64)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (vmul_u32_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 64 64 0 64 32 0 0 64 0) (vmul_u32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 32 0 0 64 0) 64 64 0 64 8 0 0 16 0)",
                "dst": "(typed:unsigned-vec-mul (typed:unsigned-vec-mul (reg (bv #x00 8)) (reg (bv #x02 8)) 32 64) (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x03 8)) 32 64) 8 64)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (vmul_u32_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64 0 64 16 0 0 32 0) (vmul_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 0 0 64 0) 64 64 0 64 8 0 0 16 0)",
                "dst": "(typed:unsigned-vec-mul (typed:signed-vec-mul (reg (bv #x02 8)) (reg (bv #x03 8)) 16 64) (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 8 64)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (vmul_u32_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 64 64 0 64 16 0 0 32 0) (vmul_u32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 0 32 0) 64 64 0 64 32 0 0 64 0)",
                "dst": "(typed:signed-vec-mul (typed:unsigned-vec-mul (reg (bv #x00 8)) (reg (bv #x02 8)) 16 64) (typed:unsigned-vec-mul (reg (bv #x03 8)) (reg (bv #x01 8)) 16 64) 32 64)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (vmul_u32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 32 0 0 64 0) (vmul_u32_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 64 64 0 64 16 0 0 32 0) 64 64 0 64 16 0 0 32 0)",
                "dst": "(typed:signed-vec-mul (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x02 8)) 32 64) (typed:signed-vec-mul (reg (bv #x03 8)) (reg (bv #x00 8)) 16 64) 16 64)"
            }
        }
    ],
    " (vmul_u32_dsl ; vmul_u32\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t (vmul_u32_dsl ; vmul_u32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t0\n\t\t64\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n )_ (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(vmul_u32_dsl (vmul_u32_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 64 64 0 64 32 0 0 64 0) (vmul_u32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 16 0 0 32 0) 64 64 0 64 16 0 0 32 0)",
                "dst": "(typed:signed-vec-mul (typed:signed-vec-mul (reg (bv #x02 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x03 8)) 32 64) 16 64)"
            }
        }
    ]
}