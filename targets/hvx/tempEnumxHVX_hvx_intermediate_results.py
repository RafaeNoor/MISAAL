{
    " (hexagon_V6_lvsplatw_128B_dsl ; hexagon_V6_lvsplatw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )_ (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t16\n\t64\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_lvsplatw_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 32 0)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 32)"
            }
        }
    ],
    " (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1024\n\t0\n )_ (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t0\n\t1\n\t32\n\t16\n\t1024\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0)",
                "dst": "(typed:slice_vectors (reg (bv #x00 8)) 16 1 16 64 2048)"
            }
        }
    ],
    " (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n )_ (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t0\n\t1\n\t32\n\t16\n\t1024\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0)",
                "dst": "(typed:slice_vectors (reg (bv #x00 8)) 0 1 32 32 2048)"
            }
        }
    ],
    " (hexagon_V6_interleave_2_128B_dsl ; hexagon_V6_interleave_2_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n )_ (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t16\n\t64\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_interleave_2_128B_dsl (reg (bv #x00 8)) 16 32)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 2)"
            }
        }
    ],
    " (hexagon_V6_vcombine_128B_dsl ; hexagon_V6_vcombine_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n\t1024\n\t8\n\t1024\n\t0\n )_ (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_vcombine_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 1024 8 1024 0)",
                "dst": "(typed:concat_vectors (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_interleave_2_128B_dsl ; hexagon_V6_interleave_2_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n )_ (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_interleave_2_128B_dsl (reg (bv #x00 8)) 16 32)",
                "dst": "(typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16)"
            }
        }
    ],
    " (hexagon_V6_interleave_4_128B_dsl ; hexagon_V6_interleave_4_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t32\n )_ (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t16\n\t64\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_interleave_4_128B_dsl (reg (bv #x00 8)) 8 32)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 4)"
            }
        }
    ],
    " (hexagon_V6_lvsplatw_128B_dsl ; hexagon_V6_lvsplatw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )_ (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t0\n\t1\n\t32\n\t16\n\t1024\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_lvsplatw_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 32 0)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 64) 128 1 128 8 2048)"
            }
        }
    ],
    " (hexagon_V6_lvsplatw_128B_dsl ; hexagon_V6_lvsplatw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )_ (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_lvsplatw_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 32 0)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) (typed:xBroadcast (reg (bv #x00 8)) 32 32 16) 8 512)"
            }
        }
    ],
    " (hexagon_V6_lvsplatb_128B_dsl ; hexagon_V6_lvsplatb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t0\n )_ (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t16\n\t64\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_lvsplatb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)",
                "dst": "(typed:xBroadcast (typed:slice_vectors (reg (bv #x00 8)) 0 1 2 8 32) 16 16 64)"
            }
        }
    ],
    " (hexagon_V6_interleave_2_128B_dsl ; hexagon_V6_interleave_2_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t16\n\t32\n )_ (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t0\n\t1\n\t32\n\t16\n\t1024\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_interleave_2_128B_dsl (reg (bv #x00 8)) 16 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 4) 4 1 4 8 64)"
            }
        }
    ],
    " (hexagon_V6_interleave_4_128B_dsl ; hexagon_V6_interleave_4_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t32\n )_ (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t16\n\t64\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_interleave_4_128B_dsl (reg (bv #x00 8)) 8 32)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 16 16 2)"
            }
        }
    ],
    " (hexagon_V6_interleave_4_128B_dsl ; hexagon_V6_interleave_4_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t32\n )_ (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t16\n\t64\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_interleave_4_128B_dsl (reg (bv #x00 8)) 8 32)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 16 16 2)"
            }
        }
    ],
    " (hexagon_V6_interleave_4_128B_dsl ; hexagon_V6_interleave_4_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t32\n )_ (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t0\n\t1\n\t32\n\t16\n\t1024\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_interleave_4_128B_dsl (reg (bv #x00 8)) 8 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 8) 4 1 4 8 64)"
            }
        }
    ],
    " (hexagon_V6_interleave_4_128B_dsl ; hexagon_V6_interleave_4_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t32\n )_ (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_interleave_4_128B_dsl (reg (bv #x00 8)) 8 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 8 16)"
            }
        }
    ],
    " (hexagon_V6_interleave_4_128B_dsl ; hexagon_V6_interleave_4_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t32\n )_ (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_interleave_4_128B_dsl (reg (bv #x00 8)) 8 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 16)"
            }
        }
    ],
    " (hexagon_V6_interleave_4_128B_dsl ; hexagon_V6_interleave_4_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t32\n )_ (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_interleave_4_128B_dsl (reg (bv #x00 8)) 8 32)",
                "dst": "(typed:concat_vectors (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) (typed:xBroadcast (reg (bv #x00 8)) 8 8 2) 8 16)"
            }
        }
    ],
    " (hexagon_V6_interleave_4_128B_dsl ; hexagon_V6_interleave_4_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t8\n\t32\n )_ (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  3 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "tempEnumxHVX",
            "property": {
                "src": "(hexagon_V6_interleave_4_128B_dsl (reg (bv #x00 8)) 8 32)",
                "dst": "(typed:concat_vectors (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 16)"
            }
        }
    ]
}