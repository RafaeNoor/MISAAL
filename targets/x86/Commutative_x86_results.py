x86_Commutative={
    "_mm256_xor_si256_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm256_xor_si256",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "output_expression": " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm256_xor_epi32_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm256_xor_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "output_expression": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm_add_si64_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm_add_si64",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm_add_si64_dsl ; _mm_add_si64\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )",
                "output_expression": " (_mm_add_si64_dsl ; _mm_add_si64\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_or_epi32_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm512_or_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm256_max_epu64_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm256_max_epu64",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_mulhi_epu16_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t16\n\t0\n\t32\n\t0\n\t0\n )",
                "output_expression": " (_mm512_mulhi_epu16_dsl ; _mm512_mulhi_epu16\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t16\n\t0\n\t32\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm256_mul_epi32_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_mul_epi32_dsl ; _mm256_mul_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t128\n\t32\n\t64\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (_mm256_mul_epi32_dsl ; _mm256_mul_epi32\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t128\n\t32\n\t64\n\t1\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "_mm_mul_su32_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm_mul_su32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm_mul_su32_dsl ; _mm_mul_su32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t64\n\t0\n\t0\n\t0\n\t0\n )",
                "output_expression": " (_mm_mul_su32_dsl ; _mm_mul_su32\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t64\n\t0\n\t0\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm_add_pi8_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm_add_pi8",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "output_expression": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )"
            }
        }
    ],
    "_mm256_mulhrs_epi16_(2, 3)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm256_mulhrs_epi16",
                "indices": [
                    2,
                    3
                ],
                "input_expression": " (_mm256_mulhrs_epi16_dsl ; _mm256_mulhrs_epi16\n\t(lit (bv #x0000000000000000000000000000000e (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t-1\n\t1\n\t32\n\t1\n\t0\n )",
                "output_expression": " (_mm256_mulhrs_epi16_dsl ; _mm256_mulhrs_epi16\n\t(lit (bv #x0000000000000000000000000000000e (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t-1\n\t1\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "_mm512_fmadd_epi32_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm512_fmadd_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_fmadd_epi32_dsl ; _mm512_fmadd_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n\t64\n\t0\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_mm512_fmadd_epi32_dsl ; _mm512_fmadd_epi32\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n\t64\n\t0\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm_avg_epu8_(2, 3)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm_avg_epu8",
                "indices": [
                    2,
                    3
                ],
                "input_expression": " (_mm_avg_epu8_dsl ; _mm_avg_epu8\n\t(lit (bv #x00000001 (bitvector 8)))\n\t(lit (bv #x00000001 (bitvector 8)))\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t-1\n\t0\n )",
                "output_expression": " (_mm_avg_epu8_dsl ; _mm_avg_epu8\n\t(lit (bv #x00000001 (bitvector 8)))\n\t(lit (bv #x00000001 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t-1\n\t0\n )"
            }
        }
    ],
    "_mm256_and_si256_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm256_and_si256",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "output_expression": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm256_extract_epi8_(0, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm256_extract_epi8",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (_mm256_extract_epi8_dsl ; _mm256_extract_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 0 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 0 x i16> False\n\t5\n\t5\n\t0\n\t5\n\t5\n\t8\n\t0\n\t256\n\t0\n\t0\n )",
                "output_expression": " (_mm256_extract_epi8_dsl ; _mm256_extract_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 0 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 0 x i16> False\n\t5\n\t5\n\t0\n\t5\n\t5\n\t8\n\t0\n\t256\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_mulhi_epu32_(1, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm512_mulhi_epu32",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (_mm512_mulhi_epu32_dsl ; _mm512_mulhi_epu32\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000020 (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_mm512_mulhi_epu32_dsl ; _mm512_mulhi_epu32\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000020 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_and_epi32_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm512_and_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm256_madd52hi_epu64_(1, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm256_madd52hi_epu64",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (_mm256_madd52hi_epu64_dsl ; _mm256_madd52hi_epu64\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t208\n\t52\n\t64\n\t-1\n\t0\n\t52\n\t52\n\t0\n\t128\n\t0\n\t52\n\t0\n )",
                "output_expression": " (_mm256_madd52hi_epu64_dsl ; _mm256_madd52hi_epu64\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t208\n\t52\n\t64\n\t-1\n\t0\n\t52\n\t52\n\t0\n\t128\n\t0\n\t52\n\t0\n )"
            }
        }
    ],
    "_mm_min_epu16_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm_min_epu16",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "output_expression": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "_m_por_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_m_por",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_m_por_dsl ; _m_por\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_m_pcmpeqb_(1, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_m_pcmpeqb",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (_m_pcmpeqb_dsl ; _m_pcmpeqb\n\t(lit (bv #x00000000 (bitvector 8)))\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t(lit (bv #x000000ff (bitvector 8)))\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )",
                "output_expression": " (_m_pcmpeqb_dsl ; _m_pcmpeqb\n\t(lit (bv #x00000000 (bitvector 8)))\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(lit (bv #x000000ff (bitvector 8)))\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )"
            }
        }
    ],
    "_mm256_maddubs_epi16_(1, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "_mm256_maddubs_epi16",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (_mm256_maddubs_epi16_dsl ; _mm_dpwssds_epi32\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (_mm256_maddubs_epi16_dsl ; _mm_dpwssds_epi32\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )"
            }
        }
    ]
}