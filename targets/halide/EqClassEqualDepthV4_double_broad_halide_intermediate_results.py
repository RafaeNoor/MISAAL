{
    " (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t16\n\t64\n )_ (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4_double_broad",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32 16)"
            }
        },
        {
            "property_name": "EqClassEqualDepthV4_double_broad",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:xBroadcast (typed:xBroadcast (reg (bv #x00 8)) 16 16 2) 32 32 16)"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t16\n\t64\n )_ (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t16\n\t64\n )": [
        {
            "property_name": "EqClassEqualDepthV4_double_broad",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16) 32 32 16)"
            }
        },
        {
            "property_name": "EqClassEqualDepthV4_double_broad",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:xBroadcast (typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x00 8)) 8 16) 32 32 16)"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t16\n\t64\n )_ (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t0\n\t1\n\t32\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_double_broad",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 64 1 64 8 1024)"
            }
        },
        {
            "property_name": "EqClassEqualDepthV4_double_broad",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:slice_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 64) 64 1 64 8 1024)"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t16\n\t16\n\t64\n )_ (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_double_broad",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 8 256)"
            }
        },
        {
            "property_name": "EqClassEqualDepthV4_double_broad",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 32)",
                "dst": "(typed:concat_vectors (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) (typed:xBroadcast (reg (bv #x00 8)) 16 16 16) 8 256)"
            }
        }
    ]
}
