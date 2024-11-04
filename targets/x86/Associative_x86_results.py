{
    "_mm512_or_epi32_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "_mm512_or_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm256_xor_epi32_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "_mm256_xor_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "output_expression": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm_add_si64_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "_mm_add_si64",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm_add_si64_dsl ; _mm_add_si64\n\t (_mm_add_si64_dsl ; _mm_add_si64\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )",
                "output_expression": " (_mm_add_si64_dsl ; _mm_add_si64\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t (_mm_add_si64_dsl ; _mm_add_si64\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm256_xor_si256_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "_mm256_xor_si256",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "output_expression": " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm256_max_epu64_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "_mm256_max_epu64",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm_add_pi8_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "_mm_add_pi8",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "output_expression": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )"
            }
        }
    ],
    "_mm256_and_si256_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "_mm256_and_si256",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "output_expression": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm_min_epu16_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "_mm_min_epu16",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "output_expression": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_and_epi32_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "_mm512_and_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_m_por_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "_m_por",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_m_por_dsl ; _m_por\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )"
            }
        }
    ]
}
