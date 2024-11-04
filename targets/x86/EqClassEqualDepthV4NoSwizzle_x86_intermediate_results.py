{
    " (_mm256_maddubs_epi16_dsl ; _mm_dpwssds_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t128\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle",
            "property": {
                "src": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 16 32) (typed:cast-uint-extend (reg (bv #x02 8)) 16 1 16 32) 512 32 0 32 16 -1 1 1 0)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x02 8)) 16 256) (reg (bv #x00 8)) 32 512)"
            }
        }
    ]
}