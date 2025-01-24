arm_swizzles_EqClassEqualDepthV3Synth={
    " (arm_swizzle_206_dsl ; arm_swizzle_53\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(arm_swizzle_206_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 2 0)",
                "dst": "(vzip1q_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 1 8 2)"
            }
        }
    ],
    " (arm_swizzle_25_dsl ; arm_swizzle_25\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i32> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i32> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(arm_swizzle_25_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 0 32 0)",
                "dst": "(vuzp2_s16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 32 32 1 16)"
            }
        }
    ],
    " (arm_swizzle_205_dsl ; arm_swizzle_9\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t32\n\t2\n\t0\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(arm_swizzle_205_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 32 2 0)",
                "dst": "(vzip2q_s64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 8 8 1 4 8 4 2 8)"
            }
        }
    ],
    " (arm_swizzle_206_dsl ; arm_swizzle_53\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(arm_swizzle_206_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 2 0)",
                "dst": "(vzip1q_u32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 1 8 2)"
            }
        }
    ],
    " (arm_swizzle_19_dsl ; arm_swizzle_19\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i32> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i32> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t96\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(arm_swizzle_19_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 32 0 96 0)",
                "dst": "(vget_high_u64_dsl (vtrn2_s8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 32 1 16 2) 64 64 0 64 64 0 64)"
            }
        }
    ],
    " (arm_swizzle_51_dsl ; arm_swizzle_51\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t32\n\t8\n\t8\n\t2\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(arm_swizzle_51_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 16 16 2 0)",
                "dst": "(vget_low_u8_dsl (vzip1q_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 16 16 1 8 2) 64 64 0 64 64 0)"
            }
        }
    ],
    " (arm_swizzle_25_dsl ; arm_swizzle_25\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i32> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i32> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t32\n\t0\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(arm_swizzle_25_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 0 32 0)",
                "dst": "(vzip2q_s64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 32 32 1 16 32 1 2 32)"
            }
        }
    ],
    " (arm_swizzle_205_dsl ; arm_swizzle_9\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i16> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t32\n\t2\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(arm_swizzle_205_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 32 2 0)",
                "dst": "(vzip2q_s64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 32 16 16 1 8 16 2 2 16)"
            }
        }
    ],
    " (arm_swizzle_21_dsl ; arm_swizzle_21\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i32> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i32> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t0\n\t32\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(arm_swizzle_21_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 0 32 0)",
                "dst": "(vget_high_u64_dsl (vzip1q_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 32 1 16 2) 64 64 0 64 64 0 64)"
            }
        }
    ],
    " (arm_swizzle_13_dsl ; arm_swizzle_13\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t64\n\t64\n\t0\n\t32\n\t16\n\t16\n\t32\n\t2\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(arm_swizzle_13_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 8 64 2 0)",
                "dst": "(vget_low_u8_dsl (vzip2q_s64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 8 8 1 4 8 8 2 8) 64 64 0 64 64 0)"
            }
        }
    ]
}