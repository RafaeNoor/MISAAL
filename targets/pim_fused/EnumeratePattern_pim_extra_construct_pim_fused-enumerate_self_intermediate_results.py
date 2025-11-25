{
    " (test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl ; test_enum_1_test_enum_custom_scaled_add_i8_s128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t8\n\t8\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n\t0\n )+ (test_enum_1_comb_2_fused_pim_op_7_dsl ; test_enum_1_comb_5_fused_pim_op_5\n\t (test_enum_1_comb_3_fused_pim_op_9_dsl ; test_enum_1_comb_5_fused_pim_op_7\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t (test_enum_1_comb_2_fused_pim_op_0_dsl ; test_enum_1_comb_5_fused_pim_op_0\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t8\n\t\t\t8\n\t\t\t0\n\t\t\t128\n\t\t\t8\n\t\t\t0\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )+256+test_enum_1_test_enum_custom_scaled_add_i8_s256+test_enum_1_comb_5_fused_pim_op_5_extended_size_256_bw_8_ctx_0": [
        {
            "property_name": "EnumeratePattern_pim_extra_construct",
            "property": {
                "src": "(test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 8 8 0 256 8 -1 0 16 0 0 0)",
                "dst": "(test_enum_1_comb_2_fused_pim_op_7_dsl (test_enum_1_comb_3_fused_pim_op_9_dsl (reg (bv #x00 8)) (test_enum_1_comb_2_fused_pim_op_0_dsl (reg (bv #x01 8)) 8 8 0 256 8 0 0) 256 256 0 256 8 1 8 1 0) (reg (bv #x02 8)) 256 256 0 256 8 -1 0)",
                "output_size": 256,
                "original_src_expr": " (test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl ; test_enum_1_test_enum_custom_scaled_add_i8_s128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t8\n\t8\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n\t0\n )",
                "original_dst_expr": " (test_enum_1_comb_2_fused_pim_op_7_dsl ; test_enum_1_comb_5_fused_pim_op_5\n\t (test_enum_1_comb_3_fused_pim_op_9_dsl ; test_enum_1_comb_5_fused_pim_op_7\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t (test_enum_1_comb_2_fused_pim_op_0_dsl ; test_enum_1_comb_5_fused_pim_op_0\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t8\n\t\t\t8\n\t\t\t0\n\t\t\t128\n\t\t\t8\n\t\t\t0\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "test_enum_1_test_enum_custom_scaled_add_i8_s256",
                "dst_ctx": "test_enum_1_comb_5_fused_pim_op_5_extended_size_256_bw_8_ctx_0"
            }
        }
    ],
    " (test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl ; test_enum_1_test_enum_custom_scaled_add_i8_s128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t8\n\t8\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n\t0\n )+ (test_enum_1_comb_2_fused_pim_op_7_dsl ; test_enum_1_comb_5_fused_pim_op_5\n\t (test_enum_1_comb_3_fused_pim_op_9_dsl ; test_enum_1_comb_5_fused_pim_op_7\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t (test_enum_1_comb_2_fused_pim_op_0_dsl ; test_enum_1_comb_5_fused_pim_op_0\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t8\n\t\t\t8\n\t\t\t0\n\t\t\t128\n\t\t\t8\n\t\t\t0\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )+256+test_enum_1_test_enum_custom_scaled_add_i16_s256+test_enum_1_comb_6_fused_pim_op_7_extended_size_256_bw_16_ctx_0": [
        {
            "property_name": "EnumeratePattern_pim_extra_construct",
            "property": {
                "src": "(test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16 0 256 16 -1 0 32 0 0 0)",
                "dst": "(test_enum_1_comb_2_fused_pim_op_7_dsl (test_enum_1_comb_3_fused_pim_op_9_dsl (reg (bv #x02 8)) (test_enum_1_comb_2_fused_pim_op_0_dsl (reg (bv #x01 8)) 16 16 0 256 16 0 0) 256 256 0 256 16 1 16 1 0) (reg (bv #x00 8)) 256 256 0 256 16 -1 0)",
                "output_size": 256,
                "original_src_expr": " (test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl ; test_enum_1_test_enum_custom_scaled_add_i8_s128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t8\n\t8\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n\t0\n )",
                "original_dst_expr": " (test_enum_1_comb_2_fused_pim_op_7_dsl ; test_enum_1_comb_5_fused_pim_op_5\n\t (test_enum_1_comb_3_fused_pim_op_9_dsl ; test_enum_1_comb_5_fused_pim_op_7\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t (test_enum_1_comb_2_fused_pim_op_0_dsl ; test_enum_1_comb_5_fused_pim_op_0\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t8\n\t\t\t8\n\t\t\t0\n\t\t\t128\n\t\t\t8\n\t\t\t0\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "test_enum_1_test_enum_custom_scaled_add_i16_s256",
                "dst_ctx": "test_enum_1_comb_6_fused_pim_op_7_extended_size_256_bw_16_ctx_0"
            }
        }
    ],
    " (test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl ; test_enum_1_test_enum_custom_scaled_add_i8_s128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t8\n\t8\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n\t0\n )+ (test_enum_1_comb_2_fused_pim_op_7_dsl ; test_enum_1_comb_5_fused_pim_op_5\n\t (test_enum_1_comb_3_fused_pim_op_9_dsl ; test_enum_1_comb_5_fused_pim_op_7\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t (test_enum_1_comb_2_fused_pim_op_0_dsl ; test_enum_1_comb_5_fused_pim_op_0\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t8\n\t\t\t8\n\t\t\t0\n\t\t\t128\n\t\t\t8\n\t\t\t0\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )+128+test_enum_1_test_enum_custom_scaled_add_i32_s128+test_enum_1_comb_7_fused_pim_op_7": [
        {
            "property_name": "EnumeratePattern_pim_extra_construct",
            "property": {
                "src": "(test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 32 32 0 128 32 -1 0 64 0 0 0)",
                "dst": "(test_enum_1_comb_2_fused_pim_op_7_dsl (test_enum_1_comb_3_fused_pim_op_9_dsl (reg (bv #x00 8)) (test_enum_1_comb_2_fused_pim_op_0_dsl (reg (bv #x01 8)) 32 32 0 128 32 0 0) 128 128 0 128 32 1 64 1 0) (reg (bv #x02 8)) 128 128 0 128 32 -1 0)",
                "output_size": 128,
                "original_src_expr": " (test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl ; test_enum_1_test_enum_custom_scaled_add_i8_s128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t8\n\t8\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n\t0\n )",
                "original_dst_expr": " (test_enum_1_comb_2_fused_pim_op_7_dsl ; test_enum_1_comb_5_fused_pim_op_5\n\t (test_enum_1_comb_3_fused_pim_op_9_dsl ; test_enum_1_comb_5_fused_pim_op_7\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t (test_enum_1_comb_2_fused_pim_op_0_dsl ; test_enum_1_comb_5_fused_pim_op_0\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t8\n\t\t\t8\n\t\t\t0\n\t\t\t128\n\t\t\t8\n\t\t\t0\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "test_enum_1_test_enum_custom_scaled_add_i32_s128",
                "dst_ctx": "test_enum_1_comb_7_fused_pim_op_7"
            }
        }
    ],
    " (test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl ; test_enum_1_test_enum_custom_scaled_add_i8_s128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t8\n\t8\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n\t0\n )+ (test_enum_1_comb_2_fused_pim_op_7_dsl ; test_enum_1_comb_5_fused_pim_op_5\n\t (test_enum_1_comb_3_fused_pim_op_9_dsl ; test_enum_1_comb_5_fused_pim_op_7\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t (test_enum_1_comb_2_fused_pim_op_0_dsl ; test_enum_1_comb_5_fused_pim_op_0\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t8\n\t\t\t8\n\t\t\t0\n\t\t\t128\n\t\t\t8\n\t\t\t0\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )+128+test_enum_1_test_enum_custom_scaled_add_i8_s128+test_enum_1_comb_5_fused_pim_op_5": [
        {
            "property_name": "EnumeratePattern_pim_extra_construct",
            "property": {
                "src": "(test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 8 8 0 128 8 -1 0 16 0 0 0)",
                "dst": "(test_enum_1_comb_2_fused_pim_op_7_dsl (test_enum_1_comb_3_fused_pim_op_9_dsl (reg (bv #x00 8)) (test_enum_1_comb_2_fused_pim_op_0_dsl (reg (bv #x01 8)) 8 8 0 128 8 0 0) 128 128 0 128 8 1 16 1 0) (reg (bv #x02 8)) 128 128 0 128 8 -1 0)",
                "output_size": 128,
                "original_src_expr": " (test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl ; test_enum_1_test_enum_custom_scaled_add_i8_s128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t8\n\t8\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n\t0\n )",
                "original_dst_expr": " (test_enum_1_comb_2_fused_pim_op_7_dsl ; test_enum_1_comb_5_fused_pim_op_5\n\t (test_enum_1_comb_3_fused_pim_op_9_dsl ; test_enum_1_comb_5_fused_pim_op_7\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t (test_enum_1_comb_2_fused_pim_op_0_dsl ; test_enum_1_comb_5_fused_pim_op_0\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t8\n\t\t\t8\n\t\t\t0\n\t\t\t128\n\t\t\t8\n\t\t\t0\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "test_enum_1_test_enum_custom_scaled_add_i8_s128",
                "dst_ctx": "test_enum_1_comb_5_fused_pim_op_5"
            }
        }
    ],
    " (test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl ; test_enum_1_test_enum_custom_scaled_add_i8_s128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t8\n\t8\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n\t0\n )+ (test_enum_1_comb_2_fused_pim_op_7_dsl ; test_enum_1_comb_5_fused_pim_op_5\n\t (test_enum_1_comb_3_fused_pim_op_9_dsl ; test_enum_1_comb_5_fused_pim_op_7\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t (test_enum_1_comb_2_fused_pim_op_0_dsl ; test_enum_1_comb_5_fused_pim_op_0\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t8\n\t\t\t8\n\t\t\t0\n\t\t\t128\n\t\t\t8\n\t\t\t0\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )+128+test_enum_1_test_enum_custom_scaled_add_i16_s128+test_enum_1_comb_6_fused_pim_op_7": [
        {
            "property_name": "EnumeratePattern_pim_extra_construct",
            "property": {
                "src": "(test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 16 16 0 128 16 -1 0 32 0 0 0)",
                "dst": "(test_enum_1_comb_2_fused_pim_op_7_dsl (test_enum_1_comb_3_fused_pim_op_9_dsl (reg (bv #x00 8)) (test_enum_1_comb_2_fused_pim_op_0_dsl (reg (bv #x01 8)) 16 16 0 128 16 0 0) 128 128 0 128 16 1 32 1 0) (reg (bv #x02 8)) 128 128 0 128 16 -1 0)",
                "output_size": 128,
                "original_src_expr": " (test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl ; test_enum_1_test_enum_custom_scaled_add_i8_s128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t8\n\t8\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n\t0\n )",
                "original_dst_expr": " (test_enum_1_comb_2_fused_pim_op_7_dsl ; test_enum_1_comb_5_fused_pim_op_5\n\t (test_enum_1_comb_3_fused_pim_op_9_dsl ; test_enum_1_comb_5_fused_pim_op_7\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t (test_enum_1_comb_2_fused_pim_op_0_dsl ; test_enum_1_comb_5_fused_pim_op_0\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t8\n\t\t\t8\n\t\t\t0\n\t\t\t128\n\t\t\t8\n\t\t\t0\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "test_enum_1_test_enum_custom_scaled_add_i16_s128",
                "dst_ctx": "test_enum_1_comb_6_fused_pim_op_7"
            }
        }
    ],
    " (test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl ; test_enum_1_test_enum_custom_scaled_add_i8_s128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t8\n\t8\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n\t0\n )+ (test_enum_1_comb_2_fused_pim_op_7_dsl ; test_enum_1_comb_5_fused_pim_op_5\n\t (test_enum_1_comb_3_fused_pim_op_9_dsl ; test_enum_1_comb_5_fused_pim_op_7\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t (test_enum_1_comb_2_fused_pim_op_0_dsl ; test_enum_1_comb_5_fused_pim_op_0\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t8\n\t\t\t8\n\t\t\t0\n\t\t\t128\n\t\t\t8\n\t\t\t0\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )+256+test_enum_1_test_enum_custom_scaled_add_i32_s256+test_enum_1_comb_7_fused_pim_op_7_extended_size_256_bw_32_ctx_0": [
        {
            "property_name": "EnumeratePattern_pim_extra_construct",
            "property": {
                "src": "(test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 256 32 -1 0 64 0 0 0)",
                "dst": "(test_enum_1_comb_2_fused_pim_op_7_dsl (test_enum_1_comb_3_fused_pim_op_9_dsl (reg (bv #x02 8)) (test_enum_1_comb_2_fused_pim_op_0_dsl (reg (bv #x01 8)) 32 32 0 256 32 0 0) 256 256 0 256 32 1 32 1 0) (reg (bv #x00 8)) 256 256 0 256 32 -1 0)",
                "output_size": 256,
                "original_src_expr": " (test_enum_1_test_enum_custom_scaled_add_i16_s256_dsl ; test_enum_1_test_enum_custom_scaled_add_i8_s128\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t8\n\t8\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n\t0\n )",
                "original_dst_expr": " (test_enum_1_comb_2_fused_pim_op_7_dsl ; test_enum_1_comb_5_fused_pim_op_5\n\t (test_enum_1_comb_3_fused_pim_op_9_dsl ; test_enum_1_comb_5_fused_pim_op_7\n\t\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t\t (test_enum_1_comb_2_fused_pim_op_0_dsl ; test_enum_1_comb_5_fused_pim_op_0\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t8\n\t\t\t8\n\t\t\t0\n\t\t\t128\n\t\t\t8\n\t\t\t0\n\t\t\t0\n\t\t )\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t8\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )",
                "src_ctx": "test_enum_1_test_enum_custom_scaled_add_i32_s256",
                "dst_ctx": "test_enum_1_comb_7_fused_pim_op_7_extended_size_256_bw_32_ctx_0"
            }
        }
    ]
}