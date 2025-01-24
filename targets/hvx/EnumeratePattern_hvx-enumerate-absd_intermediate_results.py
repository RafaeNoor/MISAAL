{
    " (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffub_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t-1\n\t0\n\t0\n )+ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+1024+hexagon_V6_vabsdiffuh_128B+typed:unsigned-vec-absd_p16_s1024_signed_0": [
        {
            "property_name": "EnumeratePattern_shift_right_w",
            "property": {
                "src": "(hexagon_V6_vabsdiffh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 -1 -1 0 0)",
                "dst": "(typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffub_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t-1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vabsdiffuh_128B",
                "dst_ctx": "typed:unsigned-vec-absd_p16_s1024_signed_0"
            }
        }
    ],
    " (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffub_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t-1\n\t0\n\t0\n )+ (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )+1024+hexagon_V6_vabsdiffub_128B+typed:unsigned-vec-absd_p8_s1024_signed_0": [
        {
            "property_name": "EnumeratePattern_shift_right_w",
            "property": {
                "src": "(hexagon_V6_vabsdiffh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 -1 -1 0 0)",
                "dst": "(typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffub_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t-1\n\t0\n\t0\n )",
                "original_dst_expr": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t8\n\t1024\n )",
                "src_ctx": "hexagon_V6_vabsdiffub_128B",
                "dst_ctx": "typed:unsigned-vec-absd_p8_s1024_signed_0"
            }
        }
    ]
}