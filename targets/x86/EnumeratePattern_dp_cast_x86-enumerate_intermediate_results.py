{
    " (_mm256_maddubs_epi16_dsl ; _mm_dpwssds_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t(buffer-index  1 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t1\n\t\t16\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t(buffer-index  2 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t1\n\t\t16\n\t\t32\n\t )\n\t128\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )+ (typed:vec-add ; typed:vec-add_p32_s512_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s256_signed_1\n\t\t(buffer-index  1 'uint8 256) ; < 32 x i8> False\n\t\t(buffer-index  2 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t256\n\t )\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t32\n\t512\n )+128+_mm_dpwssd_epi32+typed:vec-add_p32_s128_signed_None": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 4 32) (typed:cast-uint-extend (reg (bv #x02 8)) 16 1 4 32) 128 32 0 32 16 -1 1 1 0)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x02 8)) 16 64) (reg (bv #x00 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (_mm256_maddubs_epi16_dsl ; _mm_dpwssds_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t(buffer-index  1 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t1\n\t\t16\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t(buffer-index  2 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t1\n\t\t16\n\t\t32\n\t )\n\t128\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s512_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s256_signed_1\n\t\t(buffer-index  1 'uint8 256) ; < 32 x i8> False\n\t\t(buffer-index  2 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t256\n\t )\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t32\n\t512\n )",
                "src_ctx": "_mm_dpwssd_epi32",
                "dst_ctx": "typed:vec-add_p32_s128_signed_None"
            }
        }
    ],
    " (_mm256_maddubs_epi16_dsl ; _mm_dpwssds_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t(buffer-index  1 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t1\n\t\t16\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t(buffer-index  2 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t1\n\t\t16\n\t\t32\n\t )\n\t128\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )+ (typed:vec-add ; typed:vec-add_p32_s512_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s256_signed_1\n\t\t(buffer-index  1 'uint8 256) ; < 32 x i8> False\n\t\t(buffer-index  2 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t256\n\t )\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t32\n\t512\n )+256+_mm256_dpwssd_epi32+typed:vec-add_p32_s256_signed_None": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x02 8)) 16 1 8 32) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 8 32) 256 32 0 32 16 -1 1 1 0)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x02 8)) 16 128) (reg (bv #x00 8)) 32 256)",
                "output_size": 256,
                "original_src_expr": " (_mm256_maddubs_epi16_dsl ; _mm_dpwssds_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t(buffer-index  1 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t1\n\t\t16\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t(buffer-index  2 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t1\n\t\t16\n\t\t32\n\t )\n\t128\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s512_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s256_signed_1\n\t\t(buffer-index  1 'uint8 256) ; < 32 x i8> False\n\t\t(buffer-index  2 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t256\n\t )\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t32\n\t512\n )",
                "src_ctx": "_mm256_dpwssd_epi32",
                "dst_ctx": "typed:vec-add_p32_s256_signed_None"
            }
        }
    ],
    " (_mm256_maddubs_epi16_dsl ; _mm_dpwssds_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t(buffer-index  1 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t1\n\t\t16\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t(buffer-index  2 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t1\n\t\t16\n\t\t32\n\t )\n\t128\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )+ (typed:vec-add ; typed:vec-add_p32_s512_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s256_signed_1\n\t\t(buffer-index  1 'uint8 256) ; < 32 x i8> False\n\t\t(buffer-index  2 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t256\n\t )\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t32\n\t512\n )+512+_mm512_dpwssd_epi32+typed:vec-add_p32_s512_signed_None": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_maddubs_epi16_dsl (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x02 8)) 16 1 16 32) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 16 32) 512 32 0 32 16 -1 1 1 0)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x02 8)) 16 256) (reg (bv #x00 8)) 32 512)",
                "output_size": 512,
                "original_src_expr": " (_mm256_maddubs_epi16_dsl ; _mm_dpwssds_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t(buffer-index  1 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t1\n\t\t16\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is256_op32_os512_signed_0\n\t\t(buffer-index  2 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t1\n\t\t16\n\t\t32\n\t )\n\t128\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s512_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s256_signed_1\n\t\t(buffer-index  1 'uint8 256) ; < 32 x i8> False\n\t\t(buffer-index  2 'uint8 256) ; < 32 x i8> False\n\t\t16\n\t\t256\n\t )\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t32\n\t512\n )",
                "src_ctx": "_mm512_dpwssd_epi32",
                "dst_ctx": "typed:vec-add_p32_s512_signed_None"
            }
        }
    ]
}