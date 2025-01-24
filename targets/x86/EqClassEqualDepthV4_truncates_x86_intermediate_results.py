{
    " (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t64\n\t1\n\t0\n )_ (typed:cast-uint-truncate ; typed:cast-uint_1_ip16_is1024_op8_os512_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1\n\t64\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4_truncates",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0)",
                "dst": "(typed:cast-uint-truncate (reg (bv #x00 8)) 64 1 8 32)"
            }
        }
    ],
    " (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t64\n\t1\n\t0\n )_ (typed:cast-int-truncate ; typed:cast-int_1_ip16_is1024_op8_os512_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1\n\t64\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4_truncates",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0)",
                "dst": "(typed:cast-int-truncate (reg (bv #x00 8)) 64 1 8 32)"
            }
        }
    ]
}