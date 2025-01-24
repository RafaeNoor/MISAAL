{
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+ (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+512+_mm512_or_epi64+_mm512_or_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm512_or_epi32_dsl (_mm512_or_epi32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 64 0) (reg (bv #x00 8)) 512 512 0 512 64 0)",
                "dst": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (_mm512_or_epi32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 64 0) 512 512 0 512 64 0)",
                "output_size": 512,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "src_ctx": "_mm512_or_epi64",
                "dst_ctx": "_mm512_or_epi64"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+ (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+128+_mm_or_epi64+_mm_or_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm512_or_epi32_dsl (_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0) (reg (bv #x02 8)) 128 128 0 128 64 0)",
                "dst": "(_mm512_or_epi32_dsl (reg (bv #x02 8)) (_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0) 128 128 0 128 64 0)",
                "output_size": 128,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "src_ctx": "_mm_or_epi64",
                "dst_ctx": "_mm_or_epi64"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+ (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+128+_mm_or_epi64+_mm_or_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm512_or_epi32_dsl (_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0) (reg (bv #x02 8)) 128 128 0 128 64 0)",
                "dst": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 64 0) 128 128 0 128 32 0)",
                "output_size": 128,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "src_ctx": "_mm_or_epi64",
                "dst_ctx": "_mm_or_epi32"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+ (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+512+_mm512_or_epi32+_mm512_or_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm512_or_epi32_dsl (_mm512_or_epi32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 64 0) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (_mm512_or_epi32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 32 0) 512 512 0 512 32 0)",
                "output_size": 512,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "src_ctx": "_mm512_or_epi32",
                "dst_ctx": "_mm512_or_epi32"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+ (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+512+_mm512_or_epi64+_mm512_or_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm512_or_epi32_dsl (_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 64 0) (reg (bv #x00 8)) 512 512 0 512 64 0)",
                "dst": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 32 0) 512 512 0 512 32 0)",
                "output_size": 512,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "src_ctx": "_mm512_or_epi64",
                "dst_ctx": "_mm512_or_epi32"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+ (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+256+_mm256_or_epi32+_mm256_or_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm512_or_epi32_dsl (_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0) (reg (bv #x02 8)) 256 256 0 256 32 0)",
                "dst": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (_mm512_or_epi32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 256 32 0) 256 256 0 256 64 0)",
                "output_size": 256,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "src_ctx": "_mm256_or_epi32",
                "dst_ctx": "_mm256_or_epi64"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+ (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+512+_mm512_or_epi32+_mm512_or_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm512_or_epi32_dsl (_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0) (reg (bv #x02 8)) 512 512 0 512 32 0)",
                "dst": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (_mm512_or_epi32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 32 0) 512 512 0 512 64 0)",
                "output_size": 512,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "src_ctx": "_mm512_or_epi32",
                "dst_ctx": "_mm512_or_epi64"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+ (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+256+_mm256_or_epi32+_mm256_or_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm512_or_epi32_dsl (_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0) (reg (bv #x02 8)) 256 256 0 256 32 0)",
                "dst": "(_mm512_or_epi32_dsl (reg (bv #x02 8)) (_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0) 256 256 0 256 32 0)",
                "output_size": 256,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "src_ctx": "_mm256_or_epi32",
                "dst_ctx": "_mm256_or_epi32"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+ (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+256+_mm256_or_epi64+_mm256_or_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm512_or_epi32_dsl (_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0) (reg (bv #x02 8)) 256 256 0 256 64 0)",
                "dst": "(_mm512_or_epi32_dsl (reg (bv #x02 8)) (_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0) 256 256 0 256 32 0)",
                "output_size": 256,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "src_ctx": "_mm256_or_epi64",
                "dst_ctx": "_mm256_or_epi32"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+ (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+128+_mm_or_epi32+_mm_or_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm512_or_epi32_dsl (_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0) (reg (bv #x02 8)) 128 128 0 128 32 0)",
                "dst": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (_mm512_or_epi32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 64 0) 128 128 0 128 64 0)",
                "output_size": 128,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "src_ctx": "_mm_or_epi32",
                "dst_ctx": "_mm_or_epi64"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+ (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+256+_mm256_or_epi64+_mm256_or_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm512_or_epi32_dsl (_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 64 0) (reg (bv #x01 8)) 256 256 0 256 64 0)",
                "dst": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 32 0) 256 256 0 256 64 0)",
                "output_size": 256,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "src_ctx": "_mm256_or_epi64",
                "dst_ctx": "_mm256_or_epi64"
            }
        }
    ],
    " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+ (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+256+_mm256_xor_epi32+_mm256_xor_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_epi32_dsl (_mm256_xor_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0) (reg (bv #x02 8)) 256 256 0 256 32 0)",
                "dst": "(_mm256_xor_epi32_dsl (reg (bv #x01 8)) (_mm256_xor_epi32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 32 0) 256 256 0 256 64 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "src_ctx": "_mm256_xor_epi32",
                "dst_ctx": "_mm256_xor_epi64"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+ (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+128+_mm_or_epi32+_mm_or_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm512_or_epi32_dsl (_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0) (reg (bv #x02 8)) 128 128 0 128 32 0)",
                "dst": "(_mm512_or_epi32_dsl (reg (bv #x02 8)) (_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0) 128 128 0 128 32 0)",
                "output_size": 128,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_or_epi32_dsl ; _mm512_or_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "src_ctx": "_mm_or_epi32",
                "dst_ctx": "_mm_or_epi32"
            }
        }
    ],
    " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+ (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+256+_mm256_xor_epi32+_mm256_xor_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_epi32_dsl (_mm256_xor_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0) (reg (bv #x02 8)) 256 256 0 256 32 0)",
                "dst": "(_mm256_xor_epi32_dsl (reg (bv #x01 8)) (_mm256_xor_epi32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 64 0) 256 256 0 256 32 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "src_ctx": "_mm256_xor_epi32",
                "dst_ctx": "_mm256_xor_epi32"
            }
        }
    ],
    " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+ (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+512+_mm512_xor_epi32+_mm512_xor_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_epi32_dsl (_mm256_xor_epi32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 32 0) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(_mm256_xor_epi32_dsl (reg (bv #x02 8)) (_mm256_xor_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0) 512 512 0 512 32 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "src_ctx": "_mm512_xor_epi32",
                "dst_ctx": "_mm512_xor_epi32"
            }
        }
    ],
    " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+ (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+512+_mm512_xor_epi32+_mm512_xor_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_epi32_dsl (_mm256_xor_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0) (reg (bv #x02 8)) 512 512 0 512 32 0)",
                "dst": "(_mm256_xor_epi32_dsl (reg (bv #x00 8)) (_mm256_xor_epi32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 32 0) 512 512 0 512 64 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "src_ctx": "_mm512_xor_epi32",
                "dst_ctx": "_mm512_xor_epi64"
            }
        }
    ],
    " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+ (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+256+_mm256_xor_epi64+_mm256_xor_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_epi32_dsl (_mm256_xor_epi32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 32 0) (reg (bv #x01 8)) 256 256 0 256 64 0)",
                "dst": "(_mm256_xor_epi32_dsl (reg (bv #x00 8)) (_mm256_xor_epi32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 256 32 0) 256 256 0 256 64 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "src_ctx": "_mm256_xor_epi64",
                "dst_ctx": "_mm256_xor_epi64"
            }
        }
    ],
    " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+ (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+256+_mm256_xor_epi64+_mm256_xor_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_epi32_dsl (_mm256_xor_epi32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 32 0) (reg (bv #x01 8)) 256 256 0 256 64 0)",
                "dst": "(_mm256_xor_epi32_dsl (reg (bv #x00 8)) (_mm256_xor_epi32_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 32 0) 256 256 0 256 32 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "src_ctx": "_mm256_xor_epi64",
                "dst_ctx": "_mm256_xor_epi32"
            }
        }
    ],
    " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+ (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+128+_mm_xor_epi32+_mm_xor_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_epi32_dsl (_mm256_xor_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0) (reg (bv #x02 8)) 128 128 0 128 32 0)",
                "dst": "(_mm256_xor_epi32_dsl (reg (bv #x00 8)) (_mm256_xor_epi32_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 64 0) 128 128 0 128 64 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "src_ctx": "_mm_xor_epi32",
                "dst_ctx": "_mm_xor_epi64"
            }
        }
    ],
    " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+ (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+512+_mm512_xor_epi64+_mm512_xor_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_epi32_dsl (_mm256_xor_epi32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 64 0) (reg (bv #x01 8)) 512 512 0 512 64 0)",
                "dst": "(_mm256_xor_epi32_dsl (reg (bv #x02 8)) (_mm256_xor_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0) 512 512 0 512 32 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "src_ctx": "_mm512_xor_epi64",
                "dst_ctx": "_mm512_xor_epi32"
            }
        }
    ],
    " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+ (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+512+_mm512_xor_epi64+_mm512_xor_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_epi32_dsl (_mm256_xor_epi32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 64 0) (reg (bv #x01 8)) 512 512 0 512 64 0)",
                "dst": "(_mm256_xor_epi32_dsl (reg (bv #x02 8)) (_mm256_xor_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0) 512 512 0 512 64 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "src_ctx": "_mm512_xor_epi64",
                "dst_ctx": "_mm512_xor_epi64"
            }
        }
    ],
    " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+ (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+128+_mm_xor_epi32+_mm_xor_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_epi32_dsl (_mm256_xor_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0) (reg (bv #x02 8)) 128 128 0 128 32 0)",
                "dst": "(_mm256_xor_epi32_dsl (reg (bv #x02 8)) (_mm256_xor_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0) 128 128 0 128 32 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "src_ctx": "_mm_xor_epi32",
                "dst_ctx": "_mm_xor_epi32"
            }
        }
    ],
    " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+ (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+128+_mm_xor_epi64+_mm_xor_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_epi32_dsl (_mm256_xor_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0) (reg (bv #x02 8)) 128 128 0 128 64 0)",
                "dst": "(_mm256_xor_epi32_dsl (reg (bv #x01 8)) (_mm256_xor_epi32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 64 0) 128 128 0 128 32 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "src_ctx": "_mm_xor_epi64",
                "dst_ctx": "_mm_xor_epi32"
            }
        }
    ],
    " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+ (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )+128+_mm_xor_epi64+_mm_xor_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_epi32_dsl (_mm256_xor_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0) (reg (bv #x02 8)) 128 128 0 128 64 0)",
                "dst": "(_mm256_xor_epi32_dsl (reg (bv #x01 8)) (_mm256_xor_epi32_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 32 0) 128 128 0 128 64 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_epi32_dsl ; _mm256_xor_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t32\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )",
                "src_ctx": "_mm_xor_epi64",
                "dst_ctx": "_mm_xor_epi64"
            }
        }
    ],
    " (_mm_add_si64_dsl ; _mm_add_si64\n\t (_mm_add_si64_dsl ; _mm_add_si64\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )+ (_mm_add_si64_dsl ; _mm_add_si64\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_si64_dsl ; _mm_add_si64\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )+64+_mm_add_si64+_mm_add_si64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_si64_dsl (_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 64 -1 0 0) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(_mm_add_si64_dsl (reg (bv #x02 8)) (_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0) 64 64 0 64 64 -1 0 0)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_si64_dsl ; _mm_add_si64\n\t (_mm_add_si64_dsl ; _mm_add_si64\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_add_si64_dsl ; _mm_add_si64\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_si64_dsl ; _mm_add_si64\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t-1\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )",
                "src_ctx": "_mm_add_si64",
                "dst_ctx": "_mm_add_si64"
            }
        }
    ],
    " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+ (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+256+_mm256_xor_si256+_mm256_xor_si256": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_si256_dsl (_mm256_xor_si256_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 256 0 0) (reg (bv #x02 8)) 256 256 0 256 256 0 0)",
                "dst": "(_mm256_xor_si256_dsl (reg (bv #x01 8)) (_mm256_xor_si256_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 256 0 0) 256 256 0 256 256 0 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "src_ctx": "_mm256_xor_si256",
                "dst_ctx": "_mm256_xor_si256"
            }
        }
    ],
    " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+ (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+512+_mm512_xor_si512+_mm512_xor_si512": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_si256_dsl (_mm256_xor_si256_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 512 0 0) (reg (bv #x02 8)) 512 512 0 512 512 0 0)",
                "dst": "(_mm256_xor_si256_dsl (reg (bv #x02 8)) (_mm256_xor_si256_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 512 0 0) 512 512 0 512 512 0 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "src_ctx": "_mm512_xor_si512",
                "dst_ctx": "_mm512_xor_si512"
            }
        }
    ],
    " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+ (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+128+_mm_xor_si128+_mm_xor_si128": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_si256_dsl (_mm256_xor_si256_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 128 0 0) (reg (bv #x02 8)) 128 128 0 128 128 0 0)",
                "dst": "(_mm256_xor_si256_dsl (reg (bv #x00 8)) (_mm256_xor_si256_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 128 0 0) 128 128 0 128 128 0 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "src_ctx": "_mm_xor_si128",
                "dst_ctx": "_mm_xor_si128"
            }
        }
    ],
    " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+ (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+64+_mm_xor_si64+_mm_xor_si64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_xor_si256_dsl (_mm256_xor_si256_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 64 0 0) (reg (bv #x01 8)) 64 64 0 64 64 0 0)",
                "dst": "(_mm256_xor_si256_dsl (reg (bv #x02 8)) (_mm256_xor_si256_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 0 0) 64 64 0 64 64 0 0)",
                "output_size": 64,
                "original_src_expr": " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_xor_si256_dsl ; _mm256_xor_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "src_ctx": "_mm_xor_si64",
                "dst_ctx": "_mm_xor_si64"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+256+_mm256_max_epu64+_mm256_max_epu64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 16 0 0) (reg (bv #x00 8)) 256 256 0 256 64 0 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0) 256 256 0 256 64 0 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm256_max_epu64",
                "dst_ctx": "_mm256_max_epu64"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+512+_mm512_max_epu64+_mm512_max_epu64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0) (reg (bv #x02 8)) 512 512 0 512 64 0 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x02 8)) (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0) 512 512 0 512 64 0 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm512_max_epu64",
                "dst_ctx": "_mm512_max_epu64"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+128+_mm_max_epi64+_mm_max_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0) (reg (bv #x01 8)) 128 128 0 128 64 1 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0) 128 128 0 128 64 1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm_max_epi64",
                "dst_ctx": "_mm_max_epi64"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+128+_mm_max_epu8+_mm_max_epu8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0) (reg (bv #x02 8)) 128 128 0 128 8 0 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x02 8)) (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0) 128 128 0 128 8 0 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm_max_epu8",
                "dst_ctx": "_mm_max_epu8"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+512+_mm512_max_epi16+_mm512_max_epi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 64 1 0) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 64 1 0) 512 512 0 512 16 1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm512_max_epi16",
                "dst_ctx": "_mm512_max_epi16"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+256+_mm256_max_epu32+_mm256_max_epu32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0) (reg (bv #x01 8)) 256 256 0 256 32 0 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x02 8)) (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0) 256 256 0 256 32 0 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm256_max_epu32",
                "dst_ctx": "_mm256_max_epu32"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+256+_mm256_max_epu8+_mm256_max_epu8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0) (reg (bv #x02 8)) 256 256 0 256 8 0 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x02 8)) (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0) 256 256 0 256 8 0 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm256_max_epu8",
                "dst_ctx": "_mm256_max_epu8"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+256+_mm256_max_epi64+_mm256_max_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0) (reg (bv #x01 8)) 256 256 0 256 64 1 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 32 0 0) 256 256 0 256 64 1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm256_max_epi64",
                "dst_ctx": "_mm256_max_epi64"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+128+_mm_max_epi16+_mm_max_epi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 1 0) (reg (bv #x02 8)) 128 128 0 128 16 1 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x02 8)) (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1 0) 128 128 0 128 16 1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm_max_epi16",
                "dst_ctx": "_mm_max_epi16"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+64+_m_pmaxsw+_m_pmaxsw": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 8 0 0) (reg (bv #x00 8)) 64 64 0 64 16 1 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 8 0 0) 64 64 0 64 16 1 0)",
                "output_size": 64,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_m_pmaxsw",
                "dst_ctx": "_m_pmaxsw"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+64+_mm_max_pu8+_mm_max_pu8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0) (reg (bv #x00 8)) 64 64 0 64 8 0 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x02 8)) (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0) 64 64 0 64 8 0 0)",
                "output_size": 64,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm_max_pu8",
                "dst_ctx": "_mm_max_pu8"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+128+_mm_max_epi32+_mm_max_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0) (reg (bv #x00 8)) 128 128 0 128 32 1 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0) 128 128 0 128 32 1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm_max_epi32",
                "dst_ctx": "_mm_max_epi32"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+256+_mm256_max_epu16+_mm256_max_epu16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0) (reg (bv #x02 8)) 256 256 0 256 16 0 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x02 8)) (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0) 256 256 0 256 16 0 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm256_max_epu16",
                "dst_ctx": "_mm256_max_epu16"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+128+_mm_max_epu32+_mm_max_epu32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0) (reg (bv #x00 8)) 128 128 0 128 32 0 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 0) 128 128 0 128 32 0 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm_max_epu32",
                "dst_ctx": "_mm_max_epu32"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+512+_mm512_max_epi64+_mm512_max_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0) (reg (bv #x02 8)) 512 512 0 512 64 1 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x02 8)) (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0) 512 512 0 512 64 1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm512_max_epi64",
                "dst_ctx": "_mm512_max_epi64"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+256+_mm256_max_epi32+_mm256_max_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 64 1 0) (reg (bv #x00 8)) 256 256 0 256 32 1 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 64 1 0) 256 256 0 256 32 1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm256_max_epi32",
                "dst_ctx": "_mm256_max_epi32"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+512+_mm512_max_epi8+_mm512_max_epi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0) 512 512 0 512 8 1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm512_max_epi8",
                "dst_ctx": "_mm512_max_epi8"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+128+_mm_max_epi8+_mm_max_epi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1 0) (reg (bv #x02 8)) 128 128 0 128 8 1 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x02 8)) (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1 0) 128 128 0 128 8 1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm_max_epi8",
                "dst_ctx": "_mm_max_epi8"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+256+_mm256_max_epi8+_mm256_max_epi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 8 1 0) (reg (bv #x00 8)) 256 256 0 256 8 1 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 8 1 0) 256 256 0 256 8 1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm256_max_epi8",
                "dst_ctx": "_mm256_max_epi8"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+128+_mm_max_epu64+_mm_max_epu64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0) (reg (bv #x02 8)) 128 128 0 128 64 0 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x02 8)) (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0) 128 128 0 128 64 0 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm_max_epu64",
                "dst_ctx": "_mm_max_epu64"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+128+_mm_max_epu16+_mm_max_epu16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 32 1 0) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 0) 128 128 0 128 16 0 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm_max_epu16",
                "dst_ctx": "_mm_max_epu16"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+512+_mm512_max_epi32+_mm512_max_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 8 1 0) (reg (bv #x01 8)) 512 512 0 512 32 1 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 8 1 0) 512 512 0 512 32 1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm512_max_epi32",
                "dst_ctx": "_mm512_max_epi32"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+512+_mm512_max_epu32+_mm512_max_epu32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 0) (reg (bv #x01 8)) 512 512 0 512 32 0 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 0) 512 512 0 512 32 0 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm512_max_epu32",
                "dst_ctx": "_mm512_max_epu32"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+256+_mm256_max_epi16+_mm256_max_epi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0) (reg (bv #x01 8)) 256 256 0 256 16 1 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x02 8)) (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 1 0) 256 256 0 256 16 1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm256_max_epi16",
                "dst_ctx": "_mm256_max_epi16"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+512+_mm512_max_epu8+_mm512_max_epu8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 64 1 0) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 64 1 0) 512 512 0 512 8 0 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm512_max_epu8",
                "dst_ctx": "_mm512_max_epu8"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+ (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )+512+_mm512_max_epu16+_mm512_max_epu16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_max_epu64_dsl (_mm256_max_epu64_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 8 0 0) 512 512 0 512 16 0 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_max_epu64_dsl ; _mm256_max_epu64\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm512_max_epu16",
                "dst_ctx": "_mm512_max_epu16"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+64+_mm_add_pi8+_mm_add_pi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 8 0 0) (reg (bv #x00 8)) 64 64 0 64 8 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 8 0 0) 64 64 0 64 8 -1 0)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_add_pi8",
                "dst_ctx": "_mm_add_pi8"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+64+_mm_adds_pi16+_mm_adds_pi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0) (reg (bv #x02 8)) 64 64 0 64 16 1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 0) 64 64 0 64 16 1 0)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_adds_pi16",
                "dst_ctx": "_mm_adds_pi16"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+256+_mm256_add_epi16+_mm256_add_epi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 16 0 0) (reg (bv #x00 8)) 256 256 0 256 16 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0) 256 256 0 256 16 -1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm256_add_epi16",
                "dst_ctx": "_mm256_add_epi16"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+128+_mm_adds_epu16+_mm_adds_epu16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 8 0 0) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0) 128 128 0 128 16 0 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_adds_epu16",
                "dst_ctx": "_mm_adds_epu16"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+128+_mm_add_epi32+_mm_add_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0) (reg (bv #x01 8)) 128 128 0 128 32 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0) 128 128 0 128 32 -1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_add_epi32",
                "dst_ctx": "_mm_add_epi32"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+256+_mm256_adds_epu8+_mm256_adds_epu8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0) (reg (bv #x01 8)) 256 256 0 256 8 0 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0) 256 256 0 256 8 0 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm256_adds_epu8",
                "dst_ctx": "_mm256_adds_epu8"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+256+_mm256_adds_epi16+_mm256_adds_epi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 1 0) (reg (bv #x02 8)) 256 256 0 256 16 1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 1 0) 256 256 0 256 16 1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm256_adds_epi16",
                "dst_ctx": "_mm256_adds_epi16"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+64+_m_paddw+_m_paddw": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 16 0 0) (reg (bv #x00 8)) 64 64 0 64 16 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 16 0 0) 64 64 0 64 16 -1 0)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_m_paddw",
                "dst_ctx": "_m_paddw"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+64+_mm_adds_pu16+_mm_adds_pu16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 64 0 64 8 1 0) (reg (bv #x00 8)) 64 64 0 64 16 0 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 64 0 64 8 1 0) 64 64 0 64 16 0 0)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_adds_pu16",
                "dst_ctx": "_mm_adds_pu16"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+128+_mm_add_epi16+_mm_add_epi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 8 0 0) (reg (bv #x00 8)) 128 128 0 128 16 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0) 128 128 0 128 16 -1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_add_epi16",
                "dst_ctx": "_mm_add_epi16"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+256+_mm256_adds_epu16+_mm256_adds_epu16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0) (reg (bv #x02 8)) 256 256 0 256 16 0 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0) 256 256 0 256 16 0 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm256_adds_epu16",
                "dst_ctx": "_mm256_adds_epu16"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+128+_mm_adds_epu8+_mm_adds_epu8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 0) (reg (bv #x02 8)) 128 128 0 128 8 0 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0) 128 128 0 128 8 0 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_adds_epu8",
                "dst_ctx": "_mm_adds_epu8"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+512+_mm512_add_epi16+_mm512_add_epi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 64 -1 0) 512 512 0 512 16 -1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm512_add_epi16",
                "dst_ctx": "_mm512_add_epi16"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+256+_mm256_adds_epi8+_mm256_adds_epi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0) (reg (bv #x02 8)) 256 256 0 256 8 1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0) 256 256 0 256 8 1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm256_adds_epi8",
                "dst_ctx": "_mm256_adds_epi8"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+64+_mm_adds_pi8+_mm_adds_pi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 -1 0) (reg (bv #x02 8)) 64 64 0 64 8 1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 -1 0) 64 64 0 64 8 1 0)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_adds_pi8",
                "dst_ctx": "_mm_adds_pi8"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+512+_mm512_add_epi64+_mm512_add_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 64 -1 0) 512 512 0 512 64 -1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm512_add_epi64",
                "dst_ctx": "_mm512_add_epi64"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+64+_mm_add_pi32+_mm_add_pi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0) (reg (bv #x02 8)) 64 64 0 64 32 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 0) 64 64 0 64 32 -1 0)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_add_pi32",
                "dst_ctx": "_mm_add_pi32"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+512+_mm512_add_epi32+_mm512_add_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 8 1 0) 512 512 0 512 32 -1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm512_add_epi32",
                "dst_ctx": "_mm512_add_epi32"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+512+_mm512_adds_epu8+_mm512_adds_epu8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0) (reg (bv #x02 8)) 512 512 0 512 8 0 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0) 512 512 0 512 8 0 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm512_adds_epu8",
                "dst_ctx": "_mm512_adds_epu8"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+256+_mm256_add_epi64+_mm256_add_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 8 1 0) (reg (bv #x01 8)) 256 256 0 256 64 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 8 1 0) 256 256 0 256 64 -1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm256_add_epi64",
                "dst_ctx": "_mm256_add_epi64"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+128+_mm_add_epi8+_mm_add_epi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0) (reg (bv #x00 8)) 128 128 0 128 8 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 0) 128 128 0 128 8 -1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_add_epi8",
                "dst_ctx": "_mm_add_epi8"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+128+_mm_adds_epi16+_mm_adds_epi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0) (reg (bv #x01 8)) 128 128 0 128 16 1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0) 128 128 0 128 16 1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_adds_epi16",
                "dst_ctx": "_mm_adds_epi16"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+64+_mm_adds_pu8+_mm_adds_pu8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 8 -1 0) (reg (bv #x01 8)) 64 64 0 64 8 0 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 8 -1 0) 64 64 0 64 8 0 0)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_adds_pu8",
                "dst_ctx": "_mm_adds_pu8"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+256+_mm256_add_epi8+_mm256_add_epi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0) (reg (bv #x02 8)) 256 256 0 256 8 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0) 256 256 0 256 8 -1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm256_add_epi8",
                "dst_ctx": "_mm256_add_epi8"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+512+_mm512_add_epi8+_mm512_add_epi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0) (reg (bv #x02 8)) 512 512 0 512 8 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0) 512 512 0 512 8 -1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm512_add_epi8",
                "dst_ctx": "_mm512_add_epi8"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+512+_mm512_adds_epi16+_mm512_adds_epi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0) (reg (bv #x02 8)) 512 512 0 512 16 1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0) 512 512 0 512 16 1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm512_adds_epi16",
                "dst_ctx": "_mm512_adds_epi16"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+128+_mm_add_epi64+_mm_add_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0) (reg (bv #x01 8)) 128 128 0 128 64 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0) 128 128 0 128 64 -1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_add_epi64",
                "dst_ctx": "_mm_add_epi64"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+512+_mm512_adds_epi8+_mm512_adds_epi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0) (reg (bv #x02 8)) 512 512 0 512 8 1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0) 512 512 0 512 8 1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm512_adds_epi8",
                "dst_ctx": "_mm512_adds_epi8"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+128+_mm_adds_epi8+_mm_adds_epi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (_mm_add_pi8_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0) 128 128 0 128 8 1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm_adds_epi8",
                "dst_ctx": "_mm_adds_epi8"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+512+_mm512_adds_epu16+_mm512_adds_epu16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0) (reg (bv #x02 8)) 512 512 0 512 16 0 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0) 512 512 0 512 16 0 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm512_adds_epu16",
                "dst_ctx": "_mm512_adds_epu16"
            }
        }
    ],
    " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+ (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+256+_mm256_and_si256+_mm256_and_si256": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_and_si256_dsl (_mm256_and_si256_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 256 0 0) (reg (bv #x00 8)) 256 256 0 256 256 0 0)",
                "dst": "(_mm256_and_si256_dsl (reg (bv #x01 8)) (_mm256_and_si256_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 256 0 0) 256 256 0 256 256 0 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "src_ctx": "_mm256_and_si256",
                "dst_ctx": "_mm256_and_si256"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+ (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )+256+_mm256_add_epi32+_mm256_add_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_add_pi8_dsl (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0) (reg (bv #x02 8)) 256 256 0 256 32 -1 0)",
                "dst": "(_mm_add_pi8_dsl (reg (bv #x02 8)) (_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0) 256 256 0 256 32 -1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (_mm_add_pi8_dsl ; _mm_add_pi8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_mm_add_pi8_dsl ; _mm_add_pi8\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t8\n\t\t-1\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "_mm256_add_epi32",
                "dst_ctx": "_mm256_add_epi32"
            }
        }
    ],
    " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+ (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+512+_mm512_and_epi64+_mm512_and_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_and_si256_dsl (_mm256_and_si256_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 512 0 0) (reg (bv #x02 8)) 512 512 0 512 512 0 0)",
                "dst": "(_mm256_and_si256_dsl (reg (bv #x02 8)) (_mm256_and_si256_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 512 0 0) 512 512 0 512 512 0 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "src_ctx": "_mm512_and_epi64",
                "dst_ctx": "_mm512_and_epi64"
            }
        }
    ],
    " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+ (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+64+_mm_and_si64+_mm_and_si64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_and_si256_dsl (_mm256_and_si256_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 0 0) (reg (bv #x02 8)) 64 64 0 64 64 0 0)",
                "dst": "(_mm256_and_si256_dsl (reg (bv #x02 8)) (_mm256_and_si256_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0) 64 64 0 64 64 0 0)",
                "output_size": 64,
                "original_src_expr": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "src_ctx": "_mm_and_si64",
                "dst_ctx": "_mm_and_si64"
            }
        }
    ],
    " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+ (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )+128+_mm_and_si128+_mm_and_si128": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm256_and_si256_dsl (_mm256_and_si256_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 128 0 0) (reg (bv #x01 8)) 128 128 0 128 128 0 0)",
                "dst": "(_mm256_and_si256_dsl (reg (bv #x01 8)) (_mm256_and_si256_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 128 0 0) 128 128 0 128 128 0 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm256_and_si256_dsl ; _mm256_and_si256\n\t(reg (bv 0 (bitvector 8))) ; < 32 x i8> False\n\t (_mm256_and_si256_dsl ; _mm256_and_si256\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i8> False\n\t\t256\n\t\t256\n\t\t0\n\t\t256\n\t\t256\n\t\t0\n\t\t0\n\t )\n\t256\n\t256\n\t0\n\t256\n\t256\n\t0\n\t0\n )",
                "src_ctx": "_mm_and_si128",
                "dst_ctx": "_mm_and_si128"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+128+_mm_min_epu16+_mm_min_epu16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1 0) (reg (bv #x02 8)) 128 128 0 128 16 0 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x02 8)) (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1 0) 128 128 0 128 16 0 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm_min_epu16",
                "dst_ctx": "_mm_min_epu16"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+512+_mm512_min_epi8+_mm512_min_epi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0) (reg (bv #x02 8)) 512 512 0 512 8 1 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x02 8)) (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0) 512 512 0 512 8 1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm512_min_epi8",
                "dst_ctx": "_mm512_min_epi8"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+256+_mm256_min_epi32+_mm256_min_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 8 1 0) (reg (bv #x01 8)) 256 256 0 256 32 1 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0) 256 256 0 256 32 1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm256_min_epi32",
                "dst_ctx": "_mm256_min_epi32"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+256+_mm256_min_epi64+_mm256_min_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0) (reg (bv #x02 8)) 256 256 0 256 64 1 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x02 8)) (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0) 256 256 0 256 64 1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm256_min_epi64",
                "dst_ctx": "_mm256_min_epi64"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+64+_mm_min_pi16+_mm_min_pi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 0) (reg (bv #x02 8)) 64 64 0 64 16 1 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x02 8)) (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0) 64 64 0 64 16 1 0)",
                "output_size": 64,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm_min_pi16",
                "dst_ctx": "_mm_min_pi16"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+256+_mm256_min_epu16+_mm256_min_epu16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0) (reg (bv #x01 8)) 256 256 0 256 16 0 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 32 0 0) 256 256 0 256 16 0 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm256_min_epu16",
                "dst_ctx": "_mm256_min_epu16"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+256+_mm256_min_epi16+_mm256_min_epi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0) (reg (bv #x02 8)) 256 256 0 256 16 1 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x02 8)) (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0) 256 256 0 256 16 1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm256_min_epi16",
                "dst_ctx": "_mm256_min_epi16"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+128+_mm_min_epi8+_mm_min_epi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0) 128 128 0 128 8 1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm_min_epi8",
                "dst_ctx": "_mm_min_epi8"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+512+_mm512_min_epu32+_mm512_min_epu32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 16 1 0) 512 512 0 512 32 0 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm512_min_epu32",
                "dst_ctx": "_mm512_min_epu32"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+256+_mm256_min_epu64+_mm256_min_epu64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0) (reg (bv #x01 8)) 256 256 0 256 64 0 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0) 256 256 0 256 64 0 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm256_min_epu64",
                "dst_ctx": "_mm256_min_epu64"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+64+_m_pminub+_m_pminub": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 0) (reg (bv #x01 8)) 64 64 0 64 8 0 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 0) 64 64 0 64 8 0 0)",
                "output_size": 64,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_m_pminub",
                "dst_ctx": "_m_pminub"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+512+_mm512_min_epi64+_mm512_min_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 16 1 0) (reg (bv #x00 8)) 512 512 0 512 64 1 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 16 1 0) 512 512 0 512 64 1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm512_min_epi64",
                "dst_ctx": "_mm512_min_epi64"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+128+_mm_min_epi16+_mm_min_epi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0) (reg (bv #x02 8)) 128 128 0 128 16 1 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x02 8)) (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0) 128 128 0 128 16 1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm_min_epi16",
                "dst_ctx": "_mm_min_epi16"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+128+_mm_min_epu32+_mm_min_epu32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 16 0 0) (reg (bv #x01 8)) 128 128 0 128 32 0 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0) 128 128 0 128 32 0 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm_min_epu32",
                "dst_ctx": "_mm_min_epu32"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+128+_mm_min_epu8+_mm_min_epu8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 8 1 0) (reg (bv #x01 8)) 128 128 0 128 8 0 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 8 1 0) 128 128 0 128 8 0 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm_min_epu8",
                "dst_ctx": "_mm_min_epu8"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+128+_mm_min_epi64+_mm_min_epi64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 16 0 0) (reg (bv #x01 8)) 128 128 0 128 64 1 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0) 128 128 0 128 64 1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm_min_epi64",
                "dst_ctx": "_mm_min_epi64"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+512+_mm512_min_epi16+_mm512_min_epi16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0) (reg (bv #x02 8)) 512 512 0 512 16 1 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x02 8)) (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0) 512 512 0 512 16 1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm512_min_epi16",
                "dst_ctx": "_mm512_min_epi16"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+512+_mm512_min_epu8+_mm512_min_epu8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0) (reg (bv #x02 8)) 512 512 0 512 8 0 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0) 512 512 0 512 8 0 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm512_min_epu8",
                "dst_ctx": "_mm512_min_epu8"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+128+_mm_min_epi32+_mm_min_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0) (reg (bv #x02 8)) 128 128 0 128 32 1 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x02 8)) (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0) 128 128 0 128 32 1 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm_min_epi32",
                "dst_ctx": "_mm_min_epi32"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+512+_mm512_min_epi32+_mm512_min_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0) (reg (bv #x01 8)) 512 512 0 512 32 1 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0) 512 512 0 512 32 1 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm512_min_epi32",
                "dst_ctx": "_mm512_min_epi32"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+128+_mm_min_epu64+_mm_min_epu64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 1 0) (reg (bv #x02 8)) 128 128 0 128 64 0 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x02 8)) (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 0) 128 128 0 128 64 0 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm_min_epu64",
                "dst_ctx": "_mm_min_epu64"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+256+_mm256_min_epu32+_mm256_min_epu32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0) (reg (bv #x01 8)) 256 256 0 256 32 0 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 8 0 0) 256 256 0 256 32 0 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm256_min_epu32",
                "dst_ctx": "_mm256_min_epu32"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+512+_mm512_min_epu16+_mm512_min_epu16": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 1 0) (reg (bv #x02 8)) 512 512 0 512 16 0 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x02 8)) (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 1 0) 512 512 0 512 16 0 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm512_min_epu16",
                "dst_ctx": "_mm512_min_epu16"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+512+_mm512_min_epu64+_mm512_min_epu64": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0 0) (reg (bv #x02 8)) 512 512 0 512 64 0 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x02 8)) (_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0 0) 512 512 0 512 64 0 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm512_min_epu64",
                "dst_ctx": "_mm512_min_epu64"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+256+_mm256_min_epu8+_mm256_min_epu8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 1 0) (reg (bv #x02 8)) 256 256 0 256 8 0 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x02 8)) (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 1 0) 256 256 0 256 8 0 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm256_min_epu8",
                "dst_ctx": "_mm256_min_epu8"
            }
        }
    ],
    " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+ (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )+512+_mm512_and_epi32+_mm512_and_epi32": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm512_and_epi32_dsl (_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0) (reg (bv #x02 8)) 512 512 0 512 32 0)",
                "dst": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (_mm512_and_epi32_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 32 0) 512 512 0 512 32 0)",
                "output_size": 512,
                "original_src_expr": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "original_dst_expr": " (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t (_mm512_and_epi32_dsl ; _mm512_and_epi32\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i8> False\n\t\t512\n\t\t512\n\t\t0\n\t\t512\n\t\t32\n\t\t0\n\t )\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )",
                "src_ctx": "_mm512_and_epi32",
                "dst_ctx": "_mm512_and_epi32"
            }
        }
    ],
    " (_m_por_dsl ; _m_por\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )+ (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )+64+_m_por+_m_por": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_m_por_dsl (_m_por_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 64 0 64 64 0 0) (reg (bv #x01 8)) 64 64 0 64 64 0 0)",
                "dst": "(_m_por_dsl (reg (bv #x02 8)) (_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0) 64 64 0 64 64 0 0)",
                "output_size": 64,
                "original_src_expr": " (_m_por_dsl ; _m_por\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_m_por",
                "dst_ctx": "_m_por"
            }
        }
    ],
    " (_m_por_dsl ; _m_por\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )+ (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )+256+_mm256_or_si256+_mm256_or_si256": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_m_por_dsl (_m_por_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 256 0 0) (reg (bv #x01 8)) 256 256 0 256 256 0 0)",
                "dst": "(_m_por_dsl (reg (bv #x01 8)) (_m_por_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 256 0 0) 256 256 0 256 256 0 0)",
                "output_size": 256,
                "original_src_expr": " (_m_por_dsl ; _m_por\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm256_or_si256",
                "dst_ctx": "_mm256_or_si256"
            }
        }
    ],
    " (_m_por_dsl ; _m_por\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )+ (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )+128+_mm_or_si128+_mm_or_si128": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_m_por_dsl (_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 128 0 0) (reg (bv #x02 8)) 128 128 0 128 128 0 0)",
                "dst": "(_m_por_dsl (reg (bv #x00 8)) (_m_por_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 128 0 0) 128 128 0 128 128 0 0)",
                "output_size": 128,
                "original_src_expr": " (_m_por_dsl ; _m_por\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm_or_si128",
                "dst_ctx": "_mm_or_si128"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+ (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )+256+_mm256_min_epi8+_mm256_min_epi8": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_mm_min_epu16_dsl (_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 256 256 0 256 8 1 0) (reg (bv #x01 8)) 256 256 0 256 8 1 0)",
                "dst": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (_mm_min_epu16_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0) 256 256 0 256 8 1 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (_mm_min_epu16_dsl ; _mm_min_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t (_mm_min_epu16_dsl ; _mm_min_epu16\n\t\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )",
                "src_ctx": "_mm256_min_epi8",
                "dst_ctx": "_mm256_min_epi8"
            }
        }
    ],
    " (_m_por_dsl ; _m_por\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )+ (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )+512+_mm512_or_si512+_mm512_or_si512": [
        {
            "property_name": "EnumeratePattern_assoc",
            "property": {
                "src": "(_m_por_dsl (_m_por_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 512 0 0) (reg (bv #x00 8)) 512 512 0 512 512 0 0)",
                "dst": "(_m_por_dsl (reg (bv #x01 8)) (_m_por_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 512 0 0) 512 512 0 512 512 0 0)",
                "output_size": 512,
                "original_src_expr": " (_m_por_dsl ; _m_por\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (_m_por_dsl ; _m_por\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t (_m_por_dsl ; _m_por\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i8> False\n\t\t64\n\t\t64\n\t\t0\n\t\t64\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t64\n\t64\n\t0\n\t64\n\t64\n\t0\n\t0\n )",
                "src_ctx": "_mm512_or_si512",
                "dst_ctx": "_mm512_or_si512"
            }
        }
    ]
}