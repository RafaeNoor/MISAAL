hvx_Distributive={
    "hexagon_V6_vshuffob_128B+hexagon_V6_vminuh_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128Bhexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t2\n\t8\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+hexagon_V6_vor_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128Bhexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t2\n\t8\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vminuh_128B+hexagon_V6_vminuh_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vminuh_128Bhexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyieoh_128B+hexagon_V6_vmpyih_acc_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyieoh_128Bhexagon_V6_vmpyih_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vmpyieoh_128B_dsl ; hexagon_V6_vmpyieoh_128B\n\t(lit (bv #x00000000000000000000000000000010 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyih_acc_128B_dsl ; hexagon_V6_vmpyih_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t1\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyih_acc_128B_dsl ; hexagon_V6_vmpyih_acc_128B\n\t (hexagon_V6_vmpyieoh_128B_dsl ; hexagon_V6_vmpyieoh_128B\n\t\t(lit (bv #x00000000000000000000000000000010 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vmpyieoh_128B_dsl ; hexagon_V6_vmpyieoh_128B\n\t\t(lit (bv #x00000000000000000000000000000010 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyieoh_128B+hexagon_V6_vsubh_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyieoh_128Bhexagon_V6_vsubh_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vmpyieoh_128B_dsl ; hexagon_V6_vmpyieoh_128B\n\t(lit (bv #x00000000000000000000000000000010 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t1\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t (hexagon_V6_vmpyieoh_128B_dsl ; hexagon_V6_vmpyieoh_128B\n\t\t(lit (bv #x00000000000000000000000000000010 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vmpyieoh_128B_dsl ; hexagon_V6_vmpyieoh_128B\n\t\t(lit (bv #x00000000000000000000000000000010 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyieoh_128B+hexagon_V6_vaslh_acc_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyieoh_128Bhexagon_V6_vaslh_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vmpyieoh_128B_dsl ; hexagon_V6_vmpyieoh_128B\n\t(lit (bv #x00000000000000000000000000000010 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t1\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t (hexagon_V6_vmpyieoh_128B_dsl ; hexagon_V6_vmpyieoh_128B\n\t\t(lit (bv #x00000000000000000000000000000010 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vmpyieoh_128B_dsl ; hexagon_V6_vmpyieoh_128B\n\t\t(lit (bv #x00000000000000000000000000000010 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+hexagon_V6_vor_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128Bhexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwuh_sat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t0\n\t32\n\t1\n\t32\n\t0\n\t32\n\t1\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwuh_sat_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t\t32\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwuh_sat_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t\t32\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+hexagon_V6_vminuh_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128Bhexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+hexagon_V6_vor_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128Bhexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+hexagon_V6_vmux_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128Bhexagon_V6_vmux_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t8\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+hexagon_V6_vor_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128Bhexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_pred_and_128B+hexagon_V6_pred_and_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_pred_and_128Bhexagon_V6_pred_and_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t1\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t1\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_pred_and_128B+hexagon_V6_pred_xor_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_pred_and_128Bhexagon_V6_pred_xor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t (hexagon_V6_pred_xor_128B_dsl ; hexagon_V6_pred_xor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t1\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_pred_xor_128B_dsl ; hexagon_V6_pred_xor_128B\n\t (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t1\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_pred_and_128B+hexagon_V6_pred_and_n_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_pred_and_128Bhexagon_V6_pred_and_n_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t (hexagon_V6_pred_and_n_128B_dsl ; hexagon_V6_pred_and_n_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t1\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_pred_and_n_128B_dsl ; hexagon_V6_pred_and_n_128B\n\t (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t1\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyewuh_128B+hexagon_V6_vrmpybv_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyewuh_128Bhexagon_V6_vrmpybv_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vmpyewuh_128B_dsl ; hexagon_V6_vmpyewuh_128B\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000010 (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t8\n\t\t-1\n\t\t1\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t0\n\t64\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_acc_128B\n\t (hexagon_V6_vmpyewuh_128B_dsl ; hexagon_V6_vmpyewuh_128B\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000010 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vmpyewuh_128B_dsl ; hexagon_V6_vmpyewuh_128B\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000010 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyewuh_128B+hexagon_V6_vdmpyhsat_acc_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyewuh_128Bhexagon_V6_vdmpyhsat_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vmpyewuh_128B_dsl ; hexagon_V6_vmpyewuh_128B\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000010 (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vdmpyhsat_acc_128B_dsl ; hexagon_V6_vdmpyhsat_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t0\n\t64\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vdmpyhsat_acc_128B_dsl ; hexagon_V6_vdmpyhsat_acc_128B\n\t (hexagon_V6_vmpyewuh_128B_dsl ; hexagon_V6_vmpyewuh_128B\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000010 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vmpyewuh_128B_dsl ; hexagon_V6_vmpyewuh_128B\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000010 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyiewh_acc_128B+hexagon_V6_vmaxw_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyiewh_acc_128Bhexagon_V6_vmaxw_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmpyiewh_acc_128B_dsl ; hexagon_V6_vmpyiewuh_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t-1\n\t1\n\t64\n\t0\n\t64\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t (hexagon_V6_vmpyiewh_acc_128B_dsl ; hexagon_V6_vmpyiewuh_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t0\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vmpyiewh_acc_128B_dsl ; hexagon_V6_vmpyiewuh_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t0\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+hexagon_V6_vmpyih_acc_128B+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128Bhexagon_V6_vmpyih_acc_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hexagon_V6_vmpyih_acc_128B_dsl ; hexagon_V6_vmpyih_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyih_acc_128B_dsl ; hexagon_V6_vmpyih_acc_128B\n\t (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+hexagon_V6_vor_128B+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128Bhexagon_V6_vor_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+hexagon_V6_vsubh_128B+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128Bhexagon_V6_vsubh_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+hexagon_V6_vsubhnq_128B+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128Bhexagon_V6_vsubhnq_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hexagon_V6_vsubhnq_128B_dsl ; hexagon_V6_vsubhnq_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vsubhnq_128B_dsl ; hexagon_V6_vsubhnq_128B\n\t (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(lit (bv #b1 (bitvector 1)))\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+hexagon_V6_vmpyih_acc_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128Bhexagon_V6_vmpyih_acc_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyih_acc_128B_dsl ; hexagon_V6_vmpyih_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyih_acc_128B_dsl ; hexagon_V6_vmpyih_acc_128B\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+hexagon_V6_vsubh_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128Bhexagon_V6_vsubh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+hexagon_V6_vsubhnq_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128Bhexagon_V6_vsubhnq_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vsubhnq_128B_dsl ; hexagon_V6_vsubhnq_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vsubhnq_128B_dsl ; hexagon_V6_vsubhnq_128B\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t(lit (bv #b1 (bitvector 1)))\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyiwh_acc_128B+hexagon_V6_vmaxw_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyiwh_acc_128Bhexagon_V6_vmaxw_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmpyiwh_acc_128B_dsl ; hexagon_V6_vmpyiwh_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t32\n\t32\n\t0\n\t512\n\t16\n\t32\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t (hexagon_V6_vmpyiwh_acc_128B_dsl ; hexagon_V6_vmpyiwh_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t32\n\t\t32\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vmpyiwh_acc_128B_dsl ; hexagon_V6_vmpyiwh_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t32\n\t\t32\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmux_128B+hexagon_V6_vmux_128B+(0, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmux_128Bhexagon_V6_vmux_128B",
                "indices": [
                    0,
                    3
                ],
                "input_expression": " (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 8 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t8\n\t0\n )",
                "output_expression": " (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1\n\t\t8\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 8 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t8\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmux_128B+hexagon_V6_vor_128B+(0, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmux_128Bhexagon_V6_vor_128B",
                "indices": [
                    0,
                    3
                ],
                "input_expression": " (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t8\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyowh_128B+hexagon_V6_vmpyowh_128B+(3, 4)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyowh_128Bhexagon_V6_vmpyowh_128B",
                "indices": [
                    3,
                    4
                ],
                "input_expression": " (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+hexagon_V6_vminuh_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vsathub_128Bhexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t16\n\t1\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyowh_128B+hexagon_V6_vmpyowh_rnd_sacc_128B+(3, 4)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyowh_128Bhexagon_V6_vmpyowh_rnd_sacc_128B",
                "indices": [
                    3,
                    4
                ],
                "input_expression": " (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+hexagon_V6_vor_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vsathub_128Bhexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t16\n\t1\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+hexagon_V6_vrmpybus_acc_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128Bhexagon_V6_vrmpybus_acc_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vrmpybus_acc_128B_dsl ; hexagon_V6_vrmpybus_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t8\n\t\t-1\n\t\t1\n\t\t1\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vrmpybus_acc_128B_dsl ; hexagon_V6_vrmpybus_acc_128B\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+hexagon_V6_vrmpybv_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128Bhexagon_V6_vrmpybv_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t8\n\t\t-1\n\t\t1\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_acc_128B\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+hexagon_V6_vdmpyhvsat_acc_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128Bhexagon_V6_vdmpyhvsat_acc_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+hexagon_V6_vdmpyhvsat_acc_128B+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128Bhexagon_V6_vdmpyhvsat_acc_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+hexagon_V6_vdmpybus_128B+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128Bhexagon_V6_vdmpybus_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vdmpybus_128B_dsl ; hexagon_V6_vdmpybus_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t-1\n\t\t1\n\t\t0\n\t\t4\n\t\t8\n\t\t8\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vdmpybus_128B_dsl ; hexagon_V6_vdmpybus_acc_128B\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t16\n\t0\n\t16\n\t8\n\t-1\n\t1\n\t0\n\t4\n\t8\n\t8\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+hexagon_V6_vdmpyhsat_acc_128B+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128Bhexagon_V6_vdmpyhsat_acc_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vdmpyhsat_acc_128B_dsl ; hexagon_V6_vdmpyhsat_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vdmpyhsat_acc_128B_dsl ; hexagon_V6_vdmpyhsat_acc_128B\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+hexagon_V6_vmpyewuh_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128Bhexagon_V6_vmpyewuh_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyewuh_128B_dsl ; hexagon_V6_vmpyewuh_128B\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000010 (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyewuh_128B_dsl ; hexagon_V6_vmpyewuh_128B\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000010 (bitvector 64)))\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t0\n\t64\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+hexagon_V6_vdmpybus_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128Bhexagon_V6_vdmpybus_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vdmpybus_128B_dsl ; hexagon_V6_vdmpybus_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t-1\n\t\t1\n\t\t0\n\t\t4\n\t\t8\n\t\t8\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vdmpybus_128B_dsl ; hexagon_V6_vdmpybus_acc_128B\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t16\n\t0\n\t16\n\t8\n\t-1\n\t1\n\t0\n\t4\n\t8\n\t8\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+hexagon_V6_vdmpyhvsat_acc_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128Bhexagon_V6_vdmpyhvsat_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+hexagon_V6_vdmpyhsat_acc_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128Bhexagon_V6_vdmpyhsat_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vdmpyhsat_acc_128B_dsl ; hexagon_V6_vdmpyhsat_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vdmpyhsat_acc_128B_dsl ; hexagon_V6_vdmpyhsat_acc_128B\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdealb4w_128B+hexagon_V6_vor_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vdealb4w_128Bhexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdealb4w_128B_dsl ; hexagon_V6_vdealb4w_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t256\n\t8\n\t0\n\t256\n\t8\n\t0\n\t256\n\t8\n\t0\n\t256\n\t8\n\t4\n\t32\n\t16\n\t4\n\t8\n\t64\n\t4\n\t8\n\t96\n\t16\n\t4\n\t8\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vdealb4w_128B_dsl ; hexagon_V6_vdealb4w_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t4\n\t\t32\n\t\t16\n\t\t4\n\t\t8\n\t\t64\n\t\t4\n\t\t8\n\t\t96\n\t\t16\n\t\t4\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_vdealb4w_128B_dsl ; hexagon_V6_vdealb4w_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t4\n\t\t32\n\t\t16\n\t\t4\n\t\t8\n\t\t64\n\t\t4\n\t\t8\n\t\t96\n\t\t16\n\t\t4\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vrmpybv_128B+hexagon_V6_vmpyewuh_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vrmpybv_128Bhexagon_V6_vmpyewuh_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_acc_128B\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyewuh_128B_dsl ; hexagon_V6_vmpyewuh_128B\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000010 (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t\t64\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyewuh_128B_dsl ; hexagon_V6_vmpyewuh_128B\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000010 (bitvector 64)))\n\t (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_acc_128B\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t8\n\t\t-1\n\t\t1\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_acc_128B\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t8\n\t\t-1\n\t\t1\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t0\n\t64\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vrmpybus_acc_128B+hexagon_V6_vdmpyhvsat_acc_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vrmpybus_acc_128Bhexagon_V6_vdmpyhvsat_acc_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vrmpybus_acc_128B_dsl ; hexagon_V6_vrmpybus_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t (hexagon_V6_vrmpybus_acc_128B_dsl ; hexagon_V6_vrmpybus_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t8\n\t\t-1\n\t\t1\n\t\t1\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t (hexagon_V6_vrmpybus_acc_128B_dsl ; hexagon_V6_vrmpybus_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t8\n\t\t-1\n\t\t1\n\t\t1\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+hexagon_V6_vminuh_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128Bhexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+hexagon_V6_vor_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128Bhexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpabusv_128B+hexagon_V6_vmpabusv_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpabusv_128Bhexagon_V6_vmpabusv_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmpabusv_128B_dsl ; hexagon_V6_vmpabusv_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t (hexagon_V6_vmpabusv_128B_dsl ; hexagon_V6_vmpabusv_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t\t2048\n\t\t2048\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t-1\n\t\t0\n\t\t0\n\t\t1024\n\t\t0\n\t\t0\n\t\t16\n\t\t1024\n\t\t-1\n\t\t0\n\t\t0\n\t\t1032\n\t\t0\n\t\t0\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t2048\n\t2048\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t-1\n\t0\n\t0\n\t1024\n\t0\n\t0\n\t16\n\t1024\n\t-1\n\t0\n\t0\n\t1032\n\t0\n\t0\n\t8\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpabusv_128B_dsl ; hexagon_V6_vmpabusv_128B\n\t (hexagon_V6_vmpabusv_128B_dsl ; hexagon_V6_vmpabusv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i16> False\n\t\t2048\n\t\t2048\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t-1\n\t\t0\n\t\t0\n\t\t1024\n\t\t0\n\t\t0\n\t\t16\n\t\t1024\n\t\t-1\n\t\t0\n\t\t0\n\t\t1032\n\t\t0\n\t\t0\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vmpabusv_128B_dsl ; hexagon_V6_vmpabusv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t\t2048\n\t\t2048\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t-1\n\t\t0\n\t\t0\n\t\t1024\n\t\t0\n\t\t0\n\t\t16\n\t\t1024\n\t\t-1\n\t\t0\n\t\t0\n\t\t1032\n\t\t0\n\t\t0\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t2048\n\t2048\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t-1\n\t0\n\t0\n\t1024\n\t0\n\t0\n\t16\n\t1024\n\t-1\n\t0\n\t0\n\t1032\n\t0\n\t0\n\t8\n\t2\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vor_128B+hexagon_V6_vmux_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vor_128Bhexagon_V6_vmux_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t8\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vor_128B+hexagon_V6_vor_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vor_128Bhexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasruwuhsat_128B+hexagon_V6_vor_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vasruwuhsat_128Bhexagon_V6_vor_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vasruwuhsat_128B_dsl ; hexagon_V6_vasruwuhsat_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t0\n\t32\n\t1\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vasruwuhsat_128B_dsl ; hexagon_V6_vasruwuhsat_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t32\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t (hexagon_V6_vasruwuhsat_128B_dsl ; hexagon_V6_vasruwuhsat_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t32\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyowh_rnd_sacc_128B+hexagon_V6_vmpyowh_rnd_sacc_128B+(3, 4)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyowh_rnd_sacc_128Bhexagon_V6_vmpyowh_rnd_sacc_128B",
                "indices": [
                    3,
                    4
                ],
                "input_expression": " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyowh_rnd_sacc_128B+hexagon_V6_vmpyowh_128B+(3, 4)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyowh_rnd_sacc_128Bhexagon_V6_vmpyowh_128B",
                "indices": [
                    3,
                    4
                ],
                "input_expression": " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyowh_rnd_sacc_128B+hexagon_V6_vmpyowh_128B+(4, 5)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyowh_rnd_sacc_128Bhexagon_V6_vmpyowh_128B",
                "indices": [
                    4,
                    5
                ],
                "input_expression": " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyowh_rnd_sacc_128B+hexagon_V6_vmpyowh_rnd_sacc_128B+(4, 5)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyowh_rnd_sacc_128Bhexagon_V6_vmpyowh_rnd_sacc_128B",
                "indices": [
                    4,
                    5
                ],
                "input_expression": " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyowh_rnd_sacc_128B+hexagon_V6_vmpyowh_128B+(3, 5)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyowh_rnd_sacc_128Bhexagon_V6_vmpyowh_128B",
                "indices": [
                    3,
                    5
                ],
                "input_expression": " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyowh_128B_dsl ; hexagon_V6_vmpyowh_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t1\n\t64\n\t1\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyowh_rnd_sacc_128B+hexagon_V6_vmpyowh_rnd_sacc_128B+(3, 5)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmpyowh_rnd_sacc_128Bhexagon_V6_vmpyowh_rnd_sacc_128B",
                "indices": [
                    3,
                    5
                ],
                "input_expression": " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrwh_128B+hexagon_V6_vor_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vasrwh_128Bhexagon_V6_vor_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vasrwh_128B_dsl ; hexagon_V6_vasrwh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vasrwh_128B_dsl ; hexagon_V6_vasrwh_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vasrwh_128B_dsl ; hexagon_V6_vasrwh_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmaxw_128B+hexagon_V6_vmaxw_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vmaxw_128Bhexagon_V6_vmaxw_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhubsat_128B+hexagon_V6_vminuh_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vasrhubsat_128Bhexagon_V6_vminuh_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t1\n\t32\n\t16\n\t1\n\t0\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhubsat_128B+hexagon_V6_vor_128B+(1, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vasrhubsat_128Bhexagon_V6_vor_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t1\n\t32\n\t16\n\t1\n\t0\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vlsrwv_128B+hexagon_V6_vor_128B+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vlsrwv_128Bhexagon_V6_vor_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vlsrwv_128B_dsl ; hexagon_V6_vlsrwv_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(lit (bv #x00000000000000000000000000000000 (bitvector 32)))\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vlsrwv_128B_dsl ; hexagon_V6_vlsrwv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x00000000000000000000000000000000 (bitvector 32)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vlsrwv_128B_dsl ; hexagon_V6_vlsrwv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x00000000000000000000000000000000 (bitvector 32)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaddbq_128B+hexagon_V6_vmux_128B+(0, 3)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vaddbq_128Bhexagon_V6_vmux_128B",
                "indices": [
                    0,
                    3
                ],
                "input_expression": " (hexagon_V6_vaddbq_128B_dsl ; hexagon_V6_vaddbq_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 8 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t-1\n\t1\n\t8\n\t0\n )",
                "output_expression": " (hexagon_V6_vmux_128B_dsl ; hexagon_V6_vmux_128B\n\t (hexagon_V6_vaddbq_128B_dsl ; hexagon_V6_vaddbq_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t-1\n\t\t1\n\t\t8\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 8 x i16> False\n\t(lit (bv #b1 (bitvector 1)))\n\t (hexagon_V6_vaddbq_128B_dsl ; hexagon_V6_vaddbq_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t(reg (bv 3 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t-1\n\t\t1\n\t\t8\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t1\n\t8\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhv_128B+hexagon_V6_vminuh_128B+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vasrhv_128Bhexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhv_128B+hexagon_V6_vor_128B+(0, 2)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vasrhv_128Bhexagon_V6_vor_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhsat_acc_128B+hexagon_V6_vdmpyhvsat_acc_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vdmpyhsat_acc_128Bhexagon_V6_vdmpyhvsat_acc_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdmpyhsat_acc_128B_dsl ; hexagon_V6_vdmpyhsat_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t (hexagon_V6_vdmpyhsat_acc_128B_dsl ; hexagon_V6_vdmpyhsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vdmpyhsat_acc_128B_dsl ; hexagon_V6_vdmpyhsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhsat_acc_128B+hexagon_V6_vrmpybv_128B+(0, 1)": [
        {
            "property_name": "Distributive",
            "property": {
                "candidate": "hexagon_V6_vdmpyhsat_acc_128Bhexagon_V6_vrmpybv_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdmpyhsat_acc_128B_dsl ; hexagon_V6_vdmpyhsat_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_acc_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t8\n\t\t-1\n\t\t1\n\t\t1\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_acc_128B\n\t (hexagon_V6_vdmpyhsat_acc_128B_dsl ; hexagon_V6_vdmpyhsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t (hexagon_V6_vdmpyhsat_acc_128B_dsl ; hexagon_V6_vdmpyhsat_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t1\n\t0\n )"
            }
        }
    ]
}