hvx_SimplifyingSwizzles={
    " (hvx_swizzle_43_dsl ; hvx_swizzle_2\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t2048\n\t64\n\t0\n\t64\n\t32\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_43_dsl ; hvx_swizzle_2\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t2048\n\t64\n\t0\n\t64\n\t32\n\t32\n\t2\n\t0\n )",
                "simplified": "(reg (bv #x00 8))"
            }
        }
    ],
    " (hvx_swizzle_654_dsl ; hvx_swizzle_654\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t512\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_654_dsl ; hvx_swizzle_654\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t512\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_654_dsl\n (hvx_swizzle_122_dsl (reg (bv #x00 8)) 2048 1024 0 1024 32 2 0)\n (hvx_swizzle_122_dsl (reg (bv #x01 8)) 2048 1024 0 1024 32 2 0)\n 1024\n 1024\n 0\n 512\n 32\n 32\n 1536\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_651_dsl ; hvx_swizzle_238\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_17\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_17\n\t\t(reg (bv 1 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t8\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_651_dsl ; hvx_swizzle_238\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_17\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_17\n\t\t(reg (bv 1 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t8\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_43_dsl\n (hvx_swizzle_651_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  2048\n  2048\n  0\n  1024\n  8\n  8\n  2\n  0)\n 2048\n 32\n 0\n 32\n 16\n 64\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_2\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t2016\n\t1952\n\t1888\n\t1824\n\t1760\n\t1696\n\t1632\n\t1568\n\t1504\n\t1440\n\t1376\n\t1312\n\t1248\n\t1184\n\t1120\n\t1056\n\t992\n\t1984\n\t1920\n\t928\n\t1856\n\t1792\n\t864\n\t1728\n\t1664\n\t800\n\t1600\n\t1536\n\t736\n\t1472\n\t1408\n\t672\n\t1344\n\t1280\n\t608\n\t1216\n\t1152\n\t544\n\t1088\n\t1024\n\t480\n\t960\n\t896\n\t416\n\t832\n\t768\n\t352\n\t704\n\t640\n\t288\n\t576\n\t512\n\t224\n\t448\n\t384\n\t160\n\t320\n\t256\n\t96\n\t192\n\t128\n\t32\n\t64\n\t0\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_2\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t32\n\t32\n\t0\n\t32\n\t32\n\t2016\n\t1952\n\t1888\n\t1824\n\t1760\n\t1696\n\t1632\n\t1568\n\t1504\n\t1440\n\t1376\n\t1312\n\t1248\n\t1184\n\t1120\n\t1056\n\t992\n\t1984\n\t1920\n\t928\n\t1856\n\t1792\n\t864\n\t1728\n\t1664\n\t800\n\t1600\n\t1536\n\t736\n\t1472\n\t1408\n\t672\n\t1344\n\t1280\n\t608\n\t1216\n\t1152\n\t544\n\t1088\n\t1024\n\t480\n\t960\n\t896\n\t416\n\t832\n\t768\n\t352\n\t704\n\t640\n\t288\n\t576\n\t512\n\t224\n\t448\n\t384\n\t160\n\t320\n\t256\n\t96\n\t192\n\t128\n\t32\n\t64\n\t0\n\t0\n )",
                "simplified": "(reg (bv #x00 8))"
            }
        }
    ],
    " (hvx_swizzle_651_dsl ; hvx_swizzle_651\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_196\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_196\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_651_dsl ; hvx_swizzle_651\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_196\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_196\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_651_dsl\n (reg (bv #x00 8))\n (reg (bv #x02 8))\n 1024\n 1024\n 0\n 512\n 32\n 32\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_18_dsl ; hvx_swizzle_18\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_43\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t2048\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t2032\n\t2000\n\t1968\n\t1936\n\t1904\n\t1872\n\t1840\n\t1808\n\t1776\n\t1744\n\t1712\n\t1680\n\t1648\n\t1616\n\t1584\n\t1552\n\t1520\n\t1488\n\t1456\n\t1424\n\t1392\n\t1360\n\t1328\n\t1296\n\t1264\n\t1232\n\t1200\n\t1168\n\t1136\n\t1104\n\t1072\n\t1040\n\t1008\n\t2016\n\t1984\n\t976\n\t1952\n\t1920\n\t944\n\t1888\n\t1856\n\t912\n\t1824\n\t1792\n\t880\n\t1760\n\t1728\n\t848\n\t1696\n\t1664\n\t816\n\t1632\n\t1600\n\t784\n\t1568\n\t1536\n\t752\n\t1504\n\t1472\n\t720\n\t1440\n\t1408\n\t688\n\t1376\n\t1344\n\t656\n\t1312\n\t1280\n\t624\n\t1248\n\t1216\n\t592\n\t1184\n\t1152\n\t560\n\t1120\n\t1088\n\t528\n\t1056\n\t1024\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_18_dsl ; hvx_swizzle_18\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_43\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t2048\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t2032\n\t2000\n\t1968\n\t1936\n\t1904\n\t1872\n\t1840\n\t1808\n\t1776\n\t1744\n\t1712\n\t1680\n\t1648\n\t1616\n\t1584\n\t1552\n\t1520\n\t1488\n\t1456\n\t1424\n\t1392\n\t1360\n\t1328\n\t1296\n\t1264\n\t1232\n\t1200\n\t1168\n\t1136\n\t1104\n\t1072\n\t1040\n\t1008\n\t2016\n\t1984\n\t976\n\t1952\n\t1920\n\t944\n\t1888\n\t1856\n\t912\n\t1824\n\t1792\n\t880\n\t1760\n\t1728\n\t848\n\t1696\n\t1664\n\t816\n\t1632\n\t1600\n\t784\n\t1568\n\t1536\n\t752\n\t1504\n\t1472\n\t720\n\t1440\n\t1408\n\t688\n\t1376\n\t1344\n\t656\n\t1312\n\t1280\n\t624\n\t1248\n\t1216\n\t592\n\t1184\n\t1152\n\t560\n\t1120\n\t1088\n\t528\n\t1056\n\t1024\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "simplified": "(reg (bv #x00 8))"
            }
        }
    ],
    " (hvx_swizzle_654_dsl ; hvx_swizzle_654\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_2\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t512\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_654_dsl ; hvx_swizzle_654\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_2\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t512\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_654_dsl\n (hvx_swizzle_43_dsl (reg (bv #x00 8)) 2048 64 0 64 32 32 2 0)\n (hvx_swizzle_122_dsl (reg (bv #x01 8)) 2048 1024 0 1024 32 2 0)\n 1024\n 1024\n 0\n 512\n 32\n 32\n 512\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hvx_swizzle_654_dsl ; hvx_swizzle_267\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t512\n\t\t2\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hvx_swizzle_654_dsl ; hvx_swizzle_267\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t512\n\t\t2\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_1_dsl\n (hvx_swizzle_654_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  16\n  512\n  2\n  0)\n 16\n 16\n 0\n 16\n 16\n 1008\n 976\n 944\n 912\n 880\n 848\n 816\n 784\n 752\n 720\n 688\n 656\n 624\n 592\n 560\n 528\n 496\n 992\n 960\n 464\n 928\n 896\n 432\n 864\n 832\n 400\n 800\n 768\n 368\n 736\n 704\n 336\n 672\n 640\n 304\n 608\n 576\n 272\n 544\n 512\n 240\n 480\n 448\n 208\n 416\n 384\n 176\n 352\n 320\n 144\n 288\n 256\n 112\n 224\n 192\n 80\n 160\n 128\n 48\n 96\n 64\n 16\n 32\n 0\n 0)"
            }
        }
    ],
    " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_115\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_115\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "simplified": "(hvx_swizzle_651_dsl\n (reg (bv #x00 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_651_dsl ; hvx_swizzle_69\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_651_dsl ; hvx_swizzle_69\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_651_dsl\n (reg (bv #x00 8))\n (reg (bv #x02 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_651_dsl ; hvx_swizzle_655\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_651_dsl ; hvx_swizzle_655\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_654_dsl\n (hvx_swizzle_122_dsl (reg (bv #x00 8)) 2048 1024 0 1024 32 2 0)\n (hvx_swizzle_122_dsl (reg (bv #x01 8)) 2048 1024 0 1024 32 2 0)\n 1024\n 1024\n 0\n 512\n 32\n 32\n 1024\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_651_dsl ; hvx_swizzle_655\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_2\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_651_dsl ; hvx_swizzle_655\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_2\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_651_dsl\n (hvx_swizzle_43_dsl (reg (bv #x00 8)) 2048 64 0 64 32 32 2 0)\n (hvx_swizzle_1_dsl\n  (reg (bv #x01 8))\n  32\n  32\n  0\n  32\n  32\n  2016\n  1952\n  1888\n  1824\n  1760\n  1696\n  1632\n  1568\n  1504\n  1440\n  1376\n  1312\n  1248\n  1184\n  1120\n  1056\n  992\n  1984\n  1920\n  928\n  1856\n  1792\n  864\n  1728\n  1664\n  800\n  1600\n  1536\n  736\n  1472\n  1408\n  672\n  1344\n  1280\n  608\n  1216\n  1152\n  544\n  1088\n  1024\n  480\n  960\n  896\n  416\n  832\n  768\n  352\n  704\n  640\n  288\n  576\n  512\n  224\n  448\n  384\n  160\n  320\n  256\n  96\n  192\n  128\n  32\n  64\n  0\n  0)\n 1024\n 1024\n 0\n 512\n 32\n 32\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_654_dsl ; hvx_swizzle_654\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t512\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_654_dsl ; hvx_swizzle_654\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t512\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_654_dsl\n (hvx_swizzle_122_dsl (reg (bv #x00 8)) 2048 1024 0 1024 32 2 0)\n (hvx_swizzle_122_dsl (reg (bv #x01 8)) 2048 1024 0 1024 32 2 0)\n 1024\n 1024\n 0\n 512\n 32\n 32\n 1536\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_18_dsl ; hvx_swizzle_16\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t8\n\t8\n\t0\n\t8\n\t8\n\t1016\n\t1000\n\t984\n\t968\n\t952\n\t936\n\t920\n\t904\n\t888\n\t872\n\t856\n\t840\n\t824\n\t808\n\t792\n\t776\n\t760\n\t744\n\t728\n\t712\n\t696\n\t680\n\t664\n\t648\n\t632\n\t616\n\t600\n\t584\n\t568\n\t552\n\t536\n\t520\n\t504\n\t1008\n\t992\n\t488\n\t976\n\t960\n\t472\n\t944\n\t928\n\t456\n\t912\n\t896\n\t440\n\t880\n\t864\n\t424\n\t848\n\t832\n\t408\n\t816\n\t800\n\t392\n\t784\n\t768\n\t376\n\t752\n\t736\n\t360\n\t720\n\t704\n\t344\n\t688\n\t672\n\t328\n\t656\n\t640\n\t312\n\t624\n\t608\n\t296\n\t592\n\t576\n\t280\n\t560\n\t544\n\t264\n\t528\n\t512\n\t248\n\t496\n\t480\n\t232\n\t464\n\t448\n\t216\n\t432\n\t416\n\t200\n\t400\n\t384\n\t184\n\t368\n\t352\n\t168\n\t336\n\t320\n\t152\n\t304\n\t288\n\t136\n\t272\n\t256\n\t120\n\t240\n\t224\n\t104\n\t208\n\t192\n\t88\n\t176\n\t160\n\t72\n\t144\n\t128\n\t56\n\t112\n\t96\n\t40\n\t80\n\t64\n\t24\n\t48\n\t32\n\t8\n\t16\n\t0\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_18_dsl ; hvx_swizzle_16\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t8\n\t8\n\t0\n\t8\n\t8\n\t1016\n\t1000\n\t984\n\t968\n\t952\n\t936\n\t920\n\t904\n\t888\n\t872\n\t856\n\t840\n\t824\n\t808\n\t792\n\t776\n\t760\n\t744\n\t728\n\t712\n\t696\n\t680\n\t664\n\t648\n\t632\n\t616\n\t600\n\t584\n\t568\n\t552\n\t536\n\t520\n\t504\n\t1008\n\t992\n\t488\n\t976\n\t960\n\t472\n\t944\n\t928\n\t456\n\t912\n\t896\n\t440\n\t880\n\t864\n\t424\n\t848\n\t832\n\t408\n\t816\n\t800\n\t392\n\t784\n\t768\n\t376\n\t752\n\t736\n\t360\n\t720\n\t704\n\t344\n\t688\n\t672\n\t328\n\t656\n\t640\n\t312\n\t624\n\t608\n\t296\n\t592\n\t576\n\t280\n\t560\n\t544\n\t264\n\t528\n\t512\n\t248\n\t496\n\t480\n\t232\n\t464\n\t448\n\t216\n\t432\n\t416\n\t200\n\t400\n\t384\n\t184\n\t368\n\t352\n\t168\n\t336\n\t320\n\t152\n\t304\n\t288\n\t136\n\t272\n\t256\n\t120\n\t240\n\t224\n\t104\n\t208\n\t192\n\t88\n\t176\n\t160\n\t72\n\t144\n\t128\n\t56\n\t112\n\t96\n\t40\n\t80\n\t64\n\t24\n\t48\n\t32\n\t8\n\t16\n\t0\n\t0\n )",
                "simplified": "(reg (bv #x00 8))"
            }
        }
    ],
    " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_266\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_266\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_43_dsl\n (hvx_swizzle_651_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  2048\n  2048\n  0\n  1024\n  16\n  16\n  2\n  0)\n 1024\n 32\n 0\n 32\n 16\n 32\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t1008\n\t\t976\n\t\t944\n\t\t912\n\t\t880\n\t\t848\n\t\t816\n\t\t784\n\t\t752\n\t\t720\n\t\t688\n\t\t656\n\t\t624\n\t\t592\n\t\t560\n\t\t528\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "simplified": "(reg (bv #x00 8))"
            }
        }
    ],
    " (hvx_swizzle_43_dsl ; hvx_swizzle_628\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_115\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_43_dsl ; hvx_swizzle_628\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_115\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_43_dsl\n (hvx_swizzle_651_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  16\n  2\n  0)\n 1024\n 32\n 0\n 32\n 16\n 32\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_628\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_628\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "simplified": "(hvx_swizzle_88_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)"
            }
        }
    ],
    " (hvx_swizzle_43_dsl ; hvx_swizzle_43\n\t (hvx_swizzle_18_dsl ; hvx_swizzle_18\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t2032\n\t\t2000\n\t\t1968\n\t\t1936\n\t\t1904\n\t\t1872\n\t\t1840\n\t\t1808\n\t\t1776\n\t\t1744\n\t\t1712\n\t\t1680\n\t\t1648\n\t\t1616\n\t\t1584\n\t\t1552\n\t\t1520\n\t\t1488\n\t\t1456\n\t\t1424\n\t\t1392\n\t\t1360\n\t\t1328\n\t\t1296\n\t\t1264\n\t\t1232\n\t\t1200\n\t\t1168\n\t\t1136\n\t\t1104\n\t\t1072\n\t\t1040\n\t\t1008\n\t\t2016\n\t\t1984\n\t\t976\n\t\t1952\n\t\t1920\n\t\t944\n\t\t1888\n\t\t1856\n\t\t912\n\t\t1824\n\t\t1792\n\t\t880\n\t\t1760\n\t\t1728\n\t\t848\n\t\t1696\n\t\t1664\n\t\t816\n\t\t1632\n\t\t1600\n\t\t784\n\t\t1568\n\t\t1536\n\t\t752\n\t\t1504\n\t\t1472\n\t\t720\n\t\t1440\n\t\t1408\n\t\t688\n\t\t1376\n\t\t1344\n\t\t656\n\t\t1312\n\t\t1280\n\t\t624\n\t\t1248\n\t\t1216\n\t\t592\n\t\t1184\n\t\t1152\n\t\t560\n\t\t1120\n\t\t1088\n\t\t528\n\t\t1056\n\t\t1024\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t2048\n\t32\n\t0\n\t32\n\t16\n\t64\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_43_dsl ; hvx_swizzle_43\n\t (hvx_swizzle_18_dsl ; hvx_swizzle_18\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t16\n\t\t16\n\t\t0\n\t\t16\n\t\t16\n\t\t2032\n\t\t2000\n\t\t1968\n\t\t1936\n\t\t1904\n\t\t1872\n\t\t1840\n\t\t1808\n\t\t1776\n\t\t1744\n\t\t1712\n\t\t1680\n\t\t1648\n\t\t1616\n\t\t1584\n\t\t1552\n\t\t1520\n\t\t1488\n\t\t1456\n\t\t1424\n\t\t1392\n\t\t1360\n\t\t1328\n\t\t1296\n\t\t1264\n\t\t1232\n\t\t1200\n\t\t1168\n\t\t1136\n\t\t1104\n\t\t1072\n\t\t1040\n\t\t1008\n\t\t2016\n\t\t1984\n\t\t976\n\t\t1952\n\t\t1920\n\t\t944\n\t\t1888\n\t\t1856\n\t\t912\n\t\t1824\n\t\t1792\n\t\t880\n\t\t1760\n\t\t1728\n\t\t848\n\t\t1696\n\t\t1664\n\t\t816\n\t\t1632\n\t\t1600\n\t\t784\n\t\t1568\n\t\t1536\n\t\t752\n\t\t1504\n\t\t1472\n\t\t720\n\t\t1440\n\t\t1408\n\t\t688\n\t\t1376\n\t\t1344\n\t\t656\n\t\t1312\n\t\t1280\n\t\t624\n\t\t1248\n\t\t1216\n\t\t592\n\t\t1184\n\t\t1152\n\t\t560\n\t\t1120\n\t\t1088\n\t\t528\n\t\t1056\n\t\t1024\n\t\t496\n\t\t992\n\t\t960\n\t\t464\n\t\t928\n\t\t896\n\t\t432\n\t\t864\n\t\t832\n\t\t400\n\t\t800\n\t\t768\n\t\t368\n\t\t736\n\t\t704\n\t\t336\n\t\t672\n\t\t640\n\t\t304\n\t\t608\n\t\t576\n\t\t272\n\t\t544\n\t\t512\n\t\t240\n\t\t480\n\t\t448\n\t\t208\n\t\t416\n\t\t384\n\t\t176\n\t\t352\n\t\t320\n\t\t144\n\t\t288\n\t\t256\n\t\t112\n\t\t224\n\t\t192\n\t\t80\n\t\t160\n\t\t128\n\t\t48\n\t\t96\n\t\t64\n\t\t16\n\t\t32\n\t\t0\n\t\t0\n\t )\n\t2048\n\t32\n\t0\n\t32\n\t16\n\t64\n\t2\n\t0\n )",
                "simplified": "(reg (bv #x00 8))"
            }
        }
    ],
    " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_43_dsl (reg (bv #x00 8)) 1024 32 0 32 16 32 2 0)"
            }
        }
    ],
    " (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t (hvx_swizzle_18_dsl ; hvx_swizzle_16\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t8\n\t\t8\n\t\t0\n\t\t8\n\t\t8\n\t\t1016\n\t\t1000\n\t\t984\n\t\t968\n\t\t952\n\t\t936\n\t\t920\n\t\t904\n\t\t888\n\t\t872\n\t\t856\n\t\t840\n\t\t824\n\t\t808\n\t\t792\n\t\t776\n\t\t760\n\t\t744\n\t\t728\n\t\t712\n\t\t696\n\t\t680\n\t\t664\n\t\t648\n\t\t632\n\t\t616\n\t\t600\n\t\t584\n\t\t568\n\t\t552\n\t\t536\n\t\t520\n\t\t504\n\t\t1008\n\t\t992\n\t\t488\n\t\t976\n\t\t960\n\t\t472\n\t\t944\n\t\t928\n\t\t456\n\t\t912\n\t\t896\n\t\t440\n\t\t880\n\t\t864\n\t\t424\n\t\t848\n\t\t832\n\t\t408\n\t\t816\n\t\t800\n\t\t392\n\t\t784\n\t\t768\n\t\t376\n\t\t752\n\t\t736\n\t\t360\n\t\t720\n\t\t704\n\t\t344\n\t\t688\n\t\t672\n\t\t328\n\t\t656\n\t\t640\n\t\t312\n\t\t624\n\t\t608\n\t\t296\n\t\t592\n\t\t576\n\t\t280\n\t\t560\n\t\t544\n\t\t264\n\t\t528\n\t\t512\n\t\t248\n\t\t496\n\t\t480\n\t\t232\n\t\t464\n\t\t448\n\t\t216\n\t\t432\n\t\t416\n\t\t200\n\t\t400\n\t\t384\n\t\t184\n\t\t368\n\t\t352\n\t\t168\n\t\t336\n\t\t320\n\t\t152\n\t\t304\n\t\t288\n\t\t136\n\t\t272\n\t\t256\n\t\t120\n\t\t240\n\t\t224\n\t\t104\n\t\t208\n\t\t192\n\t\t88\n\t\t176\n\t\t160\n\t\t72\n\t\t144\n\t\t128\n\t\t56\n\t\t112\n\t\t96\n\t\t40\n\t\t80\n\t\t64\n\t\t24\n\t\t48\n\t\t32\n\t\t8\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t16\n\t0\n\t16\n\t8\n\t64\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t (hvx_swizzle_18_dsl ; hvx_swizzle_16\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t8\n\t\t8\n\t\t0\n\t\t8\n\t\t8\n\t\t1016\n\t\t1000\n\t\t984\n\t\t968\n\t\t952\n\t\t936\n\t\t920\n\t\t904\n\t\t888\n\t\t872\n\t\t856\n\t\t840\n\t\t824\n\t\t808\n\t\t792\n\t\t776\n\t\t760\n\t\t744\n\t\t728\n\t\t712\n\t\t696\n\t\t680\n\t\t664\n\t\t648\n\t\t632\n\t\t616\n\t\t600\n\t\t584\n\t\t568\n\t\t552\n\t\t536\n\t\t520\n\t\t504\n\t\t1008\n\t\t992\n\t\t488\n\t\t976\n\t\t960\n\t\t472\n\t\t944\n\t\t928\n\t\t456\n\t\t912\n\t\t896\n\t\t440\n\t\t880\n\t\t864\n\t\t424\n\t\t848\n\t\t832\n\t\t408\n\t\t816\n\t\t800\n\t\t392\n\t\t784\n\t\t768\n\t\t376\n\t\t752\n\t\t736\n\t\t360\n\t\t720\n\t\t704\n\t\t344\n\t\t688\n\t\t672\n\t\t328\n\t\t656\n\t\t640\n\t\t312\n\t\t624\n\t\t608\n\t\t296\n\t\t592\n\t\t576\n\t\t280\n\t\t560\n\t\t544\n\t\t264\n\t\t528\n\t\t512\n\t\t248\n\t\t496\n\t\t480\n\t\t232\n\t\t464\n\t\t448\n\t\t216\n\t\t432\n\t\t416\n\t\t200\n\t\t400\n\t\t384\n\t\t184\n\t\t368\n\t\t352\n\t\t168\n\t\t336\n\t\t320\n\t\t152\n\t\t304\n\t\t288\n\t\t136\n\t\t272\n\t\t256\n\t\t120\n\t\t240\n\t\t224\n\t\t104\n\t\t208\n\t\t192\n\t\t88\n\t\t176\n\t\t160\n\t\t72\n\t\t144\n\t\t128\n\t\t56\n\t\t112\n\t\t96\n\t\t40\n\t\t80\n\t\t64\n\t\t24\n\t\t48\n\t\t32\n\t\t8\n\t\t16\n\t\t0\n\t\t0\n\t )\n\t1024\n\t16\n\t0\n\t16\n\t8\n\t64\n\t2\n\t0\n )",
                "simplified": "(reg (bv #x00 8))"
            }
        }
    ],
    " (hvx_swizzle_651_dsl ; hvx_swizzle_655\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_2\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_651_dsl ; hvx_swizzle_655\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_2\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t64\n\t\t0\n\t\t64\n\t\t32\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_651_dsl\n (hvx_swizzle_1_dsl\n  (reg (bv #x00 8))\n  32\n  32\n  0\n  32\n  32\n  2016\n  1952\n  1888\n  1824\n  1760\n  1696\n  1632\n  1568\n  1504\n  1440\n  1376\n  1312\n  1248\n  1184\n  1120\n  1056\n  992\n  1984\n  1920\n  928\n  1856\n  1792\n  864\n  1728\n  1664\n  800\n  1600\n  1536\n  736\n  1472\n  1408\n  672\n  1344\n  1280\n  608\n  1216\n  1152\n  544\n  1088\n  1024\n  480\n  960\n  896\n  416\n  832\n  768\n  352\n  704\n  640\n  288\n  576\n  512\n  224\n  448\n  384\n  160\n  320\n  256\n  96\n  192\n  128\n  32\n  64\n  0\n  0)\n (hvx_swizzle_43_dsl (reg (bv #x01 8)) 2048 64 0 64 32 32 2 0)\n 1024\n 1024\n 0\n 512\n 32\n 32\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_654_dsl ; hvx_swizzle_267\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t512\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_654_dsl ; hvx_swizzle_267\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t512\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_654_dsl\n (reg (bv #x00 8))\n (reg (bv #x02 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 512\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_651_dsl ; hvx_swizzle_655\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_651_dsl ; hvx_swizzle_655\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_654_dsl\n (hvx_swizzle_122_dsl (reg (bv #x00 8)) 2048 1024 0 1024 32 2 0)\n (hvx_swizzle_122_dsl (reg (bv #x01 8)) 2048 1024 0 1024 32 2 0)\n 1024\n 1024\n 0\n 512\n 32\n 32\n 1024\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_654_dsl ; hvx_swizzle_650\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_196\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_196\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t512\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_654_dsl ; hvx_swizzle_650\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_196\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_196\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t512\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_654_dsl\n (reg (bv #x00 8))\n (reg (bv #x02 8))\n 1024\n 1024\n 0\n 512\n 32\n 32\n 512\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_651_dsl ; hvx_swizzle_655\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_651_dsl ; hvx_swizzle_655\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_651_dsl\n (hvx_swizzle_1_dsl\n  (reg (bv #x00 8))\n  32\n  32\n  0\n  32\n  32\n  2016\n  1952\n  1888\n  1824\n  1760\n  1696\n  1632\n  1568\n  1504\n  1440\n  1376\n  1312\n  1248\n  1184\n  1120\n  1056\n  992\n  1984\n  1920\n  928\n  1856\n  1792\n  864\n  1728\n  1664\n  800\n  1600\n  1536\n  736\n  1472\n  1408\n  672\n  1344\n  1280\n  608\n  1216\n  1152\n  544\n  1088\n  1024\n  480\n  960\n  896\n  416\n  832\n  768\n  352\n  704\n  640\n  288\n  576\n  512\n  224\n  448\n  384\n  160\n  320\n  256\n  96\n  192\n  128\n  32\n  64\n  0\n  0)\n (hvx_swizzle_122_dsl (reg (bv #x01 8)) 2048 1024 0 1024 32 2 0)\n 1024\n 1024\n 0\n 512\n 32\n 32\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_43_dsl ; hvx_swizzle_17\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_238\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t16\n\t0\n\t16\n\t8\n\t64\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_43_dsl ; hvx_swizzle_17\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_238\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t16\n\t0\n\t16\n\t8\n\t64\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_43_dsl\n (hvx_swizzle_651_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  8\n  8\n  2\n  0)\n 1024\n 16\n 0\n 16\n 8\n 64\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t (hvx_swizzle_654_dsl ; hvx_swizzle_233\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t1024\n\t\t2\n\t\t0\n\t )\n\t1024\n\t16\n\t0\n\t16\n\t8\n\t64\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t (hvx_swizzle_654_dsl ; hvx_swizzle_233\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t1024\n\t\t2\n\t\t0\n\t )\n\t1024\n\t16\n\t0\n\t16\n\t8\n\t64\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_43_dsl\n (hvx_swizzle_654_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  2048\n  2048\n  0\n  1024\n  8\n  8\n  1024\n  2\n  0)\n 1024\n 16\n 0\n 16\n 8\n 64\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_654_dsl ; hvx_swizzle_654\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t512\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_654_dsl ; hvx_swizzle_654\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_122_dsl ; hvx_swizzle_124\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t2048\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t512\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_654_dsl\n (hvx_swizzle_1_dsl\n  (reg (bv #x00 8))\n  32\n  32\n  0\n  32\n  32\n  2016\n  1952\n  1888\n  1824\n  1760\n  1696\n  1632\n  1568\n  1504\n  1440\n  1376\n  1312\n  1248\n  1184\n  1120\n  1056\n  992\n  1984\n  1920\n  928\n  1856\n  1792\n  864\n  1728\n  1664\n  800\n  1600\n  1536\n  736\n  1472\n  1408\n  672\n  1344\n  1280\n  608\n  1216\n  1152\n  544\n  1088\n  1024\n  480\n  960\n  896\n  416\n  832\n  768\n  352\n  704\n  640\n  288\n  576\n  512\n  224\n  448\n  384\n  160\n  320\n  256\n  96\n  192\n  128\n  32\n  64\n  0\n  0)\n (hvx_swizzle_1_dsl\n  (reg (bv #x01 8))\n  32\n  32\n  0\n  32\n  32\n  2016\n  1952\n  1888\n  1824\n  1760\n  1696\n  1632\n  1568\n  1504\n  1440\n  1376\n  1312\n  1248\n  1184\n  1120\n  1056\n  992\n  1984\n  1920\n  928\n  1856\n  1792\n  864\n  1728\n  1664\n  800\n  1600\n  1536\n  736\n  1472\n  1408\n  672\n  1344\n  1280\n  608\n  1216\n  1152\n  544\n  1088\n  1024\n  480\n  960\n  896\n  416\n  832\n  768\n  352\n  704\n  640\n  288\n  576\n  512\n  224\n  448\n  384\n  160\n  320\n  256\n  96\n  192\n  128\n  32\n  64\n  0\n  0)\n 1024\n 1024\n 0\n 512\n 32\n 32\n 512\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_654_dsl ; hvx_swizzle_654\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t512\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_654_dsl ; hvx_swizzle_654\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_3\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i32> False\n\t\t32\n\t\t32\n\t\t0\n\t\t32\n\t\t32\n\t\t2016\n\t\t1952\n\t\t1888\n\t\t1824\n\t\t1760\n\t\t1696\n\t\t1632\n\t\t1568\n\t\t1504\n\t\t1440\n\t\t1376\n\t\t1312\n\t\t1248\n\t\t1184\n\t\t1120\n\t\t1056\n\t\t992\n\t\t1984\n\t\t1920\n\t\t928\n\t\t1856\n\t\t1792\n\t\t864\n\t\t1728\n\t\t1664\n\t\t800\n\t\t1600\n\t\t1536\n\t\t736\n\t\t1472\n\t\t1408\n\t\t672\n\t\t1344\n\t\t1280\n\t\t608\n\t\t1216\n\t\t1152\n\t\t544\n\t\t1088\n\t\t1024\n\t\t480\n\t\t960\n\t\t896\n\t\t416\n\t\t832\n\t\t768\n\t\t352\n\t\t704\n\t\t640\n\t\t288\n\t\t576\n\t\t512\n\t\t224\n\t\t448\n\t\t384\n\t\t160\n\t\t320\n\t\t256\n\t\t96\n\t\t192\n\t\t128\n\t\t32\n\t\t64\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t512\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_654_dsl\n (hvx_swizzle_122_dsl (reg (bv #x00 8)) 2048 1024 0 1024 32 2 0)\n (hvx_swizzle_122_dsl (reg (bv #x01 8)) 2048 1024 0 1024 32 2 0)\n 1024\n 1024\n 0\n 512\n 32\n 32\n 1536\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_651_dsl ; hvx_swizzle_115\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t16\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_651_dsl ; hvx_swizzle_115\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t16\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_651_dsl\n (reg (bv #x00 8))\n (reg (bv #x02 8))\n 2048\n 2048\n 0\n 1024\n 16\n 16\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_533\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t16\n\t0\n\t16\n\t8\n\t64\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_43_dsl ; hvx_swizzle_41\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_533\n\t\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 256 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t16\n\t0\n\t16\n\t8\n\t64\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_43_dsl\n (hvx_swizzle_651_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  2048\n  2048\n  0\n  1024\n  8\n  8\n  2\n  0)\n 1024\n 16\n 0\n 16\n 8\n 64\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hvx_swizzle_654_dsl ; hvx_swizzle_113\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i16> False\n\t\t2048\n\t\t2048\n\t\t0\n\t\t1024\n\t\t16\n\t\t16\n\t\t1024\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hvx_swizzle_654_dsl ; hvx_swizzle_113\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i16> False\n\t\t2048\n\t\t2048\n\t\t0\n\t\t1024\n\t\t16\n\t\t16\n\t\t1024\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "simplified": "(hvx_swizzle_654_dsl\n (reg (bv #x00 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 1024\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_114\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i16> False\n\t\t2048\n\t\t2048\n\t\t0\n\t\t1024\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_88_dsl ; hvx_swizzle_88\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_114\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i16> False\n\t\t2048\n\t\t2048\n\t\t0\n\t\t1024\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )",
                "simplified": "(hvx_swizzle_651_dsl\n (reg (bv #x00 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hvx_swizzle_654_dsl ; hvx_swizzle_264\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t1024\n\t\t2\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t (hvx_swizzle_654_dsl ; hvx_swizzle_264\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t1024\n\t\t2\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_43_dsl\n (hvx_swizzle_654_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  2048\n  2048\n  0\n  1024\n  16\n  16\n  1024\n  2\n  0)\n 1024\n 32\n 0\n 32\n 16\n 32\n 2\n 0)"
            }
        }
    ],
    " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t (hvx_swizzle_43_dsl ; hvx_swizzle_0\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )",
                "simplified": "(reg (bv #x00 8))"
            }
        }
    ],
    " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_69\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )": [
        {
            "property_name": "SimplifyingSwizzles",
            "property": {
                "candidate": " (hvx_swizzle_122_dsl ; hvx_swizzle_122\n\t (hvx_swizzle_651_dsl ; hvx_swizzle_69\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "simplified": "(hvx_swizzle_122_dsl\n (hvx_swizzle_43_dsl (reg (bv #x00 8)) 1024 32 0 32 16 32 2 0)\n 1024\n 512\n 0\n 512\n 16\n 2\n 0)"
            }
        }
    ]
}