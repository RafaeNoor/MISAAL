{
    " (hexagon_V6_vmpyuhe_acc_128B_dsl ; hexagon_V6_vmpyuhe_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t512\n\t16\n\t32\n\t1\n\t-1\n\t0\n\t0\n\t0\n\t0\n )_ (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hexagon_V6_vmpyuhe_128B_dsl ; hexagon_V6_vmpyuhe_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t0\n\t\t0\n\t\t0\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_hvx_acc",
            "property": {
                "src": "(hexagon_V6_vmpyuhe_acc_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 32 32 0 512 16 32 1 -1 0 0 0 0)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (hexagon_V6_vmpyuhe_128B_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 32 32 0 512 16 32 1 0 0 0 0) (reg (bv #x00 8)) 1024 1024 0 1024 32 -1 0)"
            }
        }
    ],
    " (hexagon_V6_vaslh_acc_128B_dsl ; hexagon_V6_vaslh_acc_128B\n\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t0\n )_ (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hexagon_V6_vaslh_128B_dsl ; hexagon_V6_vaslh_128B\n\t\t(lit (bv #x0000000000000000000000000000000f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_hvx_acc",
            "property": {
                "src": "(hexagon_V6_vaslh_acc_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 1024 1024 0 1024 16 -1 1 32 1 32 0)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (hexagon_V6_vaslh_128B_dsl (lit (bv #x0000000f 32)) (reg (bv #x00 8)) (reg (bv #x02 8)) 1024 1024 0 1024 16 1 32 0) (reg (bv #x01 8)) 1024 1024 0 1024 16 -1 0)"
            }
        }
    ],
    " (hexagon_V6_vaddubh_acc_128B_dsl ; hexagon_V6_vaddubh_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t-1\n\t1\n\t-1\n\t16\n\t-1\n\t1\n\t-1\n\t8\n\t1024\n\t2\n\t0\n )_ (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hexagon_V6_vaddubh_128B_dsl ; hexagon_V6_vaddubh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t0\n\t\t-1\n\t\t16\n\t\t1024\n\t\t0\n\t\t-1\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_hvx_acc",
            "property": {
                "src": "(hexagon_V6_vaddubh_acc_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 1024 1024 0 512 16 0 512 16 32 1 -1 1 -1 32 -1 1 -1 16 1024 2 0)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (hexagon_V6_vaddubh_128B_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 1024 1024 0 512 16 0 512 16 32 1 1 -1 32 1024 1 -1 16 2 0) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)"
            }
        }
    ],
    " (hexagon_V6_vmpyub_acc_128B_dsl ; hexagon_V6_vmpyub_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t-1\n\t0\n\t0\n\t4\n\t4\n\t16\n\t-1\n\t0\n\t0\n\t4\n\t1\n\t4\n\t8\n\t1024\n\t2\n\t0\n )_ (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hexagon_V6_vmpyub_128B_dsl ; hexagon_V6_vmpyub_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t0\n\t\t0\n\t\t4\n\t\t4\n\t\t16\n\t\t1024\n\t\t0\n\t\t0\n\t\t4\n\t\t1\n\t\t4\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_hvx_acc",
            "property": {
                "src": "(hexagon_V6_vmpyub_acc_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 32 32 0 512 8 0 512 8 16 1 -1 1 0 4 4 16 -1 1 0 4 1 4 8 1024 2 0)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (hexagon_V6_vmpyub_128B_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 32 32 0 512 8 0 512 8 16 1 1 0 4 4 16 1024 1 0 4 1 4 8 2 0) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)"
            }
        }
    ],
    " (hexagon_V6_vmpyh_acc_128B_dsl ; hexagon_V6_vmpyh_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t512\n\t16\n\t0\n\t512\n\t16\n\t32\n\t1\n\t-1\n\t1\n\t1\n\t0\n\t32\n\t-1\n\t1\n\t1\n\t16\n\t16\n\t1024\n\t2\n\t0\n )_ (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hexagon_V6_vmpyh_128B_dsl ; hexagon_V6_vmpyh_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t512\n\t\t16\n\t\t0\n\t\t512\n\t\t16\n\t\t32\n\t\t1\n\t\t1\n\t\t1\n\t\t0\n\t\t32\n\t\t1024\n\t\t1\n\t\t1\n\t\t16\n\t\t16\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_hvx_acc",
            "property": {
                "src": "(hexagon_V6_vmpyh_acc_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 32 32 0 512 16 0 512 16 32 1 -1 0 0 0 32 -1 0 0 16 16 1024 2 0)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (hexagon_V6_vmpyh_128B_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 32 32 0 512 16 0 512 16 32 1 0 0 0 32 1024 0 0 16 16 2 0) (reg (bv #x00 8)) 2048 2048 0 2048 32 -1 0)"
            }
        }
    ],
    " (hexagon_V6_vmpyih_acc_128B_dsl ; hexagon_V6_vmpyih_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t-1\n\t1\n\t32\n\t1\n\t32\n\t1\n\t0\n )_ (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hexagon_V6_vmpyih_128B_dsl ; hexagon_V6_vmpyih_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t16\n\t\t1\n\t\t32\n\t\t1\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_hvx_acc",
            "property": {
                "src": "(hexagon_V6_vmpyih_acc_128B_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 -1 1 32 1 32 1 0)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (hexagon_V6_vmpyih_128B_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 1024 1024 0 1024 16 1 32 1 0) (reg (bv #x02 8)) 1024 1024 0 1024 16 -1 0)"
            }
        }
    ],
    " (hexagon_V6_vaslw_acc_128B_dsl ; hexagon_V6_vaslw_acc_128B\n\t(lit (bv #x0000000000000000000000000000001f (bitvector 32)))\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t32\n\t-1\n\t0\n )_ (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hexagon_V6_vaslw_128B_dsl ; hexagon_V6_vaslw_128B\n\t\t(lit (bv #x0000000000000000000000000000001f (bitvector 32)))\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t1024\n\t\t32\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_hvx_acc",
            "property": {
                "src": "(hexagon_V6_vaslw_acc_128B_dsl (lit (bv #x0000001f 32)) (reg (bv #x01 8)) (reg (bv #x00 8)) (reg (bv #x02 8)) 1024 1024 0 1024 32 -1 0)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (hexagon_V6_vaslw_128B_dsl (lit (bv #x0000001f 32)) (reg (bv #x00 8)) (reg (bv #x02 8)) 1024 1024 0 1024 32 0) (reg (bv #x01 8)) 1024 1024 0 1024 32 -1 0)"
            }
        }
    ],
    " (hexagon_V6_vmpybv_acc_128B_dsl ; hexagon_V6_vmpybv_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t-1\n\t1\n\t1\n\t16\n\t-1\n\t1\n\t1\n\t8\n\t1024\n\t2\n\t0\n )_ (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hexagon_V6_vmpybv_128B_dsl ; hexagon_V6_vmpybv_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t1024\n\t\t1024\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t1\n\t\t1\n\t\t16\n\t\t1024\n\t\t1\n\t\t1\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_hvx_acc",
            "property": {
                "src": "(hexagon_V6_vmpybv_acc_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 1024 1024 0 512 8 0 512 8 16 1 -1 0 0 16 -1 0 0 8 1024 2 0)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (hexagon_V6_vmpybv_128B_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 1024 1024 0 512 8 0 512 8 16 1 0 0 16 1024 0 0 8 2 0) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)"
            }
        }
    ],
    " (hexagon_V6_vmpabus_acc_128B_dsl ; hexagon_V6_vmpabus_acc_128B\n\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t32\n\t32\n\t0\n\t512\n\t8\n\t0\n\t512\n\t8\n\t16\n\t1\n\t-1\n\t-1\n\t1\n\t0\n\t8\n\t1024\n\t1\n\t0\n\t0\n\t16\n\t-1\n\t-1\n\t1\n\t0\n\t24\n\t1032\n\t1\n\t0\n\t16\n\t8\n\t1024\n\t2\n\t0\n )_ (hexagon_V6_vaddhsat_128B_dsl ; hexagon_V6_vaddhsat_128B\n\t (hexagon_V6_vmpabus_128B_dsl ; hexagon_V6_vmpabus_128B\n\t\t(reg (bv 0 (bitvector 8))) ; < 1 x i8> False\n\t\t(reg (bv 1 (bitvector 8))) ; < 1 x i8> False\n\t\t32\n\t\t32\n\t\t0\n\t\t512\n\t\t8\n\t\t0\n\t\t512\n\t\t8\n\t\t16\n\t\t1\n\t\t-1\n\t\t1\n\t\t0\n\t\t8\n\t\t1024\n\t\t1\n\t\t0\n\t\t0\n\t\t16\n\t\t1024\n\t\t-1\n\t\t1\n\t\t0\n\t\t24\n\t\t1032\n\t\t1\n\t\t0\n\t\t16\n\t\t8\n\t\t2\n\t\t0\n\t )\n\t(reg (bv 2 (bitvector 8))) ; < 1 x i8> False\n\t1024\n\t1024\n\t0\n\t1024\n\t16\n\t1\n\t0\n )": [
        {
            "property_name": "EqClassEqualDepthV4Full_hvx_acc",
            "property": {
                "src": "(hexagon_V6_vmpabus_acc_128B_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 32 32 0 512 8 0 512 8 16 1 -1 -1 1 0 8 1024 1 0 0 16 -1 -1 1 0 24 1032 1 0 16 8 1024 2 0)",
                "dst": "(hexagon_V6_vaddhsat_128B_dsl (hexagon_V6_vmpabus_128B_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 32 32 0 512 8 0 512 8 16 1 -1 1 0 8 1024 1 0 0 16 1024 -1 1 0 24 1032 1 0 16 8 2 0) (reg (bv #x00 8)) 2048 2048 0 2048 16 -1 0)"
            }
        }
    ]
}