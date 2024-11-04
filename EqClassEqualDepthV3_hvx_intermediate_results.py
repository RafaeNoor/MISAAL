{
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x01 8)) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) (reg (bv #x00 8)) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x00 8)) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) (reg (bv #x01 8)) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 1024) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (reg (bv #x00 8)) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) 64 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-min (reg (bv #x00 8)) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) 64 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 64 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) 64 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:unsigned-vec-min (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-min (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 1 0)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 1 0)",
                "dst": "(typed:signed-vec-min (reg (bv #x00 8)) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:signed-vec-min (reg (bv #x01 8)) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) (reg (bv #x01 8)) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:signed-vec-min (reg (bv #x00 8)) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 1024) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) (reg (bv #x00 8)) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:unsigned-vec-max (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) 64 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:unsigned-vec-max (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 1 0)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) (reg (bv #x01 8)) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:signed-vec-min (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 8 1024) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 8 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) (reg (bv #x00 8)) 16 1024) 64 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 1 0)",
                "dst": "(typed:signed-vec-min (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 32 1024) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 8 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) 16 1024) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 1024) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) 8 1024) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) (reg (bv #x00 8)) 16 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) 64 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-sat-sub (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 1024) 8 1024) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) 8 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-sat-sub (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) (reg (bv #x00 8)) 16 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) (reg (bv #x00 8)) 16 1024) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) 64 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) 16 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 32 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  5 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) 8 1024) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) 16 1024) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t\t(buffer-index  5 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  6 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 1024) 16 1024) (typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024) 8 1024) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t\t(buffer-index  5 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  6 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) 64 1024) (typed:unsigned-vec-sat-sub (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 1024) 16 1024) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  5 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 8 1024) (typed:unsigned-vec-min (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) 64 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t\t(buffer-index  5 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  6 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024) 64 1024) (typed:unsigned-vec-min (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 1024) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024) 32 1024) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )_ (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t\t (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t\t\t(buffer-index  5 'uint16 1024) ; < 64 x i16> False\n\t\t\t(buffer-index  6 'uint16 1024) ; < 64 x i16> False\n\t\t\t16\n\t\t\t1024\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV3",
            "property": {
                "src": "(hexagon_V6_vminuh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0 0)",
                "dst": "(typed:unsigned-vec-sat-sub (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) 64 1024) (typed:unsigned-vec-min (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 1024) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 1024) 16 1024) 16 1024)"
            }
        }
    ]
}