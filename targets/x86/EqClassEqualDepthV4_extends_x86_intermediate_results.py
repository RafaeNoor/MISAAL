{
    " (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t32\n\t1\n\t0\n\t0\n )_ (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4_extends",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 8 16 1 0 0)",
                "dst": "(typed:cast-uint-extend (reg (bv #x00 8)) 8 1 16 16)"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm512_cvtepu8_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t32\n\t1\n\t0\n\t0\n )_ (typed:cast-int-extend ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4_extends",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 8 16 1 1 0)",
                "dst": "(typed:cast-int-extend (reg (bv #x00 8)) 8 1 16 16)"
            }
        }
    ]
}
