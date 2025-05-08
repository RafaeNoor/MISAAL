x86_EqClassEqualDepthV4_filtered={
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epu32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 1)"
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
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 -1)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 0)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
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
    " (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t32\n\t1\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend-unsigned-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t16\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 1 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 256 16 1)"
            }
        }
    ],
    " (x86_swizzle_390_dsl ; x86_swizzle_390\n\t (x86_swizzle_404_dsl ; x86_swizzle_404\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (_mm_hadd_pi32_dsl ; _mm_hadd_pi32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t-1\n\t\t-1\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend-unsigned-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t16\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(x86_swizzle_390_dsl (x86_swizzle_404_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 0) (lit (bv #x0000000000000000 64)) 32 32 0 32 32 32 0 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 32 64 0)"
            }
        }
    ],
    " (_mm_hsub_epi16_dsl ; _mm_hsub_epi16\n\t (x86_swizzle_357_dsl ; x86_swizzle_357\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t128\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (x86_swizzle_356_dsl ; x86_swizzle_356\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t128\n\t\t16\n\t\t16\n\t\t128\n\t\t2\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t64\n\t16\n\t64\n\t128\n\t16\n\t-1\n\t16\n\t2\n\t-1\n\t112\n\t128\n\t2\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_hsub_epi16_dsl (x86_swizzle_357_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 32 32 2 0) (x86_swizzle_356_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 32 32 64 2 0) 128 128 0 64 32 64 128 32 -1 32 2 -1 96 128 2 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (x86_swizzle_390_dsl ; x86_swizzle_390\n\t (x86_swizzle_404_dsl ; x86_swizzle_404\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (_mm_hsub_pi32_dsl ; _mm_hsub_pi32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t-1\n\t\t-1\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend-unsigned-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t16\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(x86_swizzle_390_dsl (x86_swizzle_404_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 0) (lit (bv #x0000000000000000 64)) 32 32 0 32 32 32 0 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 32 64 0)"
            }
        }
    ],
    " (_mm_hsub_pi32_dsl ; _mm_hsub_pi32\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t-1\n\t-1\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p8-s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t1\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(_mm_hsub_pi32_dsl (x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 0) (x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 0 32 0) 32 32 0 32 32 -1 -1 32 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64 -1)"
            }
        }
    ]
}