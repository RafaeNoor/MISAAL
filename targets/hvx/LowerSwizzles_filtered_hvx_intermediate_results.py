{
    " (hvx_swizzle_3_dsl ; hvx_swizzle_0\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )_ (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t2\n\t64\n\t8\n\t2\n\t8\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_3_dsl (reg (bv #x00 8)) 16 16 0 16 16 1008 976 944 912 880 848 816 784 752 720 688 656 624 592 560 528 496 992 960 464 928 896 432 864 832 400 800 768 368 736 704 336 672 640 304 608 576 272 544 512 240 480 448 208 416 384 176 352 320 144 288 256 112 224 192 80 160 128 48 96 64 16 32 0 0)",
                "dst": "(hexagon_V6_vdealb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 16 0 512 16 2 32 16 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_60_dsl ; hvx_swizzle_60\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t8\n\t8\n\t0\n\t8\n\t8\n\t1016\n\t1000\n\t984\n\t968\n\t952\n\t936\n\t920\n\t904\n\t888\n\t872\n\t856\n\t840\n\t824\n\t808\n\t792\n\t776\n\t760\n\t744\n\t728\n\t712\n\t696\n\t680\n\t664\n\t648\n\t632\n\t616\n\t600\n\t584\n\t568\n\t552\n\t536\n\t520\n\t504\n\t1008\n\t992\n\t488\n\t976\n\t960\n\t472\n\t944\n\t928\n\t456\n\t912\n\t896\n\t440\n\t880\n\t864\n\t424\n\t848\n\t832\n\t408\n\t816\n\t800\n\t392\n\t784\n\t768\n\t376\n\t752\n\t736\n\t360\n\t720\n\t704\n\t344\n\t688\n\t672\n\t328\n\t656\n\t640\n\t312\n\t624\n\t608\n\t296\n\t592\n\t576\n\t280\n\t560\n\t544\n\t264\n\t528\n\t512\n\t248\n\t496\n\t480\n\t232\n\t464\n\t448\n\t216\n\t432\n\t416\n\t200\n\t400\n\t384\n\t184\n\t368\n\t352\n\t168\n\t336\n\t320\n\t152\n\t304\n\t288\n\t136\n\t272\n\t256\n\t120\n\t240\n\t224\n\t104\n\t208\n\t192\n\t88\n\t176\n\t160\n\t72\n\t144\n\t128\n\t56\n\t112\n\t96\n\t40\n\t80\n\t64\n\t24\n\t48\n\t32\n\t8\n\t16\n\t0\n\t0\n )_ (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealb_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t2\n\t64\n\t8\n\t2\n\t8\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_60_dsl (reg (bv #x00 8)) 8 8 0 8 8 1016 1000 984 968 952 936 920 904 888 872 856 840 824 808 792 776 760 744 728 712 696 680 664 648 632 616 600 584 568 552 536 520 504 1008 992 488 976 960 472 944 928 456 912 896 440 880 864 424 848 832 408 816 800 392 784 768 376 752 736 360 720 704 344 688 672 328 656 640 312 624 608 296 592 576 280 560 544 264 528 512 248 496 480 232 464 448 216 432 416 200 400 384 184 368 352 168 336 320 152 304 288 136 272 256 120 240 224 104 208 192 88 176 160 72 144 128 56 112 96 40 80 64 24 48 32 8 16 0 0)",
                "dst": "(hexagon_V6_vdealb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0)"
            }
        }
    ],
    " (hvx_swizzle_1_dsl ; hvx_swizzle_2\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )_ (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_1_dsl (reg (bv #x00 8)) 1024 16 0 16 8 64 2 0)",
                "dst": "(hexagon_V6_vshuffh_128B_dsl (reg (bv #x00 8)) 1024 16 0 16 8 16 8 0)"
            }
        }
    ],
    " (hvx_swizzle_1_dsl ; hvx_swizzle_62\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t16\n\t0\n\t16\n\t8\n\t64\n\t2\n\t0\n )_ (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_1_dsl (reg (bv #x00 8)) 1024 16 0 16 8 64 2 0)",
                "dst": "(hexagon_V6_vshuffh_128B_dsl (reg (bv #x00 8)) 1024 16 0 16 8 16 8 0)"
            }
        }
    ],
    " (hvx_swizzle_621_dsl ; hvx_swizzle_621\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )_ (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t2\n\t16\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_621_dsl (reg (bv #x00 8)) 1024 512 0 512 16 2 0)",
                "dst": "(hexagon_V6_vpackeh_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 0 512 16 2 32 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_49\n\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t2048\n\t2048\n\t0\n\t2048\n\t64\n\t0\n )_Reg": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 2048 2048 0 2048 32 0)",
                "dst": "(reg (bv #x00 8))"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_133\n\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t2048\n\t2048\n\t0\n\t2048\n\t32\n\t0\n )_Reg": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 2048 2048 0 2048 32 0)",
                "dst": "(reg (bv #x00 8))"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_48\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )_Reg": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)",
                "dst": "(reg (bv #x00 8))"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_132\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )_Reg": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)",
                "dst": "(reg (bv #x00 8))"
            }
        }
    ],
    " (hvx_swizzle_3_dsl ; hvx_swizzle_0\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )_ (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_3_dsl (reg (bv #x00 8)) 16 16 0 16 16 1008 976 944 912 880 848 816 784 752 720 688 656 624 592 560 528 496 992 960 464 928 896 432 864 832 400 800 768 368 736 704 336 672 640 304 608 576 272 544 512 240 480 448 208 416 384 176 352 320 144 288 256 112 224 192 80 160 128 48 96 64 16 32 0 0)",
                "dst": "(hexagon_V6_vpackoh_128B_dsl (hexagon_V6_vshuffob_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 2 16 0) (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0) 1024 1024 0 512 16 0 512 16 16 2 32 16 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_3_dsl ; hvx_swizzle_0\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )_ (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t2\n\t16\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_3_dsl (reg (bv #x00 8)) 16 16 0 16 16 1008 976 944 912 880 848 816 784 752 720 688 656 624 592 560 528 496 992 960 464 928 896 432 864 832 400 800 768 368 736 704 336 672 640 304 608 576 272 544 512 240 480 448 208 416 384 176 352 320 144 288 256 112 224 192 80 160 128 48 96 64 16 32 0 0)",
                "dst": "(hexagon_V6_vpackeh_128B_dsl (hexagon_V6_vshuffob_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 2 16 0) (reg (bv #x00 8)) 1024 1024 0 512 16 0 512 16 2 32 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_3_dsl ; hvx_swizzle_0\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )_ (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t2\n\t16\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_3_dsl (reg (bv #x00 8)) 16 16 0 16 16 1008 976 944 912 880 848 816 784 752 720 688 656 624 592 560 528 496 992 960 464 928 896 432 864 832 400 800 768 368 736 704 336 672 640 304 608 576 272 544 512 240 480 448 208 416 384 176 352 320 144 288 256 112 224 192 80 160 128 48 96 64 16 32 0 0)",
                "dst": "(hexagon_V6_vpackeh_128B_dsl (hexagon_V6_vshuffob_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 2 16 0) (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0) 1024 1024 0 512 16 0 512 16 2 32 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_60_dsl ; hvx_swizzle_60\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t8\n\t8\n\t0\n\t8\n\t8\n\t1016\n\t1000\n\t984\n\t968\n\t952\n\t936\n\t920\n\t904\n\t888\n\t872\n\t856\n\t840\n\t824\n\t808\n\t792\n\t776\n\t760\n\t744\n\t728\n\t712\n\t696\n\t680\n\t664\n\t648\n\t632\n\t616\n\t600\n\t584\n\t568\n\t552\n\t536\n\t520\n\t504\n\t1008\n\t992\n\t488\n\t976\n\t960\n\t472\n\t944\n\t928\n\t456\n\t912\n\t896\n\t440\n\t880\n\t864\n\t424\n\t848\n\t832\n\t408\n\t816\n\t800\n\t392\n\t784\n\t768\n\t376\n\t752\n\t736\n\t360\n\t720\n\t704\n\t344\n\t688\n\t672\n\t328\n\t656\n\t640\n\t312\n\t624\n\t608\n\t296\n\t592\n\t576\n\t280\n\t560\n\t544\n\t264\n\t528\n\t512\n\t248\n\t496\n\t480\n\t232\n\t464\n\t448\n\t216\n\t432\n\t416\n\t200\n\t400\n\t384\n\t184\n\t368\n\t352\n\t168\n\t336\n\t320\n\t152\n\t304\n\t288\n\t136\n\t272\n\t256\n\t120\n\t240\n\t224\n\t104\n\t208\n\t192\n\t88\n\t176\n\t160\n\t72\n\t144\n\t128\n\t56\n\t112\n\t96\n\t40\n\t80\n\t64\n\t24\n\t48\n\t32\n\t8\n\t16\n\t0\n\t0\n )_ (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_60_dsl (reg (bv #x00 8)) 8 8 0 8 8 1016 1000 984 968 952 936 920 904 888 872 856 840 824 808 792 776 760 744 728 712 696 680 664 648 632 616 600 584 568 552 536 520 504 1008 992 488 976 960 472 944 928 456 912 896 440 880 864 424 848 832 408 816 800 392 784 768 376 752 736 360 720 704 344 688 672 328 656 640 312 624 608 296 592 576 280 560 544 264 528 512 248 496 480 232 464 448 216 432 416 200 400 384 184 368 352 168 336 320 152 304 288 136 272 256 120 240 224 104 208 192 88 176 160 72 144 128 56 112 96 40 80 64 24 48 32 8 16 0 0)",
                "dst": "(hexagon_V6_vpackoh_128B_dsl (hexagon_V6_vshuffob_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 8 2 8 0) (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 8 8 2 0) 1024 1024 0 512 8 0 512 8 8 2 64 8 2 8 0)"
            }
        }
    ],
    " (hvx_swizzle_60_dsl ; hvx_swizzle_60\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t8\n\t8\n\t0\n\t8\n\t8\n\t1016\n\t1000\n\t984\n\t968\n\t952\n\t936\n\t920\n\t904\n\t888\n\t872\n\t856\n\t840\n\t824\n\t808\n\t792\n\t776\n\t760\n\t744\n\t728\n\t712\n\t696\n\t680\n\t664\n\t648\n\t632\n\t616\n\t600\n\t584\n\t568\n\t552\n\t536\n\t520\n\t504\n\t1008\n\t992\n\t488\n\t976\n\t960\n\t472\n\t944\n\t928\n\t456\n\t912\n\t896\n\t440\n\t880\n\t864\n\t424\n\t848\n\t832\n\t408\n\t816\n\t800\n\t392\n\t784\n\t768\n\t376\n\t752\n\t736\n\t360\n\t720\n\t704\n\t344\n\t688\n\t672\n\t328\n\t656\n\t640\n\t312\n\t624\n\t608\n\t296\n\t592\n\t576\n\t280\n\t560\n\t544\n\t264\n\t528\n\t512\n\t248\n\t496\n\t480\n\t232\n\t464\n\t448\n\t216\n\t432\n\t416\n\t200\n\t400\n\t384\n\t184\n\t368\n\t352\n\t168\n\t336\n\t320\n\t152\n\t304\n\t288\n\t136\n\t272\n\t256\n\t120\n\t240\n\t224\n\t104\n\t208\n\t192\n\t88\n\t176\n\t160\n\t72\n\t144\n\t128\n\t56\n\t112\n\t96\n\t40\n\t80\n\t64\n\t24\n\t48\n\t32\n\t8\n\t16\n\t0\n\t0\n )_ (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t2\n\t16\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_60_dsl (reg (bv #x00 8)) 8 8 0 8 8 1016 1000 984 968 952 936 920 904 888 872 856 840 824 808 792 776 760 744 728 712 696 680 664 648 632 616 600 584 568 552 536 520 504 1008 992 488 976 960 472 944 928 456 912 896 440 880 864 424 848 832 408 816 800 392 784 768 376 752 736 360 720 704 344 688 672 328 656 640 312 624 608 296 592 576 280 560 544 264 528 512 248 496 480 232 464 448 216 432 416 200 400 384 184 368 352 168 336 320 152 304 288 136 272 256 120 240 224 104 208 192 88 176 160 72 144 128 56 112 96 40 80 64 24 48 32 8 16 0 0)",
                "dst": "(hexagon_V6_vpackeh_128B_dsl (hexagon_V6_vshuffob_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 8 2 8 0) (reg (bv #x00 8)) 1024 1024 0 512 8 0 512 8 2 64 2 8 0)"
            }
        }
    ],
    " (hvx_swizzle_60_dsl ; hvx_swizzle_60\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t8\n\t8\n\t0\n\t8\n\t8\n\t1016\n\t1000\n\t984\n\t968\n\t952\n\t936\n\t920\n\t904\n\t888\n\t872\n\t856\n\t840\n\t824\n\t808\n\t792\n\t776\n\t760\n\t744\n\t728\n\t712\n\t696\n\t680\n\t664\n\t648\n\t632\n\t616\n\t600\n\t584\n\t568\n\t552\n\t536\n\t520\n\t504\n\t1008\n\t992\n\t488\n\t976\n\t960\n\t472\n\t944\n\t928\n\t456\n\t912\n\t896\n\t440\n\t880\n\t864\n\t424\n\t848\n\t832\n\t408\n\t816\n\t800\n\t392\n\t784\n\t768\n\t376\n\t752\n\t736\n\t360\n\t720\n\t704\n\t344\n\t688\n\t672\n\t328\n\t656\n\t640\n\t312\n\t624\n\t608\n\t296\n\t592\n\t576\n\t280\n\t560\n\t544\n\t264\n\t528\n\t512\n\t248\n\t496\n\t480\n\t232\n\t464\n\t448\n\t216\n\t432\n\t416\n\t200\n\t400\n\t384\n\t184\n\t368\n\t352\n\t168\n\t336\n\t320\n\t152\n\t304\n\t288\n\t136\n\t272\n\t256\n\t120\n\t240\n\t224\n\t104\n\t208\n\t192\n\t88\n\t176\n\t160\n\t72\n\t144\n\t128\n\t56\n\t112\n\t96\n\t40\n\t80\n\t64\n\t24\n\t48\n\t32\n\t8\n\t16\n\t0\n\t0\n )_ (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t2\n\t16\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_60_dsl (reg (bv #x00 8)) 8 8 0 8 8 1016 1000 984 968 952 936 920 904 888 872 856 840 824 808 792 776 760 744 728 712 696 680 664 648 632 616 600 584 568 552 536 520 504 1008 992 488 976 960 472 944 928 456 912 896 440 880 864 424 848 832 408 816 800 392 784 768 376 752 736 360 720 704 344 688 672 328 656 640 312 624 608 296 592 576 280 560 544 264 528 512 248 496 480 232 464 448 216 432 416 200 400 384 184 368 352 168 336 320 152 304 288 136 272 256 120 240 224 104 208 192 88 176 160 72 144 128 56 112 96 40 80 64 24 48 32 8 16 0 0)",
                "dst": "(hexagon_V6_vpackeh_128B_dsl (hexagon_V6_vshuffob_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 8 2 8 0) (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 8 8 2 0) 1024 1024 0 512 8 0 512 8 2 64 2 8 0)"
            }
        }
    ],
    " (hvx_swizzle_526_dsl ; hvx_swizzle_526\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t16\n\t2\n\t0\n )_ (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_526_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0)",
                "dst": "(hexagon_V6_vshuffeb_128B_dsl (hexagon_V6_vshuffh_128B_dsl (reg (bv #x00 8)) 1024 32 0 32 16 32 2 0) (hexagon_V6_vshuffh_128B_dsl (reg (bv #x01 8)) 1024 32 0 32 16 32 2 0) 1024 1024 0 512 16 16 2 0)"
            }
        }
    ],
    " (hvx_swizzle_526_dsl ; hvx_swizzle_265\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )_ (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_526_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 512 16 16 2 0)",
                "dst": "(hexagon_V6_vshuffeb_128B_dsl (hexagon_V6_vshuffh_128B_dsl (reg (bv #x01 8)) 1024 32 0 32 16 32 2 0) (hexagon_V6_vshuffh_128B_dsl (reg (bv #x00 8)) 1024 32 0 32 16 32 2 0) 1024 1024 0 512 16 16 2 0)"
            }
        }
    ],
    " (hvx_swizzle_526_dsl ; hvx_swizzle_842\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t32\n\t32\n\t2\n\t0\n )_ (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_526_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0)",
                "dst": "(hexagon_V6_vshuffeb_128B_dsl (hexagon_V6_vshuffh_128B_dsl (reg (bv #x00 8)) 1024 32 0 32 16 32 2 0) (hexagon_V6_vshuffh_128B_dsl (reg (bv #x01 8)) 1024 32 0 32 16 32 2 0) 1024 1024 0 512 16 16 2 0)"
            }
        }
    ],
    " (hvx_swizzle_621_dsl ; hvx_swizzle_621\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )_ (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealb_128B\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t2\n\t64\n\t8\n\t2\n\t8\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_621_dsl (reg (bv #x00 8)) 1024 512 0 512 16 2 0)",
                "dst": "(hexagon_V6_vdealb_128B_dsl (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0) 1024 1024 0 512 16 0 512 16 2 32 16 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_621_dsl ; hvx_swizzle_621\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )_ (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t16\n\t2\n\t32\n\t16\n\t2\n\t16\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_621_dsl (reg (bv #x00 8)) 1024 512 0 512 16 2 0)",
                "dst": "(hexagon_V6_vpackoh_128B_dsl (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0) (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0) 1024 1024 0 512 16 0 512 16 16 2 32 16 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_621_dsl ; hvx_swizzle_621\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )_ (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hexagon_V6_vpackoh_128B_dsl ; hexagon_V6_vpackoh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t16\n\t\t2\n\t\t32\n\t\t16\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t2\n\t\t32\n\t\t2\n\t\t16\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_621_dsl (reg (bv #x00 8)) 1024 512 0 512 16 2 0)",
                "dst": "(hexagon_V6_vshuffeb_128B_dsl (hexagon_V6_vpackoh_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 8 0 512 8 8 2 64 8 2 8 0) (hexagon_V6_vpackeh_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 8 0 512 8 2 64 2 8 0) 1024 1024 0 512 8 8 2 0)"
            }
        }
    ],
    " (hvx_swizzle_621_dsl ; hvx_swizzle_621\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )_ (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t2\n\t16\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_621_dsl (reg (bv #x00 8)) 1024 512 0 512 16 2 0)",
                "dst": "(hexagon_V6_vpackeh_128B_dsl (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0) (reg (bv #x00 8)) 1024 1024 0 512 16 0 512 16 2 32 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_621_dsl ; hvx_swizzle_621\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )_ (hexagon_V6_vpackeh_128B_dsl ; hexagon_V6_vpackeh_128B\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t2\n\t32\n\t2\n\t16\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_621_dsl (reg (bv #x00 8)) 1024 512 0 512 16 2 0)",
                "dst": "(hexagon_V6_vpackeh_128B_dsl (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0) (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0) 1024 1024 0 512 16 0 512 16 2 32 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_48\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )_ (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t64\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)",
                "dst": "(hexagon_V6_vshuffh_128B_dsl (hexagon_V6_vdealb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0) 1024 16 0 16 8 16 8 0)"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_48\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )_ (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealb_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t2\n\t64\n\t8\n\t2\n\t8\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)",
                "dst": "(hexagon_V6_vdealb_128B_dsl (hexagon_V6_vshuffh_128B_dsl (reg (bv #x00 8)) 1024 32 0 32 16 32 2 0) 1024 1024 0 512 16 0 512 16 2 32 16 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_48\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )_ (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)",
                "dst": "(hexagon_V6_vshuffeb_128B_dsl (hexagon_V6_vshuffob_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 2 16 0) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0)"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_48\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )_ (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)",
                "dst": "(hexagon_V6_vshuffeb_128B_dsl (hexagon_V6_vshuffob_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 2 16 0) (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0) 1024 1024 0 512 16 16 2 0)"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_48\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t0\n )_ (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t2\n\t8\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)",
                "dst": "(hexagon_V6_vshuffob_128B_dsl (hexagon_V6_vshuffob_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 2 16 0) (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0) 1024 1024 0 512 16 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_132\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )_ (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealb_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t64\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)",
                "dst": "(hexagon_V6_vshuffh_128B_dsl (hexagon_V6_vdealb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0) 1024 16 0 16 8 16 8 0)"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_132\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )_ (hexagon_V6_vdealb_128B_dsl ; hexagon_V6_vdealb_128B\n\t (hexagon_V6_vshuffh_128B_dsl ; hexagon_V6_vshuffh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t32\n\t\t0\n\t\t32\n\t\t16\n\t\t32\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t2\n\t64\n\t8\n\t2\n\t8\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)",
                "dst": "(hexagon_V6_vdealb_128B_dsl (hexagon_V6_vshuffh_128B_dsl (reg (bv #x00 8)) 1024 32 0 32 16 32 2 0) 1024 1024 0 512 16 0 512 16 2 32 16 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_132\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )_ (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)",
                "dst": "(hexagon_V6_vshuffeb_128B_dsl (hexagon_V6_vshuffob_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 2 16 0) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0)"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_132\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )_ (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)",
                "dst": "(hexagon_V6_vshuffeb_128B_dsl (hexagon_V6_vshuffob_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 2 16 0) (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0) 1024 1024 0 512 16 16 2 0)"
            }
        }
    ],
    " (hvx_swizzle_49_dsl ; hvx_swizzle_132\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )_ (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t (hexagon_V6_vshuffob_128B_dsl ; hexagon_V6_vshuffob_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t2\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_vshuffeb_128B_dsl ; hexagon_V6_vshuffeb_128B\n\t\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 3 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t2\n\t8\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_49_dsl (reg (bv #x00 8)) 1024 1024 0 1024 16 0)",
                "dst": "(hexagon_V6_vshuffob_128B_dsl (hexagon_V6_vshuffob_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 2 16 0) (hexagon_V6_vshuffeb_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0) 1024 1024 0 512 16 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_60_dsl ; hvx_swizzle_63\n\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t16\n\t16\n\t0\n\t16\n\t16\n\t2032\n\t2000\n\t1968\n\t1936\n\t1904\n\t1872\n\t1840\n\t1808\n\t1776\n\t1744\n\t1712\n\t1680\n\t1648\n\t1616\n\t1584\n\t1552\n\t1520\n\t1488\n\t1456\n\t1424\n\t1392\n\t1360\n\t1328\n\t1296\n\t1264\n\t1232\n\t1200\n\t1168\n\t1136\n\t1104\n\t1072\n\t1040\n\t1008\n\t2016\n\t1984\n\t976\n\t1952\n\t1920\n\t944\n\t1888\n\t1856\n\t912\n\t1824\n\t1792\n\t880\n\t1760\n\t1728\n\t848\n\t1696\n\t1664\n\t816\n\t1632\n\t1600\n\t784\n\t1568\n\t1536\n\t752\n\t1504\n\t1472\n\t720\n\t1440\n\t1408\n\t688\n\t1376\n\t1344\n\t656\n\t1312\n\t1280\n\t624\n\t1248\n\t1216\n\t592\n\t1184\n\t1152\n\t560\n\t1120\n\t1088\n\t528\n\t1056\n\t1024\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )_ (hexagon_V6_vdealvdd_128B_dsl ; hexagon_V6_vdealvdd_128B\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t(lit (bv -1 (bitvector 32)))\n\t2048\n\t2048\n\t0\n\t512\n\t0\n\t512\n\t0\n\t512\n\t0\n\t512\n\t8\n\t2\n\t2\n\t2\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_60_dsl (reg (bv #x00 8)) 16 16 0 16 16 2032 2000 1968 1936 1904 1872 1840 1808 1776 1744 1712 1680 1648 1616 1584 1552 1520 1488 1456 1424 1392 1360 1328 1296 1264 1232 1200 1168 1136 1104 1072 1040 1008 2016 1984 976 1952 1920 944 1888 1856 912 1824 1792 880 1760 1728 848 1696 1664 816 1632 1600 784 1568 1536 752 1504 1472 720 1440 1408 688 1376 1344 656 1312 1280 624 1248 1216 592 1184 1152 560 1120 1088 528 1056 1024 496 992 960 464 928 896 432 864 832 400 800 768 368 736 704 336 672 640 304 608 576 272 544 512 240 480 448 208 416 384 176 352 320 144 288 256 112 224 192 80 160 128 48 96 64 16 32 0 0)",
                "dst": "(hexagon_V6_vdealvdd_128B_dsl (hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0) (hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0) (lit (bv #xfffffffe 32)) 2048 2048 0 512 0 512 0 512 0 512 8 2 2 2 2 0)"
            }
        }
    ],
    " (hvx_swizzle_1_dsl ; hvx_swizzle_1\n\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t2048\n\t64\n\t0\n\t64\n\t32\n\t32\n\t2\n\t0\n )_ (hexagon_V6_vshuffvdd_128B_dsl ; hexagon_V6_vshuffvdd_128B\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t(lit (bv -1 (bitvector 32)))\n\t2048\n\t2048\n\t0\n\t1024\n\t8\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_1_dsl (reg (bv #x00 8)) 2048 64 0 64 32 32 2 0)",
                "dst": "(hexagon_V6_vshuffvdd_128B_dsl (hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0) (hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0) (lit (bv #xfffffffc 32)) 2048 2048 0 1024 8 0)"
            }
        }
    ],
    " (hvx_swizzle_1_dsl ; hvx_swizzle_61\n\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t2048\n\t32\n\t0\n\t32\n\t16\n\t64\n\t2\n\t0\n )_ (hexagon_V6_vshuffvdd_128B_dsl ; hexagon_V6_vshuffvdd_128B\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t(lit (bv -1 (bitvector 32)))\n\t2048\n\t2048\n\t0\n\t1024\n\t8\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_1_dsl (reg (bv #x00 8)) 2048 64 0 64 32 32 2 0)",
                "dst": "(hexagon_V6_vshuffvdd_128B_dsl (hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0) (hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0) (lit (bv #xfffffffc 32)) 2048 2048 0 1024 8 0)"
            }
        }
    ],
    " (hvx_swizzle_3_dsl ; hvx_swizzle_3\n\t(reg (bv 0 (bitvector 8))) ; < 256 x i8> False\n\t32\n\t32\n\t0\n\t32\n\t32\n\t2016\n\t1952\n\t1888\n\t1824\n\t1760\n\t1696\n\t1632\n\t1568\n\t1504\n\t1440\n\t1376\n\t1312\n\t1248\n\t1184\n\t1120\n\t1056\n\t992\n\t1984\n\t1920\n\t928\n\t1856\n\t1792\n\t864\n\t1728\n\t1664\n\t800\n\t1600\n\t1536\n\t736\n\t1472\n\t1408\n\t672\n\t1344\n\t1280\n\t608\n\t1216\n\t1152\n\t544\n\t1088\n\t1024\n\t480\n\t960\n\t896\n\t416\n\t832\n\t768\n\t352\n\t704\n\t640\n\t288\n\t576\n\t512\n\t224\n\t448\n\t384\n\t160\n\t320\n\t256\n\t96\n\t192\n\t128\n\t32\n\t64\n\t0\n\t0\n )_ (hexagon_V6_vdealvdd_128B_dsl ; hexagon_V6_vdealvdd_128B\n\t (hexagon_V6_lo_128B_dsl ; hexagon_V6_lo_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t1024\n\t\t0\n\t )\n\t (hexagon_V6_vassign_128B_dsl ; hexagon_V6_hi_128B\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t8\n\t\t0\n\t )\n\t(lit (bv -1 (bitvector 32)))\n\t2048\n\t2048\n\t0\n\t512\n\t0\n\t512\n\t0\n\t512\n\t0\n\t512\n\t8\n\t2\n\t2\n\t2\n\t2\n\t0\n )": [
        {
            "property_name": "LowerSwizzles_filtered",
            "property": {
                "src": "(hvx_swizzle_3_dsl (reg (bv #x00 8)) 32 32 0 32 32 2016 1952 1888 1824 1760 1696 1632 1568 1504 1440 1376 1312 1248 1184 1120 1056 992 1984 1920 928 1856 1792 864 1728 1664 800 1600 1536 736 1472 1408 672 1344 1280 608 1216 1152 544 1088 1024 480 960 896 416 832 768 352 704 640 288 576 512 224 448 384 160 320 256 96 192 128 32 64 0 0)",
                "dst": "(hexagon_V6_vdealvdd_128B_dsl (hexagon_V6_lo_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 1024 0) (hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0) (lit (bv #xfffffffc 32)) 2048 2048 0 512 0 512 0 512 0 512 8 2 2 2 2 0)"
            }
        }
    ]
}
