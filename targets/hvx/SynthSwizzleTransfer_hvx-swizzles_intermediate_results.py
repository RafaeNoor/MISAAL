{
    "hexagon_V6_vmpyih_128B+hvx_swizzle_502+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t32\n\t1\n\t0\n )",
                "output_expression": "(hexagon_V6_vmpyih_128B_dsl\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n 1024\n 1024\n 0\n 1024\n 16\n 1\n 32\n 1\n 0)"
            }
        }
    ],
    "hexagon_V6_vasruwuhrndsat_128B+hvx_swizzle_502+[3, 4]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasruwuhrndsat_128B",
                "indices": [
                    3,
                    4
                ],
                "input_expression": " (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t (hexagon_V6_vasruwuhrndsat_128B_dsl ; hexagon_V6_vasruwuhrndsat_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000001 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t-1\n\t\t32\n\t\t1\n\t\t0\n\t\t-1\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hvx_swizzle_44_dsl\n (hexagon_V6_vasruwuhrndsat_128B_dsl\n  (lit (bv #x0000000f 32))\n  (lit (bv #x00000001 32))\n  (lit (bv #x00000001 32))\n  (reg (bv #x01 8))\n  (reg (bv #x01 8))\n  (reg (bv #x02 8))\n  1024\n  1024\n  0\n  512\n  16\n  16\n  0\n  -1\n  32\n  1\n  0\n  -1\n  -1\n  0)\n 16\n 16\n 0\n 16\n 16\n 1008\n 976\n 944\n 912\n 880\n 848\n 816\n 784\n 752\n 720\n 688\n 656\n 624\n 592\n 560\n 528\n 496\n 992\n 960\n 464\n 928\n 896\n 432\n 864\n 832\n 400\n 800\n 768\n 368\n 736\n 704\n 336\n 672\n 640\n 304\n 608\n 576\n 272\n 544\n 512\n 240\n 480\n 448\n 208\n 416\n 384\n 176\n 352\n 320\n 144\n 288\n 256\n 112\n 224\n 192\n 80\n 160\n 128\n 48\n 96\n 64\n 16\n 32\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+hvx_swizzle_502+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vmpyih_128B_dsl\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n 1024\n 1024\n 0\n 1024\n 16\n 1\n 32\n 1\n 0)"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+hvx_swizzle_69+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t (hvx_swizzle_69_dsl ; hvx_swizzle_33\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_69_dsl ; hvx_swizzle_33\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t2\n\t8\n\t0\n )",
                "output_expression": "(hexagon_V6_vassign_128B_dsl\n (hvx_swizzle_70_dsl\n  (reg (bv #x03 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  1024\n  8\n  8\n  2\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vdealb4w_128B+hvx_swizzle_1+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vdealb4w_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vdealb4w_128B_dsl ; hexagon_V6_vdealb4w_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_374\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_374\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t256\n\t8\n\t0\n\t256\n\t8\n\t0\n\t256\n\t8\n\t0\n\t256\n\t8\n\t4\n\t32\n\t16\n\t4\n\t8\n\t64\n\t4\n\t8\n\t96\n\t16\n\t4\n\t8\n\t0\n )",
                "output_expression": "(hexagon_V6_vpackeh_128B_dsl\n (reg (bv #x00 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 8\n 0\n 512\n 8\n 2\n 64\n 2\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+hvx_swizzle_1+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_374\n\t (hexagon_V6_vpackwuh_sat_128B_dsl ; hexagon_V6_vpackwuh_sat_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t32\n\t\t1\n\t\t32\n\t\t0\n\t\t32\n\t\t1\n\t\t16\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vsathub_128B_dsl\n (reg (bv #x00 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 0\n 32\n 1\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vor_128B+hvx_swizzle_502+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t (hexagon_V6_vor_128B_dsl ; hexagon_V6_vor_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vpackeh_128B_dsl\n (hexagon_V6_vor_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  1024\n  16\n  0)\n (hexagon_V6_vor_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  1024\n  16\n  0)\n 1024\n 1024\n 0\n 512\n 16\n 0\n 512\n 16\n 2\n 32\n 2\n 16\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+hvx_swizzle_1+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_374\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_374\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t2\n\t16\n\t0\n )",
                "output_expression": "(hvx_swizzle_44_dsl\n (hvx_swizzle_69_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  16\n  2\n  0)\n 16\n 16\n 0\n 16\n 16\n 1008\n 976\n 944\n 912\n 880\n 848\n 816\n 784\n 752\n 720\n 688\n 656\n 624\n 592\n 560\n 528\n 496\n 992\n 960\n 464\n 928\n 896\n 432\n 864\n 832\n 400\n 800\n 768\n 368\n 736\n 704\n 336\n 672\n 640\n 304\n 608\n 576\n 272\n 544\n 512\n 240\n 480\n 448\n 208\n 416\n 384\n 176\n 352\n 320\n 144\n 288\n 256\n 112\n 224\n 192\n 80\n 160\n 128\n 48\n 96\n 64\n 16\n 32\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+hvx_swizzle_69+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_69_dsl ; hvx_swizzle_246\n\t (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vshuffeb_128B_dsl\n (reg (bv #x03 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 16\n 16\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vasrwh_128B+hvx_swizzle_502+[1, 2]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasrwh_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t (hexagon_V6_vasrwh_128B_dsl ; hexagon_V6_vasrwh_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hvx_swizzle_44_dsl\n (hexagon_V6_vasrwh_128B_dsl\n  (lit (bv #x0000000f 32))\n  (reg (bv #x01 8))\n  (reg (bv #x01 8))\n  (reg (bv #x02 8))\n  1024\n  1024\n  0\n  512\n  16\n  16\n  32\n  1\n  0)\n 16\n 16\n 0\n 16\n 16\n 1008\n 976\n 944\n 912\n 880\n 848\n 816\n 784\n 752\n 720\n 688\n 656\n 624\n 592\n 560\n 528\n 496\n 992\n 960\n 464\n 928\n 896\n 432\n 864\n 832\n 400\n 800\n 768\n 368\n 736\n 704\n 336\n 672\n 640\n 304\n 608\n 576\n 272\n 544\n 512\n 240\n 480\n 448\n 208\n 416\n 384\n 176\n 352\n 320\n 144\n 288\n 256\n 112\n 224\n 192\n 80\n 160\n 128\n 48\n 96\n 64\n 16\n 32\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+hvx_swizzle_70+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_70_dsl ; hvx_swizzle_70\n\t (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t8\n\t2\n\t0\n )",
                "output_expression": "(hvx_swizzle_69_dsl\n (hexagon_V6_vsathub_128B_dsl\n  (reg (bv #x03 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  8\n  8\n  0\n  16\n  1\n  0\n  0)\n (hexagon_V6_vsathub_128B_dsl\n  (reg (bv #x02 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  8\n  8\n  0\n  16\n  1\n  0\n  0)\n 1024\n 1024\n 0\n 1024\n 16\n 16\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+hvx_swizzle_502+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vshuffeb_128B_dsl\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  8\n  0\n  512\n  8\n  2\n  64\n  2\n  8\n  0)\n 1024\n 1024\n 0\n 512\n 8\n 8\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+hvx_swizzle_1+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_1_dsl ; hvx_swizzle_374\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vshuffeb_128B_dsl\n (hvx_swizzle_245_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  8\n  8\n  512\n  2\n  0)\n (hvx_swizzle_69_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  8\n  8\n  2\n  0)\n 1024\n 1024\n 0\n 512\n 16\n 16\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+hvx_swizzle_245+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hvx_swizzle_245_dsl ; hvx_swizzle_534\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t512\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_245_dsl ; hvx_swizzle_534\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t512\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_lo_128B_dsl\n (hvx_swizzle_70_dsl\n  (reg (bv #x02 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  1024\n  8\n  8\n  2\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 1024\n 0)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+hvx_swizzle_70+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_70_dsl ; hvx_swizzle_70\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t8\n\t8\n\t2\n\t0\n )",
                "output_expression": "(hvx_swizzle_69_dsl\n (hexagon_V6_vshuffeb_128B_dsl\n  (reg (bv #x03 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  8\n  8\n  2\n  0)\n (hexagon_V6_vshuffeb_128B_dsl\n  (reg (bv #x02 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  8\n  8\n  2\n  0)\n 1024\n 1024\n 0\n 1024\n 16\n 16\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+hvx_swizzle_502+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t-1\n\t1\n\t0\n )",
                "output_expression": "(hexagon_V6_vabsdiffh_128B_dsl\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n 1024\n 1024\n 0\n 1024\n 16\n -1\n -1\n 1\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+hvx_swizzle_69+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_69_dsl ; hvx_swizzle_246\n\t (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hvx_swizzle_245_dsl\n (hvx_swizzle_44_dsl\n  (reg (bv #x01 8))\n  16\n  16\n  0\n  16\n  16\n  1008\n  976\n  944\n  912\n  880\n  848\n  816\n  784\n  752\n  720\n  688\n  656\n  624\n  592\n  560\n  528\n  496\n  992\n  960\n  464\n  928\n  896\n  432\n  864\n  832\n  400\n  800\n  768\n  368\n  736\n  704\n  336\n  672\n  640\n  304\n  608\n  576\n  272\n  544\n  512\n  240\n  480\n  448\n  208\n  416\n  384\n  176\n  352\n  320\n  144\n  288\n  256\n  112\n  224\n  192\n  80\n  160\n  128\n  48\n  96\n  64\n  16\n  32\n  0\n  0)\n (hvx_swizzle_44_dsl\n  (reg (bv #x03 8))\n  16\n  16\n  0\n  16\n  16\n  1008\n  976\n  944\n  912\n  880\n  848\n  816\n  784\n  752\n  720\n  688\n  656\n  624\n  592\n  560\n  528\n  496\n  992\n  960\n  464\n  928\n  896\n  432\n  864\n  832\n  400\n  800\n  768\n  368\n  736\n  704\n  336\n  672\n  640\n  304\n  608\n  576\n  272\n  544\n  512\n  240\n  480\n  448\n  208\n  416\n  384\n  176\n  352\n  320\n  144\n  288\n  256\n  112\n  224\n  192\n  80\n  160\n  128\n  48\n  96\n  64\n  16\n  32\n  0\n  0)\n 1024\n 1024\n 0\n 512\n 16\n 16\n 512\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vroundwuh_128B+hvx_swizzle_502+[4, 5]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vroundwuh_128B",
                "indices": [
                    4,
                    5
                ],
                "input_expression": " (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t (hexagon_V6_vroundwuh_128B_dsl ; hexagon_V6_vroundwuh_128B\n\t\t(lit (bv #x00000000000000000000000000008000 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000010 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000008000 (bitvector 32)))\n\t\t(lit (bv #x00000000000000000000000000000010 (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t-1\n\t\t32\n\t\t1\n\t\t0\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hvx_swizzle_44_dsl\n (hexagon_V6_vroundwuh_128B_dsl\n  (lit (bv #x00008000 32))\n  (lit (bv #x00000010 32))\n  (lit (bv #x00008000 32))\n  (lit (bv #x00000010 32))\n  (reg (bv #x01 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  16\n  0\n  -1\n  32\n  1\n  0\n  -1\n  0)\n 16\n 16\n 0\n 16\n 16\n 1008\n 976\n 944\n 912\n 880\n 848\n 816\n 784\n 752\n 720\n 688\n 656\n 624\n 592\n 560\n 528\n 496\n 992\n 960\n 464\n 928\n 896\n 432\n 864\n 832\n 400\n 800\n 768\n 368\n 736\n 704\n 336\n 672\n 640\n 304\n 608\n 576\n 272\n 544\n 512\n 240\n 480\n 448\n 208\n 416\n 384\n 176\n 352\n 320\n 144\n 288\n 256\n 112\n 224\n 192\n 80\n 160\n 128\n 48\n 96\n 64\n 16\n 32\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+hvx_swizzle_245+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t (hvx_swizzle_245_dsl ; hvx_swizzle_534\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t512\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_245_dsl ; hvx_swizzle_534\n\t\t(reg (bv 2 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t512\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t2\n\t8\n\t0\n )",
                "output_expression": "(hexagon_V6_lo_128B_dsl\n (hvx_swizzle_70_dsl\n  (reg (bv #x03 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  1024\n  8\n  8\n  2\n  0)\n 1024\n 1024\n 0\n 1024\n 8\n 1024\n 0)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+hvx_swizzle_0+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_0_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vsathub_128B_dsl ; hexagon_V6_vsathub_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t0\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t8\n\t8\n\t0\n\t8\n\t8\n\t1016\n\t1000\n\t984\n\t968\n\t952\n\t936\n\t920\n\t904\n\t888\n\t872\n\t856\n\t840\n\t824\n\t808\n\t792\n\t776\n\t760\n\t744\n\t728\n\t712\n\t696\n\t680\n\t664\n\t648\n\t632\n\t616\n\t600\n\t584\n\t568\n\t552\n\t536\n\t520\n\t504\n\t1008\n\t992\n\t488\n\t976\n\t960\n\t472\n\t944\n\t928\n\t456\n\t912\n\t896\n\t440\n\t880\n\t864\n\t424\n\t848\n\t832\n\t408\n\t816\n\t800\n\t392\n\t784\n\t768\n\t376\n\t752\n\t736\n\t360\n\t720\n\t704\n\t344\n\t688\n\t672\n\t328\n\t656\n\t640\n\t312\n\t624\n\t608\n\t296\n\t592\n\t576\n\t280\n\t560\n\t544\n\t264\n\t528\n\t512\n\t248\n\t496\n\t480\n\t232\n\t464\n\t448\n\t216\n\t432\n\t416\n\t200\n\t400\n\t384\n\t184\n\t368\n\t352\n\t168\n\t336\n\t320\n\t152\n\t304\n\t288\n\t136\n\t272\n\t256\n\t120\n\t240\n\t224\n\t104\n\t208\n\t192\n\t88\n\t176\n\t160\n\t72\n\t144\n\t128\n\t56\n\t112\n\t96\n\t40\n\t80\n\t64\n\t24\n\t48\n\t32\n\t8\n\t16\n\t0\n\t0\n )",
                "output_expression": "(hexagon_V6_vpackwuh_sat_128B_dsl\n (reg (bv #x00 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 8\n 0\n 512\n 8\n 0\n 16\n 1\n 64\n 0\n 16\n 1\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+hvx_swizzle_502+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vshuffeb_128B_dsl\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  8\n  0\n  512\n  8\n  2\n  64\n  2\n  8\n  0)\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  8\n  0\n  512\n  8\n  2\n  64\n  2\n  8\n  0)\n 1024\n 1024\n 0\n 512\n 8\n 8\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+hvx_swizzle_1+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_374\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_1_dsl ; hvx_swizzle_374\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": "(hvx_swizzle_44_dsl\n (hvx_swizzle_245_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  16\n  512\n  2\n  0)\n 16\n 16\n 0\n 16\n 16\n 1008\n 976\n 944\n 912\n 880\n 848\n 816\n 784\n 752\n 720\n 688\n 656\n 624\n 592\n 560\n 528\n 496\n 992\n 960\n 464\n 928\n 896\n 432\n 864\n 832\n 400\n 800\n 768\n 368\n 736\n 704\n 336\n 672\n 640\n 304\n 608\n 576\n 272\n 544\n 512\n 240\n 480\n 448\n 208\n 416\n 384\n 176\n 352\n 320\n 144\n 288\n 256\n 112\n 224\n 192\n 80\n 160\n 128\n 48\n 96\n 64\n 16\n 32\n 0\n 0)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+hvx_swizzle_502+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vaddhsat_128B_dsl\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n 1024\n 1024\n 0\n 1024\n 16\n 1\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+hvx_swizzle_152+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_152_dsl ; hvx_swizzle_152\n\t (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t16\n\t0\n\t16\n\t8\n\t64\n\t2\n\t0\n )",
                "output_expression": "(hvx_swizzle_245_dsl\n (hvx_swizzle_44_dsl\n  (reg (bv #x01 8))\n  16\n  16\n  0\n  16\n  16\n  1008\n  976\n  944\n  912\n  880\n  848\n  816\n  784\n  752\n  720\n  688\n  656\n  624\n  592\n  560\n  528\n  496\n  992\n  960\n  464\n  928\n  896\n  432\n  864\n  832\n  400\n  800\n  768\n  368\n  736\n  704\n  336\n  672\n  640\n  304\n  608\n  576\n  272\n  544\n  512\n  240\n  480\n  448\n  208\n  416\n  384\n  176\n  352\n  320\n  144\n  288\n  256\n  112\n  224\n  192\n  80\n  160\n  128\n  48\n  96\n  64\n  16\n  32\n  0\n  0)\n (hvx_swizzle_44_dsl\n  (reg (bv #x00 8))\n  16\n  16\n  0\n  16\n  16\n  1008\n  976\n  944\n  912\n  880\n  848\n  816\n  784\n  752\n  720\n  688\n  656\n  624\n  592\n  560\n  528\n  496\n  992\n  960\n  464\n  928\n  896\n  432\n  864\n  832\n  400\n  800\n  768\n  368\n  736\n  704\n  336\n  672\n  640\n  304\n  608\n  576\n  272\n  544\n  512\n  240\n  480\n  448\n  208\n  416\n  384\n  176\n  352\n  320\n  144\n  288\n  256\n  112\n  224\n  192\n  80\n  160\n  128\n  48\n  96\n  64\n  16\n  32\n  0\n  0)\n 1024\n 1024\n 0\n 512\n 8\n 8\n 512\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+hvx_swizzle_69+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t (hvx_swizzle_69_dsl ; hvx_swizzle_246\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_69_dsl ; hvx_swizzle_246\n\t\t(reg (bv 2 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )",
                "output_expression": "(hexagon_V6_vpackeh_128B_dsl\n (hvx_swizzle_1_dsl (reg (bv #x01 8)) 1024 32 0 32 16 32 2 0)\n (hvx_swizzle_1_dsl (reg (bv #x03 8)) 1024 32 0 32 16 32 2 0)\n 1024\n 1024\n 0\n 512\n 16\n 0\n 512\n 16\n 2\n 32\n 2\n 16\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+hvx_swizzle_502+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vpackeh_128B_dsl\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n 1024\n 1024\n 0\n 512\n 16\n 0\n 512\n 16\n 2\n 32\n 2\n 16\n 0)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+hvx_swizzle_502+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t (hexagon_V6_vabsdiffh_128B_dsl ; hexagon_V6_vabsdiffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t-1\n\t\t1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vabsdiffh_128B_dsl\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n 1024\n 1024\n 0\n 1024\n 16\n -1\n -1\n 1\n 0)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+hvx_swizzle_502+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t2\n\t16\n\t0\n )",
                "output_expression": "(hexagon_V6_vpackeh_128B_dsl\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n 1024\n 1024\n 0\n 512\n 16\n 0\n 512\n 16\n 2\n 32\n 2\n 16\n 0)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+hvx_swizzle_152+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hvx_swizzle_152_dsl ; hvx_swizzle_152\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_152_dsl ; hvx_swizzle_152\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t16\n\t\t0\n\t\t16\n\t\t8\n\t\t64\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )",
                "output_expression": "(hvx_swizzle_69_dsl\n (reg (bv #x01 8))\n (reg (bv #x00 8))\n 1024\n 1024\n 0\n 512\n 8\n 8\n 2\n 0)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+hvx_swizzle_0+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_0_dsl ; hvx_swizzle_0\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t8\n\t8\n\t0\n\t8\n\t8\n\t1016\n\t1000\n\t984\n\t968\n\t952\n\t936\n\t920\n\t904\n\t888\n\t872\n\t856\n\t840\n\t824\n\t808\n\t792\n\t776\n\t760\n\t744\n\t728\n\t712\n\t696\n\t680\n\t664\n\t648\n\t632\n\t616\n\t600\n\t584\n\t568\n\t552\n\t536\n\t520\n\t504\n\t1008\n\t992\n\t488\n\t976\n\t960\n\t472\n\t944\n\t928\n\t456\n\t912\n\t896\n\t440\n\t880\n\t864\n\t424\n\t848\n\t832\n\t408\n\t816\n\t800\n\t392\n\t784\n\t768\n\t376\n\t752\n\t736\n\t360\n\t720\n\t704\n\t344\n\t688\n\t672\n\t328\n\t656\n\t640\n\t312\n\t624\n\t608\n\t296\n\t592\n\t576\n\t280\n\t560\n\t544\n\t264\n\t528\n\t512\n\t248\n\t496\n\t480\n\t232\n\t464\n\t448\n\t216\n\t432\n\t416\n\t200\n\t400\n\t384\n\t184\n\t368\n\t352\n\t168\n\t336\n\t320\n\t152\n\t304\n\t288\n\t136\n\t272\n\t256\n\t120\n\t240\n\t224\n\t104\n\t208\n\t192\n\t88\n\t176\n\t160\n\t72\n\t144\n\t128\n\t56\n\t112\n\t96\n\t40\n\t80\n\t64\n\t24\n\t48\n\t32\n\t8\n\t16\n\t0\n\t0\n )",
                "output_expression": "(hexagon_V6_vpackeh_128B_dsl\n (reg (bv #x00 8))\n (reg (bv #x01 8))\n 1024\n 1024\n 0\n 512\n 8\n 0\n 512\n 8\n 2\n 64\n 2\n 8\n 0)"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+hvx_swizzle_502+[0, 1]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t (hexagon_V6_vsubh_128B_dsl ; hexagon_V6_vsubh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t-1\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hexagon_V6_vsubh_128B_dsl\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n 1024\n 1024\n 0\n 1024\n 16\n -1\n 0)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+hvx_swizzle_502+[0, 1]+False": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "indices": [
                    0,
                    1
                ],
                "input_expression": " (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t\t1024\n\t\t512\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )",
                "output_expression": "(hexagon_V6_vaddhsat_128B_dsl\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x01 8))\n  (reg (bv #x00 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n (hexagon_V6_vpackeh_128B_dsl\n  (reg (bv #x00 8))\n  (reg (bv #x01 8))\n  1024\n  1024\n  0\n  512\n  16\n  0\n  512\n  16\n  2\n  32\n  2\n  16\n  0)\n 1024\n 1024\n 0\n 1024\n 16\n 1\n 0)"
            }
        }
    ],
    "hexagon_V6_vasruwuhsat_128B+hvx_swizzle_502+[1, 2]+True": [
        {
            "property_name": "SynthSwizzleTransfer",
            "property": {
                "candidate": "hexagon_V6_vasruwuhsat_128B",
                "indices": [
                    1,
                    2
                ],
                "input_expression": " (hvx_swizzle_502_dsl ; hvx_swizzle_502\n\t (hexagon_V6_vasruwuhsat_128B_dsl ; hexagon_V6_vasruwuhsat_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 32 x i32> False\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i32> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t0\n\t\t32\n\t\t1\n\t\t0\n\t\t0\n\t )\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )",
                "output_expression": "(hvx_swizzle_44_dsl\n (hexagon_V6_vasruwuhsat_128B_dsl\n  (lit (bv #x0000000f 32))\n  (reg (bv #x01 8))\n  (reg (bv #x01 8))\n  (reg (bv #x02 8))\n  1024\n  1024\n  0\n  512\n  16\n  16\n  0\n  32\n  1\n  0\n  0)\n 16\n 16\n 0\n 16\n 16\n 1008\n 976\n 944\n 912\n 880\n 848\n 816\n 784\n 752\n 720\n 688\n 656\n 624\n 592\n 560\n 528\n 496\n 992\n 960\n 464\n 928\n 896\n 432\n 864\n 832\n 400\n 800\n 768\n 368\n 736\n 704\n 336\n 672\n 640\n 304\n 608\n 576\n 272\n 544\n 512\n 240\n 480\n 448\n 208\n 416\n 384\n 176\n 352\n 320\n 144\n 288\n 256\n 112\n 224\n 192\n 80\n 160\n 128\n 48\n 96\n 64\n 16\n 32\n 0\n 0)"
            }
        }
    ]
}