{
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
    "_mm_mul_su32+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:cast-uint": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:cast-uint (reg (bv #x00 8)) 16 1 2 32)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:vec-shl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_cmplt_epi32_mask+typed:unsigned-vec-lt": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cmplt_epi32_mask",
                "output_expression": "(typed:unsigned-vec-lt (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm512_cmplt_epi32_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8 0 8 1 0 64 1 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:cast-int": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:cast-int (reg (bv #x00 8)) 8 1 4 16)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 1 0)"
            }
        }
    ],
    "_mm_add_si64+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:vec-add (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
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
    "_mm512_cmplt_epi32_mask+typed:signed-vec-le": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cmplt_epi32_mask",
                "output_expression": "(typed:signed-vec-le (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm512_cmplt_epi32_mask_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 8 1 1 64 1 0)"
            }
        }
    ],
    "_mm256_mul_epi32+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:cast-uint": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:cast-uint (reg (bv #x00 8)) 16 1 1 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm512_packs_epi32+typed:vec-saturate": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:vec-saturate (reg (bv #x00 8)) 16 1 2 8 #f)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 8 64 128 8 0 16 2 0 16 128 2 0)"
            }
        }
    ],
    "_mm512_sra_epi64+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sra_epi64",
                "output_expression": "(typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_sra_epi64_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #xffffffffffffffff 64)) (lit (bv #x000000000000003f 64)) 128 128 0 512 64 0 64 0 64 1 0 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:vec-shl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 512 512 0 512 32 0 32 32 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)"
            }
        }
    ],
    "_mm512_rem_epu32+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (repair-smod_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-smod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (repair-smod_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-smod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64) (repair-smod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (repair-smod_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 16 64) (repair-smod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (repair-smod_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (repair-smod_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-smod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64) (typed:signed-vec-mod (repair-smod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-smod_dsl (repair-smod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-smod_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-mod (repair-smod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-smod_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 32 64) 32 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-smod_dsl (repair-smod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 32 64) 64 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-mod (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (repair-smod_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64) (repair-smod_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (repair-smod_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 16 64) (typed:signed-vec-mod (repair-smod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-smod_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-smod_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 64) 16 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-smod_dsl (repair-smod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (repair-smod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64) 16 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-mod (repair-smod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-smod_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 16 64) 8 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-mod (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 16 64) 8 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:signed-vec-mod (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (repair-smod_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 16 64) 8 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_rem_epu32",
                "output_expression": "(repair-smod_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-mod (repair-smod_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64) 8 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        }
    ],
    "_mm512_cmplt_epi32_mask+typed:unsigned-vec-le": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cmplt_epi32_mask",
                "output_expression": "(typed:unsigned-vec-le (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm512_cmplt_epi32_mask_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 8 1 0 64 1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-sat-add (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 0 0)"
            }
        }
    ],
    "_mm_div_epi64+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_div_epi64",
                "output_expression": "(typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64)",
                "synth_expression": "(_mm_div_epi64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 8 0 0 16 0 16 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        }
    ],
    "_mm512_cmplt_epi32_mask+typed:signed-vec-lt": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cmplt_epi32_mask",
                "output_expression": "(typed:signed-vec-lt (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_cmplt_epi32_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 8 1 1 64 1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:vec-add (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        }
    ],
    "_mm512_srav_epi16+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srav_epi16",
                "output_expression": "(typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm512_srav_epi16_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (reg (bv #x00 8)) (lit (bv #xffffffffffffffff 64)) (lit (bv #b1 1)) (lit (bv #x0000000000000040 64)) 512 512 0 512 64 0 64 64 1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:vec-saturate": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:vec-saturate (reg (bv #x00 8)) 32 1 2 16 #t)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 1 32 1 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:slice_vectors (reg (bv #x00 8)) 0 1 4 8 64) (typed:slice_vectors (reg (bv #x00 8)) 4 1 4 8 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:cast-int": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(repair-saturate_dsl (typed:cast-int (reg (bv #x00 8)) 8 1 4 16) 32 8 64 #t)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 1 16 1 1 16 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:signed-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(repair-saturate_dsl (typed:signed-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32) 16 8 32 #f)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 0 16 1 0 16 64 2 0)"
            }
        }
    ],
    "_mm_add_si64+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:vec-sub (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm256_mul_epi32+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed:signed-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:cast-int": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:cast-int (repair-cast-uint_dsl (reg (bv #x00 8)) 16 64 16) 32 1 2 16)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        }
    ],
    "_mm256_mul_epi32+typed:cast-int": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (repair-cast-int_dsl (reg (bv #x01 8)) 32 64 32) (typed:cast-int (reg (bv #x00 8)) 32 1 1 64) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        }
    ],
    "_mm256_mul_epi32+typed:cast-uint": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed:cast-uint (reg (bv #x01 8)) 32 1 1 64) (typed:cast-uint (reg (bv #x00 8)) 32 1 1 64) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 0 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0)"
            }
        }
    ],
    "_mm_mul_su32+typed:cast-uint": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (typed:cast-uint (reg (bv #x00 8)) 32 1 1 64) (typed:cast-uint (reg (bv #x01 8)) 32 1 1 64) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 64 0 0 0 0)"
            }
        }
    ],
    "_mm_mul_su32+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed:signed-vec-mul (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 64 32) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)"
            }
        }
    ],
    "_mm_mul_su32+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed:unsigned-vec-mul (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 64 32) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:cast-uint": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 4 (typed:cast-uint (reg (bv #x01 8)) 32 1 2 64) 32 128)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:slice_vectors (reg (bv #x00 8)) 1 1 1 32 64) (typed:slice_vectors (reg (bv #x00 8)) 0 1 2 16 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:signed-vec-div (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:signed-vec-shr (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        }
    ],
    "_mm_hsub_pi32+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hsub_pi32",
                "output_expression": "(repair-sub_dsl (typed:slice_vectors (reg (bv #x01 8)) 1 1 1 32 64) (typed:slice_vectors (reg (bv #x01 8)) 0 1 4 8 64) 32 32)",
                "synth_expression": "(_mm_hsub_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 32 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        }
    ],
    "_mm256_mul_epi32+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed:unsigned-vec-mul (repair-cast-int_dsl (reg (bv #x01 8)) 32 64 32) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)"
            }
        }
    ],
    "_mm256_mul_epi32+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed:signed-vec-mul (repair-cast-int_dsl (reg (bv #x01 8)) 32 64 32) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)"
            }
        }
    ],
    "_mm512_cmplt_epi32_mask+typed:vec-eq": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cmplt_epi32_mask",
                "output_expression": "(typed:vec-eq (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm512_cmplt_epi32_mask_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8 0 8 1 1 64 1 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:signed-vec-shr (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 512 512 0 512 32 0 32 32 0)"
            }
        }
    ],
    "_mm_div_epi64+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_div_epi64",
                "output_expression": "(typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)",
                "synth_expression": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 8 1 1 16 1 16 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed:slice_vectors (reg (bv #x00 8)) 1 1 1 32 64) (typed:slice_vectors (reg (bv #x00 8)) 0 1 1 32 64) 32 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:vec-add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:signed-vec-div (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 512 512 0 512 32 0 32 32 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:vec-bwnot": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:vec-bwnot (reg (bv #x00 8)) 64 64) (typed:vec-bwnot (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-div (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_m_psrawi+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrawi",
                "output_expression": "(typed:signed-vec-shr (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 64 8) 64 64)",
                "synth_expression": "(_m_psrawi_dsl (reg (bv #x00 8)) (lit (bv #xffffffffffffffff 64)) (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #b1 1)) (lit (bv #x3f 8)) 8 8 0 32 8 0 8 0 64 1 1 1 0 8 0 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:signed-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:signed-vec-div (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_m_pslld+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:vec-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:vec-add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_mm512_andnot_epi32+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_andnot_epi32",
                "output_expression": "(typed:vec-bwand (repair-bwnot_dsl (reg (bv #x01 8)) 32 32) (reg (bv #x00 8)) 16 32)",
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
                "output_expression": "(typed:vec-sub (reg (bv #x00 8)) (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-div (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_m_pslld+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (reg (bv #x01 8)) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:signed-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:vec-saturate": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:vec-saturate (reg (bv #x00 8)) 64 1 1 32 #f) (typed:vec-saturate (reg (bv #x00 8)) 64 1 1 32 #f) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000009 64)) 8 32 8) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_mm512_andnot_epi32+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_andnot_epi32",
                "output_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32) 16 32)",
                "synth_expression": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_m_psrld+typed:signed-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_mm512_andnot_epi32+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_andnot_epi32",
                "output_expression": "(typed:unsigned-vec-absd (reg (bv #x00 8)) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32) 8 32)",
                "synth_expression": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_m_pslld+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000005 64)) 16 32 16) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:cast-uint": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 64 32 64) (typed:cast-uint (reg (bv #x00 8)) 64 1 1 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:unsigned-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_mm512_srli_epi16+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srli_epi16",
                "output_expression": "(typed:unsigned-vec-shr (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 64 8) 64 64)",
                "synth_expression": "(_mm512_srli_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x3f 8)) (reg (bv #x01 8)) 8 8 0 16 8 0 8 0 64 1 1 0 8 0 0)"
            }
        }
    ],
    "_m_psrld+typed:vec-saturate": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:vec-saturate (reg (bv #x00 8)) 32 1 2 16 #t) (typed:vec-saturate (reg (bv #x00 8)) 32 1 2 16 #t) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:vec-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:vec-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (reg (bv #x01 8)) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_mm256_hsub_epi32+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hsub_epi32",
                "output_expression": "(repair-sub_dsl (typed:slice_vectors (reg (bv #x00 8)) 4 1 4 8 64) (typed:slice_vectors (reg (bv #x00 8)) 0 1 1 32 64) 32 32)",
                "synth_expression": "(_mm256_hsub_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 96 128 2 0)"
            }
        }
    ],
    "_mm512_slli_epi16+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_slli_epi16",
                "output_expression": "(typed:vec-shl (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 64 8) 64 64)",
                "synth_expression": "(_mm512_slli_epi16_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x3f 8)) (reg (bv #x01 8)) 8 8 0 32 8 0 8 0 64 1 1 0 8 0 0)"
            }
        }
    ],
    "_mm_hsub_epi16+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hsub_epi16",
                "output_expression": "(repair-sub_dsl (typed:slice_vectors (reg (bv #x00 8)) 1 1 1 32 64) (typed:slice_vectors (reg (bv #x00 8)) 0 1 4 8 64) 32 32)",
                "synth_expression": "(_mm_hsub_epi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 32 2 -1 96 128 2 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:signed-vec-shr (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 256 256 0 256 64 0 64 64 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:signed-vec-div (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-rounding_shift_right (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-rounding_shift_right (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-div (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        }
    ],
    "_mm256_mul_epi32+typed:signed-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-cast-int_dsl (reg (bv #x01 8)) 32 64 32) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (typed:signed-vec-rounding_mul_shift_right (lit (bv #x0000000000000006 64)) (lit (bv #x000000000000000b 64)) (lit (bv #x0000000000000013 64)) 8 64) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)"
            }
        }
    ],
    "_mm_mul_su32+typed:unsigned-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-cast-uint_dsl (reg (bv #x01 8)) 32 64 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-usat-sub_dsl (lit (bv #x000000000000000c 64)) (lit (bv #x000000000000000f 64)) 16 64) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)"
            }
        }
    ]
}