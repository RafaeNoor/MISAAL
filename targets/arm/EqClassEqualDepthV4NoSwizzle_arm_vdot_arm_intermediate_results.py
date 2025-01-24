{
    " (vdotq_s32_dsl ; vdotq_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p16_s1024_signed_None_reduce_2\n\t\t2\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t\t16\n\t\t\t\t1024\n\t\t\t )\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_arm_vdot",
            "property": {
                "src": "(vdotq_s32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 128 32 0 32 8 -1 1 1)",
                "dst": "(typed:vec-add (typed:signed-vector_reduce_add 4 (typed:cast-int-extend (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x02 8)) 8 128) 16 1 16 32) 32 512) (reg (bv #x01 8)) 32 128)"
            }
        }
    ],

    " (vdotq_s32_dsl ; vdotq_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p16_s1024_signed_None_reduce_2\n\t\t2\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t\t16\n\t\t\t\t1024\n\t\t\t )\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_arm_vdot",
            "property": {
                "src": "(vdotq_s32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 32 0 32 8 -1 0 0)",
                "dst": "(typed:vec-add (typed:signed-vector_reduce_add 4 (typed:cast-uint-extend (typed:unsigned-vec-widen-mul (reg (bv #x02 8)) (reg (bv #x01 8)) 8 128) 16 1 16 32) 32 512) (reg (bv #x00 8)) 32 128)"
            }
        }
    ]
}
