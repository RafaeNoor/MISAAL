{
    " (vabdq_s32_dsl ; vabdq_s32\n\t(lit (bv #x00000000000000000000000000000000 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_arm_absd",
            "property": {
                "src": "(vabdq_s32_dsl (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x01 8)) 8 128)"
            }
        }
    ],
    " (vabdq_s32_dsl ; vabdq_s32\n\t(lit (bv #x00000000000000000000000000000000 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n\t-1\n\t0\n\t-1\n\t1\n\t64\n\t1\n\t64\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_arm_absd",
            "property": {
                "src": "(vabdq_s32_dsl (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x00 8)) 8 128) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 8 128) 16 128)"
            }
        }
    ],
    " (vaba_u8_dsl ; vaba_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t-1\n\t0\n\t-1\n\t0\n\t16\n\t0\n\t16\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_arm_absd",
            "property": {
                "src": "(vaba_u8_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) (reg (bv #x00 8)) 128 128 0 128 8 -1 0 -1 0 16 0 16)",
                "dst": "(typed:vec-add (typed:unsigned-vec-absd (reg (bv #x02 8)) (reg (bv #x00 8)) 8 128) (reg (bv #x01 8)) 8 128)"
            }
        }
    ]
}