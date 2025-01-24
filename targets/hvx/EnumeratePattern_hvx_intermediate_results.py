{
    " (hexagon_V6_interleave_4_128B_dsl ; hexagon_V6_interleave_4_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is8_os32_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t8\n\t8\n\t4\n )+32+hexagon_V6_interleave_4_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_interleave_4_128B_dsl (reg (bv #x00 8)) 8 32)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 4)",
                "output_size": 32,
                "original_src_expr": " (hexagon_V6_interleave_4_128B_dsl ; hexagon_V6_interleave_4_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is8_os32_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t8\n\t8\n\t4\n )",
                "src_ctx": "hexagon_V6_interleave_4_128B"
            }
        }
    ],
    " (hexagon_V6_interleave_2_128B_dsl ; hexagon_V6_interleave_2_128B\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t2\n )+32+hexagon_V6_interleave_2_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_interleave_2_128B_dsl (reg (bv #x00 8)) 16 32)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 2)",
                "output_size": 32,
                "original_src_expr": " (hexagon_V6_interleave_2_128B_dsl ; hexagon_V6_interleave_2_128B\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i8> False\n\t16\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t(buffer-index  0 'uint8 16) ; < 2 x i8> False\n\t16\n\t16\n\t2\n )",
                "src_ctx": "hexagon_V6_interleave_2_128B"
            }
        }
    ],
    " (hexagon_V6_vunpackh_128B_dsl ; hexagon_V6_vunpackub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t16\n\t1\n\t0\n\t0\n )+ (typed:cast-uint ; typed:cast-uint_1_ip8_is1024_op16_os2048_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1\n\t128\n\t16\n )+2048+hexagon_V6_vunpackuh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vunpackh_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 32 1 0 0)",
                "dst": "(typed:cast-uint (reg (bv #x00 8)) 16 1 64 32)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vunpackh_128B_dsl ; hexagon_V6_vunpackub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t16\n\t1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint ; typed:cast-uint_1_ip8_is1024_op16_os2048_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1\n\t128\n\t16\n )",
                "src_ctx": "hexagon_V6_vunpackuh_128B"
            }
        }
    ],
    " (hexagon_V6_vunpackh_128B_dsl ; hexagon_V6_vunpackub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t16\n\t1\n\t0\n\t0\n )+ (typed:cast-uint ; typed:cast-uint_1_ip8_is1024_op16_os2048_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1\n\t128\n\t16\n )+2048+hexagon_V6_vunpackub_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vunpackh_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 16 1 0 0)",
                "dst": "(typed:cast-uint (reg (bv #x00 8)) 8 1 128 16)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vunpackh_128B_dsl ; hexagon_V6_vunpackub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t16\n\t1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint ; typed:cast-uint_1_ip8_is1024_op16_os2048_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1\n\t128\n\t16\n )",
                "src_ctx": "hexagon_V6_vunpackub_128B"
            }
        }
    ],
    " (hexagon_V6_vgtb_128B_dsl ; hexagon_V6_vgtb_128B\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t8\n\t1\n\t0\n )+ (typed:signed-vec-lt ; typed:signed-vec-lt_p8_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+128+hexagon_V6_vgtb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vgtb_128B_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 8 1 0)",
                "dst": "(typed:signed-vec-lt (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024)",
                "output_size": 128,
                "original_src_expr": " (hexagon_V6_vgtb_128B_dsl ; hexagon_V6_vgtb_128B\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-lt ; typed:signed-vec-lt_p8_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vgtb_128B"
            }
        }
    ],
    " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )+ (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+1024+hexagon_V6_vand_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_pred_and_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0)",
                "dst": "(typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "hexagon_V6_vand_128B"
            }
        }
    ],
    " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )+ (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+128+hexagon_V6_pred_and_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_pred_and_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 0)",
                "dst": "(typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128)",
                "output_size": 128,
                "original_src_expr": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "hexagon_V6_pred_and_128B"
            }
        }
    ],
    " (hexagon_V6_vunpackh_128B_dsl ; hexagon_V6_vunpackb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t16\n\t1\n\t1\n\t0\n )+ (typed:cast-int ; typed:cast-int_1_ip8_is1024_op16_os2048_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1\n\t128\n\t16\n )+2048+hexagon_V6_vunpackh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vunpackh_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 32 1 1 0)",
                "dst": "(typed:cast-int (reg (bv #x00 8)) 16 1 64 32)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vunpackh_128B_dsl ; hexagon_V6_vunpackb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t16\n\t1\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int ; typed:cast-int_1_ip8_is1024_op16_os2048_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1\n\t128\n\t16\n )",
                "src_ctx": "hexagon_V6_vunpackh_128B"
            }
        }
    ],
    " (hexagon_V6_vunpackh_128B_dsl ; hexagon_V6_vunpackb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t16\n\t1\n\t1\n\t0\n )+ (typed:cast-int ; typed:cast-int_1_ip8_is1024_op16_os2048_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1\n\t128\n\t16\n )+2048+hexagon_V6_vunpackb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vunpackh_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 16 1 1 0)",
                "dst": "(typed:cast-int (reg (bv #x00 8)) 8 1 128 16)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vunpackh_128B_dsl ; hexagon_V6_vunpackb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t16\n\t1\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int ; typed:cast-int_1_ip8_is1024_op16_os2048_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1\n\t128\n\t16\n )",
                "src_ctx": "hexagon_V6_vunpackb_128B"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+1024+hexagon_V6_vminuh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vminuh_128B"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+1024+hexagon_V6_vminub_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vminub_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vaddh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-add (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddh_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vaddb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddb_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vaddw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-add (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddw_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+2048+hexagon_V6_vaddh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+2048+hexagon_V6_vaddb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+2048+hexagon_V6_vaddw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddububb_sat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+1024+hexagon_V6_vaddububb_sat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddububb_sat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddububb_sat_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddububb_sat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+2048+hexagon_V6_vadduwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddububb_sat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vadduwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddububb_sat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+1024+hexagon_V6_vadduwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddububb_sat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vadduwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddububb_sat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+1024+hexagon_V6_vadduhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddububb_sat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vadduhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddububb_sat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+2048+hexagon_V6_vadduhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddububb_sat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vadduhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddububb_sat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+2048+hexagon_V6_vaddubsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddububb_sat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddubsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddbsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t0\n )+ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+1024+hexagon_V6_vaddwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddbsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddbsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t0\n )+ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+1024+hexagon_V6_vaddhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddbsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddbsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t0\n )+ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+2048+hexagon_V6_vaddbsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 8 1 0)",
                "dst": "(typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddbsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddbsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddbsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t0\n )+ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+2048+hexagon_V6_vaddwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 1 0)",
                "dst": "(typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddbsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddbsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t0\n )+ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+1024+hexagon_V6_vaddbsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 1 0)",
                "dst": "(typed:signed-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddbsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddbsat_128B"
            }
        }
    ],
    " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )+ (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vmpyih_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vmpyih_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 32 1 0)",
                "dst": "(typed:unsigned-vec-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vmpyih_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddbsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t0\n )+ (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+2048+hexagon_V6_vaddhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 1 0)",
                "dst": "(typed:signed-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddbsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaddhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+2048+hexagon_V6_vsubh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vsubuhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )+ (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vmpyih_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vmpyih_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 32 1 0)",
                "dst": "(typed:signed-vec-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vmpyih_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vsubuwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+2048+hexagon_V6_vsubuhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vsububsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+2048+hexagon_V6_vsububsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+2048+hexagon_V6_vsubuwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 32 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+2048+hexagon_V6_vsubwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 32 1 0)",
                "dst": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vsubwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+2048+hexagon_V6_vsubhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 1 0)",
                "dst": "(typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vsubbsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 1 0)",
                "dst": "(typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubbsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vsubhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )+ (typed:signed-vec-max ; typed:signed-vec-max_p32_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vmaxw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vmaxw_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-max ; typed:signed-vec-max_p32_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vmaxw_128B"
            }
        }
    ],
    " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )+ (typed:signed-vec-max ; typed:signed-vec-max_p32_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vmaxh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vmaxw_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-max ; typed:signed-vec-max_p32_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vmaxh_128B"
            }
        }
    ],
    " (hexagon_V6_interleave_4_128B_dsl ; hexagon_V6_interleave_4_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is8_os16_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t2\n\t )\n\t16\n\t16\n\t2\n )+32+hexagon_V6_interleave_4_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_interleave_4_128B_dsl (reg (bv #x00 8)) 8 32)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16 2)",
                "output_size": 32,
                "original_src_expr": " (hexagon_V6_interleave_4_128B_dsl ; hexagon_V6_interleave_4_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is8_os16_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t8\n\t\t8\n\t\t2\n\t )\n\t16\n\t16\n\t2\n )",
                "src_ctx": "hexagon_V6_interleave_4_128B"
            }
        }
    ],
    " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )+ (typed:signed-vec-max ; typed:signed-vec-max_p32_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vmaxb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vmaxw_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 1 0)",
                "dst": "(typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-max ; typed:signed-vec-max_p32_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vmaxb_128B"
            }
        }
    ],
    " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )+ (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p64_s128_signed_None\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t64\n\t\t128\n\t )\n\t8\n\t128\n )+128+hexagon_V6_pred_and_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_pred_and_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 0)",
                "dst": "(typed:vec-bwand (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128) 8 128)",
                "output_size": 128,
                "original_src_expr": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p64_s128_signed_None\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t64\n\t\t128\n\t )\n\t8\n\t128\n )",
                "src_ctx": "hexagon_V6_pred_and_128B"
            }
        }
    ],
    " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )+ (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p64_s128_signed_None\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t64\n\t\t128\n\t )\n\t8\n\t128\n )+1024+hexagon_V6_vand_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_pred_and_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0)",
                "dst": "(typed:vec-bwand (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t8\n\t\t128\n\t )\n\t (typed:vec-bwand ; typed:vec-bwand_p64_s128_signed_None\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t64\n\t\t128\n\t )\n\t8\n\t128\n )",
                "src_ctx": "hexagon_V6_vand_128B"
            }
        }
    ],
    " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )+ (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p64_s128_signed_None\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t64\n\t\t128\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+1024+hexagon_V6_vand_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_pred_and_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0)",
                "dst": "(typed:vec-bwand (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) (reg (bv #x00 8)) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p64_s128_signed_None\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t64\n\t\t128\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "hexagon_V6_vand_128B"
            }
        }
    ],
    " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )+ (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p64_s128_signed_None\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t64\n\t\t128\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )+128+hexagon_V6_pred_and_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_pred_and_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 0)",
                "dst": "(typed:vec-bwand (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128) (reg (bv #x01 8)) 32 128)",
                "output_size": 128,
                "original_src_expr": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-bwand ; typed:vec-bwand_p8_s128_signed_None\n\t (typed:vec-bwand ; typed:vec-bwand_p64_s128_signed_None\n\t\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t\t64\n\t\t128\n\t )\n\t(buffer-index  1 'uint8 128) ; < 16 x i8> False\n\t8\n\t128\n )",
                "src_ctx": "hexagon_V6_pred_and_128B"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vminuh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vminuh_128B"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vminuh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vminuh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+2048+hexagon_V6_vsubbsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 8 1 0)",
                "dst": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubbsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vminub_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 1024) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vminub_128B"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vminub_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) (reg (bv #x00 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vminub_128B"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vminuh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vminuh_128B"
            }
        }
    ],
    " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vsh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t32\n\t1024\n\t1\n\t16\n\t2\n\t0\n )+ (hvx_swizzle_12_dsl ; hvx_swizzle_14\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t2016\n\t1952\n\t1888\n\t1824\n\t1760\n\t1696\n\t1632\n\t1568\n\t1504\n\t1440\n\t1376\n\t1312\n\t1248\n\t1184\n\t1120\n\t1056\n\t992\n\t1984\n\t1920\n\t928\n\t1856\n\t1792\n\t864\n\t1728\n\t1664\n\t800\n\t1600\n\t1536\n\t736\n\t1472\n\t1408\n\t672\n\t1344\n\t1280\n\t608\n\t1216\n\t1152\n\t544\n\t1088\n\t1024\n\t480\n\t960\n\t896\n\t416\n\t832\n\t768\n\t352\n\t704\n\t640\n\t288\n\t576\n\t512\n\t224\n\t448\n\t384\n\t160\n\t320\n\t256\n\t96\n\t192\n\t128\n\t32\n\t64\n\t0\n\t0\n )+2048+hexagon_V6_vsh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 16 0 512 16 32 1 1 32 1024 1 16 2 0)",
                "dst": "(hvx_swizzle_12_dsl (typed:cast-int (reg (bv #x00 8)) 16 1 64 32) 32 32 0 32 32 2016 1952 1888 1824 1760 1696 1632 1568 1504 1440 1376 1312 1248 1184 1120 1056 992 1984 1920 928 1856 1792 864 1728 1664 800 1600 1536 736 1472 1408 672 1344 1280 608 1216 1152 544 1088 1024 480 960 896 416 832 768 352 704 640 288 576 512 224 448 384 160 320 256 96 192 128 32 64 0 0)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vsh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t32\n\t1024\n\t1\n\t16\n\t2\n\t0\n )",
                "original_dst_expr": " (hvx_swizzle_12_dsl ; hvx_swizzle_14\n\t (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t2016\n\t1952\n\t1888\n\t1824\n\t1760\n\t1696\n\t1632\n\t1568\n\t1504\n\t1440\n\t1376\n\t1312\n\t1248\n\t1184\n\t1120\n\t1056\n\t992\n\t1984\n\t1920\n\t928\n\t1856\n\t1792\n\t864\n\t1728\n\t1664\n\t800\n\t1600\n\t1536\n\t736\n\t1472\n\t1408\n\t672\n\t1344\n\t1280\n\t608\n\t1216\n\t1152\n\t544\n\t1088\n\t1024\n\t480\n\t960\n\t896\n\t416\n\t832\n\t768\n\t352\n\t704\n\t640\n\t288\n\t576\n\t512\n\t224\n\t448\n\t384\n\t160\n\t320\n\t256\n\t96\n\t192\n\t128\n\t32\n\t64\n\t0\n\t0\n )",
                "src_ctx": "hexagon_V6_vsh_128B"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vminub_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 1024) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vminub_128B"
            }
        }
    ],
    " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vzh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t32\n\t1\n\t0\n\t32\n\t1024\n\t0\n\t16\n\t2\n\t0\n )+ (hvx_swizzle_12_dsl ; hvx_swizzle_14\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t2016\n\t1952\n\t1888\n\t1824\n\t1760\n\t1696\n\t1632\n\t1568\n\t1504\n\t1440\n\t1376\n\t1312\n\t1248\n\t1184\n\t1120\n\t1056\n\t992\n\t1984\n\t1920\n\t928\n\t1856\n\t1792\n\t864\n\t1728\n\t1664\n\t800\n\t1600\n\t1536\n\t736\n\t1472\n\t1408\n\t672\n\t1344\n\t1280\n\t608\n\t1216\n\t1152\n\t544\n\t1088\n\t1024\n\t480\n\t960\n\t896\n\t416\n\t832\n\t768\n\t352\n\t704\n\t640\n\t288\n\t576\n\t512\n\t224\n\t448\n\t384\n\t160\n\t320\n\t256\n\t96\n\t192\n\t128\n\t32\n\t64\n\t0\n\t0\n )+2048+hexagon_V6_vzh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 16 0 512 16 32 1 0 32 1024 0 16 2 0)",
                "dst": "(hvx_swizzle_12_dsl (typed:cast-uint (reg (bv #x00 8)) 16 1 64 32) 32 32 0 32 32 2016 1952 1888 1824 1760 1696 1632 1568 1504 1440 1376 1312 1248 1184 1120 1056 992 1984 1920 928 1856 1792 864 1728 1664 800 1600 1536 736 1472 1408 672 1344 1280 608 1216 1152 544 1088 1024 480 960 896 416 832 768 352 704 640 288 576 512 224 448 384 160 320 256 96 192 128 32 64 0 0)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vzh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t32\n\t1\n\t0\n\t32\n\t1024\n\t0\n\t16\n\t2\n\t0\n )",
                "original_dst_expr": " (hvx_swizzle_12_dsl ; hvx_swizzle_14\n\t (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t2016\n\t1952\n\t1888\n\t1824\n\t1760\n\t1696\n\t1632\n\t1568\n\t1504\n\t1440\n\t1376\n\t1312\n\t1248\n\t1184\n\t1120\n\t1056\n\t992\n\t1984\n\t1920\n\t928\n\t1856\n\t1792\n\t864\n\t1728\n\t1664\n\t800\n\t1600\n\t1536\n\t736\n\t1472\n\t1408\n\t672\n\t1344\n\t1280\n\t608\n\t1216\n\t1152\n\t544\n\t1088\n\t1024\n\t480\n\t960\n\t896\n\t416\n\t832\n\t768\n\t352\n\t704\n\t640\n\t288\n\t576\n\t512\n\t224\n\t448\n\t384\n\t160\n\t320\n\t256\n\t96\n\t192\n\t128\n\t32\n\t64\n\t0\n\t0\n )",
                "src_ctx": "hexagon_V6_vzh_128B"
            }
        }
    ],
    " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vzh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t32\n\t1\n\t0\n\t32\n\t1024\n\t0\n\t16\n\t2\n\t0\n )+ (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t (hvx_swizzle_12_dsl ; hvx_swizzle_12\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t16\n\t1\n\t64\n\t32\n )+2048+hexagon_V6_vzh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 16 0 512 16 32 1 0 32 1024 0 16 2 0)",
                "dst": "(typed:cast-uint (hvx_swizzle_12_dsl (reg (bv #x00 8)) 16 16 0 16 16 1008 976 944 912 880 848 816 784 752 720 688 656 624 592 560 528 496 992 960 464 928 896 432 864 832 400 800 768 368 736 704 336 672 640 304 608 576 272 544 512 240 480 448 208 416 384 176 352 320 144 288 256 112 224 192 80 160 128 48 96 64 16 32 0 0) 16 1 64 32)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vzh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t32\n\t1\n\t0\n\t32\n\t1024\n\t0\n\t16\n\t2\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t (hvx_swizzle_12_dsl ; hvx_swizzle_12\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t16\n\t1\n\t64\n\t32\n )",
                "src_ctx": "hexagon_V6_vzh_128B"
            }
        }
    ],
    " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vzb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t0\n\t16\n\t1024\n\t0\n\t8\n\t2\n\t0\n )+ (hvx_swizzle_2_dsl ; hvx_swizzle_2\n\t (typed:cast-uint ; typed:cast-uint_1_ip8_is1024_op16_os2048_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1\n\t\t128\n\t\t16\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t2032\n\t2000\n\t1968\n\t1936\n\t1904\n\t1872\n\t1840\n\t1808\n\t1776\n\t1744\n\t1712\n\t1680\n\t1648\n\t1616\n\t1584\n\t1552\n\t1520\n\t1488\n\t1456\n\t1424\n\t1392\n\t1360\n\t1328\n\t1296\n\t1264\n\t1232\n\t1200\n\t1168\n\t1136\n\t1104\n\t1072\n\t1040\n\t1008\n\t2016\n\t1984\n\t976\n\t1952\n\t1920\n\t944\n\t1888\n\t1856\n\t912\n\t1824\n\t1792\n\t880\n\t1760\n\t1728\n\t848\n\t1696\n\t1664\n\t816\n\t1632\n\t1600\n\t784\n\t1568\n\t1536\n\t752\n\t1504\n\t1472\n\t720\n\t1440\n\t1408\n\t688\n\t1376\n\t1344\n\t656\n\t1312\n\t1280\n\t624\n\t1248\n\t1216\n\t592\n\t1184\n\t1152\n\t560\n\t1120\n\t1088\n\t528\n\t1056\n\t1024\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )+2048+hexagon_V6_vzh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 16 0 512 16 32 1 0 32 1024 0 16 2 0)",
                "dst": "(hvx_swizzle_2_dsl (typed:cast-uint (reg (bv #x00 8)) 32 1 32 64) 16 16 0 16 16 2032 2000 1968 1936 1904 1872 1840 1808 1776 1744 1712 1680 1648 1616 1584 1552 1520 1488 1456 1424 1392 1360 1328 1296 1264 1232 1200 1168 1136 1104 1072 1040 1008 2016 1984 976 1952 1920 944 1888 1856 912 1824 1792 880 1760 1728 848 1696 1664 816 1632 1600 784 1568 1536 752 1504 1472 720 1440 1408 688 1376 1344 656 1312 1280 624 1248 1216 592 1184 1152 560 1120 1088 528 1056 1024 496 992 960 464 928 896 432 864 832 400 800 768 368 736 704 336 672 640 304 608 576 272 544 512 240 480 448 208 416 384 176 352 320 144 288 256 112 224 192 80 160 128 48 96 64 16 32 0 0)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vzb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t0\n\t16\n\t1024\n\t0\n\t8\n\t2\n\t0\n )",
                "original_dst_expr": " (hvx_swizzle_2_dsl ; hvx_swizzle_2\n\t (typed:cast-uint ; typed:cast-uint_1_ip8_is1024_op16_os2048_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1\n\t\t128\n\t\t16\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t2032\n\t2000\n\t1968\n\t1936\n\t1904\n\t1872\n\t1840\n\t1808\n\t1776\n\t1744\n\t1712\n\t1680\n\t1648\n\t1616\n\t1584\n\t1552\n\t1520\n\t1488\n\t1456\n\t1424\n\t1392\n\t1360\n\t1328\n\t1296\n\t1264\n\t1232\n\t1200\n\t1168\n\t1136\n\t1104\n\t1072\n\t1040\n\t1008\n\t2016\n\t1984\n\t976\n\t1952\n\t1920\n\t944\n\t1888\n\t1856\n\t912\n\t1824\n\t1792\n\t880\n\t1760\n\t1728\n\t848\n\t1696\n\t1664\n\t816\n\t1632\n\t1600\n\t784\n\t1568\n\t1536\n\t752\n\t1504\n\t1472\n\t720\n\t1440\n\t1408\n\t688\n\t1376\n\t1344\n\t656\n\t1312\n\t1280\n\t624\n\t1248\n\t1216\n\t592\n\t1184\n\t1152\n\t560\n\t1120\n\t1088\n\t528\n\t1056\n\t1024\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "src_ctx": "hexagon_V6_vzh_128B"
            }
        }
    ],
    " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vzb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t0\n\t16\n\t1024\n\t0\n\t8\n\t2\n\t0\n )+ (hvx_swizzle_2_dsl ; hvx_swizzle_2\n\t (typed:cast-uint ; typed:cast-uint_1_ip8_is1024_op16_os2048_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1\n\t\t128\n\t\t16\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t2032\n\t2000\n\t1968\n\t1936\n\t1904\n\t1872\n\t1840\n\t1808\n\t1776\n\t1744\n\t1712\n\t1680\n\t1648\n\t1616\n\t1584\n\t1552\n\t1520\n\t1488\n\t1456\n\t1424\n\t1392\n\t1360\n\t1328\n\t1296\n\t1264\n\t1232\n\t1200\n\t1168\n\t1136\n\t1104\n\t1072\n\t1040\n\t1008\n\t2016\n\t1984\n\t976\n\t1952\n\t1920\n\t944\n\t1888\n\t1856\n\t912\n\t1824\n\t1792\n\t880\n\t1760\n\t1728\n\t848\n\t1696\n\t1664\n\t816\n\t1632\n\t1600\n\t784\n\t1568\n\t1536\n\t752\n\t1504\n\t1472\n\t720\n\t1440\n\t1408\n\t688\n\t1376\n\t1344\n\t656\n\t1312\n\t1280\n\t624\n\t1248\n\t1216\n\t592\n\t1184\n\t1152\n\t560\n\t1120\n\t1088\n\t528\n\t1056\n\t1024\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )+2048+hexagon_V6_vzb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 8 0 512 8 16 1 0 16 1024 0 8 2 0)",
                "dst": "(hvx_swizzle_2_dsl (typed:cast-uint (reg (bv #x00 8)) 8 1 128 16) 16 16 0 16 16 2032 2000 1968 1936 1904 1872 1840 1808 1776 1744 1712 1680 1648 1616 1584 1552 1520 1488 1456 1424 1392 1360 1328 1296 1264 1232 1200 1168 1136 1104 1072 1040 1008 2016 1984 976 1952 1920 944 1888 1856 912 1824 1792 880 1760 1728 848 1696 1664 816 1632 1600 784 1568 1536 752 1504 1472 720 1440 1408 688 1376 1344 656 1312 1280 624 1248 1216 592 1184 1152 560 1120 1088 528 1056 1024 496 992 960 464 928 896 432 864 832 400 800 768 368 736 704 336 672 640 304 608 576 272 544 512 240 480 448 208 416 384 176 352 320 144 288 256 112 224 192 80 160 128 48 96 64 16 32 0 0)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vzb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t0\n\t16\n\t1024\n\t0\n\t8\n\t2\n\t0\n )",
                "original_dst_expr": " (hvx_swizzle_2_dsl ; hvx_swizzle_2\n\t (typed:cast-uint ; typed:cast-uint_1_ip8_is1024_op16_os2048_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1\n\t\t128\n\t\t16\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t2032\n\t2000\n\t1968\n\t1936\n\t1904\n\t1872\n\t1840\n\t1808\n\t1776\n\t1744\n\t1712\n\t1680\n\t1648\n\t1616\n\t1584\n\t1552\n\t1520\n\t1488\n\t1456\n\t1424\n\t1392\n\t1360\n\t1328\n\t1296\n\t1264\n\t1232\n\t1200\n\t1168\n\t1136\n\t1104\n\t1072\n\t1040\n\t1008\n\t2016\n\t1984\n\t976\n\t1952\n\t1920\n\t944\n\t1888\n\t1856\n\t912\n\t1824\n\t1792\n\t880\n\t1760\n\t1728\n\t848\n\t1696\n\t1664\n\t816\n\t1632\n\t1600\n\t784\n\t1568\n\t1536\n\t752\n\t1504\n\t1472\n\t720\n\t1440\n\t1408\n\t688\n\t1376\n\t1344\n\t656\n\t1312\n\t1280\n\t624\n\t1248\n\t1216\n\t592\n\t1184\n\t1152\n\t560\n\t1120\n\t1088\n\t528\n\t1056\n\t1024\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "src_ctx": "hexagon_V6_vzb_128B"
            }
        }
    ],
    " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vsb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t1\n\t16\n\t1024\n\t1\n\t8\n\t2\n\t0\n )+ (hvx_swizzle_2_dsl ; hvx_swizzle_2\n\t (typed:cast-int ; typed:cast-int_1_ip8_is1024_op16_os2048_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1\n\t\t128\n\t\t16\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t2032\n\t2000\n\t1968\n\t1936\n\t1904\n\t1872\n\t1840\n\t1808\n\t1776\n\t1744\n\t1712\n\t1680\n\t1648\n\t1616\n\t1584\n\t1552\n\t1520\n\t1488\n\t1456\n\t1424\n\t1392\n\t1360\n\t1328\n\t1296\n\t1264\n\t1232\n\t1200\n\t1168\n\t1136\n\t1104\n\t1072\n\t1040\n\t1008\n\t2016\n\t1984\n\t976\n\t1952\n\t1920\n\t944\n\t1888\n\t1856\n\t912\n\t1824\n\t1792\n\t880\n\t1760\n\t1728\n\t848\n\t1696\n\t1664\n\t816\n\t1632\n\t1600\n\t784\n\t1568\n\t1536\n\t752\n\t1504\n\t1472\n\t720\n\t1440\n\t1408\n\t688\n\t1376\n\t1344\n\t656\n\t1312\n\t1280\n\t624\n\t1248\n\t1216\n\t592\n\t1184\n\t1152\n\t560\n\t1120\n\t1088\n\t528\n\t1056\n\t1024\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )+2048+hexagon_V6_vsb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 8 0 512 8 16 1 1 16 1024 1 8 2 0)",
                "dst": "(hvx_swizzle_2_dsl (typed:cast-int (reg (bv #x00 8)) 8 1 128 16) 16 16 0 16 16 2032 2000 1968 1936 1904 1872 1840 1808 1776 1744 1712 1680 1648 1616 1584 1552 1520 1488 1456 1424 1392 1360 1328 1296 1264 1232 1200 1168 1136 1104 1072 1040 1008 2016 1984 976 1952 1920 944 1888 1856 912 1824 1792 880 1760 1728 848 1696 1664 816 1632 1600 784 1568 1536 752 1504 1472 720 1440 1408 688 1376 1344 656 1312 1280 624 1248 1216 592 1184 1152 560 1120 1088 528 1056 1024 496 992 960 464 928 896 432 864 832 400 800 768 368 736 704 336 672 640 304 608 576 272 544 512 240 480 448 208 416 384 176 352 320 144 288 256 112 224 192 80 160 128 48 96 64 16 32 0 0)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vsb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t1\n\t16\n\t1024\n\t1\n\t8\n\t2\n\t0\n )",
                "original_dst_expr": " (hvx_swizzle_2_dsl ; hvx_swizzle_2\n\t (typed:cast-int ; typed:cast-int_1_ip8_is1024_op16_os2048_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1\n\t\t128\n\t\t16\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t2032\n\t2000\n\t1968\n\t1936\n\t1904\n\t1872\n\t1840\n\t1808\n\t1776\n\t1744\n\t1712\n\t1680\n\t1648\n\t1616\n\t1584\n\t1552\n\t1520\n\t1488\n\t1456\n\t1424\n\t1392\n\t1360\n\t1328\n\t1296\n\t1264\n\t1232\n\t1200\n\t1168\n\t1136\n\t1104\n\t1072\n\t1040\n\t1008\n\t2016\n\t1984\n\t976\n\t1952\n\t1920\n\t944\n\t1888\n\t1856\n\t912\n\t1824\n\t1792\n\t880\n\t1760\n\t1728\n\t848\n\t1696\n\t1664\n\t816\n\t1632\n\t1600\n\t784\n\t1568\n\t1536\n\t752\n\t1504\n\t1472\n\t720\n\t1440\n\t1408\n\t688\n\t1376\n\t1344\n\t656\n\t1312\n\t1280\n\t624\n\t1248\n\t1216\n\t592\n\t1184\n\t1152\n\t560\n\t1120\n\t1088\n\t528\n\t1056\n\t1024\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "src_ctx": "hexagon_V6_vsb_128B"
            }
        }
    ],
    " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vsh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t32\n\t1024\n\t1\n\t16\n\t2\n\t0\n )+ (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t (hvx_swizzle_12_dsl ; hvx_swizzle_12\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t16\n\t1\n\t64\n\t32\n )+2048+hexagon_V6_vsh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 16 0 512 16 32 1 1 32 1024 1 16 2 0)",
                "dst": "(typed:cast-int (hvx_swizzle_12_dsl (reg (bv #x00 8)) 16 16 0 16 16 1008 976 944 912 880 848 816 784 752 720 688 656 624 592 560 528 496 992 960 464 928 896 432 864 832 400 800 768 368 736 704 336 672 640 304 608 576 272 544 512 240 480 448 208 416 384 176 352 320 144 288 256 112 224 192 80 160 128 48 96 64 16 32 0 0) 16 1 64 32)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vsh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t32\n\t1024\n\t1\n\t16\n\t2\n\t0\n )",
                "original_dst_expr": " (typed:cast-int ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t (hvx_swizzle_12_dsl ; hvx_swizzle_12\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t16\n\t1\n\t64\n\t32\n )",
                "src_ctx": "hexagon_V6_vsh_128B"
            }
        }
    ],
    " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vzb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t0\n\t16\n\t1024\n\t0\n\t8\n\t2\n\t0\n )+ (typed:cast-uint ; typed:cast-uint_1_ip8_is1024_op16_os2048_signed_0\n\t (hvx_swizzle_2_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t8\n\t\t8\n\t\t0\n\t\t8\n\t\t8\n\t\t1016\n\t\t1000\n\t\t984\n\t\t968\n\t\t952\n\t\t936\n\t\t920\n\t\t904\n\t\t888\n\t\t872\n\t\t856\n\t\t840\n\t\t824\n\t\t808\n\t\t792\n\t\t776\n\t\t760\n\t\t744\n\t\t728\n\t\t712\n\t\t696\n\t\t680\n\t\t664\n\t\t648\n\t\t632\n\t\t616\n\t\t600\n\t\t584\n\t\t568\n\t\t552\n\t\t536\n\t\t520\n\t\t504\n\t\t1008\n\t\t992\n\t\t488\n\t\t976\n\t\t960\n\t\t472\n\t\t944\n\t\t928\n\t\t456\n\t\t912\n\t\t896\n\t\t440\n\t\t880\n\t\t864\n\t\t424\n\t\t848\n\t\t832\n\t\t408\n\t\t816\n\t\t800\n\t\t392\n\t\t784\n\t\t768\n\t\t376\n\t\t752\n\t\t736\n\t\t360\n\t\t720\n\t\t704\n\t\t344\n\t\t688\n\t\t672\n\t\t328\n\t\t656\n\t\t640\n\t\t312\n\t\t624\n\t\t608\n\t\t296\n\t\t592\n\t\t576\n\t\t280\n\t\t560\n\t\t544\n\t\t264\n\t\t528\n\t\t512\n\t\t248\n\t\t496\n\t\t480\n\t\t232\n\t\t464\n\t\t448\n\t\t216\n\t\t432\n\t\t416\n\t\t200\n\t\t400\n\t\t384\n\t\t184\n\t\t368\n\t\t352\n\t\t168\n\t\t336\n\t\t320\n\t\t152\n\t\t304\n\t\t288\n\t\t136\n\t\t272\n\t\t256\n\t\t120\n\t\t240\n\t\t224\n\t\t104\n\t\t208\n\t\t192\n\t\t88\n\t\t176\n\t\t160\n\t\t72\n\t\t144\n\t\t128\n\t\t56\n\t\t112\n\t\t96\n\t\t40\n\t\t80\n\t\t64\n\t\t24\n\t\t48\n\t\t32\n\t\t8\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t8\n\t1\n\t128\n\t16\n )+2048+hexagon_V6_vzb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 8 0 512 8 16 1 0 16 1024 0 8 2 0)",
                "dst": "(typed:cast-uint (hvx_swizzle_2_dsl (reg (bv #x00 8)) 8 8 0 8 8 1016 1000 984 968 952 936 920 904 888 872 856 840 824 808 792 776 760 744 728 712 696 680 664 648 632 616 600 584 568 552 536 520 504 1008 992 488 976 960 472 944 928 456 912 896 440 880 864 424 848 832 408 816 800 392 784 768 376 752 736 360 720 704 344 688 672 328 656 640 312 624 608 296 592 576 280 560 544 264 528 512 248 496 480 232 464 448 216 432 416 200 400 384 184 368 352 168 336 320 152 304 288 136 272 256 120 240 224 104 208 192 88 176 160 72 144 128 56 112 96 40 80 64 24 48 32 8 16 0 0) 8 1 128 16)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vzb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t0\n\t16\n\t1024\n\t0\n\t8\n\t2\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint ; typed:cast-uint_1_ip8_is1024_op16_os2048_signed_0\n\t (hvx_swizzle_2_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t8\n\t\t8\n\t\t0\n\t\t8\n\t\t8\n\t\t1016\n\t\t1000\n\t\t984\n\t\t968\n\t\t952\n\t\t936\n\t\t920\n\t\t904\n\t\t888\n\t\t872\n\t\t856\n\t\t840\n\t\t824\n\t\t808\n\t\t792\n\t\t776\n\t\t760\n\t\t744\n\t\t728\n\t\t712\n\t\t696\n\t\t680\n\t\t664\n\t\t648\n\t\t632\n\t\t616\n\t\t600\n\t\t584\n\t\t568\n\t\t552\n\t\t536\n\t\t520\n\t\t504\n\t\t1008\n\t\t992\n\t\t488\n\t\t976\n\t\t960\n\t\t472\n\t\t944\n\t\t928\n\t\t456\n\t\t912\n\t\t896\n\t\t440\n\t\t880\n\t\t864\n\t\t424\n\t\t848\n\t\t832\n\t\t408\n\t\t816\n\t\t800\n\t\t392\n\t\t784\n\t\t768\n\t\t376\n\t\t752\n\t\t736\n\t\t360\n\t\t720\n\t\t704\n\t\t344\n\t\t688\n\t\t672\n\t\t328\n\t\t656\n\t\t640\n\t\t312\n\t\t624\n\t\t608\n\t\t296\n\t\t592\n\t\t576\n\t\t280\n\t\t560\n\t\t544\n\t\t264\n\t\t528\n\t\t512\n\t\t248\n\t\t496\n\t\t480\n\t\t232\n\t\t464\n\t\t448\n\t\t216\n\t\t432\n\t\t416\n\t\t200\n\t\t400\n\t\t384\n\t\t184\n\t\t368\n\t\t352\n\t\t168\n\t\t336\n\t\t320\n\t\t152\n\t\t304\n\t\t288\n\t\t136\n\t\t272\n\t\t256\n\t\t120\n\t\t240\n\t\t224\n\t\t104\n\t\t208\n\t\t192\n\t\t88\n\t\t176\n\t\t160\n\t\t72\n\t\t144\n\t\t128\n\t\t56\n\t\t112\n\t\t96\n\t\t40\n\t\t80\n\t\t64\n\t\t24\n\t\t48\n\t\t32\n\t\t8\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t8\n\t1\n\t128\n\t16\n )",
                "src_ctx": "hexagon_V6_vzb_128B"
            }
        }
    ],
    " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vsb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t1\n\t16\n\t1024\n\t1\n\t8\n\t2\n\t0\n )+ (typed:cast-int ; typed:cast-int_1_ip8_is1024_op16_os2048_signed_1\n\t (hvx_swizzle_2_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t8\n\t\t8\n\t\t0\n\t\t8\n\t\t8\n\t\t1016\n\t\t1000\n\t\t984\n\t\t968\n\t\t952\n\t\t936\n\t\t920\n\t\t904\n\t\t888\n\t\t872\n\t\t856\n\t\t840\n\t\t824\n\t\t808\n\t\t792\n\t\t776\n\t\t760\n\t\t744\n\t\t728\n\t\t712\n\t\t696\n\t\t680\n\t\t664\n\t\t648\n\t\t632\n\t\t616\n\t\t600\n\t\t584\n\t\t568\n\t\t552\n\t\t536\n\t\t520\n\t\t504\n\t\t1008\n\t\t992\n\t\t488\n\t\t976\n\t\t960\n\t\t472\n\t\t944\n\t\t928\n\t\t456\n\t\t912\n\t\t896\n\t\t440\n\t\t880\n\t\t864\n\t\t424\n\t\t848\n\t\t832\n\t\t408\n\t\t816\n\t\t800\n\t\t392\n\t\t784\n\t\t768\n\t\t376\n\t\t752\n\t\t736\n\t\t360\n\t\t720\n\t\t704\n\t\t344\n\t\t688\n\t\t672\n\t\t328\n\t\t656\n\t\t640\n\t\t312\n\t\t624\n\t\t608\n\t\t296\n\t\t592\n\t\t576\n\t\t280\n\t\t560\n\t\t544\n\t\t264\n\t\t528\n\t\t512\n\t\t248\n\t\t496\n\t\t480\n\t\t232\n\t\t464\n\t\t448\n\t\t216\n\t\t432\n\t\t416\n\t\t200\n\t\t400\n\t\t384\n\t\t184\n\t\t368\n\t\t352\n\t\t168\n\t\t336\n\t\t320\n\t\t152\n\t\t304\n\t\t288\n\t\t136\n\t\t272\n\t\t256\n\t\t120\n\t\t240\n\t\t224\n\t\t104\n\t\t208\n\t\t192\n\t\t88\n\t\t176\n\t\t160\n\t\t72\n\t\t144\n\t\t128\n\t\t56\n\t\t112\n\t\t96\n\t\t40\n\t\t80\n\t\t64\n\t\t24\n\t\t48\n\t\t32\n\t\t8\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t8\n\t1\n\t128\n\t16\n )+2048+hexagon_V6_vsb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 8 0 512 8 16 1 1 16 1024 1 8 2 0)",
                "dst": "(typed:cast-int (hvx_swizzle_2_dsl (reg (bv #x00 8)) 8 8 0 8 8 1016 1000 984 968 952 936 920 904 888 872 856 840 824 808 792 776 760 744 728 712 696 680 664 648 632 616 600 584 568 552 536 520 504 1008 992 488 976 960 472 944 928 456 912 896 440 880 864 424 848 832 408 816 800 392 784 768 376 752 736 360 720 704 344 688 672 328 656 640 312 624 608 296 592 576 280 560 544 264 528 512 248 496 480 232 464 448 216 432 416 200 400 384 184 368 352 168 336 320 152 304 288 136 272 256 120 240 224 104 208 192 88 176 160 72 144 128 56 112 96 40 80 64 24 48 32 8 16 0 0) 8 1 128 16)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsb_128B_dsl ; hexagon_V6_vsb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t1\n\t16\n\t1024\n\t1\n\t8\n\t2\n\t0\n )",
                "original_dst_expr": " (typed:cast-int ; typed:cast-int_1_ip8_is1024_op16_os2048_signed_1\n\t (hvx_swizzle_2_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t8\n\t\t8\n\t\t0\n\t\t8\n\t\t8\n\t\t1016\n\t\t1000\n\t\t984\n\t\t968\n\t\t952\n\t\t936\n\t\t920\n\t\t904\n\t\t888\n\t\t872\n\t\t856\n\t\t840\n\t\t824\n\t\t808\n\t\t792\n\t\t776\n\t\t760\n\t\t744\n\t\t728\n\t\t712\n\t\t696\n\t\t680\n\t\t664\n\t\t648\n\t\t632\n\t\t616\n\t\t600\n\t\t584\n\t\t568\n\t\t552\n\t\t536\n\t\t520\n\t\t504\n\t\t1008\n\t\t992\n\t\t488\n\t\t976\n\t\t960\n\t\t472\n\t\t944\n\t\t928\n\t\t456\n\t\t912\n\t\t896\n\t\t440\n\t\t880\n\t\t864\n\t\t424\n\t\t848\n\t\t832\n\t\t408\n\t\t816\n\t\t800\n\t\t392\n\t\t784\n\t\t768\n\t\t376\n\t\t752\n\t\t736\n\t\t360\n\t\t720\n\t\t704\n\t\t344\n\t\t688\n\t\t672\n\t\t328\n\t\t656\n\t\t640\n\t\t312\n\t\t624\n\t\t608\n\t\t296\n\t\t592\n\t\t576\n\t\t280\n\t\t560\n\t\t544\n\t\t264\n\t\t528\n\t\t512\n\t\t248\n\t\t496\n\t\t480\n\t\t232\n\t\t464\n\t\t448\n\t\t216\n\t\t432\n\t\t416\n\t\t200\n\t\t400\n\t\t384\n\t\t184\n\t\t368\n\t\t352\n\t\t168\n\t\t336\n\t\t320\n\t\t152\n\t\t304\n\t\t288\n\t\t136\n\t\t272\n\t\t256\n\t\t120\n\t\t240\n\t\t224\n\t\t104\n\t\t208\n\t\t192\n\t\t88\n\t\t176\n\t\t160\n\t\t72\n\t\t144\n\t\t128\n\t\t56\n\t\t112\n\t\t96\n\t\t40\n\t\t80\n\t\t64\n\t\t24\n\t\t48\n\t\t32\n\t\t8\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t8\n\t1\n\t128\n\t16\n )",
                "src_ctx": "hexagon_V6_vsb_128B"
            }
        }
    ],
    " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )+ (typed:cast-uint ; typed:cast-uint_1_ip32_is2048_op16_os1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1\n\t64\n\t16\n )+1024+hexagon_V6_vmpyih_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vmpyih_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 1 32 1 0)",
                "dst": "(typed:cast-uint (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) 32 1 64 16)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-uint ; typed:cast-uint_1_ip32_is2048_op16_os1024_signed_0\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1\n\t64\n\t16\n )",
                "src_ctx": "hexagon_V6_vmpyih_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )+ (typed:cast-int ; typed:cast-int_1_ip32_is2048_op16_os1024_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1\n\t64\n\t16\n )+1024+hexagon_V6_vmpyih_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vmpyih_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 1 32 1 0)",
                "dst": "(typed:cast-int (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) 32 1 64 16)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:cast-int ; typed:cast-int_1_ip32_is2048_op16_os1024_signed_1\n\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1\n\t64\n\t16\n )",
                "src_ctx": "hexagon_V6_vmpyih_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-bwnot (reg (bv #x00 8)) 32 1024) (typed:vec-bwnot (reg (bv #x01 8)) 8 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-bwnot (reg (bv #x00 8)) 8 1024) (typed:vec-bwnot (reg (bv #x01 8)) 16 1024) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-bwnot (reg (bv #x00 8)) 32 1024) (typed:vec-bwnot (reg (bv #x01 8)) 8 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-bwnot (reg (bv #x00 8)) 32 2048) (typed:vec-bwnot (reg (bv #x01 8)) 16 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-bwnot (reg (bv #x00 8)) 8 2048) (typed:vec-bwnot (reg (bv #x01 8)) 16 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-bwnot (reg (bv #x00 8)) 32 2048) (typed:vec-bwnot (reg (bv #x01 8)) 64 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) 64 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 16 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubuhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubuwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) 64 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )+2048+hexagon_V6_vsubh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-sub (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubuhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 2048) 64 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsububsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsububsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 2048) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubuwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 2048) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubuhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubuwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 2048) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubuhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsububsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) 64 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsububsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubuwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 2048) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p64_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubuwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p64_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p64_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubuhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p64_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p64_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubuhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p64_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p64_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsububsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p64_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p64_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsububsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p64_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p64_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubuwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p64_s1024_signed_1\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vsubuhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vsubuwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )+2048+hexagon_V6_vsubuhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vsububsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )+2048+hexagon_V6_vsububsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) 64 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )+2048+hexagon_V6_vsubuwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 2048) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) (reg (bv #x00 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) (reg (bv #x01 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 2048) (reg (bv #x01 8)) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) (reg (bv #x00 8)) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+2048+hexagon_V6_vsubh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 2048) (reg (bv #x00 8)) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubuhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubuwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 1024) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 1024) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsububsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 2048) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsububsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubuhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) (reg (bv #x01 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubuwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 2048) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048) 64 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsububsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vsubuhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) (reg (bv #x00 8)) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vsubuwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024) (reg (bv #x00 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) (reg (bv #x00 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) (reg (bv #x00 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+2048+hexagon_V6_vsubuhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) (reg (bv #x00 8)) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+2048+hexagon_V6_vsububsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (reg (bv #x00 8)) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vsububsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) (reg (bv #x01 8)) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) (reg (bv #x00 8)) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) (reg (bv #x01 8)) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+2048+hexagon_V6_vsubuwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 2048) (reg (bv #x00 8)) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+2048+hexagon_V6_vsubh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 2048) (reg (bv #x00 8)) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubuhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubuwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubuhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 2048) 64 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsububsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 2048) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsububsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubuwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 2048) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) 64 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubuwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubuhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 64 1024) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubuhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 2048) 64 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsububsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsububsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubuwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 2048) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 2048) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubh_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 2048) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 64 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubb_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 1024) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubbsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubbsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+1024+hexagon_V6_vsubhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubbsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 64 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubbsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )+2048+hexagon_V6_vsubw_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 32 -1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 2048) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vsubuwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vsubuhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t16\n\t1024\n )+2048+hexagon_V6_vsubuhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vsububsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t16\n\t1024\n )+2048+hexagon_V6_vsububsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 8 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x01 8)) 8 2048) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsububsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t16\n\t1024\n )+2048+hexagon_V6_vsubuwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 32 0 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x01 8)) 32 2048) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubuwsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubuwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )+2048+hexagon_V6_vsubwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )+2048+hexagon_V6_vsubhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vsubwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 1024) 64 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vsubbsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 1024) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubbsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vsubhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )+2048+hexagon_V6_vsubbsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubbsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )+2048+hexagon_V6_vsubwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 32 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 2048) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )+2048+hexagon_V6_vsubhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 32 2048) 64 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )+1024+hexagon_V6_vsubbsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubbsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )+1024+hexagon_V6_vsubwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )+1024+hexagon_V6_vsubhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )+2048+hexagon_V6_vsubbsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 16 2048) 32 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubwsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p64_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t32\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t64\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubbsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubwsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 32 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 2048) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 2048) 16 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubwsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubhsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubhsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubwsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubwsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubbsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubbsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vsubhsat_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubhsat_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vsubh_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubh_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )+2048+hexagon_V6_vsubbsat_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 1 0)",
                "dst": "(typed:vec-sub (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 2048) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 2048) 64 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p64_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t64\n\t\t1024\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubbsat_dv_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vsubb_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 32 1024) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )+1024+hexagon_V6_vsubw_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubw_128B"
            }
        }
    ],
    " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )+ (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )+2048+hexagon_V6_vsubb_dv_128B": [
        {
            "property_name": "EnumeratePattern",
            "property": {
                "src": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 8 -1 0)",
                "dst": "(typed:vec-sub (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 32 2048) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 2048) 8 2048)",
                "output_size": 2048,
                "original_src_expr": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vsubb_dv_128B"
            }
        }
    ]
}