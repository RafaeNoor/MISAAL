{
    " (hexagon_V6_vlsrh_128B_dsl ; hexagon_V6_vlsrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t64\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t32\n\t0\n )_ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_shifts_right",
            "property": {
                "src": "(hexagon_V6_vlsrh_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 0 32 0)",
                "dst": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) 16 1024)"
            }
        }
    ]
}