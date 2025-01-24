{
    " (hexagon_V6_vaslw_acc_128B_dsl ; hexagon_V6_vaslw_acc_128B\n\t(lit (bv #x0000001f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 4 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )+ (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is32_os1024_signed_None\n\t\t\t(buffer-index  2 'uint8 32) ; < 4 x i8> False\n\t\t\t32\n\t\t\t32\n\t\t\t32\n\t\t )\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )+1024+hexagon_V6_vaslw_acc_128B+typed:vec-add_p32_s1024_signed_None": [
        {
            "property_name": "EnumeratePattern_shift_left_acc",
            "property": {
                "src": "(hexagon_V6_vaslw_acc_128B_dsl (lit (bv #x0000001f 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-add (typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 32 32 32) 32 1024) (reg (bv #x01 8)) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vaslw_acc_128B_dsl ; hexagon_V6_vaslw_acc_128B\n\t(lit (bv #x0000001f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 4 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p32_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is32_os1024_signed_None\n\t\t\t(buffer-index  2 'uint8 32) ; < 4 x i8> False\n\t\t\t32\n\t\t\t32\n\t\t\t32\n\t\t )\n\t\t32\n\t\t1024\n\t )\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaslw_acc_128B",
                "dst_ctx": "typed:vec-add_p32_s1024_signed_None"
            }
        }
    ],
    " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip8_is16_op16_os32_signed_1\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t1\n\t\t2\n\t\t16\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )+ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vaslh_acc_128B+typed:vec-add_p16_s1024_signed_None": [
        {
            "property_name": "EnumeratePattern_shift_left_acc",
            "property": {
                "src": "(hexagon_V6_vaslh_acc_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) (typed:cast-int-extend (reg (bv #x02 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-add (typed:vec-shl (reg (bv #x01 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 64) 16 1024) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip8_is16_op16_os32_signed_1\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t1\n\t\t2\n\t\t16\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaslh_acc_128B",
                "dst_ctx": "typed:vec-add_p16_s1024_signed_None"
            }
        }
    ],
    " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is16_op16_os32_signed_0\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t1\n\t\t2\n\t\t16\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )+ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vaslh_acc_128B+typed:vec-add_p16_s1024_signed_None": [
        {
            "property_name": "EnumeratePattern_shift_left_acc",
            "property": {
                "src": "(hexagon_V6_vaslh_acc_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) (typed:cast-uint-extend (reg (bv #x02 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-add (typed:vec-shl (reg (bv #x01 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 64) 16 1024) (reg (bv #x00 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is16_op16_os32_signed_0\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t8\n\t\t1\n\t\t2\n\t\t16\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaslh_acc_128B",
                "dst_ctx": "typed:vec-add_p16_s1024_signed_None"
            }
        }
    ],
    " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )+ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p64_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t64\n\t\t1024\n\t )\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )+1024+hexagon_V6_vaslh_acc_128B+typed:vec-add_p16_s1024_signed_None": [
        {
            "property_name": "EnumeratePattern_shift_left_acc",
            "property": {
                "src": "(hexagon_V6_vaslh_acc_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 2) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-add (typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 64) 64 1024) (reg (bv #x01 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os32_signed_None\n\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t16\n\t\t16\n\t\t2\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )",
                "original_dst_expr": " (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p64_s1024_signed_None\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  2 'uint8 16) ; < 2 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t64\n\t\t1024\n\t )\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t16\n\t1024\n )",
                "src_ctx": "hexagon_V6_vaslh_acc_128B",
                "dst_ctx": "typed:vec-add_p16_s1024_signed_None"
            }
        }
    ]
}