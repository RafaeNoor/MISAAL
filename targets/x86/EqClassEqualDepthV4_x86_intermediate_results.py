{
    " (_mm_add_si64_dsl ; _mm_add_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_and_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512)"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epu32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t0\n )_ (typed:signed-vec-mod ; typed:signed-vec-mod_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512)"
            }
        }
    ],
    " (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t0\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 512 512 0 512 64 0 64 64 0)",
                "dst": "(typed:vec-shl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512)"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm_div_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t64\n\t1\n\t1\n\t128\n\t1\n\t128\n\t0\n )_ (typed:unsigned-vec-div ; typed:unsigned-vec-div_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0 16 0 16 0)",
                "dst": "(typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128)"
            }
        }
    ],
    " (_mm512_cvtusepi64_epi32_dsl ; _mm512_cvtusepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n\t64\n\t1\n\t0\n )_ (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1\n\t64\n\t8\n\t#f\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 1 16 1 0)",
                "dst": "(typed:vec-saturate (reg (bv #x00 8)) 16 1 32 8 #t)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0)",
                "dst": "(typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 64 256)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 0)",
                "dst": "(typed:signed-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 -1 0)",
                "dst": "(typed:vec-add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)",
                "dst": "(typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 128 128 0 128 32 0 32 32 0)",
                "dst": "(typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128)"
            }
        }
    ],
    " (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t16\n\t0\n\t32\n\t0\n\t0\n )_ (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 1 32 1 0)",
                "dst": "(typed:signed-vec-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t16\n\t0\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 1 32 1 0)",
                "dst": "(typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512)"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-bwand (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 512) (reg (bv #x01 8)) 64 512)"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_and_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-bwand (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) (reg (bv #x00 8)) 8 512)"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_and_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-bwand (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) 8 512)"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-bwand (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512) 16 512)"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) 32 512)"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:unsigned-vec-min (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512) (reg (bv #x00 8)) 8 512)"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-bwand (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) 16 512)"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:unsigned-vec-min (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 32 512) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512) 32 512)"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t32\n\t1\n\t0\n\t0\n )_ (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 8 32 1 1 0)",
                "dst": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 8 1 16 16) 16 1 16 32)"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t32\n\t1\n\t0\n\t0\n )_ (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 8 32 1 0 0)",
                "dst": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 8 1 16 16) 16 1 16 32)"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t32\n\t1\n\t0\n\t0\n )_ (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 8 32 1 0 0)",
                "dst": "(typed:cast-int (typed:cast-uint (reg (bv #x00 8)) 8 1 16 16) 16 1 16 32)"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epu32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t0\n )_ (typed:signed-vec-mod ; typed:signed-vec-mod_p16_s1024_signed_1\n\t (typed:signed-vec-mod ; typed:signed-vec-mod_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mod ; typed:signed-vec-mod_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:signed-vec-mod (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512) 64 512)"
            }
        }
    ],
    " (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t0\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_sllv_epi16_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 512 512 0 512 64 0 64 64 0)",
                "dst": "(typed:vec-shl (typed:vec-shl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512) (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512) 16 512)"
            }
        }
    ],
    " (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_sllv_epi16_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 512 512 0 512 32 0 32 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-shl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512) (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) 32 512)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 16 64)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-sub (typed:vec-bwnot (reg (bv #x00 8)) 64 64) (typed:vec-bwnot (reg (bv #x01 8)) 64 64) 64 64)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-sub (typed:vec-add (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:vec-add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-add (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 64 64)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 64 64)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 16 64)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) 32 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) 32 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) 32 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128) (reg (bv #x01 8)) 16 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) 16 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) (reg (bv #x01 8)) 32 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) (reg (bv #x01 8)) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128) 64 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) 16 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128) 32 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) 16 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) 32 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) 64 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 1 0)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) 64 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128) 64 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) (reg (bv #x00 8)) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) (reg (bv #x00 8)) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 16 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) 16 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) (reg (bv #x00 8)) 32 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 64 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1 0)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) 64 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128) 64 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128) 32 128)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)",
                "dst": "(typed:vec-bwand (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256) 64 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)",
                "dst": "(typed:vec-bwand (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 64 256) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 64 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 64 256) 16 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256) (reg (bv #x00 8)) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256) (reg (bv #x00 8)) 64 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 256) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256) 16 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 256) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256) 64 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 256) (reg (bv #x01 8)) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 256) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 1 0)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 256) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256) 64 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 256) 16 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256) (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 64 256) 64 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 64 256) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256) 16 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256) (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 256) 32 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)",
                "dst": "(typed:signed-vec-max (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 8 256) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256) 64 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)",
                "dst": "(typed:unsigned-vec-absd (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)",
                "dst": "(typed:signed-vec-max (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256) (reg (bv #x00 8)) 32 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)",
                "dst": "(typed:signed-vec-max (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 256) (reg (bv #x01 8)) 32 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)",
                "dst": "(typed:signed-vec-max (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 256) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256) 32 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)",
                "dst": "(typed:signed-vec-max (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 8 256) 32 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)",
                "dst": "(typed:signed-vec-max (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 256) 64 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)",
                "dst": "(typed:signed-vec-max (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 256) (reg (bv #x01 8)) 64 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)",
                "dst": "(typed:signed-vec-max (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 256) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256) 64 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 1 0)",
                "dst": "(typed:signed-vec-max (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 256) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 8 256) 32 256)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 128 128 0 128 64 0 64 64 0)",
                "dst": "(typed:unsigned-vec-shr (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) 64 128)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 128 128 0 128 64 0 64 64 0)",
                "dst": "(typed:unsigned-vec-shr (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) 64 128)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 128 128 0 128 16 0 16 16 0)",
                "dst": "(typed:unsigned-vec-shr (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) (reg (bv #x00 8)) 16 128)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 128 128 0 128 16 0 16 16 0)",
                "dst": "(typed:unsigned-vec-shr (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128) 16 128)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-rounding_shift_right ; typed:unsigned-vec-rounding_shift_right_p16_s1024_signed_0\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 128 128 0 128 16 0 16 16 0)",
                "dst": "(typed:unsigned-vec-rounding_shift_right (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) 16 128)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_shift_right ; typed:unsigned-vec-rounding_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 128 128 0 128 32 0 32 32 0)",
                "dst": "(typed:unsigned-vec-shr (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) (typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) 16 128)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-rounding_shift_right ; typed:unsigned-vec-rounding_shift_right_p16_s1024_signed_0\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_shift_right ; typed:unsigned-vec-rounding_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 128 128 0 128 16 0 16 16 0)",
                "dst": "(typed:unsigned-vec-rounding_shift_right (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) (typed:unsigned-vec-rounding_shift_right (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) 16 128)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-rounding_shift_right ; typed:unsigned-vec-rounding_shift_right_p16_s1024_signed_0\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 128 128 0 128 16 0 16 16 0)",
                "dst": "(typed:unsigned-vec-rounding_shift_right (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) (typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) 16 128)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-rounding_shift_right ; typed:unsigned-vec-rounding_shift_right_p16_s1024_signed_0\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 128 128 0 128 32 0 32 32 0)",
                "dst": "(typed:unsigned-vec-rounding_shift_right (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) 16 128)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_mul_shift_right ; typed:unsigned-vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  4 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 128 128 0 128 64 0 64 64 0)",
                "dst": "(typed:unsigned-vec-shr (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) 8 128)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 128 128 0 128 16 0 16 16 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128) (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) 32 128)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 128 128 0 128 32 0 32 32 0)",
                "dst": "(typed:signed-vec-shr (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) 32 128)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-rounding_shift_right ; typed:unsigned-vec-rounding_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 128 128 0 128 64 0 64 64 0)",
                "dst": "(typed:signed-vec-shr (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) (typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) 8 128)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 128 128 0 128 64 0 64 64 0)",
                "dst": "(typed:signed-vec-shr (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) (typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128) 16 128)"
            }
        }
    ],
    " (_mm_mul_su32_dsl ; _mm_mul_su32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t64\n\t0\n\t0\n\t0\n\t0\n )_ (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)",
                "dst": "(typed:unsigned-vec-widen-mul (typed:cast-uint (reg (bv #x01 8)) 64 1 1 32) (typed:cast-uint (reg (bv #x00 8)) 64 1 1 32) 32 32)"
            }
        }
    ],
    " (_mm256_mul_epi32_dsl ; _mm256_mul_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t128\n\t32\n\t64\n\t1\n\t1\n\t1\n\t0\n )_ (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 0 0 0)",
                "dst": "(typed:unsigned-vec-widen-mul (typed:cast-uint (reg (bv #x00 8)) 64 1 4 32) (typed:cast-uint (reg (bv #x01 8)) 64 1 4 32) 32 128)"
            }
        }
    ],
    " (_mm256_mul_epi32_dsl ; _mm256_mul_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t128\n\t32\n\t64\n\t1\n\t1\n\t1\n\t0\n )_ (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 0 0 0)",
                "dst": "(typed:unsigned-vec-widen-mul (typed:cast-int (reg (bv #x01 8)) 64 1 4 32) (typed:cast-int (reg (bv #x00 8)) 64 1 4 32) 32 128)"
            }
        }
    ],
    " (_mm256_mul_epi32_dsl ; _mm256_mul_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t128\n\t32\n\t64\n\t1\n\t1\n\t1\n\t0\n )_ (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 0 0 0)",
                "dst": "(typed:unsigned-vec-widen-mul (typed:cast-uint (reg (bv #x00 8)) 64 1 4 32) (typed:cast-int (reg (bv #x01 8)) 64 1 4 32) 32 128)"
            }
        }
    ],
    " (_mm256_mul_epi32_dsl ; _mm256_mul_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t128\n\t32\n\t64\n\t1\n\t1\n\t1\n\t0\n )_ (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)",
                "dst": "(typed:signed-vec-widen-mul (typed:cast-int (reg (bv #x00 8)) 64 1 4 32) (typed:cast-int (reg (bv #x01 8)) 64 1 4 32) 32 128)"
            }
        }
    ],
    " (_mm256_mul_epi32_dsl ; _mm256_mul_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t128\n\t32\n\t64\n\t1\n\t1\n\t1\n\t0\n )_ (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)",
                "dst": "(typed:signed-vec-widen-mul (typed:cast-uint (reg (bv #x01 8)) 64 1 4 32) (typed:cast-int (reg (bv #x00 8)) 64 1 4 32) 32 128)"
            }
        }
    ],
    " (_mm256_mul_epi32_dsl ; _mm256_mul_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t128\n\t32\n\t64\n\t1\n\t1\n\t1\n\t0\n )_ (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)",
                "dst": "(typed:signed-vec-widen-mul (typed:cast-uint (reg (bv #x01 8)) 64 1 4 32) (typed:cast-uint (reg (bv #x00 8)) 64 1 4 32) 32 128)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-bwnot (reg (bv #x00 8)) 8 512) (typed:vec-bwnot (reg (bv #x01 8)) 8 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) (reg (bv #x01 8)) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 512) (reg (bv #x01 8)) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 512) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed:vec-add (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 512) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 64 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:vec-add (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-bwnot (reg (bv #x01 8)) 8 512) (typed:vec-bwnot (reg (bv #x00 8)) 16 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512) (reg (bv #x00 8)) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512) (typed:vec-add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:vec-add (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (reg (bv #x00 8)) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (reg (bv #x00 8)) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:vec-bwnot (reg (bv #x01 8)) 32 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed:unsigned-vec-max (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 512) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-bwnot (reg (bv #x01 8)) 8 512) (typed:vec-bwnot (reg (bv #x00 8)) 32 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 512) (reg (bv #x01 8)) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:unsigned-vec-min (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed:unsigned-vec-min (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 512) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 512) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512) (reg (bv #x00 8)) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) 32 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512) 16 512)"
            }
        }
    ],
    " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_andnot_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-sub (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512) 8 512)"
            }
        }
    ],
    " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512) 32 512)"
            }
        }
    ],
    " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-bwand (typed:vec-bwnot (reg (bv #x01 8)) 8 512) (reg (bv #x00 8)) 32 512)"
            }
        }
    ],
    " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-bwand (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) (typed:vec-bwnot (reg (bv #x01 8)) 64 512) 32 512)"
            }
        }
    ],
    " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-bwand (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 512) (typed:vec-bwnot (reg (bv #x01 8)) 64 512) 8 512)"
            }
        }
    ],
    " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 8 512) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) 64 512)"
            }
        }
    ],
    " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 512) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512) 64 512)"
            }
        }
    ],
    " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:unsigned-vec-absd (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512) (reg (bv #x00 8)) 64 512)"
            }
        }
    ],
    " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:unsigned-vec-absd (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 64 512) 32 512)"
            }
        }
    ],
    " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:unsigned-vec-absd (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 512) 32 512)"
            }
        }
    ],
    " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 512) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512) 8 512)"
            }
        }
    ],
    " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512) 64 512)"
            }
        }
    ],
    " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_andnot_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) 16 512)"
            }
        }
    ],
    " (_mm_hadd_pi32_dsl ; _mm_hadd_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t-1\n\t-1\n\t0\n\t32\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)",
                "dst": "(typed:vec-add (x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 0) (x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 0 32 0) 32 64)"
            }
        }
    ],
    " (_mm_hsub_pi32_dsl ; _mm_hsub_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t-1\n\t-1\n\t32\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_hsub_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 32 0 0)",
                "dst": "(typed:vec-sub (x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 0) (x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 0 32 0) 32 64)"
            }
        }
    ],
    " (_mm256_maddubs_epi16_dsl ; _mm256_maddubs_epi16\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 256)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t16\n\t0\n\t16\n\t8\n\t1\n\t1\n\t0\n\t0\n )_ (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p16_s1024_signed_None_reduce_2\n\t2\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_maddubs_epi16_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (reg (bv #x00 8)) (reg (bv #x01 8)) 256 32 0 32 16 -1 1 1 0)",
                "dst": "(typed:signed-vector_reduce_add 2 (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 256) 32 512)"
            }
        }
    ],
    " (_mm_add_si64_dsl ; _mm_add_si64\n\t (_mm_add_si64_dsl ; _mm_add_si64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_si64_dsl (_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0) (reg (bv #x02 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-add (typed:vec-add (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x01 8)) 64 64)"
            }
        }
    ],
    " (_mm_add_si64_dsl ; _mm_add_si64\n\t (_mm_add_si64_dsl ; _mm_add_si64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t (_mm_add_si64_dsl ; _mm_add_si64\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_si64_dsl (_mm_add_si64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0) (_mm_add_si64_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-add (typed:vec-add (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64) (typed:vec-add (reg (bv #x03 8)) (reg (bv #x00 8)) 64 64) 64 64)"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_and_epi32_dsl (_mm512_and_epi32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 32 0) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-bwand (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512) (reg (bv #x02 8)) 32 512)"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_and_epi32_dsl (_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 32 0) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-bwand (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x02 8)) 64 512) 8 512)"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_and_epi32_dsl (_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 32 0) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed:vec-bwand (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x02 8)) 8 512) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) 8 512)"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_and_epi32_dsl (_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 512 512 0 512 32 0) (_mm512_and_epi32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 32 0) 512 512 0 512 32 0)",
                "dst": "(typed:vec-bwand (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x02 8)) 16 512) (typed:vec-bwand (reg (bv #x03 8)) (reg (bv #x00 8)) 8 512) 16 512)"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t32\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t32\n\t1\n\t0\n\t0\n )_ (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 32 64 1 0 0) 256 256 0 256 16 32 1 0 0)",
                "dst": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 32 1 4 64) 16 1 16 32)"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t32\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t32\n\t1\n\t0\n\t0\n )_ (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 16 32 1 1 0) 256 256 0 256 32 64 1 0 0)",
                "dst": "(typed:cast-uint (typed:cast-int (reg (bv #x00 8)) 16 1 8 32) 32 1 8 64)"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t32\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t32\n\t1\n\t0\n\t0\n )_ (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 8 16 1 1 0) 256 256 0 256 16 32 1 0 0)",
                "dst": "(typed:cast-int (typed:cast-uint (reg (bv #x00 8)) 8 1 16 16) 8 1 32 16)"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t32\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t32\n\t1\n\t0\n\t0\n )_ (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 16 32 1 1 0) 256 256 0 256 32 64 1 1 0)",
                "dst": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 16 1 8 32) 16 1 16 32)"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epu32\n\t (_mm512_rem_epu32_dsl ; _mm512_rem_epu32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t (_mm512_rem_epu32_dsl ; _mm512_rem_epu32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t0\n )_ (typed:signed-vec-mod ; typed:signed-vec-mod_p16_s1024_signed_1\n\t (typed:signed-vec-mod ; typed:signed-vec-mod_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mod ; typed:signed-vec-mod_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 8 1 0) (_mm512_rem_epu32_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0) 512 512 0 512 8 1 0)",
                "dst": "(typed:signed-vec-mod (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x02 8)) 8 512) (typed:signed-vec-mod (reg (bv #x03 8)) (reg (bv #x01 8)) 8 512) 8 512)"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epu32\n\t (_mm512_rem_epu32_dsl ; _mm512_rem_epu32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t0\n )_ (typed:signed-vec-mod ; typed:signed-vec-mod_p16_s1024_signed_1\n\t (typed:signed-vec-mod ; typed:signed-vec-mod_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 16 1 0) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:signed-vec-mod (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x02 8)) 16 512) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 0) (reg (bv #x01 8)) 64 64 0 64 8 -1 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-add (reg (bv #x02 8)) (reg (bv #x00 8)) 8 64) (reg (bv #x01 8)) 8 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 8 -1 0) (reg (bv #x00 8)) 64 64 0 64 32 -1 0)",
                "dst": "(typed:vec-add (typed:vec-add (reg (bv #x01 8)) (reg (bv #x02 8)) 8 64) (reg (bv #x00 8)) 32 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 0) (reg (bv #x01 8)) 64 64 0 64 8 -1 0)",
                "dst": "(typed:vec-add (typed:signed-vec-sat-add (reg (bv #x00 8)) (reg (bv #x02 8)) 8 64) (reg (bv #x01 8)) 8 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 32 -1 0) (reg (bv #x00 8)) 64 64 0 64 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:vec-add (reg (bv #x01 8)) (reg (bv #x02 8)) 32 64) (reg (bv #x00 8)) 8 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 1 0) (reg (bv #x02 8)) 64 64 0 64 16 1 0)",
                "dst": "(typed:signed-vec-sat-add (typed:signed-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x02 8)) 16 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 0) (reg (bv #x02 8)) 64 64 0 64 8 1 0)",
                "dst": "(typed:signed-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x02 8)) 8 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 16 -1 0) (reg (bv #x00 8)) 64 64 0 64 8 1 0)",
                "dst": "(typed:signed-vec-sat-add (typed:vec-add (reg (bv #x02 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x00 8)) 8 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0) (reg (bv #x00 8)) 64 64 0 64 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x02 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 16 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 16 1 0) (reg (bv #x01 8)) 64 64 0 64 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-sat-add (reg (bv #x00 8)) (reg (bv #x02 8)) 16 64) (reg (bv #x01 8)) 8 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 16 1 0) (_mm_add_pi8_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 64 64 0 64 8 1 0) 64 64 0 64 16 -1 0)",
                "dst": "(typed:vec-add (typed:signed-vec-sat-add (reg (bv #x02 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-sat-add (reg (bv #x03 8)) (reg (bv #x01 8)) 8 64) 16 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64 0 64 16 1 0) (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 0) 64 64 0 64 16 -1 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-sat-add (reg (bv #x02 8)) (reg (bv #x03 8)) 16 64) 16 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 8 -1 0) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 64 64 0 64 8 1 0) 64 64 0 64 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-sat-add (reg (bv #x00 8)) (reg (bv #x03 8)) 8 64) (typed:vec-add (reg (bv #x02 8)) (reg (bv #x01 8)) 8 64) 8 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64 0 64 16 0 0) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0) 64 64 0 64 32 -1 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-add (reg (bv #x02 8)) (reg (bv #x03 8)) 16 64) (typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0) (_mm_add_pi8_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64 0 64 8 1 0) 64 64 0 64 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:signed-vec-sat-add (reg (bv #x02 8)) (reg (bv #x03 8)) 8 64) 16 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 -1 0) (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64 0 64 16 0 0) 64 64 0 64 8 1 0)",
                "dst": "(typed:signed-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x03 8)) (reg (bv #x02 8)) 16 64) (typed:vec-add (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 8 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64 0 64 16 -1 0) (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 -1 0) 64 64 0 64 8 -1 0)",
                "dst": "(typed:vec-add (typed:vec-add (reg (bv #x03 8)) (reg (bv #x02 8)) 16 64) (typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 8 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 64 0 64 8 1 0) (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 0) 64 64 0 64 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:signed-vec-sat-add (reg (bv #x03 8)) (reg (bv #x02 8)) 8 64) (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 8 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 32 -1 0) (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 64 64 0 64 16 -1 0) 64 64 0 64 8 1 0)",
                "dst": "(typed:signed-vec-sat-add (typed:vec-add (reg (bv #x03 8)) (reg (bv #x01 8)) 16 64) (typed:vec-add (reg (bv #x00 8)) (reg (bv #x02 8)) 32 64) 8 64)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t (_mm_sub_si64_dsl ; _mm_sub_si64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (_mm_sub_si64_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x00 8)) 64 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 64 64 0 64 32 -1 0) (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0) 64 64 0 64 8 -1 0)",
                "dst": "(typed:vec-add (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x02 8)) 8 64) (typed:vec-add (reg (bv #x03 8)) (reg (bv #x00 8)) 32 64) 8 64)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t (_mm_sub_si64_dsl ; _mm_sub_si64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t (_mm_sub_si64_dsl ; _mm_sub_si64\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (_mm_sub_si64_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0) (_mm_sub_si64_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-add (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64) (typed:vec-sub (reg (bv #x03 8)) (reg (bv #x00 8)) 64 64) 64 64)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t (_mm_sub_si64_dsl ; _mm_sub_si64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t (_mm_sub_si64_dsl ; _mm_sub_si64\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (_mm_sub_si64_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0) (_mm_sub_si64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-sub (typed:vec-add (reg (bv #x03 8)) (reg (bv #x00 8)) 64 64) (typed:vec-add (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64) 64 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 64 64 0 64 16 -1 0) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 8 1 0) 64 64 0 64 8 1 0)",
                "dst": "(typed:signed-vec-sat-add (typed:signed-vec-sat-add (reg (bv #x02 8)) (reg (bv #x00 8)) 8 64) (typed:vec-add (reg (bv #x01 8)) (reg (bv #x03 8)) 16 64) 8 64)"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t (_mm_sub_si64_dsl ; _mm_sub_si64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t (_mm_sub_si64_dsl ; _mm_sub_si64\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_sub_si64_dsl (_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 64 -1 0 0) (_mm_sub_si64_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x03 8)) 64 64) (typed:vec-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64) 64 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 1 0) (_mm_add_pi8_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64 0 64 8 1 0) 64 64 0 64 16 1 0)",
                "dst": "(typed:signed-vec-sat-add (typed:signed-vec-sat-add (reg (bv #x03 8)) (reg (bv #x02 8)) 8 64) (typed:signed-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 16 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 16 1 0) (_mm_add_pi8_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 64 64 0 64 8 -1 0) 64 64 0 64 8 -1 0)",
                "dst": "(typed:vec-add (typed:signed-vec-sat-add (reg (bv #x02 8)) (reg (bv #x01 8)) 16 64) (typed:vec-add (reg (bv #x00 8)) (reg (bv #x03 8)) 8 64) 8 64)"
            }
        }
    ],
    " (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t16\n\t0\n\t32\n\t0\n\t0\n )_ (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_mulhi_epu16_dsl (_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 32 0 0 64 0 0) (reg (bv #x00 8)) 512 512 0 512 64 0 0 128 0 0)",
                "dst": "(typed:signed-vec-mul (typed:signed-vec-mul (reg (bv #x02 8)) (reg (bv #x01 8)) 32 512) (reg (bv #x00 8)) 64 512)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0) (reg (bv #x02 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) (reg (bv #x02 8)) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 8 0 0) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x02 8)) 8 128) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 8 128)"
            }
        }
    ],
    " (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t16\n\t0\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_mulhi_epu16_dsl (_mm512_mulhi_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 1 32 1 0) (reg (bv #x01 8)) 512 512 0 512 32 0 0 64 0 0)",
                "dst": "(typed:unsigned-vec-mul (typed:signed-vec-mul (reg (bv #x02 8)) (reg (bv #x00 8)) 16 512) (reg (bv #x01 8)) 32 512)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 64 1 0) (reg (bv #x00 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x02 8)) 64 128) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 16 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0) (reg (bv #x02 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128) (reg (bv #x02 8)) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 8 0 0) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x01 8)) 8 128) (reg (bv #x00 8)) 16 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0) (reg (bv #x02 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 16 128) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) 16 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0) (reg (bv #x02 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x01 8)) 32 128) 32 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0) (reg (bv #x02 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x02 8)) 16 128) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0) (reg (bv #x02 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x02 8)) 32 128) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) 8 128)"
            }
        }
    ],
    " (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t16\n\t16\n\t0\n\t32\n\t0\n\t0\n )_ (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_mulhi_epu16_dsl (_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 512 512 0 512 32 0 0 64 0 0) (_mm512_mulhi_epu16_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 1 32 1 0) 512 512 0 512 64 0 0 128 0 0)",
                "dst": "(typed:signed-vec-mul (typed:unsigned-vec-mul (reg (bv #x02 8)) (reg (bv #x01 8)) 16 512) (typed:unsigned-vec-mul (reg (bv #x03 8)) (reg (bv #x00 8)) 32 512) 64 512)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 8 0 0) (reg (bv #x01 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x02 8)) 8 128) 16 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0) (reg (bv #x01 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x02 8)) 8 128) 16 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x00 8)) 64 128) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 16 0 0) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x01 8)) 16 128) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128) 8 128)"
            }
        }
    ],
    " (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t16\n\t16\n\t0\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_mulhi_epu16_dsl (_mm512_mulhi_epu16_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 1 32 1 0) (_mm512_mulhi_epu16_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0 64 0 0) 512 512 0 512 32 0 0 64 0 0)",
                "dst": "(typed:unsigned-vec-mul (typed:unsigned-vec-mul (reg (bv #x00 8)) (reg (bv #x03 8)) 32 512) (typed:unsigned-vec-mul (reg (bv #x02 8)) (reg (bv #x01 8)) 16 512) 32 512)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 32 1 0) (reg (bv #x01 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) (reg (bv #x02 8)) 32 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0) (reg (bv #x02 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 16 128) 32 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0) (reg (bv #x02 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x02 8)) (reg (bv #x02 8)) 8 128) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) 32 128)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 8 0 0) (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 64 64 0 64 8 1 0) 64 64 0 64 8 1 0)",
                "dst": "(typed:signed-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x02 8)) (reg (bv #x00 8)) 8 64) (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x03 8)) 8 64) 8 64)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 64 0 0) (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 8 1 0) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x01 8)) 64 128) (typed:signed-vec-min (reg (bv #x03 8)) (reg (bv #x00 8)) 8 128) 8 128)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 64 64 0 64 16 0 0) (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0) 64 64 0 64 8 1 0)",
                "dst": "(typed:signed-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x03 8)) 16 64) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x02 8)) 8 64) 8 64)"
            }
        }
    ],
    " (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t16\n\t16\n\t0\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_mulhi_epu16_dsl (_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 512 512 0 512 16 0 1 32 1 0) (_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 32 0 0 64 0 0) 512 512 0 512 32 0 0 64 0 0)",
                "dst": "(typed:unsigned-vec-mul (typed:unsigned-vec-mul (reg (bv #x00 8)) (reg (bv #x03 8)) 16 512) (typed:signed-vec-mul (reg (bv #x02 8)) (reg (bv #x01 8)) 32 512) 32 512)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 -1 0) (_mm_add_pi8_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 64 64 0 64 32 -1 0) 64 64 0 64 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:vec-add (reg (bv #x03 8)) (reg (bv #x02 8)) 32 64) 16 64)"
            }
        }
    ],
    " (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t16\n\t16\n\t0\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_mulhi_epu16_dsl (_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 1 32 1 0) (_mm512_mulhi_epu16_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 512 512 0 512 64 0 0 128 0 0) 512 512 0 512 16 0 1 32 1 0)",
                "dst": "(typed:unsigned-vec-mul (typed:signed-vec-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512) (typed:signed-vec-mul (reg (bv #x02 8)) (reg (bv #x03 8)) 64 512) 16 512)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0) (_mm_min_epu16_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 8 0 0) 128 128 0 128 32 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x03 8)) (reg (bv #x02 8)) 8 128) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) 32 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0) (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 16 0 0) 128 128 0 128 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x03 8)) 16 128) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x02 8)) 16 128) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 8 1 0) (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 0) 128 128 0 128 16 1 0)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x03 8)) (reg (bv #x02 8)) 8 128) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128) 16 128)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 64 64 0 64 16 0 0) (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0) 64 64 0 64 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x02 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x03 8)) 16 64) 8 64)"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 64 64 0 64 8 -1 0) (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 8 0 0) 64 64 0 64 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (typed:unsigned-vec-sat-add (reg (bv #x02 8)) (reg (bv #x01 8)) 8 64) (typed:vec-add (reg (bv #x00 8)) (reg (bv #x03 8)) 8 64) 8 64)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 32 0 0) (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 16 0 0) 128 128 0 128 8 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x01 8)) 32 128) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x03 8)) 16 128) 8 128)"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0) (_mm_min_epu16_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 32 1 0) 128 128 0 128 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) (typed:signed-vec-min (reg (bv #x02 8)) (reg (bv #x03 8)) 32 128) 16 128)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0) (reg (bv #x02 8)) 256 256 0 256 64 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 8 256) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 256) 64 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0) (reg (bv #x02 8)) 256 256 0 256 8 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256) (typed:vec-bwand (reg (bv #x02 8)) (reg (bv #x02 8)) 64 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0) (reg (bv #x01 8)) 256 256 0 256 16 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x02 8)) 8 256) (reg (bv #x01 8)) 16 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 16 1 0) (reg (bv #x01 8)) 256 256 0 256 32 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-max (reg (bv #x02 8)) (reg (bv #x00 8)) 16 256) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256) 32 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0) (reg (bv #x00 8)) 256 256 0 256 16 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256) (typed:signed-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 64 256) 16 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 32 1 0) (reg (bv #x00 8)) 256 256 0 256 8 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x02 8)) 32 256) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 32 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 32 1 0) (reg (bv #x00 8)) 256 256 0 256 64 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-max (reg (bv #x02 8)) (reg (bv #x01 8)) 32 256) (reg (bv #x00 8)) 64 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 32 0 0) (reg (bv #x00 8)) 256 256 0 256 32 1 0)",
                "dst": "(typed:signed-vec-max (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x01 8)) 32 256) (reg (bv #x00 8)) 32 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0) (reg (bv #x02 8)) 256 256 0 256 16 1 0)",
                "dst": "(typed:signed-vec-max (typed:signed-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 64 256) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 64 256) 16 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0) (reg (bv #x01 8)) 256 256 0 256 64 1 0)",
                "dst": "(typed:signed-vec-max (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x02 8)) 64 256) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256) 64 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0) (reg (bv #x00 8)) 256 256 0 256 32 1 0)",
                "dst": "(typed:signed-vec-max (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x02 8)) 8 256) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 32 256) 32 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 64 1 0) (reg (bv #x01 8)) 256 256 0 256 16 1 0)",
                "dst": "(typed:signed-vec-max (typed:signed-vec-max (reg (bv #x02 8)) (reg (bv #x00 8)) 64 256) (reg (bv #x01 8)) 16 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 8 0 0) (reg (bv #x00 8)) 256 256 0 256 8 1 0)",
                "dst": "(typed:signed-vec-max (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 256) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x01 8)) 8 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0) (reg (bv #x02 8)) 256 256 0 256 8 1 0)",
                "dst": "(typed:signed-vec-max (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 64 256) (typed:signed-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 8 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 256 256 0 256 64 1 0) (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0) 256 256 0 256 8 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-max (reg (bv #x02 8)) (reg (bv #x03 8)) 64 256) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 256 256 0 256 16 1 0) (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0) 256 256 0 256 64 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x02 8)) 64 256) (typed:signed-vec-max (reg (bv #x03 8)) (reg (bv #x01 8)) 16 256) 64 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0) (_mm256_max_epu64_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0) 256 256 0 256 8 1 0)",
                "dst": "(typed:signed-vec-max (typed:unsigned-vec-max (reg (bv #x03 8)) (reg (bv #x01 8)) 8 256) (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x02 8)) 32 256) 8 256)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t )\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0010 16)) (reg (bv #x02 8)) 128 128 0 128 16 0 16 16 0) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 128 128 0 128 64 0 64 64 0)",
                "dst": "(typed:unsigned-vec-shr (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128) (typed:unsigned-vec-shr (reg (bv #x02 8)) (reg (bv #x00 8)) 16 128) 64 128)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0) (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 32 0 0) 256 256 0 256 8 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-max (reg (bv #x03 8)) (reg (bv #x00 8)) 8 256) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x02 8)) 32 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 256 256 0 256 8 0 0) (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0) 256 256 0 256 8 1 0)",
                "dst": "(typed:signed-vec-max (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x02 8)) 16 256) (typed:unsigned-vec-max (reg (bv #x03 8)) (reg (bv #x01 8)) 8 256) 8 256)"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 256 256 0 256 8 1 0) (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 64 1 0) 256 256 0 256 8 1 0)",
                "dst": "(typed:signed-vec-max (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x03 8)) 8 256) (typed:signed-vec-max (reg (bv #x02 8)) (reg (bv #x01 8)) 64 256) 8 256)"
            }
        }
    ],
    " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t )\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )_ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_srlv_epi32_dsl (_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0010 16)) (reg (bv #x03 8)) 128 128 0 128 16 0 16 16 0) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0000000000000040 64)) (_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x0000000000000040 64)) (reg (bv #x02 8)) 128 128 0 128 64 0 64 64 0) 128 128 0 128 64 0 64 64 0)",
                "dst": "(typed:unsigned-vec-shr (typed:unsigned-vec-shr (reg (bv #x02 8)) (reg (bv #x00 8)) 64 128) (typed:unsigned-vec-shr (reg (bv #x03 8)) (reg (bv #x01 8)) 16 128) 64 128)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 16 512) (reg (bv #x00 8)) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 16 512) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 16 512) (reg (bv #x00 8)) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 16 1 0) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x02 8)) 16 512) (reg (bv #x01 8)) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0) (reg (bv #x02 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 64 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0) (reg (bv #x02 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 32 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0) (reg (bv #x02 8)) 512 512 0 512 64 -1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x02 8)) 8 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x02 8)) 8 512) (typed:vec-add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0) (reg (bv #x02 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512) (reg (bv #x02 8)) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0) (reg (bv #x02 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 64 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 8 512) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 16 512) (typed:unsigned-vec-min (reg (bv #x02 8)) (reg (bv #x00 8)) 16 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 8 -1 0) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x02 8)) 8 512) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 8 512) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 16 512) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0) (reg (bv #x02 8)) 512 512 0 512 64 -1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 32 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:vec-sub (reg (bv #x02 8)) (reg (bv #x01 8)) 64 512) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 64 -1 0) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) (typed:vec-add (reg (bv #x02 8)) (reg (bv #x00 8)) 64 512) 64 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 8 -1 0) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x02 8)) 8 512) (reg (bv #x00 8)) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0) (reg (bv #x02 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 32 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 8 0 0) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 32 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 8 512) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 8 1 0) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x02 8)) 8 512) (reg (bv #x00 8)) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 32 512) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0) (reg (bv #x02 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 32 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0) (reg (bv #x02 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512) (reg (bv #x02 8)) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 16 512) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512) 8 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 8 -1 0) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x02 8)) 8 512) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0) (reg (bv #x02 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512) (typed:unsigned-vec-max (reg (bv #x02 8)) (reg (bv #x02 8)) 32 512) 16 512)"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t (_mm512_subs_epi8_dsl ; _mm512_subs_epi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t8\n\t\t1\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (_mm512_subs_epi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0) (_mm512_subs_epi8_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0) 512 512 0 512 8 1 0)",
                "dst": "(typed:signed-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 16 512) (typed:unsigned-vec-sat-sub (reg (bv #x03 8)) (reg (bv #x01 8)) 8 512) 8 512)"
            }
        }
    ],
    " (x86_swizzle_390_dsl ; x86_swizzle_390\n\t (_mm_hadd_pi32_dsl ; _mm_hadd_pi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t-1\n\t\t-1\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (_mm_hadd_pi32_dsl ; _mm_hadd_pi32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t-1\n\t\t-1\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(x86_swizzle_390_dsl (_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0) (_mm_hadd_pi32_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 32 32 0 32 32 -1 -1 0 32 0) 32 32 0 32 32 0 32 0)",
                "dst": "(typed:vec-add (x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 32 32 0 32 32 32 0 0) (x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 32 32 0 32 32 0 32 0) 32 64)"
            }
        }
    ],
    " (_mm_hadd_pi32_dsl ; _mm_hadd_pi32\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t-1\n\t-1\n\t0\n\t32\n\t0\n )_ (x86_swizzle_390_dsl ; x86_swizzle_390\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_hadd_pi32_dsl (x86_swizzle_390_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 0) (x86_swizzle_390_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 32 32 0 32 32 32 0 0) 32 32 0 32 32 -1 -1 0 32 0)",
                "dst": "(x86_swizzle_390_dsl (typed:vec-add (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64) (typed:vec-add (reg (bv #x03 8)) (reg (bv #x01 8)) 32 64) 32 32 0 32 32 32 0 0)"
            }
        }
    ],
    " (_mm_hadd_pi32_dsl ; _mm_hadd_pi32\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t-1\n\t-1\n\t0\n\t32\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_hadd_pi32_dsl (x86_swizzle_390_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 32 32 0 32 32 32 0 0) (x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 0) 32 32 0 32 32 -1 -1 0 32 0)",
                "dst": "(typed:vec-add (x86_swizzle_390_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 0) (x86_swizzle_390_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 0) 32 64)"
            }
        }
    ],
    " (x86_swizzle_390_dsl ; x86_swizzle_390\n\t (_mm_hsub_pi32_dsl ; _mm_hsub_pi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t-1\n\t\t-1\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (_mm_hsub_pi32_dsl ; _mm_hsub_pi32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t-1\n\t\t-1\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(x86_swizzle_390_dsl (_mm_hsub_pi32_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 32 32 0 32 32 -1 -1 32 0 0) (_mm_hsub_pi32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 32 32 0 32 32 -1 -1 32 0 0) 32 32 0 32 32 32 0 0)",
                "dst": "(typed:vec-sub (x86_swizzle_390_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 0) (x86_swizzle_390_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 0 32 0) 32 64)"
            }
        }
    ],
    " (_mm_hsub_pi32_dsl ; _mm_hsub_pi32\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t-1\n\t-1\n\t32\n\t0\n\t0\n )_ (x86_swizzle_390_dsl ; x86_swizzle_390\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_hsub_pi32_dsl (x86_swizzle_390_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 32 32 0 32 32 0 32 0) (x86_swizzle_390_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 32 32 0 32 32 0 32 0) 32 32 0 32 32 -1 -1 32 0 0)",
                "dst": "(x86_swizzle_390_dsl (typed:vec-sub (reg (bv #x02 8)) (reg (bv #x00 8)) 32 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x03 8)) 32 64) 32 32 0 32 32 0 32 0)"
            }
        }
    ],
    " (_mm_hsub_pi32_dsl ; _mm_hsub_pi32\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t-1\n\t-1\n\t32\n\t0\n\t0\n )_ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t (x86_swizzle_390_dsl ; x86_swizzle_390\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm_hsub_pi32_dsl (x86_swizzle_390_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 32 32 0 32 32 32 0 0) (x86_swizzle_390_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 0) 32 32 0 32 32 -1 -1 32 0 0)",
                "dst": "(typed:vec-sub (x86_swizzle_390_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 32 32 0 32 32 32 0 0) (x86_swizzle_390_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 0) 32 64)"
            }
        }
    ],
    " (_mm256_maddubs_epi16_dsl ; _mm256_maddubs_epi16\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 256)))\n\t (x86_swizzle_445_dsl ; x86_swizzle_445\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t (x86_swizzle_445_dsl ; x86_swizzle_445\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t256\n\t16\n\t0\n\t16\n\t8\n\t1\n\t1\n\t0\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4",
            "property": {
                "src": "(_mm256_maddubs_epi16_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (x86_swizzle_445_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 16 2 0) (x86_swizzle_445_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 16 2 0) 256 32 0 32 16 -1 1 1 0)",
                "dst": "(typed:vec-add (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x02 8)) 16 128) (typed:signed-vec-widen-mul (reg (bv #x03 8)) (reg (bv #x01 8)) 16 128) 32 256)"
            }
        }
    ]
}