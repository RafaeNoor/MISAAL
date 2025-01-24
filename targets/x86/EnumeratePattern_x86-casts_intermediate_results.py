{
    " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )+ (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is512_op32_os256_signed_0\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )+128+_mm256_cvtepi64_epi32+typed:cast-uint_1_ip64_is256_op32_os128_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 32 64 1 0)",
                "dst": "(typed:cast-uint-truncate (reg (bv #x00 8)) 64 1 4 32)",
                "output_size": 128,
                "original_src_expr": " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is512_op32_os256_signed_0\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )",
                "src_ctx": "_mm256_cvtepi64_epi32",
                "dst_ctx": "typed:cast-uint_1_ip64_is256_op32_os128_signed_0"
            }
        }
    ],
    " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )+ (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is512_op32_os256_signed_0\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )+128+_mm256_cvtepi16_epi8+typed:cast-uint_1_ip16_is256_op8_os128_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 8 16 1 0)",
                "dst": "(typed:cast-uint-truncate (reg (bv #x00 8)) 16 1 16 8)",
                "output_size": 128,
                "original_src_expr": " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is512_op32_os256_signed_0\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )",
                "src_ctx": "_mm256_cvtepi16_epi8",
                "dst_ctx": "typed:cast-uint_1_ip16_is256_op8_os128_signed_0"
            }
        }
    ],
    " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )+ (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is512_op32_os256_signed_0\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )+128+_mm256_cvtepi32_epi16+typed:cast-uint_1_ip32_is256_op16_os128_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 16 32 1 0)",
                "dst": "(typed:cast-uint-truncate (reg (bv #x00 8)) 32 1 8 16)",
                "output_size": 128,
                "original_src_expr": " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is512_op32_os256_signed_0\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )",
                "src_ctx": "_mm256_cvtepi32_epi16",
                "dst_ctx": "typed:cast-uint_1_ip32_is256_op16_os128_signed_0"
            }
        }
    ],
    " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )+ (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is512_op32_os256_signed_0\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )+256+_mm512_cvtepi32_epi16+typed:cast-uint_1_ip32_is512_op16_os256_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0)",
                "dst": "(typed:cast-uint-truncate (reg (bv #x00 8)) 32 1 16 16)",
                "output_size": 256,
                "original_src_expr": " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is512_op32_os256_signed_0\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )",
                "src_ctx": "_mm512_cvtepi32_epi16",
                "dst_ctx": "typed:cast-uint_1_ip32_is512_op16_os256_signed_0"
            }
        }
    ],
    " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )+ (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is512_op32_os256_signed_0\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )+256+_mm512_cvtepi64_epi32+typed:cast-uint_1_ip64_is512_op32_os256_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0)",
                "dst": "(typed:cast-uint-truncate (reg (bv #x00 8)) 64 1 8 32)",
                "output_size": 256,
                "original_src_expr": " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is512_op32_os256_signed_0\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )",
                "src_ctx": "_mm512_cvtepi64_epi32",
                "dst_ctx": "typed:cast-uint_1_ip64_is512_op32_os256_signed_0"
            }
        }
    ],
    " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )+ (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is512_op32_os256_signed_0\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )+256+_mm512_cvtepi16_epi8+typed:cast-uint_1_ip16_is512_op8_os256_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 0)",
                "dst": "(typed:cast-uint-truncate (reg (bv #x00 8)) 16 1 32 8)",
                "output_size": 256,
                "original_src_expr": " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is512_op32_os256_signed_0\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )",
                "src_ctx": "_mm512_cvtepi16_epi8",
                "dst_ctx": "typed:cast-uint_1_ip16_is512_op8_os256_signed_0"
            }
        }
    ],
    " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )+ (typed:cast-int-truncate ; typed:cast-int_1_ip64_is512_op32_os256_signed_1\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )+128+_mm256_cvtepi64_epi32+typed:cast-int_1_ip64_is256_op32_os128_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 32 64 1 0)",
                "dst": "(typed:cast-int-truncate (reg (bv #x00 8)) 64 1 4 32)",
                "output_size": 128,
                "original_src_expr": " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int-truncate ; typed:cast-int_1_ip64_is512_op32_os256_signed_1\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )",
                "src_ctx": "_mm256_cvtepi64_epi32",
                "dst_ctx": "typed:cast-int_1_ip64_is256_op32_os128_signed_1"
            }
        }
    ],
    " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )+ (typed:cast-int-truncate ; typed:cast-int_1_ip64_is512_op32_os256_signed_1\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )+128+_mm256_cvtepi32_epi16+typed:cast-int_1_ip32_is256_op16_os128_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 16 32 1 0)",
                "dst": "(typed:cast-int-truncate (reg (bv #x00 8)) 32 1 8 16)",
                "output_size": 128,
                "original_src_expr": " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int-truncate ; typed:cast-int_1_ip64_is512_op32_os256_signed_1\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )",
                "src_ctx": "_mm256_cvtepi32_epi16",
                "dst_ctx": "typed:cast-int_1_ip32_is256_op16_os128_signed_1"
            }
        }
    ],
    " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )+ (typed:cast-int-truncate ; typed:cast-int_1_ip64_is512_op32_os256_signed_1\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )+256+_mm512_cvtepi32_epi16+typed:cast-int_1_ip32_is512_op16_os256_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0)",
                "dst": "(typed:cast-int-truncate (reg (bv #x00 8)) 32 1 16 16)",
                "output_size": 256,
                "original_src_expr": " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int-truncate ; typed:cast-int_1_ip64_is512_op32_os256_signed_1\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )",
                "src_ctx": "_mm512_cvtepi32_epi16",
                "dst_ctx": "typed:cast-int_1_ip32_is512_op16_os256_signed_1"
            }
        }
    ],
    " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )+ (typed:cast-int-truncate ; typed:cast-int_1_ip64_is512_op32_os256_signed_1\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )+128+_mm256_cvtepi16_epi8+typed:cast-int_1_ip16_is256_op8_os128_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 8 16 1 0)",
                "dst": "(typed:cast-int-truncate (reg (bv #x00 8)) 16 1 16 8)",
                "output_size": 128,
                "original_src_expr": " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int-truncate ; typed:cast-int_1_ip64_is512_op32_os256_signed_1\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )",
                "src_ctx": "_mm256_cvtepi16_epi8",
                "dst_ctx": "typed:cast-int_1_ip16_is256_op8_os128_signed_1"
            }
        }
    ],
    " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )+ (typed:cast-int-truncate ; typed:cast-int_1_ip64_is512_op32_os256_signed_1\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )+256+_mm512_cvtepi16_epi8+typed:cast-int_1_ip16_is512_op8_os256_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 0)",
                "dst": "(typed:cast-int-truncate (reg (bv #x00 8)) 16 1 32 8)",
                "output_size": 256,
                "original_src_expr": " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int-truncate ; typed:cast-int_1_ip64_is512_op32_os256_signed_1\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )",
                "src_ctx": "_mm512_cvtepi16_epi8",
                "dst_ctx": "typed:cast-int_1_ip16_is512_op8_os256_signed_1"
            }
        }
    ],
    " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )+ (typed:cast-int-truncate ; typed:cast-int_1_ip64_is512_op32_os256_signed_1\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )+256+_mm512_cvtepi64_epi32+typed:cast-int_1_ip64_is512_op32_os256_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm256_cvtepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0)",
                "dst": "(typed:cast-int-truncate (reg (bv #x00 8)) 64 1 8 32)",
                "output_size": 256,
                "original_src_expr": " (_mm256_cvtepi64_epi32_dsl ; _mm512_cvtepi64_epi32\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t64\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int-truncate ; typed:cast-int_1_ip64_is512_op32_os256_signed_1\n\t(buffer-index  0 'uint8 512) ; < 64 x i8> False\n\t64\n\t1\n\t8\n\t32\n )",
                "src_ctx": "_mm512_cvtepi64_epi32",
                "dst_ctx": "typed:cast-int_1_ip64_is512_op32_os256_signed_1"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepu8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t0\n\t0\n )+ (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is128_op16_os256_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )+512+_mm512_cvtepu32_epi64+typed:cast-uint_1_ip32_is256_op64_os512_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)",
                "dst": "(typed:cast-uint-extend (reg (bv #x00 8)) 32 1 8 64)",
                "output_size": 512,
                "original_src_expr": " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepu8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is128_op16_os256_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )",
                "src_ctx": "_mm512_cvtepu32_epi64",
                "dst_ctx": "typed:cast-uint_1_ip32_is256_op64_os512_signed_0"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepu8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t0\n\t0\n )+ (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is128_op16_os256_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )+512+_mm512_cvtepu16_epi32+typed:cast-uint_1_ip16_is256_op32_os512_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0 0)",
                "dst": "(typed:cast-uint-extend (reg (bv #x00 8)) 16 1 16 32)",
                "output_size": 512,
                "original_src_expr": " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepu8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is128_op16_os256_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )",
                "src_ctx": "_mm512_cvtepu16_epi32",
                "dst_ctx": "typed:cast-uint_1_ip16_is256_op32_os512_signed_0"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepu8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t0\n\t0\n )+ (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is128_op16_os256_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )+512+_mm512_cvtepu8_epi16+typed:cast-uint_1_ip8_is256_op16_os512_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 0 0)",
                "dst": "(typed:cast-uint-extend (reg (bv #x00 8)) 8 1 32 16)",
                "output_size": 512,
                "original_src_expr": " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepu8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is128_op16_os256_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )",
                "src_ctx": "_mm512_cvtepu8_epi16",
                "dst_ctx": "typed:cast-uint_1_ip8_is256_op16_os512_signed_0"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepu8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t0\n\t0\n )+ (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is128_op16_os256_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )+256+_mm256_cvtepu8_epi16+typed:cast-uint_1_ip8_is128_op16_os256_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 8 16 1 0 0)",
                "dst": "(typed:cast-uint-extend (reg (bv #x00 8)) 8 1 16 16)",
                "output_size": 256,
                "original_src_expr": " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepu8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is128_op16_os256_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )",
                "src_ctx": "_mm256_cvtepu8_epi16",
                "dst_ctx": "typed:cast-uint_1_ip8_is128_op16_os256_signed_0"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepu8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t0\n\t0\n )+ (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is128_op16_os256_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )+256+_mm256_cvtepu32_epi64+typed:cast-uint_1_ip32_is128_op64_os256_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 32 64 1 0 0)",
                "dst": "(typed:cast-uint-extend (reg (bv #x00 8)) 32 1 4 64)",
                "output_size": 256,
                "original_src_expr": " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepu8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is128_op16_os256_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )",
                "src_ctx": "_mm256_cvtepu32_epi64",
                "dst_ctx": "typed:cast-uint_1_ip32_is128_op64_os256_signed_0"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepu8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t0\n\t0\n )+ (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is128_op16_os256_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )+256+_mm256_cvtepu16_epi32+typed:cast-uint_1_ip16_is128_op32_os256_signed_0": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 16 32 1 0 0)",
                "dst": "(typed:cast-uint-extend (reg (bv #x00 8)) 16 1 8 32)",
                "output_size": 256,
                "original_src_expr": " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepu8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is128_op16_os256_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )",
                "src_ctx": "_mm256_cvtepu16_epi32",
                "dst_ctx": "typed:cast-uint_1_ip16_is128_op32_os256_signed_0"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepi8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t1\n\t0\n )+ (typed:cast-int-extend ; typed:cast-int_1_ip8_is128_op16_os256_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )+256+_mm256_cvtepi16_epi32+typed:cast-int_1_ip16_is128_op32_os256_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 16 32 1 1 0)",
                "dst": "(typed:cast-int-extend (reg (bv #x00 8)) 16 1 8 32)",
                "output_size": 256,
                "original_src_expr": " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepi8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int-extend ; typed:cast-int_1_ip8_is128_op16_os256_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )",
                "src_ctx": "_mm256_cvtepi16_epi32",
                "dst_ctx": "typed:cast-int_1_ip16_is128_op32_os256_signed_1"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepi8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t1\n\t0\n )+ (typed:cast-int-extend ; typed:cast-int_1_ip8_is128_op16_os256_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )+256+_mm256_cvtepi8_epi16+typed:cast-int_1_ip8_is128_op16_os256_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 8 16 1 1 0)",
                "dst": "(typed:cast-int-extend (reg (bv #x00 8)) 8 1 16 16)",
                "output_size": 256,
                "original_src_expr": " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepi8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int-extend ; typed:cast-int_1_ip8_is128_op16_os256_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )",
                "src_ctx": "_mm256_cvtepi8_epi16",
                "dst_ctx": "typed:cast-int_1_ip8_is128_op16_os256_signed_1"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepi8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t1\n\t0\n )+ (typed:cast-int-extend ; typed:cast-int_1_ip8_is128_op16_os256_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )+256+_mm256_cvtepi32_epi64+typed:cast-int_1_ip32_is128_op64_os256_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 128 128 0 128 32 64 1 1 0)",
                "dst": "(typed:cast-int-extend (reg (bv #x00 8)) 32 1 4 64)",
                "output_size": 256,
                "original_src_expr": " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepi8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int-extend ; typed:cast-int_1_ip8_is128_op16_os256_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )",
                "src_ctx": "_mm256_cvtepi32_epi64",
                "dst_ctx": "typed:cast-int_1_ip32_is128_op64_os256_signed_1"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepi8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t1\n\t0\n )+ (typed:cast-int-extend ; typed:cast-int_1_ip8_is128_op16_os256_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )+512+_mm512_cvtepi8_epi16+typed:cast-int_1_ip8_is256_op16_os512_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 1 0)",
                "dst": "(typed:cast-int-extend (reg (bv #x00 8)) 8 1 32 16)",
                "output_size": 512,
                "original_src_expr": " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepi8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int-extend ; typed:cast-int_1_ip8_is128_op16_os256_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )",
                "src_ctx": "_mm512_cvtepi8_epi16",
                "dst_ctx": "typed:cast-int_1_ip8_is256_op16_os512_signed_1"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepi8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t1\n\t0\n )+ (typed:cast-int-extend ; typed:cast-int_1_ip8_is128_op16_os256_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )+512+_mm512_cvtepi16_epi32+typed:cast-int_1_ip16_is256_op32_os512_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 1 0)",
                "dst": "(typed:cast-int-extend (reg (bv #x00 8)) 16 1 16 32)",
                "output_size": 512,
                "original_src_expr": " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepi8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int-extend ; typed:cast-int_1_ip8_is128_op16_os256_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )",
                "src_ctx": "_mm512_cvtepi16_epi32",
                "dst_ctx": "typed:cast-int_1_ip16_is256_op32_os512_signed_1"
            }
        }
    ],
    " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepi8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t1\n\t0\n )+ (typed:cast-int-extend ; typed:cast-int_1_ip8_is128_op16_os256_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )+512+_mm512_cvtepi32_epi64+typed:cast-int_1_ip32_is256_op64_os512_signed_1": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 1 0)",
                "dst": "(typed:cast-int-extend (reg (bv #x00 8)) 32 1 8 64)",
                "output_size": 512,
                "original_src_expr": " (_mm512_cvtepu8_epi32_dsl ; _mm256_cvtepi8_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int-extend ; typed:cast-int_1_ip8_is128_op16_os256_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t1\n\t16\n\t16\n )",
                "src_ctx": "_mm512_cvtepi32_epi64",
                "dst_ctx": "typed:cast-int_1_ip32_is256_op64_os512_signed_1"
            }
        }
    ]
}