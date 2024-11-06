{
    " (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t-1\n\t1\n\t0\n )_ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_absd",
            "property": {
                "src": "(hexagon_V6_vabsdiffh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 -1 0 0)",
                "dst": "(typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024)"
            }
        }
    ]
}