x86_EnumeratePattern={
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+512+_mm512_or_epi32+typed-folded:vec-bwor-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512)",
                "output_size": 512,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm512_or_epi32",
                "dst_ctx": "typed-folded:vec-bwor-p32-s512"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+512+_mm512_or_epi32+typed-folded:vec-bwor-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512)",
                "output_size": 512,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm512_or_epi32",
                "dst_ctx": "typed-folded:vec-bwor-p16-s512"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+512+_mm512_or_epi32+typed-folded:vec-bwor-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512)",
                "output_size": 512,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm512_or_epi32",
                "dst_ctx": "typed-folded:vec-bwor-p8-s512"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+512+_mm512_or_epi32+typed-folded:vec-bwor-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512)",
                "output_size": 512,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm512_or_epi32",
                "dst_ctx": "typed-folded:vec-bwor-p64-s512"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+512+_mm512_or_epi64+typed-folded:vec-bwor-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512)",
                "output_size": 512,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm512_or_epi64",
                "dst_ctx": "typed-folded:vec-bwor-p64-s512"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+512+_mm512_or_epi64+typed-folded:vec-bwor-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512)",
                "output_size": 512,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm512_or_epi64",
                "dst_ctx": "typed-folded:vec-bwor-p16-s512"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+512+_mm512_or_epi64+typed-folded:vec-bwor-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512)",
                "output_size": 512,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm512_or_epi64",
                "dst_ctx": "typed-folded:vec-bwor-p8-s512"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+512+_mm512_or_epi64+typed-folded:vec-bwor-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512)",
                "output_size": 512,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm512_or_epi64",
                "dst_ctx": "typed-folded:vec-bwor-p32-s512"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+256+_mm256_or_epi32+typed-folded:vec-bwor-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256)",
                "output_size": 256,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm256_or_epi32",
                "dst_ctx": "typed-folded:vec-bwor-p32-s256"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+256+_mm256_or_epi32+typed-folded:vec-bwor-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256)",
                "output_size": 256,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm256_or_epi32",
                "dst_ctx": "typed-folded:vec-bwor-p16-s256"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+256+_mm256_or_epi32+typed-folded:vec-bwor-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 256)",
                "output_size": 256,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm256_or_epi32",
                "dst_ctx": "typed-folded:vec-bwor-p8-s256"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+256+_mm256_or_epi32+typed-folded:vec-bwor-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 256)",
                "output_size": 256,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm256_or_epi32",
                "dst_ctx": "typed-folded:vec-bwor-p64-s256"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+128+_mm_or_epi64+typed-folded:vec-bwor-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128)",
                "output_size": 128,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm_or_epi64",
                "dst_ctx": "typed-folded:vec-bwor-p16-s128"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+128+_mm_or_epi64+typed-folded:vec-bwor-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm_or_epi64",
                "dst_ctx": "typed-folded:vec-bwor-p8-s128"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+128+_mm_or_epi64+typed-folded:vec-bwor-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm_or_epi64",
                "dst_ctx": "typed-folded:vec-bwor-p32-s128"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+128+_mm_or_epi64+typed-folded:vec-bwor-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128)",
                "output_size": 128,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm_or_epi64",
                "dst_ctx": "typed-folded:vec-bwor-p64-s128"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+256+_mm256_or_epi64+typed-folded:vec-bwor-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 256)",
                "output_size": 256,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm256_or_epi64",
                "dst_ctx": "typed-folded:vec-bwor-p8-s256"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+256+_mm256_or_epi64+typed-folded:vec-bwor-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256)",
                "output_size": 256,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm256_or_epi64",
                "dst_ctx": "typed-folded:vec-bwor-p16-s256"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+256+_mm256_or_epi64+typed-folded:vec-bwor-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 256)",
                "output_size": 256,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm256_or_epi64",
                "dst_ctx": "typed-folded:vec-bwor-p64-s256"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+256+_mm256_or_epi64+typed-folded:vec-bwor-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256)",
                "output_size": 256,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm256_or_epi64",
                "dst_ctx": "typed-folded:vec-bwor-p32-s256"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+128+_mm_or_epi32+typed-folded:vec-bwor-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm_or_epi32",
                "dst_ctx": "typed-folded:vec-bwor-p8-s128"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+128+_mm_or_epi32+typed-folded:vec-bwor-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128)",
                "output_size": 128,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm_or_epi32",
                "dst_ctx": "typed-folded:vec-bwor-p16-s128"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+128+_mm_or_epi32+typed-folded:vec-bwor-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm_or_epi32",
                "dst_ctx": "typed-folded:vec-bwor-p32-s128"
            }
        }
    ],
    " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+128+_mm_or_epi32+typed-folded:vec-bwor-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128)",
                "output_size": 128,
                "original_src_expr": " (_mm512_or_epi32_dsl ; _mm512_or_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm_or_epi32",
                "dst_ctx": "typed-folded:vec-bwor-p64-s128"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+256+_mm256_max_epu64+typed-folded:vec-max-unsigned-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 256 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm256_max_epu64",
                "dst_ctx": "typed-folded:vec-max-unsigned-p64-s256"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+512+_mm512_max_epu64+typed-folded:vec-max-unsigned-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm512_max_epu64",
                "dst_ctx": "typed-folded:vec-max-unsigned-p64-s512"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+128+_mm_max_epi64+typed-folded:vec-max-signed-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm_max_epi64",
                "dst_ctx": "typed-folded:vec-max-signed-p64-s128"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+128+_mm_max_epu8+typed-folded:vec-max-unsigned-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm_max_epu8",
                "dst_ctx": "typed-folded:vec-max-unsigned-p8-s128"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+512+_mm512_max_epi16+typed-folded:vec-max-signed-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm512_max_epi16",
                "dst_ctx": "typed-folded:vec-max-signed-p16-s512"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+256+_mm256_max_epu32+typed-folded:vec-max-unsigned-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm256_max_epu32",
                "dst_ctx": "typed-folded:vec-max-unsigned-p32-s256"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+256+_mm256_max_epu8+typed-folded:vec-max-unsigned-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm256_max_epu8",
                "dst_ctx": "typed-folded:vec-max-unsigned-p8-s256"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+256+_mm256_max_epi64+typed-folded:vec-max-signed-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm256_max_epi64",
                "dst_ctx": "typed-folded:vec-max-signed-p64-s256"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+128+_mm_max_epi16+typed-folded:vec-max-signed-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm_max_epi16",
                "dst_ctx": "typed-folded:vec-max-signed-p16-s128"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+64+_m_pmaxsw+typed-folded:vec-max-signed-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64 1)",
                "output_size": 64,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_m_pmaxsw",
                "dst_ctx": "typed-folded:vec-max-signed-p16-s64"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+64+_mm_max_pu8+typed-folded:vec-max-unsigned-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64 0)",
                "output_size": 64,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm_max_pu8",
                "dst_ctx": "typed-folded:vec-max-unsigned-p8-s64"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+128+_mm_max_epi32+typed-folded:vec-max-signed-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm_max_epi32",
                "dst_ctx": "typed-folded:vec-max-signed-p32-s128"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+256+_mm256_max_epu16+typed-folded:vec-max-unsigned-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256 0)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm256_max_epu16",
                "dst_ctx": "typed-folded:vec-max-unsigned-p16-s256"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+128+_mm_max_epu32+typed-folded:vec-max-unsigned-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm_max_epu32",
                "dst_ctx": "typed-folded:vec-max-unsigned-p32-s128"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+512+_mm512_max_epi64+typed-folded:vec-max-signed-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm512_max_epi64",
                "dst_ctx": "typed-folded:vec-max-signed-p64-s512"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+256+_mm256_max_epi32+typed-folded:vec-max-signed-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm256_max_epi32",
                "dst_ctx": "typed-folded:vec-max-signed-p32-s256"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+512+_mm512_max_epi8+typed-folded:vec-max-signed-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm512_max_epi8",
                "dst_ctx": "typed-folded:vec-max-signed-p8-s512"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+128+_mm_max_epi8+typed-folded:vec-max-signed-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm_max_epi8",
                "dst_ctx": "typed-folded:vec-max-signed-p8-s128"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+256+_mm256_max_epi8+typed-folded:vec-max-signed-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm256_max_epi8",
                "dst_ctx": "typed-folded:vec-max-signed-p8-s256"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+128+_mm_max_epu64+typed-folded:vec-max-unsigned-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm_max_epu64",
                "dst_ctx": "typed-folded:vec-max-unsigned-p64-s128"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+128+_mm_max_epu16+typed-folded:vec-max-unsigned-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 0)",
                "output_size": 128,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm_max_epu16",
                "dst_ctx": "typed-folded:vec-max-unsigned-p16-s128"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+512+_mm512_max_epi32+typed-folded:vec-max-signed-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm512_max_epi32",
                "dst_ctx": "typed-folded:vec-max-signed-p32-s512"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+512+_mm512_max_epu32+typed-folded:vec-max-unsigned-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm512_max_epu32",
                "dst_ctx": "typed-folded:vec-max-unsigned-p32-s512"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+256+_mm256_max_epi16+typed-folded:vec-max-signed-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm256_max_epi16",
                "dst_ctx": "typed-folded:vec-max-signed-p16-s256"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+512+_mm512_max_epu8+typed-folded:vec-max-unsigned-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm512_max_epu8",
                "dst_ctx": "typed-folded:vec-max-unsigned-p8-s512"
            }
        }
    ],
    " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )+ (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )+512+_mm512_max_epu16+typed-folded:vec-max-unsigned-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 0)",
                "output_size": 512,
                "original_src_expr": " (_mm256_max_epu64_dsl ; _mm512_max_epu16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-max_dsl ; typed-folded:vec-max-unsigned-p16-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t0\n )",
                "src_ctx": "_mm512_max_epu16",
                "dst_ctx": "typed-folded:vec-max-unsigned-p16-s512"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+64+_m_por+typed-folded:vec-bwor-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)",
                "output_size": 64,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_m_por",
                "dst_ctx": "typed-folded:vec-bwor-p8-s64"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+64+_m_por+typed-folded:vec-bwor-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64)",
                "output_size": 64,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_m_por",
                "dst_ctx": "typed-folded:vec-bwor-p16-s64"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+64+_m_por+typed-folded:vec-bwor-p32-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64)",
                "output_size": 64,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_m_por",
                "dst_ctx": "typed-folded:vec-bwor-p32-s64"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+64+_m_por+typed-folded:vec-bwor-p64-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)",
                "output_size": 64,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_m_por",
                "dst_ctx": "typed-folded:vec-bwor-p64-s64"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+256+_mm256_or_si256+typed-folded:vec-bwor-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 256 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256)",
                "output_size": 256,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm256_or_si256",
                "dst_ctx": "typed-folded:vec-bwor-p8-s256"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+256+_mm256_or_si256+typed-folded:vec-bwor-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 256 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 256)",
                "output_size": 256,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm256_or_si256",
                "dst_ctx": "typed-folded:vec-bwor-p16-s256"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+256+_mm256_or_si256+typed-folded:vec-bwor-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 256 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256)",
                "output_size": 256,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm256_or_si256",
                "dst_ctx": "typed-folded:vec-bwor-p32-s256"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+256+_mm256_or_si256+typed-folded:vec-bwor-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 256 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 256)",
                "output_size": 256,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm256_or_si256",
                "dst_ctx": "typed-folded:vec-bwor-p64-s256"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+128+_mm_or_si128+typed-folded:vec-bwor-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 128 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm_or_si128",
                "dst_ctx": "typed-folded:vec-bwor-p8-s128"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+128+_mm_or_si128+typed-folded:vec-bwor-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 128 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128)",
                "output_size": 128,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm_or_si128",
                "dst_ctx": "typed-folded:vec-bwor-p16-s128"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+128+_mm_or_si128+typed-folded:vec-bwor-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 128 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm_or_si128",
                "dst_ctx": "typed-folded:vec-bwor-p32-s128"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+128+_mm_or_si128+typed-folded:vec-bwor-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 128 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128)",
                "output_size": 128,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm_or_si128",
                "dst_ctx": "typed-folded:vec-bwor-p64-s128"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+512+_mm512_or_si512+typed-folded:vec-bwor-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 512 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512)",
                "output_size": 512,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm512_or_si512",
                "dst_ctx": "typed-folded:vec-bwor-p8-s512"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+512+_mm512_or_si512+typed-folded:vec-bwor-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 512 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512)",
                "output_size": 512,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm512_or_si512",
                "dst_ctx": "typed-folded:vec-bwor-p16-s512"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+512+_mm512_or_si512+typed-folded:vec-bwor-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 512 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512)",
                "output_size": 512,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm512_or_si512",
                "dst_ctx": "typed-folded:vec-bwor-p32-s512"
            }
        }
    ],
    " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )+ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )+512+_mm512_or_si512+typed-folded:vec-bwor-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 512 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512)",
                "output_size": 512,
                "original_src_expr": " (_m_por_dsl ; _mm512_or_si512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t512\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n )",
                "src_ctx": "_mm512_or_si512",
                "dst_ctx": "typed-folded:vec-bwor-p64-s512"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+64+_mm_add_pi8+typed-folded:vec-add-nosigned-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_add_pi8",
                "dst_ctx": "typed-folded:vec-add-nosigned-p8-s64"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+64+_mm_adds_pi16+typed-folded:vec-add-signed-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64 1)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_adds_pi16",
                "dst_ctx": "typed-folded:vec-add-signed-p16-s64"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+256+_mm256_add_epi16+typed-folded:vec-add-nosigned-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm256_add_epi16",
                "dst_ctx": "typed-folded:vec-add-nosigned-p16-s256"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+128+_mm_adds_epu16+typed-folded:vec-add-unsigned-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_adds_epu16",
                "dst_ctx": "typed-folded:vec-add-unsigned-p16-s128"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+128+_mm_add_epi32+typed-folded:vec-add-nosigned-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_add_epi32",
                "dst_ctx": "typed-folded:vec-add-nosigned-p32-s128"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+256+_mm256_adds_epu8+typed-folded:vec-add-unsigned-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm256_adds_epu8",
                "dst_ctx": "typed-folded:vec-add-unsigned-p8-s256"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+256+_mm256_adds_epi16+typed-folded:vec-add-signed-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm256_adds_epi16",
                "dst_ctx": "typed-folded:vec-add-signed-p16-s256"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+64+_m_paddw+typed-folded:vec-add-nosigned-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_m_paddw",
                "dst_ctx": "typed-folded:vec-add-nosigned-p16-s64"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+64+_mm_adds_pu16+typed-folded:vec-add-unsigned-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64 0)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_adds_pu16",
                "dst_ctx": "typed-folded:vec-add-unsigned-p16-s64"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+128+_mm_add_epi16+typed-folded:vec-add-nosigned-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_add_epi16",
                "dst_ctx": "typed-folded:vec-add-nosigned-p16-s128"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+256+_mm256_adds_epu16+typed-folded:vec-add-unsigned-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm256_adds_epu16",
                "dst_ctx": "typed-folded:vec-add-unsigned-p16-s256"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+128+_mm_adds_epu8+typed-folded:vec-add-unsigned-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_adds_epu8",
                "dst_ctx": "typed-folded:vec-add-unsigned-p8-s128"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+512+_mm512_add_epi16+typed-folded:vec-add-nosigned-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm512_add_epi16",
                "dst_ctx": "typed-folded:vec-add-nosigned-p16-s512"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+256+_mm256_adds_epi8+typed-folded:vec-add-signed-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm256_adds_epi8",
                "dst_ctx": "typed-folded:vec-add-signed-p8-s256"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+64+_mm_adds_pi8+typed-folded:vec-add-signed-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64 1)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_adds_pi8",
                "dst_ctx": "typed-folded:vec-add-signed-p8-s64"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+512+_mm512_add_epi64+typed-folded:vec-add-nosigned-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm512_add_epi64",
                "dst_ctx": "typed-folded:vec-add-nosigned-p64-s512"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+64+_mm_add_pi32+typed-folded:vec-add-nosigned-p32-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_add_pi32",
                "dst_ctx": "typed-folded:vec-add-nosigned-p32-s64"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+512+_mm512_add_epi32+typed-folded:vec-add-nosigned-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm512_add_epi32",
                "dst_ctx": "typed-folded:vec-add-nosigned-p32-s512"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+512+_mm512_adds_epu8+typed-folded:vec-add-unsigned-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm512_adds_epu8",
                "dst_ctx": "typed-folded:vec-add-unsigned-p8-s512"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+256+_mm256_add_epi64+typed-folded:vec-add-nosigned-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm256_add_epi64",
                "dst_ctx": "typed-folded:vec-add-nosigned-p64-s256"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+128+_mm_add_epi8+typed-folded:vec-add-nosigned-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_add_epi8",
                "dst_ctx": "typed-folded:vec-add-nosigned-p8-s128"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+128+_mm_adds_epi16+typed-folded:vec-add-signed-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_adds_epi16",
                "dst_ctx": "typed-folded:vec-add-signed-p16-s128"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+64+_mm_adds_pu8+typed-folded:vec-add-unsigned-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64 0)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_adds_pu8",
                "dst_ctx": "typed-folded:vec-add-unsigned-p8-s64"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+256+_mm256_add_epi8+typed-folded:vec-add-nosigned-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm256_add_epi8",
                "dst_ctx": "typed-folded:vec-add-nosigned-p8-s256"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+512+_mm512_add_epi8+typed-folded:vec-add-nosigned-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm512_add_epi8",
                "dst_ctx": "typed-folded:vec-add-nosigned-p8-s512"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+512+_mm512_adds_epi16+typed-folded:vec-add-signed-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm512_adds_epi16",
                "dst_ctx": "typed-folded:vec-add-signed-p16-s512"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+128+_mm_add_epi64+typed-folded:vec-add-nosigned-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_add_epi64",
                "dst_ctx": "typed-folded:vec-add-nosigned-p64-s128"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+512+_mm512_adds_epi8+typed-folded:vec-add-signed-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm512_adds_epi8",
                "dst_ctx": "typed-folded:vec-add-signed-p8-s512"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+128+_mm_adds_epi8+typed-folded:vec-add-signed-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm_adds_epi8",
                "dst_ctx": "typed-folded:vec-add-signed-p8-s128"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+512+_mm512_adds_epu16+typed-folded:vec-add-unsigned-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm512_adds_epu16",
                "dst_ctx": "typed-folded:vec-add-unsigned-p16-s512"
            }
        }
    ],
    " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )+256+_mm256_add_epi32+typed-folded:vec-add-nosigned-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_mm_add_pi8_dsl ; _mm512_adds_epu8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-unsigned-p8-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t0\n )",
                "src_ctx": "_mm256_add_epi32",
                "dst_ctx": "typed-folded:vec-add-nosigned-p32-s256"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+512+_mm512_rem_epu32+typed-folded:vec-mod-signed-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm512_rem_epu32",
                "dst_ctx": "typed-folded:vec-mod-signed-p32-s512"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+256+_mm256_rem_epi16+typed-folded:vec-mod-signed-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm256_rem_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p16-s256"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+128+_mm_irem_epi32+typed-folded:vec-mod-signed-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_irem_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p32-s128"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+256+_mm256_rem_epi8+typed-folded:vec-mod-signed-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm256_rem_epi8",
                "dst_ctx": "typed-folded:vec-mod-signed-p8-s256"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+256+_mm256_rem_epu64+typed-folded:vec-mod-signed-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm256_rem_epu64",
                "dst_ctx": "typed-folded:vec-mod-signed-p64-s256"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+512+_mm512_rem_epi16+typed-folded:vec-mod-signed-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm512_rem_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p16-s512"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+256+_mm256_rem_epi32+typed-folded:vec-mod-signed-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm256_rem_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p32-s256"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+128+_mm_rem_epu64+typed-folded:vec-mod-signed-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_rem_epu64",
                "dst_ctx": "typed-folded:vec-mod-signed-p64-s128"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+512+_mm512_rem_epu64+typed-folded:vec-mod-signed-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm512_rem_epu64",
                "dst_ctx": "typed-folded:vec-mod-signed-p64-s512"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+128+_mm_rem_epi16+typed-folded:vec-mod-signed-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_rem_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p16-s128"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+512+_mm512_rem_epi8+typed-folded:vec-mod-signed-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm512_rem_epi8",
                "dst_ctx": "typed-folded:vec-mod-signed-p8-s512"
            }
        }
    ],
    " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+128+_mm_rem_epu8+typed-folded:vec-mod-signed-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm512_rem_epu32_dsl ; _mm512_rem_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_rem_epu8",
                "dst_ctx": "typed-folded:vec-mod-signed-p8-s128"
            }
        }
    ],
    " (_mm_add_si64_dsl ; _mm_add_si64\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )+ (typed-folded:vec-add_dsl ; typed-folded:vec-add-nosigned-p64-s64\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t-1\n )+64+_mm_add_si64+typed-folded:vec-add-nosigned-p64-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_mm_add_si64_dsl ; _mm_add_si64\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-add_dsl ; typed-folded:vec-add-nosigned-p64-s64\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t-1\n )",
                "src_ctx": "_mm_add_si64",
                "dst_ctx": "typed-folded:vec-add-nosigned-p64-s64"
            }
        }
    ],
    " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s64\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t-1\n )+64+_mm_sub_si64+typed-folded:vec-sub-nosigned-p64-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_mm_sub_si64_dsl ; _mm_sub_si64\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t64\n\t-1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s64\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t-1\n )",
                "src_ctx": "_mm_sub_si64",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p64-s64"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+128+_mm_min_epu16+typed-folded:vec-min-unsigned-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm_min_epu16",
                "dst_ctx": "typed-folded:vec-min-unsigned-p16-s128"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+512+_mm512_min_epi8+typed-folded:vec-min-signed-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm512_min_epi8",
                "dst_ctx": "typed-folded:vec-min-signed-p8-s512"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+256+_mm256_min_epi32+typed-folded:vec-min-signed-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm256_min_epi32",
                "dst_ctx": "typed-folded:vec-min-signed-p32-s256"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+256+_mm256_min_epi64+typed-folded:vec-min-signed-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm256_min_epi64",
                "dst_ctx": "typed-folded:vec-min-signed-p64-s256"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+64+_mm_min_pi16+typed-folded:vec-min-signed-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64 1)",
                "output_size": 64,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm_min_pi16",
                "dst_ctx": "typed-folded:vec-min-signed-p16-s64"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+256+_mm256_min_epu16+typed-folded:vec-min-unsigned-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm256_min_epu16",
                "dst_ctx": "typed-folded:vec-min-unsigned-p16-s256"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+256+_mm256_min_epi16+typed-folded:vec-min-signed-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm256_min_epi16",
                "dst_ctx": "typed-folded:vec-min-signed-p16-s256"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+128+_mm_min_epi8+typed-folded:vec-min-signed-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm_min_epi8",
                "dst_ctx": "typed-folded:vec-min-signed-p8-s128"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+512+_mm512_min_epu32+typed-folded:vec-min-unsigned-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm512_min_epu32",
                "dst_ctx": "typed-folded:vec-min-unsigned-p32-s512"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+256+_mm256_min_epu64+typed-folded:vec-min-unsigned-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 256 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm256_min_epu64",
                "dst_ctx": "typed-folded:vec-min-unsigned-p64-s256"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+64+_m_pminub+typed-folded:vec-min-unsigned-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64 0)",
                "output_size": 64,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_m_pminub",
                "dst_ctx": "typed-folded:vec-min-unsigned-p8-s64"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+512+_mm512_min_epi64+typed-folded:vec-min-signed-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm512_min_epi64",
                "dst_ctx": "typed-folded:vec-min-signed-p64-s512"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+128+_mm_min_epi16+typed-folded:vec-min-signed-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm_min_epi16",
                "dst_ctx": "typed-folded:vec-min-signed-p16-s128"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+128+_mm_min_epu32+typed-folded:vec-min-unsigned-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm_min_epu32",
                "dst_ctx": "typed-folded:vec-min-unsigned-p32-s128"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+128+_mm_min_epu8+typed-folded:vec-min-unsigned-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm_min_epu8",
                "dst_ctx": "typed-folded:vec-min-unsigned-p8-s128"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+128+_mm_min_epi64+typed-folded:vec-min-signed-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm_min_epi64",
                "dst_ctx": "typed-folded:vec-min-signed-p64-s128"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+512+_mm512_min_epi16+typed-folded:vec-min-signed-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm512_min_epi16",
                "dst_ctx": "typed-folded:vec-min-signed-p16-s512"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+512+_mm512_min_epu8+typed-folded:vec-min-unsigned-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm512_min_epu8",
                "dst_ctx": "typed-folded:vec-min-unsigned-p8-s512"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+128+_mm_min_epi32+typed-folded:vec-min-signed-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm_min_epi32",
                "dst_ctx": "typed-folded:vec-min-signed-p32-s128"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+512+_mm512_min_epi32+typed-folded:vec-min-signed-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm512_min_epi32",
                "dst_ctx": "typed-folded:vec-min-signed-p32-s512"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+128+_mm_min_epu64+typed-folded:vec-min-unsigned-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 0)",
                "output_size": 128,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm_min_epu64",
                "dst_ctx": "typed-folded:vec-min-unsigned-p64-s128"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+256+_mm256_min_epu32+typed-folded:vec-min-unsigned-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm256_min_epu32",
                "dst_ctx": "typed-folded:vec-min-unsigned-p32-s256"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+512+_mm512_min_epu16+typed-folded:vec-min-unsigned-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm512_min_epu16",
                "dst_ctx": "typed-folded:vec-min-unsigned-p16-s512"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+512+_mm512_min_epu64+typed-folded:vec-min-unsigned-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 0)",
                "output_size": 512,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm512_min_epu64",
                "dst_ctx": "typed-folded:vec-min-unsigned-p64-s512"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+256+_mm256_min_epu8+typed-folded:vec-min-unsigned-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 256 0)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm256_min_epu8",
                "dst_ctx": "typed-folded:vec-min-unsigned-p8-s256"
            }
        }
    ],
    " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )+ (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )+256+_mm256_min_epi8+typed-folded:vec-min-signed-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm_min_epu16_dsl ; _mm512_min_epi8\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-min_dsl ; typed-folded:vec-min-signed-p8-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t8\n\t512\n\t1\n )",
                "src_ctx": "_mm256_min_epi8",
                "dst_ctx": "typed-folded:vec-min-signed-p8-s256"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+512+_mm512_subs_epi8+typed-folded:vec-sub-signed-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm512_subs_epi8",
                "dst_ctx": "typed-folded:vec-sub-signed-p8-s512"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+128+_mm_subs_epu16+typed-folded:vec-sub-unsigned-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 0)",
                "output_size": 128,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_subs_epu16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p16-s128"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+64+_mm_subs_pu16+typed-folded:vec-sub-unsigned-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64 0)",
                "output_size": 64,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_subs_pu16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p16-s64"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+64+_m_psubb+typed-folded:vec-sub-nosigned-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_m_psubb",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p8-s64"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+512+_mm512_subs_epi16+typed-folded:vec-sub-signed-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 1)",
                "output_size": 512,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm512_subs_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p16-s512"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+512+_mm512_subs_epu16+typed-folded:vec-sub-unsigned-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)",
                "output_size": 512,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm512_subs_epu16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p16-s512"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+128+_mm_sub_epi16+typed-folded:vec-sub-nosigned-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_sub_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p16-s128"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+64+_m_psubsw+typed-folded:vec-sub-signed-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64 1)",
                "output_size": 64,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_m_psubsw",
                "dst_ctx": "typed-folded:vec-sub-signed-p16-s64"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+64+_mm_sub_pi16+typed-folded:vec-sub-nosigned-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_sub_pi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p16-s64"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+512+_mm512_sub_epi64+typed-folded:vec-sub-nosigned-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm512_sub_epi64",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p64-s512"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+128+_mm_subs_epi16+typed-folded:vec-sub-signed-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_subs_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p16-s128"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+256+_mm256_sub_epi8+typed-folded:vec-sub-nosigned-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm256_sub_epi8",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p8-s256"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+512+_mm512_sub_epi32+typed-folded:vec-sub-nosigned-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm512_sub_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p32-s512"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+128+_mm_sub_epi32+typed-folded:vec-sub-nosigned-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_sub_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p32-s128"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+512+_mm512_sub_epi16+typed-folded:vec-sub-nosigned-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm512_sub_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p16-s512"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+256+_mm256_subs_epu8+typed-folded:vec-sub-unsigned-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 256 0)",
                "output_size": 256,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm256_subs_epu8",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p8-s256"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+64+_m_psubd+typed-folded:vec-sub-nosigned-p32-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_m_psubd",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p32-s64"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+512+_mm512_sub_epi8+typed-folded:vec-sub-nosigned-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm512_sub_epi8",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p8-s512"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+512+_mm512_subs_epu8+typed-folded:vec-sub-unsigned-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 0)",
                "output_size": 512,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm512_subs_epu8",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p8-s512"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+256+_mm256_subs_epi8+typed-folded:vec-sub-signed-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm256_subs_epi8",
                "dst_ctx": "typed-folded:vec-sub-signed-p8-s256"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+128+_mm_sub_epi8+typed-folded:vec-sub-nosigned-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_sub_epi8",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p8-s128"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+64+_m_psubsb+typed-folded:vec-sub-signed-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64 1)",
                "output_size": 64,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_m_psubsb",
                "dst_ctx": "typed-folded:vec-sub-signed-p8-s64"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+128+_mm_subs_epu8+typed-folded:vec-sub-unsigned-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)",
                "output_size": 128,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_subs_epu8",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p8-s128"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+128+_mm_subs_epi8+typed-folded:vec-sub-signed-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)",
                "output_size": 128,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_subs_epi8",
                "dst_ctx": "typed-folded:vec-sub-signed-p8-s128"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+256+_mm256_subs_epi16+typed-folded:vec-sub-signed-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256 1)",
                "output_size": 256,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm256_subs_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p16-s256"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+128+_mm_sub_epi64+typed-folded:vec-sub-nosigned-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm_sub_epi64",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p64-s128"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+64+_m_psubusb+typed-folded:vec-sub-unsigned-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64 0)",
                "output_size": 64,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_m_psubusb",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p8-s64"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+256+_mm256_subs_epu16+typed-folded:vec-sub-unsigned-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 256 0)",
                "output_size": 256,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm256_subs_epu16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p16-s256"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+256+_mm256_sub_epi64+typed-folded:vec-sub-nosigned-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm256_sub_epi64",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p64-s256"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+256+_mm256_sub_epi16+typed-folded:vec-sub-nosigned-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm256_sub_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p16-s256"
            }
        }
    ],
    " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )+256+_mm256_sub_epi32+typed-folded:vec-sub-nosigned-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_mm512_subs_epi8_dsl ; _mm512_subs_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-signed-p16-s512\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t16\n\t512\n\t1\n )",
                "src_ctx": "_mm256_sub_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p32-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi16+typed-folded:vec-mod-unsigned-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p8-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi16+typed-folded:vec-mod-signed-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p8-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi16+typed-folded:vec-mod-signed-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p16-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi16+typed-folded:vec-mod-unsigned-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p16-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi16+typed-folded:vec-mod-signed-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p32-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi16+typed-folded:vec-mod-unsigned-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p32-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi16+typed-folded:vec-mod-signed-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p64-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi16+typed-folded:vec-mod-unsigned-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p64-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrlw+typed-folded:vec-mod-signed-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-mod-signed-p8-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrlw+typed-folded:vec-mod-unsigned-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p16-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrlw+typed-folded:vec-mod-signed-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-mod-signed-p16-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrlw+typed-folded:vec-mod-unsigned-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p8-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrlw+typed-folded:vec-mod-signed-p32-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-mod-signed-p32-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrlw+typed-folded:vec-mod-unsigned-p32-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p32-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrlw+typed-folded:vec-mod-unsigned-p64-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p64-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrlw+typed-folded:vec-mod-signed-p64-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-mod-signed-p64-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi16+typed-folded:vec-mod-signed-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p8-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi16+typed-folded:vec-mod-unsigned-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p8-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi16+typed-folded:vec-mod-unsigned-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p16-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi16+typed-folded:vec-mod-signed-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p16-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi16+typed-folded:vec-mod-signed-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p32-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi16+typed-folded:vec-mod-unsigned-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p32-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi16+typed-folded:vec-mod-signed-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p64-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi16+typed-folded:vec-mod-unsigned-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p64-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_sll_epi16+typed-folded:vec-mod-signed-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p8-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_sll_epi16+typed-folded:vec-mod-unsigned-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p8-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_sll_epi16+typed-folded:vec-mod-signed-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p16-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_sll_epi16+typed-folded:vec-mod-unsigned-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p16-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_sll_epi16+typed-folded:vec-mod-signed-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p32-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_sll_epi16+typed-folded:vec-mod-unsigned-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p32-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_sll_epi16+typed-folded:vec-mod-signed-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-mod-signed-p64-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_sll_epi16+typed-folded:vec-mod-unsigned-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p64-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrld+typed-folded:vec-mod-signed-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-mod-signed-p8-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrld+typed-folded:vec-mod-unsigned-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p8-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrld+typed-folded:vec-mod-signed-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-mod-signed-p16-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrld+typed-folded:vec-mod-unsigned-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p16-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrld+typed-folded:vec-mod-signed-p32-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-mod-signed-p32-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrld+typed-folded:vec-mod-unsigned-p32-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p32-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrld+typed-folded:vec-mod-signed-p64-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-mod-signed-p64-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+64+_m_psrld+typed-folded:vec-mod-unsigned-p64-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p64-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi32+typed-folded:vec-mod-signed-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p8-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi32+typed-folded:vec-mod-unsigned-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p8-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi32+typed-folded:vec-mod-signed-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p16-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi32+typed-folded:vec-mod-unsigned-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p16-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi32+typed-folded:vec-mod-signed-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p32-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi32+typed-folded:vec-mod-unsigned-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p32-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi32+typed-folded:vec-mod-signed-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p64-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+256+_mm256_srl_epi32+typed-folded:vec-mod-unsigned-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p64-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi32+typed-folded:vec-mod-signed-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p8-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi32+typed-folded:vec-mod-unsigned-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p8-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi32+typed-folded:vec-mod-signed-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p16-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi32+typed-folded:vec-mod-unsigned-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p16-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi32+typed-folded:vec-mod-signed-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p32-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi32+typed-folded:vec-mod-unsigned-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p32-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi32+typed-folded:vec-mod-signed-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p64-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+512+_mm512_srl_epi32+typed-folded:vec-mod-unsigned-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p64-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_srl_epi32+typed-folded:vec-mod-unsigned-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p8-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_srl_epi32+typed-folded:vec-mod-unsigned-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p16-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_srl_epi32+typed-folded:vec-mod-signed-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p16-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_srl_epi32+typed-folded:vec-mod-signed-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p8-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_srl_epi32+typed-folded:vec-mod-signed-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p32-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_srl_epi32+typed-folded:vec-mod-signed-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-signed-p64-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_srl_epi32+typed-folded:vec-mod-unsigned-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p32-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )+128+_mm_srl_epi32+typed-folded:vec-mod-unsigned-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-mod_dsl ; typed-folded:vec-mod-unsigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t0\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-mod-unsigned-p64-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrld+typed-folded:vec-sub-signed-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-sub-signed-p8-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrld+typed-folded:vec-sub-unsigned-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p8-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrld+typed-folded:vec-sub-signed-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-sub-signed-p16-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrld+typed-folded:vec-sub-nosigned-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p8-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrld+typed-folded:vec-sub-unsigned-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p16-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrld+typed-folded:vec-sub-nosigned-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p16-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrld+typed-folded:vec-sub-signed-p32-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-sub-signed-p32-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrld+typed-folded:vec-sub-unsigned-p32-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p32-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrld+typed-folded:vec-sub-nosigned-p32-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p32-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrld+typed-folded:vec-sub-signed-p64-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-sub-signed-p64-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrld+typed-folded:vec-sub-nosigned-p64-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p64-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrld+typed-folded:vec-sub-unsigned-p64-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrld",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p64-s64"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi32+typed-folded:vec-sub-signed-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-signed-p8-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi32+typed-folded:vec-sub-unsigned-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p8-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi32+typed-folded:vec-sub-nosigned-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p8-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi32+typed-folded:vec-sub-signed-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-signed-p16-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi32+typed-folded:vec-sub-unsigned-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p16-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi32+typed-folded:vec-sub-nosigned-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p16-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi32+typed-folded:vec-sub-signed-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-signed-p32-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi32+typed-folded:vec-sub-unsigned-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p32-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi32+typed-folded:vec-sub-nosigned-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p32-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi32+typed-folded:vec-sub-signed-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-signed-p64-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi32+typed-folded:vec-sub-unsigned-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p64-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi32+typed-folded:vec-sub-nosigned-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 256 256 0 256 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p64-s256"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi32+typed-folded:vec-sub-signed-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-signed-p8-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi32+typed-folded:vec-sub-unsigned-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p8-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi32+typed-folded:vec-sub-nosigned-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p8-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi32+typed-folded:vec-sub-signed-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-signed-p16-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi32+typed-folded:vec-sub-unsigned-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p16-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi32+typed-folded:vec-sub-nosigned-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p16-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi32+typed-folded:vec-sub-signed-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-signed-p32-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi32+typed-folded:vec-sub-unsigned-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p32-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi32+typed-folded:vec-sub-nosigned-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p32-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi32+typed-folded:vec-sub-signed-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-signed-p64-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi32+typed-folded:vec-sub-unsigned-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p64-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi32+typed-folded:vec-sub-nosigned-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p64-s512"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_srl_epi32+typed-folded:vec-sub-signed-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-signed-p8-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_srl_epi32+typed-folded:vec-sub-unsigned-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p8-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_srl_epi32+typed-folded:vec-sub-signed-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-signed-p16-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_srl_epi32+typed-folded:vec-sub-nosigned-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p8-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_srl_epi32+typed-folded:vec-sub-unsigned-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p16-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_srl_epi32+typed-folded:vec-sub-nosigned-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p16-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_srl_epi32+typed-folded:vec-sub-signed-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-signed-p32-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_srl_epi32+typed-folded:vec-sub-unsigned-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p32-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_srl_epi32+typed-folded:vec-sub-nosigned-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p32-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_srl_epi32+typed-folded:vec-sub-signed-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-signed-p64-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_srl_epi32+typed-folded:vec-sub-nosigned-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p64-s128"
            }
        }
    ],
    " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_srl_epi32+typed-folded:vec-sub-unsigned-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 32 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_psrld_dsl ; _mm512_srl_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000001f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t32\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_srl_epi32",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p64-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi16+typed-folded:vec-sub-nosigned-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p8-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi16+typed-folded:vec-sub-unsigned-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p8-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi16+typed-folded:vec-sub-signed-p8-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p8-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi16+typed-folded:vec-sub-signed-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p16-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi16+typed-folded:vec-sub-unsigned-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p16-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi16+typed-folded:vec-sub-signed-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p32-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi16+typed-folded:vec-sub-nosigned-p16-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p16-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi16+typed-folded:vec-sub-unsigned-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p32-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi16+typed-folded:vec-sub-nosigned-p32-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p32-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi16+typed-folded:vec-sub-unsigned-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256 0)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p64-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi16+typed-folded:vec-sub-signed-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256 1)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p64-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+256+_mm256_srl_epi16+typed-folded:vec-sub-nosigned-p64-s256": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 256 256 0 256 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 256 -1)",
                "output_size": 256,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm256_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p64-s256"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrlw+typed-folded:vec-sub-signed-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-sub-signed-p8-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrlw+typed-folded:vec-sub-unsigned-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p8-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrlw+typed-folded:vec-sub-nosigned-p8-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p8-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrlw+typed-folded:vec-sub-signed-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-sub-signed-p16-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrlw+typed-folded:vec-sub-unsigned-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p16-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrlw+typed-folded:vec-sub-unsigned-p32-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p32-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrlw+typed-folded:vec-sub-signed-p32-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-sub-signed-p32-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrlw+typed-folded:vec-sub-nosigned-p16-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p16-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrlw+typed-folded:vec-sub-nosigned-p32-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p32-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrlw+typed-folded:vec-sub-signed-p64-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 1)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-sub-signed-p64-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrlw+typed-folded:vec-sub-unsigned-p64-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p64-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+64+_m_psrlw+typed-folded:vec-sub-nosigned-p64-s64": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 -1)",
                "output_size": 64,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_m_psrlw",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p64-s64"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi16+typed-folded:vec-sub-signed-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p8-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi16+typed-folded:vec-sub-unsigned-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p8-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi16+typed-folded:vec-sub-nosigned-p8-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p8-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi16+typed-folded:vec-sub-signed-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p16-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi16+typed-folded:vec-sub-unsigned-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p16-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi16+typed-folded:vec-sub-nosigned-p16-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p16-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi16+typed-folded:vec-sub-unsigned-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p32-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi16+typed-folded:vec-sub-signed-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p32-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi16+typed-folded:vec-sub-nosigned-p32-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p32-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi16+typed-folded:vec-sub-signed-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 1)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p64-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi16+typed-folded:vec-sub-nosigned-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 -1)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p64-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+512+_mm512_srl_epi16+typed-folded:vec-sub-unsigned-p64-s512": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 512 512 0 512 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 512 0)",
                "output_size": 512,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm512_srl_epi16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p64-s512"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_sll_epi16+typed-folded:vec-sub-signed-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p8-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_sll_epi16+typed-folded:vec-sub-signed-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p16-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_sll_epi16+typed-folded:vec-sub-nosigned-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p8-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_sll_epi16+typed-folded:vec-sub-unsigned-p8-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p8-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_sll_epi16+typed-folded:vec-sub-unsigned-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p16-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_sll_epi16+typed-folded:vec-sub-unsigned-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p32-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_sll_epi16+typed-folded:vec-sub-nosigned-p16-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p16-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_sll_epi16+typed-folded:vec-sub-signed-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p32-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_sll_epi16+typed-folded:vec-sub-nosigned-p32-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p32-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_sll_epi16+typed-folded:vec-sub-nosigned-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128 -1)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-sub-nosigned-p64-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_sll_epi16+typed-folded:vec-sub-unsigned-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128 0)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-sub-unsigned-p64-s128"
            }
        }
    ],
    " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )+ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )+128+_mm_sll_epi16+typed-folded:vec-sub-signed-p64-s128": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 128 128 0 128 16 0 64 0 16 0 64 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128 1)",
                "output_size": 128,
                "original_src_expr": " (_m_pslld_dsl ; _mm512_srl_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t64\n\t0\n\t16\n\t0\n\t64\n\t0\n\t0\n )",
                "original_dst_expr": " (typed-folded:vec-sub_dsl ; typed-folded:vec-sub-nosigned-p64-s512\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t64\n\t512\n\t-1\n )",
                "src_ctx": "_mm_sll_epi16",
                "dst_ctx": "typed-folded:vec-sub-signed-p64-s128"
            }
        }
    ]
}