{
    " (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(hexagon_V6_vasrhv_128B_dsl (reg (bv #x00 8)) (lit (bv #x00000000 32)) (reg (bv #x01 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vlsrwv_128B_dsl ; hexagon_V6_vlsrwv_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x00000000000000000000000000000000 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )_ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(hexagon_V6_vlsrwv_128B_dsl (reg (bv #x01 8)) (lit (bv #x0000 16)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )_ (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_filtered",
            "property": {
                "src": "(hexagon_V6_vaslhv_128B_dsl (reg (bv #x01 8)) (lit (bv #x00000000 32)) (reg (bv #x00 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:vec-shl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024)"
            }
        }
    ]
}
