{
    " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavguw_128B\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t0\n )+ (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vavguw_128B+typed:unsigned-vec-halving_add_p32_s1024_signed_0": [
        {
            "property_name": "EnumeratePattern_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavguw_128B_dsl (lit (bv #x00000002 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 0 -1 0)",
                "dst": "(typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavguw_128B\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vavguw_128B",
                "dst_ctx": "typed:unsigned-vec-halving_add_p32_s1024_signed_0"
            }
        }
    ],
    " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavguw_128B\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t0\n )+ (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vavguh_128B+typed:unsigned-vec-halving_add_p16_s1024_signed_0": [
        {
            "property_name": "EnumeratePattern_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavguw_128B_dsl (lit (bv #x0002 16)) (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 -1 0)",
                "dst": "(typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavguw_128B\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vavguh_128B",
                "dst_ctx": "typed:unsigned-vec-halving_add_p16_s1024_signed_0"
            }
        }
    ],
    " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavguw_128B\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t0\n )+ (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vavgub_128B+typed:unsigned-vec-halving_add_p8_s1024_signed_0": [
        {
            "property_name": "EnumeratePattern_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavguw_128B_dsl (lit (bv #x02 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 -1 0)",
                "dst": "(typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavguw_128B\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vavgub_128B",
                "dst_ctx": "typed:unsigned-vec-halving_add_p8_s1024_signed_0"
            }
        }
    ],
    " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavgwrnd_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t-1\n\t-1\n\t0\n )+ (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p32_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vavgwrnd_128B+typed:signed-vec-rounding_halving_add_p32_s1024_signed_1": [
        {
            "property_name": "EnumeratePattern_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x00000001 32)) (lit (bv #x00000002 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 1 -1 -1 0)",
                "dst": "(typed:signed-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavgwrnd_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t-1\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p32_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vavgwrnd_128B",
                "dst_ctx": "typed:signed-vec-rounding_halving_add_p32_s1024_signed_1"
            }
        }
    ],
    " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavgwrnd_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t-1\n\t-1\n\t0\n )+ (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p32_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vavghrnd_128B+typed:signed-vec-rounding_halving_add_p16_s1024_signed_1": [
        {
            "property_name": "EnumeratePattern_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) (lit (bv #x0002 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 1 -1 -1 0)",
                "dst": "(typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavgwrnd_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t-1\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p32_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vavghrnd_128B",
                "dst_ctx": "typed:signed-vec-rounding_halving_add_p16_s1024_signed_1"
            }
        }
    ],
    " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavgwrnd_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t-1\n\t-1\n\t0\n )+ (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p32_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vavgbrnd_128B+typed:signed-vec-rounding_halving_add_p8_s1024_signed_1": [
        {
            "property_name": "EnumeratePattern_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x01 8)) (lit (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 1 -1 -1 0)",
                "dst": "(typed:signed-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavgwrnd_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t-1\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p32_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vavgbrnd_128B",
                "dst_ctx": "typed:signed-vec-rounding_halving_add_p8_s1024_signed_1"
            }
        }
    ],
    " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavguwrnd_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t-1\n\t0\n )+ (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vavguwrnd_128B+typed:unsigned-vec-rounding_halving_add_p32_s1024_signed_0": [
        {
            "property_name": "EnumeratePattern_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x00000001 32)) (lit (bv #x00000002 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 0 -1 -1 0)",
                "dst": "(typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavguwrnd_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vavguwrnd_128B",
                "dst_ctx": "typed:unsigned-vec-rounding_halving_add_p32_s1024_signed_0"
            }
        }
    ],
    " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavguwrnd_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t-1\n\t0\n )+ (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vavgubrnd_128B+typed:unsigned-vec-rounding_halving_add_p8_s1024_signed_0": [
        {
            "property_name": "EnumeratePattern_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x01 8)) (lit (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 -1 -1 0)",
                "dst": "(typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavguwrnd_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vavgubrnd_128B",
                "dst_ctx": "typed:unsigned-vec-rounding_halving_add_p8_s1024_signed_0"
            }
        }
    ],
    " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavguwrnd_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t-1\n\t0\n )+ (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vavguhrnd_128B+typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0": [
        {
            "property_name": "EnumeratePattern_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) (lit (bv #x0002 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0 -1 -1 0)",
                "dst": "(typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavguwrnd_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vavguhrnd_128B",
                "dst_ctx": "typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0"
            }
        }
    ],
    " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavgh_128B\n\t(lit (bv #x0002 (bitvector 16)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t-1\n\t0\n )+ (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vavgh_128B+typed:signed-vec-halving_add_p16_s1024_signed_1": [
        {
            "property_name": "EnumeratePattern_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavguw_128B_dsl (lit (bv #x0002 16)) (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 -1 0)",
                "dst": "(typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavgh_128B\n\t(lit (bv #x0002 (bitvector 16)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vavgh_128B",
                "dst_ctx": "typed:signed-vec-halving_add_p16_s1024_signed_1"
            }
        }
    ],
    " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavgh_128B\n\t(lit (bv #x0002 (bitvector 16)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t-1\n\t0\n )+ (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vavgb_128B+typed:signed-vec-halving_add_p8_s1024_signed_1": [
        {
            "property_name": "EnumeratePattern_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavguw_128B_dsl (lit (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 1 -1 0)",
                "dst": "(typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavgh_128B\n\t(lit (bv #x0002 (bitvector 16)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vavgb_128B",
                "dst_ctx": "typed:signed-vec-halving_add_p8_s1024_signed_1"
            }
        }
    ],
    " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavgh_128B\n\t(lit (bv #x0002 (bitvector 16)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t-1\n\t0\n )+ (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vavgw_128B+typed:signed-vec-halving_add_p32_s1024_signed_1": [
        {
            "property_name": "EnumeratePattern_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavguw_128B_dsl (lit (bv #x00000002 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 1 -1 0)",
                "dst": "(typed:signed-vec-halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavgh_128B\n\t(lit (bv #x0002 (bitvector 16)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vavgw_128B",
                "dst_ctx": "typed:signed-vec-halving_add_p32_s1024_signed_1"
            }
        }
    ]
}