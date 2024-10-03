x86_Distributive={
    "_mm512_or_epi32+_mm512_or_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_or_epi32_mm512_or_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_or_epi32+_mm512_and_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_or_epi32_mm512_and_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_unpacklo_epi64+_mm512_or_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_unpacklo_epi64_mm512_or_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_unpacklo_epi64_dsl ; _mm512_unpacklo_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t256\n\t64\n\t64\n\t0\n\t0\n\t2\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_unpacklo_epi64_dsl ; _mm512_unpacklo_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t256\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t\t2\n\t\t0\n\t )\n\t (_mm512_unpacklo_epi64_dsl ; _mm512_unpacklo_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t256\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t\t2\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_unpacklo_epi64+_mm512_and_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_unpacklo_epi64_mm512_and_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_unpacklo_epi64_dsl ; _mm512_unpacklo_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t256\n\t64\n\t64\n\t0\n\t0\n\t2\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_unpacklo_epi64_dsl ; _mm512_unpacklo_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t256\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t\t2\n\t\t0\n\t )\n\t (_mm512_unpacklo_epi64_dsl ; _mm512_unpacklo_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t256\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t\t2\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm256_max_epu64+_mm256_max_epu64+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_max_epu64_mm256_max_epu64",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm_unpacklo_pi32+_m_por+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm_unpacklo_pi32_m_por",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )",
                "output_expression": " (_m_por_dsl ; _m_por\n\t (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_srav_epi16+_mm512_or_epi32+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_srav_epi16_mm512_or_epi32",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (_mm512_srav_epi16_dsl ; _mm512_srav_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(lit (bv #x000000000000ffff (bitvector 16)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t1\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_srav_epi16_dsl ; _mm512_srav_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000ffff (bitvector 16)))\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t (_mm512_srav_epi16_dsl ; _mm512_srav_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000ffff (bitvector 16)))\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_srav_epi16+_mm512_andnot_epi32+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_srav_epi16_mm512_andnot_epi32",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (_mm512_srav_epi16_dsl ; _mm512_srav_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(lit (bv #x000000000000ffff (bitvector 16)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t1\n\t0\n )",
                "output_expression": " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t (_mm512_srav_epi16_dsl ; _mm512_srav_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000ffff (bitvector 16)))\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t (_mm512_srav_epi16_dsl ; _mm512_srav_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000ffff (bitvector 16)))\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_srav_epi16+_mm512_and_epi32+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_srav_epi16_mm512_and_epi32",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (_mm512_srav_epi16_dsl ; _mm512_srav_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(lit (bv #x000000000000ffff (bitvector 16)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t1\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_srav_epi16_dsl ; _mm512_srav_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000ffff (bitvector 16)))\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t (_mm512_srav_epi16_dsl ; _mm512_srav_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000ffff (bitvector 16)))\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm_unpacklo_pi8+_m_por+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm_unpacklo_pi8_m_por",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )",
                "output_expression": " (_m_por_dsl ; _m_por\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm_mul_su32+_m_psrld+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm_mul_su32_m_psrld",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm_mul_su32_dsl ; _mm_mul_su32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t (_m_psrld_dsl ; _m_psrld\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t64\n\t\t0\n\t\t32\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t64\n\t0\n\t0\n\t0\n\t0\n )",
                "output_expression": " (_m_psrld_dsl ; _m_psrld\n\t (_mm_mul_su32_dsl ; _mm_mul_su32\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t\t0\n\t\t0\n\t )\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t (_mm_mul_su32_dsl ; _mm_mul_su32\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_sll_epi64+_mm512_or_epi32+(1, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_sll_epi64_mm512_or_epi32",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (_mm512_sll_epi64_dsl ; _mm512_sll_epi64\n\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000003f (bitvector 64)))\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t64\n\t0\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_sll_epi64_dsl ; _mm512_sll_epi64\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000003f (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm512_sll_epi64_dsl ; _mm512_sll_epi64\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000003f (bitvector 64)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm_sign_pi16+_m_por+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm_sign_pi16_m_por",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (_mm_sign_pi16_dsl ; _mm_sign_pi16\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t(reg (bv 3 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t16\n\t16\n\t16\n\t0\n )",
                "output_expression": " (_m_por_dsl ; _m_por\n\t (_mm_sign_pi16_dsl ; _mm_sign_pi16\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t1\n\t\t16\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t (_mm_sign_pi16_dsl ; _mm_sign_pi16\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t1\n\t\t16\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_sll_epi64+_mm512_and_epi32+(1, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_sll_epi64_mm512_and_epi32",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (_mm512_sll_epi64_dsl ; _mm512_sll_epi64\n\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000003f (bitvector 64)))\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t64\n\t0\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_sll_epi64_dsl ; _mm512_sll_epi64\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000003f (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm512_sll_epi64_dsl ; _mm512_sll_epi64\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000003f (bitvector 64)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm_sign_pi16+_m_psrld+(1, 4)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm_sign_pi16_m_psrld",
                "indices": [
                    1,
                    4
                ],
                "input_expression": " (_mm_sign_pi16_dsl ; _mm_sign_pi16\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (_m_psrld_dsl ; _m_psrld\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t64\n\t\t0\n\t\t32\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t16\n\t16\n\t16\n\t0\n )",
                "output_expression": " (_m_psrld_dsl ; _m_psrld\n\t (_mm_sign_pi16_dsl ; _mm_sign_pi16\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t1\n\t\t16\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t (_mm_sign_pi16_dsl ; _mm_sign_pi16\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t16\n\t\t1\n\t\t16\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm256_mulhrs_epi16+_mm256_blend_epi16+(2, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_mulhrs_epi16_mm256_blend_epi16",
                "indices": [
                    2,
                    3
                ],
                "input_expression": " (_mm256_mulhrs_epi16_dsl ; _mm256_mulhrs_epi16\n\t(lit (bv #x0000000000000000000000000000000e (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t16\n\t\t1\n\t\t8\n\t\t16\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t-1\n\t1\n\t32\n\t1\n\t0\n )",
                "output_expression": " (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (_mm256_mulhrs_epi16_dsl ; _mm256_mulhrs_epi16\n\t\t(lit (bv #x0000000000000000000000000000000e (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t16\n\t\t1\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t (_mm256_mulhrs_epi16_dsl ; _mm256_mulhrs_epi16\n\t\t(lit (bv #x0000000000000000000000000000000e (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t16\n\t\t1\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t8\n\t16\n\t0\n )"
            }
        }
    ],
    "_mm256_mulhrs_epi16+_mm_movm_epi8+(2, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_mulhrs_epi16_mm_movm_epi8",
                "indices": [
                    2,
                    3
                ],
                "input_expression": " (_mm256_mulhrs_epi16_dsl ; _mm256_mulhrs_epi16\n\t(lit (bv #x0000000000000000000000000000000e (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t1\n\t\t64\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t-1\n\t1\n\t32\n\t1\n\t0\n )",
                "output_expression": " (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (_mm256_mulhrs_epi16_dsl ; _mm256_mulhrs_epi16\n\t\t(lit (bv #x0000000000000000000000000000000e (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t16\n\t\t1\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t (_mm256_mulhrs_epi16_dsl ; _mm256_mulhrs_epi16\n\t\t(lit (bv #x0000000000000000000000000000000e (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t16\n\t\t1\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t1\n\t64\n\t0\n )"
            }
        }
    ],
    "_mm512_unpacklo_epi16+_mm512_or_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_unpacklo_epi16_mm512_or_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_unpacklo_epi16_dsl ; _mm512_unpacklo_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t128\n\t0\n\t64\n\t16\n\t16\n\t2\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_unpacklo_epi16_dsl ; _mm512_unpacklo_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t128\n\t\t0\n\t\t64\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (_mm512_unpacklo_epi16_dsl ; _mm512_unpacklo_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t128\n\t\t0\n\t\t64\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_unpacklo_epi16+_mm512_and_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_unpacklo_epi16_mm512_and_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_unpacklo_epi16_dsl ; _mm512_unpacklo_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t128\n\t0\n\t64\n\t16\n\t16\n\t2\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_unpacklo_epi16_dsl ; _mm512_unpacklo_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t128\n\t\t0\n\t\t64\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (_mm512_unpacklo_epi16_dsl ; _mm512_unpacklo_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t128\n\t\t0\n\t\t64\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_fmadd_epi32+_mm512_fmadd_epi32+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_fmadd_epi32_mm512_fmadd_epi32",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (_mm512_fmadd_epi32_dsl ; _mm512_fmadd_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_fmadd_epi32_dsl ; _mm512_fmadd_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t-1\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n\t64\n\t0\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_mm512_fmadd_epi32_dsl ; _mm512_fmadd_epi32\n\t (_mm512_fmadd_epi32_dsl ; _mm512_fmadd_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t-1\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm512_fmadd_epi32_dsl ; _mm512_fmadd_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t-1\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n\t64\n\t0\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_fmadd_epi32+_mm512_fmadd_epi32+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_fmadd_epi32_mm512_fmadd_epi32",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (_mm512_fmadd_epi32_dsl ; _mm512_fmadd_epi32\n\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_fmadd_epi32_dsl ; _mm512_fmadd_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t-1\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n\t64\n\t0\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_mm512_fmadd_epi32_dsl ; _mm512_fmadd_epi32\n\t (_mm512_fmadd_epi32_dsl ; _mm512_fmadd_epi32\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t-1\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm512_fmadd_epi32_dsl ; _mm512_fmadd_epi32\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t-1\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n\t64\n\t0\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm256_unpackhi_epi16+_mm256_and_si256+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_unpackhi_epi16_mm256_and_si256",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_unpackhi_epi16_dsl ; _mm256_unpackhi_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t128\n\t0\n\t64\n\t16\n\t16\n\t2\n\t64\n\t0\n )",
                "output_expression": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t (_mm256_unpackhi_epi16_dsl ; _mm256_unpackhi_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t128\n\t\t0\n\t\t64\n\t\t16\n\t\t16\n\t\t2\n\t\t64\n\t\t0\n\t )\n\t (_mm256_unpackhi_epi16_dsl ; _mm256_unpackhi_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t128\n\t\t0\n\t\t64\n\t\t16\n\t\t16\n\t\t2\n\t\t64\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_sllv_epi16+_mm512_or_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_sllv_epi16_mm512_or_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_sllv_epi16+_mm512_and_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_sllv_epi16_mm512_and_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_sllv_epi16+_mm512_or_epi32+(0, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_sllv_epi16_mm512_or_epi32",
                "indices": [
                    0,
                    3
                ],
                "input_expression": " (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_sllv_epi16+_mm512_and_epi32+(0, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_sllv_epi16_mm512_and_epi32",
                "indices": [
                    0,
                    3
                ],
                "input_expression": " (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_sllv_epi16+_mm512_andnot_epi32+(0, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_sllv_epi16_mm512_andnot_epi32",
                "indices": [
                    0,
                    3
                ],
                "input_expression": " (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t0\n )",
                "output_expression": " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_sllv_epi16+_mm512_or_epi32+(1, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_sllv_epi16_mm512_or_epi32",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_sllv_epi16+_mm512_and_epi32+(1, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_sllv_epi16_mm512_and_epi32",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t (_mm512_sllv_epi16_dsl ; _mm512_sllv_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm256_and_si256+_mm256_xor_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_and_si256_mm256_xor_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "output_expression": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm256_and_si256+_mm256_xor_si256+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_and_si256_mm256_xor_si256",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "output_expression": " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm256_and_si256+_mm256_and_si256+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_and_si256_mm256_and_si256",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "output_expression": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm256_madd52hi_epu64+_mm256_dpbusd_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_madd52hi_epu64_mm256_dpbusd_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm256_madd52hi_epu64_dsl ; _mm256_madd52hi_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_dpbusd_epi32_dsl ; _mm256_dpbusd_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t32\n\t\t0\n\t\t32\n\t\t8\n\t\t-1\n\t\t1\n\t\t1\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t208\n\t52\n\t64\n\t-1\n\t0\n\t52\n\t52\n\t0\n\t128\n\t0\n\t52\n\t0\n )",
                "output_expression": " (_mm256_dpbusd_epi32_dsl ; _mm256_dpbusd_epi32\n\t (_mm256_madd52hi_epu64_dsl ; _mm256_madd52hi_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t208\n\t\t52\n\t\t64\n\t\t-1\n\t\t0\n\t\t52\n\t\t52\n\t\t0\n\t\t128\n\t\t0\n\t\t52\n\t\t0\n\t )\n\t (_mm256_madd52hi_epu64_dsl ; _mm256_madd52hi_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t208\n\t\t52\n\t\t64\n\t\t-1\n\t\t0\n\t\t52\n\t\t52\n\t\t0\n\t\t128\n\t\t0\n\t\t52\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm_min_epu16+_mm_min_epu16+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm_min_epu16_mm_min_epu16",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "output_expression": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm_andnot_si128+_mm_andnot_si128+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm_andnot_si128_mm_andnot_si128",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm_andnot_si128_dsl ; _mm_andnot_si128\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t (_mm_andnot_si128_dsl ; _mm_andnot_si128\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t128\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t128\n\t0\n\t0\n )",
                "output_expression": " (_mm_andnot_si128_dsl ; _mm_andnot_si128\n\t (_mm_andnot_si128_dsl ; _mm_andnot_si128\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t128\n\t\t0\n\t\t0\n\t )\n\t (_mm_andnot_si128_dsl ; _mm_andnot_si128\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t128\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t128\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_and_epi32+_mm512_or_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_and_epi32_mm512_or_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_and_epi32+_mm512_and_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_and_epi32_mm512_and_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_and_epi32+_mm512_andnot_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_and_epi32_mm512_andnot_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "output_expression": " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_andnot_epi32+_mm512_or_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_andnot_epi32_mm512_or_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_m_pslld+_m_por+(1, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_m_pslld_m_por",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (_m_pslld_dsl ; _m_pslld\n\t(reg (bv 3 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_m_por_dsl ; _m_por\n\t (_m_pslld_dsl ; _m_pslld\n\t\t(reg (bv 3 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t64\n\t\t0\n\t\t32\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_m_pslld_dsl ; _m_pslld\n\t\t(reg (bv 3 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t64\n\t\t0\n\t\t32\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_andnot_epi32+_mm512_andnot_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_andnot_epi32_mm512_andnot_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "output_expression": " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_andnot_epi32+_mm512_and_epi32+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_andnot_epi32_mm512_and_epi32",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t (_mm512_andnot_epi32_dsl ; _mm512_andnot_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_m_psrld+_m_por+(1, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_m_psrld_m_por",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (_m_psrld_dsl ; _m_psrld\n\t(reg (bv 3 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_m_por_dsl ; _m_por\n\t (_m_psrld_dsl ; _m_psrld\n\t\t(reg (bv 3 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t64\n\t\t0\n\t\t32\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_m_psrld_dsl ; _m_psrld\n\t\t(reg (bv 3 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000001f (bitvector 64)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t\t64\n\t\t0\n\t\t32\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_srli_epi16+_mm512_and_epi32+(1, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_srli_epi16_mm512_and_epi32",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (_mm512_srli_epi16_dsl ; _mm512_srli_epi16\n\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x0000000f (bitvector 8)))\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t8\n\t8\n\t0\n\t256\n\t8\n\t0\n\t8\n\t0\n\t16\n\t1\n\t1\n\t0\n\t8\n\t0\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_srli_epi16_dsl ; _mm512_srli_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000f (bitvector 8)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t8\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t1\n\t\t0\n\t\t8\n\t\t0\n\t\t0\n\t )\n\t (_mm512_srli_epi16_dsl ; _mm512_srli_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000f (bitvector 8)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t8\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t1\n\t\t0\n\t\t8\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_srli_epi16+_mm512_or_epi32+(1, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_srli_epi16_mm512_or_epi32",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (_mm512_srli_epi16_dsl ; _mm512_srli_epi16\n\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x0000000f (bitvector 8)))\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t8\n\t8\n\t0\n\t256\n\t8\n\t0\n\t8\n\t0\n\t16\n\t1\n\t1\n\t0\n\t8\n\t0\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_srli_epi16_dsl ; _mm512_srli_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000f (bitvector 8)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t8\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t1\n\t\t0\n\t\t8\n\t\t0\n\t\t0\n\t )\n\t (_mm512_srli_epi16_dsl ; _mm512_srli_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000f (bitvector 8)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t8\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t1\n\t\t0\n\t\t8\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_slli_epi16+_mm512_or_epi32+(1, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_slli_epi16_mm512_or_epi32",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (_mm512_slli_epi16_dsl ; _mm512_slli_epi16\n\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x0000000f (bitvector 8)))\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t8\n\t8\n\t0\n\t256\n\t8\n\t0\n\t8\n\t0\n\t16\n\t1\n\t1\n\t0\n\t8\n\t0\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_slli_epi16_dsl ; _mm512_slli_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000f (bitvector 8)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t8\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t1\n\t\t0\n\t\t8\n\t\t0\n\t\t0\n\t )\n\t (_mm512_slli_epi16_dsl ; _mm512_slli_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000f (bitvector 8)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t8\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t1\n\t\t0\n\t\t8\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm512_slli_epi16+_mm512_and_epi32+(1, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_slli_epi16_mm512_and_epi32",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (_mm512_slli_epi16_dsl ; _mm512_slli_epi16\n\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x0000000f (bitvector 8)))\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t8\n\t8\n\t0\n\t256\n\t8\n\t0\n\t8\n\t0\n\t16\n\t1\n\t1\n\t0\n\t8\n\t0\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_slli_epi16_dsl ; _mm512_slli_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000f (bitvector 8)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t8\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t1\n\t\t0\n\t\t8\n\t\t0\n\t\t0\n\t )\n\t (_mm512_slli_epi16_dsl ; _mm512_slli_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x0000000f (bitvector 8)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t8\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t1\n\t\t0\n\t\t8\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_m_por+_m_por+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_m_por_m_por",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_m_por_dsl ; _m_por\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 4 x i16> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm256_blendv_epi8+_mm_movm_epi8+(2, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_blendv_epi8_mm_movm_epi8",
                "indices": [
                    2,
                    3
                ],
                "input_expression": " (_mm256_blendv_epi8_dsl ; _mm256_blendv_epi8\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t\t(reg (bv 4 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t1\n\t\t64\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t7\n\t0\n )",
                "output_expression": " (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t(reg (bv 4 (bitvector 8))) ; < 0 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (_mm256_blendv_epi8_dsl ; _mm256_blendv_epi8\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t8\n\t\t1\n\t\t7\n\t\t0\n\t )\n\t (_mm256_blendv_epi8_dsl ; _mm256_blendv_epi8\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t8\n\t\t1\n\t\t7\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t1\n\t64\n\t0\n )"
            }
        }
    ],
    "_mm256_blendv_epi8+_mm256_blend_epi16+(2, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_blendv_epi8_mm256_blend_epi16",
                "indices": [
                    2,
                    3
                ],
                "input_expression": " (_mm256_blendv_epi8_dsl ; _mm256_blendv_epi8\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t\t(reg (bv 4 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t16\n\t\t1\n\t\t8\n\t\t16\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t7\n\t0\n )",
                "output_expression": " (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t(reg (bv 4 (bitvector 8))) ; < 0 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (_mm256_blendv_epi8_dsl ; _mm256_blendv_epi8\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t8\n\t\t1\n\t\t7\n\t\t0\n\t )\n\t (_mm256_blendv_epi8_dsl ; _mm256_blendv_epi8\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t8\n\t\t1\n\t\t7\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t8\n\t16\n\t0\n )"
            }
        }
    ],
    "_mm256_blendv_epi8+_mm256_and_si256+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_blendv_epi8_mm256_and_si256",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (_mm256_blendv_epi8_dsl ; _mm256_blendv_epi8\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t7\n\t0\n )",
                "output_expression": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t (_mm256_blendv_epi8_dsl ; _mm256_blendv_epi8\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t8\n\t\t1\n\t\t7\n\t\t0\n\t )\n\t (_mm256_blendv_epi8_dsl ; _mm256_blendv_epi8\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t8\n\t\t1\n\t\t7\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm256_blendv_epi8+_mm256_and_si256+(1, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_blendv_epi8_mm256_and_si256",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (_mm256_blendv_epi8_dsl ; _mm256_blendv_epi8\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t7\n\t0\n )",
                "output_expression": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t (_mm256_blendv_epi8_dsl ; _mm256_blendv_epi8\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t8\n\t\t1\n\t\t7\n\t\t0\n\t )\n\t (_mm256_blendv_epi8_dsl ; _mm256_blendv_epi8\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t8\n\t\t1\n\t\t7\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm512_srl_epi64+_mm512_or_epi32+(1, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_srl_epi64_mm512_or_epi32",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (_mm512_srl_epi64_dsl ; _mm512_srl_epi64\n\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000003f (bitvector 64)))\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t64\n\t0\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_srl_epi64_dsl ; _mm512_srl_epi64\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000003f (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm512_srl_epi64_dsl ; _mm512_srl_epi64\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000003f (bitvector 64)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm256_blend_epi16+_mm256_blend_epi16+(2, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_blend_epi16_mm256_blend_epi16",
                "indices": [
                    2,
                    3
                ],
                "input_expression": " (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t\t(reg (bv 4 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t16\n\t\t1\n\t\t8\n\t\t16\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t8\n\t16\n\t0\n )",
                "output_expression": " (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t(reg (bv 4 (bitvector 8))) ; < 0 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t16\n\t\t1\n\t\t8\n\t\t16\n\t\t0\n\t )\n\t (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t16\n\t\t1\n\t\t8\n\t\t16\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t8\n\t16\n\t0\n )"
            }
        }
    ],
    "_mm256_blend_epi16+_mm_movm_epi8+(2, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm256_blend_epi16_mm_movm_epi8",
                "indices": [
                    2,
                    3
                ],
                "input_expression": " (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t\t(reg (bv 4 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t1\n\t\t64\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t8\n\t16\n\t0\n )",
                "output_expression": " (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t(reg (bv 4 (bitvector 8))) ; < 0 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t16\n\t\t1\n\t\t8\n\t\t16\n\t\t0\n\t )\n\t (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t16\n\t\t1\n\t\t8\n\t\t16\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t1\n\t64\n\t0\n )"
            }
        }
    ],
    "_mm512_srl_epi64+_mm512_and_epi32+(1, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm512_srl_epi64_mm512_and_epi32",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (_mm512_srl_epi64_dsl ; _mm512_srl_epi64\n\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000003f (bitvector 64)))\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t64\n\t0\n\t64\n\t0\n\t0\n )",
                "output_expression": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_srl_epi64_dsl ; _mm512_srl_epi64\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000003f (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm512_srl_epi64_dsl ; _mm512_srl_epi64\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i16> False\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000003f (bitvector 64)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )"
            }
        }
    ],
    "_mm_movm_epi8+_mm_movm_epi8+(2, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm_movm_epi8_mm_movm_epi8",
                "indices": [
                    2,
                    3
                ],
                "input_expression": " (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t\t(reg (bv 4 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t1\n\t\t64\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t1\n\t64\n\t0\n )",
                "output_expression": " (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t(reg (bv 4 (bitvector 8))) ; < 0 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t1\n\t\t64\n\t\t0\n\t )\n\t (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t1\n\t\t64\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t1\n\t64\n\t0\n )"
            }
        }
    ],
    "_mm_movm_epi8+_mm256_blend_epi16+(2, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm_movm_epi8_mm256_blend_epi16",
                "indices": [
                    2,
                    3
                ],
                "input_expression": " (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t\t(reg (bv 4 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t16\n\t\t1\n\t\t8\n\t\t16\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t1\n\t64\n\t0\n )",
                "output_expression": " (_mm256_blend_epi16_dsl ; _mm256_blend_epi16\n\t(reg (bv 4 (bitvector 8))) ; < 0 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t1\n\t\t64\n\t\t0\n\t )\n\t (_mm_movm_epi8_dsl ; _mm256_mask_blend_epi64\n\t\t(reg (bv 3 (bitvector 8))) ; < 0 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i16> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t1\n\t\t64\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t8\n\t16\n\t0\n )"
            }
        }
    ],
    "_mm_srlv_epi32+_mm_min_epu16+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm_srlv_epi32_mm_min_epu16",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )",
                "output_expression": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t )\n\t (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "_mm_srlv_epi32+_mm_andnot_si128+(0, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "_mm_srlv_epi32_mm_andnot_si128",
                "indices": [
                    0,
                    3
                ],
                "input_expression": " (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t (_mm_andnot_si128_dsl ; _mm_andnot_si128\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t128\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t32\n\t32\n\t0\n )",
                "output_expression": " (_mm_andnot_si128_dsl ; _mm_andnot_si128\n\t (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t )\n\t (_mm_srlv_epi32_dsl ; _mm_srlv_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 128)))\n\t\t(lit (bv #x00000000000000000000000000000020 (bitvector 32)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t128\n\t0\n\t0\n )"
            }
        }
    ]
}