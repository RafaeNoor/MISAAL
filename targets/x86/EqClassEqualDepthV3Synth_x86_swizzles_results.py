x86_swizzles_EqClassEqualDepthV3Synth={
    " (x86_swizzle_356_dsl ; x86_swizzle_819\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t32\n\t2\n\t0\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(x86_swizzle_356_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 32 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_390_dsl ; x86_swizzle_390\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i32> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i32> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n\t0\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 0 32 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 0 32 0)"
            }
        }
    ],
    " (x86_swizzle_357_dsl ; x86_swizzle_820\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t2\n\t0\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(x86_swizzle_357_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_843_dsl ; x86_swizzle_283\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t0\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(x86_swizzle_843_dsl (reg (bv #x00 8)) 32 32 0 32 16 0)",
                "dst": "(_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 0)"
            }
        }
    ],
    " (x86_swizzle_179_dsl ; x86_swizzle_462\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i32> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t0\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(x86_swizzle_179_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 0)",
                "dst": "(_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 0)"
            }
        }
    ],
    " (x86_swizzle_356_dsl ; x86_swizzle_819\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t32\n\t2\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(x86_swizzle_356_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 8 32 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 8 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_659\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x01 8)) 32 32 0 32 32 0 32) (_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 32) 64 64 0 32 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_390_dsl ; x86_swizzle_390\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i32> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i32> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 0)"
            }
        }
    ],
    " (x86_swizzle_357_dsl ; x86_swizzle_820\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t2\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(x86_swizzle_357_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_404_dsl ; x86_swizzle_404\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i32> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i32> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(x86_swizzle_404_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 32) (_m_from_int_dsl (reg (bv #x01 8)) 32 32 0 32 32 0 32) 32 32 0 32 32 32 0 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_795\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i16> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t64\n\t2\n\t0\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 128 2 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 32 64 1 0) (_mm256_cvtepi64_epi32_dsl (reg (bv #x01 8)) 128 128 0 128 32 64 1 0) 128 128 0 64 16 16 2 64 0) 64 64 0 64 64 0 0)"
            }
        }
    ]
}