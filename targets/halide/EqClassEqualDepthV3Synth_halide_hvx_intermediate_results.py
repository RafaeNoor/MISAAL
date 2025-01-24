{
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048)",
                "dst": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 0 0)"
            }
        }
    ],
    " (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1024\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x01 8)) 64 1024)",
                "dst": "(hexagon_V6_vcombine_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 0 1024 8 1024 0)"
            }
        },
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:concat_vectors (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024)",
                "dst": "(hexagon_V6_vcombine_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 8 0 1024 8 1024 0)"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 0 0)"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os2048_signed_None\n\t(buffer-index  0 'uint16 16) ; < 1 x i16> False\n\t16\n\t16\n\t128\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)"
            }
        },
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s2048_signed_1\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048)",
                "dst": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 1 0)"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "dst": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 -1 0)"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s2048_signed_1\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:signed-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 1 0)"
            }
        }
    ],
    " (typed:slice_vectors ; typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_0_1_64\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t0\n\t1\n\t64\n\t16\n\t2048\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:slice_vectors (reg (bv #x00 8)) 64 1 64 16 2048)",
                "dst": "(hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0)"
            }
        },
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:slice_vectors (reg (bv #x00 8)) 0 1 32 32 2048)",
                "dst": "(hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0)"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 -1 0)"
            }
        }
    ],
    " (typed:cast-int-extend ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1\n\t64\n\t32\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:cast-int-extend (reg (bv #x00 8)) 16 1 64 32)",
                "dst": "(hexagon_V6_vunpackh_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 32 1 1 0)"
            }
        }
    ],
    " (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1\n\t64\n\t32\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:cast-uint-extend (reg (bv #x00 8)) 16 1 64 32)",
                "dst": "(hexagon_V6_vunpackh_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 32 1 0 0)"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "dst": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 0 0)"
            }
        }
    ],
    " (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1024\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024)",
                "dst": "(typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024)"
            }
        },
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x01 8)) 64 1024)",
                "dst": "(typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024)"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 0 0)"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s2048_signed_1\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "dst": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 1 0)"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os2048_signed_None\n\t(buffer-index  0 'uint16 16) ; < 1 x i16> False\n\t16\n\t16\n\t128\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)"
            }
        },
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048)",
                "dst": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)"
            }
        }
    ],
    " (typed:slice_vectors ; typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_0_1_64\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t0\n\t1\n\t64\n\t16\n\t2048\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:slice_vectors (reg (bv #x00 8)) 64 1 64 16 2048)",
                "dst": "(hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0)"
            }
        },
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:slice_vectors (reg (bv #x00 8)) 16 1 16 64 2048)",
                "dst": "(hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0)"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s2048_signed_1\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:signed-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 1 0)"
            }
        }
    ],
    " (typed:cast-int-extend ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1\n\t64\n\t32\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:cast-int-extend (reg (bv #x00 8)) 16 1 64 32)",
                "dst": "(hexagon_V6_vunpackh_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 32 1 1 0)"
            }
        }
    ],
    " (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1\n\t64\n\t32\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:cast-uint-extend (reg (bv #x00 8)) 16 1 64 32)",
                "dst": "(hexagon_V6_vunpackh_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 32 1 0 0)"
            }
        }
    ],
    " (typed:cast-uint-truncate ; typed:cast-uint_1_ip16_is2048_op8_os1024_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t16\n\t1\n\t128\n\t8\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:cast-uint-truncate (reg (bv #x00 8)) 16 1 128 8)",
                "dst": "(hexagon_V6_vpackeh_128B_dsl (typed:slice_vectors (reg (bv #x00 8)) 128 1 128 8 2048) (typed:slice_vectors (reg (bv #x00 8)) 0 1 128 8 2048) 1024 1024 0 512 8 0 512 8 2 64 2 8 0)"
            }
        }
    ],
    " (typed:cast-int-truncate ; typed:cast-int_1_ip16_is2048_op8_os1024_signed_1\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t16\n\t1\n\t128\n\t8\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:cast-int-truncate (reg (bv #x00 8)) 32 1 64 16)",
                "dst": "(hexagon_V6_vpackeh_128B_dsl (typed:slice_vectors (reg (bv #x00 8)) 128 1 128 8 2048) (typed:slice_vectors (reg (bv #x00 8)) 0 1 64 16 2048) 1024 1024 0 512 16 0 512 16 2 32 2 16 0)"
            }
        }
    ],
    " (typed:vec-bwand ; typed:vec-bwand_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "dst": "(typed:concat_vectors (hexagon_V6_pred_and_128B_dsl (typed:slice_vectors (reg (bv #x01 8)) 64 1 64 16 2048) (typed:slice_vectors (reg (bv #x00 8)) 64 1 64 16 2048) 1024 1024 0 1024 16 0) (hexagon_V6_pred_and_128B_dsl (typed:slice_vectors (reg (bv #x00 8)) 0 1 64 16 2048) (typed:slice_vectors (reg (bv #x01 8)) 0 1 64 16 2048) 1024 1024 0 1024 16 0) 16 1024)"
            }
        }
    ],
    " (typed:signed-vec-max ; typed:signed-vec-max_p16_s2048_signed_1\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "dst": "(typed:concat_vectors (hexagon_V6_vmaxw_128B_dsl (typed:slice_vectors (reg (bv #x01 8)) 64 1 64 16 2048) (typed:slice_vectors (reg (bv #x00 8)) 64 1 64 16 2048) 1024 1024 0 1024 16 1 0) (hexagon_V6_vmaxw_128B_dsl (typed:slice_vectors (reg (bv #x01 8)) 0 1 64 16 2048) (typed:slice_vectors (reg (bv #x00 8)) 0 1 64 16 2048) 1024 1024 0 1024 16 1 0) 16 1024)"
            }
        }
    ],
    " (typed:signed-vec-min ; typed:signed-vec-min_p16_s2048_signed_1\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048)",
                "dst": "(typed:concat_vectors (hexagon_V6_vminuh_128B_dsl (typed:slice_vectors (reg (bv #x00 8)) 64 1 64 16 2048) (typed:slice_vectors (reg (bv #x01 8)) 64 1 64 16 2048) 1024 1024 0 1024 16 1 0) (hexagon_V6_vminuh_128B_dsl (typed:slice_vectors (reg (bv #x00 8)) 0 1 64 16 2048) (typed:slice_vectors (reg (bv #x01 8)) 0 1 64 16 2048) 1024 1024 0 1024 16 1 0) 16 1024)"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048)",
                "dst": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 2048 2048 0 2048 16 0 0)"
            }
        }
    ],
    " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 2048)",
                "dst": "(typed:concat_vectors (hexagon_V6_vmaxw_128B_dsl (typed:slice_vectors (reg (bv #x01 8)) 64 1 64 16 2048) (typed:slice_vectors (reg (bv #x00 8)) 64 1 64 16 2048) 1024 1024 0 1024 16 0 0) (hexagon_V6_vmaxw_128B_dsl (typed:slice_vectors (reg (bv #x00 8)) 0 1 64 16 2048) (typed:slice_vectors (reg (bv #x01 8)) 0 1 64 16 2048) 1024 1024 0 1024 16 0 0) 16 1024)"
            }
        }
    ],
    " (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1024\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024)",
                "dst": "(typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024)"
            }
        },
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x01 8)) 32 1024)",
                "dst": "(typed:concat_vectors (reg (bv #x00 8)) (reg (bv #x01 8)) 8 1024)"
            }
        }
    ],
    " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "dst": "(typed:concat_vectors (hexagon_V6_vminuh_128B_dsl (typed:slice_vectors (reg (bv #x00 8)) 64 1 64 16 2048) (typed:slice_vectors (reg (bv #x01 8)) 64 1 64 16 2048) 1024 1024 0 1024 16 0 0) (hexagon_V6_vminuh_128B_dsl (typed:slice_vectors (reg (bv #x00 8)) 0 1 64 16 2048) (typed:slice_vectors (reg (bv #x01 8)) 0 1 64 16 2048) 1024 1024 0 1024 16 0 0) 16 1024)"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is16_os2048_signed_None\n\t(buffer-index  0 'uint16 16) ; < 1 x i16> False\n\t16\n\t16\n\t128\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)"
            }
        },
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 128)"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s2048_signed_1\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> False\n\t16\n\t2048\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 2048)",
                "dst": "(hexagon_V6_vsubh_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 2048 2048 0 2048 16 1 0)"
            }
        }
    ],
    " (typed:slice_vectors ; typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_0_1_64\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t0\n\t1\n\t64\n\t16\n\t2048\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:slice_vectors (reg (bv #x00 8)) 64 1 64 16 2048)",
                "dst": "(hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0)"
            }
        },
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:slice_vectors (reg (bv #x00 8)) 0 1 64 16 2048)",
                "dst": "(hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0)"
            }
        }
    ],
    " (typed:cast-int-extend ; typed:cast-int_1_ip16_is1024_op32_os2048_signed_1\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1\n\t64\n\t32\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:cast-int-extend (reg (bv #x00 8)) 16 1 64 32)",
                "dst": "(hexagon_V6_vunpackh_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 32 1 1 0)"
            }
        }
    ],
    " (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is1024_op32_os2048_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> False\n\t16\n\t1\n\t64\n\t32\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:cast-uint-extend (reg (bv #x00 8)) 16 1 64 32)",
                "dst": "(hexagon_V6_vunpackh_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 32 1 0 0)"
            }
        }
    ],
    " (typed:cast-int-truncate ; typed:cast-int_1_ip16_is2048_op8_os1024_signed_1\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t16\n\t1\n\t128\n\t8\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:cast-int-truncate (reg (bv #x00 8)) 16 1 128 8)",
                "dst": "(hexagon_V6_vpackeh_128B_dsl (typed:slice_vectors (reg (bv #x00 8)) 128 1 128 8 2048) (typed:slice_vectors (reg (bv #x00 8)) 0 1 16 64 2048) 1024 1024 0 512 8 0 512 8 2 64 2 8 0)"
            }
        }
    ],
    " (typed:cast-uint-truncate ; typed:cast-uint_1_ip16_is2048_op8_os1024_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> False\n\t16\n\t1\n\t128\n\t8\n )+D3": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(typed:cast-uint-truncate (reg (bv #x00 8)) 16 1 128 8)",
                "dst": "(hexagon_V6_vpackeh_128B_dsl (typed:slice_vectors (reg (bv #x00 8)) 64 1 64 16 2048) (typed:slice_vectors (reg (bv #x00 8)) 0 1 32 32 2048) 1024 1024 0 512 8 0 512 8 2 64 2 8 0)"
            }
        }
    ]
}