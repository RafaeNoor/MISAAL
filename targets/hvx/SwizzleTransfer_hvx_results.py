hvx_SwizzleTransfer={
    "hexagon_V6_vminuh_128B+hexagon_V6_vshuffh_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vminuh_128B+hexagon_V6_vdealb_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrh_acc_128B+hexagon_V6_vdealb_128B+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrh_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrh_acc_128B+hexagon_V6_vshuffh_128B+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrh_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslh_acc_128B+hexagon_V6_vshuffh_128B+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaslh_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslh_acc_128B+hexagon_V6_vdealb_128B+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaslh_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+hexagon_V6_vdealb_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t-1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t-1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+hexagon_V6_vshuffh_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t-1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t-1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+hexagon_V6_vshuffh_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+hexagon_V6_vshuffh_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+hexagon_V6_vdealb_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasruhubrndsat_128B+hexagon_V6_vdealb_128B+[3, 4]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasruhubrndsat_128B",
                "indices": [
                    3,
                    4
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vasruhubrndsat_128B_dsl ; hexagon_V6_vasruhubrndsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t-1\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t0\n\t\t32\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vasruhubrndsat_128B_dsl ; hexagon_V6_vasruhubrndsat_128B\n\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t-1\n\t0\n\t32\n\t16\n\t1\n\t0\n\t-1\n\t0\n\t32\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+hexagon_V6_vdealb_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasruhubrndsat_128B+hexagon_V6_vshuffh_128B+[3, 4]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasruhubrndsat_128B",
                "indices": [
                    3,
                    4
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vasruhubrndsat_128B_dsl ; hexagon_V6_vasruhubrndsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t-1\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t0\n\t\t32\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vasruhubrndsat_128B_dsl ; hexagon_V6_vasruhubrndsat_128B\n\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t-1\n\t0\n\t32\n\t16\n\t1\n\t0\n\t-1\n\t0\n\t32\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+hexagon_V6_vdealb_128B+[0, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+hexagon_V6_vshuffh_128B+[0, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+hexagon_V6_vdealb_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+hexagon_V6_vshuffh_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+hexagon_V6_vdealb_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t16\n\t1\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vrounduhub_128B+hexagon_V6_vdealb_128B+[4, 5]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vrounduhub_128B",
                "indices": [
                    4,
                    5
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vrounduhub_128B_dsl ; hexagon_V6_vrounduhub_128B\n\t\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t-1\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vrounduhub_128B_dsl ; hexagon_V6_vrounduhub_128B\n\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t-1\n\t16\n\t1\n\t0\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+hexagon_V6_vshuffh_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t16\n\t1\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vrounduhub_128B+hexagon_V6_vshuffh_128B+[4, 5]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vrounduhub_128B",
                "indices": [
                    4,
                    5
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vrounduhub_128B_dsl ; hexagon_V6_vrounduhub_128B\n\t\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t-1\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vrounduhub_128B_dsl ; hexagon_V6_vrounduhub_128B\n\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t-1\n\t16\n\t1\n\t0\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vor_128B+hexagon_V6_vdealb_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vor_128B+hexagon_V6_vshuffh_128B+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhubsat_128B+hexagon_V6_vdealb_128B+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrhubsat_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t1\n\t32\n\t16\n\t1\n\t0\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhubsat_128B+hexagon_V6_vshuffh_128B+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrhubsat_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t1\n\t32\n\t16\n\t1\n\t0\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhv_128B+hexagon_V6_vshuffh_128B+[0, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrhv_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhv_128B+hexagon_V6_vdealb_128B+[0, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrhv_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ]
}