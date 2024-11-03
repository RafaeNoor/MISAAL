{
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )+64+_mm_set1_pi32+typed:xBroadcast_is32_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 2)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )",
                "src_ctx": "_mm_set1_pi32",
                "dst_ctx": "typed:xBroadcast_is32_os64_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )+512+_mm512_set1_epi8+typed:xBroadcast_is8_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 512 8 0 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 64)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )",
                "src_ctx": "_mm512_set1_epi8",
                "dst_ctx": "typed:xBroadcast_is8_os512_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )+256+_mm256_set1_epi32+typed:xBroadcast_is32_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 256 32 0 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 8)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )",
                "src_ctx": "_mm256_set1_epi32",
                "dst_ctx": "typed:xBroadcast_is32_os256_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )+512+_mm512_set1_epi16+typed:xBroadcast_is16_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 512 16 0 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )",
                "src_ctx": "_mm512_set1_epi16",
                "dst_ctx": "typed:xBroadcast_is16_os512_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )+128+_mm_set1_epi8+typed:xBroadcast_is8_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 128 8 0 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )",
                "src_ctx": "_mm_set1_epi8",
                "dst_ctx": "typed:xBroadcast_is8_os128_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )+128+_mm_set1_epi16+typed:xBroadcast_is16_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 128 16 0 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )",
                "src_ctx": "_mm_set1_epi16",
                "dst_ctx": "typed:xBroadcast_is16_os128_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )+64+_mm_set1_pi16+typed:xBroadcast_is16_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 0 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )",
                "src_ctx": "_mm_set1_pi16",
                "dst_ctx": "typed:xBroadcast_is16_os64_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )+512+_mm512_set1_epi32+typed:xBroadcast_is32_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 512 32 0 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 16)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )",
                "src_ctx": "_mm512_set1_epi32",
                "dst_ctx": "typed:xBroadcast_is32_os512_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )+128+_mm_set1_epi32+typed:xBroadcast_is32_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 128 32 0 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )",
                "src_ctx": "_mm_set1_epi32",
                "dst_ctx": "typed:xBroadcast_is32_os128_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )+256+_mm256_set1_epi8+typed:xBroadcast_is8_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 256 8 0 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 32)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )",
                "src_ctx": "_mm256_set1_epi8",
                "dst_ctx": "typed:xBroadcast_is8_os256_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )+64+_mm_set1_pi8+typed:xBroadcast_is8_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 64 8 0 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )",
                "src_ctx": "_mm_set1_pi8",
                "dst_ctx": "typed:xBroadcast_is8_os64_signed_None"
            }
        }
    ],
    " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )+ (x86_swizzle_622_dsl ; x86_swizzle_127\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )+128+_mm_broadcast_i32x2+x86_swizzle_127": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)",
                "dst": "(x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )",
                "original_dst_expr": " (x86_swizzle_622_dsl ; x86_swizzle_127\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )",
                "src_ctx": "_mm_broadcast_i32x2",
                "dst_ctx": "x86_swizzle_127"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )+256+_mm256_set1_epi16+typed:xBroadcast_is16_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 256 16 0 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 16)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os64_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t4\n )",
                "src_ctx": "_mm256_set1_epi16",
                "dst_ctx": "typed:xBroadcast_is16_os256_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )+128+_mm_set1_epi8+typed:xBroadcast_is32_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 128 8 0 0)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 32 32 4)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )",
                "src_ctx": "_mm_set1_epi8",
                "dst_ctx": "typed:xBroadcast_is32_os128_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )+64+_mm_set1_pi16+typed:xBroadcast_is32_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 0 0)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32 2)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )",
                "src_ctx": "_mm_set1_pi16",
                "dst_ctx": "typed:xBroadcast_is32_os64_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )+128+_mm_set1_epi16+typed:xBroadcast_is32_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 128 16 0 0)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32 4)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )",
                "src_ctx": "_mm_set1_epi16",
                "dst_ctx": "typed:xBroadcast_is32_os128_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )+128+_mm_set1_epi8+typed:xBroadcast_is16_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 128 8 0 0)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16 8)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )",
                "src_ctx": "_mm_set1_epi8",
                "dst_ctx": "typed:xBroadcast_is16_os128_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )+512+_mm512_set1_epi16+typed:xBroadcast_is32_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 512 16 0 0)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32 16)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )",
                "src_ctx": "_mm512_set1_epi16",
                "dst_ctx": "typed:xBroadcast_is32_os512_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )+512+_mm512_set1_epi8+typed:xBroadcast_is32_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 512 8 0 0)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 32 32 16)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )",
                "src_ctx": "_mm512_set1_epi8",
                "dst_ctx": "typed:xBroadcast_is32_os512_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )+64+_mm_set1_pi8+typed:xBroadcast_is16_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 64 8 0 0)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16 4)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )",
                "src_ctx": "_mm_set1_pi8",
                "dst_ctx": "typed:xBroadcast_is16_os64_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )+512+_mm512_set1_epi8+typed:xBroadcast_is16_os512_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 512 8 0 0)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16 32)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )",
                "src_ctx": "_mm512_set1_epi8",
                "dst_ctx": "typed:xBroadcast_is16_os512_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )+256+_mm256_set1_epi8+typed:xBroadcast_is16_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 256 8 0 0)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16 16)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )",
                "src_ctx": "_mm256_set1_epi8",
                "dst_ctx": "typed:xBroadcast_is16_os256_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )+256+_mm256_set1_epi8+typed:xBroadcast_is32_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 256 8 0 0)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 32 32 8)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )",
                "src_ctx": "_mm256_set1_epi8",
                "dst_ctx": "typed:xBroadcast_is32_os256_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )+256+_mm256_set1_epi16+typed:xBroadcast_is32_os256_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 256 16 0 0)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32 8)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )",
                "src_ctx": "_mm256_set1_epi16",
                "dst_ctx": "typed:xBroadcast_is32_os256_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )+64+_mm_set1_pi8+typed:xBroadcast_is32_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 64 8 0 0)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 4) 32 32 2)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os64_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t32\n\t32\n\t2\n )",
                "src_ctx": "_mm_set1_pi8",
                "dst_ctx": "typed:xBroadcast_is32_os64_signed_None"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi16+typed:slice_vectors_ip16_is128_op16_os64_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 0 1 4 16 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi16",
                "dst_ctx": "typed:slice_vectors_ip16_is128_op16_os64_signed_None_0_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi16+typed:slice_vectors_ip64_is128_op64_os64_signed_None_1_1_1": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 1 1 1 64 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi16",
                "dst_ctx": "typed:slice_vectors_ip64_is128_op64_os64_signed_None_1_1_1"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi16+typed:slice_vectors_ip64_is128_op64_os64_signed_None_0_1_1": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 0 1 1 64 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi16",
                "dst_ctx": "typed:slice_vectors_ip64_is128_op64_os64_signed_None_0_1_1"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi16+typed:slice_vectors_ip16_is128_op16_os64_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 4 1 4 16 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi16",
                "dst_ctx": "typed:slice_vectors_ip16_is128_op16_os64_signed_None_4_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi16+typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 8 1 8 8 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi16",
                "dst_ctx": "typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi32+typed:slice_vectors_ip16_is128_op16_os64_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 0 1 4 16 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi32",
                "dst_ctx": "typed:slice_vectors_ip16_is128_op16_os64_signed_None_0_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi32+typed:slice_vectors_ip32_is128_op32_os64_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 2 1 2 32 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi32",
                "dst_ctx": "typed:slice_vectors_ip32_is128_op32_os64_signed_None_2_1_2"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi32+typed:slice_vectors_ip32_is128_op32_os64_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 0 1 2 32 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi32",
                "dst_ctx": "typed:slice_vectors_ip32_is128_op32_os64_signed_None_0_1_2"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi32+typed:slice_vectors_ip64_is128_op64_os64_signed_None_0_1_1": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 0 1 1 64 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi32",
                "dst_ctx": "typed:slice_vectors_ip64_is128_op64_os64_signed_None_0_1_1"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi32+typed:slice_vectors_ip16_is128_op16_os64_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 4 1 4 16 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi32",
                "dst_ctx": "typed:slice_vectors_ip16_is128_op16_os64_signed_None_4_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi32+typed:slice_vectors_ip8_is128_op8_os64_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 0 1 8 8 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi32",
                "dst_ctx": "typed:slice_vectors_ip8_is128_op8_os64_signed_None_0_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi16+typed:slice_vectors_ip32_is128_op32_os64_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 0 1 2 32 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi16",
                "dst_ctx": "typed:slice_vectors_ip32_is128_op32_os64_signed_None_0_1_2"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi32+typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 8 1 8 8 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi32",
                "dst_ctx": "typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi16+typed:slice_vectors_ip32_is128_op32_os64_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 2 1 2 32 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi16",
                "dst_ctx": "typed:slice_vectors_ip32_is128_op32_os64_signed_None_2_1_2"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi16+typed:slice_vectors_ip8_is128_op8_os64_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) 0 1 8 8 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi16",
                "dst_ctx": "typed:slice_vectors_ip8_is128_op8_os64_signed_None_0_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi32+typed:slice_vectors_ip64_is128_op64_os64_signed_None_1_1_1": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 64 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 4) 1 1 1 64 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi32",
                "dst_ctx": "typed:slice_vectors_ip64_is128_op64_os64_signed_None_1_1_1"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi16+typed:slice_vectors_ip16_is256_op16_os128_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 128 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 8 1 8 16 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip16_is256_op16_os128_signed_None_8_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi16+typed:slice_vectors_ip64_is256_op64_os128_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 128 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 0 1 2 64 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip64_is256_op64_os128_signed_None_0_1_2"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi8+typed:slice_vectors_ip32_is256_op32_os128_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 128 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 4 1 4 32 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip32_is256_op32_os128_signed_None_4_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi8+typed:slice_vectors_ip64_is256_op64_os128_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 128 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 2 1 2 64 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip64_is256_op64_os128_signed_None_2_1_2"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi32+typed:slice_vectors_ip64_is1024_op64_os512_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 512 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 8 1 8 64 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip64_is1024_op64_os512_signed_None_8_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi16+typed:slice_vectors_ip64_is256_op64_os128_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 128 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 2 1 2 64 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip64_is256_op64_os128_signed_None_2_1_2"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi8+typed:slice_vectors_ip32_is256_op32_os128_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 128 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 0 1 4 32 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip32_is256_op32_os128_signed_None_0_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi16+typed:slice_vectors_ip16_is256_op16_os128_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 128 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 0 1 8 16 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip16_is256_op16_os128_signed_None_0_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi16+typed:slice_vectors_ip32_is256_op32_os128_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 128 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 4 1 4 32 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip32_is256_op32_os128_signed_None_4_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi32+typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 512 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 64 1 64 8 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi16+typed:slice_vectors_ip32_is256_op32_os128_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 128 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 0 1 4 32 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip32_is256_op32_os128_signed_None_0_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi8+typed:slice_vectors_ip64_is256_op64_os128_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 128 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 0 1 2 64 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip64_is256_op64_os128_signed_None_0_1_2"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi8+typed:slice_vectors_ip16_is256_op16_os128_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 128 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 8 1 8 16 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip16_is256_op16_os128_signed_None_8_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi32+typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 512 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 0 1 32 16 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi8+typed:slice_vectors_ip8_is256_op8_os128_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 128 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 16 1 16 8 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip8_is256_op8_os128_signed_None_16_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi32+typed:slice_vectors_ip16_is1024_op16_os512_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 512 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 32 1 32 16 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip16_is1024_op16_os512_signed_None_32_1_32"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi8+typed:slice_vectors_ip8_is256_op8_os128_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 128 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 0 1 16 8 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip8_is256_op8_os128_signed_None_0_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi16+typed:slice_vectors_ip8_is256_op8_os128_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 128 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 0 1 16 8 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip8_is256_op8_os128_signed_None_0_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi32+typed:slice_vectors_ip32_is1024_op32_os512_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 512 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 16 1 16 32 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip32_is1024_op32_os512_signed_None_16_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi32+typed:slice_vectors_ip8_is1024_op8_os512_signed_None_0_1_64": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 512 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 0 1 64 8 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip8_is1024_op8_os512_signed_None_0_1_64"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi32+typed:slice_vectors_ip64_is1024_op64_os512_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 512 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 0 1 8 64 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip64_is1024_op64_os512_signed_None_0_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi32+typed:slice_vectors_ip32_is1024_op32_os512_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 512 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 32) 0 1 16 32 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip32_is1024_op32_os512_signed_None_0_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi8+typed:slice_vectors_ip16_is256_op16_os128_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 128 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 32) 0 1 8 16 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip16_is256_op16_os128_signed_None_0_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi16+typed:slice_vectors_ip8_is256_op8_os128_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 128 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 16 1 16 8 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip8_is256_op8_os128_signed_None_16_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi16+typed:slice_vectors_ip32_is1024_op32_os512_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 512 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 0 1 16 32 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip32_is1024_op32_os512_signed_None_0_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi16+typed:slice_vectors_ip64_is1024_op64_os512_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 512 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 8 1 8 64 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip64_is1024_op64_os512_signed_None_8_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi16+typed:slice_vectors_ip16_is1024_op16_os512_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 512 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 32 1 32 16 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip16_is1024_op16_os512_signed_None_32_1_32"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi16+typed:slice_vectors_ip32_is1024_op32_os512_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 512 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 16 1 16 32 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip32_is1024_op32_os512_signed_None_16_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi16+typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 512 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 0 1 32 16 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi8+typed:slice_vectors_ip32_is1024_op32_os512_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 512 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 0 1 16 32 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip32_is1024_op32_os512_signed_None_0_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi16+typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 512 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 64 1 64 8 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi8+typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 512 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 0 1 32 16 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi32+typed:slice_vectors_ip64_is512_op64_os256_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 256 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 4 1 4 64 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip64_is512_op64_os256_signed_None_4_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi16+typed:slice_vectors_ip64_is1024_op64_os512_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 512 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 0 1 8 64 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip64_is1024_op64_os512_signed_None_0_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi32+typed:slice_vectors_ip32_is512_op32_os256_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 256 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 8 1 8 32 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip32_is512_op32_os256_signed_None_8_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi8+typed:slice_vectors_ip32_is1024_op32_os512_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 512 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 16 1 16 32 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip32_is1024_op32_os512_signed_None_16_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi32+typed:slice_vectors_ip16_is256_op16_os128_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 128 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 0 1 8 16 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip16_is256_op16_os128_signed_None_0_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi8+typed:slice_vectors_ip64_is1024_op64_os512_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 512 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 8 1 8 64 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip64_is1024_op64_os512_signed_None_8_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi16+typed:slice_vectors_ip8_is1024_op8_os512_signed_None_0_1_64": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 512 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 0 1 64 8 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip8_is1024_op8_os512_signed_None_0_1_64"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi8+typed:slice_vectors_ip64_is1024_op64_os512_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 512 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 0 1 8 64 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip64_is1024_op64_os512_signed_None_0_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi32+typed:slice_vectors_ip64_is512_op64_os256_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 256 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 0 1 4 64 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip64_is512_op64_os256_signed_None_0_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi32+typed:slice_vectors_ip32_is512_op32_os256_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 256 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 0 1 8 32 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip32_is512_op32_os256_signed_None_0_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi8+typed:slice_vectors_ip8_is1024_op8_os512_signed_None_0_1_64": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 512 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 0 1 64 8 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip8_is1024_op8_os512_signed_None_0_1_64"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi32+typed:slice_vectors_ip16_is512_op16_os256_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 256 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 16 1 16 16 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip16_is512_op16_os256_signed_None_16_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi32+typed:slice_vectors_ip64_is256_op64_os128_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 128 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 2 1 2 64 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip64_is256_op64_os128_signed_None_2_1_2"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi8+typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 512 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 64 1 64 8 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip8_is1024_op8_os512_signed_None_64_1_64"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi32+typed:slice_vectors_ip8_is512_op8_os256_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 256 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 32 1 32 8 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip8_is512_op8_os256_signed_None_32_1_32"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+512+_mm512_set1_epi8+typed:slice_vectors_ip16_is1024_op16_os512_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 512 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 128) 32 1 32 16 1024)",
                "output_size": 512,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm512_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip16_is1024_op16_os512_signed_None_32_1_32"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi32+typed:slice_vectors_ip32_is256_op32_os128_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 128 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 0 1 4 32 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip32_is256_op32_os128_signed_None_0_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi32+typed:slice_vectors_ip32_is256_op32_os128_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 128 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 4 1 4 32 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip32_is256_op32_os128_signed_None_4_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi32+typed:slice_vectors_ip8_is512_op8_os256_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 256 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 0 1 32 8 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip8_is512_op8_os256_signed_None_0_1_32"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi32+typed:slice_vectors_ip64_is256_op64_os128_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 128 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 0 1 2 64 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip64_is256_op64_os128_signed_None_0_1_2"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi32+typed:slice_vectors_ip16_is512_op16_os256_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 256 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 0 1 16 16 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip16_is512_op16_os256_signed_None_0_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi32+typed:slice_vectors_ip16_is256_op16_os128_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 128 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 8 1 8 16 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip16_is256_op16_os128_signed_None_8_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi8+typed:slice_vectors_ip16_is512_op16_os256_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 256 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 0 1 16 16 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip16_is512_op16_os256_signed_None_0_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi8+typed:slice_vectors_ip32_is512_op32_os256_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 256 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 0 1 8 32 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip32_is512_op32_os256_signed_None_0_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi32+typed:slice_vectors_ip8_is256_op8_os128_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 128 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 0 1 16 8 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip8_is256_op8_os128_signed_None_0_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+128+_mm_set1_epi32+typed:slice_vectors_ip8_is256_op8_os128_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 32 32 0 128 32 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 8) 16 1 16 8 256)",
                "output_size": 128,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_epi32",
                "dst_ctx": "typed:slice_vectors_ip8_is256_op8_os128_signed_None_16_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi8+typed:slice_vectors_ip32_is512_op32_os256_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 256 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 8 1 8 32 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip32_is512_op32_os256_signed_None_8_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi16+typed:slice_vectors_ip8_is512_op8_os256_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 256 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 0 1 32 8 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip8_is512_op8_os256_signed_None_0_1_32"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi8+typed:slice_vectors_ip16_is512_op16_os256_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 256 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 16 1 16 16 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip16_is512_op16_os256_signed_None_16_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi8+typed:slice_vectors_ip64_is512_op64_os256_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 256 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 0 1 4 64 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip64_is512_op64_os256_signed_None_0_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi8+typed:slice_vectors_ip64_is128_op64_os64_signed_None_1_1_1": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 64 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 1 1 1 64 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi8",
                "dst_ctx": "typed:slice_vectors_ip64_is128_op64_os64_signed_None_1_1_1"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi16+typed:slice_vectors_ip16_is512_op16_os256_signed_None_0_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 256 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 0 1 16 16 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip16_is512_op16_os256_signed_None_0_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi16+typed:slice_vectors_ip64_is512_op64_os256_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 256 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 4 1 4 64 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip64_is512_op64_os256_signed_None_4_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi8+typed:slice_vectors_ip8_is128_op8_os64_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 64 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 0 1 8 8 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi8",
                "dst_ctx": "typed:slice_vectors_ip8_is128_op8_os64_signed_None_0_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi8+typed:slice_vectors_ip64_is512_op64_os256_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 256 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 4 1 4 64 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip64_is512_op64_os256_signed_None_4_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi16+typed:slice_vectors_ip16_is512_op16_os256_signed_None_16_1_16": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 256 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 16 1 16 16 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip16_is512_op16_os256_signed_None_16_1_16"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi16+typed:slice_vectors_ip32_is512_op32_os256_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 256 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 8 1 8 32 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip32_is512_op32_os256_signed_None_8_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi16+typed:slice_vectors_ip64_is512_op64_os256_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 256 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 0 1 4 64 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip64_is512_op64_os256_signed_None_0_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi16+typed:slice_vectors_ip8_is512_op8_os256_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 256 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 32 1 32 8 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip8_is512_op8_os256_signed_None_32_1_32"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi8+typed:slice_vectors_ip32_is128_op32_os64_signed_None_2_1_2": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 64 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 2 1 2 32 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi8",
                "dst_ctx": "typed:slice_vectors_ip32_is128_op32_os64_signed_None_2_1_2"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi8+typed:slice_vectors_ip32_is128_op32_os64_signed_None_0_1_2": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 64 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 0 1 2 32 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi8",
                "dst_ctx": "typed:slice_vectors_ip32_is128_op32_os64_signed_None_0_1_2"
            }
        }
    ],
    " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )+ (x86_swizzle_622_dsl ; x86_swizzle_127\n\t (x86_swizzle_622_dsl ; x86_swizzle_127\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t )\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )+128+_mm_broadcast_i32x2+x86_swizzle_622": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)",
                "dst": "(x86_swizzle_622_dsl (x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0) 128 128 0 128 16 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )",
                "original_dst_expr": " (x86_swizzle_622_dsl ; x86_swizzle_127\n\t (x86_swizzle_622_dsl ; x86_swizzle_127\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t )\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )",
                "src_ctx": "_mm_broadcast_i32x2",
                "dst_ctx": "x86_swizzle_622"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi16+typed:slice_vectors_ip32_is512_op32_os256_signed_None_0_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 16 16 0 256 16 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 32) 0 1 8 32 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi16",
                "dst_ctx": "typed:slice_vectors_ip32_is512_op32_os256_signed_None_0_1_8"
            }
        }
    ],
    " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )+ (x86_swizzle_622_dsl ; x86_swizzle_127\n\t (x86_swizzle_622_dsl ; x86_swizzle_127\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t )\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )+128+_mm_broadcast_i32x2+x86_swizzle_326": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)",
                "dst": "(x86_swizzle_622_dsl (x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0) 128 128 0 128 8 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )",
                "original_dst_expr": " (x86_swizzle_622_dsl ; x86_swizzle_127\n\t (x86_swizzle_622_dsl ; x86_swizzle_127\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t )\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )",
                "src_ctx": "_mm_broadcast_i32x2",
                "dst_ctx": "x86_swizzle_326"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi8+typed:slice_vectors_ip8_is512_op8_os256_signed_None_32_1_32": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 256 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 32 1 32 8 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip8_is512_op8_os256_signed_None_32_1_32"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+256+_mm256_set1_epi8+typed:slice_vectors_ip8_is512_op8_os256_signed_None_0_1_32": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 256 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 64) 0 1 32 8 512)",
                "output_size": 256,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm256_set1_epi8",
                "dst_ctx": "typed:slice_vectors_ip8_is512_op8_os256_signed_None_0_1_32"
            }
        }
    ],
    " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )+ (x86_swizzle_622_dsl ; x86_swizzle_127\n\t (x86_swizzle_622_dsl ; x86_swizzle_127\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t )\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )+128+_mm_broadcast_i32x2+x86_swizzle_228": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)",
                "dst": "(x86_swizzle_622_dsl (x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0) 128 128 0 128 32 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )",
                "original_dst_expr": " (x86_swizzle_622_dsl ; x86_swizzle_127\n\t (x86_swizzle_622_dsl ; x86_swizzle_127\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t )\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )",
                "src_ctx": "_mm_broadcast_i32x2",
                "dst_ctx": "x86_swizzle_228"
            }
        }
    ],
    " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )+ (x86_swizzle_622_dsl ; x86_swizzle_127\n\t (x86_swizzle_622_dsl ; x86_swizzle_127\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t )\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )+128+_mm_broadcast_i32x2+x86_swizzle_127": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)",
                "dst": "(x86_swizzle_622_dsl (x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0) 128 64 0 64 32 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )",
                "original_dst_expr": " (x86_swizzle_622_dsl ; x86_swizzle_127\n\t (x86_swizzle_622_dsl ; x86_swizzle_127\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t )\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )",
                "src_ctx": "_mm_broadcast_i32x2",
                "dst_ctx": "x86_swizzle_127"
            }
        }
    ],
    " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )+ (x86_swizzle_622_dsl ; x86_swizzle_127\n\t (x86_swizzle_622_dsl ; x86_swizzle_127\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t )\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )+128+_mm_broadcast_i32x2+x86_swizzle_70": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm_broadcast_i32x2_dsl (reg (bv #x00 8)) 128 128 0 128 32 2 32 0)",
                "dst": "(x86_swizzle_622_dsl (x86_swizzle_622_dsl (reg (bv #x00 8)) 128 64 0 64 32 0) 128 128 0 128 64 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_broadcast_i32x2_dsl ; _mm_broadcast_i32x2\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t2\n\t32\n\t0\n )",
                "original_dst_expr": " (x86_swizzle_622_dsl ; x86_swizzle_127\n\t (x86_swizzle_622_dsl ; x86_swizzle_127\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t0\n\t )\n\t128\n\t64\n\t0\n\t64\n\t32\n\t0\n )",
                "src_ctx": "_mm_broadcast_i32x2",
                "dst_ctx": "x86_swizzle_70"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi8+typed:slice_vectors_ip16_is128_op16_os64_signed_None_0_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 64 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 0 1 4 16 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi8",
                "dst_ctx": "typed:slice_vectors_ip16_is128_op16_os64_signed_None_0_1_4"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi8+typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 64 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 8 1 8 8 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi8",
                "dst_ctx": "typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi8+typed:slice_vectors_ip64_is128_op64_os64_signed_None_0_1_1": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 64 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 0 1 1 64 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi8",
                "dst_ctx": "typed:slice_vectors_ip64_is128_op64_os64_signed_None_0_1_1"
            }
        }
    ],
    " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )+ (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )+64+_mm_set1_pi8+typed:slice_vectors_ip16_is128_op16_os64_signed_None_4_1_4": [
        {
            "property_name": "EnumeratePattern_broadcasts",
            "property": {
                "src": "(_mm512_broadcastq_epi64_dsl (reg (bv #x00 8)) 8 8 0 64 8 0 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 16) 4 1 4 16 128)",
                "output_size": 64,
                "original_src_expr": " (_mm512_broadcastq_epi64_dsl ; _mm_set1_pi16\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:slice_vectors ; typed:slice_vectors_ip8_is128_op8_os64_signed_None_8_1_8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os128_signed_None\n\t\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t8\n\t )\n\t8\n\t1\n\t8\n\t8\n\t128\n )",
                "src_ctx": "_mm_set1_pi8",
                "dst_ctx": "typed:slice_vectors_ip16_is128_op16_os64_signed_None_4_1_4"
            }
        }
    ]
}