{
    " (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_128B\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t1\n\t0\n )+ (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s4096_signed_None_reduce_4\n\t4\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s1024_signed_1\n\t\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t\t8\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t32\n\t4096\n )+1024+hexagon_V6_vrmpybv_128B+typed:signed-vector_reduce_add_p32_s4096_signed_None_reduce_4": [
        {
            "property_name": "EnumeratePatternhvx_rmpy",
            "property": {
                "src": "(hexagon_V6_vrmpybv_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 32 0 32 8 -1 1 1 16 1 0)",
                "dst": "(typed:signed-vector_reduce_add 4 (typed:cast-int-extend (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 16 1 128 32) 32 4096)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_128B\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s4096_signed_None_reduce_4\n\t4\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s1024_signed_1\n\t\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t\t8\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t32\n\t4096\n )",
                "src_ctx": "hexagon_V6_vrmpybv_128B",
                "dst_ctx": "typed:signed-vector_reduce_add_p32_s4096_signed_None_reduce_4"
            }
        }
    ],

    "1 (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_128B\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t1\n\t0\n )+ (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s4096_signed_None_reduce_4\n\t4\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s1024_signed_1\n\t\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t\t8\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t32\n\t4096\n )+1024+hexagon_V6_vrmpybv_128B+typed:signed-vector_reduce_add_p32_s4096_signed_None_reduce_4": [
        {
            "property_name": "EnumeratePatternhvx_rmpy",
            "property": {
                "src": "(hexagon_V6_vrmpybv_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 32 0 32 8 -1 1 1 16 1 0)",
                "dst": "(typed:signed-vector_reduce_add 4 (typed:cast-uint-extend (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 16 1 128 32) 32 4096)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_128B\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s4096_signed_None_reduce_4\n\t4\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s1024_signed_1\n\t\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t\t8\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t32\n\t4096\n )",
                "src_ctx": "hexagon_V6_vrmpybv_128B",
                "dst_ctx": "typed:signed-vector_reduce_add_p32_s4096_signed_None_reduce_4"
            }
        }
    ],

    "2 (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_128B\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t1\n\t0\n )+ (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s4096_signed_None_reduce_4\n\t4\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s1024_signed_1\n\t\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t\t8\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t32\n\t4096\n )+1024+hexagon_V6_vrmpybv_128B+typed:signed-vector_reduce_add_p32_s4096_signed_None_reduce_4": [
        {
            "property_name": "EnumeratePatternhvx_rmpy",
            "property": {
                "src": "(hexagon_V6_vrmpybv_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 32 0 32 8 -1 1 1 16 1 0)",
                "dst": "(typed:signed-vector_reduce_add 4 (typed:cast-int-extend (typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 16 1 128 32) 32 4096)",
                "output_size": 1024,
                "original_src_expr": " (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_128B\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t1\n\t0\n )",
                "original_dst_expr": " (typed:signed-vector_reduce_add ; typed:signed-vector_reduce_add_p32_s4096_signed_None_reduce_4\n\t4\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s1024_signed_1\n\t\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> False\n\t\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t\t\t8\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t32\n\t4096\n )",
                "src_ctx": "hexagon_V6_vrmpybv_128B",
                "dst_ctx": "typed:signed-vector_reduce_add_p32_s4096_signed_None_reduce_4"
            }
        }
    ]
}
