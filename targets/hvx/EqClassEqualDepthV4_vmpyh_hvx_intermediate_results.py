{
    " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vmpyh_128B_dsl ; hexagon_V6_vmpyh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t (hexagon_V6_interleave_2_128B_dsl ; hexagon_V6_interleave_2_128B\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t16\n\t\t\t32\n\t\t )\n\t\t32\n\t\t32\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t\t32\n\t\t1024\n\t\t1\n\t\t1\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t2048\n\t64\n\t0\n\t64\n\t32\n\t32\n\t2\n\t0\n )_ (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_vmpyh",
            "property": {
                "src": "(hvx_swizzle_1_dsl (hexagon_V6_vmpyh_128B_dsl (reg (bv #x00 8)) (hexagon_V6_interleave_2_128B_dsl (reg (bv #x01 8)) 16 32) 32 32 0 512 16 0 512 16 32 1 0 0 0 32 1024 0 0 16 16 2 0) 2048 64 0 64 32 32 2 0)",
                "dst": "(typed:unsigned-vec-widen-mul (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) (reg (bv #x00 8)) 16 1024)"
            }
        }
    ],
    " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vmpyh_128B_dsl ; hexagon_V6_vmpyh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t (hexagon_V6_interleave_2_128B_dsl ; hexagon_V6_interleave_2_128B\n\t\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t\t16\n\t\t\t32\n\t\t )\n\t\t32\n\t\t32\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t\t32\n\t\t1024\n\t\t1\n\t\t1\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t2048\n\t64\n\t0\n\t64\n\t32\n\t32\n\t2\n\t0\n )_ (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_vmpyh",
            "property": {
                "src": "(hvx_swizzle_1_dsl (hexagon_V6_vmpyh_128B_dsl (reg (bv #x00 8)) (hexagon_V6_interleave_2_128B_dsl (reg (bv #x01 8)) 16 32) 32 32 0 512 16 0 512 16 32 1 1 1 0 32 1024 1 1 16 16 2 0) 2048 64 0 64 32 32 2 0)",
                "dst": "(typed:signed-vec-widen-mul (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) (reg (bv #x00 8)) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vmpyh_128B_dsl ; hexagon_V6_vmpyh_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t2048\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_interleave_2_128B_dsl ; hexagon_V6_interleave_2_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t )\n\t32\n\t32\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t1\n\t0\n\t32\n\t1024\n\t1\n\t1\n\t16\n\t16\n\t2\n\t0\n )_ (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_vmpyh",
            "property": {
                "src": "(hexagon_V6_vmpyh_128B_dsl (hvx_swizzle_1_dsl (reg (bv #x00 8)) 1024 32 0 32 16 32 2 0) (hexagon_V6_interleave_2_128B_dsl (reg (bv #x01 8)) 16 32) 32 32 0 512 16 0 512 16 32 1 0 0 0 32 1024 0 0 16 16 2 0)",
                "dst": "(typed:unsigned-vec-widen-mul (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) (reg (bv #x00 8)) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vmpyh_128B_dsl ; hexagon_V6_vmpyh_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t2048\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_interleave_2_128B_dsl ; hexagon_V6_interleave_2_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t16\n\t\t32\n\t )\n\t32\n\t32\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t1\n\t0\n\t32\n\t1024\n\t1\n\t1\n\t16\n\t16\n\t2\n\t0\n )_ (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_vmpyh",
            "property": {
                "src": "(hexagon_V6_vmpyh_128B_dsl (hvx_swizzle_1_dsl (reg (bv #x00 8)) 1024 32 0 32 16 32 2 0) (hexagon_V6_interleave_2_128B_dsl (reg (bv #x01 8)) 16 32) 32 32 0 512 16 0 512 16 32 1 1 1 0 32 1024 1 1 16 16 2 0)",
                "dst": "(typed:signed-vec-widen-mul (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) (reg (bv #x00 8)) 16 1024)"
            }
        }
    ]
}
