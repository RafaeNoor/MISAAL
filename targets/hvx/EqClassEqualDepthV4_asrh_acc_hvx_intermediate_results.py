{
    " (hexagon_V6_vasrw_acc_128B_dsl ; hexagon_V6_vasrw_128B\n\t(lit (bv #x0000000000000000000000000000001f (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000000 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrw_acc_128B_dsl (lit (bv #x0000001f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 32 32 32) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrw_acc_128B_dsl ; hexagon_V6_vasrw_128B\n\t(lit (bv #x0000000000000000000000000000001f (bitvector 32)))\n\t(lit (bv #x00000000000000000000000000000000 (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrw_acc_128B_dsl (lit (bv #x0000001f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (typed:xBroadcast (reg (bv #x01 8)) 32 32 2) 64 64 16) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrw_acc_128B_dsl ; hexagon_V6_vasrw_acc_128B\n\t(lit (bv #x0000000000000000000000000000001f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrw_acc_128B_dsl (lit (bv #x0000001f 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(typed:vec-add (typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 32 32 32) 32 1024) (reg (bv #x01 8)) 32 1024)"
            }
        }
    ],

    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1\n\t64\n\t8\n\t#f\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-saturate (typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 16 1 64 32) (typed:xBroadcast (reg (bv #x01 8)) 32 32 64) 32 2048) 32 1 64 16 #t)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t64\n\t\t\t8\n\t\t\t#f\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (typed:vec-saturate (reg (bv #x01 8)) 32 1 1 16 #t) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:vec-saturate (typed:xBroadcast (reg (bv #x01 8)) 32 32 64) 16 1 128 8 #t) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t64\n\t\t\t8\n\t\t\t#f\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-uint-extend (reg (bv #x00 8)) 32 1 32 64) 64 1 32 32 #f) (typed:xBroadcast (typed:vec-saturate (reg (bv #x01 8)) 16 1 2 8 #t) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-uint-extend (reg (bv #x00 8)) 8 1 128 16) 16 1 128 8 #f) (typed:vec-saturate (typed:xBroadcast (reg (bv #x01 8)) 32 32 64) 16 1 128 8 #t) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t64\n\t\t\t8\n\t\t\t#f\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-int-extend (reg (bv #x00 8)) 8 1 128 16) 16 1 128 8 #t) (typed:xBroadcast (typed:vec-saturate (reg (bv #x01 8)) 32 1 1 16 #t) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-int-extend (reg (bv #x00 8)) 32 1 32 64) 64 1 32 32 #t) (typed:vec-saturate (typed:xBroadcast (reg (bv #x01 8)) 32 32 64) 16 1 128 8 #t) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:xBroadcast (reg (bv #x01 8)) 32 32 32) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:cast-int-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1\n\t64\n\t8\n\t#f\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-int-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-saturate (typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 32 1 32 64) (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 16 2048) 64 1 32 32 #t)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1\n\t64\n\t8\n\t#f\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-saturate (typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 64 32) (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 16 2048) 32 1 64 16 #f)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-int-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 16) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-int-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:slice_vectors (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 0 1 32 32 2048) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 64 32) 32 1 64 16 #f) (typed:xBroadcast (typed:xBroadcast (reg (bv #x01 8)) 16 16 2) 32 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-uint-extend (reg (bv #x00 8)) 32 1 32 64) 64 1 32 32 #f) (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-uint-extend (reg (bv #x00 8)) 8 1 128 16) 16 1 128 8 #f) (typed:slice_vectors (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 128 1 128 8 2048) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-int-extend (reg (bv #x00 8)) 32 1 32 64) 64 1 32 32 #t) (typed:xBroadcast (typed:xBroadcast (reg (bv #x01 8)) 16 16 2) 32 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-int-extend (reg (bv #x00 8)) 32 1 32 64) 64 1 32 32 #t) (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-int-extend (reg (bv #x00 8)) 32 1 32 64) 64 1 32 32 #t) (typed:slice_vectors (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 64 1 64 16 2048) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1\n\t64\n\t8\n\t#f\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-saturate (typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 16 1 64 32) (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 16 2048) 32 1 64 16 #t)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1\n\t64\n\t8\n\t#f\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-saturate (typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 32 1 32 64) (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 16 2048) 64 1 32 32 #f)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (typed:xBroadcast (reg (bv #x01 8)) 16 16 2) 32 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:slice_vectors (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 0 1 16 64 2048) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 64 32) 32 1 64 16 #f) (typed:xBroadcast (typed:xBroadcast (reg (bv #x01 8)) 16 16 2) 32 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-uint-extend (reg (bv #x00 8)) 32 1 32 64) 64 1 32 32 #f) (typed:slice_vectors (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 32 1 32 32 2048) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 64 32) 32 1 64 16 #f) (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-int-extend (reg (bv #x00 8)) 16 1 64 32) 32 1 64 16 #t) (typed:xBroadcast (typed:xBroadcast (reg (bv #x01 8)) 16 16 2) 32 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-int-extend (reg (bv #x00 8)) 32 1 32 64) 64 1 32 32 #t) (typed:xBroadcast (reg (bv #x01 8)) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:vec-saturate (typed:cast-int-extend (reg (bv #x00 8)) 8 1 128 16) 16 1 128 8 #t) (typed:slice_vectors (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 16 1 16 64 2048) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:xBroadcast (typed:xBroadcast (reg (bv #x01 8)) 32 32 2) 64 64 16) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:slice_vectors (typed:xBroadcast (reg (bv #x01 8)) 32 32 64) 0 1 16 64 2048) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t64\n\t\t\t8\n\t\t\t#f\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:xBroadcast (typed:vec-saturate (reg (bv #x01 8)) 16 1 2 8 #t) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:vec-saturate (typed:xBroadcast (reg (bv #x01 8)) 32 32 64) 32 1 64 16 #t) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1\n\t128\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-int-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:cast-int-extend (typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 32) 16 512) 32 1 16 64)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:xBroadcast (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 16) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:xBroadcast (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 32 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-int-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:xBroadcast (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 32 32 32) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t64\n\t\t\t8\n\t\t\t#f\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:xBroadcast (typed:vec-saturate (reg (bv #x01 8)) 16 1 1 8 #t) 8 8 128) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:slice_vectors (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 128 1 128 8 2048) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:cast-int-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:vec-saturate (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 16 1 128 8 #t) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-uint-extend (typed:xBroadcast (reg (bv #x01 8)) 16 16 32) 32 1 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-int-extend (typed:xBroadcast (reg (bv #x01 8)) 16 16 32) 16 1 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1\n\t128\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:cast-int-extend (typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 32) 16 512) 32 1 16 64)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:xBroadcast (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 32 32 32) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:xBroadcast (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 16) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:xBroadcast (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 32 32 32) 32 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t64\n\t\t\t8\n\t\t\t#f\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:xBroadcast (typed:vec-saturate (reg (bv #x01 8)) 16 1 1 8 #t) 8 8 128) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 16 1 32 32) (typed:slice_vectors (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 128 1 128 8 2048) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-uint-extend (typed:xBroadcast (reg (bv #x01 8)) 16 16 32) 32 1 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-int-extend (typed:xBroadcast (reg (bv #x01 8)) 16 16 32) 32 1 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-int-extend (reg (bv #x00 8)) 8 1 64 16) (typed:vec-saturate (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 16 1 128 8 #t) 8 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t64\n\t\t\t8\n\t\t\t#f\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 8 1 64 16) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 8 1 64 16) (typed:xBroadcast (typed:vec-saturate (reg (bv #x01 8)) 16 1 2 8 #t) 16 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 8 1 64 16) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 8 1 64 16) (typed:vec-saturate (typed:xBroadcast (reg (bv #x01 8)) 32 32 64) 32 1 64 16 #t) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1\n\t128\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:cast-uint-extend (typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 32) 16 512) 32 1 16 64)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 8 1 64 16) (typed:cast-int-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 8 1 64 16) (typed:xBroadcast (typed:xBroadcast (reg (bv #x01 8)) 16 16 4) 64 64 16) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-int-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:xBroadcast (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 32 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-int-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 32 1 16 64) (typed:slice_vectors (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 0 1 64 16 2048) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:xBroadcast (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 32 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-uint-extend (typed:xBroadcast (reg (bv #x01 8)) 16 16 32) 32 1 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-int-extend (typed:xBroadcast (reg (bv #x01 8)) 16 16 32) 16 1 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1\n\t128\n\t32\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:cast-uint-extend (typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x01 8)) 16 16 32) 16 512) 16 1 32 32)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 8 1 64 16) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 8 1 64 16) (typed:xBroadcast (typed:xBroadcast (reg (bv #x01 8)) 16 16 2) 32 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:xBroadcast (typed:cast-int-extend (reg (bv #x01 8)) 16 1 1 32) 32 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t16\n\t\t64\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:xBroadcast (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 32 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:slice_vectors ; typed:slice_vectors_ip16_is1024_op16_os512_signed_None_0_1_32\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t0\n\t\t1\n\t\t32\n\t\t16\n\t\t1024\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:slice_vectors (typed:xBroadcast (reg (bv #x01 8)) 16 16 128) 32 1 32 32 2048) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-uint-extend (reg (bv #x01 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 32 32) (typed:cast-uint-extend (typed:xBroadcast (reg (bv #x01 8)) 16 16 32) 16 1 32 32) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(lit (bv #x0000000000000000000000000000000 (bitvector 1024)))\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 1024)) (typed:cast-uint-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-uint-extend (reg (bv #x01 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:signed-vec-shr (typed:cast-uint-extend (reg (bv #x00 8)) 32 1 16 64) (typed:cast-int-extend (typed:xBroadcast (reg (bv #x01 8)) 16 16 32) 32 1 16 64) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) (typed:cast-int-extend (reg (bv #x02 8)) 8 1 2 16) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-add (typed:signed-vec-shr (reg (bv #x01 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 64) 16 1024) (reg (bv #x00 8)) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) (typed:cast-int-extend (reg (bv #x02 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-add (typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 64) 16 1024) (typed:vec-saturate (typed:cast-int-extend (reg (bv #x01 8)) 32 1 32 64) 64 1 32 32 #t) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) (typed:cast-int-extend (reg (bv #x02 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-add (typed:signed-vec-shr (reg (bv #x01 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 64) 16 1024) (typed:vec-saturate (typed:cast-uint-extend (reg (bv #x00 8)) 8 1 128 16) 16 1 128 8 #f) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x02 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-add (typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 64) 16 1024) (reg (bv #x01 8)) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-int-extend ; typed:cast-int_1_ip16_is2048_op32_os4096_signed_1\n\t\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) (typed:cast-uint-extend (reg (bv #x02 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-add (typed:signed-vec-shr (reg (bv #x00 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 64) 16 1024) (typed:vec-saturate (typed:cast-int-extend (reg (bv #x01 8)) 8 1 128 16) 16 1 128 8 #t) 16 1024)"
            }
        }
    ],
    " (hexagon_V6_vasrh_acc_128B_dsl ; hexagon_V6_vasrh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t16\n\t\t1\n\t\t128\n\t\t32\n\t )\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (typed:vec-add ; typed:vec-add_p16_s1024_signed_None\n\t (typed:signed-vec-shr ; typed:signed-vec-shr_p16_s1024_signed_1\n\t\t(buffer-index  0 'uint8 8) ; < 1 x i8> False\n\t\t (typed:xBroadcast ; typed:xBroadcast_is16_os1024_signed_None\n\t\t\t(buffer-index  1 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t16\n\t\t\t64\n\t\t )\n\t\t16\n\t\t1024\n\t )\n\t (typed:vec-saturate ; typed:vec-saturate_1_ip16_is1024_op8_os512_signed_0\n\t\t (typed:cast-uint-extend ; typed:cast-uint_1_ip16_is2048_op32_os4096_signed_0\n\t\t\t(buffer-index  2 'uint8 8) ; < 1 x i8> False\n\t\t\t16\n\t\t\t1\n\t\t\t128\n\t\t\t32\n\t\t )\n\t\t16\n\t\t1\n\t\t64\n\t\t8\n\t\t#f\n\t )\n\t16\n\t1024\n )": [
        {
            "property_name": "EqClassEqualDepthV4_asrh_acc",
            "property": {
                "src": "(hexagon_V6_vasrh_acc_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x00 8)) (reg (bv #x01 8)) (typed:cast-uint-extend (reg (bv #x02 8)) 16 1 1 32) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(typed:vec-add (typed:signed-vec-shr (reg (bv #x01 8)) (typed:xBroadcast (reg (bv #x02 8)) 16 16 64) 16 1024) (typed:vec-saturate (typed:cast-uint-extend (reg (bv #x00 8)) 16 1 64 32) 32 1 64 16 #f) 16 1024)"
            }
        }
    ]
}
