{
    " (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t1\n\t64\n\t8\n\t#f\n )_ (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwuh_sat_128B\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t0\n\t32\n\t1\n\t32\n\t0\n\t32\n\t1\n\t16\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4NoSwizzle_hvx_sat",
            "property": {
                "src": "(typed:vec-saturate (reg (bv #x00 8)) 32 1 64 16 #t)",
                "dst": "(hexagon_V6_vpackwuh_sat_128B_dsl (hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0) (hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0) 1024 1024 0 512 16 0 512 16 1 32 1 32 1 32 1 16 0)"
            }
        }
    ]
}