{
    " (test_enum_1_comb_11_fused_pim_op_943_dsl ; test_enum_1_comb_11_fused_pim_op_943\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t64\n\t32\n\t1\n\t1\n\t1\n\t64\n\t1\n\t64\n\t0\n\t0\n )_ (typed-folded:vec-shl_dsl ; typed-folded:vec-shl_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_943_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16 0 128 16 1 1 1 32 1 32 0 0)",
                "dst": "(typed-folded:vec-shl_dsl (reg (bv #x00 8)) (typed-folded:xBroadcast_dsl (reg (bv #x01 8)) 16 8) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1048_dsl ; test_enum_1_comb_10_fused_pim_op_1048\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1048_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-div_dsl (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 8 128 -1) (reg (bv #x01 8)) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1048_dsl ; test_enum_1_comb_10_fused_pim_op_1048\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1048_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-div_dsl (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1) (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 128 -1) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1048_dsl ; test_enum_1_comb_10_fused_pim_op_1048\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1048_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-div_dsl (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 128 -1) (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128 1) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1048_dsl ; test_enum_1_comb_10_fused_pim_op_1048\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1048_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-div_dsl (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 128 -1) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1048_dsl ; test_enum_1_comb_10_fused_pim_op_1048\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1048_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-div_dsl (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 8 128 -1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128 1) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1048_dsl ; test_enum_1_comb_10_fused_pim_op_1048\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1048_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 0)",
                "dst": "(typed-folded:vec-div_dsl (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 64 128 -1) (typed-folded:vec-halving_add_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128 128 1) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_2368_dsl ; test_enum_1_comb_9_fused_pim_op_2368\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t0\n\t64\n\t8\n\t0\n\t16\n\t2\n\t0\n\t32\n\t4\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_2368_dsl (lit (bv #b1 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 8 8 0 128 8 0 16 2 0 32 4 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-lt_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 32 512 0) (typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 8 16) (typed-folded:cast-truncate_dsl (reg (bv #x01 8)) 16 256 8) 8 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_2368_dsl ; test_enum_1_comb_9_fused_pim_op_2368\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t0\n\t64\n\t8\n\t0\n\t16\n\t2\n\t0\n\t32\n\t4\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_2368_dsl (lit (bv #b1 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x02 8)) 8 8 0 128 8 0 16 2 0 32 4 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-le_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 32 512 0) (typed-folded:cast-truncate_dsl (reg (bv #x01 8)) 16 256 8) (typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 8 16) 8 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_2368_dsl ; test_enum_1_comb_9_fused_pim_op_2368\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t0\n\t64\n\t8\n\t0\n\t16\n\t2\n\t0\n\t32\n\t4\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_2368_dsl (lit (bv #b1 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x02 8)) 8 8 0 128 8 0 16 2 0 32 4 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-gt_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 32 512 0) (typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 8 16) (typed-folded:cast-truncate_dsl (reg (bv #x01 8)) 16 256 8) 8 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_2368_dsl ; test_enum_1_comb_9_fused_pim_op_2368\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b0 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t8\n\t0\n\t64\n\t8\n\t0\n\t16\n\t2\n\t0\n\t32\n\t4\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_2368_dsl (lit (bv #b1 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x02 8)) 8 8 0 128 8 0 16 2 0 32 4 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-ge_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 32 512 0) (typed-folded:cast-truncate_dsl (reg (bv #x01 8)) 16 256 8) (typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 8 16) 8 128)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1952_dsl ; test_enum_1_comb_11_fused_pim_op_1952\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-saturate_dsl ; typed-folded:vec-saturate_ip16_is1024_op8_os512_signed_0\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n\t8\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1952_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-saturate_dsl (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 128 16 1) 16 256 8 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1952_dsl ; test_enum_1_comb_11_fused_pim_op_1952\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-reduce-add_dsl ; typed-folded:vec-reduce-add_p16_s1024_signed_-1_reduce_2\n\t2\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1952_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-reduce-add_dsl 2 (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 32 128 64 0) 32 256 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1952_dsl ; test_enum_1_comb_11_fused_pim_op_1952\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1952_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 128 -1) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1952_dsl ; test_enum_1_comb_11_fused_pim_op_1952\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1952_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:cast-truncate_dsl (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 128 16 1) 16 256 8)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1952_dsl ; test_enum_1_comb_11_fused_pim_op_1952\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1952_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwor_dsl (typed-folded:vec-bwxor_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 8 128 -1) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1952_dsl ; test_enum_1_comb_11_fused_pim_op_1952\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1952_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwor_dsl (typed-folded:vec-bwxor_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 32 128 -1) (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 128 -1) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_1952_dsl ; test_enum_1_comb_11_fused_pim_op_1952\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_1952_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwor_dsl (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 64 128 -1) (reg (bv #x01 8)) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128) (typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) (reg (bv #x01 8)) 16 128) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 64 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 32 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 8 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (typed-folded:vec-halving_add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32 128 0) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 8 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 64 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x00 8)) (typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x03 8)) 16 128) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 8 -1) (reg (bv #x01 8)) (reg (bv #x02 8)) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 16 128 -1) (reg (bv #x03 8)) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 32 128 -1) (typed-folded:vec-max_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 128 1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 16 128 -1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 64 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 32 128 -1) (typed-folded:vec-halving_add_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 16 128 1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 128 -1) (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 32 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 16 128 -1) (typed-folded:vec-if_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) (reg (bv #x03 8)) 16 128) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 1) (reg (bv #x01 8)) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 32 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 1) (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 128 0) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 8 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 1) (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 1) (typed-folded:vec-halving_add_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 32 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 1) (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 1) (reg (bv #x03 8)) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 8 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 32 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 1) (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 1) (typed-folded:vec-halving_add_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 64 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 1) (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 8 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 1) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16 8 1) (reg (bv #x02 8)) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16 8 1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16 8 1) (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 32 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16 8 1) (typed-folded:vec-halving_add_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 64 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16 8 1) (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16 8 1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 -1) (reg (bv #x02 8)) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) 32 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-halving_add_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 64 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 32 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 -1) (reg (bv #x03 8)) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 64 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 32 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-max_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-halving_add_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 64 128 1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1922_dsl ; test_enum_1_comb_9_fused_pim_op_1922\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1922_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x01 8)) 128 128 0 128 16 1 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8 -1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x03 8)) 16 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1470_dsl ; test_enum_1_comb_12_fused_pim_op_1470\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1470_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (typed-folded:vec-le_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1470_dsl ; test_enum_1_comb_12_fused_pim_op_1470\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1470_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-bwnot_dsl (typed-folded:vec-ge_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 0) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1470_dsl ; test_enum_1_comb_12_fused_pim_op_1470\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1470_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (reg (bv #x02 8)) (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 -1) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1470_dsl ; test_enum_1_comb_12_fused_pim_op_1470\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1470_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 16 2048 -1) (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 64 2048 -1) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1470_dsl ; test_enum_1_comb_12_fused_pim_op_1470\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1470_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 0 8 0 8 0)",
                "dst": "(typed-folded:vec-lt_dsl (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 1024 16 0) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 1024 16 0) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1470_dsl ; test_enum_1_comb_12_fused_pim_op_1470\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-lt_dsl ; typed-folded:vec-lt_p16_s1024_signed_0\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1470_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x02 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-lt_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048 1) (reg (bv #x02 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1470_dsl ; test_enum_1_comb_12_fused_pim_op_1470\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1470_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x02 8)) 128 128 0 128 1 0 16 0 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (reg (bv #x02 8)) (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048 0) 16 2048 0)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1470_dsl ; test_enum_1_comb_12_fused_pim_op_1470\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1470_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 2048 -1) (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 16 2048 -1) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1470_dsl ; test_enum_1_comb_12_fused_pim_op_1470\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1470_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 1 0 8 0 8 0)",
                "dst": "(typed-folded:vec-gt_dsl (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 1024 16 0) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 1024 16 0) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_12_fused_pim_op_1470_dsl ; test_enum_1_comb_12_fused_pim_op_1470\n\t(lit (bv #b0 (bitvector 1)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n\t32\n\t0\n\t32\n\t0\n )_ (typed-folded:vec-gt_dsl ; typed-folded:vec-gt_p16_s1024_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_12_fused_pim_op_1470_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 1 1 16 1 16 0)",
                "dst": "(typed-folded:vec-gt_dsl (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 64 2048 -1) (reg (bv #x01 8)) 16 2048 1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_2036_dsl ; test_enum_1_comb_13_fused_pim_op_2036\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t16\n\t2\n\t0\n\t16\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_2036_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 8 1 16 2 0 16 0 8 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x02 8)) (typed-folded:vec-mul_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 8 16 128 1) (typed-folded:cast-truncate_dsl (reg (bv #x01 8)) 16 256 8) 8 128)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_2036_dsl ; test_enum_1_comb_13_fused_pim_op_2036\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t16\n\t2\n\t0\n\t16\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_2036_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 16 2 0 16 0 8 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x02 8)) 8 16 -1) (typed-folded:cast-truncate_dsl (reg (bv #x01 8)) 16 256 8) (typed-folded:vec-mul_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 8 16 128 1) 8 128)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_2036_dsl ; test_enum_1_comb_13_fused_pim_op_2036\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t16\n\t2\n\t0\n\t16\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_2036_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 8 1 16 2 0 16 0 8 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 16 1) (typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 8 16 128 0) (typed-folded:cast-truncate_dsl (reg (bv #x01 8)) 16 256 8) 8 128)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_2036_dsl ; test_enum_1_comb_13_fused_pim_op_2036\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t16\n\t2\n\t0\n\t16\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_2036_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 16 2 0 16 0 8 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 16 1) (typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 8 16 128 0) (typed-folded:cast-truncate_dsl (reg (bv #x01 8)) 16 256 8) 8 128)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_2036_dsl ; test_enum_1_comb_13_fused_pim_op_2036\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t16\n\t2\n\t0\n\t16\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_2036_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 8 1 16 2 0 16 0 8 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 16 16 1) (typed-folded:vec-mul_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 8 16 128 0) (typed-folded:cast-truncate_dsl (reg (bv #x01 8)) 16 256 8) 8 128)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_2036_dsl ; test_enum_1_comb_13_fused_pim_op_2036\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t16\n\t2\n\t0\n\t16\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_2036_dsl (reg (bv #x03 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 1 16 2 0 16 0 8 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 16 -1) (typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 8 16 128 1) (typed-folded:cast-truncate_dsl (reg (bv #x01 8)) 16 256 8) 8 128)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_2036_dsl ; test_enum_1_comb_13_fused_pim_op_2036\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t1\n\t16\n\t2\n\t0\n\t16\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_2036_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (lit (bv #b1 1)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 8 1 16 2 0 16 0 8 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 16 -1) (typed-folded:vec-mul_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 8 16 128 0) (typed-folded:cast-truncate_dsl (reg (bv #x01 8)) 16 256 8) 8 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-min_dsl (typed-folded:vec-if_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 16 128) (typed-folded:vec-if_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 16 128) 16 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x01 8)) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 128 0) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x01 8)) (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 128 1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x01 8)) (typed-folded:vec-halving_add_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 16 128 0) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x01 8)) (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 128 -1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x01 8)) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 128 -1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (reg (bv #x01 8)) (typed-folded:vec-if_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 16 128) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 8 8 -1) (reg (bv #x02 8)) (reg (bv #x01 8)) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 16 128 0) (reg (bv #x02 8)) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 16 128 0) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 16 128 0) (typed-folded:vec-halving_add_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 64 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 16 128 0) (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 16 128 0) (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 16 128 0) (typed-folded:vec-if_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 16 128) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 16 128 0) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 128 -1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 1) (reg (bv #x02 8)) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 128 0) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 1) (typed-folded:vec-max_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 32 128 1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 1) (typed-folded:vec-halving_add_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32 128 1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 1) (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128 -1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 1) (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128 -1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 1) (reg (bv #x03 8)) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128 1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 1) (typed-folded:vec-max_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 8 128 1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 1) (typed-folded:vec-halving_add_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16 128 0) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 1) (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 128 -1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 64 128 -1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 8 1) (reg (bv #x02 8)) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 8 1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 128 1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 8 1) (typed-folded:vec-max_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 128 1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 8 1) (typed-folded:vec-halving_add_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128 128 1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 8 1) (typed-folded:vec-bwor_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 128 -1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 8 1) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 16 128 -1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 -1) (reg (bv #x00 8)) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 128 1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-max_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 64 128 1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-halving_add_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64 128 0) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128 -1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-bwand_dsl (reg (bv #x03 8)) (reg (bv #x03 8)) 32 128 -1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 -1) (reg (bv #x03 8)) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 128 1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 128 1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x03 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-halving_add_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 8 16 128 1) (typed-folded:vec-min_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x02 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 128 -1) (typed-folded:vec-min_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_1921_dsl ; test_enum_1_comb_9_fused_pim_op_1921\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t1\n\t0\n\t8\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_1921_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 16 1 0 16 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8 -1) (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x02 8)) 16 128 -1) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x03 8)) 16 128 0) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_560_dsl ; test_enum_1_comb_11_fused_pim_op_560\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_560_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 16 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (reg (bv #x01 8)) (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 32 128 -1) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_560_dsl ; test_enum_1_comb_11_fused_pim_op_560\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_560_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 64 128 -1) (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 16 128 -1) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_560_dsl ; test_enum_1_comb_11_fused_pim_op_560\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_560_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x02 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1) (reg (bv #x02 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_560_dsl ; test_enum_1_comb_11_fused_pim_op_560\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_560_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-bwand_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 64 128 -1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_560_dsl ; test_enum_1_comb_11_fused_pim_op_560\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t-1\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_560_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 64 128 -1) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_511_dsl ; test_enum_1_comb_13_fused_pim_op_511\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t2\n\t0\n )_ (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_511_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 32 2 0)",
                "dst": "(typed-folded:cast-truncate_dsl (typed-folded:vec-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64 256 0) 32 256 16)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_511_dsl ; test_enum_1_comb_13_fused_pim_op_511\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t16\n\t2\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t (typed-folded:cast-truncate_dsl ; typed-folded:cast-truncate_ip16_is1024_op8_os512_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t8\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_511_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 32 2 0)",
                "dst": "(typed-folded:vec-mul_dsl (typed-folded:cast-truncate_dsl (reg (bv #x00 8)) 32 256 16) (typed-folded:cast-truncate_dsl (reg (bv #x01 8)) 32 256 16) 16 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_15_fused_pim_op_719_dsl ; test_enum_1_comb_15_fused_pim_op_719\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t128\n\t32\n\t0\n\t1\n\t1\n\t64\n\t1\n\t64\n\t0\n )_ (typed-folded:vec-shl_dsl ; typed-folded:vec-shl_p16_s1024_signed_-1\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_15_fused_pim_op_719_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16 0 128 16 0 1 1 32 1 32 0)",
                "dst": "(typed-folded:vec-shl_dsl (reg (bv #x00 8)) (typed-folded:xBroadcast_dsl (reg (bv #x01 8)) 16 8) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 1) (reg (bv #x00 8)) 16 32 64 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 1) (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 1) 16 32 64 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 1) (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 1) 8 16 64 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 0) (reg (bv #x01 8)) 16 32 64 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 2 1 1 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 0) (typed-folded:vec-min_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0) 16 32 64 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 1) (typed-folded:vec-max_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 1) 16 32 64 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 -1) (reg (bv #x01 8)) 16 32 64 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-halving_add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 16 64 1) (typed-folded:vec-halving_add_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16 64 1) 8 16 64 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 -1) (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 -1) 8 16 64 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64 -1) (reg (bv #x01 8)) 8 16 64 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 2 1 1 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 -1) (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 0) 8 16 64 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 -1) (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 1) 16 32 64 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 2 1 1 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 -1) (typed-folded:vec-min_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 1) 8 16 64 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64 -1) (typed-folded:vec-max_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 0) 8 16 64 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64 -1) (typed-folded:vec-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64 -1) 16 32 64 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 2 0 0 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 -1) (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 -1) 8 16 64 0)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-mul_dsl ; typed-folded:vec-mul_p16_s1024_signed_0\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 2 0 1 0)",
                "dst": "(typed-folded:vec-mul_dsl (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 64 32 0) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 64 32 1) 32 64 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-min_dsl ; typed-folded:vec-min_p16_s1024_signed_0\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 2 0 0 0)",
                "dst": "(typed-folded:vec-min_dsl (typed-folded:vec-widen-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32 64 0) (typed-folded:vec-widen-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 64 0) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-max_dsl ; typed-folded:vec-max_p16_s1024_signed_0\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 2 1 1 0)",
                "dst": "(typed-folded:vec-max_dsl (typed-folded:vec-widen-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32 64 1) (typed-folded:vec-widen-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 64 1) 8 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-halving_add_dsl ; typed-folded:vec-halving_add_p16_s1024_signed_0\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 2 1 1 0)",
                "dst": "(typed-folded:vec-halving_add_dsl (typed-folded:vec-widen-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 64 1) (typed-folded:vec-widen-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 64 1) 64 128 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 2 0 0 0)",
                "dst": "(typed-folded:vec-bwor_dsl (typed-folded:vec-widen-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 64 0) (typed-folded:vec-widen-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16 64 0) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 2 1 1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (typed-folded:vec-widen-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 64 1) (typed-folded:vec-widen-mul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32 64 1) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 2 0 0 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-le_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64 0) (typed-folded:vec-widen-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 64 0) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 64 16 1) 32 128)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-le_dsl ; typed-folded:vec-le_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:concat_vectors_dsl ; typed-folded:concat_vectors_ip8_is1024_op8_os2048_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 2 0 0 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-le_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64 0) (typed-folded:vec-widen-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 64 0) (typed-folded:concat_vectors_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 64 128)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 2 0 0 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-ge_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 0) (typed-folded:vec-widen-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32 64 0) (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 64 16 1) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-ge_dsl ; typed-folded:vec-ge_p16_s1024_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:concat_vectors_dsl ; typed-folded:concat_vectors_ip8_is1024_op8_os2048_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 2 0 0 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-ge_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 0) (typed-folded:vec-widen-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 64 0) (typed-folded:concat_vectors_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 2 0 0 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 -1) (typed-folded:vec-widen-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 64 0) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 16 64 32 1) 32 128)"
            }
        }
    ],
    " (test_enum_1_comb_11_fused_pim_op_606_dsl ; test_enum_1_comb_11_fused_pim_op_606\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t1\n\t0\n\t0\n )_ (typed-folded:vec-if_dsl ; typed-folded:vec-if_p16_s1024_signed_None\n\t (typed-folded:vec-eq_dsl ; typed-folded:vec-eq_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t\t1024\n\t\t0\n\t )\n\t (typed-folded:concat_vectors_dsl ; typed-folded:concat_vectors_ip8_is1024_op8_os2048_signed_-1\n\t\t(reg (bv 4 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 5 (bitvector 8))) ; < 1 x i8> False\n\t\t8\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_11_fused_pim_op_606_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 2 0 0 0)",
                "dst": "(typed-folded:vec-if_dsl (typed-folded:vec-eq_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64 -1) (typed-folded:vec-widen-mul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16 64 0) (typed-folded:concat_vectors_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 128)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1496_dsl ; test_enum_1_comb_13_fused_pim_op_1496\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1496_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0)",
                "dst": "(typed-folded:vec-bwxor_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x00 8)) 32 128 -1) (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 64 128 -1) 16 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1496_dsl ; test_enum_1_comb_13_fused_pim_op_1496\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1496_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 0)",
                "dst": "(typed-folded:vec-bwand_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 8 128 -1) (reg (bv #x00 8)) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1496_dsl ; test_enum_1_comb_13_fused_pim_op_1496\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1496_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (typed-folded:vec-bwxor_dsl (reg (bv #x00 8)) (reg (bv #x02 8)) 8 128 -1) (reg (bv #x01 8)) 64 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_13_fused_pim_op_1496_dsl ; test_enum_1_comb_13_fused_pim_op_1496\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t8\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwor_dsl ; typed-folded:vec-bwor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_13_fused_pim_op_1496_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x03 8)) 128 128 0 128 16 0)",
                "dst": "(typed-folded:vec-bwand_dsl (typed-folded:vec-bwxor_dsl (reg (bv #x02 8)) (reg (bv #x03 8)) 32 128 -1) (typed-folded:vec-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128 -1) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1842_dsl ; test_enum_1_comb_14_fused_pim_op_1842\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t16\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1842_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16 0 128 16 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (typed-folded:xBroadcast_dsl (reg (bv #x00 8)) 16 8) (reg (bv #x01 8)) 8 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1842_dsl ; test_enum_1_comb_14_fused_pim_op_1842\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t16\n\t0\n\t128\n\t16\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1842_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 16 16 0 128 16 0 0)",
                "dst": "(typed-folded:vec-bwand_dsl (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128 -1) (typed-folded:xBroadcast_dsl (reg (bv #x02 8)) 16 8) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_14_fused_pim_op_1188_dsl ; test_enum_1_comb_14_fused_pim_op_1188\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t16\n\t1\n\t0\n )_ (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_14_fused_pim_op_1188_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x03 8)) (reg (bv #x00 8)) 128 128 0 128 16 1 0)",
                "dst": "(typed-folded:vec-div_dsl (typed-folded:vec-bwxor_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 128 -1) (typed-folded:vec-bwxor_dsl (reg (bv #x03 8)) (reg (bv #x00 8)) 64 128 -1) 16 128 1)"
            }
        }
    ],
    " (test_enum_1_comb_9_fused_pim_op_312_dsl ; test_enum_1_comb_9_fused_pim_op_312\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n )_ (typed-folded:vec-sub_dsl ; typed-folded:vec-sub_p16_s1024_signed_-1\n\t (typed-folded:vec-bwnot_dsl ; typed-folded:vec-bwnot_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-bwxor_dsl ; typed-folded:vec-bwxor_p16_s1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_9_fused_pim_op_312_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 128 128 0 128 32 -1 0)",
                "dst": "(typed-folded:vec-sub_dsl (typed-folded:vec-bwnot_dsl (reg (bv #x01 8)) 64 128 -1) (typed-folded:vec-bwxor_dsl (reg (bv #x02 8)) (reg (bv #x00 8)) 8 128 -1) 32 128 -1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1541_dsl ; test_enum_1_comb_10_fused_pim_op_1541\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t16\n\t2\n\t0\n\t0\n\t0\n )_ (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t16\n\t1024\n\t32\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1541_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 16 2 1 1 0)",
                "dst": "(typed-folded:cast-extend_dsl (typed-folded:vec-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 -1) 8 64 16 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1541_dsl ; test_enum_1_comb_10_fused_pim_op_1541\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t16\n\t2\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-widen-mul_dsl ; typed-folded:vec-widen-mul_p16_s1024_signed_0\n\t (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t-1\n\t )\n\t (typed-folded:vec-div_dsl ; typed-folded:vec-div_p16_s1024_signed_0\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t0\n\t )\n\t16\n\t32\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1541_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 16 32 2 1 1 0)",
                "dst": "(typed-folded:vec-widen-mul_dsl (typed-folded:vec-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64 -1) (typed-folded:vec-div_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64 1) 16 32 64 1)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1541_dsl ; test_enum_1_comb_10_fused_pim_op_1541\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t16\n\t2\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-mod_dsl ; typed-folded:vec-mod_p16_s1024_signed_0\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (typed-folded:xBroadcast_dsl ; typed-folded:xBroadcast_is16_os1024_signed_-1\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1541_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64 0 64 16 32 2 0 1 0)",
                "dst": "(typed-folded:vec-mod_dsl (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 16 64 32 0) (typed-folded:xBroadcast_dsl (reg (bv #x01 8)) 16 8) 32 128 0)"
            }
        }
    ],
    " (test_enum_1_comb_10_fused_pim_op_1541_dsl ; test_enum_1_comb_10_fused_pim_op_1541\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t8\n\t16\n\t2\n\t0\n\t0\n\t0\n )_ (typed-folded:vec-bwand_dsl ; typed-folded:vec-bwand_p16_s1024_signed_-1\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (typed-folded:cast-extend_dsl ; typed-folded:cast-extend_ip16_is1024_op32_os2048_signed_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t16\n\t1024\n\t-1\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full",
            "property": {
                "src": "(test_enum_1_comb_10_fused_pim_op_1541_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 16 2 1 1 0)",
                "dst": "(typed-folded:vec-bwand_dsl (typed-folded:cast-extend_dsl (reg (bv #x00 8)) 8 64 16 1) (typed-folded:cast-extend_dsl (reg (bv #x01 8)) 8 64 16 1) 8 128 -1)"
            }
        }
    ]
}