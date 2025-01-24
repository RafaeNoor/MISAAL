{
    " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )+ (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )+128+_mm_srav_epi16+typed:signed-vec-shr_p16_s128_signed_1": [
        {
            "property_name": "EnumeratePattern_shr",
            "property": {
                "src": "(_mm512_srav_epi16_dsl (reg (bv #x01 8)) (lit (bv #x0000 16)) (reg (bv #x00 8)) (lit (bv #xffff 16)) (lit (bv #b1 1)) (lit (bv #x0010 16)) 128 128 0 128 16 0 16 16 1 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128)",
                "output_size": 128,
                "original_src_expr": " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )",
                "src_ctx": "_mm_srav_epi16",
                "dst_ctx": "typed:signed-vec-shr_p16_s128_signed_1"
            }
        }
    ],
    " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )+ (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )+512+_mm512_srav_epi16+typed:signed-vec-shr_p16_s512_signed_1": [
        {
            "property_name": "EnumeratePattern_shr",
            "property": {
                "src": "(_mm512_srav_epi16_dsl (reg (bv #x01 8)) (lit (bv #x0000 16)) (reg (bv #x00 8)) (lit (bv #xffff 16)) (lit (bv #b1 1)) (lit (bv #x0010 16)) 512 512 0 512 16 0 16 16 1 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512)",
                "output_size": 512,
                "original_src_expr": " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )",
                "src_ctx": "_mm512_srav_epi16",
                "dst_ctx": "typed:signed-vec-shr_p16_s512_signed_1"
            }
        }
    ],
    " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )+ (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )+128+_mm_srav_epi32+typed:signed-vec-shr_p32_s128_signed_1": [
        {
            "property_name": "EnumeratePattern_shr",
            "property": {
                "src": "(_mm512_srav_epi16_dsl (reg (bv #x01 8)) (lit (bv #x00000000 32)) (reg (bv #x00 8)) (lit (bv #xffffffff 32)) (lit (bv #b1 1)) (lit (bv #x00000020 32)) 128 128 0 128 32 0 32 32 1 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )",
                "src_ctx": "_mm_srav_epi32",
                "dst_ctx": "typed:signed-vec-shr_p32_s128_signed_1"
            }
        }
    ],
    " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )+ (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )+512+_mm512_srav_epi32+typed:signed-vec-shr_p32_s512_signed_1": [
        {
            "property_name": "EnumeratePattern_shr",
            "property": {
                "src": "(_mm512_srav_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000 32)) (reg (bv #x01 8)) (lit (bv #xffffffff 32)) (lit (bv #b1 1)) (lit (bv #x00000020 32)) 512 512 0 512 32 0 32 32 1 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512)",
                "output_size": 512,
                "original_src_expr": " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )",
                "src_ctx": "_mm512_srav_epi32",
                "dst_ctx": "typed:signed-vec-shr_p32_s512_signed_1"
            }
        }
    ],
    " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )+ (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )+512+_mm512_srav_epi64+typed:signed-vec-shr_p64_s512_signed_1": [
        {
            "property_name": "EnumeratePattern_shr",
            "property": {
                "src": "(_mm512_srav_epi16_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (reg (bv #x00 8)) (lit (bv #xffffffffffffffff 64)) (lit (bv #b1 1)) (lit (bv #x0000000000000040 64)) 512 512 0 512 64 0 64 64 1 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512)",
                "output_size": 512,
                "original_src_expr": " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )",
                "src_ctx": "_mm512_srav_epi64",
                "dst_ctx": "typed:signed-vec-shr_p64_s512_signed_1"
            }
        }
    ],
    " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )+ (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )+256+_mm256_srav_epi64+typed:signed-vec-shr_p64_s256_signed_1": [
        {
            "property_name": "EnumeratePattern_shr",
            "property": {
                "src": "(_mm512_srav_epi16_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (reg (bv #x00 8)) (lit (bv #xffffffffffffffff 64)) (lit (bv #b1 1)) (lit (bv #x0000000000000040 64)) 256 256 0 256 64 0 64 64 1 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 64 256)",
                "output_size": 256,
                "original_src_expr": " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )",
                "src_ctx": "_mm256_srav_epi64",
                "dst_ctx": "typed:signed-vec-shr_p64_s256_signed_1"
            }
        }
    ],
    " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )+ (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )+128+_mm_srav_epi64+typed:signed-vec-shr_p64_s128_signed_1": [
        {
            "property_name": "EnumeratePattern_shr",
            "property": {
                "src": "(_mm512_srav_epi16_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (reg (bv #x01 8)) (lit (bv #xffffffffffffffff 64)) (lit (bv #b1 1)) (lit (bv #x0000000000000040 64)) 128 128 0 128 64 0 64 64 1 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128)",
                "output_size": 128,
                "original_src_expr": " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )",
                "src_ctx": "_mm_srav_epi64",
                "dst_ctx": "typed:signed-vec-shr_p64_s128_signed_1"
            }
        }
    ],
    " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )+ (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )+256+_mm256_srav_epi16+typed:signed-vec-shr_p16_s256_signed_1": [
        {
            "property_name": "EnumeratePattern_shr",
            "property": {
                "src": "(_mm512_srav_epi16_dsl (reg (bv #x00 8)) (lit (bv #x0000 16)) (reg (bv #x01 8)) (lit (bv #xffff 16)) (lit (bv #b1 1)) (lit (bv #x0010 16)) 256 256 0 256 16 0 16 16 1 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 16 256)",
                "output_size": 256,
                "original_src_expr": " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )",
                "src_ctx": "_mm256_srav_epi16",
                "dst_ctx": "typed:signed-vec-shr_p16_s256_signed_1"
            }
        }
    ],
    " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )+ (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )+256+_mm256_srav_epi32+typed:signed-vec-shr_p32_s256_signed_1": [
        {
            "property_name": "EnumeratePattern_shr",
            "property": {
                "src": "(_mm512_srav_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000 32)) (reg (bv #x01 8)) (lit (bv #xffffffff 32)) (lit (bv #b1 1)) (lit (bv #x00000020 32)) 256 256 0 256 32 0 32 32 1 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 32 256)",
                "output_size": 256,
                "original_src_expr": " (_mm512_srav_epi16_dsl ; _mm512_srav_epi64\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 64)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i8> False\n\t(lit (bv #xffffffffffffffff (bitvector 64)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000040 (bitvector 64)))\n\t512\n\t512\n\t0\n\t512\n\t64\n\t0\n\t64\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-shr ; typed:signed-vec-shr_p64_s512_signed_1\n\t(buffer-index  1 'uint8 512) ; < 64 x i8> False\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t512\n )",
                "src_ctx": "_mm256_srav_epi32",
                "dst_ctx": "typed:signed-vec-shr_p32_s256_signed_1"
            }
        }
    ]
}