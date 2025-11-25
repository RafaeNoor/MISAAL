{
    " (test_enum_2_comb_27_fused_pim_op_2019_dsl ; test_enum_2_comb_27_fused_pim_op_2019\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t-1\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2019_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0 16 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1595_dsl ; test_enum_2_comb_21_fused_pim_op_1595\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1595_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 -1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_2232_dsl ; test_enum_2_comb_26_fused_pim_op_2232\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_2232_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1026_dsl ; test_enum_2_comb_18_fused_pim_op_1026\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1026_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_227_dsl ; test_enum_2_comb_30_fused_pim_op_227\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_227_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_847_dsl ; test_enum_2_comb_30_fused_pim_op_847\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_847_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2301_dsl ; test_enum_2_comb_22_fused_pim_op_2301\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2301_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_3_fused_pim_op_3_dsl ; test_enum_2_comb_3_fused_pim_op_3\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_3_fused_pim_op_3_dsl (reg (bv #x00 8)) 512 512 0 512 16 32 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 32 1024 16)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2323_dsl ; test_enum_2_comb_22_fused_pim_op_2323\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2323_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1644_dsl ; test_enum_2_comb_17_fused_pim_op_1644\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1644_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_267_dsl ; test_enum_2_comb_19_fused_pim_op_267\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_267_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1301_dsl ; test_enum_2_comb_20_fused_pim_op_1301\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t16\n\t0\n\t0\n\t32\n\t0\n\t32\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1301_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 16 0 0 32 0 32 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1301_dsl ; test_enum_2_comb_20_fused_pim_op_1301\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t16\n\t0\n\t0\n\t32\n\t0\n\t32\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1301_dsl (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 16 0 0 32 0 32 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1065_dsl ; test_enum_2_comb_25_fused_pim_op_1065\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1065_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_289_dsl ; test_enum_2_comb_23_fused_pim_op_289\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_289_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_1169_dsl ; test_enum_2_comb_22_fused_pim_op_1169\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_1169_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1884_dsl ; test_enum_2_comb_23_fused_pim_op_1884\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n\t64\n\t0\n\t64\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1884_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0 32 0 32 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_1913_dsl ; test_enum_2_comb_31_fused_pim_op_1913\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t512\n\t32\n\t0\n\t0\n\t0\n )_ (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_1913_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0 512 16 0 0 0)",
                "dst": "(typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 16 32)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_527_dsl ; test_enum_2_comb_23_fused_pim_op_527\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_527_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_130_dsl ; test_enum_2_comb_25_fused_pim_op_130\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_130_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_130_dsl ; test_enum_2_comb_25_fused_pim_op_130\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_130_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_124_dsl ; test_enum_2_comb_17_fused_pim_op_124\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_124_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0 32 0 -1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_574_dsl ; test_enum_2_comb_22_fused_pim_op_574\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_574_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_774_dsl ; test_enum_2_comb_18_fused_pim_op_774\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_774_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2391_dsl ; test_enum_2_comb_22_fused_pim_op_2391\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2391_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1191_dsl ; test_enum_2_comb_29_fused_pim_op_1191\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1191_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_882_dsl ; test_enum_2_comb_29_fused_pim_op_882\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_882_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_3610_dsl ; test_enum_2_comb_31_fused_pim_op_3610\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_3610_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_2112_dsl ; test_enum_2_comb_18_fused_pim_op_2112\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_2112_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_511_dsl ; test_enum_2_comb_23_fused_pim_op_511\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n\t64\n\t0\n\t64\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_511_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0 0 32 0 32 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_1105_dsl ; test_enum_2_comb_16_fused_pim_op_1105\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t16\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_1105_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 16 8 1 8 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_1390_dsl ; test_enum_2_comb_27_fused_pim_op_1390\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_1390_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_1390_dsl ; test_enum_2_comb_27_fused_pim_op_1390\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_1390_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1015_dsl ; test_enum_2_comb_17_fused_pim_op_1015\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1015_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1096_dsl ; test_enum_2_comb_25_fused_pim_op_1096\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1096_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256 1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1879_dsl ; test_enum_2_comb_23_fused_pim_op_1879\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n\t64\n\t0\n\t64\n\t0\n\t0\n\t64\n\t0\n\t64\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1879_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0 16 0 16 0 0 16 0 16 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1511_dsl ; test_enum_2_comb_21_fused_pim_op_1511\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1511_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_634_dsl ; test_enum_2_comb_29_fused_pim_op_634\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_634_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_483_dsl ; test_enum_2_comb_20_fused_pim_op_483\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_483_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_483_dsl ; test_enum_2_comb_20_fused_pim_op_483\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_483_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_1819_dsl ; test_enum_2_comb_30_fused_pim_op_1819\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_1819_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_1819_dsl ; test_enum_2_comb_30_fused_pim_op_1819\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_1819_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_520_dsl ; test_enum_2_comb_31_fused_pim_op_520\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t-1\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_520_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 -1 0 16 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_453_dsl ; test_enum_2_comb_19_fused_pim_op_453\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_453_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1061_dsl ; test_enum_2_comb_18_fused_pim_op_1061\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1061_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_194_dsl ; test_enum_2_comb_27_fused_pim_op_194\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_194_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_859_dsl ; test_enum_2_comb_28_fused_pim_op_859\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_859_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_859_dsl ; test_enum_2_comb_28_fused_pim_op_859\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_859_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1336_dsl ; test_enum_2_comb_29_fused_pim_op_1336\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t0\n\t512\n\t8\n\t0\n\t0\n\t0\n )_ (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1336_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0 512 16 0 0 0)",
                "dst": "(typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 16 32)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_635_dsl ; test_enum_2_comb_31_fused_pim_op_635\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_635_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2120_dsl ; test_enum_2_comb_22_fused_pim_op_2120\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2120_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0 16 0 16 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_56_dsl ; test_enum_2_comb_26_fused_pim_op_56\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_56_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1915_dsl ; test_enum_2_comb_18_fused_pim_op_1915\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1915_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1915_dsl ; test_enum_2_comb_18_fused_pim_op_1915\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1915_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1272_dsl ; test_enum_2_comb_21_fused_pim_op_1272\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1272_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1884_dsl ; test_enum_2_comb_29_fused_pim_op_1884\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1884_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2107_dsl ; test_enum_2_comb_22_fused_pim_op_2107\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2107_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_2062_dsl ; test_enum_2_comb_18_fused_pim_op_2062\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_2062_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_276_dsl ; test_enum_2_comb_31_fused_pim_op_276\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_276_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1495_dsl ; test_enum_2_comb_17_fused_pim_op_1495\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1495_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1495_dsl ; test_enum_2_comb_17_fused_pim_op_1495\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1495_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_834_dsl ; test_enum_2_comb_26_fused_pim_op_834\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_834_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_525_dsl ; test_enum_2_comb_19_fused_pim_op_525\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_525_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_525_dsl ; test_enum_2_comb_19_fused_pim_op_525\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-absd_dsl ; typed-folded:vec-absd_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_525_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0 0 0)",
                "dst": "(typed-folded:vec-absd_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_665_dsl ; test_enum_2_comb_26_fused_pim_op_665\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t2\n\t0\n\t1\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_665_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 32 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 256 0)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1594_dsl ; test_enum_2_comb_21_fused_pim_op_1594\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1594_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 -1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_437_dsl ; test_enum_2_comb_17_fused_pim_op_437\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_437_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1876_dsl ; test_enum_2_comb_21_fused_pim_op_1876\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1876_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1849_dsl ; test_enum_2_comb_23_fused_pim_op_1849\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1849_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_869_dsl ; test_enum_2_comb_25_fused_pim_op_869\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_869_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_535_dsl ; test_enum_2_comb_18_fused_pim_op_535\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_535_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 -1 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_261_dsl ; test_enum_2_comb_30_fused_pim_op_261\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_261_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1962_dsl ; test_enum_2_comb_23_fused_pim_op_1962\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1962_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1962_dsl ; test_enum_2_comb_23_fused_pim_op_1962\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1962_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_1354_dsl ; test_enum_2_comb_22_fused_pim_op_1354\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_1354_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_1602_dsl ; test_enum_2_comb_26_fused_pim_op_1602\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_1602_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_1918_dsl ; test_enum_2_comb_22_fused_pim_op_1918\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_1918_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 256 256 0 256 8 16 2 1 0 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 256 16 1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_576_dsl ; test_enum_2_comb_19_fused_pim_op_576\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_576_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_39_dsl ; test_enum_2_comb_22_fused_pim_op_39\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t32\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_39_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 64 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 64 1024 32)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_547_dsl ; test_enum_2_comb_31_fused_pim_op_547\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_547_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_2391_dsl ; test_enum_2_comb_27_fused_pim_op_2391\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t1\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2391_dsl (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 512 512 0 512 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2233_dsl ; test_enum_2_comb_22_fused_pim_op_2233\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2233_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1864_dsl ; test_enum_2_comb_29_fused_pim_op_1864\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1864_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_191_dsl ; test_enum_2_comb_28_fused_pim_op_191\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_191_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_191_dsl ; test_enum_2_comb_28_fused_pim_op_191\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_191_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1831_dsl ; test_enum_2_comb_21_fused_pim_op_1831\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1831_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_856_dsl ; test_enum_2_comb_29_fused_pim_op_856\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_856_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_1839_dsl ; test_enum_2_comb_31_fused_pim_op_1839\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_1839_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_2115_dsl ; test_enum_2_comb_18_fused_pim_op_2115\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_2115_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_2115_dsl ; test_enum_2_comb_18_fused_pim_op_2115\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_2115_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_2143_dsl ; test_enum_2_comb_29_fused_pim_op_2143\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_2143_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_2143_dsl ; test_enum_2_comb_29_fused_pim_op_2143\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_2143_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1936_dsl ; test_enum_2_comb_19_fused_pim_op_1936\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1936_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_589_dsl ; test_enum_2_comb_22_fused_pim_op_589\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_589_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_2111_dsl ; test_enum_2_comb_27_fused_pim_op_2111\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2111_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1894_dsl ; test_enum_2_comb_19_fused_pim_op_1894\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1894_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1245_dsl ; test_enum_2_comb_17_fused_pim_op_1245\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1245_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1103_dsl ; test_enum_2_comb_19_fused_pim_op_1103\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t64\n\t32\n\t1\n\t0\n\t0\n\t0\n )_ (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1103_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0 512 16 1 0 0 0)",
                "dst": "(typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 16 32)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_1768_dsl ; test_enum_2_comb_31_fused_pim_op_1768\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_1768_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_2084_dsl ; test_enum_2_comb_26_fused_pim_op_2084\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_2084_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_230_dsl ; test_enum_2_comb_17_fused_pim_op_230\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_230_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0 0 64 0 64 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1621_dsl ; test_enum_2_comb_25_fused_pim_op_1621\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t-1\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1621_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0 0 16 0 16 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1858_dsl ; test_enum_2_comb_18_fused_pim_op_1858\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t32\n\t0\n\t0\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1858_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 16 0 0 16 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1790_dsl ; test_enum_2_comb_29_fused_pim_op_1790\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1790_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1790_dsl ; test_enum_2_comb_29_fused_pim_op_1790\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1790_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_126_dsl ; test_enum_2_comb_25_fused_pim_op_126\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t-1\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_126_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0 -1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1464_dsl ; test_enum_2_comb_29_fused_pim_op_1464\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1464_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_341_dsl ; test_enum_2_comb_26_fused_pim_op_341\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_341_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_422_dsl ; test_enum_2_comb_29_fused_pim_op_422\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_422_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1486_dsl ; test_enum_2_comb_20_fused_pim_op_1486\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1486_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1486_dsl ; test_enum_2_comb_20_fused_pim_op_1486\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1486_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-le_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1486_dsl ; test_enum_2_comb_20_fused_pim_op_1486\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1486_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-ge_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_597_dsl ; test_enum_2_comb_27_fused_pim_op_597\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_597_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_320_dsl ; test_enum_2_comb_18_fused_pim_op_320\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_320_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_1522_dsl ; test_enum_2_comb_16_fused_pim_op_1522\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_1522_dsl (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 16 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_342_dsl ; test_enum_2_comb_22_fused_pim_op_342\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_342_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_24_fused_pim_op_803_dsl ; test_enum_2_comb_24_fused_pim_op_803\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t1\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_24_fused_pim_op_803_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_24_fused_pim_op_803_dsl ; test_enum_2_comb_24_fused_pim_op_803\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t1\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_24_fused_pim_op_803_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_2362_dsl ; test_enum_2_comb_31_fused_pim_op_2362\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_2362_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1655_dsl ; test_enum_2_comb_25_fused_pim_op_1655\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1655_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1655_dsl ; test_enum_2_comb_25_fused_pim_op_1655\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1655_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_1636_dsl ; test_enum_2_comb_26_fused_pim_op_1636\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_1636_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_612_dsl ; test_enum_2_comb_22_fused_pim_op_612\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_612_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_612_dsl ; test_enum_2_comb_22_fused_pim_op_612\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_612_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1851_dsl ; test_enum_2_comb_21_fused_pim_op_1851\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1851_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_1874_dsl ; test_enum_2_comb_27_fused_pim_op_1874\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_1874_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_1874_dsl ; test_enum_2_comb_27_fused_pim_op_1874\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_1874_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_307_dsl ; test_enum_2_comb_23_fused_pim_op_307\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_307_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1207_dsl ; test_enum_2_comb_25_fused_pim_op_1207\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1207_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_452_dsl ; test_enum_2_comb_19_fused_pim_op_452\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_452_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_239_dsl ; test_enum_2_comb_22_fused_pim_op_239\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_239_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_187_dsl ; test_enum_2_comb_23_fused_pim_op_187\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_187_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1144_dsl ; test_enum_2_comb_17_fused_pim_op_1144\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t0\n\t64\n\t8\n\t1\n\t0\n\t0\n\t0\n )_ (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1144_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0 512 16 1 0 0 0)",
                "dst": "(typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 16 32)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_2591_dsl ; test_enum_2_comb_25_fused_pim_op_2591\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_2591_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #b0 1)) 512 512 0 512 8 16 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 16 1024 8)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_2234_dsl ; test_enum_2_comb_30_fused_pim_op_2234\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t32\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_2234_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 16 0 -1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_519_dsl ; test_enum_2_comb_16_fused_pim_op_519\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_519_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_519_dsl ; test_enum_2_comb_16_fused_pim_op_519\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_519_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_199_dsl ; test_enum_2_comb_23_fused_pim_op_199\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t-1\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_199_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 -1 0 32 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_957_dsl ; test_enum_2_comb_25_fused_pim_op_957\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t16\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_957_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 16 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 16 1024 8)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1877_dsl ; test_enum_2_comb_21_fused_pim_op_1877\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1877_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_188_dsl ; test_enum_2_comb_17_fused_pim_op_188\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_188_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1243_dsl ; test_enum_2_comb_18_fused_pim_op_1243\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1243_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_409_dsl ; test_enum_2_comb_19_fused_pim_op_409\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_409_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_898_dsl ; test_enum_2_comb_22_fused_pim_op_898\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_898_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_8_fused_pim_op_1_dsl ; test_enum_2_comb_8_fused_pim_op_1\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_8_fused_pim_op_1_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 8 8 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_8_fused_pim_op_1_dsl ; test_enum_2_comb_8_fused_pim_op_1\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_8_fused_pim_op_1_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 8 8 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_1150_dsl ; test_enum_2_comb_22_fused_pim_op_1150\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_1150_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1110_dsl ; test_enum_2_comb_29_fused_pim_op_1110\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1110_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_304_dsl ; test_enum_2_comb_19_fused_pim_op_304\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_304_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_417_dsl ; test_enum_2_comb_21_fused_pim_op_417\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_417_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 -1 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_453_dsl ; test_enum_2_comb_29_fused_pim_op_453\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_453_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1287_dsl ; test_enum_2_comb_25_fused_pim_op_1287\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1287_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1287_dsl ; test_enum_2_comb_25_fused_pim_op_1287\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1287_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_7_fused_pim_op_13_dsl ; test_enum_2_comb_7_fused_pim_op_13\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_7_fused_pim_op_13_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_779_dsl ; test_enum_2_comb_27_fused_pim_op_779\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t1\n\t64\n\t1\n\t1\n\t1\n\t64\n\t1\n\t64\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_779_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 64 1 1 1 64 1 64 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1834_dsl ; test_enum_2_comb_29_fused_pim_op_1834\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1834_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1237_dsl ; test_enum_2_comb_20_fused_pim_op_1237\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1237_dsl (lit (bv #b0 1)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 16 0 16 0)",
                "dst": "(typed-folded:vec-ge_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1237_dsl ; test_enum_2_comb_20_fused_pim_op_1237\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1237_dsl (lit (bv #b0 1)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 16 0 16 0)",
                "dst": "(typed-folded:vec-le_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1237_dsl ; test_enum_2_comb_20_fused_pim_op_1237\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1237_dsl (lit (bv #b0 1)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 16 0 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_2603_dsl ; test_enum_2_comb_26_fused_pim_op_2603\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_2603_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_184_dsl ; test_enum_2_comb_23_fused_pim_op_184\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n\t64\n\t0\n\t64\n\t-1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_184_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0 0 16 0 16 -1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_792_dsl ; test_enum_2_comb_18_fused_pim_op_792\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_792_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1297_dsl ; test_enum_2_comb_19_fused_pim_op_1297\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1297_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_1336_dsl ; test_enum_2_comb_31_fused_pim_op_1336\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t1\n\t64\n\t1\n\t64\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_1336_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 1 16 1 16 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_742_dsl ; test_enum_2_comb_19_fused_pim_op_742\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_742_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_1133_dsl ; test_enum_2_comb_22_fused_pim_op_1133\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_1133_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1533_dsl ; test_enum_2_comb_25_fused_pim_op_1533\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1533_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 64 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 64 1024 32)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_524_dsl ; test_enum_2_comb_30_fused_pim_op_524\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t-1\n\t0\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_524_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0 16 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_1822_dsl ; test_enum_2_comb_30_fused_pim_op_1822\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_1822_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_1822_dsl ; test_enum_2_comb_30_fused_pim_op_1822\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_1822_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_470_dsl ; test_enum_2_comb_19_fused_pim_op_470\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_470_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1319_dsl ; test_enum_2_comb_29_fused_pim_op_1319\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1319_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_2356_dsl ; test_enum_2_comb_27_fused_pim_op_2356\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2356_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 16 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_402_dsl ; test_enum_2_comb_23_fused_pim_op_402\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_402_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 -1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_257_dsl ; test_enum_2_comb_26_fused_pim_op_257\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_257_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1079_dsl ; test_enum_2_comb_17_fused_pim_op_1079\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1079_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1079_dsl ; test_enum_2_comb_17_fused_pim_op_1079\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1079_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_561_dsl ; test_enum_2_comb_23_fused_pim_op_561\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_561_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_617_dsl ; test_enum_2_comb_25_fused_pim_op_617\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_617_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1015_dsl ; test_enum_2_comb_20_fused_pim_op_1015\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t8\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1015_dsl (reg (bv #x00 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) 128 128 0 128 1 16 0 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1015_dsl ; test_enum_2_comb_20_fused_pim_op_1015\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t8\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1015_dsl (reg (bv #x00 8)) (lit (bv #b0 1)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) 128 128 0 128 1 16 0 16 0)",
                "dst": "(typed-folded:vec-le_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1015_dsl ; test_enum_2_comb_20_fused_pim_op_1015\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t8\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1015_dsl (reg (bv #x01 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) 128 128 0 128 1 16 0 16 0)",
                "dst": "(typed-folded:vec-ge_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_1373_dsl ; test_enum_2_comb_30_fused_pim_op_1373\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_1373_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1463_dsl ; test_enum_2_comb_25_fused_pim_op_1463\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1463_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1463_dsl ; test_enum_2_comb_25_fused_pim_op_1463\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1463_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_577_dsl ; test_enum_2_comb_30_fused_pim_op_577\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_577_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_358_dsl ; test_enum_2_comb_25_fused_pim_op_358\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_358_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_599_dsl ; test_enum_2_comb_31_fused_pim_op_599\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_599_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1946_dsl ; test_enum_2_comb_18_fused_pim_op_1946\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1946_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_267_dsl ; test_enum_2_comb_20_fused_pim_op_267\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_267_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_267_dsl ; test_enum_2_comb_20_fused_pim_op_267\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_267_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2292_dsl ; test_enum_2_comb_22_fused_pim_op_2292\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2292_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_188_dsl ; test_enum_2_comb_31_fused_pim_op_188\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_188_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1028_dsl ; test_enum_2_comb_18_fused_pim_op_1028\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1028_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_778_dsl ; test_enum_2_comb_19_fused_pim_op_778\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_778_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1880_dsl ; test_enum_2_comb_25_fused_pim_op_1880\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1880_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1880_dsl ; test_enum_2_comb_25_fused_pim_op_1880\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1880_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1504_dsl ; test_enum_2_comb_28_fused_pim_op_1504\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1504_dsl (lit (bv #b0 1)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 16 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_2260_dsl ; test_enum_2_comb_31_fused_pim_op_2260\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_2260_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_24_fused_pim_op_1521_dsl ; test_enum_2_comb_24_fused_pim_op_1521\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_24_fused_pim_op_1521_dsl (lit (bv #b1 1)) (reg (bv #x01 8)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 1 16 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1056_dsl ; test_enum_2_comb_28_fused_pim_op_1056\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1056_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 0 16 16 0)",
                "dst": "(typed-folded:vec-le_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1056_dsl ; test_enum_2_comb_28_fused_pim_op_1056\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1056_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 0 16 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1056_dsl ; test_enum_2_comb_28_fused_pim_op_1056\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1056_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 0 16 16 0)",
                "dst": "(typed-folded:vec-ge_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_1641_dsl ; test_enum_2_comb_31_fused_pim_op_1641\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_1641_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_1236_dsl ; test_enum_2_comb_16_fused_pim_op_1236\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_1236_dsl (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 16 0 16 0)",
                "dst": "(typed-folded:vec-le_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_1236_dsl ; test_enum_2_comb_16_fused_pim_op_1236\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_1236_dsl (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 1 16 0 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_1236_dsl ; test_enum_2_comb_16_fused_pim_op_1236\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_1236_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 16 0 16 0)",
                "dst": "(typed-folded:vec-ge_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_2146_dsl ; test_enum_2_comb_18_fused_pim_op_2146\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_2146_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_24_fused_pim_op_1299_dsl ; test_enum_2_comb_24_fused_pim_op_1299\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t1\n\t-1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_24_fused_pim_op_1299_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 -1 16 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_500_dsl ; test_enum_2_comb_20_fused_pim_op_500\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_500_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_500_dsl ; test_enum_2_comb_20_fused_pim_op_500\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_500_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_24_fused_pim_op_588_dsl ; test_enum_2_comb_24_fused_pim_op_588\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_24_fused_pim_op_588_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_24_fused_pim_op_588_dsl ; test_enum_2_comb_24_fused_pim_op_588\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_24_fused_pim_op_588_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_2121_dsl ; test_enum_2_comb_26_fused_pim_op_2121\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_2121_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_2121_dsl ; test_enum_2_comb_26_fused_pim_op_2121\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_2121_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_2185_dsl ; test_enum_2_comb_19_fused_pim_op_2185\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_2185_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_2185_dsl ; test_enum_2_comb_19_fused_pim_op_2185\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_2185_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_916_dsl ; test_enum_2_comb_29_fused_pim_op_916\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_916_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1587_dsl ; test_enum_2_comb_29_fused_pim_op_1587\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1587_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2104_dsl ; test_enum_2_comb_22_fused_pim_op_2104\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2104_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1958_dsl ; test_enum_2_comb_19_fused_pim_op_1958\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1958_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_13_dsl ; test_enum_2_comb_27_fused_pim_op_13\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t32\n\t0\n\t2\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_13_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 256 256 0 256 8 16 1 2 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 256 16 1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_229_dsl ; test_enum_2_comb_29_fused_pim_op_229\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_229_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0 16 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_309_dsl ; test_enum_2_comb_30_fused_pim_op_309\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_309_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_309_dsl ; test_enum_2_comb_30_fused_pim_op_309\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_309_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_2091_dsl ; test_enum_2_comb_27_fused_pim_op_2091\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2091_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_2091_dsl ; test_enum_2_comb_27_fused_pim_op_2091\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2091_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1700_dsl ; test_enum_2_comb_21_fused_pim_op_1700\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1700_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1700_dsl ; test_enum_2_comb_21_fused_pim_op_1700\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1700_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1043_dsl ; test_enum_2_comb_28_fused_pim_op_1043\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1043_dsl (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 1 16 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1598_dsl ; test_enum_2_comb_17_fused_pim_op_1598\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1598_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1598_dsl ; test_enum_2_comb_17_fused_pim_op_1598\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1598_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_1390_dsl ; test_enum_2_comb_22_fused_pim_op_1390\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_1390_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_1368_dsl ; test_enum_2_comb_26_fused_pim_op_1368\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_1368_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_1166_dsl ; test_enum_2_comb_26_fused_pim_op_1166\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_1166_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1849_dsl ; test_enum_2_comb_25_fused_pim_op_1849\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1849_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_1113_dsl ; test_enum_2_comb_22_fused_pim_op_1113\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_1113_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1898_dsl ; test_enum_2_comb_18_fused_pim_op_1898\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1898_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1898_dsl ; test_enum_2_comb_18_fused_pim_op_1898\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1898_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1659_dsl ; test_enum_2_comb_29_fused_pim_op_1659\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1659_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_900_dsl ; test_enum_2_comb_31_fused_pim_op_900\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_900_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_15_fused_pim_op_16_dsl ; test_enum_2_comb_15_fused_pim_op_16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_15_fused_pim_op_16_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) 512 512 0 512 32 1 32 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 32 512)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1768_dsl ; test_enum_2_comb_21_fused_pim_op_1768\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1768_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_7_fused_pim_op_11_dsl ; test_enum_2_comb_7_fused_pim_op_11\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_7_fused_pim_op_11_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_292_dsl ; test_enum_2_comb_16_fused_pim_op_292\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t1\n\t16\n\t8\n\t0\n\t16\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_292_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 1 16 8 1 16 8 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_292_dsl ; test_enum_2_comb_16_fused_pim_op_292\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t1\n\t16\n\t8\n\t0\n\t16\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_292_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 0 0 16 8 0 16 8 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_1_fused_pim_op_0_dsl ; test_enum_2_comb_1_fused_pim_op_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_1_fused_pim_op_0_dsl (reg (bv #x00 8)) 32 32 0 512 32 0 0)",
                "dst": "(typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 32 16)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_789_dsl ; test_enum_2_comb_18_fused_pim_op_789\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_789_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1642_dsl ; test_enum_2_comb_29_fused_pim_op_1642\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1642_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_833_dsl ; test_enum_2_comb_27_fused_pim_op_833\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_833_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1785_dsl ; test_enum_2_comb_25_fused_pim_op_1785\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1785_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0 16 0 16 -1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_11_dsl ; test_enum_2_comb_21_fused_pim_op_11\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_11_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 64 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 64 1024 32)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_2308_dsl ; test_enum_2_comb_27_fused_pim_op_2308\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2308_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_457_dsl ; test_enum_2_comb_23_fused_pim_op_457\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_457_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0 -1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_271_dsl ; test_enum_2_comb_18_fused_pim_op_271\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_271_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_271_dsl ; test_enum_2_comb_18_fused_pim_op_271\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_271_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_1820_dsl ; test_enum_2_comb_26_fused_pim_op_1820\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_1820_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1234_dsl ; test_enum_2_comb_19_fused_pim_op_1234\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1234_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2637_dsl ; test_enum_2_comb_22_fused_pim_op_2637\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2637_dsl (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_24_fused_pim_op_1119_dsl ; test_enum_2_comb_24_fused_pim_op_1119\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t256\n\t256\n\t0\n\t256\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_24_fused_pim_op_1119_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) 64 64 0 64 1 8 8 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_26_dsl ; test_enum_2_comb_21_fused_pim_op_26\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_26_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_706_dsl ; test_enum_2_comb_19_fused_pim_op_706\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t64\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_706_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 16 1 16 1 16 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_1_fused_pim_op_12_dsl ; test_enum_2_comb_1_fused_pim_op_12\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_1_fused_pim_op_12_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_506_dsl ; test_enum_2_comb_22_fused_pim_op_506\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_506_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1932_dsl ; test_enum_2_comb_18_fused_pim_op_1932\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1932_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1932_dsl ; test_enum_2_comb_18_fused_pim_op_1932\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1932_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1040_dsl ; test_enum_2_comb_28_fused_pim_op_1040\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1040_dsl (reg (bv #x01 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 1 0 16 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1040_dsl ; test_enum_2_comb_28_fused_pim_op_1040\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1040_dsl (reg (bv #x01 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 1 0 16 16 0)",
                "dst": "(typed-folded:vec-ge_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1040_dsl ; test_enum_2_comb_28_fused_pim_op_1040\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1040_dsl (reg (bv #x00 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 0 16 16 0)",
                "dst": "(typed-folded:vec-le_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1221_dsl ; test_enum_2_comb_28_fused_pim_op_1221\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t16\n\t0\n\t0\n\t32\n\t0\n\t32\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1221_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 16 0 0 32 0 32 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1221_dsl ; test_enum_2_comb_28_fused_pim_op_1221\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t16\n\t0\n\t0\n\t32\n\t0\n\t32\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1221_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 16 0 0 32 0 32 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_2164_dsl ; test_enum_2_comb_18_fused_pim_op_2164\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_2164_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_1151_dsl ; test_enum_2_comb_27_fused_pim_op_1151\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_1151_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_224_dsl ; test_enum_2_comb_21_fused_pim_op_224\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_224_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_1540_dsl ; test_enum_2_comb_16_fused_pim_op_1540\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_1540_dsl (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 16 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_780_dsl ; test_enum_2_comb_26_fused_pim_op_780\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_780_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 1 32 1 32 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1253_dsl ; test_enum_2_comb_20_fused_pim_op_1253\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1253_dsl (reg (bv #x01 8)) (lit (bv #b0 1)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 16 0 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1253_dsl ; test_enum_2_comb_20_fused_pim_op_1253\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1253_dsl (reg (bv #x00 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 16 0 16 0)",
                "dst": "(typed-folded:vec-le_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1253_dsl ; test_enum_2_comb_20_fused_pim_op_1253\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1253_dsl (reg (bv #x00 8)) (lit (bv #b0 1)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 16 0 16 0)",
                "dst": "(typed-folded:vec-ge_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1463_dsl ; test_enum_2_comb_23_fused_pim_op_1463\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1463_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1463_dsl ; test_enum_2_comb_23_fused_pim_op_1463\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1463_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_2002_dsl ; test_enum_2_comb_31_fused_pim_op_2002\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_2002_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_55_dsl ; test_enum_2_comb_26_fused_pim_op_55\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_55_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_308_dsl ; test_enum_2_comb_30_fused_pim_op_308\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_308_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_538_dsl ; test_enum_2_comb_20_fused_pim_op_538\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_538_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_538_dsl ; test_enum_2_comb_20_fused_pim_op_538\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_538_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_253_dsl ; test_enum_2_comb_18_fused_pim_op_253\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_253_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2001_dsl ; test_enum_2_comb_22_fused_pim_op_2001\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t0\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2001_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0 64 0 64 -1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_6_fused_pim_op_12_dsl ; test_enum_2_comb_6_fused_pim_op_12\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_6_fused_pim_op_12_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1657_dsl ; test_enum_2_comb_25_fused_pim_op_1657\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1657_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2306_dsl ; test_enum_2_comb_22_fused_pim_op_2306\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2306_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1833_dsl ; test_enum_2_comb_21_fused_pim_op_1833\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1833_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_839_dsl ; test_enum_2_comb_16_fused_pim_op_839\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_839_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_839_dsl ; test_enum_2_comb_16_fused_pim_op_839\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_839_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_343_dsl ; test_enum_2_comb_27_fused_pim_op_343\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_343_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_884_dsl ; test_enum_2_comb_25_fused_pim_op_884\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_884_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_3106_dsl ; test_enum_2_comb_27_fused_pim_op_3106\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_3106_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_842_dsl ; test_enum_2_comb_20_fused_pim_op_842\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_842_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_842_dsl ; test_enum_2_comb_20_fused_pim_op_842\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_842_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_1982_dsl ; test_enum_2_comb_30_fused_pim_op_1982\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_1982_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_224_dsl ; test_enum_2_comb_19_fused_pim_op_224\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_224_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_220_dsl ; test_enum_2_comb_18_fused_pim_op_220\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_220_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0 0 16 0 16 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1858_dsl ; test_enum_2_comb_25_fused_pim_op_1858\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1858_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1301_dsl ; test_enum_2_comb_25_fused_pim_op_1301\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1301_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1068_dsl ; test_enum_2_comb_25_fused_pim_op_1068\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1068_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_41_dsl ; test_enum_2_comb_19_fused_pim_op_41\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_41_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 16 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 16 1024 8)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_2182_dsl ; test_enum_2_comb_23_fused_pim_op_2182\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_2182_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_2182_dsl ; test_enum_2_comb_23_fused_pim_op_2182\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_2182_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_1406_dsl ; test_enum_2_comb_27_fused_pim_op_1406\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_1406_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_1406_dsl ; test_enum_2_comb_27_fused_pim_op_1406\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_1406_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1787_dsl ; test_enum_2_comb_21_fused_pim_op_1787\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1787_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 -1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_1180_dsl ; test_enum_2_comb_16_fused_pim_op_1180\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t-1\n\t16\n\t-1\n\t16\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_1180_dsl (reg (bv #x01 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 -1 16 -1 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_278_dsl ; test_enum_2_comb_31_fused_pim_op_278\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_278_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_2063_dsl ; test_enum_2_comb_18_fused_pim_op_2063\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_2063_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_2047_dsl ; test_enum_2_comb_18_fused_pim_op_2047\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_2047_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_2075_dsl ; test_enum_2_comb_27_fused_pim_op_2075\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2075_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_2075_dsl ; test_enum_2_comb_27_fused_pim_op_2075\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2075_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_3_fused_pim_op_2_dsl ; test_enum_2_comb_3_fused_pim_op_2\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t1\n\t2\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_3_fused_pim_op_2_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 2 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 256 16 1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1286_dsl ; test_enum_2_comb_21_fused_pim_op_1286\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1286_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_236_dsl ; test_enum_2_comb_30_fused_pim_op_236\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t-1\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_236_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 -1 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_490_dsl ; test_enum_2_comb_31_fused_pim_op_490\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_490_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1303_dsl ; test_enum_2_comb_17_fused_pim_op_1303\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1303_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1303_dsl ; test_enum_2_comb_17_fused_pim_op_1303\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1303_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_774_dsl ; test_enum_2_comb_23_fused_pim_op_774\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t64\n\t1\n\t64\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_774_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 1 32 1 32 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_9_fused_pim_op_6_dsl ; test_enum_2_comb_9_fused_pim_op_6\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_9_fused_pim_op_6_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1247_dsl ; test_enum_2_comb_19_fused_pim_op_1247\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1247_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_15_fused_pim_op_4_dsl ; test_enum_2_comb_15_fused_pim_op_4\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_15_fused_pim_op_4_dsl (reg (bv #x00 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1890_dsl ; test_enum_2_comb_17_fused_pim_op_1890\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1890_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0 16 0 16 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_535_dsl ; test_enum_2_comb_22_fused_pim_op_535\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t-1\n\t0\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_535_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 -1 0 0 64 0 64 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_542_dsl ; test_enum_2_comb_18_fused_pim_op_542\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_542_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_122_dsl ; test_enum_2_comb_25_fused_pim_op_122\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t-1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_122_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_1078_dsl ; test_enum_2_comb_31_fused_pim_op_1078\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t64\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_1078_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 1 1 32 1 32 1 32 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1896_dsl ; test_enum_2_comb_18_fused_pim_op_1896\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1896_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1896_dsl ; test_enum_2_comb_18_fused_pim_op_1896\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1896_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_2393_dsl ; test_enum_2_comb_31_fused_pim_op_2393\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_2393_dsl (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1779_dsl ; test_enum_2_comb_21_fused_pim_op_1779\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1779_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1281_dsl ; test_enum_2_comb_23_fused_pim_op_1281\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1281_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1828_dsl ; test_enum_2_comb_17_fused_pim_op_1828\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1828_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_821_dsl ; test_enum_2_comb_28_fused_pim_op_821\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_821_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_821_dsl ; test_enum_2_comb_28_fused_pim_op_821\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_821_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1931_dsl ; test_enum_2_comb_18_fused_pim_op_1931\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1931_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_797_dsl ; test_enum_2_comb_22_fused_pim_op_797\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_797_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1223_dsl ; test_enum_2_comb_17_fused_pim_op_1223\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t16\n\t1\n\t1\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1223_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 1 64 1 1 64 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_1030_dsl ; test_enum_2_comb_16_fused_pim_op_1030\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_1030_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 16 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1590_dsl ; test_enum_2_comb_17_fused_pim_op_1590\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1590_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1273_dsl ; test_enum_2_comb_21_fused_pim_op_1273\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1273_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1290_dsl ; test_enum_2_comb_29_fused_pim_op_1290\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1290_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1315_dsl ; test_enum_2_comb_18_fused_pim_op_1315\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1315_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1786_dsl ; test_enum_2_comb_17_fused_pim_op_1786\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1786_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 -1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1651_dsl ; test_enum_2_comb_29_fused_pim_op_1651\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1651_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1468_dsl ; test_enum_2_comb_23_fused_pim_op_1468\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1468_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1682_dsl ; test_enum_2_comb_19_fused_pim_op_1682\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1682_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_6_fused_pim_op_9_dsl ; test_enum_2_comb_6_fused_pim_op_9\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_6_fused_pim_op_9_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 16 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1031_dsl ; test_enum_2_comb_17_fused_pim_op_1031\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t16\n\t1\n\t1\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1031_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 16 1 1 16 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_1855_dsl ; test_enum_2_comb_26_fused_pim_op_1855\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_1855_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_1214_dsl ; test_enum_2_comb_16_fused_pim_op_1214\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t-1\n\t16\n\t16\n\t0\n\t0\n\t32\n\t0\n\t32\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_1214_dsl (lit (bv #b0 1)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 -1 16 16 0 0 32 0 32 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_1214_dsl ; test_enum_2_comb_16_fused_pim_op_1214\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t-1\n\t16\n\t16\n\t0\n\t0\n\t32\n\t0\n\t32\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_1214_dsl (lit (bv #b0 1)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 1 -1 16 16 0 0 32 0 32 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_2354_dsl ; test_enum_2_comb_27_fused_pim_op_2354\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2354_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1639_dsl ; test_enum_2_comb_21_fused_pim_op_1639\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1639_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1639_dsl ; test_enum_2_comb_21_fused_pim_op_1639\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1639_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_3605_dsl ; test_enum_2_comb_27_fused_pim_op_3605\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_3605_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_2148_dsl ; test_enum_2_comb_23_fused_pim_op_2148\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_2148_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_1455_dsl ; test_enum_2_comb_26_fused_pim_op_1455\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t1\n\t2\n\t0\n\t1\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_1455_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 256 256 0 256 16 32 1 2 0 1 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 256 32 1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_3389_dsl ; test_enum_2_comb_31_fused_pim_op_3389\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t256\n\t256\n\t0\n\t256\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_3389_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) 256 256 0 256 8 16 2 1 1 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 256 16 1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_12_dsl ; test_enum_2_comb_27_fused_pim_op_12\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t32\n\t0\n\t2\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_12_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 256 256 0 256 8 16 1 2 1 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 256 16 1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1465_dsl ; test_enum_2_comb_17_fused_pim_op_1465\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1465_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1465_dsl ; test_enum_2_comb_17_fused_pim_op_1465\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1465_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_999_dsl ; test_enum_2_comb_17_fused_pim_op_999\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_999_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_2092_dsl ; test_enum_2_comb_27_fused_pim_op_2092\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2092_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_2092_dsl ; test_enum_2_comb_27_fused_pim_op_2092\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2092_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1669_dsl ; test_enum_2_comb_17_fused_pim_op_1669\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1669_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1669_dsl ; test_enum_2_comb_17_fused_pim_op_1669\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1669_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_168_dsl ; test_enum_2_comb_26_fused_pim_op_168\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t-1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_168_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_190_dsl ; test_enum_2_comb_25_fused_pim_op_190\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_190_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_1385_dsl ; test_enum_2_comb_22_fused_pim_op_1385\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_1385_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_178_dsl ; test_enum_2_comb_23_fused_pim_op_178\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_178_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 -1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_153_dsl ; test_enum_2_comb_25_fused_pim_op_153\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t-1\n\t-1\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_153_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 -1 0 0 64 0 64 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_1374_dsl ; test_enum_2_comb_27_fused_pim_op_1374\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_1374_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_1374_dsl ; test_enum_2_comb_27_fused_pim_op_1374\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_1374_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_1807_dsl ; test_enum_2_comb_22_fused_pim_op_1807\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_1807_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1716_dsl ; test_enum_2_comb_18_fused_pim_op_1716\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1716_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2730_dsl ; test_enum_2_comb_22_fused_pim_op_2730\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t2\n\t0\n\t1\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2730_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) 256 256 0 256 8 16 2 1 1 0 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 256 16 1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_2589_dsl ; test_enum_2_comb_27_fused_pim_op_2589\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t1\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2589_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x02 8)) 512 512 0 512 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_1841_dsl ; test_enum_2_comb_26_fused_pim_op_1841\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_1841_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1080_dsl ; test_enum_2_comb_25_fused_pim_op_1080\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1080_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1096_dsl ; test_enum_2_comb_17_fused_pim_op_1096\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1096_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1110_dsl ; test_enum_2_comb_19_fused_pim_op_1110\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t0\n\t2\n\t0\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1110_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 256 256 0 256 16 32 1 2 1 0 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 256 32 0)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_360_dsl ; test_enum_2_comb_21_fused_pim_op_360\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_360_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_562_dsl ; test_enum_2_comb_22_fused_pim_op_562\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_562_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_1783_dsl ; test_enum_2_comb_22_fused_pim_op_1783\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t32\n\t0\n\t0\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_1783_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 16 0 0 16 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1865_dsl ; test_enum_2_comb_17_fused_pim_op_1865\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1865_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1865_dsl ; test_enum_2_comb_17_fused_pim_op_1865\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1865_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1396_dsl ; test_enum_2_comb_20_fused_pim_op_1396\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t-1\n\t32\n\t-1\n\t32\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1396_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 -1 16 -1 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 -1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_1856_dsl ; test_enum_2_comb_27_fused_pim_op_1856\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_1856_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_1151_dsl ; test_enum_2_comb_30_fused_pim_op_1151\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_1151_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1866_dsl ; test_enum_2_comb_17_fused_pim_op_1866\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1866_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_442_dsl ; test_enum_2_comb_21_fused_pim_op_442\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_442_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_2003_dsl ; test_enum_2_comb_31_fused_pim_op_2003\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t64\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_2003_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 32 0 -1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_706_dsl ; test_enum_2_comb_17_fused_pim_op_706\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_706_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_438_dsl ; test_enum_2_comb_21_fused_pim_op_438\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_438_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_274_dsl ; test_enum_2_comb_30_fused_pim_op_274\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_274_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1864_dsl ; test_enum_2_comb_18_fused_pim_op_1864\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1864_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 32 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_145_dsl ; test_enum_2_comb_29_fused_pim_op_145\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_145_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0 16 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_272_dsl ; test_enum_2_comb_18_fused_pim_op_272\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_272_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1494_dsl ; test_enum_2_comb_29_fused_pim_op_1494\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1494_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1596_dsl ; test_enum_2_comb_17_fused_pim_op_1596\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1596_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_297_dsl ; test_enum_2_comb_31_fused_pim_op_297\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_297_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_800_dsl ; test_enum_2_comb_22_fused_pim_op_800\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_800_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_759_dsl ; test_enum_2_comb_23_fused_pim_op_759\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_759_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1703_dsl ; test_enum_2_comb_21_fused_pim_op_1703\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1703_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1850_dsl ; test_enum_2_comb_21_fused_pim_op_1850\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1850_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1850_dsl ; test_enum_2_comb_21_fused_pim_op_1850\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1850_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_1405_dsl ; test_enum_2_comb_30_fused_pim_op_1405\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_1405_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_1405_dsl ; test_enum_2_comb_30_fused_pim_op_1405\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_1405_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1383_dsl ; test_enum_2_comb_17_fused_pim_op_1383\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1383_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_469_dsl ; test_enum_2_comb_16_fused_pim_op_469\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_469_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_469_dsl ; test_enum_2_comb_16_fused_pim_op_469\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_469_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1695_dsl ; test_enum_2_comb_29_fused_pim_op_1695\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1695_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_589_dsl ; test_enum_2_comb_19_fused_pim_op_589\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_589_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_589_dsl ; test_enum_2_comb_19_fused_pim_op_589\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_589_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_2041_dsl ; test_enum_2_comb_30_fused_pim_op_2041\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_2041_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_2_fused_pim_op_15_dsl ; test_enum_2_comb_2_fused_pim_op_15\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_2_fused_pim_op_15_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_24_fused_pim_op_1416_dsl ; test_enum_2_comb_24_fused_pim_op_1416\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t1\n\t32\n\t0\n\t0\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_24_fused_pim_op_1416_dsl (reg (bv #x01 8)) (lit (bv #b0 1)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 16 0 0 32 0 32 16 -1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_24_fused_pim_op_1416_dsl ; test_enum_2_comb_24_fused_pim_op_1416\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t1\n\t32\n\t0\n\t0\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_24_fused_pim_op_1416_dsl (reg (bv #x00 8)) (lit (bv #b0 1)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 16 0 0 32 0 32 16 -1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_236_dsl ; test_enum_2_comb_18_fused_pim_op_236\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_236_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_502_dsl ; test_enum_2_comb_16_fused_pim_op_502\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_502_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_502_dsl ; test_enum_2_comb_16_fused_pim_op_502\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_502_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1496_dsl ; test_enum_2_comb_29_fused_pim_op_1496\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1496_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_1684_dsl ; test_enum_2_comb_22_fused_pim_op_1684\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_1684_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 256 256 0 256 16 32 2 0 1 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 256 32 0)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_1813_dsl ; test_enum_2_comb_29_fused_pim_op_1813\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t-1\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_1813_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0 0 64 0 64 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_287_dsl ; test_enum_2_comb_23_fused_pim_op_287\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_287_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2119_dsl ; test_enum_2_comb_22_fused_pim_op_2119\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2119_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1081_dsl ; test_enum_2_comb_23_fused_pim_op_1081\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1081_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_607_dsl ; test_enum_2_comb_21_fused_pim_op_607\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_607_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1967_dsl ; test_enum_2_comb_23_fused_pim_op_1967\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1967_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1967_dsl ; test_enum_2_comb_23_fused_pim_op_1967\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1967_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1285_dsl ; test_enum_2_comb_17_fused_pim_op_1285\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1285_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1285_dsl ; test_enum_2_comb_17_fused_pim_op_1285\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1285_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_888_dsl ; test_enum_2_comb_25_fused_pim_op_888\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_888_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_2275_dsl ; test_enum_2_comb_30_fused_pim_op_2275\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_2275_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_763_dsl ; test_enum_2_comb_19_fused_pim_op_763\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_763_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_536_dsl ; test_enum_2_comb_20_fused_pim_op_536\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_536_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_536_dsl ; test_enum_2_comb_20_fused_pim_op_536\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_536_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_572_dsl ; test_enum_2_comb_18_fused_pim_op_572\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_572_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_183_dsl ; test_enum_2_comb_17_fused_pim_op_183\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_183_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 -1 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_904_dsl ; test_enum_2_comb_29_fused_pim_op_904\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_904_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1047_dsl ; test_enum_2_comb_19_fused_pim_op_1047\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1047_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_1989_dsl ; test_enum_2_comb_22_fused_pim_op_1989\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_1989_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1717_dsl ; test_enum_2_comb_19_fused_pim_op_1717\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1717_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_575_dsl ; test_enum_2_comb_18_fused_pim_op_575\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_575_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_595_dsl ; test_enum_2_comb_31_fused_pim_op_595\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_595_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1507_dsl ; test_enum_2_comb_20_fused_pim_op_1507\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1507_dsl (lit (bv #b0 1)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 16 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2101_dsl ; test_enum_2_comb_22_fused_pim_op_2101\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2101_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_563_dsl ; test_enum_2_comb_23_fused_pim_op_563\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_563_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_1824_dsl ; test_enum_2_comb_30_fused_pim_op_1824\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_1824_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_11_dsl ; test_enum_2_comb_23_fused_pim_op_11\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t32\n\t0\n\t2\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_11_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 256 256 0 256 8 16 0 2 0 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 256 16 0)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1485_dsl ; test_enum_2_comb_19_fused_pim_op_1485\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1485_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_420_dsl ; test_enum_2_comb_29_fused_pim_op_420\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_420_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_1463_dsl ; test_enum_2_comb_22_fused_pim_op_1463\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t32\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_1463_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 64 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 64 1024 32)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_809_dsl ; test_enum_2_comb_16_fused_pim_op_809\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_809_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_809_dsl ; test_enum_2_comb_16_fused_pim_op_809\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_809_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_50_dsl ; test_enum_2_comb_16_fused_pim_op_50\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_50_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 1 1 8 8 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_16_fused_pim_op_50_dsl ; test_enum_2_comb_16_fused_pim_op_50\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_16_fused_pim_op_50_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 8 8 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_872_dsl ; test_enum_2_comb_21_fused_pim_op_872\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_872_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_563_dsl ; test_enum_2_comb_27_fused_pim_op_563\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_563_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1055_dsl ; test_enum_2_comb_20_fused_pim_op_1055\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1055_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 0 16 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1055_dsl ; test_enum_2_comb_20_fused_pim_op_1055\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1055_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 0 16 16 0)",
                "dst": "(typed-folded:vec-le_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1055_dsl ; test_enum_2_comb_20_fused_pim_op_1055\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1055_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 16 16 0)",
                "dst": "(typed-folded:vec-ge_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_306_dsl ; test_enum_2_comb_31_fused_pim_op_306\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_306_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_2338_dsl ; test_enum_2_comb_31_fused_pim_op_2338\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_2338_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_620_dsl ; test_enum_2_comb_25_fused_pim_op_620\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_620_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_10_fused_pim_op_10_dsl ; test_enum_2_comb_10_fused_pim_op_10\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_10_fused_pim_op_10_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_217_dsl ; test_enum_2_comb_20_fused_pim_op_217\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_217_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_217_dsl ; test_enum_2_comb_20_fused_pim_op_217\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_217_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1820_dsl ; test_enum_2_comb_21_fused_pim_op_1820\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1820_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0 64 0 64 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2389_dsl ; test_enum_2_comb_22_fused_pim_op_2389\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2389_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_304_dsl ; test_enum_2_comb_30_fused_pim_op_304\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_304_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_304_dsl ; test_enum_2_comb_30_fused_pim_op_304\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_304_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1640_dsl ; test_enum_2_comb_25_fused_pim_op_1640\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1640_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1715_dsl ; test_enum_2_comb_19_fused_pim_op_1715\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1715_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_828_dsl ; test_enum_2_comb_23_fused_pim_op_828\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_828_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_635_dsl ; test_enum_2_comb_29_fused_pim_op_635\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_635_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_27_dsl ; test_enum_2_comb_22_fused_pim_op_27\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t1\n\t2\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_27_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 256 256 0 256 16 32 1 2 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 256 32 1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_829_dsl ; test_enum_2_comb_22_fused_pim_op_829\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_829_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_235_dsl ; test_enum_2_comb_29_fused_pim_op_235\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_235_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_2304_dsl ; test_enum_2_comb_22_fused_pim_op_2304\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_2304_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 32 0 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_1603_dsl ; test_enum_2_comb_26_fused_pim_op_1603\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_1603_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1257_dsl ; test_enum_2_comb_25_fused_pim_op_1257\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1257_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1257_dsl ; test_enum_2_comb_25_fused_pim_op_1257\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1257_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_2094_dsl ; test_enum_2_comb_21_fused_pim_op_2094\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_2094_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x02 8)) 512 512 0 512 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_2344_dsl ; test_enum_2_comb_27_fused_pim_op_2344\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_2344_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1888_dsl ; test_enum_2_comb_25_fused_pim_op_1888\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1888_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1888_dsl ; test_enum_2_comb_25_fused_pim_op_1888\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1888_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1798_dsl ; test_enum_2_comb_25_fused_pim_op_1798\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1798_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0 16 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_217_dsl ; test_enum_2_comb_17_fused_pim_op_217\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_217_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_614_dsl ; test_enum_2_comb_26_fused_pim_op_614\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_614_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_614_dsl ; test_enum_2_comb_26_fused_pim_op_614\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_614_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_276_dsl ; test_enum_2_comb_22_fused_pim_op_276\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_276_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_897_dsl ; test_enum_2_comb_21_fused_pim_op_897\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_897_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1450_dsl ; test_enum_2_comb_28_fused_pim_op_1450\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t32\n\t0\n\t0\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1450_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 16 0 0 32 0 32 16 0 0 32 0 32 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_1686_dsl ; test_enum_2_comb_21_fused_pim_op_1686\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_1686_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_26_fused_pim_op_3085_dsl ; test_enum_2_comb_26_fused_pim_op_3085\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t16\n\t32\n\t0\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_26_fused_pim_op_3085_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) 512 512 0 512 8 16 0 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 16 1024 8)"
            }
        }
    ],
    " (test_enum_2_comb_27_fused_pim_op_247_dsl ; test_enum_2_comb_27_fused_pim_op_247\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_27_fused_pim_op_247_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_3_fused_pim_op_7_dsl ; test_enum_2_comb_3_fused_pim_op_7\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_3_fused_pim_op_7_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_253_dsl ; test_enum_2_comb_19_fused_pim_op_253\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_253_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_664_dsl ; test_enum_2_comb_17_fused_pim_op_664\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_664_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_1510_dsl ; test_enum_2_comb_25_fused_pim_op_1510\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_1510_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_1586_dsl ; test_enum_2_comb_30_fused_pim_op_1586\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t16\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_1586_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 1 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_356_dsl ; test_enum_2_comb_21_fused_pim_op_356\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_356_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0 -1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_2146_dsl ; test_enum_2_comb_21_fused_pim_op_2146\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_2146_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_21_fused_pim_op_25_dsl ; test_enum_2_comb_21_fused_pim_op_25\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_21_fused_pim_op_25_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_183_dsl ; test_enum_2_comb_18_fused_pim_op_183\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_183_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0 -1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1825_dsl ; test_enum_2_comb_19_fused_pim_op_1825\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1825_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_1950_dsl ; test_enum_2_comb_18_fused_pim_op_1950\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_1950_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_24_fused_pim_op_806_dsl ; test_enum_2_comb_24_fused_pim_op_806\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_24_fused_pim_op_806_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_24_fused_pim_op_806_dsl ; test_enum_2_comb_24_fused_pim_op_806\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_24_fused_pim_op_806_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1485_dsl ; test_enum_2_comb_28_fused_pim_op_1485\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1485_dsl (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1485_dsl ; test_enum_2_comb_28_fused_pim_op_1485\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1485_dsl (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-le_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1485_dsl ; test_enum_2_comb_28_fused_pim_op_1485\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1485_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-ge_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_1873_dsl ; test_enum_2_comb_31_fused_pim_op_1873\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_1873_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_31_fused_pim_op_1873_dsl ; test_enum_2_comb_31_fused_pim_op_1873\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_31_fused_pim_op_1873_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1010_dsl ; test_enum_2_comb_28_fused_pim_op_1010\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t0\n\t8\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1010_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-le_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1010_dsl ; test_enum_2_comb_28_fused_pim_op_1010\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t0\n\t8\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1010_dsl (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_1010_dsl ; test_enum_2_comb_28_fused_pim_op_1010\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t0\n\t8\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_1010_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 0 64 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-ge_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 0)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1968_dsl ; test_enum_2_comb_23_fused_pim_op_1968\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1968_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 512 512 0 512 16 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_19_fused_pim_op_1662_dsl ; test_enum_2_comb_19_fused_pim_op_1662\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n\t64\n\t0\n\t0\n\t64\n\t0\n\t64\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_19_fused_pim_op_1662_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0 32 0 32 0 0 32 0 32 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 512 0)"
            }
        }
    ],
    " (test_enum_2_comb_29_fused_pim_op_219_dsl ; test_enum_2_comb_29_fused_pim_op_219\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_29_fused_pim_op_219_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_518_dsl ; test_enum_2_comb_28_fused_pim_op_518\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_518_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_28_fused_pim_op_518_dsl ; test_enum_2_comb_28_fused_pim_op_518\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t512\n\t512\n\t0\n\t512\n\t1\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_28_fused_pim_op_518_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024 1)"
            }
        }
    ],
    " (test_enum_2_comb_23_fused_pim_op_1746_dsl ; test_enum_2_comb_23_fused_pim_op_1746\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_23_fused_pim_op_1746_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 512 512 0 512 8 0 16 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 32 512 -1) (typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 8 16 512 1) 64 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_3198_dsl ; test_enum_2_comb_30_fused_pim_op_3198\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t0\n\t2\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_3198_dsl (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 256 256 0 256 8 16 0 2 8 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256 -1) (typed-folded:xBroadcast_dsl (reg (bv #x03 8)) 16 32) (reg (bv #x02 8)) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_3198_dsl ; test_enum_2_comb_30_fused_pim_op_3198\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t0\n\t2\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_3198_dsl (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 256 256 0 256 8 16 0 2 8 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256 -1) (typed-folded:xBroadcast_dsl (reg (bv #x03 8)) 16 32) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 512 1) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_3198_dsl ; test_enum_2_comb_30_fused_pim_op_3198\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t0\n\t2\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_3198_dsl (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 256 256 0 256 8 16 0 2 8 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256 -1) (typed-folded:xBroadcast_dsl (reg (bv #x03 8)) 16 32) (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 512 1) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_3198_dsl ; test_enum_2_comb_30_fused_pim_op_3198\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t0\n\t2\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_3198_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 256 256 0 256 8 16 0 2 8 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256 -1) (typed-folded:xBroadcast_dsl (reg (bv #x03 8)) 16 32) (typed-folded:vec-halving_add_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 16 512 1) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_3198_dsl ; test_enum_2_comb_30_fused_pim_op_3198\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t0\n\t2\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_3198_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 256 256 0 256 8 16 0 2 8 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256 -1) (typed-folded:xBroadcast_dsl (reg (bv #x03 8)) 16 32) (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 512 -1) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_3198_dsl ; test_enum_2_comb_30_fused_pim_op_3198\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t0\n\t2\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_3198_dsl (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 256 256 0 256 8 16 0 2 8 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256 -1) (typed-folded:xBroadcast_dsl (reg (bv #x03 8)) 16 32) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 512 -1) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_30_fused_pim_op_3198_dsl ; test_enum_2_comb_30_fused_pim_op_3198\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t0\n\t2\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_30_fused_pim_op_3198_dsl (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 256 256 0 256 8 16 0 2 8 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 256 -1) (typed-folded:xBroadcast_dsl (reg (bv #x03 8)) 16 32) (typed-folded:vec-if_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) (reg (bv #x02 8)) 32 512) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_18_fused_pim_op_176_dsl ; test_enum_2_comb_18_fused_pim_op_176\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-shr_dsl ; typed-folded:vec-shr_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_18_fused_pim_op_176_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16 0 512 16 -1 0 -1 0)",
                "dst": "(typed-folded:vec-shr_dsl (reg (bv #x00 8)) (typed-folded:xBroadcast_dsl (reg (bv #x01 8)) 16 32) 16 512 1)"
            }
        }
    ],
    " (test_enum_2_comb_17_fused_pim_op_1446_dsl ; test_enum_2_comb_17_fused_pim_op_1446\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_17_fused_pim_op_1446_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0 32 0 32 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (typed-folded:vec-div_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 512 0) (reg (bv #x00 8)) 8 512 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1001_dsl ; test_enum_2_comb_20_fused_pim_op_1001\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t8\n\t0\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1001_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) 128 128 0 128 1 16 0 0 16 0)",
                "dst": "(typed-folded:vec-eq_dsl (typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 16 128) (reg (bv #x01 8)) 16 2048 -1)"
            }
        }
    ],
    " (test_enum_2_comb_20_fused_pim_op_1001_dsl ; test_enum_2_comb_20_fused_pim_op_1001\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t8\n\t0\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_20_fused_pim_op_1001_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b0 1)) (reg (bv #x02 8)) 128 128 0 128 1 8 0 0 8 0)",
                "dst": "(typed-folded:vec-eq_dsl (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 8 1024 0) (typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 8 128) 8 1024 -1)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_2561_dsl ; test_enum_2_comb_25_fused_pim_op_2561\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t2\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_2561_dsl (lit (bv #b1 1)) (lit (bv #b1 1)) (reg (bv #x03 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 16 32 2 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 32 1024 -1) (reg (bv #x01 8)) (typed-folded:cast-truncate_dsl (reg (bv #x02 8)) 32 1024 16) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_2561_dsl ; test_enum_2_comb_25_fused_pim_op_2561\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t2\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_2561_dsl (lit (bv #b1 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x02 8)) 512 512 0 512 16 32 2 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 32 1024 -1) (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 1) (typed-folded:cast-truncate_dsl (reg (bv #x03 8)) 32 1024 16) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_2561_dsl ; test_enum_2_comb_25_fused_pim_op_2561\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t2\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_2561_dsl (lit (bv #b1 1)) (lit (bv #b1 1)) (reg (bv #x03 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 512 512 0 512 16 32 2 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 32 1024 -1) (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 1) (typed-folded:cast-truncate_dsl (reg (bv #x02 8)) 32 1024 16) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_2561_dsl ; test_enum_2_comb_25_fused_pim_op_2561\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t2\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_2561_dsl (lit (bv #b1 1)) (lit (bv #b1 1)) (reg (bv #x02 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 512 512 0 512 16 32 2 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 32 1024 -1) (typed-folded:vec-halving_add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 512 1) (typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 32 1024 16) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_2561_dsl ; test_enum_2_comb_25_fused_pim_op_2561\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t2\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_2561_dsl (lit (bv #b1 1)) (lit (bv #b1 1)) (reg (bv #x03 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 512 512 0 512 8 16 2 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 1024 -1) (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 -1) (typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 16 1024 8) 8 512)"
            }
        }
    ],
    " (test_enum_2_comb_25_fused_pim_op_2561_dsl ; test_enum_2_comb_25_fused_pim_op_2561\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t256\n\t256\n\t0\n\t256\n\t8\n\t16\n\t2\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_25_fused_pim_op_2561_dsl (lit (bv #b1 1)) (lit (bv #b1 1)) (reg (bv #x02 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 512 512 0 512 16 32 2 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 32 1024 -1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 512 -1) (typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 32 1024 16) 16 512)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_14_dsl ; test_enum_2_comb_22_fused_pim_op_14\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t8\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_14_dsl (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 32 0 2 1 16 0)",
                "dst": "(typed-folded:cast-extend_dsl (typed-folded:vec-if_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 16 256) 16 256 32 0)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_14_dsl ; test_enum_2_comb_22_fused_pim_op_14\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_14_dsl (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 32 0 2 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x01 8)) (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 256 32 0) (typed-folded:cast-extend_dsl (reg (bv #x02 8)) 16 256 32 0) 32 512)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_14_dsl ; test_enum_2_comb_22_fused_pim_op_14\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_14_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 16 32 1 2 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 8 16 -1) (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 256 32 1) (typed-folded:cast-extend_dsl (reg (bv #x02 8)) 16 256 32 1) 32 512)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_14_dsl ; test_enum_2_comb_22_fused_pim_op_14\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_14_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 16 32 1 2 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 1) (typed-folded:cast-extend_dsl (reg (bv #x02 8)) 16 256 32 1) (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 256 32 1) 32 512)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_14_dsl ; test_enum_2_comb_22_fused_pim_op_14\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_14_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 256 256 0 256 16 32 0 2 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 1) (typed-folded:cast-extend_dsl (reg (bv #x02 8)) 16 256 32 0) (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 256 32 0) 32 512)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_14_dsl ; test_enum_2_comb_22_fused_pim_op_14\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_14_dsl (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 32 0 2 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 16 1) (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 256 32 0) (typed-folded:cast-extend_dsl (reg (bv #x02 8)) 16 256 32 0) 32 512)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_14_dsl ; test_enum_2_comb_22_fused_pim_op_14\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_14_dsl (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 32 1 2 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 -1) (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 256 32 1) (typed-folded:cast-extend_dsl (reg (bv #x02 8)) 16 256 32 1) 32 512)"
            }
        }
    ],
    " (test_enum_2_comb_22_fused_pim_op_14_dsl ; test_enum_2_comb_22_fused_pim_op_14\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_bi_map_v2",
            "property": {
                "src": "(test_enum_2_comb_22_fused_pim_op_14_dsl (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 32 1 2 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 -1) (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 256 32 1) (typed-folded:cast-extend_dsl (reg (bv #x02 8)) 16 256 32 1) 32 512)"
            }
        }
    ]
}