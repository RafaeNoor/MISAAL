{
    " (_mm512_srav_epi16_dsl ; _mm512_srav_epi16\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(lit (bv #x000000000000ffff (bitvector 16)))\n\t(lit (bv #b1 (bitvector 1)))\n\t(lit (bv #x0000000000000010 (bitvector 16)))\n\t512\n\t512\n\t0\n\t512\n\t16\n\t0\n\t16\n\t16\n\t1\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_x86_shr",
            "property": {
                "src": "(_mm512_srav_epi16_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (reg (bv #x01 8)) (lit (bv #xffffffffffffffff 64)) (lit (bv #b1 1)) (lit (bv #x0000000000000040 64)) 512 512 0 512 64 0 64 64 1 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 64 512)"
            }
        }
    ]
}