hvx_Commutative={
    "hexagon_V6_veqw_xor_128B_(2, 3)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_veqw_xor_128B",
                "indices": [
                    2,
                    3
                ],
                "input_expression": " (hexagon_V6_veqw_xor_128B_dsl ; hexagon_V6_veqw_xor_128B\n\t(lit (bv #x000f (bitvector 4)))\n\t(lit (bv #x0000 (bitvector 4)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t4\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_veqw_xor_128B_dsl ; hexagon_V6_veqw_xor_128B\n\t(lit (bv #x000f (bitvector 4)))\n\t(lit (bv #x0000 (bitvector 4)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t4\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B_(1, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vmpyih_acc_128B_dsl ; hexagon_V6_vmpyih_acc_128B\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyih_acc_128B_dsl ; hexagon_V6_vmpyih_acc_128B\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrw_acc_128B_(0, 3)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vasrw_acc_128B",
                "indices": [
                    0,
                    3
                ],
                "input_expression": " (hexagon_V6_vasrw_acc_128B_dsl ; hexagon_V6_vasrw_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrw_acc_128B_dsl ; hexagon_V6_vasrw_acc_128B\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vminuh_128B_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslw_acc_128B_(0, 3)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vaslw_acc_128B",
                "indices": [
                    0,
                    3
                ],
                "input_expression": " (hexagon_V6_vaslw_acc_128B_dsl ; hexagon_V6_vaslw_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslw_acc_128B_dsl ; hexagon_V6_vaslw_acc_128B\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaddcarrysat_128B_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vaddcarrysat_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vaddcarrysat_128B_dsl ; hexagon_V6_vaddcarrysat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t32\n\t1\n\t32\n\t1\n\t1\n\t1\n\t4\n\t-1\n\t0\n )",
                "output_expression": " (hexagon_V6_vaddcarrysat_128B_dsl ; hexagon_V6_vaddcarrysat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t32\n\t1\n\t32\n\t1\n\t1\n\t1\n\t4\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_pred_and_128B_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_pred_and_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_pred_and_128B_dsl ; hexagon_V6_pred_and_128B\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vaddubh_128B_dsl ; hexagon_V6_vaddubh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t0\n\t-1\n\t16\n\t1024\n\t0\n\t-1\n\t8\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vaddubh_128B_dsl ; hexagon_V6_vaddubh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t0\n\t-1\n\t16\n\t1024\n\t0\n\t-1\n\t8\n\t2\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t-1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t-1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_veqw_or_128B_(0, 3)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_veqw_or_128B",
                "indices": [
                    0,
                    3
                ],
                "input_expression": " (hexagon_V6_veqw_or_128B_dsl ; hexagon_V6_veqw_or_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(lit (bv #x0000 (bitvector 4)))\n\t(lit (bv #x000f (bitvector 4)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t4\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_veqw_or_128B_dsl ; hexagon_V6_veqw_or_128B\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(lit (bv #x0000 (bitvector 4)))\n\t(lit (bv #x000f (bitvector 4)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t4\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vlsrh_128B_(0, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vlsrh_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vlsrh_128B_dsl ; hexagon_V6_vlsrh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t32\n\t0\n )",
                "output_expression": " (hexagon_V6_vlsrh_128B_dsl ; hexagon_V6_vlsrh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslh_128B_(0, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vaslh_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vaslh_128B_dsl ; hexagon_V6_vaslh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslh_128B_dsl ; hexagon_V6_vaslh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vlsrw_128B_(0, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vlsrw_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vlsrw_128B_dsl ; hexagon_V6_vlsrw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )",
                "output_expression": " (hexagon_V6_vlsrw_128B_dsl ; hexagon_V6_vlsrw_128B\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_veqw_128B_(1, 3)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_veqw_128B",
                "indices": [
                    1,
                    3
                ],
                "input_expression": " (hexagon_V6_veqw_128B_dsl ; hexagon_V6_veqw_128B\n\t(lit (bv #x000f (bitvector 4)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(lit (bv #x0000 (bitvector 4)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t4\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_veqw_128B_dsl ; hexagon_V6_veqw_128B\n\t(lit (bv #x000f (bitvector 4)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(lit (bv #x0000 (bitvector 4)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t4\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B_(1, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vdmpyhvsat_acc_128B_dsl ; hexagon_V6_vdmpyhvsat_acc_128B\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t1\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vrmpybv_128B_(1, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vrmpybv_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_acc_128B\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vrmpybv_128B_dsl ; hexagon_V6_vrmpybv_acc_128B\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t8\n\t-1\n\t1\n\t1\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_veqh_and_128B_(2, 3)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_veqh_and_128B",
                "indices": [
                    2,
                    3
                ],
                "input_expression": " (hexagon_V6_veqh_and_128B_dsl ; hexagon_V6_veqh_and_128B\n\t(lit (bv #b11 (bitvector 2)))\n\t(lit (bv #b00 (bitvector 2)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t2\n\t16\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_veqh_and_128B_dsl ; hexagon_V6_veqh_and_128B\n\t(lit (bv #b11 (bitvector 2)))\n\t(lit (bv #b00 (bitvector 2)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t2\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpabusv_128B_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vmpabusv_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmpabusv_128B_dsl ; hexagon_V6_vmpabusv_128B\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i16> False\n\t2048\n\t2048\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t-1\n\t0\n\t0\n\t1024\n\t0\n\t0\n\t16\n\t1024\n\t-1\n\t0\n\t0\n\t1032\n\t0\n\t0\n\t8\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpabusv_128B_dsl ; hexagon_V6_vmpabusv_128B\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t2048\n\t2048\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t-1\n\t0\n\t0\n\t1024\n\t0\n\t0\n\t16\n\t1024\n\t-1\n\t0\n\t0\n\t1032\n\t0\n\t0\n\t8\n\t2\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vor_128B_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasruwuhsat_128B_(0, 3)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vasruwuhsat_128B",
                "indices": [
                    0,
                    3
                ],
                "input_expression": " (hexagon_V6_vasruwuhsat_128B_dsl ; hexagon_V6_vasruwuhsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t0\n\t32\n\t1\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vasruwuhsat_128B_dsl ; hexagon_V6_vasruwuhsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t0\n\t32\n\t1\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_pred_xor_128B_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_pred_xor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_pred_xor_128B_dsl ; hexagon_V6_pred_xor_128B\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_pred_xor_128B_dsl ; hexagon_V6_pred_xor_128B\n\t(reg (bv 1 (bitvector 8))) ; < 8 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i16> False\n\t128\n\t128\n\t0\n\t128\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaddubh_acc_128B_(1, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vaddubh_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vaddubh_acc_128B_dsl ; hexagon_V6_vaddubh_acc_128B\n\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t-1\n\t1\n\t-1\n\t16\n\t-1\n\t1\n\t-1\n\t8\n\t1024\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vaddubh_acc_128B_dsl ; hexagon_V6_vaddubh_acc_128B\n\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t-1\n\t1\n\t-1\n\t16\n\t-1\n\t1\n\t-1\n\t8\n\t1024\n\t2\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vavgwrnd_128B_(2, 3)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vavgwrnd_128B",
                "indices": [
                    2,
                    3
                ],
                "input_expression": " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavgwrnd_128B\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t-1\n\t-1\n\t0\n )",
                "output_expression": " (hexagon_V6_vavgwrnd_128B_dsl ; hexagon_V6_vavgwrnd_128B\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t-1\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrwh_128B_(0, 3)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vasrwh_128B",
                "indices": [
                    0,
                    3
                ],
                "input_expression": " (hexagon_V6_vasrwh_128B_dsl ; hexagon_V6_vasrwh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrwh_128B_dsl ; hexagon_V6_vasrwh_128B\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasruwuhrndsat_128B_(0, 5)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vasruwuhrndsat_128B",
                "indices": [
                    0,
                    5
                ],
                "input_expression": " (hexagon_V6_vasruwuhrndsat_128B_dsl ; hexagon_V6_vasruwuhrndsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t0\n\t-1\n\t32\n\t1\n\t0\n\t-1\n\t-1\n\t0\n )",
                "output_expression": " (hexagon_V6_vasruwuhrndsat_128B_dsl ; hexagon_V6_vasruwuhrndsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t0\n\t-1\n\t32\n\t1\n\t0\n\t-1\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslw_128B_(0, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vaslw_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vaslw_128B_dsl ; hexagon_V6_vaslw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslw_128B_dsl ; hexagon_V6_vaslw_128B\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmaxw_128B_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vmaxw_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vmaxw_128B_dsl ; hexagon_V6_vmaxw_128B\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vavguw_128B_(1, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vavguw_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavguw_128B\n\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t0\n )",
                "output_expression": " (hexagon_V6_vavguw_128B_dsl ; hexagon_V6_vavguw_128B\n\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhubsat_128B_(0, 3)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vasrhubsat_128B",
                "indices": [
                    0,
                    3
                ],
                "input_expression": " (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t1\n\t32\n\t16\n\t1\n\t0\n\t1\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t(reg (bv 1 (bitvector 8))) ; < 2 x i16> False\n\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t1\n\t32\n\t16\n\t1\n\t0\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B_(0, 1)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmpybv_128B_dsl ; hexagon_V6_vmpybv_128B\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t1\n\t1\n\t16\n\t1024\n\t1\n\t1\n\t8\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpybv_128B_dsl ; hexagon_V6_vmpybv_128B\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t1\n\t1\n\t16\n\t1024\n\t1\n\t1\n\t8\n\t2\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpybv_acc_128B_(1, 2)": [
        {
            "property_name": "Commutative",
            "property": {
                "candidate": "hexagon_V6_vmpybv_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vmpybv_acc_128B_dsl ; hexagon_V6_vmpybv_acc_128B\n\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t-1\n\t1\n\t1\n\t16\n\t-1\n\t1\n\t1\n\t8\n\t1024\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpybv_acc_128B_dsl ; hexagon_V6_vmpybv_acc_128B\n\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t-1\n\t1\n\t1\n\t16\n\t-1\n\t1\n\t1\n\t8\n\t1024\n\t2\n\t0\n )"
            }
        }
    ]
}