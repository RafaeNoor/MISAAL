hvx_RepairRelavance={
    "hexagon_V6_vshuffob_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (reg (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (reg (bv #x00 8)) (typed:unsigned-vec-mod (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x01 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vshuffob_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffob_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdmpyhb_acc_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpyhb_acc_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-widen-mul (reg (bv #x00 8)) (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 16) 16 32) 32 64)"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #f) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #f)"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(repair-saturate_dsl (typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 32 1 1 64) 64 1 1 32) 32 16 32 #f)"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-saturate_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (lit (bv #x00000001 32)) (lit (bv #x00000001 32)) 32 32) 32 32) 32 16 32 #f)"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(repair-saturate_dsl (typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32) 32 32) 32 16 32 #f)"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-saturate_dsl (typed:unsigned-vec-mod (reg (bv #x00 8)) (typed:unsigned-vec-mod (reg (bv #x00 8)) (lit (bv #x00000001 32)) 32 32) 32 32) 32 16 32 #f)"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-saturate_dsl (typed:unsigned-vec-widen-mul (lit (bv #x0001 16)) (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #f) 16 16) 32 16 32 #f)"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-saturate_dsl (typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 32 32) 32 32) 32 16 32 #f)"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(repair-saturate_dsl (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32) 32 32) 32 16 32 #f)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vpackwuh_sat_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackwuh_sat_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #f)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (reg (bv #x00 8)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:signed-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (reg (bv #x00 8)) (typed:unsigned-vec-mod (reg (bv #x00 8)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (lit (bv #x0001 16)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vpackeh_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackeh_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(repair-add_dsl (repair-smul_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 16) (typed:cast-int (typed:cast-int (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(repair-add_dsl (typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16) (repair-smul_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(repair-add_dsl (reg (bv #x00 8)) (typed:signed-vec-mul (reg (bv #x02 8)) (reg (bv #x01 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-add_dsl (repair-smul_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 16) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-ssat-sub_dsl (repair-add_dsl (repair-smul_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 16 16) (reg (bv #x00 8)) 16 16) (typed:signed-vec-mod (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_lvsplatb_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lvsplatb_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_lvsplatb_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lvsplatb_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_lvsplatb_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lvsplatb_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lvsplatb_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lvsplatb_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lvsplatb_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lvsplatb_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:signed-vec-shr (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lvsplatb_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lvsplatb_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (typed:signed-vec-sat-sub (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lvsplatb_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lvsplatb_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lvsplatb_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lvsplatb_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (reg (bv #x00 8)) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lvsplatb_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lvsplatb_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lvsplatb_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lvsplatb_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x01 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lvsplatb_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lvsplatb_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-add_dsl (reg (bv #x00 8)) (repair-smul_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-add_dsl (repair-smul_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 16) (typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:vec-bwand": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:vec-bwand",
                "synth_expression": "(repair-add_dsl (reg (bv #x00 8)) (repair-ssat-add_dsl (repair-smul_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 16 16) (typed:vec-bwand (reg (bv #x01 8)) (lit (bv #x0001 16)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-ssat-add_dsl (repair-add_dsl (repair-smul_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 16 16) (reg (bv #x00 8)) 16 16) (typed:unsigned-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x01 8)) 8 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(repair-add_dsl (typed:unsigned-vec-mul (reg (bv #x02 8)) (reg (bv #x01 8)) 16 16) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-ssat-sub_dsl (repair-add_dsl (repair-smul_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 16) (reg (bv #x00 8)) 16 16) (typed:signed-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x01 8)) 8 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(repair-add_dsl (typed:signed-vec-shr (repair-smul_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 16 16) (typed:signed-vec-shr (lit (bv #x0001 16)) (reg (bv #x01 8)) 16 16) 16 16) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(typed:signed-vec-sat-sub (repair-add_dsl (repair-smul_dsl (reg (bv #x02 8)) (reg (bv #x01 8)) 16 16) (reg (bv #x00 8)) 16 16) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_acc_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_acc_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (typed:unsigned-vec-mod (reg (bv #x02 8)) (reg (bv #x02 8)) 16 16) 16 16) (repair-smul_dsl (reg (bv #x01 8)) (reg (bv #x02 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpabus_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpabus_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (repair-smul_dsl (typed:cast-uint (reg (bv #x00 8)) 8 1 2 16) (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 16) 16 32) 16 32)"
            }
        }
    ],
    "hexagon_V6_vmpabus_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpabus_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 16) (typed:unsigned-vec-widen-mul (lit (bv #x0101 16)) (reg (bv #x00 8)) 8 16) 16 32) 16 32)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(repair-sabsd_dsl (reg (bv #x01 8)) (typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(repair-sabsd_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (typed:signed-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-sabsd_dsl (reg (bv #x01 8)) (repair-sub_dsl (reg (bv #x00 8)) (typed:signed-vec-widen-mul (lit (bv #x01 8)) (lit (bv #x00 8)) 8 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "output_expression": "typed:unsigned-vec-sat-add",
                "synth_expression": "(typed:unsigned-vec-sat-add (lit (bv #x0001 16)) (repair-sub_dsl (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (typed:signed-vec-sat-sub (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(repair-sub_dsl (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (typed:unsigned-vec-sat-sub (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (reg (bv #x00 8)) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-sabsd_dsl (reg (bv #x00 8)) (repair-sub_dsl (reg (bv #x01 8)) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-sub_dsl (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (typed:unsigned-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x01 8)) 8 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-sabsd_dsl (reg (bv #x01 8)) (typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(repair-sabsd_dsl (reg (bv #x01 8)) (typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vabsdiffh_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vabsdiffh_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-sub_dsl (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshuffeb_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffeb_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vgtb_128B+typed:signed-vec-lt": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vgtb_128B",
                "output_expression": "typed:signed-vec-lt",
                "synth_expression": "(typed:signed-vec-lt (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-cast-uint_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8) 8 16 8)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8) 8 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-cast-uint_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8) 8 16 8)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(repair-usat-add_dsl (repair-cast-uint_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8) 8 16 8) (typed:signed-vec-shr (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(repair-usat-add_dsl (repair-umul_dsl (lit (bv #x0000 16)) (typed:unsigned-vec-mul (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16) (repair-cast-uint_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8) 8 16 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(typed:unsigned-vec-widen-mul (lit (bv #x01 8)) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(repair-usat-add_dsl (repair-cast-uint_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8) 8 16 8) (typed:unsigned-vec-sat-sub (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-cast-uint_dsl (repair-usat-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8) 8 8) 8 16 8)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8) 8 16 8) (typed:signed-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x01 8)) 8 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(repair-smul_dsl (typed:cast-int (reg (bv #x00 8)) 16 1 1 32) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(repair-usat-add_dsl (repair-cast-uint_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8) 8 16 8) (typed:cast-int (lit (bv #x00000000 32)) 32 1 1 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(repair-ssat-add_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) 32 32) (typed:cast-uint (lit (bv #x0000000000000000 64)) 64 1 1 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) 32 32) (typed:signed-vec-div (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-ssat-sub_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) 32 32) (typed:signed-vec-mod (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vaddubh_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddubh_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8) 8 16 8) (typed:vec-bwnot (typed:vec-bwnot (lit (bv #x0000 16)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(typed:signed-vec-shr (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) 32 32) (typed:signed-vec-shr (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:vec-bwand": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:vec-bwand",
                "synth_expression": "(repair-ssat-add_dsl (typed:vec-bwand (lit (bv #x00010001 32)) (repair-ssat-add_dsl (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32) (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(typed:unsigned-vec-mul (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) 32 32) (typed:unsigned-vec-shr (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(typed:signed-vec-mul (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(repair-ssat-sub_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) 32 32) (typed:unsigned-vec-sat-sub (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:unsigned-vec-sat-add",
                "synth_expression": "(typed:unsigned-vec-sat-add (repair-smul_dsl (lit (bv #x00000000 32)) (typed:unsigned-vec-sat-add (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32) (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(repair-ssat-add_dsl (typed:signed-vec-sat-sub (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(repair-smul_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) (typed:unsigned-vec-div (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-ssat-add_dsl (typed:vec-bwnot (typed:vec-bwnot (lit (bv #x00000000 32)) 32 32) 32 32) (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vshufoeh_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vshufoeh_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vshufoeh_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshufoeh_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshufoeh_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (typed:signed-vec-sat-sub (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshufoeh_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:signed-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshufoeh_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (reg (bv #x00 8)) (typed:unsigned-vec-mod (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-ssat-sub_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) 32 32) (typed:unsigned-vec-mod (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vshufoeh_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshufoeh_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshufoeh_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshufoeh_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:signed-vec-sat-add",
                "synth_expression": "(repair-ssat-sub_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) 32 32) (repair-smul_dsl (lit (bv #x00000000 32)) (typed:signed-vec-sat-add (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyh_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyh_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-smul_dsl (typed:unsigned-vec-widen-mul (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-ssat-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-ssat-add_dsl (repair-ssat-add_dsl (reg (bv #x01 8)) (typed:signed-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x00 8)) 8 8) 16 16) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (repair-ssat-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (repair-ssat-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(repair-ssat-add_dsl (reg (bv #x00 8)) (repair-ssat-add_dsl (reg (bv #x01 8)) (typed:signed-vec-shr (lit (bv #x0001 16)) (reg (bv #x00 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:signed-vec-sat-add",
                "synth_expression": "(typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(repair-ssat-add_dsl (typed:signed-vec-mul (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 16 16) (lit (bv #x0000 16)) 16 16) (repair-ssat-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(repair-ssat-add_dsl (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x01 8)) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-ssat-add_dsl (reg (bv #x01 8)) (typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(repair-ssat-add_dsl (typed:unsigned-vec-mul (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (lit (bv #x0000 16)) 16 16) (repair-ssat-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (repair-ssat-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-ssat-add_dsl (reg (bv #x01 8)) (repair-ssat-add_dsl (reg (bv #x00 8)) (typed:unsigned-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x01 8)) 8 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-ssat-add_dsl (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) (repair-ssat-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (repair-ssat-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (typed:unsigned-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:vec-bwand": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:vec-bwand",
                "synth_expression": "(repair-ssat-add_dsl (repair-ssat-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (typed:vec-bwand (lit (bv #x0000 16)) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaddhsat_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaddhsat_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-ssat-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-bwor_dsl (lit (bv #x00000001 32)) (repair-usat-sub_dsl (reg (bv #x00 8)) (lit (bv #x00000001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 32 1 1 64) 64 1 1 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 32 1 1 64) 64 1 1 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-bwor_dsl (typed:signed-vec-widen-mul (lit (bv #x0000 16)) (lit (bv #x0001 16)) 16 16) (reg (bv #x00 8)) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(repair-shl_dsl (reg (bv #x00 8)) (typed:signed-vec-shr (lit (bv #x00000001 32)) (reg (bv #x00 8)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(repair-usat-add_dsl (reg (bv #x00 8)) (typed:signed-vec-sat-sub (lit (bv #x00000001 32)) (lit (bv #x00000001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-bwor_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32) (reg (bv #x00 8)) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(repair-umul_dsl (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(repair-usat-sub_dsl (reg (bv #x00 8)) (typed:signed-vec-div (lit (bv #x00000001 32)) (reg (bv #x00 8)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-bwor_dsl (repair-usat-sub_dsl (reg (bv #x00 8)) (lit (bv #x00000001 32)) 32 32) (lit (bv #x00000001 32)) 32 32)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-cast-uint_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-shl_dsl (reg (bv #x00 8)) (typed:unsigned-vec-widen-mul (lit (bv #x0000 16)) (lit (bv #x0000 16)) 16 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 32 16) (typed:cast-int (lit (bv #x0000 16)) 16 1 1 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(repair-shl_dsl (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x00000001 32)) (reg (bv #x00 8)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:vec-bwand": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:vec-bwand",
                "synth_expression": "(repair-shl_dsl (reg (bv #x00 8)) (typed:vec-bwand (lit (bv #x00000001 32)) (repair-usat-add_dsl (lit (bv #x00000001 32)) (lit (bv #x00000001 32)) 32 32) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(repair-usat-sub_dsl (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (lit (bv #x00000001 32)) (lit (bv #x00000001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(repair-cast-uint_dsl (typed:signed-vec-mul (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (repair-sub_dsl (lit (bv #x0000 16)) (lit (bv #x0001 16)) 16 16) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:unsigned-vec-sat-add",
                "synth_expression": "(typed:unsigned-vec-sat-add (repair-usat-sub_dsl (reg (bv #x00 8)) (lit (bv #x00000001 32)) 32 32) (lit (bv #x00000001 32)) 32 32)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 1 1 32)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-cast-uint_dsl (repair-usat-sub_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(repair-bwor_dsl (reg (bv #x00 8)) (typed:unsigned-vec-mul (typed:unsigned-vec-mul (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32) (lit (bv #x00000000 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackoh_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackoh_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-bwor_dsl (reg (bv #x00 8)) (typed:unsigned-vec-mod (lit (bv #x00000001 32)) (lit (bv #x00000001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(repair-sub_dsl (typed:cast-int (typed:cast-int (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16) (reg (bv #x01 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-sub_dsl (reg (bv #x00 8)) (repair-sub_dsl (reg (bv #x01 8)) (typed:signed-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x01 8)) 8 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(repair-sub_dsl (reg (bv #x00 8)) (typed:signed-vec-shr (reg (bv #x01 8)) (typed:signed-vec-shr (lit (bv #x0001 16)) (reg (bv #x01 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(typed:signed-vec-mul (repair-sub_dsl (lit (bv #x0000 16)) (lit (bv #x0001 16)) 16 16) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-cast-uint_dsl (repair-sub_dsl (typed:vec-bwnot (reg (bv #x01 8)) 16 16) (typed:vec-bwnot (reg (bv #x00 8)) 16 16) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(repair-sub_dsl (repair-sub_dsl (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16) (reg (bv #x01 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-uabsd_dsl (typed:unsigned-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x01 8)) 8 8) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-sub_dsl (typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 16 16) 16 16) (reg (bv #x01 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-uabsd_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (repair-sabsd_dsl (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+typed:vec-bwand": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "output_expression": "typed:vec-bwand",
                "synth_expression": "(repair-uabsd_dsl (typed:vec-bwand (repair-usat-add_dsl (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) (lit (bv #x00010001 32)) 32 32) (repair-cast-uint_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 32 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(repair-cast-uint_dsl (repair-usat-sub_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (typed:unsigned-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-cast-uint_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-sub_dsl (repair-sub_dsl (reg (bv #x00 8)) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) (reg (bv #x01 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsubh_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubh_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(typed:unsigned-vec-mul (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (repair-sub_dsl (lit (bv #x0000 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(repair-cast-uint_dsl (typed:unsigned-vec-mul (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (repair-sub_dsl (lit (bv #x0000 16)) (lit (bv #x0001 16)) 16 16) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (repair-cast-uint_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 32 16) (typed:unsigned-vec-mod (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(typed:unsigned-vec-widen-mul (lit (bv #x0001 16)) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsubuhw_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsubuhw_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-cast-uint_dsl (repair-umul_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (typed:signed-vec-widen-mul (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-shl_dsl (repair-sshr_dsl (reg (bv #x01 8)) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) (repair-smax_dsl (reg (bv #x00 8)) (typed:unsigned-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x01 8)) 8 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-shl_dsl (repair-sshr_dsl (reg (bv #x01 8)) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) (repair-smax_dsl (reg (bv #x00 8)) (typed:signed-vec-widen-mul (lit (bv #x01 8)) (lit (bv #x00 8)) 8 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (repair-smul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (repair-smul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-ssat-sub_dsl (repair-smul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (typed:signed-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x00 8)) 8 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(repair-smul_dsl (reg (bv #x00 8)) (repair-ssat-add_dsl (reg (bv #x01 8)) (typed:signed-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-smul_dsl (repair-ssat-sub_dsl (reg (bv #x00 8)) (typed:unsigned-vec-mod (reg (bv #x01 8)) (lit (bv #x0001 16)) 16 16) 16 16) (reg (bv #x01 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(repair-shl_dsl (repair-sshr_dsl (reg (bv #x01 8)) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) (repair-smax_dsl (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (lit (bv #x0001 16)) (reg (bv #x01 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(repair-shl_dsl (repair-sshr_dsl (reg (bv #x01 8)) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) (repair-smax_dsl (reg (bv #x00 8)) (typed:signed-vec-sat-sub (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (repair-smul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vaslhv_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vaslhv_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(repair-shl_dsl (repair-sshr_dsl (reg (bv #x01 8)) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) (repair-smax_dsl (typed:cast-uint (lit (bv #x00000000 32)) 32 1 1 16) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-ssat-add_dsl (typed:unsigned-vec-widen-mul (lit (bv #x01 8)) (lit (bv #x00 8)) 8 8) (repair-smul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (repair-smul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(repair-smul_dsl (reg (bv #x01 8)) (repair-ssat-add_dsl (typed:unsigned-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyih_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyih_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(repair-ssat-add_dsl (repair-smul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (typed:unsigned-vec-sat-sub (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vdealb_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_vdealb_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_vdealb_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:signed-vec-shr (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (typed:signed-vec-sat-sub (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (reg (bv #x00 8)) (typed:unsigned-vec-mod (reg (bv #x00 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(repair-saturate_dsl (typed:cast-int (typed:cast-int (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16) 16 8 16 #f)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (repair-saturate_dsl (reg (bv #x00 8)) 16 8 16 #f) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-saturate_dsl (reg (bv #x00 8)) 16 8 16 #f)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(repair-saturate_dsl (typed:signed-vec-shr (reg (bv #x00 8)) (typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) 16 8 16 #f)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(repair-saturate_dsl (typed:signed-vec-sat-sub (reg (bv #x00 8)) (typed:signed-vec-sat-sub (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16) 16 8 16 #f)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (repair-saturate_dsl (reg (bv #x00 8)) 16 8 16 #f) (typed:unsigned-vec-mod (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(repair-saturate_dsl (typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) 16 8 16 #f)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-saturate_dsl (reg (bv #x00 8)) 16 8 16 #f)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-saturate_dsl (typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 16 16) 16 16) 16 8 16 #f)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-saturate_dsl (typed:unsigned-vec-widen-mul (repair-saturate_dsl (reg (bv #x00 8)) 16 8 16 #f) (lit (bv #x01 8)) 8 8) 16 8 16 #f)"
            }
        }
    ],
    "hexagon_V6_vsathub_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsathub_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (repair-saturate_dsl (reg (bv #x00 8)) 16 8 16 #f) (typed:unsigned-vec-sat-sub (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32) 32 64)"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (typed:cast-int (reg (bv #x00 8)) 16 1 2 32) 32 64) 32 64)"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:unsigned-vec-mul (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 32) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 32 64) 32 64)"
            }
        }
    ],
    "hexagon_V6_vdmpyhvsat_acc_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpyhvsat_acc_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-mul (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 32) 32 64) 32 64)"
            }
        }
    ],
    "hexagon_V6_vdealb4w_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb4w_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb4w_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb4w_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_vdealb4w_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb4w_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_vdealb4w_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb4w_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb4w_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb4w_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:signed-vec-shr (lit (bv #x01 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb4w_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb4w_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb4w_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb4w_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb4w_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb4w_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (reg (bv #x00 8)) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb4w_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb4w_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb4w_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb4w_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vdealb4w_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdealb4w_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vrmpybv_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vrmpybv_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 4 (repair-cast-int_dsl (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32) 16 32 64) 32 128)"
            }
        }
    ],
    "hexagon_V6_vdmpybus_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpybus_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 16) (typed:cast-uint (reg (bv #x00 8)) 8 1 2 16) 16 32) 16 32)"
            }
        }
    ],
    "hexagon_V6_vrmpybus_acc_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vrmpybus_acc_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 4 (repair-cast-uint_dsl (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32) 16 32 64) 32 128)"
            }
        }
    ],
    "hexagon_V6_vrmpybus_acc_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vrmpybus_acc_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 4 (typed:signed-vec-widen-mul (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 32) 16 64) 32 128)"
            }
        }
    ],
    "hexagon_V6_vdmpybus_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpybus_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 16) (typed:unsigned-vec-widen-mul (lit (bv #x0101 16)) (reg (bv #x00 8)) 8 16) 16 32) 16 32)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(typed:signed-vec-shr (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) 32 32) (typed:signed-vec-shr (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(repair-usat-add_dsl (typed:cast-int (lit (bv #x0000000000000000 64)) 64 1 1 32) (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(repair-umul_dsl (typed:cast-uint (reg (bv #x01 8)) 16 1 1 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-usat-sub_dsl (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32) (typed:vec-bwnot (typed:vec-bwnot (lit (bv #x00000000 32)) 32 32) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:signed-vec-sat-add",
                "synth_expression": "(repair-usat-add_dsl (repair-usat-sub_dsl (lit (bv #x00000000 32)) (typed:signed-vec-sat-add (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32) (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (typed:signed-vec-sat-sub (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:signed-vec-shr (lit (bv #x0001 16)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(typed:signed-vec-mul (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (reg (bv #x00 8)) (typed:unsigned-vec-mod (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(repair-usat-add_dsl (typed:signed-vec-sat-sub (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:unsigned-vec-sat-add",
                "synth_expression": "(typed:unsigned-vec-sat-add (repair-usat-sub_dsl (lit (bv #x00010001 32)) (typed:unsigned-vec-sat-add (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32) (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(repair-usat-sub_dsl (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32) (typed:unsigned-vec-shr (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(repair-usat-sub_dsl (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32) (typed:unsigned-vec-sat-sub (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(typed:unsigned-vec-mul (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) (typed:unsigned-vec-div (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:vec-bwand": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:vec-bwand",
                "synth_expression": "(repair-umul_dsl (typed:vec-bwand (repair-umul_dsl (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) (lit (bv #x00010001 32)) 32 32) (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) 32 32) (typed:signed-vec-div (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vpackoh_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vpackoh_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32) (typed:signed-vec-mod (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32) (typed:unsigned-vec-mod (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vdmpyhisat_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpyhisat_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 32) (typed:cast-int (reg (bv #x01 8)) 16 1 2 32) 32 64) 32 64)"
            }
        }
    ],
    "hexagon_V6_vmpyuhe_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyuhe_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-usat-add_dsl (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 32 16) 32 32) (typed:signed-vec-widen-mul (lit (bv #x0000 16)) (reg (bv #x00 8)) 16 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vdmpyhisat_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpyhisat_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32) 32 64)"
            }
        }
    ],
    "hexagon_V6_vdmpyhisat_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpyhisat_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-mul (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 32) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 32 64) 32 64)"
            }
        }
    ],
    "hexagon_V6_vdmpyhisat_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpyhisat_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:unsigned-vec-mul (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 32) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 32 64) 32 64)"
            }
        }
    ],
    "hexagon_V6_vshuffh_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffh_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vshuffh_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffh_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vshuffh_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffh_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshuffh_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffh_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:signed-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshuffh_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffh_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshuffh_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffh_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshuffh_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffh_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (reg (bv #x00 8)) (typed:unsigned-vec-mod (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshuffh_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffh_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshuffh_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffh_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshuffh_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffh_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vshuffh_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vshuffh_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vmpabusv_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpabusv_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (repair-umul_dsl (typed:cast-uint (reg (bv #x01 8)) 8 1 2 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 16) 16 32) 16 32)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(repair-bwor_dsl (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (typed:signed-vec-mul (lit (bv #x0000 16)) (typed:signed-vec-mul (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-bwor_dsl (reg (bv #x01 8)) (repair-bwor_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (lit (bv #x0001 16)) 16 16) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpabusv_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpabusv_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16) 16 32)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-bwor_dsl (reg (bv #x00 8)) (repair-bwor_dsl (typed:signed-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x01 8)) 8 8) (reg (bv #x01 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(repair-bwor_dsl (typed:signed-vec-sat-sub (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-bwor_dsl (repair-bwor_dsl (reg (bv #x01 8)) (typed:unsigned-vec-mod (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(repair-bwor_dsl (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (typed:unsigned-vec-mul (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 16 16) (lit (bv #x0000 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) (typed:unsigned-vec-sat-sub (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-bwor_dsl (repair-bwor_dsl (reg (bv #x00 8)) (typed:unsigned-vec-widen-mul (lit (bv #x01 8)) (lit (bv #x00 8)) 8 8) 16 16) (reg (bv #x01 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:vec-bwand": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:vec-bwand",
                "synth_expression": "(repair-bwor_dsl (repair-bwor_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (reg (bv #x00 8)) 16 16) (reg (bv #x01 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-bwor_dsl (reg (bv #x00 8)) (typed:vec-bwnot (typed:vec-bwnot (reg (bv #x01 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vor_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vor_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(repair-bwor_dsl (reg (bv #x01 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpabusv_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpabusv_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:unsigned-vec-mul (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 16) (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 16) 16 32) 16 32)"
            }
        }
    ],
    "hexagon_V6_vmpabusv_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpabusv_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-mul (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 16) (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 16) 16 32) 16 32)"
            }
        }
    ],
    "hexagon_V6_vandvrt_128B+typed:unsigned-vec-lt": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vandvrt_128B",
                "output_expression": "typed:unsigned-vec-lt",
                "synth_expression": "(typed:unsigned-vec-lt (lit (bv #x00 8)) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vandvrt_128B+typed:unsigned-vec-le": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vandvrt_128B",
                "output_expression": "typed:unsigned-vec-le",
                "synth_expression": "(typed:unsigned-vec-le (lit (bv #x01 8)) (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vavgwrnd_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vavgwrnd_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (repair-add_dsl (lit (bv #x00000001 32)) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 32 32) (repair-add_dsl (lit (bv #x00000001 32)) (lit (bv #x00000001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmaxw_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmaxw_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (repair-smax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 32 1 1 64) 64 1 1 32)"
            }
        }
    ],
    "hexagon_V6_vmaxw_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmaxw_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (repair-smax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 32 1 1 64) 64 1 1 32)"
            }
        }
    ],
    "hexagon_V6_vmaxw_128B+typed:vec-bwand": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmaxw_128B",
                "output_expression": "typed:vec-bwand",
                "synth_expression": "(repair-smax_dsl (repair-smax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmaxw_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmaxw_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-smax_dsl (typed:vec-bwnot (typed:vec-bwnot (reg (bv #x01 8)) 32 32) 32 32) (reg (bv #x00 8)) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmaxw_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmaxw_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-smax_dsl (reg (bv #x01 8)) (typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (lit (bv #x00000001 32)) (lit (bv #x00000001 32)) 32 32) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmaxw_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmaxw_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-smax_dsl (reg (bv #x00 8)) (typed:unsigned-vec-mod (reg (bv #x01 8)) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(repair-usat-sub_dsl (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) 16 16) (typed:cast-int (lit (bv #x00000000 32)) 32 1 1 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) (typed:cast-uint (reg (bv #x01 8)) 8 1 1 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (typed:signed-vec-div (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-usat-sub_dsl (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) 16 16) (typed:signed-vec-mod (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(typed:signed-vec-mul (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(repair-usat-sub_dsl (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (typed:unsigned-vec-shr (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(typed:unsigned-vec-mul (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(repair-usat-add_dsl (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (typed:signed-vec-shr (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:unsigned-vec-sat-add",
                "synth_expression": "(repair-usat-add_dsl (repair-umul_dsl (lit (bv #x0000 16)) (typed:unsigned-vec-sat-add (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16) (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(repair-usat-add_dsl (typed:unsigned-vec-sat-sub (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-umul_dsl (typed:signed-vec-widen-mul (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(repair-umul_dsl (typed:unsigned-vec-div (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:signed-vec-sat-add",
                "synth_expression": "(repair-usat-sub_dsl (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (repair-usat-sub_dsl (lit (bv #x0000 16)) (typed:signed-vec-sat-add (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-usat-sub_dsl (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (typed:unsigned-vec-mod (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(repair-usat-add_dsl (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (typed:signed-vec-sat-sub (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-usat-add_dsl (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) 16 16) (typed:vec-bwnot (typed:vec-bwnot (lit (bv #x0000 16)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpyub_128B+typed:vec-bwand": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpyub_128B",
                "output_expression": "typed:vec-bwand",
                "synth_expression": "(repair-umul_dsl (typed:vec-bwand (lit (bv #x0101 16)) (repair-umul_dsl (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16) (repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 8) (repair-cast-uint_dsl (reg (bv #x01 8)) 8 16 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vavguw_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vavguw_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (lit (bv #x00000001 32)) 32 32)"
            }
        }
    ],
    "hexagon_V6_vavguw_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vavguw_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(typed:unsigned-vec-div (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (repair-add_dsl (lit (bv #x00000001 32)) (lit (bv #x00000001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_lo_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lo_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lo_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lo_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lo_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lo_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_lo_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lo_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_lo_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lo_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:signed-vec-shr (lit (bv #x01 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lo_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lo_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lo_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lo_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lo_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lo_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (reg (bv #x00 8)) (typed:unsigned-vec-mod (reg (bv #x00 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lo_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lo_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (lit (bv #x01 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lo_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lo_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_lo_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_lo_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vassign_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vassign_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_vassign_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vassign_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_vassign_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vassign_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vassign_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vassign_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vassign_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vassign_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:signed-vec-shr (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vassign_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vassign_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vassign_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vassign_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (reg (bv #x00 8)) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vassign_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vassign_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vassign_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vassign_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vassign_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vassign_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vassign_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vassign_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (reg (bv #x00 8)) 16 1 1 32)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(repair-cast-int_dsl (typed:cast-uint (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) 32 1 1 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(repair-cast-int_dsl (repair-ssat-add_dsl (typed:signed-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) (reg (bv #x00 8)) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:signed-vec-sat-add",
                "synth_expression": "(typed:signed-vec-sat-add (lit (bv #x00010001 32)) (repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(typed:signed-vec-widen-mul (lit (bv #x0001 16)) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(repair-smul_dsl (typed:unsigned-vec-div (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(repair-cast-int_dsl (typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-cast-int_dsl (repair-ssat-sub_dsl (reg (bv #x00 8)) (typed:signed-vec-mod (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (reg (bv #x00 8)) 8 1 1 16) 16 1 1 8)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (reg (bv #x00 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (reg (bv #x00 8)) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(typed:signed-vec-shr (reg (bv #x00 8)) (typed:signed-vec-shr (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (reg (bv #x00 8)) (typed:unsigned-vec-mod (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vcombine_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vcombine_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 8 8) 8 8)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-cast-int_dsl (typed:vec-bwnot (typed:vec-bwnot (reg (bv #x00 8)) 16 16) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:vec-bwand": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:vec-bwand",
                "synth_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 16) (typed:vec-bwand (repair-ssat-add_dsl (lit (bv #x00010001 32)) (lit (bv #x00010001 32)) 32 32) (lit (bv #x00010001 32)) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(repair-cast-int_dsl (typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-cast-int_dsl (repair-cast-int_dsl (typed:unsigned-vec-widen-mul (lit (bv #x0001 16)) (reg (bv #x00 8)) 16 16) 32 16 32) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vunpackh_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vunpackh_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-cast-int_dsl (repair-ssat-add_dsl (typed:unsigned-vec-mod (reg (bv #x00 8)) (lit (bv #x0001 16)) 16 16) (reg (bv #x00 8)) 16 16) 16 32 16)"
            }
        }
    ],
    "hexagon_V6_vmpauhb_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpauhb_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-widen-mul (reg (bv #x00 8)) (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 16) 16 32) 32 64)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (reg (bv #x00 8)) 8 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vlsrwv_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vlsrwv_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(repair-smax_dsl (lit (bv #x00000000 32)) (typed:unsigned-vec-div (reg (bv #x01 8)) (repair-shl_dsl (lit (bv #x00000001 32)) (reg (bv #x00 8)) 32 32) 32 32) 32 32)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(typed:signed-vec-widen-mul (lit (bv #x01 8)) (reg (bv #x00 8)) 8 8)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-cast-int_dsl (repair-cast-int_dsl (typed:unsigned-vec-widen-mul (lit (bv #x01 8)) (reg (bv #x00 8)) 8 8) 16 8 16) 8 16 8)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (repair-cast-int_dsl (typed:vec-bwnot (reg (bv #x00 8)) 8 8) 8 16 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(repair-cast-int_dsl (typed:unsigned-vec-shr (reg (bv #x00 8)) (typed:unsigned-vec-shr (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8) 8 16 8)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(repair-ssat-add_dsl (typed:signed-vec-shr (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) (typed:unsigned-vec-mul (typed:unsigned-vec-mul (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) (lit (bv #x0000 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:vec-bwand": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:vec-bwand",
                "synth_expression": "(repair-ssat-add_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) (typed:vec-bwand (lit (bv #x0101 16)) (repair-ssat-add_dsl (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(repair-cast-int_dsl (repair-smul_dsl (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) 8 8) 8 16 8)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(typed:signed-vec-sat-sub (lit (bv #x0101 16)) (typed:signed-vec-sat-sub (lit (bv #x0101 16)) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:signed-vec-sat-add",
                "synth_expression": "(typed:signed-vec-sat-add (repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) (lit (bv #x0101 16)) 16 16) (lit (bv #x0101 16)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-cast-int_dsl (repair-ssat-sub_dsl (reg (bv #x00 8)) (typed:unsigned-vec-mod (lit (bv #x01 8)) (lit (bv #x01 8)) 8 8) 8 8) 8 16 8)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-cast-int_dsl (repair-ssat-add_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (lit (bv #x01 8)) 8 8) (reg (bv #x00 8)) 8 8) 8 16 8)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(repair-ssat-sub_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) (typed:unsigned-vec-sat-sub (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(repair-smul_dsl (typed:cast-int (reg (bv #x01 8)) 8 1 1 16) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(typed:signed-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(repair-ssat-add_dsl (typed:signed-vec-shr (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(typed:signed-vec-mul (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:signed-vec-div",
                "synth_expression": "(typed:signed-vec-div (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (typed:signed-vec-div (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(typed:unsigned-vec-mul (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(repair-ssat-add_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (typed:signed-vec-sat-sub (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(typed:unsigned-vec-div (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (typed:unsigned-vec-div (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:signed-vec-sat-add",
                "synth_expression": "(repair-ssat-sub_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (repair-smul_dsl (typed:signed-vec-sat-add (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) (lit (bv #x0000 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(repair-ssat-add_dsl (typed:unsigned-vec-shr (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-ssat-sub_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (typed:signed-vec-mod (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(repair-ssat-sub_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) 16 16) (typed:unsigned-vec-mod (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(repair-ssat-add_dsl (typed:unsigned-vec-sat-sub (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:unsigned-vec-sat-add",
                "synth_expression": "(repair-ssat-sub_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (repair-smul_dsl (typed:unsigned-vec-sat-add (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) (lit (bv #x0000 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:vec-bwand": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:vec-bwand",
                "synth_expression": "(repair-ssat-add_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (repair-cast-int_dsl (typed:vec-bwand (reg (bv #x00 8)) (lit (bv #x01 8)) 8 8) 8 16 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(repair-smul_dsl (typed:cast-uint (lit (bv #x01 8)) 8 1 1 16) (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-ssat-add_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16) (typed:unsigned-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x01 8)) 8 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-ssat-add_dsl (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) 16 16) (typed:vec-bwnot (typed:vec-bwnot (lit (bv #x0000 16)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vsb_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vsb_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(repair-ssat-add_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) (repair-smul_dsl (typed:signed-vec-mul (lit (bv #x0101 16)) (lit (bv #x0101 16)) 16 16) (lit (bv #x0000 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vmpybv_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vmpybv_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 8 16 8) (repair-cast-int_dsl (reg (bv #x00 8)) 8 16 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vasrhv_128B+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vasrhv_128B",
                "output_expression": "typed:unsigned-vec-widen-mul",
                "synth_expression": "(repair-sshr_dsl (repair-shl_dsl (repair-sshr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) (typed:unsigned-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x00 8)) 8 8) 16 16)"
            }
        }
    ],
    "hexagon_V6_vasrhv_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vasrhv_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(repair-sshr_dsl (repair-shl_dsl (reg (bv #x01 8)) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) (typed:cast-int (typed:cast-int (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vasrhv_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vasrhv_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-sshr_dsl (repair-shl_dsl (reg (bv #x01 8)) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) (repair-smax_dsl (reg (bv #x00 8)) (typed:signed-vec-widen-mul (lit (bv #x00 8)) (lit (bv #x01 8)) 8 8) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vasrhv_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vasrhv_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(repair-shl_dsl (repair-sshr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (repair-sshr_dsl (reg (bv #x00 8)) (typed:vec-bwnot (reg (bv #x00 8)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vasrhv_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vasrhv_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(repair-sshr_dsl (repair-shl_dsl (reg (bv #x01 8)) (repair-sshr_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) (typed:cast-uint (typed:cast-uint (reg (bv #x00 8)) 16 1 1 32) 32 1 1 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vdmpyhsat_acc_128B+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpyhsat_acc_128B",
                "output_expression": "typed:signed-vec-widen-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32) 32 64)"
            }
        }
    ],
    "hexagon_V6_vdmpyhsat_acc_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpyhsat_acc_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) (typed:cast-int (reg (bv #x00 8)) 16 1 2 32) 32 64) 32 64)"
            }
        }
    ],
    "hexagon_V6_vdmpyhsat_acc_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpyhsat_acc_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-mul (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 32) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 32 64) 32 64)"
            }
        }
    ],
    "hexagon_V6_vdmpyhsat_acc_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vdmpyhsat_acc_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(repair-vector-reduce-add_dsl 2 (typed:unsigned-vec-mul (repair-cast-int_dsl (reg (bv #x00 8)) 16 32 32) (repair-cast-int_dsl (reg (bv #x01 8)) 16 32 32) 32 64) 32 64)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:concat_vectors": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:concat_vectors",
                "synth_expression": "(repair-bwnot_dsl (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:cast-uint": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:cast-uint",
                "synth_expression": "(typed:cast-uint (typed:cast-uint (repair-bwnot_dsl (reg (bv #x00 8)) 16 16) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:cast-int": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:cast-int",
                "synth_expression": "(typed:cast-int (typed:cast-int (repair-bwnot_dsl (reg (bv #x00 8)) 16 16) 16 1 1 32) 32 1 1 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:signed-vec-shr",
                "synth_expression": "(repair-bwnot_dsl (typed:signed-vec-shr (reg (bv #x00 8)) (typed:signed-vec-shr (lit (bv #x0001 16)) (lit (bv #x0001 16)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:signed-vec-sat-sub",
                "synth_expression": "(typed:signed-vec-sat-sub (repair-bwnot_dsl (lit (bv #x0000 16)) 16 16) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:signed-vec-mod",
                "synth_expression": "(repair-bwnot_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (typed:signed-vec-mod (reg (bv #x00 8)) (lit (bv #x0001 16)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:signed-vec-sat-add",
                "synth_expression": "(typed:signed-vec-sat-add (repair-bwnot_dsl (reg (bv #x00 8)) 16 16) (typed:signed-vec-sat-add (repair-bwnot_dsl (lit (bv #x0000 16)) 16 16) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:unsigned-vec-mod",
                "synth_expression": "(typed:unsigned-vec-mod (repair-bwnot_dsl (reg (bv #x00 8)) 16 16) (typed:unsigned-vec-mod (reg (bv #x00 8)) (lit (bv #x0001 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:signed-vec-mul",
                "synth_expression": "(typed:signed-vec-mul (typed:signed-vec-mul (repair-bwnot_dsl (reg (bv #x00 8)) 16 16) (repair-bwnot_dsl (lit (bv #x0000 16)) 16 16) 16 16) (repair-bwnot_dsl (lit (bv #x0000 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:unsigned-vec-mul",
                "synth_expression": "(typed:unsigned-vec-mul (typed:unsigned-vec-mul (repair-bwnot_dsl (reg (bv #x00 8)) 16 16) (repair-bwnot_dsl (lit (bv #x0000 16)) 16 16) 16 16) (repair-bwnot_dsl (lit (bv #x0000 16)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:unsigned-vec-sat-sub",
                "synth_expression": "(typed:unsigned-vec-sat-sub (repair-bwnot_dsl (lit (bv #x0000 16)) 16 16) (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:unsigned-vec-shr",
                "synth_expression": "(typed:unsigned-vec-shr (repair-bwnot_dsl (reg (bv #x00 8)) 16 16) (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:xBroadcast": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:xBroadcast",
                "synth_expression": "(repair-bwnot_dsl (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:unsigned-vec-sat-add",
                "synth_expression": "(typed:unsigned-vec-sat-add (lit (bv #x0001 16)) (repair-bwnot_dsl (typed:unsigned-vec-sat-add (reg (bv #x00 8)) (lit (bv #x0001 16)) 16 16) 16 16) 16 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:vec-bwnot",
                "synth_expression": "(typed:vec-bwnot (reg (bv #x00 8)) 16 16)"
            }
        }
    ],
    "hexagon_V6_vnot_128B+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavance",
            "property": {
                "candidate": "hexagon_V6_vnot_128B",
                "output_expression": "typed:unsigned-vec-div",
                "synth_expression": "(repair-bwnot_dsl (typed:unsigned-vec-div (reg (bv #x00 8)) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 16) 16 16) 16 16)"
            }
        }
    ]
}
