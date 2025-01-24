{
    " (x86_swizzle_357_dsl ; x86_swizzle_820\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_357_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_357_dsl ; x86_swizzle_218\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t64\n\t16\n\t16\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_357_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_357_dsl ; x86_swizzle_369\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t64\n\t8\n\t8\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_357_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_357_dsl ; x86_swizzle_658\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_357_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_357_dsl ; x86_swizzle_173\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t64\n\t32\n\t32\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_357_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_843_dsl ; x86_swizzle_283\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_843_dsl (reg (bv #x00 8)) 32 32 0 32 16 0)",
                "dst": "(_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 0)"
            }
        }
    ],
    " (x86_swizzle_843_dsl ; x86_swizzle_409\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_843_dsl (reg (bv #x00 8)) 32 32 0 32 16 0)",
                "dst": "(_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 0)"
            }
        }
    ],
    " (x86_swizzle_843_dsl ; x86_swizzle_299\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_843_dsl (reg (bv #x00 8)) 64 64 0 64 16 0)",
                "dst": "(_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_843_dsl ; x86_swizzle_58\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_843_dsl (reg (bv #x00 8)) 64 64 0 64 16 0)",
                "dst": "(_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_843_dsl ; x86_swizzle_271\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_843_dsl (reg (bv #x00 8)) 64 64 0 64 16 0)",
                "dst": "(_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_227_dsl ; x86_swizzle_227\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_227_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0)",
                "dst": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_227_dsl ; x86_swizzle_227\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_227_dsl (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 128 128 0 128 8 0 0)"
            }
        }
    ],
    " (x86_swizzle_227_dsl ; x86_swizzle_227\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_227_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_227_dsl ; x86_swizzle_621\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_227_dsl (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 128 128 0 128 8 0 0)"
            }
        }
    ],
    " (x86_swizzle_227_dsl ; x86_swizzle_621\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_227_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0)",
                "dst": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_227_dsl ; x86_swizzle_621\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_227_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_227_dsl ; x86_swizzle_69\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n )_ (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_227_dsl (reg (bv #x00 8)) 128 128 0 128 16 0 0)",
                "dst": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 128 128 0 128 16 0 0)"
            }
        }
    ],
    " (x86_swizzle_227_dsl ; x86_swizzle_69\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n )_ (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_227_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0)",
                "dst": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_227_dsl ; x86_swizzle_69\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_227_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_227_dsl ; x86_swizzle_325\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_227_dsl (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 128 128 0 128 8 0 0)"
            }
        }
    ],
    " (x86_swizzle_227_dsl ; x86_swizzle_325\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_227_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0)",
                "dst": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_227_dsl ; x86_swizzle_325\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_227_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_356_dsl ; x86_swizzle_23\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t64\n\t8\n\t8\n\t64\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_356_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 16 16 64 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 16 16 2 64 0)"
            }
        }
    ],
    " (x86_swizzle_356_dsl ; x86_swizzle_349\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t64\n\t16\n\t16\n\t64\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_356_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 64 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 2 64 0)"
            }
        }
    ],
    " (x86_swizzle_356_dsl ; x86_swizzle_819\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t32\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_356_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 32 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_356_dsl ; x86_swizzle_172\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t64\n\t32\n\t32\n\t64\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_356_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 64 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 2 64 0)"
            }
        }
    ],
    " (x86_swizzle_356_dsl ; x86_swizzle_657\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t32\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_356_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 16 16 32 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 16 16 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_179_dsl ; x86_swizzle_179\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_179_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0)",
                "dst": "(_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_179_dsl ; x86_swizzle_462\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_179_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 0)",
                "dst": "(_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 0)"
            }
        }
    ],
    " (x86_swizzle_390_dsl ; x86_swizzle_390\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_390_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 0)"
            }
        }
    ],
    " (x86_swizzle_390_dsl ; x86_swizzle_391\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_390_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 0 32 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 0 32 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_622\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )_Reg": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(reg (bv #x00 8))"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_622\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )_ (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_622\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )_ (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_326\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_Reg": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(reg (bv #x00 8))"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_622\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_326\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_326\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_228\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n )_Reg": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(reg (bv #x00 8))"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_326\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_228\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n )_ (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_228\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n )_ (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_228\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_70\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n )_Reg": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(reg (bv #x00 8))"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_70\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n )_ (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_70\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n )_ (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_70\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t64\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_127\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )_Reg": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(reg (bv #x00 8))"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_127\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_127\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_622_dsl ; x86_swizzle_127\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_816\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t64\n\t2\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 8 64 2 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 8 8 2 64 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_816\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t64\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 32 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0) (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 0) 64 64 0 32 16 16 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_266\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t96\n\t2\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 8 64 2 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 8 8 2 64 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_266\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t96\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 8 32 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 0) (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0) 64 64 0 32 8 8 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_817\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t32\n\t2\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 64 2 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 2 64 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_817\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t32\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 32 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0) (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 0) 64 64 0 32 8 8 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_660\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t96\n\t2\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 64 2 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 2 64 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_660\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t96\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 32 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0) (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 0) 64 64 0 32 16 16 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_662\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t32\n\t2\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 64 2 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 2 64 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_662\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t32\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 32 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0) (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 0) 64 64 0 32 8 8 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_661\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t64\n\t2\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 64 2 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 2 64 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_661\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t64\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 32 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0) (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 0) 64 64 0 32 16 16 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_3_dsl ; x86_swizzle_818\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t2\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_3_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 8 2 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 8 8 2 0 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_3_dsl ; x86_swizzle_818\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_3_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0) (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 0) 64 64 0 32 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_3_dsl ; x86_swizzle_663\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_3_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 8 2 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 8 8 2 0 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_3_dsl ; x86_swizzle_663\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_3_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0) (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 0) 64 64 0 32 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_389_dsl ; x86_swizzle_403\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_389_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 32 32 2 0 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_389_dsl ; x86_swizzle_403\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_389_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 0 32 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 0) (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0) 32 32 0 32 32 0 32 0)"
            }
        }
    ],
    " (x86_swizzle_389_dsl ; x86_swizzle_402\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_389_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 32 2 0 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_389_dsl ; x86_swizzle_402\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_389_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 0 32 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 0) (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 0) 32 32 0 32 32 0 32 0)"
            }
        }
    ],
    " (x86_swizzle_504_dsl ; x86_swizzle_11\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t32\n\t8\n\t0\n\t32\n\t8\n\t0\n\t32\n\t8\n\t8\n\t96\n\t4\n\t16\n\t96\n\t4\n\t24\n\t96\n\t4\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_504_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 32 8 0 32 8 0 32 8 8 96 4 16 96 4 24 96 4 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 2 64 0) (_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 64 32 32 2 64 0) 64 64 0 64 64 0 64 0)"
            }
        }
    ],
    " (x86_swizzle_504_dsl ; x86_swizzle_12\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t32\n\t8\n\t0\n\t32\n\t8\n\t0\n\t32\n\t8\n\t8\n\t64\n\t4\n\t16\n\t64\n\t4\n\t24\n\t64\n\t4\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_504_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 32 8 0 32 8 0 32 8 8 32 4 16 32 4 24 32 4 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 64 8 8 2 0 0) (_mm_unpacklo_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 64 32 32 2 0 0) 64 64 0 64 64 0 64 0)"
            }
        }
    ],
    " (x86_swizzle_504_dsl ; x86_swizzle_13\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t32\n\t8\n\t0\n\t32\n\t8\n\t0\n\t32\n\t8\n\t8\n\t32\n\t4\n\t16\n\t32\n\t4\n\t24\n\t32\n\t4\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_504_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 32 8 0 32 8 0 32 8 8 64 4 16 64 4 24 64 4 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 64 8 8 2 64 0) (_mm_unpacklo_pi8_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 64 32 32 2 64 0) 64 64 0 64 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_404_dsl ; x86_swizzle_404\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_404_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 32) (_m_from_int_dsl (reg (bv #x01 8)) 32 32 0 32 32 0 32) 32 32 0 32 32 32 0 0)"
            }
        }
    ],
    " (x86_swizzle_404_dsl ; x86_swizzle_404\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_404_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 32) (_mm512_broadcastq_epi64_dsl (reg (bv #x01 8)) 32 32 0 64 32 0 0) 32 32 0 32 32 32 0 0)"
            }
        }
    ],
    " (x86_swizzle_404_dsl ; x86_swizzle_404\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_404_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x01 8)) 32 32 0 64 32 0 0) (_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 32) 32 32 0 32 32 32 0 0)"
            }
        }
    ],
    " (x86_swizzle_404_dsl ; x86_swizzle_404\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_404_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x01 8)) 32 32 0 64 32 0 0) (_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0) 32 32 0 32 32 32 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_163\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t32\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 64) (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 64) 128 128 0 64 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_163\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t32\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 64) (_mm512_broadcastq_epi64_dsl (reg (bv #x01 8)) 64 64 0 128 64 0 0) 128 128 0 64 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_163\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t32\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 64 64 0 128 64 0 0) (_mm512_broadcastq_epi64_dsl (reg (bv #x01 8)) 64 64 0 128 64 0 0) 128 128 0 64 8 8 2 64 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_163\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t32\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x01 8)) 64 64 0 128 64 0 0) (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 64) 128 128 0 64 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_351\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t16\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 64) (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 64) 128 128 0 64 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_351\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t16\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 64) (_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 64 64 0 128 64 0 0) 128 128 0 64 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_351\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t16\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 64 64 0 128 64 0 0) (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 64) 128 128 0 64 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_351\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t16\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x01 8)) 64 64 0 128 64 0 0) (_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 64 64 0 128 64 0 0) 128 128 0 64 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_659\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 32) (_m_from_int_dsl (reg (bv #x01 8)) 32 32 0 32 32 0 32) 64 64 0 32 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_659\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 32) (_mm512_broadcastq_epi64_dsl (reg (bv #x01 8)) 32 32 0 64 32 0 0) 64 64 0 32 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_659\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0) (_mm512_broadcastq_epi64_dsl (reg (bv #x01 8)) 32 32 0 64 32 0 0) 64 64 0 32 16 16 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_659\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0) (_m_from_int_dsl (reg (bv #x01 8)) 32 32 0 32 32 0 32) 64 64 0 32 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_359\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t8\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 64) (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 64) 128 128 0 64 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_359\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t8\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 32 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 64) (_mm512_broadcastq_epi64_dsl (reg (bv #x01 8)) 64 64 0 128 64 0 0) 128 128 0 64 32 32 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_359\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t8\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 64 64 0 128 64 0 0) (_m_from_int_dsl (reg (bv #x01 8)) 64 64 0 64 64 0 64) 128 128 0 64 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_359\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t8\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x01 8)) 64 64 0 128 64 0 0) (_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 64 64 0 128 64 0 0) 128 128 0 64 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_814\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t16\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x01 8)) 32 32 0 32 32 0 32) (_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 32) 64 64 0 32 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_814\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t16\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 32 32 0 32 32 0 32) (_mm512_broadcastq_epi64_dsl (reg (bv #x01 8)) 32 32 0 64 32 0 0) 64 64 0 32 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_814\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t16\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 16 16 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0) (_mm512_broadcastq_epi64_dsl (reg (bv #x01 8)) 32 32 0 64 32 0 0) 64 64 0 32 16 16 2 32 0)"
            }
        }
    ],
    " (x86_swizzle_445_dsl ; x86_swizzle_814\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t16\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_445_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 8 8 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0) (_m_from_int_dsl (reg (bv #x01 8)) 32 32 0 32 32 0 32) 64 64 0 32 8 8 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_128_dsl ; x86_swizzle_128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t2\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_128_dsl (reg (bv #x00 8)) 128 64 0 64 32 2 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 64 0) 128 128 0 64 32 32 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_128_dsl ; x86_swizzle_128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t2\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_m_from_int_dsl ; _m_from_int\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t )\n\t (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_128_dsl (reg (bv #x00 8)) 128 64 0 64 32 2 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_m_from_int_dsl (reg (bv #x00 8)) 64 64 0 64 64 0 64) (_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 64 0) 128 128 0 64 32 32 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_128_dsl ; x86_swizzle_128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t2\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_128_dsl (reg (bv #x00 8)) 128 64 0 64 32 2 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0) (reg (bv #x00 8)) 128 128 0 64 32 32 2 64 0)"
            }
        }
    ],
    " (x86_swizzle_128_dsl ; x86_swizzle_128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t2\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t512\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_128_dsl (reg (bv #x00 8)) 128 64 0 64 32 2 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 128 128 0 128 64 0 0) (_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 64 0) 128 128 0 64 32 32 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_128_dsl ; x86_swizzle_128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t2\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t2\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_128_dsl (reg (bv #x00 8)) 128 64 0 64 32 2 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0) (reg (bv #x00 8)) 128 128 0 64 32 32 2 64 0)"
            }
        }
    ],
    " (x86_swizzle_128_dsl ; x86_swizzle_128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t2\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t2\n\t\t32\n\t\t0\n\t )\n\t (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_128_dsl (reg (bv #x00 8)) 128 64 0 64 32 2 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0) (_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 64 0) 128 128 0 64 32 32 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_128_dsl ; x86_swizzle_128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t2\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_128_dsl (reg (bv #x00 8)) 128 64 0 64 32 2 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 64 0 0) (reg (bv #x00 8)) 128 128 0 64 32 32 2 64 0)"
            }
        }
    ],
    " (x86_swizzle_128_dsl ; x86_swizzle_128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t2\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_128_dsl (reg (bv #x00 8)) 128 64 0 64 32 2 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 64 0 0) (_mm_unpacklo_pi32_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 64 0) 128 128 0 64 32 32 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_379_dsl ; x86_swizzle_401\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t64\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_379_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 64 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 32 32 2 64 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_379_dsl ; x86_swizzle_400\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t96\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_379_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 32 0 64 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 32 32 2 64 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_506_dsl ; x86_swizzle_14\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t32\n\t8\n\t0\n\t32\n\t8\n\t0\n\t32\n\t8\n\t8\n\t4\n\t16\n\t4\n\t24\n\t4\n\t0\n )_ (_mm_unpacklo_pi32_dsl ; _mm_unpacklo_pi32\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_506_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 32 8 0 32 8 0 32 8 8 4 16 4 24 4 0)",
                "dst": "(_mm_unpacklo_pi32_dsl (_mm_unpacklo_pi8_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 64 8 8 2 0 0) (_mm_unpacklo_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 32 2 0 0) 64 64 0 64 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_795\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t64\n\t2\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t\t128\n\t\t\t128\n\t\t\t0\n\t\t\t128\n\t\t\t32\n\t\t\t64\n\t\t\t1\n\t\t\t0\n\t\t )\n\t\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t128\n\t\t\t128\n\t\t\t0\n\t\t\t128\n\t\t\t32\n\t\t\t64\n\t\t\t1\n\t\t\t0\n\t\t )\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 8 128 2 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (_mm256_cvtepi64_epi32_dsl (reg (bv #x01 8)) 128 128 0 128 32 64 1 0) (_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 32 64 1 0) 128 128 0 64 8 8 2 64 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_176\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t128\n\t128\n\t0\n\t64\n\t32\n\t32\n\t64\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t (_mm256_unpackhi_epi16_dsl ; _mm256_unpackhi_epi16\n\t\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t256\n\t\t\t128\n\t\t\t0\n\t\t\t64\n\t\t\t16\n\t\t\t16\n\t\t\t2\n\t\t\t64\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t (_mm256_unpackhi_epi16_dsl ; _mm256_unpackhi_epi16\n\t\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t\t256\n\t\t\t128\n\t\t\t0\n\t\t\t64\n\t\t\t16\n\t\t\t16\n\t\t\t2\n\t\t\t64\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 16 16 64 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm256_cvtepi64_epi32_dsl (_mm256_unpackhi_epi16_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 256 128 0 64 32 32 2 64 0) 128 128 0 128 32 64 1 0) (_mm256_cvtepi64_epi32_dsl (_mm256_unpackhi_epi16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 128 0 64 8 8 2 64 0) 128 128 0 128 8 16 1 0) 128 128 0 64 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_176\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t128\n\t128\n\t0\n\t64\n\t32\n\t32\n\t64\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t (_mm512_unpacklo_epi16_dsl ; _mm512_unpacklo_epi16\n\t\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t512\n\t\t\t128\n\t\t\t0\n\t\t\t64\n\t\t\t16\n\t\t\t16\n\t\t\t2\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t (_mm512_unpacklo_epi16_dsl ; _mm512_unpacklo_epi16\n\t\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t\t512\n\t\t\t128\n\t\t\t0\n\t\t\t64\n\t\t\t16\n\t\t\t16\n\t\t\t2\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 64 8 8 128 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm256_cvtepi64_epi32_dsl (_mm512_unpacklo_epi16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 128 0 64 8 8 2 0) 128 128 0 128 8 16 1 0) (_mm256_cvtepi64_epi32_dsl (_mm512_unpacklo_epi16_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 256 128 0 64 16 16 2 0) 128 128 0 128 16 32 1 0) 128 128 0 64 8 8 2 64 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_651\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t160\n\t2\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t\t128\n\t\t\t128\n\t\t\t0\n\t\t\t128\n\t\t\t32\n\t\t\t64\n\t\t\t1\n\t\t\t0\n\t\t )\n\t\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t128\n\t\t\t128\n\t\t\t0\n\t\t\t128\n\t\t\t32\n\t\t\t64\n\t\t\t1\n\t\t\t0\n\t\t )\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 128 2 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 32 64 1 0) (_mm256_cvtepi64_epi32_dsl (reg (bv #x01 8)) 128 128 0 128 32 64 1 0) 128 128 0 64 16 16 2 64 0) 64 64 0 64 64 0 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_346\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t128\n\t128\n\t0\n\t64\n\t16\n\t16\n\t128\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t (_mm256_unpackhi_epi16_dsl ; _mm256_unpackhi_epi16\n\t\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t256\n\t\t\t128\n\t\t\t0\n\t\t\t64\n\t\t\t16\n\t\t\t16\n\t\t\t2\n\t\t\t64\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t (_mm256_unpackhi_epi16_dsl ; _mm256_unpackhi_epi16\n\t\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t\t256\n\t\t\t128\n\t\t\t0\n\t\t\t64\n\t\t\t16\n\t\t\t16\n\t\t\t2\n\t\t\t64\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 16 16 64 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm256_cvtepi64_epi32_dsl (_mm256_unpackhi_epi16_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 256 128 0 64 8 8 2 64 0) 128 128 0 128 8 16 1 0) (_mm256_cvtepi64_epi32_dsl (_mm256_unpackhi_epi16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 128 0 64 32 32 2 64 0) 128 128 0 128 32 64 1 0) 128 128 0 64 16 16 2 0 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_346\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t128\n\t128\n\t0\n\t64\n\t16\n\t16\n\t128\n\t2\n\t0\n )_ (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t (_mm512_unpacklo_epi16_dsl ; _mm512_unpacklo_epi16\n\t\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t512\n\t\t\t128\n\t\t\t0\n\t\t\t64\n\t\t\t16\n\t\t\t16\n\t\t\t2\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t (_mm512_unpacklo_epi16_dsl ; _mm512_unpacklo_epi16\n\t\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t\t512\n\t\t\t128\n\t\t\t0\n\t\t\t64\n\t\t\t16\n\t\t\t16\n\t\t\t2\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t32\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 16 16 128 2 0)",
                "dst": "(_mm_unpacklo_pi8_dsl (_mm256_cvtepi64_epi32_dsl (_mm512_unpacklo_epi16_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 256 128 0 64 32 32 2 0) 128 128 0 128 32 64 1 0) (_mm256_cvtepi64_epi32_dsl (_mm512_unpacklo_epi16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 128 0 64 16 16 2 0) 128 128 0 128 16 32 1 0) 128 128 0 64 16 16 2 64 0)"
            }
        }
    ],
    " (x86_swizzle_499_dsl ; x86_swizzle_258\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t224\n\t2\n\t0\n )_ (_m_from_int_dsl ; _m_from_int\n\t (_mm_unpacklo_pi8_dsl ; _mm_unpacklo_pi8\n\t\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t\t128\n\t\t\t128\n\t\t\t0\n\t\t\t128\n\t\t\t32\n\t\t\t64\n\t\t\t1\n\t\t\t0\n\t\t )\n\t\t (_mm256_cvtepi64_epi32_dsl ; _mm256_cvtepi64_epi32\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t128\n\t\t\t128\n\t\t\t0\n\t\t\t128\n\t\t\t32\n\t\t\t64\n\t\t\t1\n\t\t\t0\n\t\t )\n\t\t64\n\t\t64\n\t\t0\n\t\t32\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(x86_swizzle_499_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 8 128 2 0)",
                "dst": "(_m_from_int_dsl (_mm_unpacklo_pi8_dsl (_mm256_cvtepi64_epi32_dsl (reg (bv #x01 8)) 128 128 0 128 32 64 1 0) (_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 32 64 1 0) 128 128 0 64 8 8 2 64 0) 64 64 0 64 64 0 0)"
            }
        }
    ]
}