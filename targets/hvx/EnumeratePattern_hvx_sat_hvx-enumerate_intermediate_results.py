{
    " (typed:vec-saturate ; typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_1\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> False\n\t32\n\t1\n\t64\n\t16\n\t#t\n )+ (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwh_sat_128B\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t1\n\t32\n\t1\n\t32\n\t1\n\t32\n\t1\n\t16\n\t0\n )+1024+typed:vec-saturate_1_ip16_is2048_op8_os1024_signed_0+hexagon_V6_vpackhub_sat_128B": [
        {
            "property_name": "EnumeratePattern_hvx_sat",
            "property": {
                "src": "(typed:vec-saturate (reg (bv #x00 8)) 16 1 128 8 #f)",
                "dst": "(hexagon_V6_vpackwuh_sat_128B_dsl (hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0) (hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0) 1024 1024 0 512 8 0 512 8 0 16 1 64 0 16 1 8 0)",
                "output_size": 1024,
                "original_src_expr": " (typed:vec-saturate ; typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_1\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> False\n\t32\n\t1\n\t64\n\t16\n\t#t\n )",
                "original_dst_expr": " (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwh_sat_128B\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t1\n\t32\n\t1\n\t32\n\t1\n\t32\n\t1\n\t16\n\t0\n )",
                "src_ctx": "typed:vec-saturate_1_ip16_is2048_op8_os1024_signed_0",
                "dst_ctx": "hexagon_V6_vpackhub_sat_128B"
            }
        }
    ],
    " (typed:vec-saturate ; typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_1\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> False\n\t32\n\t1\n\t64\n\t16\n\t#t\n )+ (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwh_sat_128B\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t1\n\t32\n\t1\n\t32\n\t1\n\t32\n\t1\n\t16\n\t0\n )+1024+typed:vec-saturate_1_ip16_is2048_op8_os1024_signed_1+hexagon_V6_vpackhb_sat_128B": [
        {
            "property_name": "EnumeratePattern_hvx_sat",
            "property": {
                "src": "(typed:vec-saturate (reg (bv #x00 8)) 16 1 128 8 #t)",
                "dst": "(hexagon_V6_vpackwuh_sat_128B_dsl (hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0) (hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0) 1024 1024 0 512 8 0 512 8 1 16 1 64 1 16 1 8 0)",
                "output_size": 1024,
                "original_src_expr": " (typed:vec-saturate ; typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_1\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> False\n\t32\n\t1\n\t64\n\t16\n\t#t\n )",
                "original_dst_expr": " (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwh_sat_128B\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t1\n\t32\n\t1\n\t32\n\t1\n\t32\n\t1\n\t16\n\t0\n )",
                "src_ctx": "typed:vec-saturate_1_ip16_is2048_op8_os1024_signed_1",
                "dst_ctx": "hexagon_V6_vpackhb_sat_128B"
            }
        }
    ],
    " (typed:vec-saturate ; typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_1\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> False\n\t32\n\t1\n\t64\n\t16\n\t#t\n )+ (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwh_sat_128B\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t1\n\t32\n\t1\n\t32\n\t1\n\t32\n\t1\n\t16\n\t0\n )+1024+typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_0+hexagon_V6_vpackwuh_sat_128B": [
        {
            "property_name": "EnumeratePattern_hvx_sat",
            "property": {
                "src": "(typed:vec-saturate (reg (bv #x00 8)) 32 1 64 16 #f)",
                "dst": "(hexagon_V6_vpackwuh_sat_128B_dsl (hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0) (hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0) 1024 1024 0 512 16 0 512 16 0 32 1 32 0 32 1 16 0)",
                "output_size": 1024,
                "original_src_expr": " (typed:vec-saturate ; typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_1\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> False\n\t32\n\t1\n\t64\n\t16\n\t#t\n )",
                "original_dst_expr": " (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwh_sat_128B\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t1\n\t32\n\t1\n\t32\n\t1\n\t32\n\t1\n\t16\n\t0\n )",
                "src_ctx": "typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_0",
                "dst_ctx": "hexagon_V6_vpackwuh_sat_128B"
            }
        }
    ],
    " (typed:vec-saturate ; typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_1\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> False\n\t32\n\t1\n\t64\n\t16\n\t#t\n )+ (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwh_sat_128B\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t1\n\t32\n\t1\n\t32\n\t1\n\t32\n\t1\n\t16\n\t0\n )+1024+typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_1+hexagon_V6_vpackwh_sat_128B": [
        {
            "property_name": "EnumeratePattern_hvx_sat",
            "property": {
                "src": "(typed:vec-saturate (reg (bv #x00 8)) 32 1 64 16 #t)",
                "dst": "(hexagon_V6_vpackwuh_sat_128B_dsl (hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0) (hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0) 1024 1024 0 512 16 0 512 16 1 32 1 32 1 32 1 16 0)",
                "output_size": 1024,
                "original_src_expr": " (typed:vec-saturate ; typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_1\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> False\n\t32\n\t1\n\t64\n\t16\n\t#t\n )",
                "original_dst_expr": " (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwh_sat_128B\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t1\n\t32\n\t1\n\t32\n\t1\n\t32\n\t1\n\t16\n\t0\n )",
                "src_ctx": "typed:vec-saturate_1_ip32_is2048_op16_os1024_signed_1",
                "dst_ctx": "hexagon_V6_vpackwh_sat_128B"
            }
        }
    ]
}