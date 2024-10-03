hvx_SwizzleTransfer={
    "hexagon_V6_vmpyih_128B+hvx_swizzle_122+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhv_128B+hvx_swizzle_122+[0, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrhv_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+hvx_swizzle_122+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t16\n\t1\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+hvx_swizzle_43+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t-1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t-1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+hvx_swizzle_122+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+hvx_swizzle_43+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t16\n\t1\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasruhubrndsat_128B+hvx_swizzle_1+[3, 4]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasruhubrndsat_128B",
                "indices": [
                    3,
                    4
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vasruhubrndsat_128B_dsl ; hexagon_V6_vasruhubrndsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t-1\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t0\n\t\t32\n\t\t-1\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vasruhubrndsat_128B_dsl ; hexagon_V6_vasruhubrndsat_128B\n\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t-1\n\t0\n\t32\n\t16\n\t1\n\t0\n\t-1\n\t0\n\t32\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslh_acc_128B+hvx_swizzle_43+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaslh_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vminuh_128B+hvx_swizzle_43+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+hvx_swizzle_1+[0, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyhvsrs_128B+hvx_swizzle_43+[4, 5]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpyhvsrs_128B",
                "indices": [
                    4,
                    5
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vmpyhvsrs_128B_dsl ; hexagon_V6_vmpyhvsrs_128B\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t1\n\t\t64\n\t\t1\n\t\t1\n\t\t-1\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyhvsrs_128B_dsl ; hexagon_V6_vmpyhvsrs_128B\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 64)))\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t32\n\t1\n\t1\n\t1\n\t64\n\t1\n\t1\n\t-1\n\t32\n\t16\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhubsat_128B+hvx_swizzle_122+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrhubsat_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t1\n\t32\n\t16\n\t1\n\t0\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+hvx_swizzle_1+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+hvx_swizzle_43+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhv_128B+hvx_swizzle_43+[0, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrhv_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vrounduhub_128B+hvx_swizzle_43+[4, 5]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vrounduhub_128B",
                "indices": [
                    4,
                    5
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vrounduhub_128B_dsl ; hexagon_V6_vrounduhub_128B\n\t\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t-1\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vrounduhub_128B_dsl ; hexagon_V6_vrounduhub_128B\n\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t-1\n\t16\n\t1\n\t0\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+hvx_swizzle_122+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+hvx_swizzle_1+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t2\n\t8\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+hvx_swizzle_1+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vor_128B+hvx_swizzle_43+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasruhubrndsat_128B+hvx_swizzle_122+[3, 4]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasruhubrndsat_128B",
                "indices": [
                    3,
                    4
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vasruhubrndsat_128B_dsl ; hexagon_V6_vasruhubrndsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t-1\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t0\n\t\t32\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vasruhubrndsat_128B_dsl ; hexagon_V6_vasruhubrndsat_128B\n\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t-1\n\t0\n\t32\n\t16\n\t1\n\t0\n\t-1\n\t0\n\t32\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+hvx_swizzle_122+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+hvx_swizzle_1+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vrounduhub_128B+hvx_swizzle_1+[4, 5]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vrounduhub_128B",
                "indices": [
                    4,
                    5
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vrounduhub_128B_dsl ; hexagon_V6_vrounduhub_128B\n\t\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t-1\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vrounduhub_128B_dsl ; hexagon_V6_vrounduhub_128B\n\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t-1\n\t16\n\t1\n\t0\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhubsat_128B+hvx_swizzle_1+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrhubsat_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t1\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t1\n\t32\n\t16\n\t1\n\t0\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+hvx_swizzle_43+[0, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+hvx_swizzle_43+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrh_acc_128B+hvx_swizzle_122+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrh_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vrounduhub_128B+hvx_swizzle_122+[4, 5]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vrounduhub_128B",
                "indices": [
                    4,
                    5
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vrounduhub_128B_dsl ; hexagon_V6_vrounduhub_128B\n\t\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t-1\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vrounduhub_128B_dsl ; hexagon_V6_vrounduhub_128B\n\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t(lit (bv #x0000000000000080 (bitvector 16)))\n\t(lit (bv #x0000000000000008 (bitvector 16)))\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t-1\n\t16\n\t1\n\t0\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vor_128B+hvx_swizzle_122+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+hvx_swizzle_43+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vor_128B+hvx_swizzle_1+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vminuh_128B+hvx_swizzle_122+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasruhubrndsat_128B+hvx_swizzle_43+[3, 4]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasruhubrndsat_128B",
                "indices": [
                    3,
                    4
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vasruhubrndsat_128B_dsl ; hexagon_V6_vasruhubrndsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t-1\n\t\t0\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t0\n\t\t32\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vasruhubrndsat_128B_dsl ; hexagon_V6_vasruhubrndsat_128B\n\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t-1\n\t0\n\t32\n\t16\n\t1\n\t0\n\t-1\n\t0\n\t32\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vminuh_128B+hvx_swizzle_1+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+hvx_swizzle_1+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t16\n\t1\n\t0\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhv_128B+hvx_swizzle_1+[0, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrhv_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrhv_128B_dsl ; hexagon_V6_vasrhv_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+hvx_swizzle_1+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t-1\n\t\t1\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t-1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslh_acc_128B+hvx_swizzle_1+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaslh_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+hvx_swizzle_1+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrhubsat_128B+hvx_swizzle_43+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrhubsat_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1\n\t\t0\n\t\t1\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrhubsat_128B_dsl ; hexagon_V6_vasrhubsat_128B\n\t(lit (bv #x00000000000000000000000000000007 (bitvector 32)))\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t0\n\t1\n\t32\n\t16\n\t1\n\t0\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyhvsrs_128B+hvx_swizzle_1+[4, 5]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpyhvsrs_128B",
                "indices": [
                    4,
                    5
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vmpyhvsrs_128B_dsl ; hexagon_V6_vmpyhvsrs_128B\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t1\n\t\t64\n\t\t1\n\t\t1\n\t\t-1\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyhvsrs_128B_dsl ; hexagon_V6_vmpyhvsrs_128B\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 64)))\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t32\n\t1\n\t1\n\t1\n\t64\n\t1\n\t1\n\t-1\n\t32\n\t16\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vmpyhvsrs_128B+hvx_swizzle_122+[4, 5]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpyhvsrs_128B",
                "indices": [
                    4,
                    5
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vmpyhvsrs_128B_dsl ; hexagon_V6_vmpyhvsrs_128B\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 64)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t1\n\t\t64\n\t\t1\n\t\t1\n\t\t-1\n\t\t32\n\t\t16\n\t\t1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vmpyhvsrs_128B_dsl ; hexagon_V6_vmpyhvsrs_128B\n\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000002 (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 64)))\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t32\n\t1\n\t1\n\t1\n\t64\n\t1\n\t1\n\t-1\n\t32\n\t16\n\t1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslh_acc_128B+hvx_swizzle_122+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaslh_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+hvx_swizzle_122+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t-1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t-1\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+hvx_swizzle_122+[0, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vaslhv_128B_dsl ; hexagon_V6_vaslhv_128B\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t(lit (bv #x0000000000000000 (bitvector 16)))\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+hvx_swizzle_122+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t2\n\t8\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrh_acc_128B+hvx_swizzle_43+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrh_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vasrh_acc_128B+hvx_swizzle_1+[1, 2]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrh_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t1\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 3 (bitvector 8))) ; < 2 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )"
            }
        }
    ],
    "hexagon_V6_vor_128B+hvx_swizzle_18+[0, 1]": [
        {
            "property_name": "SwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_18_dsl ; hvx_swizzle_16\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t8\n\t8\n\t0\n\t8\n\t8\n\t1016\n\t1000\n\t984\n\t968\n\t952\n\t936\n\t920\n\t904\n\t888\n\t872\n\t856\n\t840\n\t824\n\t808\n\t792\n\t776\n\t760\n\t744\n\t728\n\t712\n\t696\n\t680\n\t664\n\t648\n\t632\n\t616\n\t600\n\t584\n\t568\n\t552\n\t536\n\t520\n\t504\n\t1008\n\t992\n\t488\n\t976\n\t960\n\t472\n\t944\n\t928\n\t456\n\t912\n\t896\n\t440\n\t880\n\t864\n\t424\n\t848\n\t832\n\t408\n\t816\n\t800\n\t392\n\t784\n\t768\n\t376\n\t752\n\t736\n\t360\n\t720\n\t704\n\t344\n\t688\n\t672\n\t328\n\t656\n\t640\n\t312\n\t624\n\t608\n\t296\n\t592\n\t576\n\t280\n\t560\n\t544\n\t264\n\t528\n\t512\n\t248\n\t496\n\t480\n\t232\n\t464\n\t448\n\t216\n\t432\n\t416\n\t200\n\t400\n\t384\n\t184\n\t368\n\t352\n\t168\n\t336\n\t320\n\t152\n\t304\n\t288\n\t136\n\t272\n\t256\n\t120\n\t240\n\t224\n\t104\n\t208\n\t192\n\t88\n\t176\n\t160\n\t72\n\t144\n\t128\n\t56\n\t112\n\t96\n\t40\n\t80\n\t64\n\t24\n\t48\n\t32\n\t8\n\t16\n\t0\n\t0\n )",
                "output_expression": " (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t (hvx_swizzle_18_dsl ; hvx_swizzle_16\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t8\n\t\t8\n\t\t0\n\t\t8\n\t\t8\n\t\t1016\n\t\t1000\n\t\t984\n\t\t968\n\t\t952\n\t\t936\n\t\t920\n\t\t904\n\t\t888\n\t\t872\n\t\t856\n\t\t840\n\t\t824\n\t\t808\n\t\t792\n\t\t776\n\t\t760\n\t\t744\n\t\t728\n\t\t712\n\t\t696\n\t\t680\n\t\t664\n\t\t648\n\t\t632\n\t\t616\n\t\t600\n\t\t584\n\t\t568\n\t\t552\n\t\t536\n\t\t520\n\t\t504\n\t\t1008\n\t\t992\n\t\t488\n\t\t976\n\t\t960\n\t\t472\n\t\t944\n\t\t928\n\t\t456\n\t\t912\n\t\t896\n\t\t440\n\t\t880\n\t\t864\n\t\t424\n\t\t848\n\t\t832\n\t\t408\n\t\t816\n\t\t800\n\t\t392\n\t\t784\n\t\t768\n\t\t376\n\t\t752\n\t\t736\n\t\t360\n\t\t720\n\t\t704\n\t\t344\n\t\t688\n\t\t672\n\t\t328\n\t\t656\n\t\t640\n\t\t312\n\t\t624\n\t\t608\n\t\t296\n\t\t592\n\t\t576\n\t\t280\n\t\t560\n\t\t544\n\t\t264\n\t\t528\n\t\t512\n\t\t248\n\t\t496\n\t\t480\n\t\t232\n\t\t464\n\t\t448\n\t\t216\n\t\t432\n\t\t416\n\t\t200\n\t\t400\n\t\t384\n\t\t184\n\t\t368\n\t\t352\n\t\t168\n\t\t336\n\t\t320\n\t\t152\n\t\t304\n\t\t288\n\t\t136\n\t\t272\n\t\t256\n\t\t120\n\t\t240\n\t\t224\n\t\t104\n\t\t208\n\t\t192\n\t\t88\n\t\t176\n\t\t160\n\t\t72\n\t\t144\n\t\t128\n\t\t56\n\t\t112\n\t\t96\n\t\t40\n\t\t80\n\t\t64\n\t\t24\n\t\t48\n\t\t32\n\t\t8\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_18_dsl ; hvx_swizzle_16\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t8\n\t\t8\n\t\t0\n\t\t8\n\t\t8\n\t\t1016\n\t\t1000\n\t\t984\n\t\t968\n\t\t952\n\t\t936\n\t\t920\n\t\t904\n\t\t888\n\t\t872\n\t\t856\n\t\t840\n\t\t824\n\t\t808\n\t\t792\n\t\t776\n\t\t760\n\t\t744\n\t\t728\n\t\t712\n\t\t696\n\t\t680\n\t\t664\n\t\t648\n\t\t632\n\t\t616\n\t\t600\n\t\t584\n\t\t568\n\t\t552\n\t\t536\n\t\t520\n\t\t504\n\t\t1008\n\t\t992\n\t\t488\n\t\t976\n\t\t960\n\t\t472\n\t\t944\n\t\t928\n\t\t456\n\t\t912\n\t\t896\n\t\t440\n\t\t880\n\t\t864\n\t\t424\n\t\t848\n\t\t832\n\t\t408\n\t\t816\n\t\t800\n\t\t392\n\t\t784\n\t\t768\n\t\t376\n\t\t752\n\t\t736\n\t\t360\n\t\t720\n\t\t704\n\t\t344\n\t\t688\n\t\t672\n\t\t328\n\t\t656\n\t\t640\n\t\t312\n\t\t624\n\t\t608\n\t\t296\n\t\t592\n\t\t576\n\t\t280\n\t\t560\n\t\t544\n\t\t264\n\t\t528\n\t\t512\n\t\t248\n\t\t496\n\t\t480\n\t\t232\n\t\t464\n\t\t448\n\t\t216\n\t\t432\n\t\t416\n\t\t200\n\t\t400\n\t\t384\n\t\t184\n\t\t368\n\t\t352\n\t\t168\n\t\t336\n\t\t320\n\t\t152\n\t\t304\n\t\t288\n\t\t136\n\t\t272\n\t\t256\n\t\t120\n\t\t240\n\t\t224\n\t\t104\n\t\t208\n\t\t192\n\t\t88\n\t\t176\n\t\t160\n\t\t72\n\t\t144\n\t\t128\n\t\t56\n\t\t112\n\t\t96\n\t\t40\n\t\t80\n\t\t64\n\t\t24\n\t\t48\n\t\t32\n\t\t8\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )"
            }
        }
    ]
}