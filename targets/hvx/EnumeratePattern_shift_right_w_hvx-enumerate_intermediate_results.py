{
    " (hexagon_V6_vlsrw_128B_dsl ; hexagon_V6_vlsrw_128B\n\t(lit (bv #x0000001f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )+ (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is32_os1024_signed_None\n\t\t(buffer-index  1 'uint8 32) ; < 4 x i8> False\n\t\t32\n\t\t32\n\t\t32\n\t )\n\t32\n\t1024\n )+1024+hexagon_V6_vlsrw_128B+typed:unsigned-vec-shr_p32_s1024_signed_0": [
        {
            "property_name": "EnumeratePattern_shift_right_w",
            "property": {
                "src": "(hexagon_V6_vlsrw_128B_dsl (lit (bv #x0000001f 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 0)",
                "dst": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 32 32 32) 32 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vlsrw_128B_dsl ; hexagon_V6_vlsrw_128B\n\t(lit (bv #x0000001f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 4 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is32_os1024_signed_None\n\t\t(buffer-index  1 'uint8 32) ; < 4 x i8> False\n\t\t32\n\t\t32\n\t\t32\n\t )\n\t32\n\t1024\n )",
                "src_ctx": "hexagon_V6_vlsrw_128B",
                "dst_ctx": "typed:unsigned-vec-shr_p32_s1024_signed_0"
            }
        }
    ]
}