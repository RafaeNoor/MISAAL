{
    " (hexagon_V6_interleave_2_128B_dsl ; hexagon_V6_interleave_2_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n )_ (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4_interleave_2",
            "property": {
                "src": "(hexagon_V6_interleave_2_128B_dsl (reg (bv #x00 8)) 16 32)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 2)"
            }
        }
    ],
    " (hexagon_V6_interleave_2_128B_dsl ; hexagon_V6_interleave_2_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n )_ (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_interleave_2",
            "property": {
                "src": "(hexagon_V6_interleave_2_128B_dsl (reg (bv #x00 8)) 16 32)",
                "dst": "(typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16)"
            }
        }
    ]
}