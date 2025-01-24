{
    " (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t (hexagon_V6_vcombine_128B_dsl ; hexagon_V6_vcombine_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1024\n\t0\n )_Reg": [
        {
            "property_name": "EqClassEqualDepthV4_hvx_combine_simpl",
            "property": {
                "src": "(hexagon_V6_lo_128B_dsl (hexagon_V6_vcombine_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 1024 8 1024 0) 1024 1024 0 1024 8 1024 0)",
                "dst": "(reg (bv #x01 8))"
            }
        }
    ],
    " (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t (hexagon_V6_vcombine_128B_dsl ; hexagon_V6_vcombine_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n )_Reg": [
        {
            "property_name": "EqClassEqualDepthV4_hvx_combine_simpl",
            "property": {
                "src": "(hexagon_V6_vassign_128B_dsl (hexagon_V6_vcombine_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 1024 8 1024 0) 1024 1024 0 1024 8 0)",
                "dst": "(reg (bv #x01 8))"
            }
        }
    ]
}