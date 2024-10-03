{
    "_mm512_rem_epu32+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)"
            }
        }
    ],
    "_mm_add_si64+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_m_packssdw+typed:vec-saturate": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:vec-saturate (reg (bv #x00 8)) 16 1 2 8 #t)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 1 16 1 1 16 64 2 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)"
            }
        }
    ],
    "_mm256_mul_epi32+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)"
            }
        }
    ],
    "_mm256_mul_epi32+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 0 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 1 32 1 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 1 32 1 0)"
            }
        }
    ],
    "_mm_mul_su32+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 0 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:vec-add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 -1 0)"
            }
        }
    ],
    "_mm_div_epi64+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_div_epi64",
                "output_expression": "(typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64)",
                "synth_expression": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 0 32 0 32 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm512_packs_epi32+typed:vec-saturate": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:vec-saturate (reg (bv #x00 8)) 32 1 1 16 #t)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 16 64 128 16 1 32 2 1 32 128 2 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 16)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 16)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 0 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:vec-saturate": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:vec-saturate (reg (bv #x00 8)) 64 1 1 32 #t)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 1 64 1 0)"
            }
        }
    ],
    "_mm_add_si64+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8) 8 8)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 8) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8) 8 8)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8) 8 8)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8) (reg (bv #x00 8)) 8 8)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 8) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8) 8 8)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 8 -1 0)"
            }
        }
    ],
    "_mm512_cmplt_epi32_mask+typed:unsigned-vec-lt": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cmplt_epi32_mask",
                "output_expression": "(typed:unsigned-vec-lt (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (reg (bv #x00 8)) 32 32)",
                "synth_expression": "(_mm512_cmplt_epi32_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16 0 16 1 0 32 1 0)"
            }
        }
    ],
    "_mm512_packs_epi32+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #t) 8 16)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 16 64 128 16 1 32 2 1 32 128 2 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-uabsd_dsl (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 16) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 16 16) 16 16)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-max (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32) (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_andnot_epi32+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_andnot_epi32",
                "output_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32) 32 32)",
                "synth_expression": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_andnot_epi32+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_andnot_epi32",
                "output_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32) 8 32)",
                "synth_expression": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_andnot_epi32+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_andnot_epi32",
                "output_expression": "(typed:vec-sub (reg (bv #x01 8)) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32) 8 32)",
                "synth_expression": "(_mm512_andnot_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-min (repair-ssat-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8) (repair-ssat-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8) 8 8)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)"
            }
        }
    ],
    "_m_por+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_por",
                "output_expression": "(repair-bwor_dsl (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    "_m_por+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_por",
                "output_expression": "(repair-bwor_dsl (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    "_m_por+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_por",
                "output_expression": "(repair-bwor_dsl (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    "_m_por+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_por",
                "output_expression": "(repair-bwor_dsl (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x01 8)) 8 64)",
                "synth_expression": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    "_m_por+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_por",
                "output_expression": "(repair-bwor_dsl (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    "_m_por+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_por",
                "output_expression": "(repair-bwor_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    "_m_por+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_por",
                "output_expression": "(repair-bwor_dsl (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    "_m_por+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_por",
                "output_expression": "(repair-bwor_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    "_m_por+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_por",
                "output_expression": "(repair-bwor_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_m_por_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    "_m_por+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_por",
                "output_expression": "(repair-bwor_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 16 64)",
                "synth_expression": "(_m_por_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 0 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:signed-vec-min (repair-bwor_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32) (reg (bv #x01 8)) 32 32) (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32) 16 32)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-bwor_dsl (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32) (reg (bv #x01 8)) 16 32) (repair-bwor_dsl (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 32) (reg (bv #x01 8)) 32 32) 8 32)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0)"
            }
        }
    ]
}

