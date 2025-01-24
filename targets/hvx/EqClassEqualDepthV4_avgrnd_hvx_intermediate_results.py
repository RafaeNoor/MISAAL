{
    " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavguw_128B\n\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t0\n )_ (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavguw_128B_dsl (lit (bv #x00000002 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 0 -1 0)",
                "dst": "(typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavgwrnd_128B\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t-1\n\t-1\n\t0\n )_ (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x00000001 32)) (lit (bv #x00000002 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 1 -1 -1 0)",
                "dst": "(typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavgwrnd_128B\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t-1\n\t-1\n\t0\n )_ (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x00000001 32)) (lit (bv #x00000002 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 0 -1 -1 0)",
                "dst": "(typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavguw_128B\n\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t0\n )_ (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_avgrnd",
            "property": {
                "src": "(hexagon_V6_vavguw_128B_dsl (lit (bv #x0002 16)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 1 -1 0)",
                "dst": "(typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024)"
            }
        }
    ]
}