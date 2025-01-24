hvx_swizzles_EqClassEqualDepthV3Synth={
    " (hvx_swizzle_499_dsl ; hvx_swizzle_499\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_499_dsl (reg (bv #x00 8)) 1024 16 0 16 8 64 2 0)",
                "dst": "(hexagon_V6_vshuffh_128B_dsl (reg (bv #x00 8)) 1024 16 0 16 8 16 8 0)"
            }
        }
    ],
    " (hvx_swizzle_271_dsl ; hvx_swizzle_271\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_271_dsl (reg (bv #x00 8)) 1024 512 0 512 16 2 0)",
                "dst": "(hexagon_V6_vpackeh_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 0 512 16 2 32 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_2_dsl ; hvx_swizzle_0\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t8\n\t8\n\t0\n\t8\n\t8\n\t1016\n\t1000\n\t984\n\t968\n\t952\n\t936\n\t920\n\t904\n\t888\n\t872\n\t856\n\t840\n\t824\n\t808\n\t792\n\t776\n\t760\n\t744\n\t728\n\t712\n\t696\n\t680\n\t664\n\t648\n\t632\n\t616\n\t600\n\t584\n\t568\n\t552\n\t536\n\t520\n\t504\n\t1008\n\t992\n\t488\n\t976\n\t960\n\t472\n\t944\n\t928\n\t456\n\t912\n\t896\n\t440\n\t880\n\t864\n\t424\n\t848\n\t832\n\t408\n\t816\n\t800\n\t392\n\t784\n\t768\n\t376\n\t752\n\t736\n\t360\n\t720\n\t704\n\t344\n\t688\n\t672\n\t328\n\t656\n\t640\n\t312\n\t624\n\t608\n\t296\n\t592\n\t576\n\t280\n\t560\n\t544\n\t264\n\t528\n\t512\n\t248\n\t496\n\t480\n\t232\n\t464\n\t448\n\t216\n\t432\n\t416\n\t200\n\t400\n\t384\n\t184\n\t368\n\t352\n\t168\n\t336\n\t320\n\t152\n\t304\n\t288\n\t136\n\t272\n\t256\n\t120\n\t240\n\t224\n\t104\n\t208\n\t192\n\t88\n\t176\n\t160\n\t72\n\t144\n\t128\n\t56\n\t112\n\t96\n\t40\n\t80\n\t64\n\t24\n\t48\n\t32\n\t8\n\t16\n\t0\n\t0\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_2_dsl (reg (bv #x00 8)) 8 8 0 8 8 1016 1000 984 968 952 936 920 904 888 872 856 840 824 808 792 776 760 744 728 712 696 680 664 648 632 616 600 584 568 552 536 520 504 1008 992 488 976 960 472 944 928 456 912 896 440 880 864 424 848 832 408 816 800 392 784 768 376 752 736 360 720 704 344 688 672 328 656 640 312 624 608 296 592 576 280 560 544 264 528 512 248 496 480 232 464 448 216 432 416 200 400 384 184 368 352 168 336 320 152 304 288 136 272 256 120 240 224 104 208 192 88 176 160 72 144 128 56 112 96 40 80 64 24 48 32 8 16 0 0)",
                "dst": "(hexagon_V6_vdealb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0)"
            }
        }
    ],
    " (hvx_swizzle_12_dsl ; hvx_swizzle_12\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_12_dsl (reg (bv #x00 8)) 16 16 0 16 16 1008 976 944 912 880 848 816 784 752 720 688 656 624 592 560 528 496 992 960 464 928 896 432 864 832 400 800 768 368 736 704 336 672 640 304 608 576 272 544 512 240 480 448 208 416 384 176 352 320 144 288 256 112 224 192 80 160 128 48 96 64 16 32 0 0)",
                "dst": "(hexagon_V6_vdealb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 16 0 512 16 2 32 16 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_68_dsl ; hvx_swizzle_68\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )+D1": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_68_dsl (reg (bv #x00 8)) 1024 1024 0 1024 32 0)",
                "dst": "(hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0)"
            }
        }
    ],
    " (hvx_swizzle_13_dsl ; hvx_swizzle_13\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_13_dsl (reg (bv #x00 8)) 1024 16 0 16 8 64 2 0)",
                "dst": "(hexagon_V6_vshuffh_128B_dsl (hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0) 1024 16 0 16 8 16 8 0)"
            }
        }
    ],
    " (hvx_swizzle_499_dsl ; hvx_swizzle_499\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t32\n\t0\n\t32\n\t16\n\t32\n\t2\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_499_dsl (reg (bv #x00 8)) 1024 32 0 32 16 32 2 0)",
                "dst": "(hexagon_V6_vshuffh_128B_dsl (reg (bv #x00 8)) 1024 32 0 32 16 32 2 0)"
            }
        }
    ],
    " (hvx_swizzle_936_dsl ; hvx_swizzle_936\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t(reg (bv 1 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t16\n\t2\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_936_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 8 8 2 0)",
                "dst": "(hexagon_V6_vshufoeh_128B_dsl (hexagon_V6_vshuffh_128B_dsl (reg (bv #x01 8)) 1024 16 0 16 8 16 8 0) (hexagon_V6_vshuffh_128B_dsl (reg (bv #x00 8)) 1024 16 0 16 8 16 8 0) 1024 1024 0 512 8 0 512 8 8 2 1032 1024 8 2 0)"
            }
        }
    ],
    " (hvx_swizzle_2_dsl ; hvx_swizzle_0\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t8\n\t8\n\t0\n\t8\n\t8\n\t1016\n\t1000\n\t984\n\t968\n\t952\n\t936\n\t920\n\t904\n\t888\n\t872\n\t856\n\t840\n\t824\n\t808\n\t792\n\t776\n\t760\n\t744\n\t728\n\t712\n\t696\n\t680\n\t664\n\t648\n\t632\n\t616\n\t600\n\t584\n\t568\n\t552\n\t536\n\t520\n\t504\n\t1008\n\t992\n\t488\n\t976\n\t960\n\t472\n\t944\n\t928\n\t456\n\t912\n\t896\n\t440\n\t880\n\t864\n\t424\n\t848\n\t832\n\t408\n\t816\n\t800\n\t392\n\t784\n\t768\n\t376\n\t752\n\t736\n\t360\n\t720\n\t704\n\t344\n\t688\n\t672\n\t328\n\t656\n\t640\n\t312\n\t624\n\t608\n\t296\n\t592\n\t576\n\t280\n\t560\n\t544\n\t264\n\t528\n\t512\n\t248\n\t496\n\t480\n\t232\n\t464\n\t448\n\t216\n\t432\n\t416\n\t200\n\t400\n\t384\n\t184\n\t368\n\t352\n\t168\n\t336\n\t320\n\t152\n\t304\n\t288\n\t136\n\t272\n\t256\n\t120\n\t240\n\t224\n\t104\n\t208\n\t192\n\t88\n\t176\n\t160\n\t72\n\t144\n\t128\n\t56\n\t112\n\t96\n\t40\n\t80\n\t64\n\t24\n\t48\n\t32\n\t8\n\t16\n\t0\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_2_dsl (reg (bv #x00 8)) 8 8 0 8 8 1016 1000 984 968 952 936 920 904 888 872 856 840 824 808 792 776 760 744 728 712 696 680 664 648 632 616 600 584 568 552 536 520 504 1008 992 488 976 960 472 944 928 456 912 896 440 880 864 424 848 832 408 816 800 392 784 768 376 752 736 360 720 704 344 688 672 328 656 640 312 624 608 296 592 576 280 560 544 264 528 512 248 496 480 232 464 448 216 432 416 200 400 384 184 368 352 168 336 320 152 304 288 136 272 256 120 240 224 104 208 192 88 176 160 72 144 128 56 112 96 40 80 64 24 48 32 8 16 0 0)",
                "dst": "(hexagon_V6_vdealb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0)"
            }
        }
    ],
    " (hvx_swizzle_271_dsl ; hvx_swizzle_271\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t1024\n\t512\n\t0\n\t512\n\t16\n\t2\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_271_dsl (reg (bv #x00 8)) 1024 512 0 512 16 2 0)",
                "dst": "(hexagon_V6_vpackeh_128B_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 0 512 16 2 32 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_12_dsl ; hvx_swizzle_12\n\t(reg (bv 0 (bitvector 8))) ; < 64 x i16> False\n\t16\n\t16\n\t0\n\t16\n\t16\n\t1008\n\t976\n\t944\n\t912\n\t880\n\t848\n\t816\n\t784\n\t752\n\t720\n\t688\n\t656\n\t624\n\t592\n\t560\n\t528\n\t496\n\t992\n\t960\n\t464\n\t928\n\t896\n\t432\n\t864\n\t832\n\t400\n\t800\n\t768\n\t368\n\t736\n\t704\n\t336\n\t672\n\t640\n\t304\n\t608\n\t576\n\t272\n\t544\n\t512\n\t240\n\t480\n\t448\n\t208\n\t416\n\t384\n\t176\n\t352\n\t320\n\t144\n\t288\n\t256\n\t112\n\t224\n\t192\n\t80\n\t160\n\t128\n\t48\n\t96\n\t64\n\t16\n\t32\n\t0\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_12_dsl (reg (bv #x00 8)) 16 16 0 16 16 1008 976 944 912 880 848 816 784 752 720 688 656 624 592 560 528 496 992 960 464 928 896 432 864 832 400 800 768 368 736 704 336 672 640 304 608 576 272 544 512 240 480 448 208 416 384 176 352 320 144 288 256 112 224 192 80 160 128 48 96 64 16 32 0 0)",
                "dst": "(hexagon_V6_vdealb_128B_dsl (reg (bv #x00 8)) 1024 1024 0 512 16 0 512 16 2 32 16 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_173_dsl ; hvx_swizzle_222\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t2\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_173_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 512 16 16 2 0)",
                "dst": "(hexagon_V6_vshuffeb_128B_dsl (hexagon_V6_vshuffh_128B_dsl (reg (bv #x00 8)) 1024 32 0 32 16 32 2 0) (hexagon_V6_vshuffh_128B_dsl (reg (bv #x01 8)) 1024 32 0 32 16 32 2 0) 1024 1024 0 512 16 16 2 0)"
            }
        }
    ],
    " (hvx_swizzle_172_dsl ; hvx_swizzle_124\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 128 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t8\n\t512\n\t2\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_172_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 512 16 16 512 2 0)",
                "dst": "(hexagon_V6_vshuffob_128B_dsl (hexagon_V6_vshuffh_128B_dsl (reg (bv #x01 8)) 1024 32 0 32 16 32 2 0) (hexagon_V6_vshuffh_128B_dsl (reg (bv #x00 8)) 1024 32 0 32 16 32 2 0) 1024 1024 0 512 16 2 16 0)"
            }
        }
    ],
    " (hvx_swizzle_68_dsl ; hvx_swizzle_68\n\t(reg (bv 0 (bitvector 8))) ; < 128 x i16> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t0\n )+D2": [
        {
            "property_name": "EqClassEqualDepthV3Synth",
            "property": {
                "src": "(hvx_swizzle_68_dsl (reg (bv #x00 8)) 1024 1024 0 1024 32 0)",
                "dst": "(hexagon_V6_vassign_128B_dsl (reg (bv #x00 8)) 1024 1024 0 1024 8 0)"
            }
        }
    ]
}