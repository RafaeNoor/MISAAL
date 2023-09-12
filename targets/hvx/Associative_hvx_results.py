hvx_Associative={
    "hexagon_V6_pred_and_128B_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "hexagon_V6_pred_and_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t1\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vminuh_128B_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "hexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vor_128B_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_pred_xor_128B_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "hexagon_V6_pred_xor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_pred_xor_128B_dsl ; hexagon_V6_pred_xor_128B\n\t (hexagon_V6_pred_xor_128B_dsl ; hexagon_V6_pred_xor_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_pred_xor_128B_dsl ; hexagon_V6_pred_xor_128B\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t (hexagon_V6_pred_xor_128B_dsl ; hexagon_V6_pred_xor_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t\t128\n\t\t128\n\t\t0\n\t\t128\n\t\t1\n\t\t0\n\t )\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmaxw_128B_(0, 1)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "hexagon_V6_vmaxw_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B_(1, 2)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyowh_rnd_sacc_128B_(4, 5)": [
        {
            "property_name": "Associative",
            "property": {
                "candidate": "hexagon_V6_vmpyowh_rnd_sacc_128B",
                "indices": [
                    4,
                    5
                ],
                "input_expression": " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t (hexagon_V6_vmpyowh_rnd_sacc_128B_dsl ; hexagon_V6_vmpyowh_rnd_sacc_128B\n\t\t(lit (bv #x000000000000000000000000000000000000000000000000000000000000000e (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(lit (bv #x0000000000000000000000000000000000000000000000000000000000000001 (bitvector 64)))\n\t\t(reg (bv 4 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t64\n\t\t1\n\t\t64\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t32\n\t1\n\t1\n\t-1\n\t-1\n\t1\n\t64\n\t1\n\t64\n\t1\n\t16\n\t0\n )"
            }
        }
    ]
}