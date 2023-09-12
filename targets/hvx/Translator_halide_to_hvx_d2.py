{
    " (vec-max ; vec-max_p16_s2048_signed_0\n\t (cast-uint ; cast-uint_ip8_is1024_op16_os2048_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t\t128\n\t\t16\n\t )\n\t (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-max ; vec-max_p16_s2048_signed_0\n\t (cast-uint ; cast-uint_ip8_is1024_op16_os2048_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t\t128\n\t\t16\n\t )\n\t (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vunpackh_128B_dsl \n(reg 0)  1024  1024  0  1024  8  16  1  0  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) ; <1 x i16>\n  (lit (bv #x0002 16)) ; <1 x i16>\n  \n(reg 1)  \n(reg 0)  1024  1024  0  1024  16  0  -1  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vnot_128B_dsl \n(reg 1)  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_vlsrwv_128B_dsl \n(reg 1)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vnot_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <64 x i16>\n  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) ; <1 x i16>\n  (lit (bv #x0002 16)) ; <1 x i16>\n  \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  0  -1  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  0  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(reg 1)  1024  1024  0  1024  16  0  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) ; <1 x i16>\n  (lit (bv #x0002 16)) ; <1 x i16>\n  \n(reg 2)  \n(reg 0)  1024  1024  0  1024  16  0  -1  -1  0  );<64 x i16>\n  \n(hexagon_V6_vnot_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  16  0  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) ; <1 x i16>\n  (lit (bv #x0002 16)) ; <1 x i16>\n  \n(reg 1)  \n(reg 2)  1024  1024  0  1024  16  0  -1  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  0  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-sat-add ; vec-sat-add_p16_s2048_signed_0\n\t (vec-shr ; vec-shr_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (cast-int ; cast-int_ip8_is1024_op16_os2048_signed_1\n\t\t(buffer-index  2 'int8 1024) ; < 128 x i8> 1\n\t\t128\n\t\t16\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-add ; vec-sat-add_p16_s2048_signed_0\n\t (vec-shr ; vec-shr_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (cast-int ; cast-int_ip8_is1024_op16_os2048_signed_1\n\t\t(buffer-index  2 'int8 1024) ; < 128 x i8> 1\n\t\t128\n\t\t16\n\t )\n )",
                "simplified": "\n(hexagon_V6_vunpackh_128B_dsl \n(reg 2)  1024  1024  0  1024  8  16  1  1  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-shl ; vec-shl_p16_s2048_signed_None\n\t (vec-shr ; vec-shr_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-shl ; vec-shl_p16_s2048_signed_None\n\t (vec-shr ; vec-shr_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-widen-mul ; vec-widen-mul_p16_s1024_signed_0\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-widen-mul ; vec-widen-mul_p16_s1024_signed_0\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-bwand ; vec-bwand_p16_s2048_signed_None\n\t (vec-absd ; vec-absd_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-abs ; vec-abs_p16_s2048_signed_1\n\t\t(buffer-index  2 'int16 2048) ; < 128 x i16> 1\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwand ; vec-bwand_p16_s2048_signed_None\n\t (vec-absd ; vec-absd_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-abs ; vec-abs_p16_s2048_signed_1\n\t\t(buffer-index  2 'int16 2048) ; < 128 x i16> 1\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-abs ; vec-abs_p16_s2048_signed_1\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-abs ; vec-abs_p16_s2048_signed_1\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vabsh_128B_dsl \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vabsw_sat_128B_dsl \n(reg 1)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-abs ; vec-abs_p16_s2048_signed_1\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-abs ; vec-abs_p16_s2048_signed_1\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vabsh_128B_dsl \n(reg 1)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vabsh_128B_dsl \n(reg 1)  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-mod ; vec-mod_p16_s1024_signed_0\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-mod ; vec-mod_p16_s1024_signed_0\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (cast-int ; cast-int_ip16_is2048_op8_os1024_signed_1\n\t (vec-absd ; vec-absd_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t128\n\t8\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-int ; cast-int_ip16_is2048_op8_os1024_signed_1\n\t (vec-absd ; vec-absd_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t128\n\t8\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (xBroadcast ; xBroadcast_is32_os1024_signed_None\n\t(buffer-index  0 'uint32 32) ; < 1 x i32> False\n\t32\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (xBroadcast ; xBroadcast_is32_os1024_signed_None\n\t(buffer-index  0 'uint32 32) ; < 1 x i32> False\n\t32\n )",
                "simplified": "\n(hexagon_V6_lvsplatw_128B_dsl \n(reg 0)  1024  1024  0  1024  32  0  );<32 x i32>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vlsrwv_128B_dsl \n(reg 2)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 1)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(reg 1)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vlsrwv_128B_dsl \n(reg 2)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 1)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vlsrwv_128B_dsl \n(reg 2)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 1)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n  (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <128 x i8>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-saturate ; vec-saturate_ip32_is2048_op16_os1024_signed_0\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> False\n\t64\n\t16\n\t#f\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-saturate ; vec-saturate_ip32_is2048_op16_os1024_signed_0\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> False\n\t64\n\t16\n\t#f\n )",
                "simplified": "\n(hexagon_V6_vpackwuh_sat_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  512  16  0  512  16  0  32  1  32  0  32  1  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-shl ; vec-shl_p16_s1024_signed_None\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-shl ; vec-shl_p16_s1024_signed_None\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaslhv_128B_dsl \n(hexagon_V6_vaddhsat_128B_dsl \n(reg 3)  \n(reg 2)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-abs ; vec-abs_p16_s1024_signed_1\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-abs ; vec-abs_p16_s1024_signed_1\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vabsh_128B_dsl \n(hexagon_V6_vaddhsat_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-abs ; vec-abs_p16_s1024_signed_1\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-abs ; vec-abs_p16_s1024_signed_1\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vabsw_sat_128B_dsl \n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) ; <1 x i16>\n  (lit (bv #x0002 16)) ; <1 x i16>\n  (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <64 x i16>\n  \n(hexagon_V6_vaddhsat_128B_dsl \n(reg 3)  \n(reg 2)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  16  0  -1  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) ; <1 x i16>\n  (lit (bv #x0002 16)) ; <1 x i16>\n  \n(hexagon_V6_vaddhsat_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  \n(hexagon_V6_vlsrwv_128B_dsl \n(reg 1)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  1024  1024  0  1024  16  0  -1  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) ; <1 x i16>\n  (lit (bv #x0002 16)) ; <1 x i16>\n  \n(hexagon_V6_vlsrwv_128B_dsl \n(reg 2)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vaddhsat_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  16  0  -1  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (xBroadcast ; xBroadcast_is32_os2048_signed_None\n\t(buffer-index  0 'uint32 32) ; < 1 x i32> False\n\t64\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (xBroadcast ; xBroadcast_is32_os2048_signed_None\n\t(buffer-index  0 'uint32 32) ; < 1 x i32> False\n\t64\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_lvsplatw_128B_dsl \n(reg 0)  1024  1024  0  1024  32  0  );<32 x i32>\n  \n(hexagon_V6_lvsplatw_128B_dsl \n(reg 0)  1024  1024  0  1024  32  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<64 x i32>\n"
            }
        }
    ],
    " (vec-saturate ; vec-saturate_ip16_is2048_op8_os1024_signed_0\n\t (vec-halving_add ; vec-halving_add_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t128\n\t8\n\t#f\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-saturate ; vec-saturate_ip16_is2048_op8_os1024_signed_0\n\t (vec-halving_add ; vec-halving_add_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t128\n\t8\n\t#f\n )",
                "simplified": "\n(hexagon_V6_vpackwuh_sat_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  512  8  0  512  8  0  16  1  64  0  16  1  8  0  );<128 x i8>\n"
            }
        }
    ],
    " (vec-bwand ; vec-bwand_p16_s2048_signed_None\n\t (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-div ; vec-div_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwand ; vec-bwand_p16_s2048_signed_None\n\t (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-div ; vec-div_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-shr ; vec-shr_p16_s1024_signed_0\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-shr ; vec-shr_p16_s1024_signed_0\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vlsrwv_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(hexagon_V6_vminuh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-shr ; vec-shr_p16_s1024_signed_0\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-shr ; vec-shr_p16_s1024_signed_0\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vlsrwv_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-shr ; vec-shr_p16_s1024_signed_0\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-shr ; vec-shr_p16_s1024_signed_0\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vlsrwv_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 1)  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-shl ; vec-shl_p16_s2048_signed_None\n\t (vec-sub ; vec-sub_p16_s2048_signed_None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t )\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-shl ; vec-shl_p16_s2048_signed_None\n\t (vec-sub ; vec-sub_p16_s2048_signed_None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t )\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vaslhv_128B_dsl \n(reg 1)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vminuh_128B_dsl \n(reg 3)  \n(reg 2)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vaslhv_128B_dsl \n(reg 1)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 1)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vminuh_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vabsdiffh_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  16  -1  -1  0  0  );<64 x i16>\n  \n(hexagon_V6_vnot_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <128 x i8>\n  \n(hexagon_V6_vnot_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<2 x i1024>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vaslhv_128B_dsl \n(reg 2)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vminuh_128B_dsl \n(reg 3)  \n(reg 2)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-min ; vec-min_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vaslhv_128B_dsl \n(reg 1)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 2)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vminuh_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (xBroadcast ; xBroadcast_is32_os1024_signed_None\n\t\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t\t32\n\t )\n\t64\n\t32\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (xBroadcast ; xBroadcast_is32_os1024_signed_None\n\t\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t\t32\n\t )\n\t64\n\t32\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_lvsplatw_128B_dsl \n(reg 0)  1024  1024  0  1024  32  0  );<32 x i32>\n  \n(hexagon_V6_lvsplatw_128B_dsl \n(reg 0)  1024  1024  0  1024  32  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<64 x i32>\n"
            }
        }
    ],
    " (vec-rounding_mul_shift_right ; vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  5 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-rounding_mul_shift_right ; vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  5 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (cast-uint ; cast-uint_ip32_is2048_op16_os1024_signed_0\n\t (xBroadcast ; xBroadcast_is32_os2048_signed_None\n\t\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t\t64\n\t )\n\t64\n\t16\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-uint ; cast-uint_ip32_is2048_op16_os1024_signed_0\n\t (xBroadcast ; xBroadcast_is32_os2048_signed_None\n\t\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t\t64\n\t )\n\t64\n\t16\n )",
                "simplified": "\n(hexagon_V6_lvsplatb_128B_dsl \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-saturate ; vec-saturate_ip32_is2048_op16_os1024_signed_0\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t )\n\t64\n\t16\n\t#f\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-saturate ; vec-saturate_ip32_is2048_op16_os1024_signed_0\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t )\n\t64\n\t16\n\t#f\n )",
                "simplified": "\n(reg 0)"
            }
        }
    ],
    " (vec-saturate ; vec-saturate_ip32_is2048_op16_os1024_signed_0\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t )\n\t64\n\t16\n\t#f\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-saturate ; vec-saturate_ip32_is2048_op16_os1024_signed_0\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t )\n\t64\n\t16\n\t#f\n )",
                "simplified": "\n(reg 1)"
            }
        }
    ],
    " (vec-min ; vec-min_p16_s1024_signed_0\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-min ; vec-min_p16_s1024_signed_0\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vminuh_128B_dsl \n(hexagon_V6_vaslhv_128B_dsl \n(reg 1)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vnot_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  16  0  0  );<64 x i16>\n"
            }
        }
    ],
    " (cast-uint ; cast-uint_ip32_is2048_op16_os1024_signed_0\n\t (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t64\n\t\t32\n\t )\n\t64\n\t16\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-uint ; cast-uint_ip32_is2048_op16_os1024_signed_0\n\t (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t64\n\t\t32\n\t )\n\t64\n\t16\n )",
                "simplified": "\n(reg 0)"
            }
        }
    ],
    " (vec-saturate ; vec-saturate_ip16_is2048_op8_os1024_signed_1\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t128\n\t8\n\t#t\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-saturate ; vec-saturate_ip16_is2048_op8_os1024_signed_1\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t128\n\t8\n\t#t\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_vaddhsat_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_vaddhsat_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (cast-uint ; cast-uint_ip16_is2048_op8_os1024_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t128\n\t8\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-uint ; cast-uint_ip16_is2048_op8_os1024_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t128\n\t8\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-mod ; vec-mod_p16_s1024_signed_0\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-mod ; vec-mod_p16_s1024_signed_0\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-abs ; vec-abs_p16_s1024_signed_1\n\t (vec-halving_add ; vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-abs ; vec-abs_p16_s1024_signed_1\n\t (vec-halving_add ; vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vabsw_sat_128B_dsl \n(reg 1)  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_32_1_32\n\t (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t64\n\t\t32\n\t )\n\t32\n\t1\n\t32\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_32_1_32\n\t (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t64\n\t\t32\n\t )\n\t32\n\t1\n\t32\n )",
                "simplified": "\n(hexagon_V6_vassign_128B_dsl \n(hexagon_V6_vunpackh_128B_dsl \n(reg 0)  1024  1024  0  1024  16  32  1  0  0  );<64 x i32>\n  1024  1024  0  1024  8  0  );<32 x i32>\n"
            }
        }
    ],
    " (cast-uint ; cast-uint_ip8_is1024_op16_os2048_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t128\n\t16\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-uint ; cast-uint_ip8_is1024_op16_os2048_signed_0\n\t(buffer-index  0 'uint8 1024) ; < 128 x i8> False\n\t128\n\t16\n )",
                "simplified": "\n(hexagon_V6_vunpackh_128B_dsl \n(reg 0)  1024  1024  0  1024  8  16  1  0  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) ; <1 x i16>\n  (lit (bv #x0002 16)) ; <1 x i16>\n  \n(hexagon_V6_vnot_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <64 x i16>\n  1024  1024  0  1024  16  0  -1  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-max ; vec-max_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-add ; vec-add_p16_s2048_signed_None\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-max ; vec-max_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-add ; vec-add_p16_s2048_signed_None\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 2)  \n(reg 3)  2048  2048  0  2048  16  -1  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-max ; vec-max_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-max ; vec-max_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (slice_vectors ; slice_vectors_ip8_is2048_op8_os1024_signed_1_128_1_128\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> False\n\t128\n\t1\n\t128\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (slice_vectors ; slice_vectors_ip8_is2048_op8_os1024_signed_1_128_1_128\n\t(buffer-index  0 'uint8 2048) ; < 256 x i8> False\n\t128\n\t1\n\t128\n )",
                "simplified": "\n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n"
            }
        }
    ],
    " (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-max ; vec-max_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-max ; vec-max_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-max ; vec-max_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-max ; vec-max_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_32_1_32\n\t (cast-int ; cast-int_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t\t64\n\t\t32\n\t )\n\t32\n\t1\n\t32\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_32_1_32\n\t (cast-int ; cast-int_ip16_is1024_op32_os2048_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t\t64\n\t\t32\n\t )\n\t32\n\t1\n\t32\n )",
                "simplified": "\n(hexagon_V6_vassign_128B_dsl \n(hexagon_V6_vunpackh_128B_dsl \n(reg 0)  1024  1024  0  1024  16  32  1  1  0  );<64 x i32>\n  1024  1024  0  1024  8  0  );<32 x i32>\n"
            }
        }
    ],
    " (vec-sub ; vec-sub_p16_s2048_signed_None\n\t (vec-halving_add ; vec-halving_add_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  2 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  3 'int16 1024) ; < 64 x i16> 1\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sub ; vec-sub_p16_s2048_signed_None\n\t (vec-halving_add ; vec-halving_add_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  2 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  3 'int16 1024) ; < 64 x i16> 1\n\t )\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 1)  \n(hexagon_V6_vcombine_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n  2048  2048  0  2048  16  -1  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-bwnot ; vec-bwnot_p16_s2048_signed_0\n\t (xBroadcast ; xBroadcast_is32_os2048_signed_None\n\t\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t\t64\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwnot ; vec-bwnot_p16_s2048_signed_0\n\t (xBroadcast ; xBroadcast_is32_os2048_signed_None\n\t\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t\t64\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_lvsplatw_128B_dsl \n(reg 0)  1024  1024  0  1024  32  0  );<32 x i32>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_lvsplatw_128B_dsl \n(reg 0)  1024  1024  0  1024  32  0  );<32 x i32>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-bwnot ; vec-bwnot_p16_s2048_signed_0\n\t (vec-min ; vec-min_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwnot ; vec-bwnot_p16_s2048_signed_0\n\t (vec-min ; vec-min_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-widen-mul ; vec-widen-mul_p16_s1024_signed_0\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-widen-mul ; vec-widen-mul_p16_s1024_signed_0\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (cast-int ; cast-int_ip32_is2048_op16_os1024_signed_1\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> False\n\t64\n\t16\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-int ; cast-int_ip32_is2048_op16_os1024_signed_1\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> False\n\t64\n\t16\n )",
                "simplified": "\n(hexagon_V6_vpackeh_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  512  16  0  512  16  2  32  2  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-sat-add ; vec-sat-add_p16_s2048_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-add ; vec-add_p16_s2048_signed_None\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-add ; vec-sat-add_p16_s2048_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-add ; vec-add_p16_s2048_signed_None\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  2048  2048  0  2048  16  0  0  );<128 x i16>\n  \n(hexagon_V6_vaddhsat_128B_dsl \n(reg 2)  \n(reg 3)  2048  2048  0  2048  16  -1  0  );<128 x i16>\n  2048  2048  0  2048  16  0  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-sat-add ; vec-sat-add_p16_s2048_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-add ; vec-add_p16_s2048_signed_None\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-add ; vec-sat-add_p16_s2048_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-add ; vec-add_p16_s2048_signed_None\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 3)  \n(reg 2)  2048  2048  0  2048  16  -1  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-shr ; vec-shr_p16_s1024_signed_0\n\t (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_64_1_64\n\t\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t\t64\n\t\t1\n\t\t64\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-shr ; vec-shr_p16_s1024_signed_0\n\t (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_64_1_64\n\t\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t\t64\n\t\t1\n\t\t64\n\t )\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vasrhv_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(reg 1)  1024  1024  0  1024  16  0  );<64 x i16>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-abs ; vec-abs_p16_s1024_signed_1\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-abs ; vec-abs_p16_s1024_signed_1\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vabsh_128B_dsl \n(hexagon_V6_vnot_128B_dsl \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (slice_vectors ; slice_vectors_ip8_is2048_op8_os1024_signed_1_0_1_128\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t )\n\t0\n\t1\n\t128\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (slice_vectors ; slice_vectors_ip8_is2048_op8_os1024_signed_1_0_1_128\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t )\n\t0\n\t1\n\t128\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n"
            }
        }
    ],
    " (slice_vectors ; slice_vectors_ip8_is2048_op8_os1024_signed_1_0_1_128\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t )\n\t0\n\t1\n\t128\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (slice_vectors ; slice_vectors_ip8_is2048_op8_os1024_signed_1_0_1_128\n\t (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t\t(buffer-index  1 'int16 1024) ; < 64 x i16> 1\n\t )\n\t0\n\t1\n\t128\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(reg 1)  \n(reg 1)  1024  1024  0  1024  8  0  1024  8  1024  0  );<256 x i8>\n"
            }
        }
    ],
    " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t64\n\t32\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t64\n\t32\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-min ; vec-min_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-div ; vec-div_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-min ; vec-min_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-div ; vec-div_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-widen-mul ; vec-widen-mul_p16_s1024_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_64_1_64\n\t\t(buffer-index  2 'int16 2048) ; < 128 x i16> 1\n\t\t64\n\t\t1\n\t\t64\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-widen-mul ; vec-widen-mul_p16_s1024_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_64_1_64\n\t\t(buffer-index  2 'int16 2048) ; < 128 x i16> 1\n\t\t64\n\t\t1\n\t\t64\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-mul ; vec-mul_p16_s1024_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-max ; vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-mul ; vec-mul_p16_s1024_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-max ; vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-rounding_shift_right ; vec-rounding_shift_right_p16_s2048_signed_0\n\t (cast-int ; cast-int_ip8_is1024_op16_os2048_signed_1\n\t\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t\t128\n\t\t16\n\t )\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-rounding_shift_right ; vec-rounding_shift_right_p16_s2048_signed_0\n\t (cast-int ; cast-int_ip8_is1024_op16_os2048_signed_1\n\t\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t\t128\n\t\t16\n\t )\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vunpackh_128B_dsl \n(reg 0)  1024  1024  0  1024  8  16  1  1  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  16  0  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(hexagon_V6_vlsrwv_128B_dsl \n(reg 1)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vsubh_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  16  0  0  );<64 x i16>\n"
            }
        }
    ],
    " (cast-uint ; cast-uint_ip32_is2048_op16_os1024_signed_0\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> False\n\t64\n\t16\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-uint ; cast-uint_ip32_is2048_op16_os1024_signed_0\n\t(buffer-index  0 'uint32 2048) ; < 64 x i32> False\n\t64\n\t16\n )",
                "simplified": "\n(hexagon_V6_vpackeh_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  512  16  0  512  16  2  32  2  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-halving_add ; vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-halving_add ; vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-shl ; vec-shl_p16_s1024_signed_None\n\t (cast-uint ; cast-uint_ip32_is2048_op16_os1024_signed_0\n\t\t(buffer-index  0 'uint32 2048) ; < 64 x i32> 0\n\t\t64\n\t\t16\n\t )\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-shl ; vec-shl_p16_s1024_signed_None\n\t (cast-uint ; cast-uint_ip32_is2048_op16_os1024_signed_0\n\t\t(buffer-index  0 'uint32 2048) ; < 64 x i32> 0\n\t\t64\n\t\t16\n\t )\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vpackeh_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  512  16  0  512  16  2  32  2  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_64_1_64\n\t (vec-shr ; vec-shr_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t64\n\t1\n\t64\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_64_1_64\n\t (vec-shr ; vec-shr_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t64\n\t1\n\t64\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_64_1_64\n\t (vec-shr ; vec-shr_p16_s2048_signed_0\n\t\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t64\n\t1\n\t64\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_64_1_64\n\t (vec-shr ; vec-shr_p16_s2048_signed_0\n\t\t(buffer-index  0 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t64\n\t1\n\t64\n )",
                "simplified": "\n(hexagon_V6_vlsrwv_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-max ; vec-max_p16_s1024_signed_0\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t )\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-max ; vec-max_p16_s1024_signed_0\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t )\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vmaxw_128B_dsl \n(hexagon_V6_vabsh_128B_dsl \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n  (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <64 x i16>\n  1024  1024  0  1024  16  1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(hexagon_V6_vabsh_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vsubh_128B_dsl \n(reg 1)  \n(reg 2)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(hexagon_V6_vabsh_128B_dsl \n(reg 1)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vsubh_128B_dsl \n(reg 2)  \n(reg 1)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(hexagon_V6_vsubh_128B_dsl \n(reg 1)  \n(reg 2)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  \n(hexagon_V6_vabsh_128B_dsl \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-rounding_shift_right ; vec-rounding_shift_right_p16_s1024_signed_0\n\t (xBroadcast ; xBroadcast_is32_os1024_signed_None\n\t\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t\t32\n\t )\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-rounding_shift_right ; vec-rounding_shift_right_p16_s1024_signed_0\n\t (xBroadcast ; xBroadcast_is32_os1024_signed_None\n\t\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t\t32\n\t )\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_lvsplatw_128B_dsl \n(reg 0)  1024  1024  0  1024  32  0  );<32 x i32>\n"
            }
        }
    ],
    " (vec-bwnot ; vec-bwnot_p16_s2048_signed_0\n\t (vec-sub ; vec-sub_p16_s2048_signed_None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwnot ; vec-bwnot_p16_s2048_signed_0\n\t (vec-sub ; vec-sub_p16_s2048_signed_None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vnot_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <64 x i16>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vnot_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <64 x i16>\n  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-widen-mul ; vec-widen-mul_p16_s1024_signed_0\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-widen-mul ; vec-widen-mul_p16_s1024_signed_0\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-min ; vec-min_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-rounding_shift_right ; vec-rounding_shift_right_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-min ; vec-min_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-rounding_shift_right ; vec-rounding_shift_right_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-mul ; vec-mul_p16_s2048_signed_0\n\t (vec-sub ; vec-sub_p16_s2048_signed_None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t )\n\t (xBroadcast ; xBroadcast_is32_os2048_signed_None\n\t\t(buffer-index  2 'uint32 32) ; < 1 x i32> None\n\t\t64\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-mul ; vec-mul_p16_s2048_signed_0\n\t (vec-sub ; vec-sub_p16_s2048_signed_None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t )\n\t (xBroadcast ; xBroadcast_is32_os2048_signed_None\n\t\t(buffer-index  2 'uint32 32) ; < 1 x i32> None\n\t\t64\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_32_1_32\n\t (xBroadcast ; xBroadcast_is32_os2048_signed_None\n\t\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t\t64\n\t )\n\t32\n\t1\n\t32\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_32_1_32\n\t (xBroadcast ; xBroadcast_is32_os2048_signed_None\n\t\t(buffer-index  0 'uint32 32) ; < 1 x i32> None\n\t\t64\n\t )\n\t32\n\t1\n\t32\n )",
                "simplified": "\n(hexagon_V6_lvsplatw_128B_dsl \n(reg 0)  1024  1024  0  1024  32  0  );<32 x i32>\n"
            }
        }
    ],
    " (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_0_1_64\n\t\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t\t0\n\t\t1\n\t\t64\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_0_1_64\n\t\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t\t0\n\t\t1\n\t\t64\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) ; <1 x i16>\n  (lit (bv #x0002 16)) ; <1 x i16>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <64 x i16>\n  1024  1024  0  1024  16  1  -1  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t )\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t )\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vabsw_sat_128B_dsl \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_vaddhsat_128B_dsl \n(reg 2)  \n(reg 1)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vabsh_128B_dsl \n(reg 2)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vaddbq_128B_dsl \n(reg 2)  (lit (bv #b1 1)) ; <1/16 x i16>\n  (lit (bv #x00000000000000000000000000000000 128)) ; <8 x i16>\n  \n(reg 1)  1024  1024  0  1024  16  -1  1  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t )\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-abs ; vec-abs_p16_s1024_signed_1\n\t\t(buffer-index  0 'int16 1024) ; < 64 x i16> 1\n\t )\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vabsh_128B_dsl \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vaddbq_128B_dsl \n(reg 2)  (lit (bv #b1 1)) ; <1/16 x i16>\n  (lit (bv #x00000000000000000000000000000000 128)) ; <8 x i16>\n  \n(reg 2)  1024  1024  0  1024  16  -1  1  16  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vabsdiffh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  -1  -1  0  0  );<64 x i16>\n  \n(hexagon_V6_vabsdiffh_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  16  -1  -1  0  0  );<64 x i16>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-bwand ; vec-bwand_p16_s2048_signed_None\n\t (vec-sub ; vec-sub_p16_s2048_signed_None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwand ; vec-bwand_p16_s2048_signed_None\n\t (vec-sub ; vec-sub_p16_s2048_signed_None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t )\n\t (vec-sat-add ; vec-sat-add_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (xBroadcast ; xBroadcast_is32_os1024_signed_None\n\t\t(buffer-index  2 'uint32 32) ; < 1 x i32> None\n\t\t32\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (xBroadcast ; xBroadcast_is32_os1024_signed_None\n\t\t(buffer-index  2 'uint32 32) ; < 1 x i32> None\n\t\t32\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vaddhsat_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  \n(hexagon_V6_lvsplatw_128B_dsl \n(reg 2)  1024  1024  0  1024  32  0  );<32 x i32>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (cast-uint ; cast-uint_ip32_is2048_op16_os1024_signed_0\n\t\t(buffer-index  2 'uint32 2048) ; < 64 x i32> 0\n\t\t64\n\t\t16\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (cast-uint ; cast-uint_ip32_is2048_op16_os1024_signed_0\n\t\t(buffer-index  2 'uint32 2048) ; < 64 x i32> 0\n\t\t64\n\t\t16\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-rounding_mul_shift_right ; vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-rounding_mul_shift_right ; vec-rounding_mul_shift_right_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  4 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-rounding_shift_right ; vec-rounding_shift_right_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-rounding_shift_right ; vec-rounding_shift_right_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-sub ; vec-sub_p16_s1024_signed_None\n\t (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_0_1_32\n\t\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t\t0\n\t\t1\n\t\t32\n\t )\n\t (xBroadcast ; xBroadcast_is32_os1024_signed_None\n\t\t(buffer-index  1 'uint32 32) ; < 1 x i32> None\n\t\t32\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sub ; vec-sub_p16_s1024_signed_None\n\t (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_0_1_32\n\t\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t\t0\n\t\t1\n\t\t32\n\t )\n\t (xBroadcast ; xBroadcast_is32_os1024_signed_None\n\t\t(buffer-index  1 'uint32 32) ; < 1 x i32> None\n\t\t32\n\t )\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_lvsplatw_128B_dsl \n(reg 1)  1024  1024  0  1024  32  0  );<32 x i32>\n  1024  1024  0  1024  32  -1  0  );<32 x i32>\n"
            }
        }
    ],
    " (vec-add ; vec-add_p16_s2048_signed_None\n\t (vec-absd ; vec-absd_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-add ; vec-add_p16_s2048_signed_None\n\t (vec-absd ; vec-absd_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 2)  \n(reg 3)  2048  2048  0  2048  16  0  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-min ; vec-min_p16_s1024_signed_0\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-min ; vec-min_p16_s1024_signed_0\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(hexagon_V6_pred_and_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vsubh_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(hexagon_V6_vsubh_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  \n(reg 1)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-max ; vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-max ; vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(hexagon_V6_vmaxw_128B_dsl \n(reg 1)  \n(reg 0)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  \n(hexagon_V6_vsubh_128B_dsl \n(reg 3)  \n(reg 2)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-max ; vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-max ; vec-max_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(reg 1)  \n(hexagon_V6_vsubh_128B_dsl \n(reg 3)  \n(reg 2)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-max ; vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-max ; vec-max_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(hexagon_V6_vsubh_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  \n(hexagon_V6_vmaxw_128B_dsl \n(reg 2)  \n(reg 1)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-max ; vec-max_p16_s1024_signed_0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-max ; vec-max_p16_s1024_signed_0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(hexagon_V6_vmaxw_128B_dsl \n(reg 3)  \n(reg 1)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  \n(hexagon_V6_vsubh_128B_dsl \n(reg 3)  \n(reg 2)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-max ; vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-add ; vec-add_p16_s1024_signed_None\n\t (vec-max ; vec-max_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(hexagon_V6_vmaxw_128B_dsl \n(reg 0)  \n(reg 2)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  \n(hexagon_V6_vsubh_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-sub ; vec-sub_p16_s2048_signed_None\n\t (cast-int ; cast-int_ip8_is1024_op16_os2048_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t\t128\n\t\t16\n\t )\n\t (cast-uint ; cast-uint_ip8_is1024_op16_os2048_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t\t128\n\t\t16\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sub ; vec-sub_p16_s2048_signed_None\n\t (cast-int ; cast-int_ip8_is1024_op16_os2048_signed_1\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t\t128\n\t\t16\n\t )\n\t (cast-uint ; cast-uint_ip8_is1024_op16_os2048_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t\t128\n\t\t16\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-sub ; vec-sub_p16_s2048_signed_None\n\t (cast-int ; cast-int_ip8_is1024_op16_os2048_signed_1\n\t\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t\t128\n\t\t16\n\t )\n\t (cast-uint ; cast-uint_ip8_is1024_op16_os2048_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t\t128\n\t\t16\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sub ; vec-sub_p16_s2048_signed_None\n\t (cast-int ; cast-int_ip8_is1024_op16_os2048_signed_1\n\t\t(buffer-index  0 'int8 1024) ; < 128 x i8> 1\n\t\t128\n\t\t16\n\t )\n\t (cast-uint ; cast-uint_ip8_is1024_op16_os2048_signed_0\n\t\t(buffer-index  1 'uint8 1024) ; < 128 x i8> 0\n\t\t128\n\t\t16\n\t )\n )",
                "simplified": "\n(hexagon_V6_vsubh_128B_dsl \n(hexagon_V6_vunpackh_128B_dsl \n(reg 0)  1024  1024  0  1024  8  16  1  1  0  );<128 x i16>\n  \n(hexagon_V6_vunpackh_128B_dsl \n(reg 1)  1024  1024  0  1024  8  16  1  0  0  );<128 x i16>\n  2048  2048  0  2048  16  -1  0  );<128 x i16>\n"
            }
        }
    ],
    " (vec-mod ; vec-mod_p16_s1024_signed_0\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-mod ; vec-mod_p16_s1024_signed_0\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-mul ; vec-mul_p16_s1024_signed_0\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-mul ; vec-mul_p16_s1024_signed_0\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "\n(hexagon_V6_vnot_128B_dsl \n(reg 0)  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-mul ; vec-mul_p16_s2048_signed_0\n\t (vec-sub ; vec-sub_p16_s2048_signed_None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t )\n\t (vec-shl ; vec-shl_p16_s2048_signed_None\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-mul ; vec-mul_p16_s2048_signed_0\n\t (vec-sub ; vec-sub_p16_s2048_signed_None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t )\n\t (vec-shl ; vec-shl_p16_s2048_signed_None\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> None\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t64\n\t32\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t64\n\t32\n )",
                "simplified": "\n(hexagon_V6_vunpackh_128B_dsl \n(reg 1)  1024  1024  0  1024  16  32  1  0  0  );<64 x i32>\n"
            }
        }
    ],
    " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t64\n\t32\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t64\n\t32\n )",
                "simplified": "\n(hexagon_V6_vunpackh_128B_dsl \n(hexagon_V6_pred_and_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  0  );<64 x i16>\n  1024  1024  0  1024  16  32  1  0  0  );<64 x i32>\n"
            }
        }
    ],
    " (vec-saturate ; vec-saturate_ip16_is2048_op8_os1024_signed_1\n\t (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t128\n\t8\n\t#t\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-saturate ; vec-saturate_ip16_is2048_op8_os1024_signed_1\n\t (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t128\n\t8\n\t#t\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_32_1_32\n\t\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t\t32\n\t\t1\n\t\t32\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwnot ; vec-bwnot_p16_s1024_signed_0\n\t (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_32_1_32\n\t\t(buffer-index  0 'int32 2048) ; < 64 x i32> 1\n\t\t32\n\t\t1\n\t\t32\n\t )\n )",
                "simplified": "\n(hexagon_V6_vnot_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_0_1_32\n\t\t(buffer-index  2 'int32 2048) ; < 64 x i32> 1\n\t\t0\n\t\t1\n\t\t32\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_0_1_32\n\t\t(buffer-index  2 'int32 2048) ; < 64 x i32> 1\n\t\t0\n\t\t1\n\t\t32\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl \n(hexagon_V6_vlsrwv_128B_dsl \n(reg 1)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 0)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 2)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<128 x i16>\n"
            }
        }
    ],
    " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_0_1_32\n\t\t(buffer-index  2 'int32 2048) ; < 64 x i32> 1\n\t\t0\n\t\t1\n\t\t32\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (concat_vectors ; concat_vectors_ip16_is1024_op16_os2048_signed_1\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (slice_vectors ; slice_vectors_ip32_is2048_op32_os1024_signed_1_0_1_32\n\t\t(buffer-index  2 'int32 2048) ; < 64 x i32> 1\n\t\t0\n\t\t1\n\t\t32\n\t )\n )",
                "simplified": "\n(hexagon_V6_vcombine_128B_dsl (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) ; <128 x i8>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 2)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  8  0  1024  8  1024  0  );<2 x i1024>\n"
            }
        }
    ],
    " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (vec-sub ; vec-sub_p16_s1024_signed_None\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t )\n\t (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_pred_and_128B_dsl \n(hexagon_V6_pred_and_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  16  0  );<64 x i16>\n  \n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-saturate ; vec-saturate_ip16_is2048_op8_os1024_signed_1\n\t (vec-bwand ; vec-bwand_p16_s2048_signed_None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t )\n\t128\n\t8\n\t#t\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-saturate ; vec-saturate_ip16_is2048_op8_os1024_signed_1\n\t (vec-bwand ; vec-bwand_p16_s2048_signed_None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> None\n\t )\n\t128\n\t8\n\t#t\n )",
                "simplified": "\n(hexagon_V6_vpackwuh_sat_128B_dsl \n(hexagon_V6_lo_128B_dsl \n(reg 1)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  \n(hexagon_V6_vassign_128B_dsl \n(reg 1)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  512  8  0  512  8  1  16  1  64  1  16  1  8  0  );<128 x i8>\n"
            }
        }
    ],
    " (vec-abs ; vec-abs_p16_s2048_signed_1\n\t (cast-uint ; cast-uint_ip8_is1024_op16_os2048_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t\t128\n\t\t16\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-abs ; vec-abs_p16_s2048_signed_1\n\t (cast-uint ; cast-uint_ip8_is1024_op16_os2048_signed_0\n\t\t(buffer-index  0 'uint8 1024) ; < 128 x i8> 0\n\t\t128\n\t\t16\n\t )\n )",
                "simplified": "\n(hexagon_V6_vunpackh_128B_dsl \n(reg 0)  1024  1024  0  1024  8  16  1  0  0  );<128 x i16>\n"
            }
        }
    ],
    " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t64\n\t32\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t64\n\t32\n )",
                "simplified": "\n(hexagon_V6_vunpackh_128B_dsl \n(hexagon_V6_vsubh_128B_dsl \n(reg 0)  \n(reg 1)  1024  1024  0  1024  16  0  0  );<64 x i16>\n  1024  1024  0  1024  16  32  1  0  0  );<64 x i32>\n"
            }
        }
    ],
    " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t64\n\t32\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t64\n\t32\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t (vec-shr ; vec-shr_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-min ; vec-min_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-sub ; vec-sat-sub_p16_s2048_signed_0\n\t (vec-shr ; vec-shr_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-min ; vec-min_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t64\n\t32\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  0 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t64\n\t32\n )",
                "simplified": "\n(hexagon_V6_vunpackh_128B_dsl \n(hexagon_V6_vavgwrnd_128B_dsl (lit (bv #x0001 16)) ; <1 x i16>\n  (lit (bv #x0002 16)) ; <1 x i16>\n  \n(reg 1)  \n(reg 0)  1024  1024  0  1024  16  0  -1  -1  0  );<64 x i16>\n  1024  1024  0  1024  16  32  1  0  0  );<64 x i32>\n"
            }
        }
    ],
    " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t64\n\t32\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (cast-uint ; cast-uint_ip16_is1024_op32_os2048_signed_0\n\t (vec-rounding_halving_add ; vec-rounding_halving_add_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t64\n\t32\n )",
                "simplified": "\n(hexagon_V6_vunpackh_128B_dsl \n(reg 1)  1024  1024  0  1024  16  32  1  0  0  );<64 x i32>\n"
            }
        }
    ],
    " (vec-min ; vec-min_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-min ; vec-min_p16_s1024_signed_0\n\t (vec-shr ; vec-shr_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (vec-mul ; vec-mul_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-div ; vec-div_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-mul ; vec-mul_p16_s2048_signed_0\n\t (vec-mod ; vec-mod_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n\t (vec-div ; vec-div_p16_s2048_signed_0\n\t\t(buffer-index  2 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  3 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-abs ; vec-abs_p16_s2048_signed_1\n\t (vec-absd ; vec-absd_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-abs ; vec-abs_p16_s2048_signed_1\n\t (vec-absd ; vec-absd_p16_s2048_signed_0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t\t(buffer-index  1 'uint16 2048) ; < 128 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))"
            }
        }
    ],
    " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_0_1_64\n\t\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t\t0\n\t\t1\n\t\t64\n\t )\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_0_1_64\n\t\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t\t0\n\t\t1\n\t\t64\n\t )\n\t (vec-shl ; vec-shl_p16_s1024_signed_None\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_pred_and_128B_dsl \n(hexagon_V6_vaslhv_128B_dsl \n(reg 2)  (lit (bv #x0000 16)) ; <1 x i16>\n  \n(reg 1)  1024  1024  0  1024  16  1  0  );<64 x i16>\n  \n(hexagon_V6_lo_128B_dsl \n(reg 0)  1024  1024  0  1024  8  1024  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-sat-add ; vec-sat-add_p16_s1024_signed_0\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-add ; vec-add_p16_s1024_signed_None\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> None\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> None\n\t )\n )",
                "simplified": "\n(hexagon_V6_vaddhsat_128B_dsl \n(reg 2)  \n(reg 3)  1024  1024  0  1024  16  -1  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-shr ; vec-shr_p16_s1024_signed_0\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-halving_add ; vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-shr ; vec-shr_p16_s1024_signed_0\n\t (vec-absd ; vec-absd_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-halving_add ; vec-halving_add_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    " (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_64_1_64\n\t (vec-abs ; vec-abs_p16_s2048_signed_1\n\t\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t )\n\t64\n\t1\n\t64\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (slice_vectors ; slice_vectors_ip16_is2048_op16_os1024_signed_1_64_1_64\n\t (vec-abs ; vec-abs_p16_s2048_signed_1\n\t\t(buffer-index  0 'int16 2048) ; < 128 x i16> 1\n\t )\n\t64\n\t1\n\t64\n )",
                "simplified": "\n(hexagon_V6_vabsh_128B_dsl \n(hexagon_V6_vassign_128B_dsl \n(reg 0)  1024  1024  0  1024  8  0  );<128 x i8>\n  1024  1024  0  1024  16  0  );<64 x i16>\n"
            }
        }
    ],
    " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )": [
        {
            "property_name": "Translator",
            "property": {
                "candidate": " (vec-bwand ; vec-bwand_p16_s1024_signed_None\n\t (vec-sat-sub ; vec-sat-sub_p16_s1024_signed_0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  1 'uint16 1024) ; < 64 x i16> 0\n\t )\n\t (vec-mod ; vec-mod_p16_s1024_signed_0\n\t\t(buffer-index  2 'uint16 1024) ; < 64 x i16> 0\n\t\t(buffer-index  3 'uint16 1024) ; < 64 x i16> 0\n\t )\n )",
                "simplified": "(lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ]
}