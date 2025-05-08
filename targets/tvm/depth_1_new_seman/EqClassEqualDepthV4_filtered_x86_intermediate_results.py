{
    " (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 512 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512)"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 -1)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 1)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 -1)"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t32\n\t1\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend-unsigned-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t16\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 1 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 256 16 1)"
            }
        }
    ],
    " (_mm_add_si64_dsl ; _mm_add_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 -1)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epu32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 1)"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm_div_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t64\n\t1\n\t1\n\t128\n\t1\n\t128\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ]
}