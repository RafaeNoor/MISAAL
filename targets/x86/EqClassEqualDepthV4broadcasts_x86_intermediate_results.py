{
    " (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t0\n )_ (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 0 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)"
            }
        }
    ],
    " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )_ (x86_swizzle_622_dsl ; x86_swizzle_622\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4broadcasts",
            "property": {
                "src": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)",
                "dst": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t0\n )_ (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 0 0)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32 2)"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm512_broadcastq_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t512\n\t64\n\t0\n\t0\n )_ (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t0\n\t1\n\t32\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 8 1 8 8 128)"
            }
        }
    ],
    " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )_ (x86_swizzle_622_dsl ; x86_swizzle_622\n\t (x86_swizzle_622_dsl ; x86_swizzle_622\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4broadcasts",
            "property": {
                "src": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)",
                "dst": "(x86_swizzle_622_dsl (x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0) 128 64 0 64 32 0)"
            }
        }
    ]
}