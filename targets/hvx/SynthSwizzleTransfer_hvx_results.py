hvx_SynthSwizzleTransfer={
    "hexagon_V6_vshufoeh_128B+hvx_swizzle_43+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_43\n\t (hexagon_V6_vshufoeh_128B_dsl ; hexagon_V6_vshufoeh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t1040\n\t\t1024\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t2048\n\t32\n\t0\n\t32\n\t16\n\t64\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vcombine_128B_dsl\n (hvx_swizzle_654_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  32\n  32\n  512\n  2\n  0)\n (hvx_swizzle_651_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  32\n  32\n  2\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 0\n 1024\n 8\n 1024\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+hvx_swizzle_43+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t2\n\t16\n\t0\n )",
                "output_expression": "(hvx_swizzle_1_dsl\n (hvx_swizzle_651_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  16\n  2\n  0)\n 16\n 16\n 0\n 16\n 16\n 1008\n 976\n 944\n 912\n 880\n 848\n 816\n 784\n 752\n 720\n 688\n 656\n 624\n 592\n 560\n 528\n 496\n 992\n 960\n 464\n 928\n 896\n 432\n 864\n 832\n 400\n 800\n 768\n 368\n 736\n 704\n 336\n 672\n 640\n 304\n 608\n 576\n 272\n 544\n 512\n 240\n 480\n 448\n 208\n 416\n 384\n 176\n 352\n 320\n 144\n 288\n 256\n 112\n 224\n 192\n 80\n 160\n 128\n 48\n 96\n 64\n 16\n 32\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+hvx_swizzle_18+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_18_dsl ; hvx_swizzle_16\n\t (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t8\n\t8\n\t0\n\t8\n\t8\n\t1016\n\t1000\n\t984\n\t968\n\t952\n\t936\n\t920\n\t904\n\t888\n\t872\n\t856\n\t840\n\t824\n\t808\n\t792\n\t776\n\t760\n\t744\n\t728\n\t712\n\t696\n\t680\n\t664\n\t648\n\t632\n\t616\n\t600\n\t584\n\t568\n\t552\n\t536\n\t520\n\t504\n\t1008\n\t992\n\t488\n\t976\n\t960\n\t472\n\t944\n\t928\n\t456\n\t912\n\t896\n\t440\n\t880\n\t864\n\t424\n\t848\n\t832\n\t408\n\t816\n\t800\n\t392\n\t784\n\t768\n\t376\n\t752\n\t736\n\t360\n\t720\n\t704\n\t344\n\t688\n\t672\n\t328\n\t656\n\t640\n\t312\n\t624\n\t608\n\t296\n\t592\n\t576\n\t280\n\t560\n\t544\n\t264\n\t528\n\t512\n\t248\n\t496\n\t480\n\t232\n\t464\n\t448\n\t216\n\t432\n\t416\n\t200\n\t400\n\t384\n\t184\n\t368\n\t352\n\t168\n\t336\n\t320\n\t152\n\t304\n\t288\n\t136\n\t272\n\t256\n\t120\n\t240\n\t224\n\t104\n\t208\n\t192\n\t88\n\t176\n\t160\n\t72\n\t144\n\t128\n\t56\n\t112\n\t96\n\t40\n\t80\n\t64\n\t24\n\t48\n\t32\n\t8\n\t16\n\t0\n\t0\n )",
                "output_expression": "(hexagon_V6_vpackwuh_sat_128B_dsl\n (reg (bv #x00 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 8\n 0\n 512\n 8\n 0\n 16\n 1\n 64\n 0\n 16\n 1\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+hvx_swizzle_1+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t (hexagon_V6_vsubuhw_128B_dsl ; hexagon_V6_vsubuhw_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t\t-1\n\t\t32\n\t\t1024\n\t\t0\n\t\t-1\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t2016\n\t1952\n\t1888\n\t1824\n\t1760\n\t1696\n\t1632\n\t1568\n\t1504\n\t1440\n\t1376\n\t1312\n\t1248\n\t1184\n\t1120\n\t1056\n\t992\n\t1984\n\t1920\n\t928\n\t1856\n\t1792\n\t864\n\t1728\n\t1664\n\t800\n\t1600\n\t1536\n\t736\n\t1472\n\t1408\n\t672\n\t1344\n\t1280\n\t608\n\t1216\n\t1152\n\t544\n\t1088\n\t1024\n\t480\n\t960\n\t896\n\t416\n\t832\n\t768\n\t352\n\t704\n\t640\n\t288\n\t576\n\t512\n\t224\n\t448\n\t384\n\t160\n\t320\n\t256\n\t96\n\t192\n\t128\n\t32\n\t64\n\t0\n\t0\n )",
                "output_expression": "(hexagon_V6_vsubuhw_128B_dsl\n (hvx_swizzle_1_dsl\n  (reg (bv #x00 8))\n  16\n  16\n  0\n  16\n  16\n  1008\n  976\n  944\n  912\n  880\n  848\n  816\n  784\n  752\n  720\n  688\n  656\n  624\n  592\n  560\n  528\n  496\n  992\n  960\n  464\n  928\n  896\n  432\n  864\n  832\n  400\n  800\n  768\n  368\n  736\n  704\n  336\n  672\n  640\n  304\n  608\n  576\n  272\n  544\n  512\n  240\n  480\n  448\n  208\n  416\n  384\n  176\n  352\n  320\n  144\n  288\n  256\n  112\n  224\n  192\n  80\n  160\n  128\n  48\n  96\n  64\n  16\n  32\n  0\n  0)\n (hvx_swizzle_1_dsl\n  (reg (bv #x01 8))\n  16\n  16\n  0\n  16\n  16\n  1008\n  976\n  944\n  912\n  880\n  848\n  816\n  784\n  752\n  720\n  688\n  656\n  624\n  592\n  560\n  528\n  496\n  992\n  960\n  464\n  928\n  896\n  432\n  864\n  832\n  400\n  800\n  768\n  368\n  736\n  704\n  336\n  672\n  640\n  304\n  608\n  576\n  272\n  544\n  512\n  240\n  480\n  448\n  208\n  416\n  384\n  176\n  352\n  320\n  144\n  288\n  256\n  112\n  224\n  192\n  80\n  160\n  128\n  48\n  96\n  64\n  16\n  32\n  0\n  0)\n 1024\n 1024\n 0\n 512\n 16\n 0\n 512\n 16\n 32\n 1\n 0\n -1\n 32\n 1024\n 0\n -1\n 16\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+hvx_swizzle_43+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vsubuhw_128B_dsl ; hexagon_V6_vsubuhw_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t32\n\t1\n\t0\n\t-1\n\t32\n\t1024\n\t0\n\t-1\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vunpackh_128B_dsl\n (hexagon_V6_vsubh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  1024\n  16\n  -1\n  0)\n 1024\n 1024\n 0\n 1024\n 16\n 32\n 1\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+hvx_swizzle_18+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_18_dsl ; hvx_swizzle_16\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t8\n\t8\n\t0\n\t8\n\t8\n\t1016\n\t1000\n\t984\n\t968\n\t952\n\t936\n\t920\n\t904\n\t888\n\t872\n\t856\n\t840\n\t824\n\t808\n\t792\n\t776\n\t760\n\t744\n\t728\n\t712\n\t696\n\t680\n\t664\n\t648\n\t632\n\t616\n\t600\n\t584\n\t568\n\t552\n\t536\n\t520\n\t504\n\t1008\n\t992\n\t488\n\t976\n\t960\n\t472\n\t944\n\t928\n\t456\n\t912\n\t896\n\t440\n\t880\n\t864\n\t424\n\t848\n\t832\n\t408\n\t816\n\t800\n\t392\n\t784\n\t768\n\t376\n\t752\n\t736\n\t360\n\t720\n\t704\n\t344\n\t688\n\t672\n\t328\n\t656\n\t640\n\t312\n\t624\n\t608\n\t296\n\t592\n\t576\n\t280\n\t560\n\t544\n\t264\n\t528\n\t512\n\t248\n\t496\n\t480\n\t232\n\t464\n\t448\n\t216\n\t432\n\t416\n\t200\n\t400\n\t384\n\t184\n\t368\n\t352\n\t168\n\t336\n\t320\n\t152\n\t304\n\t288\n\t136\n\t272\n\t256\n\t120\n\t240\n\t224\n\t104\n\t208\n\t192\n\t88\n\t176\n\t160\n\t72\n\t144\n\t128\n\t56\n\t112\n\t96\n\t40\n\t80\n\t64\n\t24\n\t48\n\t32\n\t8\n\t16\n\t0\n\t0\n )",
                "output_expression": "(hexagon_V6_vpackeh_128B_dsl\n (reg (bv #x00 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 8\n 0\n 512\n 8\n 2\n 64\n 2\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+hvx_swizzle_18+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_18_dsl ; hvx_swizzle_18\n\t (hexagon_V6_vaddubh_128B_dsl ; hexagon_V6_vaddubh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t16\n\t\t1024\n\t\t0\n\t\t-1\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t2032\n\t2000\n\t1968\n\t1936\n\t1904\n\t1872\n\t1840\n\t1808\n\t1776\n\t1744\n\t1712\n\t1680\n\t1648\n\t1616\n\t1584\n\t1552\n\t1520\n\t1488\n\t1456\n\t1424\n\t1392\n\t1360\n\t1328\n\t1296\n\t1264\n\t1232\n\t1200\n\t1168\n\t1136\n\t1104\n\t1072\n\t1040\n\t1008\n\t2016\n\t1984\n\t976\n\t1952\n\t1920\n\t944\n\t1888\n\t1856\n\t912\n\t1824\n\t1792\n\t880\n\t1760\n\t1728\n\t848\n\t1696\n\t1664\n\t816\n\t1632\n\t1600\n\t784\n\t1568\n\t1536\n\t752\n\t1504\n\t1472\n\t720\n\t1440\n\t1408\n\t688\n\t1376\n\t1344\n\t656\n\t1312\n\t1280\n\t624\n\t1248\n\t1216\n\t592\n\t1184\n\t1152\n\t560\n\t1120\n\t1088\n\t528\n\t1056\n\t1024\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": "(hexagon_V6_vaddubh_128B_dsl\n (hvx_swizzle_18_dsl\n  (reg (bv #x00 8))\n  8\n  8\n  0\n  8\n  8\n  1016\n  1000\n  984\n  968\n  952\n  936\n  920\n  904\n  888\n  872\n  856\n  840\n  824\n  808\n  792\n  776\n  760\n  744\n  728\n  712\n  696\n  680\n  664\n  648\n  632\n  616\n  600\n  584\n  568\n  552\n  536\n  520\n  504\n  1008\n  992\n  488\n  976\n  960\n  472\n  944\n  928\n  456\n  912\n  896\n  440\n  880\n  864\n  424\n  848\n  832\n  408\n  816\n  800\n  392\n  784\n  768\n  376\n  752\n  736\n  360\n  720\n  704\n  344\n  688\n  672\n  328\n  656\n  640\n  312\n  624\n  608\n  296\n  592\n  576\n  280\n  560\n  544\n  264\n  528\n  512\n  248\n  496\n  480\n  232\n  464\n  448\n  216\n  432\n  416\n  200\n  400\n  384\n  184\n  368\n  352\n  168\n  336\n  320\n  152\n  304\n  288\n  136\n  272\n  256\n  120\n  240\n  224\n  104\n  208\n  192\n  88\n  176\n  160\n  72\n  144\n  128\n  56\n  112\n  96\n  40\n  80\n  64\n  24\n  48\n  32\n  8\n  16\n  0\n  0)\n (hvx_swizzle_18_dsl\n  (reg (bv #x01 8))\n  8\n  8\n  0\n  8\n  8\n  1016\n  1000\n  984\n  968\n  952\n  936\n  920\n  904\n  888\n  872\n  856\n  840\n  824\n  808\n  792\n  776\n  760\n  744\n  728\n  712\n  696\n  680\n  664\n  648\n  632\n  616\n  600\n  584\n  568\n  552\n  536\n  520\n  504\n  1008\n  992\n  488\n  976\n  960\n  472\n  944\n  928\n  456\n  912\n  896\n  440\n  880\n  864\n  424\n  848\n  832\n  408\n  816\n  800\n  392\n  784\n  768\n  376\n  752\n  736\n  360\n  720\n  704\n  344\n  688\n  672\n  328\n  656\n  640\n  312\n  624\n  608\n  296\n  592\n  576\n  280\n  560\n  544\n  264\n  528\n  512\n  248\n  496\n  480\n  232\n  464\n  448\n  216\n  432\n  416\n  200\n  400\n  384\n  184\n  368\n  352\n  168\n  336\n  320\n  152\n  304\n  288\n  136\n  272\n  256\n  120\n  240\n  224\n  104\n  208\n  192\n  88\n  176\n  160\n  72\n  144\n  128\n  56\n  112\n  96\n  40\n  80\n  64\n  24\n  48\n  32\n  8\n  16\n  0\n  0)\n 1024\n 1024\n 0\n 512\n 8\n 0\n 512\n 8\n 16\n 1\n 0\n -1\n 16\n 1024\n 0\n -1\n 8\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vswap_128B+hvx_swizzle_88+[0, 2]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vswap_128B",
                "indices": [
                    0,
                    2
                ],
                "input_expression": " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hexagon_V6_vswap_128B_dsl ; hexagon_V6_vswap_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 16 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t(lit (bv #b1 (bitvector 1)))\n\t\t128\n\t\t128\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t\t128\n\t\t1\n\t\t1\n\t\t8\n\t\t8\n\t\t1024\n\t\t1\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "output_expression": "(hexagon_V6_vmux_128B_dsl\n (reg (bv #x00 8))\n (reg (bv #x02 8))\n (lit (bv #b1 1))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 1024\n 8\n 1\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+hvx_swizzle_43+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_2\n\t (hexagon_V6_vsubuhw_128B_dsl ; hexagon_V6_vsubuhw_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t\t-1\n\t\t32\n\t\t1024\n\t\t0\n\t\t-1\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t2048\n\t64\n\t0\n\t64\n\t32\n\t32\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vunpackh_128B_dsl\n (hexagon_V6_vsubh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  1024\n  16\n  -1\n  0)\n 1024\n 1024\n 0\n 1024\n 16\n 32\n 1\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vshufoeh_128B+hvx_swizzle_43+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshufoeh_128B_dsl ; hexagon_V6_vshufoeh_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t16\n\t2\n\t1040\n\t1024\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vcombine_128B_dsl\n (hvx_swizzle_654_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  16\n  512\n  2\n  0)\n (hvx_swizzle_651_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  16\n  2\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 0\n 1024\n 8\n 1024\n 0)"
            }
        }
    ],
    "hexagon_V6_vmpyieoh_128B+hvx_swizzle_122+[1, 2]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpyieoh_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vmpyieoh_128B_dsl ; hexagon_V6_vmpyieoh_128B\n\t\t(lit (bv #x00000000000000000000000000000010 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": "(lit\n (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024))"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+hvx_swizzle_43+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwuh_sat_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t\t32\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vsathub_128B_dsl\n (reg (bv #x00 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 0\n 32\n 1\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+hvx_swizzle_654+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_654_dsl ; hvx_swizzle_267\n\t (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t512\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vshuffeb_128B_dsl\n (reg (bv #x02 8))\n (reg (bv #x00 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+hvx_swizzle_43+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": "(hvx_swizzle_1_dsl\n (hvx_swizzle_654_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  16\n  512\n  2\n  0)\n 16\n 16\n 0\n 16\n 16\n 1008\n 976\n 944\n 912\n 880\n 848\n 816\n 784\n 752\n 720\n 688\n 656\n 624\n 592\n 560\n 528\n 496\n 992\n 960\n 464\n 928\n 896\n 432\n 864\n 832\n 400\n 800\n 768\n 368\n 736\n 704\n 336\n 672\n 640\n 304\n 608\n 576\n 272\n 544\n 512\n 240\n 480\n 448\n 208\n 416\n 384\n 176\n 352\n 320\n 144\n 288\n 256\n 112\n 224\n 192\n 80\n 160\n 128\n 48\n 96\n 64\n 16\n 32\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+hvx_swizzle_18+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_18_dsl ; hvx_swizzle_18\n\t (hexagon_V6_vmpybv_128B_dsl ; hexagon_V6_vmpybv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t16\n\t\t1024\n\t\t1\n\t\t1\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t2032\n\t2000\n\t1968\n\t1936\n\t1904\n\t1872\n\t1840\n\t1808\n\t1776\n\t1744\n\t1712\n\t1680\n\t1648\n\t1616\n\t1584\n\t1552\n\t1520\n\t1488\n\t1456\n\t1424\n\t1392\n\t1360\n\t1328\n\t1296\n\t1264\n\t1232\n\t1200\n\t1168\n\t1136\n\t1104\n\t1072\n\t1040\n\t1008\n\t2016\n\t1984\n\t976\n\t1952\n\t1920\n\t944\n\t1888\n\t1856\n\t912\n\t1824\n\t1792\n\t880\n\t1760\n\t1728\n\t848\n\t1696\n\t1664\n\t816\n\t1632\n\t1600\n\t784\n\t1568\n\t1536\n\t752\n\t1504\n\t1472\n\t720\n\t1440\n\t1408\n\t688\n\t1376\n\t1344\n\t656\n\t1312\n\t1280\n\t624\n\t1248\n\t1216\n\t592\n\t1184\n\t1152\n\t560\n\t1120\n\t1088\n\t528\n\t1056\n\t1024\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": "(hexagon_V6_vmpybv_acc_128B_dsl\n (lit\n  (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))\n (hvx_swizzle_18_dsl\n  (reg (bv #x00 8))\n  8\n  8\n  0\n  8\n  8\n  1016\n  1000\n  984\n  968\n  952\n  936\n  920\n  904\n  888\n  872\n  856\n  840\n  824\n  808\n  792\n  776\n  760\n  744\n  728\n  712\n  696\n  680\n  664\n  648\n  632\n  616\n  600\n  584\n  568\n  552\n  536\n  520\n  504\n  1008\n  992\n  488\n  976\n  960\n  472\n  944\n  928\n  456\n  912\n  896\n  440\n  880\n  864\n  424\n  848\n  832\n  408\n  816\n  800\n  392\n  784\n  768\n  376\n  752\n  736\n  360\n  720\n  704\n  344\n  688\n  672\n  328\n  656\n  640\n  312\n  624\n  608\n  296\n  592\n  576\n  280\n  560\n  544\n  264\n  528\n  512\n  248\n  496\n  480\n  232\n  464\n  448\n  216\n  432\n  416\n  200\n  400\n  384\n  184\n  368\n  352\n  168\n  336\n  320\n  152\n  304\n  288\n  136\n  272\n  256\n  120\n  240\n  224\n  104\n  208\n  192\n  88\n  176\n  160\n  72\n  144\n  128\n  56\n  112\n  96\n  40\n  80\n  64\n  24\n  48\n  32\n  8\n  16\n  0\n  0)\n (hvx_swizzle_18_dsl\n  (reg (bv #x01 8))\n  8\n  8\n  0\n  8\n  8\n  1016\n  1000\n  984\n  968\n  952\n  936\n  920\n  904\n  888\n  872\n  856\n  840\n  824\n  808\n  792\n  776\n  760\n  744\n  728\n  712\n  696\n  680\n  664\n  648\n  632\n  616\n  600\n  584\n  568\n  552\n  536\n  520\n  504\n  1008\n  992\n  488\n  976\n  960\n  472\n  944\n  928\n  456\n  912\n  896\n  440\n  880\n  864\n  424\n  848\n  832\n  408\n  816\n  800\n  392\n  784\n  768\n  376\n  752\n  736\n  360\n  720\n  704\n  344\n  688\n  672\n  328\n  656\n  640\n  312\n  624\n  608\n  296\n  592\n  576\n  280\n  560\n  544\n  264\n  528\n  512\n  248\n  496\n  480\n  232\n  464\n  448\n  216\n  432\n  416\n  200\n  400\n  384\n  184\n  368\n  352\n  168\n  336\n  320\n  152\n  304\n  288\n  136\n  272\n  256\n  120\n  240\n  224\n  104\n  208\n  192\n  88\n  176\n  160\n  72\n  144\n  128\n  56\n  112\n  96\n  40\n  80\n  64\n  24\n  48\n  32\n  8\n  16\n  0\n  0)\n 1024\n 1024\n 0\n 512\n 8\n 0\n 512\n 8\n 16\n 1\n -1\n 1\n 1\n 16\n -1\n 1\n 1\n 8\n 1024\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vmpybv_acc_128B+hvx_swizzle_88+[1, 2]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpybv_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hexagon_V6_vmpybv_acc_128B_dsl ; hexagon_V6_vmpybv_acc_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t-1\n\t\t1\n\t\t1\n\t\t16\n\t\t-1\n\t\t1\n\t\t1\n\t\t8\n\t\t1024\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "output_expression": "(hexagon_V6_vassign_128B_dsl\n (hexagon_V6_vmpybv_acc_128B_dsl\n  (reg (bv #x02 8))\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  8\n  0\n  512\n  8\n  16\n  1\n  -1\n  1\n  1\n  16\n  -1\n  1\n  1\n  8\n  1024\n  2\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+hvx_swizzle_654+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_654_dsl ; hvx_swizzle_283\n\t (hexagon_V6_vcombine_128B_dsl ; hexagon_V6_vcombine_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t (hexagon_V6_vcombine_128B_dsl ; hexagon_V6_vcombine_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t512\n\t2\n\t0\n )",
                "output_expression": "(hvx_swizzle_654_dsl\n (reg (bv #x01 8))\n (reg (bv #x03 8))\n 1024\n 1024\n 0\n 512\n 8\n 8\n 512\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+hvx_swizzle_88+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hexagon_V6_vaddubh_128B_dsl ; hexagon_V6_vaddubh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t16\n\t\t1024\n\t\t0\n\t\t-1\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "output_expression": "(hexagon_V6_vassign_128B_dsl\n (hexagon_V6_vaddubh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  8\n  0\n  512\n  8\n  16\n  1\n  0\n  -1\n  16\n  1024\n  0\n  -1\n  8\n  2\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+hvx_swizzle_88+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hexagon_V6_vmpybv_128B_dsl ; hexagon_V6_vmpybv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t16\n\t\t1024\n\t\t1\n\t\t1\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "output_expression": "(hexagon_V6_vassign_128B_dsl\n (hexagon_V6_vmpybv_acc_128B_dsl\n  (lit\n   (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  8\n  0\n  512\n  8\n  16\n  1\n  -1\n  1\n  1\n  16\n  -1\n  1\n  1\n  8\n  1024\n  2\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vmpahb_acc_128B+hvx_swizzle_88+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpahb_acc_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_88_dsl ; hvx_swizzle_196\n\t (hexagon_V6_vmpahb_acc_128B_dsl ; hexagon_V6_vmpahb_acc_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t256\n\t\t8\n\t\t0\n\t\t256\n\t\t8\n\t\t32\n\t\t1\n\t\t-1\n\t\t-1\n\t\t1\n\t\t1\n\t\t8\n\t\t16\n\t\t1024\n\t\t1\n\t\t1\n\t\t0\n\t\t16\n\t\t32\n\t\t-1\n\t\t-1\n\t\t1\n\t\t1\n\t\t24\n\t\t16\n\t\t1040\n\t\t1\n\t\t1\n\t\t16\n\t\t16\n\t\t16\n\t\t1024\n\t\t4\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )",
                "output_expression": "(hexagon_V6_vassign_128B_dsl\n (hexagon_V6_vmpahb_acc_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  (reg (bv #x02 8))\n  32\n  32\n  0\n  256\n  8\n  0\n  256\n  8\n  32\n  1\n  -1\n  -1\n  1\n  1\n  8\n  16\n  1024\n  1\n  1\n  0\n  16\n  32\n  -1\n  -1\n  1\n  1\n  24\n  16\n  1040\n  1\n  1\n  16\n  16\n  16\n  1024\n  4\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+hvx_swizzle_651+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_651_dsl ; hvx_swizzle_69\n\t (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vshuffeb_128B_dsl\n (reg (bv #x03 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+hvx_swizzle_43+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_43\n\t (hexagon_V6_vaddubh_128B_dsl ; hexagon_V6_vaddubh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t16\n\t\t1024\n\t\t0\n\t\t-1\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t2048\n\t32\n\t0\n\t32\n\t16\n\t64\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vunpackh_128B_dsl\n (hexagon_V6_vaddhsat_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  1024\n  8\n  -1\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 16\n 1\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+hvx_swizzle_651+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_651_dsl ; hvx_swizzle_237\n\t (hexagon_V6_vcombine_128B_dsl ; hexagon_V6_vcombine_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t (hexagon_V6_vcombine_128B_dsl ; hexagon_V6_vcombine_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t2048\n\t2048\n\t0\n\t1024\n\t8\n\t8\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vcombine_128B_dsl\n (hvx_swizzle_654_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x03 8))\n  1024\n  1024\n  0\n  512\n  8\n  8\n  512\n  2\n  0)\n (hvx_swizzle_651_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x03 8))\n  1024\n  1024\n  0\n  512\n  8\n  8\n  2\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 0\n 1024\n 8\n 1024\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+hvx_swizzle_654+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_654_dsl ; hvx_swizzle_267\n\t (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwuh_sat_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t\t32\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwuh_sat_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t\t32\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t512\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vsathub_128B_dsl\n (reg (bv #x02 8))\n (reg (bv #x00 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 0\n 32\n 1\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+hvx_swizzle_43+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )",
                "output_expression": "(hvx_swizzle_651_dsl\n (reg (bv #x01 8))\n (reg (bv #x00 8))\n 1024\n 1024\n 0\n 512\n 8\n 8\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+hvx_swizzle_43+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_17\n\t (hexagon_V6_vcombine_128B_dsl ; hexagon_V6_vcombine_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t1024\n\t16\n\t0\n\t16\n\t8\n\t64\n\t2\n\t0\n )",
                "output_expression": "(hvx_swizzle_43_dsl (reg (bv #x01 8)) 1024 16 0 16 8 64 2 0)"
            }
        }
    ],
    "hexagon_V6_vshufoeh_128B+hvx_swizzle_88+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hexagon_V6_vshufoeh_128B_dsl ; hexagon_V6_vshufoeh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t1040\n\t\t1024\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "output_expression": "(hexagon_V6_vshuffeb_128B_dsl\n (reg (bv #x00 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+hvx_swizzle_43+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t2\n\t8\n\t0\n )",
                "output_expression": "(hvx_swizzle_654_dsl\n (reg (bv #x01 8))\n (reg (bv #x00 8))\n 1024\n 1024\n 0\n 512\n 8\n 8\n 512\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+hvx_swizzle_43+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": "(hvx_swizzle_654_dsl\n (hvx_swizzle_1_dsl\n  (reg (bv #x01 8))\n  16\n  16\n  0\n  16\n  16\n  1008\n  976\n  944\n  912\n  880\n  848\n  816\n  784\n  752\n  720\n  688\n  656\n  624\n  592\n  560\n  528\n  496\n  992\n  960\n  464\n  928\n  896\n  432\n  864\n  832\n  400\n  800\n  768\n  368\n  736\n  704\n  336\n  672\n  640\n  304\n  608\n  576\n  272\n  544\n  512\n  240\n  480\n  448\n  208\n  416\n  384\n  176\n  352\n  320\n  144\n  288\n  256\n  112\n  224\n  192\n  80\n  160\n  128\n  48\n  96\n  64\n  16\n  32\n  0\n  0)\n (hvx_swizzle_1_dsl\n  (reg (bv #x00 8))\n  16\n  16\n  0\n  16\n  16\n  1008\n  976\n  944\n  912\n  880\n  848\n  816\n  784\n  752\n  720\n  688\n  656\n  624\n  592\n  560\n  528\n  496\n  992\n  960\n  464\n  928\n  896\n  432\n  864\n  832\n  400\n  800\n  768\n  368\n  736\n  704\n  336\n  672\n  640\n  304\n  608\n  576\n  272\n  544\n  512\n  240\n  480\n  448\n  208\n  416\n  384\n  176\n  352\n  320\n  144\n  288\n  256\n  112\n  224\n  192\n  80\n  160\n  128\n  48\n  96\n  64\n  16\n  32\n  0\n  0)\n 1024\n 1024\n 0\n 512\n 16\n 16\n 512\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vminuh_128B+hvx_swizzle_122+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vminuh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hexagon_V6_vminuh_128B_dsl ; hexagon_V6_vminuh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vminuh_128B_dsl\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n 1024\n 1024\n 0\n 1024\n 16\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+hvx_swizzle_651+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_651_dsl ; hvx_swizzle_69\n\t (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwuh_sat_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t\t32\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwuh_sat_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 32 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t\t32\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vsathub_128B_dsl\n (reg (bv #x03 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 0\n 32\n 1\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vshufoeh_128B+hvx_swizzle_18+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_18_dsl ; hvx_swizzle_18\n\t (hexagon_V6_vshufoeh_128B_dsl ; hexagon_V6_vshufoeh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t1040\n\t\t1024\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t2032\n\t2000\n\t1968\n\t1936\n\t1904\n\t1872\n\t1840\n\t1808\n\t1776\n\t1744\n\t1712\n\t1680\n\t1648\n\t1616\n\t1584\n\t1552\n\t1520\n\t1488\n\t1456\n\t1424\n\t1392\n\t1360\n\t1328\n\t1296\n\t1264\n\t1232\n\t1200\n\t1168\n\t1136\n\t1104\n\t1072\n\t1040\n\t1008\n\t2016\n\t1984\n\t976\n\t1952\n\t1920\n\t944\n\t1888\n\t1856\n\t912\n\t1824\n\t1792\n\t880\n\t1760\n\t1728\n\t848\n\t1696\n\t1664\n\t816\n\t1632\n\t1600\n\t784\n\t1568\n\t1536\n\t752\n\t1504\n\t1472\n\t720\n\t1440\n\t1408\n\t688\n\t1376\n\t1344\n\t656\n\t1312\n\t1280\n\t624\n\t1248\n\t1216\n\t592\n\t1184\n\t1152\n\t560\n\t1120\n\t1088\n\t528\n\t1056\n\t1024\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "output_expression": "(hexagon_V6_vcombine_128B_dsl\n (hvx_swizzle_1_dsl\n  (reg (bv #x00 8))\n  16\n  16\n  0\n  16\n  16\n  1008\n  976\n  944\n  912\n  880\n  848\n  816\n  784\n  752\n  720\n  688\n  656\n  624\n  592\n  560\n  528\n  496\n  992\n  960\n  464\n  928\n  896\n  432\n  864\n  832\n  400\n  800\n  768\n  368\n  736\n  704\n  336\n  672\n  640\n  304\n  608\n  576\n  272\n  544\n  512\n  240\n  480\n  448\n  208\n  416\n  384\n  176\n  352\n  320\n  144\n  288\n  256\n  112\n  224\n  192\n  80\n  160\n  128\n  48\n  96\n  64\n  16\n  32\n  0\n  0)\n (hvx_swizzle_1_dsl\n  (reg (bv #x01 8))\n  16\n  16\n  0\n  16\n  16\n  1008\n  976\n  944\n  912\n  880\n  848\n  816\n  784\n  752\n  720\n  688\n  656\n  624\n  592\n  560\n  528\n  496\n  992\n  960\n  464\n  928\n  896\n  432\n  864\n  832\n  400\n  800\n  768\n  368\n  736\n  704\n  336\n  672\n  640\n  304\n  608\n  576\n  272\n  544\n  512\n  240\n  480\n  448\n  208\n  416\n  384\n  176\n  352\n  320\n  144\n  288\n  256\n  112\n  224\n  192\n  80\n  160\n  128\n  48\n  96\n  64\n  16\n  32\n  0\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 0\n 1024\n 8\n 1024\n 0)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+hvx_swizzle_43+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_43\n\t (hexagon_V6_vmpybv_128B_dsl ; hexagon_V6_vmpybv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t16\n\t\t1024\n\t\t1\n\t\t1\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t2048\n\t32\n\t0\n\t32\n\t16\n\t64\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vmpybv_acc_128B_dsl\n (lit\n  (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 2048))\n (hvx_swizzle_43_dsl (reg (bv #x00 8)) 1024 16 0 16 8 64 2 0)\n (hvx_swizzle_43_dsl (reg (bv #x01 8)) 1024 16 0 16 8 64 2 0)\n 1024\n 1024\n 0\n 512\n 8\n 0\n 512\n 8\n 16\n 1\n -1\n 1\n 1\n 16\n -1\n 1\n 1\n 8\n 1024\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+hvx_swizzle_88+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_88_dsl ; hvx_swizzle_196\n\t (hexagon_V6_vsubuhw_128B_dsl ; hexagon_V6_vsubuhw_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t\t-1\n\t\t32\n\t\t1024\n\t\t0\n\t\t-1\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )",
                "output_expression": "(hexagon_V6_vassign_128B_dsl\n (hexagon_V6_vsubuhw_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  32\n  1\n  0\n  -1\n  32\n  1024\n  0\n  -1\n  16\n  2\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+hvx_swizzle_43+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vshuffeb_128B_dsl\n (reg (bv #x00 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+hvx_swizzle_88+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hexagon_V6_vcombine_128B_dsl ; hexagon_V6_vcombine_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "output_expression": "(reg (bv #x01 8))"
            }
        }
    ],
    "hexagon_V6_vaddubh_acc_128B+hvx_swizzle_88+[1, 2]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaddubh_acc_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hexagon_V6_vaddubh_acc_128B_dsl ; hexagon_V6_vaddubh_acc_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t-1\n\t\t1\n\t\t-1\n\t\t16\n\t\t-1\n\t\t1\n\t\t-1\n\t\t8\n\t\t1024\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "output_expression": "(hexagon_V6_vassign_128B_dsl\n (hexagon_V6_vaddubh_acc_128B_dsl\n  (reg (bv #x02 8))\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  8\n  0\n  512\n  8\n  16\n  1\n  -1\n  1\n  -1\n  16\n  -1\n  1\n  -1\n  8\n  1024\n  2\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vmpabusv_128B+hvx_swizzle_88+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpabusv_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hexagon_V6_vmpabusv_128B_dsl ; hexagon_V6_vmpabusv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 256 x i8> False\n\t\t2048\n\t\t2048\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t-1\n\t\t0\n\t\t0\n\t\t1024\n\t\t0\n\t\t0\n\t\t16\n\t\t1024\n\t\t-1\n\t\t0\n\t\t0\n\t\t1032\n\t\t0\n\t\t0\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "output_expression": "(hexagon_V6_vassign_128B_dsl\n (hexagon_V6_vmpabusv_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  2048\n  2048\n  0\n  512\n  8\n  0\n  512\n  8\n  16\n  1\n  -1\n  0\n  0\n  1024\n  0\n  0\n  16\n  1024\n  -1\n  0\n  0\n  1032\n  0\n  0\n  8\n  2\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+hvx_swizzle_43+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vaddubh_128B_dsl ; hexagon_V6_vaddubh_128B\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t0\n\t-1\n\t16\n\t1024\n\t0\n\t-1\n\t8\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vunpackh_128B_dsl\n (hexagon_V6_vaddhsat_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  1024\n  8\n  -1\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 16\n 1\n 0\n 0)"
            }
        }
    ]
}