{
    " (hvx_swizzle_1_dsl ; hvx_swizzle_61\n\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t2048\n\t32\n\t0\n\t32\n\t16\n\t64\n\t2\n\t0\n )_ (hexagon_V6_vshuffvdd_128B_dsl ; hexagon_V6_vshuffvdd_128B\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t(lit (bv -1 (bitvector 32)))\n\t2048\n\t2048\n\t0\n\t1024\n\t8\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_hvx_swizzle",
            "property": {
                "src": "(hvx_swizzle_1_dsl (reg (bv #x00 8)) 2048 32 0 32 16 64 2 0)",
                "dst": "(hexagon_V6_vshuffvdd_128B_dsl (hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0) (hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0) (lit (bv #xfffffffe 32)) 2048 2048 0 1024 8 0)"
            }
        }
    ]
}