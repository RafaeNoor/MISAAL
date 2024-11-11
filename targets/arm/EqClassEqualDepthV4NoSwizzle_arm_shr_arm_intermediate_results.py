{
    " (vshrq_n_u8_dsl ; vshrq_n_u8\n\t(lit (bv #x00000000 (bitvector 8)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )_ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_arm_shr",
            "property": {
                "src": "(vshrq_n_u8_dsl (lit (bv #x00000000 32)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 4 16) 128 128 0 128 32 -1 0 0 64)",
                "dst": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 32 32 4) 32 128)"
            }
        }
    ],
    " (vshl_s8_dsl ; vshl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t1\n\t16\n\t1\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 128 128 0 128 64 0 0 128 1)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 8) 32 128)"
            }
        }
    ],
    " (vshl_s8_dsl ; vshl_s8\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t0\n\t1\n\t16\n\t1\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_arm_shr",
            "property": {
                "src": "(vshl_s8_dsl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 128 128 0 128 16 0 0 32 1)",
                "dst": "(typed:vec-shl (typed:xBroadcast (reg (bv #x00 8)) 16 16 8) (reg (bv #x01 8)) 16 128)"
            }
        }
    ],
    " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_arm_shr",
            "property": {
                "src": "(vsraq_n_u8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x02 8)) 8 1 4 16) 128 128 0 128 32 -1 0 0 64)",
                "dst": "(typed:vec-add (typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 32 32 4) 32 128) (reg (bv #x01 8)) 32 128)"
            }
        }
    ],
    " (vsraq_n_u8_dsl ; vsraq_n_u8\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t128\n\t128\n\t0\n\t128\n\t8\n\t-1\n\t0\n\t0\n\t64\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_arm_shr",
            "property": {
                "src": "(vsraq_n_u8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 4) 128 128 0 128 8 -1 0 0 64)",
                "dst": "(typed:vec-add (typed:unsigned-vec-shr (reg (bv #x01 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 8) 32 128) (reg (bv #x00 8)) 8 128)"
            }
        }
    ]

}
