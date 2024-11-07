{
    " (hexagon_V6_vmpyhvsrs_128B_dsl ; hexagon_V6_vmpyhvsrs_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t32\n\t1\n\t1\n\t1\n\t64\n\t1\n\t1\n\t-1\n\t32\n\t16\n\t1\n\t1\n\t0\n )+ (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(lit (bv 15 (bitvector 16)))\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "MulShiftRight",
            "property": {
                "src": " (hexagon_V6_vmpyhvsrs_128B_dsl ; hexagon_V6_vmpyhvsrs_128B\n\t(lit (bv #x00000001 (bitvector 32)))\n\t(lit (bv #x0000000f (bitvector 32)))\n\t(lit (bv #x00000002 (bitvector 32)))\n\t(lit (bv #x000000000000000f (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t32\n\t1\n\t1\n\t1\n\t64\n\t1\n\t1\n\t-1\n\t32\n\t16\n\t1\n\t1\n\t0\n )",
                "dst": " (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(lit (bv 15 (bitvector 16)))\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )",
                "output_size": 1024
            }
        }
    ],
    " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000001 (bitvector 64)))\n\t (hexagon_V6_vmpyewuh_128B_dsl ; hexagon_V6_vmpyewuh_128B\n\t\t(lit (bv #x0000000000000010 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )+ (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p32_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is32_os1024_signed_None\n\t\t(lit (bv 31 (bitvector 32)))\n\t\t32\n\t\t32\n\t\t32\n\t )\n\t32\n\t1024\n )": [
        {
            "property_name": "MulShiftRight",
            "property": {
                "src": " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000001 (bitvector 64)))\n\t (hexagon_V6_vmpyewuh_128B_dsl ; hexagon_V6_vmpyewuh_128B\n\t\t(lit (bv #x0000000000000010 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )",
                "dst": " (typed:signed-vec-rounding_mul_shift_right ; typed:signed-vec-rounding_mul_shift_right_p32_s1024_signed_1\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is32_os1024_signed_None\n\t\t(lit (bv 31 (bitvector 32)))\n\t\t32\n\t\t32\n\t\t32\n\t )\n\t32\n\t1024\n )",
                "output_size": 1024
            }
        }
    ]
}
