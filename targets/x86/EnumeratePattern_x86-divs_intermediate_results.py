{
    " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )+ (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+512+_mm512_div_epu32+typed:unsigned-vec-div_p32_s512_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0 64 0 64 0)",
                "dst": "(typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512)",
                "output_size": 512,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm512_div_epu32",
                "dst_ctx": "typed:unsigned-vec-div_p32_s512_signed_0"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )+ (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+512+_mm512_div_epu64+typed:unsigned-vec-div_p64_s512_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0 0 128 0 128 0)",
                "dst": "(typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512)",
                "output_size": 512,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm512_div_epu64",
                "dst_ctx": "typed:unsigned-vec-div_p64_s512_signed_0"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )+ (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+128+_mm_div_epu64+typed:unsigned-vec-div_p64_s128_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 128 0)",
                "dst": "(typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128)",
                "output_size": 128,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm_div_epu64",
                "dst_ctx": "typed:unsigned-vec-div_p64_s128_signed_0"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )+ (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+512+_mm512_div_epu16+typed:unsigned-vec-div_p16_s512_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0 32 0 32 0)",
                "dst": "(typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512)",
                "output_size": 512,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm512_div_epu16",
                "dst_ctx": "typed:unsigned-vec-div_p16_s512_signed_0"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )+ (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+256+_mm256_udiv_epi32+typed:unsigned-vec-div_p32_s256_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0 64 0 64 0)",
                "dst": "(typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256)",
                "output_size": 256,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm256_udiv_epi32",
                "dst_ctx": "typed:unsigned-vec-div_p32_s256_signed_0"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )+ (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+128+_mm_div_epu32+typed:unsigned-vec-div_p32_s128_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 64 0)",
                "dst": "(typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm_div_epu32",
                "dst_ctx": "typed:unsigned-vec-div_p32_s128_signed_0"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )+ (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+128+_mm_div_epu16+typed:unsigned-vec-div_p16_s128_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0 32 0 32 0)",
                "dst": "(typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128)",
                "output_size": 128,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm_div_epu16",
                "dst_ctx": "typed:unsigned-vec-div_p16_s128_signed_0"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )+ (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+256+_mm256_div_epu16+typed:unsigned-vec-div_p16_s256_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0 32 0 32 0)",
                "dst": "(typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256)",
                "output_size": 256,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm256_div_epu16",
                "dst_ctx": "typed:unsigned-vec-div_p16_s256_signed_0"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )+ (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+512+_mm512_div_epu8+typed:unsigned-vec-div_p8_s512_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0 16 0 16 0)",
                "dst": "(typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512)",
                "output_size": 512,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm512_div_epu8",
                "dst_ctx": "typed:unsigned-vec-div_p8_s512_signed_0"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )+ (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+256+_mm256_div_epu8+typed:unsigned-vec-div_p8_s256_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0 16 0 16 0)",
                "dst": "(typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256)",
                "output_size": 256,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm256_div_epu8",
                "dst_ctx": "typed:unsigned-vec-div_p8_s256_signed_0"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )+ (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+128+_mm_div_epu8+typed:unsigned-vec-div_p8_s128_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0 16 0 16 0)",
                "dst": "(typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm_div_epu8",
                "dst_ctx": "typed:unsigned-vec-div_p8_s128_signed_0"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )+ (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+256+_mm256_div_epu64+typed:unsigned-vec-div_p64_s256_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0 128 0 128 0)",
                "dst": "(typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x01 8)) 64 256)",
                "output_size": 256,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epu8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-div ; typed:unsigned-vec-div_p8_s512_signed_0\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm256_div_epu64",
                "dst_ctx": "typed:unsigned-vec-div_p64_s256_signed_0"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )+ (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+256+_mm256_div_epi8+typed:signed-vec-div_p8_s256_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 1 16 1 16 0)",
                "dst": "(typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x00 8)) 8 256)",
                "output_size": 256,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm256_div_epi8",
                "dst_ctx": "typed:signed-vec-div_p8_s256_signed_1"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )+ (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+128+_mm_div_epi8+typed:signed-vec-div_p8_s128_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 16 1 16 0)",
                "dst": "(typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm_div_epi8",
                "dst_ctx": "typed:signed-vec-div_p8_s128_signed_1"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )+ (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+512+_mm512_div_epi8+typed:signed-vec-div_p8_s512_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 16 1 16 0)",
                "dst": "(typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512)",
                "output_size": 512,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm512_div_epi8",
                "dst_ctx": "typed:signed-vec-div_p8_s512_signed_1"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )+ (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+128+_mm_div_epi16+typed:signed-vec-div_p16_s128_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128)",
                "output_size": 128,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm_div_epi16",
                "dst_ctx": "typed:signed-vec-div_p16_s128_signed_1"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )+ (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+256+_mm256_div_epi16+typed:signed-vec-div_p16_s256_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256)",
                "output_size": 256,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm256_div_epi16",
                "dst_ctx": "typed:signed-vec-div_p16_s256_signed_1"
            }
        }
    ],
    " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )+ (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+512+_mm512_div_epi16+typed:signed-vec-div_p16_s512_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512)",
                "output_size": 512,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm512_div_epi16",
                "dst_ctx": "typed:signed-vec-div_p16_s512_signed_1"
            }
        }
    ],

    "_ (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )+ (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+512+_mm512_div_epi16+typed:signed-vec-div_p16_s512_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 1 64 1 64 0)",
                "dst": "(typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512)",
                "output_size": 512,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm512_div_epi32",
                "dst_ctx": "typed:signed-vec-div_p32_s512_signed_1"
            }
        }
    ],
    "_s64 (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )+ (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )+512+_mm512_div_epi16+typed:signed-vec-div_p16_s512_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 1 1 128 1 128 0)",
                "dst": "(typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512)",
                "output_size": 512,
                "original_src_expr": " (_mm_div_epi64_dsl ; _mm512_div_epi8\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-div ; typed:signed-vec-div_p8_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t8\n\t512\n )",
                "src_ctx": "_mm512_div_epi64",
                "dst_ctx": "typed:signed-vec-div_p64_s512_signed_1"
            }
        }
    ]
}
