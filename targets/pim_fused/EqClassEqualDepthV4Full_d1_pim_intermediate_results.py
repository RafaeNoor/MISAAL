{
    " (test_enum_1_comb_14_fused_pim_op_1388_dsl ; test_enum_1_comb_14_fused_pim_op_1388\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1388_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_41_dsl ; test_enum_1_comb_11_fused_pim_op_41\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_41_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 64 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 64 256 32)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1063_dsl ; test_enum_1_comb_11_fused_pim_op_1063\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1063_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2016_dsl ; test_enum_1_comb_14_fused_pim_op_2016\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2016_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0 64 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_1_fused_pim_op_11_dsl ; test_enum_1_comb_1_fused_pim_op_11\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_1_fused_pim_op_11_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2275_dsl ; test_enum_1_comb_14_fused_pim_op_2275\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2275_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1928_dsl ; test_enum_1_comb_11_fused_pim_op_1928\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1928_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1383_dsl ; test_enum_1_comb_13_fused_pim_op_1383\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1383_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1867_dsl ; test_enum_1_comb_15_fused_pim_op_1867\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1867_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 16 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_2179_dsl ; test_enum_1_comb_15_fused_pim_op_2179\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_2179_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_2179_dsl ; test_enum_1_comb_15_fused_pim_op_2179\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_2179_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1082_dsl ; test_enum_1_comb_11_fused_pim_op_1082\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1082_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_376_dsl ; test_enum_1_comb_13_fused_pim_op_376\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_376_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_576_dsl ; test_enum_1_comb_11_fused_pim_op_576\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_576_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1798_dsl ; test_enum_1_comb_13_fused_pim_op_1798\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1798_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 0 64 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1405_dsl ; test_enum_1_comb_14_fused_pim_op_1405\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1405_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1405_dsl ; test_enum_1_comb_14_fused_pim_op_1405\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1405_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1078_dsl ; test_enum_1_comb_9_fused_pim_op_1078\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1078_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 1 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_882_dsl ; test_enum_1_comb_13_fused_pim_op_882\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_882_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1787_dsl ; test_enum_1_comb_9_fused_pim_op_1787\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1787_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 -1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_236_dsl ; test_enum_1_comb_14_fused_pim_op_236\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_236_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 -1 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1131_dsl ; test_enum_1_comb_14_fused_pim_op_1131\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1131_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_634_dsl ; test_enum_1_comb_9_fused_pim_op_634\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_634_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1900_dsl ; test_enum_1_comb_11_fused_pim_op_1900\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1900_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_2151_dsl ; test_enum_1_comb_15_fused_pim_op_2151\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_2151_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_252_dsl ; test_enum_1_comb_10_fused_pim_op_252\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_252_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_2064_dsl ; test_enum_1_comb_10_fused_pim_op_2064\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_2064_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_2064_dsl ; test_enum_1_comb_10_fused_pim_op_2064\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_2064_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1415_dsl ; test_enum_1_comb_13_fused_pim_op_1415\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t16\n\t0\n\t0\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1415_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 16 0 0 16 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_546_dsl ; test_enum_1_comb_11_fused_pim_op_546\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_546_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1280_dsl ; test_enum_1_comb_11_fused_pim_op_1280\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1280_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_183_dsl ; test_enum_1_comb_10_fused_pim_op_183\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_183_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0 -1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_439_dsl ; test_enum_1_comb_13_fused_pim_op_439\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_439_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_525_dsl ; test_enum_1_comb_11_fused_pim_op_525\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_525_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_525_dsl ; test_enum_1_comb_11_fused_pim_op_525\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-absd_dsl ; typed-folded:vec-absd_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_525_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0 0 0)",
                "dst": "(typed-folded:vec-absd_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_240_dsl ; test_enum_1_comb_11_fused_pim_op_240\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_240_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1492_dsl ; test_enum_1_comb_13_fused_pim_op_1492\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1492_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1492_dsl ; test_enum_1_comb_13_fused_pim_op_1492\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1492_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_2062_dsl ; test_enum_1_comb_11_fused_pim_op_2062\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t64\n\t0\n\t64\n\t-1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_2062_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 64 -1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_2180_dsl ; test_enum_1_comb_15_fused_pim_op_2180\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_2180_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 16 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_9_dsl ; test_enum_1_comb_13_fused_pim_op_9\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t16\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_9_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 64 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 64 256 32)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_542_dsl ; test_enum_1_comb_10_fused_pim_op_542\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_542_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1094_dsl ; test_enum_1_comb_9_fused_pim_op_1094\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1094_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1115_dsl ; test_enum_1_comb_14_fused_pim_op_1115\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1115_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_122_dsl ; test_enum_1_comb_9_fused_pim_op_122\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_122_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1915_dsl ; test_enum_1_comb_10_fused_pim_op_1915\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1915_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1915_dsl ; test_enum_1_comb_10_fused_pim_op_1915\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1915_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1062_dsl ; test_enum_1_comb_10_fused_pim_op_1062\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1062_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1057_dsl ; test_enum_1_comb_12_fused_pim_op_1057\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1057_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1057_dsl ; test_enum_1_comb_12_fused_pim_op_1057\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1057_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1248_dsl ; test_enum_1_comb_10_fused_pim_op_1248\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1248_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_484_dsl ; test_enum_1_comb_14_fused_pim_op_484\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_484_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0 -1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1467_dsl ; test_enum_1_comb_13_fused_pim_op_1467\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1467_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1952_dsl ; test_enum_1_comb_11_fused_pim_op_1952\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1952_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1065_dsl ; test_enum_1_comb_10_fused_pim_op_1065\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1065_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_481_dsl ; test_enum_1_comb_14_fused_pim_op_481\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_481_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1807_dsl ; test_enum_1_comb_14_fused_pim_op_1807\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1807_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_2152_dsl ; test_enum_1_comb_15_fused_pim_op_2152\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_2152_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_2152_dsl ; test_enum_1_comb_15_fused_pim_op_2152\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_2152_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 2 1 1 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32 64 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1820_dsl ; test_enum_1_comb_14_fused_pim_op_1820\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1820_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_532_dsl ; test_enum_1_comb_12_fused_pim_op_532\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t-1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_532_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 -1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_532_dsl ; test_enum_1_comb_12_fused_pim_op_532\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t-1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_532_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 -1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2089_dsl ; test_enum_1_comb_14_fused_pim_op_2089\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2089_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2089_dsl ; test_enum_1_comb_14_fused_pim_op_2089\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2089_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1825_dsl ; test_enum_1_comb_11_fused_pim_op_1825\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1825_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1494_dsl ; test_enum_1_comb_13_fused_pim_op_1494\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1494_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2850_dsl ; test_enum_1_comb_14_fused_pim_op_2850\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2850_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_2125_dsl ; test_enum_1_comb_10_fused_pim_op_2125\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_2125_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_306_dsl ; test_enum_1_comb_15_fused_pim_op_306\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_306_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_306_dsl ; test_enum_1_comb_15_fused_pim_op_306\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_306_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1037_dsl ; test_enum_1_comb_12_fused_pim_op_1037\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t-1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1037_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 -1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1037_dsl ; test_enum_1_comb_12_fused_pim_op_1037\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t-1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1037_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 0 -1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_2060_dsl ; test_enum_1_comb_11_fused_pim_op_2060\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_2060_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1839_dsl ; test_enum_1_comb_11_fused_pim_op_1839\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1839_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1288_dsl ; test_enum_1_comb_12_fused_pim_op_1288\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1288_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1288_dsl ; test_enum_1_comb_12_fused_pim_op_1288\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1288_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1246_dsl ; test_enum_1_comb_11_fused_pim_op_1246\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1246_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1083_dsl ; test_enum_1_comb_9_fused_pim_op_1083\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1083_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_321_dsl ; test_enum_1_comb_11_fused_pim_op_321\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_321_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1754_dsl ; test_enum_1_comb_15_fused_pim_op_1754\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t128\n\t32\n\t0\n\t0\n\t0\n )_ (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1754_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0 128 16 0 0 0)",
                "dst": "(typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 16 8)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_536_dsl ; test_enum_1_comb_8_fused_pim_op_536\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_536_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_536_dsl ; test_enum_1_comb_8_fused_pim_op_536\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_536_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1257_dsl ; test_enum_1_comb_9_fused_pim_op_1257\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1257_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 1 1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1257_dsl ; test_enum_1_comb_9_fused_pim_op_1257\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1257_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1480_dsl ; test_enum_1_comb_11_fused_pim_op_1480\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1480_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_312_dsl ; test_enum_1_comb_9_fused_pim_op_312\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_312_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_2132_dsl ; test_enum_1_comb_10_fused_pim_op_2132\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_2132_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_2132_dsl ; test_enum_1_comb_10_fused_pim_op_2132\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_2132_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1895_dsl ; test_enum_1_comb_9_fused_pim_op_1895\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1895_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1299_dsl ; test_enum_1_comb_11_fused_pim_op_1299\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1299_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_253_dsl ; test_enum_1_comb_15_fused_pim_op_253\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_253_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_172_dsl ; test_enum_1_comb_12_fused_pim_op_172\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_172_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_172_dsl ; test_enum_1_comb_12_fused_pim_op_172\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_172_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_206_dsl ; test_enum_1_comb_9_fused_pim_op_206\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_206_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1844_dsl ; test_enum_1_comb_11_fused_pim_op_1844\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t64\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1844_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 16 0 -1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_527_dsl ; test_enum_1_comb_15_fused_pim_op_527\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_527_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_11_dsl ; test_enum_1_comb_8_fused_pim_op_11\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_11_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_11_dsl ; test_enum_1_comb_8_fused_pim_op_11\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_11_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1482_dsl ; test_enum_1_comb_15_fused_pim_op_1482\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1482_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_2_fused_pim_op_0_dsl ; test_enum_1_comb_2_fused_pim_op_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t16\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_2_fused_pim_op_0_dsl (reg (bv #x00 8)) 16 16 0 128 16 0 0)",
                "dst": "(typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 16 8)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_438_dsl ; test_enum_1_comb_9_fused_pim_op_438\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_438_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2040_dsl ; test_enum_1_comb_14_fused_pim_op_2040\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2040_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0 16 0 16 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1700_dsl ; test_enum_1_comb_9_fused_pim_op_1700\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1700_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1700_dsl ; test_enum_1_comb_9_fused_pim_op_1700\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1700_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_43_dsl ; test_enum_1_comb_15_fused_pim_op_43\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t64\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_43_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 64 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 64 256 32)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_470_dsl ; test_enum_1_comb_15_fused_pim_op_470\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_470_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2845_dsl ; test_enum_1_comb_14_fused_pim_op_2845\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2845_dsl (lit (bv #b1 1)) (reg (bv #x01 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2845_dsl ; test_enum_1_comb_14_fused_pim_op_2845\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2845_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_270_dsl ; test_enum_1_comb_10_fused_pim_op_270\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_270_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_29_dsl ; test_enum_1_comb_11_fused_pim_op_29\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t1\n\t2\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_29_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 1 2 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 64 16 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1935_dsl ; test_enum_1_comb_11_fused_pim_op_1935\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1935_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1935_dsl ; test_enum_1_comb_11_fused_pim_op_1935\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1935_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1336_dsl ; test_enum_1_comb_13_fused_pim_op_1336\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t0\n\t128\n\t8\n\t0\n\t0\n\t0\n )_ (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1336_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0 128 16 0 0 0)",
                "dst": "(typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 16 8)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1303_dsl ; test_enum_1_comb_9_fused_pim_op_1303\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1303_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1303_dsl ; test_enum_1_comb_9_fused_pim_op_1303\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1303_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1516_dsl ; test_enum_1_comb_11_fused_pim_op_1516\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1516_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_526_dsl ; test_enum_1_comb_11_fused_pim_op_526\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_526_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2290_dsl ; test_enum_1_comb_14_fused_pim_op_2290\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2290_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_632_dsl ; test_enum_1_comb_12_fused_pim_op_632\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t32\n\t16\n\t1\n\t32\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_632_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 1 32 16 1 32 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_632_dsl ; test_enum_1_comb_12_fused_pim_op_632\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t32\n\t16\n\t1\n\t32\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_632_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 1 32 16 1 32 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1448_dsl ; test_enum_1_comb_10_fused_pim_op_1448\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1448_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1210_dsl ; test_enum_1_comb_15_fused_pim_op_1210\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t64\n\t1\n\t1\n\t64\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1210_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 32 1 1 32 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_115_dsl ; test_enum_1_comb_9_fused_pim_op_115\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_115_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_456_dsl ; test_enum_1_comb_13_fused_pim_op_456\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_456_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_596_dsl ; test_enum_1_comb_11_fused_pim_op_596\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_596_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1463_dsl ; test_enum_1_comb_14_fused_pim_op_1463\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t32\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1463_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 16 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 16 256 8)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_124_dsl ; test_enum_1_comb_9_fused_pim_op_124\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_124_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0 64 0 -1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1468_dsl ; test_enum_1_comb_15_fused_pim_op_1468\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1468_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_2_fused_pim_op_7_dsl ; test_enum_1_comb_2_fused_pim_op_7\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_2_fused_pim_op_7_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1495_dsl ; test_enum_1_comb_9_fused_pim_op_1495\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1495_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1495_dsl ; test_enum_1_comb_9_fused_pim_op_1495\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1495_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_994_dsl ; test_enum_1_comb_15_fused_pim_op_994\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t64\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_994_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 1 1 1 64 1 64 1 64 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_2132_dsl ; test_enum_1_comb_11_fused_pim_op_2132\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_2132_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1114_dsl ; test_enum_1_comb_14_fused_pim_op_1114\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1114_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1853_dsl ; test_enum_1_comb_14_fused_pim_op_1853\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1853_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1053_dsl ; test_enum_1_comb_9_fused_pim_op_1053\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1053_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_2060_dsl ; test_enum_1_comb_10_fused_pim_op_2060\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_2060_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 -1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_297_dsl ; test_enum_1_comb_11_fused_pim_op_297\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_297_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_253_dsl ; test_enum_1_comb_10_fused_pim_op_253\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_253_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1659_dsl ; test_enum_1_comb_9_fused_pim_op_1659\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1659_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1697_dsl ; test_enum_1_comb_15_fused_pim_op_1697\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1697_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_424_dsl ; test_enum_1_comb_13_fused_pim_op_424\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_424_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_2059_dsl ; test_enum_1_comb_11_fused_pim_op_2059\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_2059_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_2119_dsl ; test_enum_1_comb_11_fused_pim_op_2119\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_2119_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2073_dsl ; test_enum_1_comb_14_fused_pim_op_2073\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2073_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1779_dsl ; test_enum_1_comb_13_fused_pim_op_1779\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1779_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1831_dsl ; test_enum_1_comb_9_fused_pim_op_1831\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1831_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_123_dsl ; test_enum_1_comb_9_fused_pim_op_123\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_123_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_307_dsl ; test_enum_1_comb_15_fused_pim_op_307\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_307_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1174_dsl ; test_enum_1_comb_11_fused_pim_op_1174\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1174_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2348_dsl ; test_enum_1_comb_14_fused_pim_op_2348\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2348_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1878_dsl ; test_enum_1_comb_9_fused_pim_op_1878\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1878_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_468_dsl ; test_enum_1_comb_13_fused_pim_op_468\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_468_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_206_dsl ; test_enum_1_comb_11_fused_pim_op_206\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_206_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0 32 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1820_dsl ; test_enum_1_comb_9_fused_pim_op_1820\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1820_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 64 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_3_fused_pim_op_10_dsl ; test_enum_1_comb_3_fused_pim_op_10\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t64\n\t1\n\t64\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_3_fused_pim_op_10_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 32 1 32 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_459_dsl ; test_enum_1_comb_11_fused_pim_op_459\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_459_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_500_dsl ; test_enum_1_comb_8_fused_pim_op_500\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_500_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_500_dsl ; test_enum_1_comb_8_fused_pim_op_500\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_500_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1624_dsl ; test_enum_1_comb_14_fused_pim_op_1624\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1624_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1445_dsl ; test_enum_1_comb_11_fused_pim_op_1445\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t1\n\t64\n\t1\n\t64\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1445_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 1 1 16 1 16 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_284_dsl ; test_enum_1_comb_15_fused_pim_op_284\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_284_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_1_fused_pim_op_1_dsl ; test_enum_1_comb_1_fused_pim_op_1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_1_fused_pim_op_1_dsl (reg (bv #x00 8)) 128 128 0 128 16 32 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 32 256 16)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1953_dsl ; test_enum_1_comb_11_fused_pim_op_1953\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1953_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1113_dsl ; test_enum_1_comb_14_fused_pim_op_1113\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1113_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1081_dsl ; test_enum_1_comb_15_fused_pim_op_1081\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1081_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1894_dsl ; test_enum_1_comb_15_fused_pim_op_1894\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1894_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_709_dsl ; test_enum_1_comb_13_fused_pim_op_709\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_709_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1843_dsl ; test_enum_1_comb_11_fused_pim_op_1843\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1843_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_228_dsl ; test_enum_1_comb_13_fused_pim_op_228\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_228_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_228_dsl ; test_enum_1_comb_13_fused_pim_op_228\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_228_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_55_dsl ; test_enum_1_comb_10_fused_pim_op_55\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_55_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1837_dsl ; test_enum_1_comb_14_fused_pim_op_1837\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1837_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1837_dsl ; test_enum_1_comb_14_fused_pim_op_1837\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1837_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_741_dsl ; test_enum_1_comb_15_fused_pim_op_741\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_741_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1271_dsl ; test_enum_1_comb_13_fused_pim_op_1271\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1271_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 1 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_216_dsl ; test_enum_1_comb_11_fused_pim_op_216\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n\t0\n\t64\n\t0\n\t64\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_216_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 -1 0 0 16 0 16 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1456_dsl ; test_enum_1_comb_14_fused_pim_op_1456\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t1\n\t2\n\t1\n\t1\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1456_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 1 2 1 0 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 64 16 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1461_dsl ; test_enum_1_comb_10_fused_pim_op_1461\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1461_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1399_dsl ; test_enum_1_comb_13_fused_pim_op_1399\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1399_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1319_dsl ; test_enum_1_comb_13_fused_pim_op_1319\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1319_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_839_dsl ; test_enum_1_comb_8_fused_pim_op_839\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_839_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_839_dsl ; test_enum_1_comb_8_fused_pim_op_839\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_839_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1555_dsl ; test_enum_1_comb_10_fused_pim_op_1555\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t32\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1555_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 64 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 64 256 32)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1079_dsl ; test_enum_1_comb_9_fused_pim_op_1079\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1079_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1079_dsl ; test_enum_1_comb_9_fused_pim_op_1079\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1079_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1273_dsl ; test_enum_1_comb_13_fused_pim_op_1273\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1273_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1931_dsl ; test_enum_1_comb_10_fused_pim_op_1931\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1931_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1015_dsl ; test_enum_1_comb_13_fused_pim_op_1015\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1015_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1248_dsl ; test_enum_1_comb_12_fused_pim_op_1248\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t-1\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1248_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 -1 16 0 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1248_dsl ; test_enum_1_comb_12_fused_pim_op_1248\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t-1\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1248_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 -1 16 0 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_795_dsl ; test_enum_1_comb_15_fused_pim_op_795\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_795_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_722_dsl ; test_enum_1_comb_15_fused_pim_op_722\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t64\n\t1\n\t1\n\t1\n\t64\n\t1\n\t64\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_722_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 16 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_2_fused_pim_op_14_dsl ; test_enum_1_comb_2_fused_pim_op_14\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_2_fused_pim_op_14_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_866_dsl ; test_enum_1_comb_9_fused_pim_op_866\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_866_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2101_dsl ; test_enum_1_comb_14_fused_pim_op_2101\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2101_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1685_dsl ; test_enum_1_comb_9_fused_pim_op_1685\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1685_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1110_dsl ; test_enum_1_comb_11_fused_pim_op_1110\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t0\n\t2\n\t0\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1110_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 1 2 1 1 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 64 16 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2307_dsl ; test_enum_1_comb_14_fused_pim_op_2307\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2307_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_774_dsl ; test_enum_1_comb_15_fused_pim_op_774\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t64\n\t1\n\t64\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_774_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 1 1 64 1 64 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1758_dsl ; test_enum_1_comb_10_fused_pim_op_1758\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t16\n\t2\n\t0\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1758_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 2 0 1 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 64 32 1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_254_dsl ; test_enum_1_comb_15_fused_pim_op_254\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_254_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_521_dsl ; test_enum_1_comb_11_fused_pim_op_521\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_521_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 -1 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1932_dsl ; test_enum_1_comb_15_fused_pim_op_1932\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1932_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1932_dsl ; test_enum_1_comb_15_fused_pim_op_1932\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1932_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_2503_dsl ; test_enum_1_comb_9_fused_pim_op_2503\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_2503_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_187_dsl ; test_enum_1_comb_11_fused_pim_op_187\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_187_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1447_dsl ; test_enum_1_comb_13_fused_pim_op_1447\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1447_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1447_dsl ; test_enum_1_comb_13_fused_pim_op_1447\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1447_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1482_dsl ; test_enum_1_comb_9_fused_pim_op_1482\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1482_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_2166_dsl ; test_enum_1_comb_10_fused_pim_op_2166\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_2166_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_2166_dsl ; test_enum_1_comb_10_fused_pim_op_2166\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_2166_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1409_dsl ; test_enum_1_comb_15_fused_pim_op_1409\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1409_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_2063_dsl ; test_enum_1_comb_10_fused_pim_op_2063\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_2063_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_2165_dsl ; test_enum_1_comb_15_fused_pim_op_2165\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_2165_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1519_dsl ; test_enum_1_comb_12_fused_pim_op_1519\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t0\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1519_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 0 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1519_dsl ; test_enum_1_comb_12_fused_pim_op_1519\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t0\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1519_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_662_dsl ; test_enum_1_comb_13_fused_pim_op_662\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_662_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_707_dsl ; test_enum_1_comb_13_fused_pim_op_707\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_707_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1913_dsl ; test_enum_1_comb_10_fused_pim_op_1913\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1913_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1913_dsl ; test_enum_1_comb_10_fused_pim_op_1913\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1913_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_305_dsl ; test_enum_1_comb_15_fused_pim_op_305\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_305_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1730_dsl ; test_enum_1_comb_9_fused_pim_op_1730\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1730_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_2133_dsl ; test_enum_1_comb_15_fused_pim_op_2133\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_2133_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1080_dsl ; test_enum_1_comb_15_fused_pim_op_1080\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1080_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1863_dsl ; test_enum_1_comb_9_fused_pim_op_1863\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1863_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1103_dsl ; test_enum_1_comb_11_fused_pim_op_1103\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t64\n\t32\n\t1\n\t0\n\t0\n\t0\n )_ (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1103_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0 128 16 1 0 0 0)",
                "dst": "(typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 16 8)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_478_dsl ; test_enum_1_comb_12_fused_pim_op_478\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t-1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_478_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 0 -1 16 0 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_478_dsl ; test_enum_1_comb_12_fused_pim_op_478\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t-1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_478_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 0 -1 16 0 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1048_dsl ; test_enum_1_comb_10_fused_pim_op_1048\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1048_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_291_dsl ; test_enum_1_comb_11_fused_pim_op_291\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_291_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_201_dsl ; test_enum_1_comb_13_fused_pim_op_201\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_201_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2234_dsl ; test_enum_1_comb_14_fused_pim_op_2234\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t32\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2234_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 16 0 -1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1962_dsl ; test_enum_1_comb_11_fused_pim_op_1962\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1962_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1962_dsl ; test_enum_1_comb_11_fused_pim_op_1962\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1962_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1712_dsl ; test_enum_1_comb_10_fused_pim_op_1712\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1712_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_804_dsl ; test_enum_1_comb_12_fused_pim_op_804\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_804_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 0 16 0 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_804_dsl ; test_enum_1_comb_12_fused_pim_op_804\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_804_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1833_dsl ; test_enum_1_comb_13_fused_pim_op_1833\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1833_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_708_dsl ; test_enum_1_comb_13_fused_pim_op_708\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_708_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_758_dsl ; test_enum_1_comb_10_fused_pim_op_758\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_758_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_622_dsl ; test_enum_1_comb_9_fused_pim_op_622\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_622_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_427_dsl ; test_enum_1_comb_14_fused_pim_op_427\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_427_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 -1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_186_dsl ; test_enum_1_comb_10_fused_pim_op_186\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_186_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_186_dsl ; test_enum_1_comb_10_fused_pim_op_186\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_186_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_458_dsl ; test_enum_1_comb_9_fused_pim_op_458\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_458_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2054_dsl ; test_enum_1_comb_14_fused_pim_op_2054\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2054_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1902_dsl ; test_enum_1_comb_15_fused_pim_op_1902\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1902_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_162_dsl ; test_enum_1_comb_10_fused_pim_op_162\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_162_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_3_fused_pim_op_9_dsl ; test_enum_1_comb_3_fused_pim_op_9\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t64\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_3_fused_pim_op_9_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 32 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1255_dsl ; test_enum_1_comb_9_fused_pim_op_1255\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1255_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1255_dsl ; test_enum_1_comb_9_fused_pim_op_1255\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1255_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1133_dsl ; test_enum_1_comb_14_fused_pim_op_1133\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1133_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_742_dsl ; test_enum_1_comb_15_fused_pim_op_742\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_742_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1485_dsl ; test_enum_1_comb_11_fused_pim_op_1485\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1485_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1480_dsl ; test_enum_1_comb_13_fused_pim_op_1480\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1480_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_552_dsl ; test_enum_1_comb_8_fused_pim_op_552\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t16\n\t1\n\t1\n\t32\n\t1\n\t32\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_552_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 16 0 0 32 0 32 16 16 0)",
                "dst": "(typed-folded:vec-le_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_552_dsl ; test_enum_1_comb_8_fused_pim_op_552\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t16\n\t1\n\t1\n\t32\n\t1\n\t32\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_552_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 16 0 0 32 0 32 16 16 0)",
                "dst": "(typed-folded:vec-ge_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1470_dsl ; test_enum_1_comb_12_fused_pim_op_1470\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1470_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1470_dsl ; test_enum_1_comb_12_fused_pim_op_1470\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1470_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1348_dsl ; test_enum_1_comb_15_fused_pim_op_1348\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1348_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_258_dsl ; test_enum_1_comb_15_fused_pim_op_258\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_258_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_11_dsl ; test_enum_1_comb_15_fused_pim_op_11\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t32\n\t0\n\t2\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_11_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 1 2 1 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 64 32 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_190_dsl ; test_enum_1_comb_9_fused_pim_op_190\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_190_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_590_dsl ; test_enum_1_comb_12_fused_pim_op_590\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_590_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_590_dsl ; test_enum_1_comb_12_fused_pim_op_590\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_590_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1541_dsl ; test_enum_1_comb_10_fused_pim_op_1541\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t16\n\t2\n\t0\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1541_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 2 0 1 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 64 32 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_633_dsl ; test_enum_1_comb_13_fused_pim_op_633\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_633_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_408_dsl ; test_enum_1_comb_13_fused_pim_op_408\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_408_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0 0 64 0 64 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_10_dsl ; test_enum_1_comb_8_fused_pim_op_10\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_10_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_10_dsl ; test_enum_1_comb_8_fused_pim_op_10\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_10_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1144_dsl ; test_enum_1_comb_9_fused_pim_op_1144\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t0\n\t64\n\t8\n\t1\n\t0\n\t0\n\t0\n )_ (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1144_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0 128 16 1 0 0 0)",
                "dst": "(typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 16 8)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_2183_dsl ; test_enum_1_comb_11_fused_pim_op_2183\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_2183_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_2183_dsl ; test_enum_1_comb_11_fused_pim_op_2183\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_2183_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_203_dsl ; test_enum_1_comb_13_fused_pim_op_203\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_203_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_235_dsl ; test_enum_1_comb_10_fused_pim_op_235\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_235_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_169_dsl ; test_enum_1_comb_8_fused_pim_op_169\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t1\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_169_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_169_dsl ; test_enum_1_comb_8_fused_pim_op_169\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t1\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_169_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_24_dsl ; test_enum_1_comb_9_fused_pim_op_24\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_24_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1127_dsl ; test_enum_1_comb_9_fused_pim_op_1127\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1127_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_205_dsl ; test_enum_1_comb_13_fused_pim_op_205\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_205_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_205_dsl ; test_enum_1_comb_13_fused_pim_op_205\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_205_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_25_dsl ; test_enum_1_comb_9_fused_pim_op_25\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_25_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1499_dsl ; test_enum_1_comb_15_fused_pim_op_1499\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1499_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1499_dsl ; test_enum_1_comb_15_fused_pim_op_1499\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1499_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_579_dsl ; test_enum_1_comb_11_fused_pim_op_579\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_579_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_579_dsl ; test_enum_1_comb_11_fused_pim_op_579\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_579_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1701_dsl ; test_enum_1_comb_9_fused_pim_op_1701\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1701_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1701_dsl ; test_enum_1_comb_9_fused_pim_op_1701\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1701_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_262_dsl ; test_enum_1_comb_13_fused_pim_op_262\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_262_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1223_dsl ; test_enum_1_comb_9_fused_pim_op_1223\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t16\n\t1\n\t1\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1223_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 32 1 1 32 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_2115_dsl ; test_enum_1_comb_10_fused_pim_op_2115\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_2115_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_2115_dsl ; test_enum_1_comb_10_fused_pim_op_2115\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_2115_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1248_dsl ; test_enum_1_comb_11_fused_pim_op_1248\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1248_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_4_fused_pim_op_3_dsl ; test_enum_1_comb_4_fused_pim_op_3\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_4_fused_pim_op_3_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 8 8 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024 1)"
            }
        }
    ],
    " (test_enum_1_comb_4_fused_pim_op_3_dsl ; test_enum_1_comb_4_fused_pim_op_3\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_4_fused_pim_op_3_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 8 8 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_872_dsl ; test_enum_1_comb_13_fused_pim_op_872\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_872_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1894_dsl ; test_enum_1_comb_9_fused_pim_op_1894\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1894_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1894_dsl ; test_enum_1_comb_9_fused_pim_op_1894\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1894_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_1270_dsl ; test_enum_1_comb_8_fused_pim_op_1270\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t0\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_1270_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_1270_dsl ; test_enum_1_comb_8_fused_pim_op_1270\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t0\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_1270_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_3589_dsl ; test_enum_1_comb_14_fused_pim_op_3589\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t32\n\t0\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_3589_dsl (lit (bv #b0 1)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) 128 128 0 128 8 16 0 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 16 256 8)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1623_dsl ; test_enum_1_comb_13_fused_pim_op_1623\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1623_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0 32 0 32 0 0 32 0 32 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_260_dsl ; test_enum_1_comb_9_fused_pim_op_260\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_260_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_1000_dsl ; test_enum_1_comb_8_fused_pim_op_1000\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t0\n\t8\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_1000_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_1000_dsl ; test_enum_1_comb_8_fused_pim_op_1000\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t0\n\t8\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_1000_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_2145_dsl ; test_enum_1_comb_15_fused_pim_op_2145\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_2145_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_290_dsl ; test_enum_1_comb_15_fused_pim_op_290\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_290_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1043_dsl ; test_enum_1_comb_12_fused_pim_op_1043\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1043_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1043_dsl ; test_enum_1_comb_12_fused_pim_op_1043\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1043_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1247_dsl ; test_enum_1_comb_15_fused_pim_op_1247\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1247_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_392_dsl ; test_enum_1_comb_9_fused_pim_op_392\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_392_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0 32 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1507_dsl ; test_enum_1_comb_12_fused_pim_op_1507\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1507_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1507_dsl ; test_enum_1_comb_12_fused_pim_op_1507\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1507_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1894_dsl ; test_enum_1_comb_10_fused_pim_op_1894\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1894_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1894_dsl ; test_enum_1_comb_10_fused_pim_op_1894\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1894_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1494_dsl ; test_enum_1_comb_10_fused_pim_op_1494\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1494_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1494_dsl ; test_enum_1_comb_10_fused_pim_op_1494\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1494_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_24_dsl ; test_enum_1_comb_10_fused_pim_op_24\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t16\n\t1\n\t2\n\t1\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_24_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 1 2 1 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 64 16 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2106_dsl ; test_enum_1_comb_14_fused_pim_op_2106\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2106_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_777_dsl ; test_enum_1_comb_11_fused_pim_op_777\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_777_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_586_dsl ; test_enum_1_comb_9_fused_pim_op_586\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t1\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_586_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 1 32 1 32 1 32 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_9_dsl ; test_enum_1_comb_12_fused_pim_op_9\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_9_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_9_dsl ; test_enum_1_comb_12_fused_pim_op_9\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_9_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_777_dsl ; test_enum_1_comb_10_fused_pim_op_777\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_777_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_226_dsl ; test_enum_1_comb_14_fused_pim_op_226\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_226_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0 0 64 0 64 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1593_dsl ; test_enum_1_comb_13_fused_pim_op_1593\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1593_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 64 -1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1702_dsl ; test_enum_1_comb_9_fused_pim_op_1702\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1702_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2288_dsl ; test_enum_1_comb_14_fused_pim_op_2288\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2288_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1824_dsl ; test_enum_1_comb_14_fused_pim_op_1824\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1824_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1885_dsl ; test_enum_1_comb_15_fused_pim_op_1885\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1885_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1479_dsl ; test_enum_1_comb_9_fused_pim_op_1479\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1479_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_487_dsl ; test_enum_1_comb_11_fused_pim_op_487\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_487_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 -1 0 16 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_1028_dsl ; test_enum_1_comb_8_fused_pim_op_1028\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t0\n\t8\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_1028_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_1028_dsl ; test_enum_1_comb_8_fused_pim_op_1028\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t0\n\t8\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_1028_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_2168_dsl ; test_enum_1_comb_11_fused_pim_op_2168\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_2168_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1450_dsl ; test_enum_1_comb_13_fused_pim_op_1450\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1450_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1450_dsl ; test_enum_1_comb_13_fused_pim_op_1450\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1450_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_2_fused_pim_op_11_dsl ; test_enum_1_comb_2_fused_pim_op_11\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_2_fused_pim_op_11_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_271_dsl ; test_enum_1_comb_15_fused_pim_op_271\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_271_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_743_dsl ; test_enum_1_comb_11_fused_pim_op_743\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_743_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_512_dsl ; test_enum_1_comb_15_fused_pim_op_512\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_512_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1951_dsl ; test_enum_1_comb_11_fused_pim_op_1951\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1951_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_613_dsl ; test_enum_1_comb_14_fused_pim_op_613\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_613_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_436_dsl ; test_enum_1_comb_9_fused_pim_op_436\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_436_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_2150_dsl ; test_enum_1_comb_10_fused_pim_op_2150\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_2150_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1080_dsl ; test_enum_1_comb_9_fused_pim_op_1080\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1080_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_560_dsl ; test_enum_1_comb_11_fused_pim_op_560\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_560_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_559_dsl ; test_enum_1_comb_15_fused_pim_op_559\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_559_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1511_dsl ; test_enum_1_comb_13_fused_pim_op_1511\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1511_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1700_dsl ; test_enum_1_comb_15_fused_pim_op_1700\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1700_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1700_dsl ; test_enum_1_comb_15_fused_pim_op_1700\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1700_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_2136_dsl ; test_enum_1_comb_11_fused_pim_op_2136\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_2136_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_1416_dsl ; test_enum_1_comb_8_fused_pim_op_1416\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t0\n\t32\n\t0\n\t0\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t32\n\t0\n )_ (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_1416_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 0 16 0 0 32 0 32 16 -1 16 0)",
                "dst": "(typed-folded:vec-le_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_1416_dsl ; test_enum_1_comb_8_fused_pim_op_1416\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t0\n\t32\n\t0\n\t0\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t32\n\t0\n )_ (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_1416_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 0 16 0 0 32 0 32 16 -1 16 0)",
                "dst": "(typed-folded:vec-ge_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_726_dsl ; test_enum_1_comb_10_fused_pim_op_726\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_726_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1998_dsl ; test_enum_1_comb_14_fused_pim_op_1998\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1998_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_577_dsl ; test_enum_1_comb_11_fused_pim_op_577\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_577_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_577_dsl ; test_enum_1_comb_11_fused_pim_op_577\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_577_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1966_dsl ; test_enum_1_comb_10_fused_pim_op_1966\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1966_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_778_dsl ; test_enum_1_comb_11_fused_pim_op_778\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_778_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2121_dsl ; test_enum_1_comb_14_fused_pim_op_2121\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2121_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2121_dsl ; test_enum_1_comb_14_fused_pim_op_2121\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2121_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1908_dsl ; test_enum_1_comb_10_fused_pim_op_1908\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1908_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1124_dsl ; test_enum_1_comb_15_fused_pim_op_1124\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t64\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1124_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 16 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 16 256 8)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1083_dsl ; test_enum_1_comb_15_fused_pim_op_1083\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1083_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_126_dsl ; test_enum_1_comb_9_fused_pim_op_126\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_126_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 -1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_352_dsl ; test_enum_1_comb_9_fused_pim_op_352\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_352_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_1_fused_pim_op_6_dsl ; test_enum_1_comb_1_fused_pim_op_6\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_1_fused_pim_op_6_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_358_dsl ; test_enum_1_comb_9_fused_pim_op_358\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_358_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 -1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_348_dsl ; test_enum_1_comb_8_fused_pim_op_348\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_348_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_348_dsl ; test_enum_1_comb_8_fused_pim_op_348\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t1\n\t16\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_348_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_216_dsl ; test_enum_1_comb_13_fused_pim_op_216\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_216_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_884_dsl ; test_enum_1_comb_9_fused_pim_op_884\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_884_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1588_dsl ; test_enum_1_comb_14_fused_pim_op_1588\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1588_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1583_dsl ; test_enum_1_comb_9_fused_pim_op_1583\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1583_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_648_dsl ; test_enum_1_comb_9_fused_pim_op_648\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_648_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_250_dsl ; test_enum_1_comb_15_fused_pim_op_250\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_250_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 -1 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1846_dsl ; test_enum_1_comb_15_fused_pim_op_1846\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1846_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 -1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1805_dsl ; test_enum_1_comb_13_fused_pim_op_1805\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1805_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 64 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_561_dsl ; test_enum_1_comb_15_fused_pim_op_561\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_561_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_5_fused_pim_op_10_dsl ; test_enum_1_comb_5_fused_pim_op_10\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_5_fused_pim_op_10_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1596_dsl ; test_enum_1_comb_9_fused_pim_op_1596\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1596_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_420_dsl ; test_enum_1_comb_9_fused_pim_op_420\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_420_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1621_dsl ; test_enum_1_comb_13_fused_pim_op_1621\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1621_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0 0 64 0 64 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1496_dsl ; test_enum_1_comb_13_fused_pim_op_1496\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1496_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1095_dsl ; test_enum_1_comb_13_fused_pim_op_1095\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1095_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1095_dsl ; test_enum_1_comb_13_fused_pim_op_1095\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1095_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_592_dsl ; test_enum_1_comb_14_fused_pim_op_592\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_592_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1108_dsl ; test_enum_1_comb_9_fused_pim_op_1108\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1108_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_542_dsl ; test_enum_1_comb_11_fused_pim_op_542\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_542_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_303_dsl ; test_enum_1_comb_14_fused_pim_op_303\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_303_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2003_dsl ; test_enum_1_comb_14_fused_pim_op_2003\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2003_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 -1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_2_fused_pim_op_4_dsl ; test_enum_1_comb_2_fused_pim_op_4\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_2_fused_pim_op_4_dsl (reg (bv #x00 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_481_dsl ; test_enum_1_comb_13_fused_pim_op_481\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_481_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_481_dsl ; test_enum_1_comb_13_fused_pim_op_481\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_481_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1109_dsl ; test_enum_1_comb_9_fused_pim_op_1109\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1109_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1109_dsl ; test_enum_1_comb_9_fused_pim_op_1109\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1109_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_426_dsl ; test_enum_1_comb_13_fused_pim_op_426\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_426_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2267_dsl ; test_enum_1_comb_14_fused_pim_op_2267\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2267_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0 0 64 0 64 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_308_dsl ; test_enum_1_comb_11_fused_pim_op_308\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_308_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_227_dsl ; test_enum_1_comb_14_fused_pim_op_227\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_227_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1431_dsl ; test_enum_1_comb_9_fused_pim_op_1431\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n\t0\n\t16\n\t0\n\t16\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1431_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0 16 0 16 0 0 16 0 16 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2071_dsl ; test_enum_1_comb_14_fused_pim_op_2071\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2071_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2071_dsl ; test_enum_1_comb_14_fused_pim_op_2071\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2071_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_1285_dsl ; test_enum_1_comb_15_fused_pim_op_1285\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_1285_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_462_dsl ; test_enum_1_comb_12_fused_pim_op_462\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t16\n\t1\n\t1\n\t32\n\t1\n\t32\n\t16\n\t16\n\t1\n\t1\n\t32\n\t1\n\t32\n\t16\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_462_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 16 0 0 32 0 32 16 16 0 0 32 0 32 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_462_dsl ; test_enum_1_comb_12_fused_pim_op_462\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t16\n\t1\n\t1\n\t32\n\t1\n\t32\n\t16\n\t16\n\t1\n\t1\n\t32\n\t1\n\t32\n\t16\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_462_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 16 0 0 32 0 32 16 16 0 0 32 0 32 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_901_dsl ; test_enum_1_comb_9_fused_pim_op_901\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_901_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_1487_dsl ; test_enum_1_comb_8_fused_pim_op_1487\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_1487_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_8_fused_pim_op_1487_dsl ; test_enum_1_comb_8_fused_pim_op_1487\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_8_fused_pim_op_1487_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_202_dsl ; test_enum_1_comb_12_fused_pim_op_202\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_202_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_202_dsl ; test_enum_1_comb_12_fused_pim_op_202\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_202_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 1 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2017_dsl ; test_enum_1_comb_14_fused_pim_op_2017\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n\t32\n\t0\n\t0\n\t32\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2017_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 32 0 0 32 0 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1695_dsl ; test_enum_1_comb_13_fused_pim_op_1695\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1695_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_307_dsl ; test_enum_1_comb_14_fused_pim_op_307\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_307_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_821_dsl ; test_enum_1_comb_12_fused_pim_op_821\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_821_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_821_dsl ; test_enum_1_comb_12_fused_pim_op_821\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_821_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 0 0 16 0 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_233_dsl ; test_enum_1_comb_10_fused_pim_op_233\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_233_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 -1 0 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_817_dsl ; test_enum_1_comb_14_fused_pim_op_817\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_817_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1887_dsl ; test_enum_1_comb_9_fused_pim_op_1887\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1887_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1513_dsl ; test_enum_1_comb_14_fused_pim_op_1513\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1513_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2092_dsl ; test_enum_1_comb_14_fused_pim_op_2092\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2092_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1955_dsl ; test_enum_1_comb_10_fused_pim_op_1955\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1955_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1826_dsl ; test_enum_1_comb_11_fused_pim_op_1826\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1826_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1637_dsl ; test_enum_1_comb_14_fused_pim_op_1637\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1637_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_899_dsl ; test_enum_1_comb_13_fused_pim_op_899\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_899_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1017_dsl ; test_enum_1_comb_11_fused_pim_op_1017\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1017_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1473_dsl ; test_enum_1_comb_12_fused_pim_op_1473\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1473_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1473_dsl ; test_enum_1_comb_12_fused_pim_op_1473\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1473_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_360_dsl ; test_enum_1_comb_13_fused_pim_op_360\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_360_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_323_dsl ; test_enum_1_comb_15_fused_pim_op_323\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_323_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_604_dsl ; test_enum_1_comb_9_fused_pim_op_604\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_604_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 1 32 1 32 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_454_dsl ; test_enum_1_comb_10_fused_pim_op_454\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t-1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_454_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 -1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1081_dsl ; test_enum_1_comb_13_fused_pim_op_1081\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1081_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1081_dsl ; test_enum_1_comb_13_fused_pim_op_1081\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1081_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1775_dsl ; test_enum_1_comb_9_fused_pim_op_1775\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1775_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 -1 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_238_dsl ; test_enum_1_comb_10_fused_pim_op_238\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-add_dsl ; typed-folded:vec-add_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_238_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 0)",
                "dst": "(typed-folded:vec-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_3234_dsl ; test_enum_1_comb_14_fused_pim_op_3234\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t2\n\t0\n\t1\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_3234_dsl (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 2 1 1 0 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 64 16 1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_706_dsl ; test_enum_1_comb_13_fused_pim_op_706\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_706_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 1 1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_897_dsl ; test_enum_1_comb_13_fused_pim_op_897\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t1\n\t1\n\t16\n\t1\n\t16\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_897_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1896_dsl ; test_enum_1_comb_10_fused_pim_op_1896\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1896_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1896_dsl ; test_enum_1_comb_10_fused_pim_op_1896\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1896_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_181_dsl ; test_enum_1_comb_10_fused_pim_op_181\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t-1\n\t0\n\t0\n\t32\n\t0\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_181_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0 0 64 0 64 -1 0)",
                "dst": "(typed-folded:vec-div_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_2284_dsl ; test_enum_1_comb_14_fused_pim_op_2284\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t-1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_2284_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1643_dsl ; test_enum_1_comb_9_fused_pim_op_1643\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1643_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1643_dsl ; test_enum_1_comb_9_fused_pim_op_1643\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1643_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_191_dsl ; test_enum_1_comb_12_fused_pim_op_191\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_191_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 16 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_191_dsl ; test_enum_1_comb_12_fused_pim_op_191\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t1\n\t8\n\t8\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_191_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_27_dsl ; test_enum_1_comb_14_fused_pim_op_27\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t1\n\t2\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_27_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 1 2 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 64 32 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1464_dsl ; test_enum_1_comb_9_fused_pim_op_1464\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1464_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_2_fused_pim_op_2_dsl ; test_enum_1_comb_2_fused_pim_op_2\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t16\n\t1\n\t2\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_2_fused_pim_op_2_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0)",
                "dst": "(typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 64 16 0)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1388_dsl ; test_enum_1_comb_14_fused_pim_op_1388\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-saturate_dsl ; typed-folded:vec-saturate_ip16_is1024_op8_os512_signed_0\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n\t8\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1388_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-saturate_dsl (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 128 16 1) 16 256 8 1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1388_dsl ; test_enum_1_comb_14_fused_pim_op_1388\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-reduce-add_dsl ; typed-folded:vec-reduce-add_p16_s1024_signed_-1_reduce_2\n\t2\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1388_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-reduce-add_dsl 2 (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 128 32 0) 16 256 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1388_dsl ; test_enum_1_comb_14_fused_pim_op_1388\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1388_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1388_dsl ; test_enum_1_comb_14_fused_pim_op_1388\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1388_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:cast-truncate_dsl (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 128 16 1) 16 256 8)"
            }
        }
    ]
}