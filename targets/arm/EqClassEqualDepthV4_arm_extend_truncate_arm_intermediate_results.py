{
    " (vmov_n_u16_dsl ; vmov_n_u16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t16\n )_ (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4_arm_extend_truncate",
            "property": {
                "src": "(vmov_n_u16_dsl (reg (bv #x00 8)) 128 128 0 128 32)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)"
            }
        }
    ],
    " (vmovn_s16_dsl ; vmovn_s16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t2\n )_ (typed:cast-int-truncate ; typed:cast-int_1_ip16_is1024_op8_os512_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1\n\t64\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4_arm_extend_truncate",
            "property": {
                "src": "(vmovn_s16_dsl (reg (bv #x00 8)) 64 64 0 64 32 2)",
                "dst": "(typed:cast-int-truncate (reg (bv #x00 8)) 64 1 2 32)"
            }
        }
    ],
    " (vmovn_s16_dsl ; vmovn_s16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t2\n )_ (typed:cast-uint-truncate ; typed:cast-uint_1_ip16_is1024_op8_os512_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1\n\t64\n\t8\n )": [
        {
            "property_name": "EqClassEqualDepthV4_arm_extend_truncate",
            "property": {
                "src": "(vmovn_s16_dsl (reg (bv #x00 8)) 64 64 0 64 32 2)",
                "dst": "(typed:cast-uint-truncate (reg (bv #x00 8)) 64 1 2 32)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4_arm_extend_truncate",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16)",
                "dst": "(typed:cast-uint-extend (reg (bv #x00 8)) 8 1 8 16)"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t64\n\t0\n\t2\n\t1\n\t64\n )_ (typed:cast-int-extend ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1\n\t64\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4_arm_extend_truncate",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16)",
                "dst": "(typed:cast-int-extend (reg (bv #x00 8)) 8 1 8 16)"
            }
        }
    ]
}