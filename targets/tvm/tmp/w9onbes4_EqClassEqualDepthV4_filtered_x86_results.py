w9onbes4_x86_EqClassEqualDepthV4_filtered={
    " (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 512 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 -1)"
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
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epu32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 1)"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 1)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 1)"
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
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm_div_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t64\n\t1\n\t1\n\t128\n\t1\n\t128\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0 16 0 16 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 0)"
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
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s8\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-min_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s8\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0 0)",
                "dst": "(typed-folded:vec-min_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 0) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 0) 8 512 0)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 -1) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 -1) 32 64 1)"
            }
        }
    ],
    " (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 512 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t )\n\t8\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 512 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512) 64 512)"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t32\n\t1\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend-unsigned-p8-s8\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend-unsigned-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t16\n\t\t0\n\t )\n\t8\n\t8\n\t16\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 8 32 1 0 0)",
                "dst": "(typed-folded:cast-extend_dsl (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 128 16 0) 8 256 16 0)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max-signed-p8-s8\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 1 0)",
                "dst": "(typed-folded:vec-max_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 1) (reg (bv #x00 8)) 64 512 1)"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t )\n\t8\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512) (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512) 32 512)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max-signed-p8-s8\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 1 0)",
                "dst": "(typed-folded:vec-max_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 1) (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 1) 64 512 0)"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epu32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 1) (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512 1) 16 512 1)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1) (typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512 1) 8 512 1)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) (reg (bv #x01 8)) 64 512 0)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) 64 512 0)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) 64 512 0)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) (reg (bv #x01 8)) 64 512 0)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) 64 512 0)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) 64 512 0)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) (reg (bv #x01 8)) 8 512 0)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) 64 512 -1)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) 64 512 -1)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) 64 512 -1)"
            }
        }
    ],
    " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) 64 512 -1)"
            }
        }
    ],
    " (_mm_hsub_pi32_dsl ; _mm_hsub_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t-1\n\t-1\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_hsub_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 32 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 0) (x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 0 32 0) 32 64 -1)"
            }
        }
    ],
    " (_mm_hadd_pi32_dsl ; _mm_hadd_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t-1\n\t-1\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add-signed-p8-s8\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)",
                "dst": "(typed-folded:vec-add_dsl (x86_swizzle_390_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 0 32 0) (x86_swizzle_390_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 0) 32 64 -1)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) (reg (bv #x01 8)) 64 512 0)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) 64 512 0)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) (reg (bv #x01 8)) 64 512 0)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) 64 512 0)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) 64 512 0)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) 64 512 0)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) (reg (bv #x01 8)) 64 512 0)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) 64 512 -1)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) 64 512 -1)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) 64 512 -1)"
            }
        }
    ],
    " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t1\n\t )\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1) (typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0) 64 512 -1)"
            }
        }
    ]
}