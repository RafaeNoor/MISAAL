{
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 1)",
                "dst": "(typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128)"
            }
        }
    ],
    " (vmax_u8_dsl ; vmax_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_arm_max_min",
            "property": {
                "src": "(vmax_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0)",
                "dst": "(typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 1)",
                "dst": "(typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 128)"
            }
        }
    ],
    " (vmin_u32_dsl ; vmin_u32\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_arm_max_min",
            "property": {
                "src": "(vmin_u32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 128)"
            }
        }
    ]
}