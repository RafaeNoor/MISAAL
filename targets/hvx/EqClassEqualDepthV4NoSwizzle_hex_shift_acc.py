{
    " (hexagon_V6_vaslw_acc_128B_dsl ; hexagon_V6_vaslw_acc_128B\n\t(lit (bv #x0000000000000000000000000000001f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_hex_shift_scalar_Acc",
            "property": {
                "src": "(hexagon_V6_vaslw_acc_128B_dsl (lit (bv #x0000001f 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-add (typed:vec-shl (reg (bv #x01 8)) (typed:xBroadcast (reg (bv #x02 8)) 32 32 32) 32 1024) (reg (bv #x00 8)) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_hex_shift_scalar_Acc_hb",
            "property": {
                "src": "(hexagon_V6_vaslh_acc_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) (typed:cast-int-extend (reg (bv #x02 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-add (typed:vec-shl (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 64) 16 1024) (reg (bv #x01 8)) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_hex_shift_scalar_Acc_hb",
            "property": {
                "src": "(hexagon_V6_vaslh_acc_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) (typed:cast-uint-extend (reg (bv #x02 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-add (typed:vec-shl (reg (bv #x01 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 64) 16 1024) (reg (bv #x00 8)) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_hex_shift_scalar_Acc_hb",
            "property": {
                "src": "(hexagon_V6_vaslh_acc_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 2) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-add (typed:vec-shl (reg (bv #x01 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 64) 64 1024) (reg (bv #x00 8)) 16 1024)"
            }
        }
    ]

}
