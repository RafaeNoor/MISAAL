{
    " (hexagon_V6_vlsrw_128B_dsl ; hexagon_V6_vlsrw_128B\n\t(lit (bv #x0000000000000000000000000000001f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )_ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_shifts_right_w",
            "property": {
                "src": "(hexagon_V6_vlsrw_128B_dsl (lit (bv #x0000001f 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 0)",
                "dst": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 32 32 32) 32 1024)"
            }
        }
    ]
}