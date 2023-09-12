{
    " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-mod ; typed:signed-vec-mod_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-mod ; typed:signed-vec-mod_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:concat_vectors ; typed:concat_vectors_ip8_is1024_op8_os2048_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:concat_vectors ; typed:concat_vectors_ip8_is1024_op8_os2048_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:concat_vectors ; typed:concat_vectors_ip8_is1024_op8_os2048_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:concat_vectors ; typed:concat_vectors_ip8_is1024_op8_os2048_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-abs ; typed:signed-vec-abs_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-abs ; typed:signed-vec-abs_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vabsh_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  8  1  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p32_s2048_signed_None\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-add ; typed:vec-add_p32_s2048_signed_None\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 0)  2048  2048  0  2048  32  -1  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p32_s2048_signed_None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-add ; typed:vec-add_p32_s2048_signed_None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  2048  2048  0  2048  32  -1  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  2048  2048  0  2048  8  1  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vmaxw_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  0  0  );<64 x i16>\n  \n(hexagon_V6_vmaxw_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s2048_signed_1\n\t(buffer-index  0 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s2048_signed_1\n\t(buffer-index  0 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 0)  2048  2048  0  2048  8  1  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s2048_signed_0\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s2048_signed_0\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  8  0  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-sub ; typed:vec-sub_p16_s1024_signed_None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmpybv_acc_128B_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048)) ; <128 x i16>\n  \n(interleave-vector_dsl \n(reg 0)  1024  8  );<128 x i8>\n  \n(interleave-vector_dsl \n(reg 1)  1024  8  );<128 x i8>\n  1024  1024  0  512  8  0  512  8  16  1  -1  0  0  16  -1  0  0  8  1024  2  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vshuffeb_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(hexagon_V6_vmpybv_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  512  8  0  512  8  16  1  0  0  16  1024  0  0  8  2  0  );<128 x i16>\n  1024  1024  0  1024  8  1024  0  );<64 x i16>\n  \n(hexagon_V6_vassign_128B_dsl \n(hexagon_V6_vmpybv_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  512  8  0  512  8  16  1  0  0  16  1024  0  0  8  2  0  );<128 x i16>\n  1024  1024  0  1024  8  0  );<64 x i16>\n  1024  1024  0  512  8  8  2  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmpybv_acc_128B_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048)) ; <128 x i16>\n  \n(interleave-vector_dsl \n(reg 1)  1024  8  );<128 x i8>\n  \n(interleave-vector_dsl \n(reg 1)  1024  8  );<128 x i8>\n  1024  1024  0  512  8  0  512  8  16  1  -1  0  0  16  -1  0  0  8  1024  2  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  8  0  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:signed-vec-max ; typed:signed-vec-max_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-max ; typed:signed-vec-max_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmaxw_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  32  1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-max ; typed:signed-vec-max_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-max ; typed:signed-vec-max_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:vec-shl ; typed:vec-shl_p32_s2048_signed_None\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-shl ; typed:vec-shl_p32_s2048_signed_None\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vaslhv_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  \n(hexagon_V6_vaslhv_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmpybv_acc_128B_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048)) ; <128 x i16>\n  \n(interleave-vector_dsl \n(reg 0)  1024  8  );<128 x i8>\n  \n(interleave-vector_dsl \n(reg 1)  1024  8  );<128 x i8>\n  1024  1024  0  512  8  0  512  8  16  1  -1  1  1  16  -1  1  1  8  1024  2  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x00000001 32)) ; <1 x i32>\n  (lit (bv #x00000002 32)) ; <1 x i32>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  32  1  -1  -1  0  );<32 x i32>\n  \n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x00000001 32)) ; <1 x i32>\n  (lit (bv #x00000002 32)) ; <1 x i32>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  32  1  -1  -1  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:concat_vectors ; typed:concat_vectors_ip32_is1024_op32_os2048_signed_None\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:concat_vectors ; typed:concat_vectors_ip32_is1024_op32_os2048_signed_None\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:concat_vectors ; typed:concat_vectors_ip32_is1024_op32_os2048_signed_None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:concat_vectors ; typed:concat_vectors_ip32_is1024_op32_os2048_signed_None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmpybv_acc_128B_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048)) ; <128 x i16>\n  \n(interleave-vector_dsl \n(reg 1)  1024  8  );<128 x i8>\n  \n(interleave-vector_dsl \n(reg 1)  1024  8  );<128 x i8>\n  1024  1024  0  512  8  0  512  8  16  1  -1  1  1  16  -1  1  1  8  1024  2  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vshuffeb_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(hexagon_V6_vmpybv_acc_128B_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048)) ; <64 x i32>\n  \n(reg 1)  \n(reg 1)  1024  1024  0  512  16  0  512  16  32  1  -1  0  0  32  -1  0  0  16  1024  2  0  );<64 x i32>\n  1024  1024  0  1024  8  1024  0  );<32 x i32>\n  \n(hexagon_V6_vassign_128B_dsl \n(hexagon_V6_vmpybv_acc_128B_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048)) ; <64 x i32>\n  \n(reg 1)  \n(reg 1)  1024  1024  0  512  16  0  512  16  32  1  -1  0  0  32  -1  0  0  16  1024  2  0  );<64 x i32>\n  1024  1024  0  1024  8  0  );<32 x i32>\n  1024  1024  0  512  16  16  2  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p32_s1024_signed_0\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p32_s1024_signed_0\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  32  0  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  32  0  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s2048_signed_0\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s2048_signed_0\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vminuh_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  8  0  0  );<128 x i8>\n  \n(hexagon_V6_vminuh_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  8  0  0  );<128 x i8>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-mul ; typed:unsigned-vec-mul_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vshuffeb_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(hexagon_V6_vmpybv_acc_128B_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048)) ; <64 x i32>\n  \n(reg 1)  \n(reg 0)  1024  1024  0  512  16  0  512  16  32  1  -1  0  0  32  -1  0  0  16  1024  2  0  );<64 x i32>\n  1024  1024  0  1024  8  1024  0  );<32 x i32>\n  \n(hexagon_V6_vassign_128B_dsl \n(hexagon_V6_vmpybv_acc_128B_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048)) ; <64 x i32>\n  \n(reg 0)  \n(reg 1)  1024  1024  0  512  16  0  512  16  32  1  -1  0  0  32  -1  0  0  16  1024  2  0  );<64 x i32>\n  1024  1024  0  1024  8  0  );<32 x i32>\n  1024  1024  0  512  16  16  2  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:vec-shl ; typed:vec-shl_p32_s2048_signed_None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-shl ; typed:vec-shl_p32_s2048_signed_None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vaslhv_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  \n(hexagon_V6_vaslhv_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-absd ; typed:signed-vec-absd_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-absd ; typed:signed-vec-absd_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-absd ; typed:signed-vec-absd_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-absd ; typed:signed-vec-absd_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vabsdiffh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  -1  -1  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x01 8)) ; <1 x i8>\n  (lit (bv #x02 8)) ; <1 x i8>\n  \n(reg 1)  \n(reg 1)  1024  1024  0  1024  8  1  -1  -1  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x01 8)) ; <1 x i8>\n  (lit (bv #x02 8)) ; <1 x i8>\n  \n(reg 1)  \n(reg 0)  1024  1024  0  1024  8  1  -1  -1  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-max ; typed:signed-vec-max_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-max ; typed:signed-vec-max_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-max ; typed:signed-vec-max_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-max ; typed:signed-vec-max_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmaxw_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  8  1  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p16_s2048_signed_None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-sub ; typed:vec-sub_p16_s2048_signed_None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-sub ; typed:vec-sub_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  16  -1  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  8  0  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  16  1  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:vec-bwnot ; typed:vec-bwnot_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwnot ; typed:vec-bwnot_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:vec-bwand ; typed:vec-bwand_p16_s2048_signed_None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwand ; typed:vec-bwand_p16_s2048_signed_None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-shr ; typed:signed-vec-shr_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-shr ; typed:signed-vec-shr_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vasrhv_128B_dsl \n(reg 1)  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(reg 0)  1024  1024  0  1024  32  1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  8  0  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  2048  2048  0  2048  32  1  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 0)  2048  2048  0  2048  32  1  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vabsdiffh_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  16  -1  -1  0  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:vec-bwand ; typed:vec-bwand_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwand ; typed:vec-bwand_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_pred_and_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_pred_and_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:concat_vectors ; typed:concat_vectors_ip16_is1024_op16_os2048_signed_None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwnot ; typed:vec-bwnot_p32_s1024_signed_None\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vnot_128B_dsl \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:vec-bwand ; typed:vec-bwand_p8_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwand ; typed:vec-bwand_p8_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_pred_and_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:vec-bwand ; typed:vec-bwand_p8_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwand ; typed:vec-bwand_p8_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is32_os2048_signed_None\n\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t32\n\t32\n\t64\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:xBroadcast ; typed:xBroadcast_is32_os2048_signed_None\n\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t32\n\t32\n\t64\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_lvsplatw_128B_dsl \n(reg 0)  1024  1024  0  1024  32  0  );<32 x i32>\n  \n(hexagon_V6_lvsplatw_128B_dsl \n(reg 0)  1024  1024  0  1024  32  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p8_s2048_signed_None\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-add ; typed:vec-add_p8_s2048_signed_None\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  8  -1  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-min ; typed:signed-vec-min_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-min ; typed:signed-vec-min_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vminuh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  32  1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p8_s2048_signed_None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-add ; typed:vec-add_p8_s2048_signed_None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  2048  2048  0  2048  8  -1  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-min ; typed:signed-vec-min_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-min ; typed:signed-vec-min_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-mod ; typed:signed-vec-mod_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-mod ; typed:signed-vec-mod_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:signed-vec-abs ; typed:signed-vec-abs_p8_s2048_signed_1\n\t(buffer-index  0 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-abs ; typed:signed-vec-abs_p8_s2048_signed_1\n\t(buffer-index  0 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vabsh_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vabsh_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  16  0  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwnot ; typed:vec-bwnot_p16_s1024_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vnot_128B_dsl \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:vec-bwand ; typed:vec-bwand_p32_s2048_signed_None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwand ; typed:vec-bwand_p32_s2048_signed_None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:vec-bwand ; typed:vec-bwand_p32_s2048_signed_None\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwand ; typed:vec-bwand_p32_s2048_signed_None\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_pred_and_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_pred_and_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  16  0  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  2048  2048  0  2048  16  0  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:slice_vectors ; typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_0_1_32\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t0\n\t1\n\t32\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:slice_vectors ; typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_0_1_32\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t0\n\t1\n\t32\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaslhv_128B_dsl \n(reg 1)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-shl ; typed:vec-shl_p16_s1024_signed_None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaslhv_128B_dsl \n(reg 1)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 1)  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:vec-bwnot ; typed:vec-bwnot_p32_s2048_signed_None\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwnot ; typed:vec-bwnot_p32_s2048_signed_None\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-min ; typed:signed-vec-min_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vminuh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p32_s2048_signed_0\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p32_s2048_signed_0\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  32  0  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  2048  2048  0  2048  32  0  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-absd ; typed:signed-vec-absd_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-absd ; typed:signed-vec-absd_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:signed-vec-max ; typed:signed-vec-max_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-max ; typed:signed-vec-max_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  32  1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  32  1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-mod ; typed:signed-vec-mod_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-mod ; typed:signed-vec-mod_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vabsdiffh_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  8  -1  -1  0  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmpybv_acc_128B_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048)) ; <64 x i32>\n  \n(interleave-vector_dsl \n(reg 1)  1024  16  );<64 x i16>\n  \n(interleave-vector_dsl \n(reg 1)  1024  16  );<64 x i16>\n  1024  1024  0  512  16  0  512  16  32  1  -1  1  1  32  -1  1  1  16  1024  2  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-absd ; typed:signed-vec-absd_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-absd ; typed:signed-vec-absd_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vabsdiffh_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  32  -1  -1  1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmpybv_acc_128B_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048)) ; <64 x i32>\n  \n(interleave-vector_dsl \n(reg 0)  1024  16  );<64 x i16>\n  \n(interleave-vector_dsl \n(reg 1)  1024  16  );<64 x i16>\n  1024  1024  0  512  16  0  512  16  32  1  -1  1  1  32  -1  1  1  16  1024  2  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-absd ; typed:signed-vec-absd_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-absd ; typed:signed-vec-absd_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:signed-vec-absd ; typed:signed-vec-absd_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-absd ; typed:signed-vec-absd_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:slice_vectors ; typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_32_1_32\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t32\n\t1\n\t32\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:slice_vectors ; typed:slice_vectors_ip32_is2048_op32_os1024_signed_None_32_1_32\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t32\n\t1\n\t32\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s2048_signed_0\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s2048_signed_0\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vmaxw_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  8  0  0  );<128 x i8>\n  \n(hexagon_V6_vmaxw_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  8  0  0  );<128 x i8>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-max ; typed:signed-vec-max_p8_s2048_signed_1\n\t(buffer-index  0 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-max ; typed:signed-vec-max_p8_s2048_signed_1\n\t(buffer-index  0 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vmaxw_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  8  1  0  );<128 x i8>\n  \n(hexagon_V6_vmaxw_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  8  1  0  );<128 x i8>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-absd ; typed:signed-vec-absd_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-absd ; typed:signed-vec-absd_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vabsdiffh_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  32  -1  -1  1  0  );<32 x i32>\n  \n(hexagon_V6_vabsdiffh_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  32  -1  -1  1  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s2048_signed_0\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s2048_signed_0\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  32  0  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-min ; typed:signed-vec-min_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-min ; typed:signed-vec-min_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-min ; typed:signed-vec-min_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-min ; typed:signed-vec-min_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vminuh_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  8  1  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x01 8)) ; <1 x i8>\n  (lit (bv #x02 8)) ; <1 x i8>\n  \n(reg 0)  \n(reg 1)  1024  1024  0  1024  8  0  -1  -1  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  16  0  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  32  1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  16  0  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p8_s2048_signed_None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-sub ; typed:vec-sub_p8_s2048_signed_None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:signed-vec-mod ; typed:signed-vec-mod_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-mod ; typed:signed-vec-mod_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:slice_vectors ; typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_128_1_128\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> None\n\t128\n\t1\n\t128\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:slice_vectors ; typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_128_1_128\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> None\n\t128\n\t1\n\t128\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p8_s2048_signed_None\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-sub ; typed:vec-sub_p8_s2048_signed_None\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  8  -1  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:vec-bwnot ; typed:vec-bwnot_p8_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwnot ; typed:vec-bwnot_p8_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vnot_128B_dsl \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmpybv_acc_128B_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048)) ; <64 x i32>\n  \n(interleave-vector_dsl \n(reg 1)  1024  16  );<64 x i16>\n  \n(interleave-vector_dsl \n(reg 1)  1024  16  );<64 x i16>\n  1024  1024  0  512  16  0  512  16  32  1  -1  0  0  32  -1  0  0  16  1024  2  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-widen-mul ; typed:unsigned-vec-widen-mul_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmpybv_acc_128B_dsl (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048)) ; <64 x i32>\n  \n(interleave-vector_dsl \n(reg 0)  1024  16  );<64 x i16>\n  \n(interleave-vector_dsl \n(reg 1)  1024  16  );<64 x i16>\n  1024  1024  0  512  16  0  512  16  32  1  -1  0  0  32  -1  0  0  16  1024  2  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:vec-bwand ; typed:vec-bwand_p8_s2048_signed_None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwand ; typed:vec-bwand_p8_s2048_signed_None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:vec-bwand ; typed:vec-bwand_p32_s1024_signed_None\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwand ; typed:vec-bwand_p32_s1024_signed_None\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_pred_and_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:vec-bwand ; typed:vec-bwand_p32_s1024_signed_None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwand ; typed:vec-bwand_p32_s1024_signed_None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vminuh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  0  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vmpyih_acc_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <64 x i16>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  -1  1  32  1  32  1  0  );<64 x i16>\n  \n(hexagon_V6_vmpyih_acc_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <64 x i16>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  -1  1  32  1  32  1  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  32  1  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:vec-bwand ; typed:vec-bwand_p8_s2048_signed_None\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwand ; typed:vec-bwand_p8_s2048_signed_None\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> None\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_pred_and_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_pred_and_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmpyih_acc_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <64 x i16>\n  \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  -1  1  32  1  32  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-mod ; typed:signed-vec-mod_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-mod ; typed:signed-vec-mod_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vmpyih_acc_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <64 x i16>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  -1  1  32  1  32  1  0  );<64 x i16>\n  \n(hexagon_V6_vmpyih_acc_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <64 x i16>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  -1  1  32  1  32  1  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-mul ; typed:signed-vec-mul_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmpyih_acc_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <64 x i16>\n  \n(reg 1)  \n(reg 1)  1024  1024  0  1024  16  -1  1  32  1  32  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:xBroadcast ; typed:xBroadcast_is32_os1024_signed_None\n\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t32\n\t32\n\t32\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:xBroadcast ; typed:xBroadcast_is32_os1024_signed_None\n\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t32\n\t32\n\t32\n )",
                "simplified": "\n(hexagon_V6_lvsplatw_128B_dsl \n(reg 0)  1024  1024  0  1024  32  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s2048_signed_0\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s2048_signed_0\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x00000001 32)) ; <1 x i32>\n  (lit (bv #x00000002 32)) ; <1 x i32>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  32  0  -1  -1  0  );<32 x i32>\n  \n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x00000001 32)) ; <1 x i32>\n  (lit (bv #x00000002 32)) ; <1 x i32>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  32  0  -1  -1  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-min ; typed:signed-vec-min_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-min ; typed:signed-vec-min_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-min ; typed:signed-vec-min_p8_s2048_signed_1\n\t(buffer-index  0 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-min ; typed:signed-vec-min_p8_s2048_signed_1\n\t(buffer-index  0 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vminuh_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  8  1  0  );<128 x i8>\n  \n(hexagon_V6_vminuh_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  8  1  0  );<128 x i8>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:slice_vectors ; typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_0_1_128\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> None\n\t0\n\t1\n\t128\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:slice_vectors ; typed:slice_vectors_ip8_is2048_op8_os1024_signed_None_0_1_128\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> None\n\t0\n\t1\n\t128\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-sub ; typed:vec-sub_p8_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  8  -1  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p8_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-add ; typed:vec-add_p8_s1024_signed_None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  8  -1  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p8_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-add ; typed:vec-add_p8_s1024_signed_None\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> None\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> None\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  8  -1  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-max ; typed:signed-vec-max_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-max ; typed:signed-vec-max_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  32  -1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-add ; typed:vec-add_p32_s1024_signed_None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  32  -1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p32_s2048_signed_None\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-sub ; typed:vec-sub_p32_s2048_signed_None\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  32  -1  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p32_s2048_signed_None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-sub ; typed:vec-sub_p32_s2048_signed_None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> None\n\t32\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:signed-vec-mod ; typed:signed-vec-mod_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-mod ; typed:signed-vec-mod_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  2048  2048  0  2048  16  1  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 0)  2048  2048  0  2048  16  1  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-max ; typed:signed-vec-max_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-max ; typed:signed-vec-max_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vmaxw_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vmaxw_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-absd ; typed:unsigned-vec-absd_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:signed-vec-abs ; typed:signed-vec-abs_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-abs ; typed:signed-vec-abs_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vabsh_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vabsh_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s2048_signed_1\n\t(buffer-index  0 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s2048_signed_1\n\t(buffer-index  0 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  8  1  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-sub ; typed:signed-vec-sat-sub_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) ; <1 x i16>\n  (lit (bv #x0002 16)) ; <1 x i16>\n  \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  0  -1  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-min ; typed:signed-vec-min_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-min ; typed:signed-vec-min_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-min ; typed:signed-vec-min_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-min ; typed:signed-vec-min_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-min ; typed:signed-vec-min_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-min ; typed:signed-vec-min_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vminuh_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  \n(hexagon_V6_vminuh_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-min ; typed:signed-vec-min_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-min ; typed:signed-vec-min_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vminuh_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vminuh_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmaxw_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  8  0  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmaxw_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  16  0  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-max ; typed:unsigned-vec-max_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s1024_signed_0\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s1024_signed_0\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vlsrwv_128B_dsl \n(reg 1)  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(reg 0)  1024  1024  0  1024  32  1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vmaxw_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s2048_signed_1\n\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vasrhv_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vasrhv_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:slice_vectors ; typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_64_1_64\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t64\n\t1\n\t64\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:slice_vectors ; typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_64_1_64\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t64\n\t1\n\t64\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-max ; typed:signed-vec-max_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-absd ; typed:signed-vec-absd_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-absd ; typed:signed-vec-absd_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:slice_vectors ; typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_0_1_64\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t0\n\t1\n\t64\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:slice_vectors ; typed:slice_vectors_ip16_is2048_op16_os1024_signed_None_0_1_64\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t0\n\t1\n\t64\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-shr ; typed:signed-vec-shr_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-shr ; typed:signed-vec-shr_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vasrhv_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  \n(hexagon_V6_vasrhv_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-halving_add ; typed:signed-vec-halving_add_p16_s2048_signed_1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t(buffer-index  1 'int16 2048) ; < 128 x i16> 1\n\t16\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-absd ; typed:signed-vec-absd_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-absd ; typed:signed-vec-absd_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(hexagon_V6_vmaxw_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  8  1  0  );<128 x i8>\n  \n(hexagon_V6_vminuh_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  8  1  0  );<128 x i8>\n  1024  1024  0  1024  8  -1  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:vec-shl ; typed:vec-shl_p32_s1024_signed_None\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-shl ; typed:vec-shl_p32_s1024_signed_None\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaslhv_128B_dsl \n(reg 1)  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(reg 0)  1024  1024  0  1024  32  1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p8_s1024_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vminuh_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  8  0  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:vec-shl ; typed:vec-shl_p32_s1024_signed_None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-shl ; typed:vec-shl_p32_s1024_signed_None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaslhv_128B_dsl \n(reg 1)  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(reg 1)  1024  1024  0  1024  32  1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:vec-bwnot ; typed:vec-bwnot_p8_s2048_signed_None\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwnot ; typed:vec-bwnot_p8_s2048_signed_None\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> None\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_pred_and_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-bwand ; typed:vec-bwand_p16_s1024_signed_None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t16\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s2048_signed_0\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p32_s2048_signed_0\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vlsrwv_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  \n(hexagon_V6_vlsrwv_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-abs ; typed:signed-vec-abs_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-abs ; typed:signed-vec-abs_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vabsh_128B_dsl \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-absd ; typed:signed-vec-absd_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-absd ; typed:signed-vec-absd_p8_s2048_signed_1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t(buffer-index  1 'int8 2048) ; < 256 x i8> 1\n\t8\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  32  -1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-min ; typed:unsigned-vec-min_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vminuh_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  0  0  );<64 x i16>\n  \n(hexagon_V6_vminuh_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  32  0  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-sub ; typed:vec-sub_p32_s1024_signed_None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> None\n\t32\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p8_s1024_signed_0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t8\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:signed-vec-shr ; typed:signed-vec-shr_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-shr ; typed:signed-vec-shr_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vasrhv_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  \n(hexagon_V6_vasrhv_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  (lit (bv #x00000000 32)) ; <1 x i32>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  8  1  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-sat-add ; typed:signed-vec-sat-add_p8_s1024_signed_1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t(buffer-index  1 'int8 1024) ; < 128 x i8> 1\n\t8\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  8  1  0  );<128 x i8>\n"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-add ; typed:vec-add_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  16  -1  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:vec-add ; typed:vec-add_p16_s2048_signed_None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-add ; typed:vec-add_p16_s2048_signed_None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  2048  2048  0  2048  16  -1  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s2048_signed_0\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vlsrwv_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vlsrwv_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s1024_signed_0\n\t(buffer-index  0 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x00000001 32)) ; <1 x i32>\n  (lit (bv #x00000002 32)) ; <1 x i32>\n  \n(reg 1)  \n(reg 0)  1024  1024  0  1024  32  0  -1  -1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-rounding_halving_add ; typed:unsigned-vec-rounding_halving_add_p32_s1024_signed_0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t(buffer-index  1 'uint32 1024) ; < 32 x i32> 0\n\t32\n\t1024\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:signed-vec-max ; typed:signed-vec-max_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-max ; typed:signed-vec-max_p32_s2048_signed_1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-mod ; typed:unsigned-vec-mod_p32_s2048_signed_0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t(buffer-index  1 'uint32 2048) ; < 64 x i32> 0\n\t32\n\t2048\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-sub ; typed:unsigned-vec-sat-sub_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  0  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vasrhv_128B_dsl \n(reg 1)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s2048_signed_0\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s2048_signed_0\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  8  0  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-sat-add ; typed:unsigned-vec-sat-add_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  2048  2048  0  2048  8  0  0  );<256 x i8>\n"
            }
        }
    ],
    " (typed:signed-vec-max ; typed:signed-vec-max_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-max ; typed:signed-vec-max_p32_s2048_signed_1\n\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t(buffer-index  1 'int32 2048) ; < 64 x i32> 1\n\t32\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vmaxw_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  \n(hexagon_V6_vmaxw_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  32  1  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<64 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p16_s1024_signed_1\n\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) ; <1 x i16>\n  (lit (bv #x0002 16)) ; <1 x i16>\n  \n(reg 1)  \n(reg 0)  1024  1024  0  1024  16  1  -1  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p16_s1024_signed_1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) ; <1 x i16>\n  (lit (bv #x0002 16)) ; <1 x i16>\n  \n(reg 1)  \n(reg 1)  1024  1024  0  1024  16  1  -1  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p8_s2048_signed_0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t(buffer-index  1 'uint8 2048) ; < 256 x i8> 0\n\t8\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p32_s1024_signed_1\n\t(buffer-index  0 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x00000001 32)) ; <1 x i32>\n  (lit (bv #x00000002 32)) ; <1 x i32>\n  \n(reg 1)  \n(reg 0)  1024  1024  0  1024  32  1  -1  -1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:signed-vec-rounding_halving_add ; typed:signed-vec-rounding_halving_add_p32_s1024_signed_1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t(buffer-index  1 'int32 1024) ; < 32 x i32> 1\n\t32\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x00000001 32)) ; <1 x i32>\n  (lit (bv #x00000002 32)) ; <1 x i32>\n  \n(reg 1)  \n(reg 1)  1024  1024  0  1024  32  1  -1  -1  0  );<32 x i32>\n"
            }
        }
    ],
    " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "\n(hexagon_V6_vlsrwv_128B_dsl \n(reg 1)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-shr ; typed:unsigned-vec-shr_p16_s1024_signed_0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t16\n\t1024\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:unsigned-vec-halving_add ; typed:unsigned-vec-halving_add_p16_s2048_signed_0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t16\n\t2048\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (typed:vec-shl ; typed:vec-shl_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-shl ; typed:vec-shl_p16_s2048_signed_None\n\t(buffer-index  0 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vaslhv_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vaslhv_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (typed:vec-shl ; typed:vec-shl_p16_s2048_signed_None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (typed:vec-shl ; typed:vec-shl_p16_s2048_signed_None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t16\n\t2048\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vaslhv_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vaslhv_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ]
}