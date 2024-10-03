{
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
                "output_expression": "(typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64)",
                "synth_expression": "(_mm512_rem_epu32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
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
        },
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
                "output_expression": "(typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:cast-uint (reg (bv #x00 8)) 16 1 1 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srav_epi16",
                "output_expression": "(typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm512_srav_epi16_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (reg (bv #x00 8)) (lit (bv #xffffffffffffffff 64)) (lit (bv #b1 1)) (lit (bv #x0000000000000040 64)) 512 512 0 512 64 0 64 64 1 0)"
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
        },
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
                "output_expression": "(typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed:unsigned-vec-widen-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 0 0 0)"
            }
        }
    ],
    "_mm256_mask_testn_epi32_mask+typed:signed-vec-le": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_testn_epi32_mask",
                "output_expression": "(typed:signed-vec-le (lit (bv #x0013 16)) (lit (bv #x0012 16)) 8 8)",
                "synth_expression": "(_mm256_mask_testn_epi32_mask_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (lit (bv #x00 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_testn_epi32_mask",
                "output_expression": "(typed:signed-vec-le (lit (bv #x0009 16)) (repair-bwand_dsl (lit (bv #x0008 16)) (lit (bv #x0007 16)) 16 16) 16 16)",
                "synth_expression": "(_mm256_mask_testn_epi32_mask_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (lit (bv #x00 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_testn_epi32_mask",
                "output_expression": "(typed:signed-vec-le (repair-bwand_dsl (lit (bv #x000f 16)) (lit (bv #x000c 16)) 8 8) (repair-bwand_dsl (lit (bv #x000f 16)) (lit (bv #x0007 16)) 8 8) 8 8)",
                "synth_expression": "(_mm256_mask_testn_epi32_mask_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (lit (bv #x00 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 64 1 4)"
            }
        }
    ],
    "_mm256_mask_testn_epi32_mask+typed:signed-vec-lt": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_testn_epi32_mask",
                "output_expression": "(typed:signed-vec-lt (lit (bv #x0010 16)) (lit (bv #x0009 16)) 8 8)",
                "synth_expression": "(_mm256_mask_testn_epi32_mask_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (lit (bv #x00 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_testn_epi32_mask",
                "output_expression": "(typed:signed-vec-lt (lit (bv #x0007 16)) (lit (bv #x0006 16)) 8 8)",
                "synth_expression": "(_mm256_mask_testn_epi32_mask_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (lit (bv #x00 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 64 1 4)"
            }
        }
    ],
    "_mm256_mask_testn_epi32_mask+typed:unsigned-vec-le": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_testn_epi32_mask",
                "output_expression": "(typed:unsigned-vec-le (lit (bv #x0012 16)) (lit (bv #x000a 16)) 8 8)",
                "synth_expression": "(_mm256_mask_testn_epi32_mask_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (lit (bv #x00 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_testn_epi32_mask",
                "output_expression": "(typed:unsigned-vec-le (lit (bv #x0014 16)) (lit (bv #x000b 16)) 16 16)",
                "synth_expression": "(_mm256_mask_testn_epi32_mask_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (lit (bv #x00 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 64 1 4)"
            }
        }
    ],
    "_mm256_mask_testn_epi32_mask+typed:unsigned-vec-lt": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_testn_epi32_mask",
                "output_expression": "(typed:unsigned-vec-lt (lit (bv #x0015 16)) (lit (bv #x0013 16)) 8 8)",
                "synth_expression": "(_mm256_mask_testn_epi32_mask_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (lit (bv #x00 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_testn_epi32_mask",
                "output_expression": "(typed:unsigned-vec-lt (lit (bv #x0011 16)) (lit (bv #x0010 16)) 8 8)",
                "synth_expression": "(_mm256_mask_testn_epi32_mask_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (lit (bv #x00 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 64 1 4)"
            }
        }
    ],
    "_mm256_mask_testn_epi32_mask+typed:vec-eq": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_testn_epi32_mask",
                "output_expression": "(typed:vec-eq (lit (bv #x0007 16)) (lit (bv #x000b 16)) 8 8)",
                "synth_expression": "(_mm256_mask_testn_epi32_mask_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (lit (bv #x00 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_testn_epi32_mask",
                "output_expression": "(typed:vec-eq (lit (bv #x0011 16)) (lit (bv #x0012 16)) 8 8)",
                "synth_expression": "(_mm256_mask_testn_epi32_mask_dsl (lit (bv #b1 1)) (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (lit (bv #x00 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 64 1 4)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed:unsigned-vec-widen-mul (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 64 0 0 0 0)"
            }
        }
    ],
    "_mm256_mask_cmpeq_epu8_mask+typed:signed-vec-lt": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpeq_epu8_mask",
                "output_expression": "(typed:signed-vec-lt (lit (bv #x000a 16)) (lit (bv #x0006 16)) 16 16)",
                "synth_expression": "(_mm256_mask_cmpeq_epu8_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) 8 8 0 4 1 1 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpeq_epu8_mask",
                "output_expression": "(typed:signed-vec-lt (lit (bv #x0013 16)) (lit (bv #x000a 16)) 8 8)",
                "synth_expression": "(_mm256_mask_cmpeq_epu8_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) 8 8 0 4 1 1 64 1 4)"
            }
        }
    ],
    "_mm256_mask_cmpeq_epu8_mask+typed:unsigned-vec-le": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpeq_epu8_mask",
                "output_expression": "(typed:unsigned-vec-le (lit (bv #x0014 16)) (lit (bv #x0010 16)) 16 16)",
                "synth_expression": "(_mm256_mask_cmpeq_epu8_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) 8 8 0 4 1 1 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpeq_epu8_mask",
                "output_expression": "(typed:unsigned-vec-le (lit (bv #x0014 16)) (lit (bv #x000a 16)) 8 8)",
                "synth_expression": "(_mm256_mask_cmpeq_epu8_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) 8 8 0 4 1 1 64 1 4)"
            }
        }
    ],
    "_mm256_mask_cmpeq_epu8_mask+typed:unsigned-vec-lt": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpeq_epu8_mask",
                "output_expression": "(typed:unsigned-vec-lt (lit (bv #x0015 16)) (lit (bv #x0010 16)) 16 16)",
                "synth_expression": "(_mm256_mask_cmpeq_epu8_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) 8 8 0 4 1 1 64 1 4)"
            }
        }
    ],
    "_mm256_mask_cmpeq_epu8_mask+typed:vec-eq": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpeq_epu8_mask",
                "output_expression": "(typed:vec-eq (lit (bv #x0005 16)) (lit (bv #x0011 16)) 8 8)",
                "synth_expression": "(_mm256_mask_cmpeq_epu8_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) 8 8 0 4 1 1 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpeq_epu8_mask",
                "output_expression": "(typed:vec-eq (lit (bv #x0008 16)) (lit (bv #x000b 16)) 8 8)",
                "synth_expression": "(_mm256_mask_cmpeq_epu8_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) 8 8 0 4 1 1 64 1 4)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:vec-shl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sra_epi64",
                "output_expression": "(typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_sra_epi64_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #xffffffffffffffff 64)) (lit (bv #x000000000000003f 64)) 128 128 0 512 64 0 64 0 64 1 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_div_epi64",
                "output_expression": "(typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm_div_epi64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 64 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cmplt_epi32_mask",
                "output_expression": "(typed:signed-vec-le (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm512_cmplt_epi32_mask_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 8 1 1 64 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cmplt_epi32_mask",
                "output_expression": "(typed:signed-vec-lt (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_cmplt_epi32_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 8 1 1 64 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cmplt_epi32_mask",
                "output_expression": "(typed:unsigned-vec-le (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_cmplt_epi32_mask_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8 0 8 1 0 64 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cmplt_epi32_mask",
                "output_expression": "(typed:unsigned-vec-lt (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_cmplt_epi32_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 8 1 0 64 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:vec-shl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 512 512 0 512 32 0 32 32 0)"
            }
        }
    ],
    "_mm256_cmpeq_epu64_mask+typed:signed-vec-le": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_cmpeq_epu64_mask",
                "output_expression": "(typed:signed-vec-le (lit (bv #x0014 16)) (lit (bv #x000c 16)) 8 8)",
                "synth_expression": "(_mm256_cmpeq_epu64_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8 0 4 1 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_cmpeq_epu64_mask",
                "output_expression": "(typed:signed-vec-le (lit (bv #x0012 16)) (lit (bv #x000c 16)) 16 16)",
                "synth_expression": "(_mm256_cmpeq_epu64_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 4 1 64 1 4)"
            }
        }
    ],
    "_mm256_cmpeq_epu64_mask+typed:signed-vec-lt": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_cmpeq_epu64_mask",
                "output_expression": "(typed:signed-vec-lt (lit (bv #x0011 16)) (lit (bv #x000c 16)) 16 16)",
                "synth_expression": "(_mm256_cmpeq_epu64_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 4 1 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_cmpeq_epu64_mask",
                "output_expression": "(typed:signed-vec-lt (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm256_cmpeq_epu64_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 4 1 64 1 4)"
            }
        }
    ],
    "_mm256_cmpeq_epu64_mask+typed:unsigned-vec-lt": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_cmpeq_epu64_mask",
                "output_expression": "(typed:unsigned-vec-lt (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm256_cmpeq_epu64_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 4 1 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_cmpeq_epu64_mask",
                "output_expression": "(typed:unsigned-vec-lt (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm256_cmpeq_epu64_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 4 1 64 1 4)"
            }
        }
    ],
    "_mm256_cmpeq_epu64_mask+typed:unsigned-vec-le": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_cmpeq_epu64_mask",
                "output_expression": "(typed:unsigned-vec-le (lit (bv #x000c 16)) (lit (bv #x000a 16)) 16 16)",
                "synth_expression": "(_mm256_cmpeq_epu64_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 4 1 64 1 4)"
            }
        }
    ],
    "_mm256_cmpeq_epu64_mask+typed:vec-eq": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_cmpeq_epu64_mask",
                "output_expression": "(typed:vec-eq (lit (bv #x0013 16)) (lit (bv #x0005 16)) 8 8)",
                "synth_expression": "(_mm256_cmpeq_epu64_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8 0 4 1 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_cmpeq_epu64_mask",
                "output_expression": "(typed:vec-eq (lit (bv #x0011 16)) (lit (bv #x000f 16)) 8 8)",
                "synth_expression": "(_mm256_cmpeq_epu64_mask_dsl (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8 0 4 1 64 1 4)"
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
        },
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
                "output_expression": "(typed:vec-saturate (reg (bv #x00 8)) 16 1 2 8 #f)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 8 64 128 8 0 16 2 0 16 128 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:vec-saturate (reg (bv #x00 8)) 16 1 2 8 #t)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 8 64 128 8 1 16 2 1 16 128 2 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        }
    ],
    "_mm256_maskz_cvtepi16_epi8+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_maskz_cvtepi16_epi8",
                "output_expression": "(typed:slice_vectors (lit (bv #x0000000000000015 64)) 2 1 2 16 64)",
                "synth_expression": "(_mm256_maskz_cvtepi16_epi8_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 64 32 1 32 64 1 64)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_maskz_cvtepi16_epi8",
                "output_expression": "(typed:slice_vectors (lit (bv #x000000000000000f 64)) 2 1 2 16 64)",
                "synth_expression": "(_mm256_maskz_cvtepi16_epi8_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) 128 128 0 64 32 1 32 64 1 64)"
            }
        }
    ],
    "_mm_test_epi64_mask+typed:signed-vec-lt": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_test_epi64_mask",
                "output_expression": "(typed:signed-vec-lt (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm_test_epi64_mask_dsl (lit (bv #x0000000000000000 64)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) 8 8 0 2 1 64 1 6)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_test_epi64_mask",
                "output_expression": "(typed:signed-vec-lt (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm_test_epi64_mask_dsl (lit (bv #x00000000 32)) (reg (bv #x00 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) 8 8 0 4 1 32 1 4)"
            }
        }
    ],
    "_mm_test_epi64_mask+typed:signed-vec-le": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_test_epi64_mask",
                "output_expression": "(typed:signed-vec-le (lit (bv #x000e 16)) (lit (bv #x000c 16)) 16 16)",
                "synth_expression": "(_mm_test_epi64_mask_dsl (lit (bv #x0000000000000000 64)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) 8 8 0 2 1 64 1 6)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_test_epi64_mask",
                "output_expression": "(typed:signed-vec-le (lit (bv #x0005 16)) (repair-bwand_dsl (lit (bv #x0014 16)) (lit (bv #x000f 16)) 8 16) 16 16)",
                "synth_expression": "(_mm_test_epi64_mask_dsl (lit (bv #x0000000000000000 64)) (reg (bv #x01 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x00 8)) 8 8 0 2 1 64 1 6)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_test_epi64_mask",
                "output_expression": "(typed:signed-vec-le (repair-bwand_dsl (lit (bv #x0014 16)) (lit (bv #x0011 16)) 16 16) (lit (bv #x000d 16)) 16 16)",
                "synth_expression": "(_mm_test_epi64_mask_dsl (lit (bv #x0000000000000000 64)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) 8 8 0 2 1 64 1 6)"
            }
        }
    ],
    "_mm_test_epi64_mask+typed:unsigned-vec-le": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_test_epi64_mask",
                "output_expression": "(typed:unsigned-vec-le (lit (bv #x0010 16)) (lit (bv #x0007 16)) 16 16)",
                "synth_expression": "(_mm_test_epi64_mask_dsl (lit (bv #x00000000 32)) (reg (bv #x00 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) 8 8 0 4 1 32 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_test_epi64_mask",
                "output_expression": "(typed:unsigned-vec-le (lit (bv #x0015 16)) (lit (bv #x0008 16)) 8 8)",
                "synth_expression": "(_mm_test_epi64_mask_dsl (lit (bv #x00000000 32)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) 8 8 0 4 1 32 1 4)"
            }
        }
    ],
    "_mm_test_epi64_mask+typed:unsigned-vec-lt": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_test_epi64_mask",
                "output_expression": "(typed:unsigned-vec-lt (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm_test_epi64_mask_dsl (lit (bv #x0000000000000000 64)) (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (reg (bv #x01 8)) 8 8 0 2 1 64 1 6)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_test_epi64_mask",
                "output_expression": "(typed:unsigned-vec-lt (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm_test_epi64_mask_dsl (lit (bv #x0000000000000000 64)) (reg (bv #x00 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) 8 8 0 2 1 64 1 6)"
            }
        }
    ],
    "_mm_test_epi64_mask+typed:vec-eq": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_test_epi64_mask",
                "output_expression": "(typed:vec-eq (lit (bv #x0013 16)) (lit (bv #x000e 16)) 8 8)",
                "synth_expression": "(_mm_test_epi64_mask_dsl (lit (bv #x00000000 32)) (reg (bv #x00 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) 8 8 0 4 1 32 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_test_epi64_mask",
                "output_expression": "(typed:vec-eq (lit (bv #x0014 16)) (lit (bv #x0010 16)) 8 8)",
                "synth_expression": "(_mm_test_epi64_mask_dsl (lit (bv #x00000000 32)) (reg (bv #x00 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) 8 8 0 4 1 32 1 4)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:cast-int (reg (bv #x00 8)) 32 1 1 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:cast-uint (reg (bv #x00 8)) 8 1 4 16)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 0 0)"
            }
        }
    ],
    "_mm256_mask_cmpgt_epu64_mask+typed:signed-vec-lt": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpgt_epu64_mask",
                "output_expression": "(typed:signed-vec-lt (lit (bv #x000f 16)) (lit (bv #x0008 16)) 16 16)",
                "synth_expression": "(_mm256_mask_cmpgt_epu64_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 0 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpgt_epu64_mask",
                "output_expression": "(typed:signed-vec-lt (lit (bv #x000f 16)) (lit (bv #x000e 16)) 8 8)",
                "synth_expression": "(_mm256_mask_cmpgt_epu64_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 0 64 1 4)"
            }
        }
    ],
    "_mm256_mask_cmpgt_epu64_mask+typed:signed-vec-le": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpgt_epu64_mask",
                "output_expression": "(typed:signed-vec-le (lit (bv #x0013 16)) (lit (bv #x0009 16)) 8 8)",
                "synth_expression": "(_mm256_mask_cmpgt_epu64_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 0 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpgt_epu64_mask",
                "output_expression": "(typed:signed-vec-le (lit (bv #x000f 16)) (lit (bv #x0005 16)) 8 8)",
                "synth_expression": "(_mm256_mask_cmpgt_epu64_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 0 64 1 4)"
            }
        }
    ],
    "_mm256_mask_cmpgt_epu64_mask+typed:unsigned-vec-lt": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpgt_epu64_mask",
                "output_expression": "(typed:unsigned-vec-lt (lit (bv #x000e 16)) (lit (bv #x000c 16)) 8 8)",
                "synth_expression": "(_mm256_mask_cmpgt_epu64_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) (reg (bv #x02 8)) (reg (bv #x01 8)) 8 8 0 4 1 1 0 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpgt_epu64_mask",
                "output_expression": "(typed:unsigned-vec-lt (lit (bv #x000f 16)) (lit (bv #x0009 16)) 16 16)",
                "synth_expression": "(_mm256_mask_cmpgt_epu64_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 0 64 1 4)"
            }
        }
    ],
    "_mm256_mask_cmpgt_epu64_mask+typed:unsigned-vec-le": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpgt_epu64_mask",
                "output_expression": "(typed:unsigned-vec-le (lit (bv #x0015 16)) (lit (bv #x0010 16)) 8 8)",
                "synth_expression": "(_mm256_mask_cmpgt_epu64_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 0 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpgt_epu64_mask",
                "output_expression": "(typed:unsigned-vec-le (lit (bv #x0014 16)) (lit (bv #x0008 16)) 16 16)",
                "synth_expression": "(_mm256_mask_cmpgt_epu64_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 1 64 1 4)"
            }
        }
    ],
    "_mm256_mask_cmpgt_epu64_mask+typed:vec-eq": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpgt_epu64_mask",
                "output_expression": "(typed:vec-eq (lit (bv #x0014 16)) (lit (bv #x000e 16)) 8 8)",
                "synth_expression": "(_mm256_mask_cmpgt_epu64_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 0 64 1 4)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpgt_epu64_mask",
                "output_expression": "(typed:vec-eq (lit (bv #x0009 16)) (lit (bv #x000d 16)) 16 16)",
                "synth_expression": "(_mm256_mask_cmpgt_epu64_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) (reg (bv #x01 8)) (reg (bv #x02 8)) 8 8 0 4 1 1 1 64 1 4)"
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
        },
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
                "output_expression": "(typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:vec-saturate (reg (bv #x00 8)) 16 1 4 8 #t)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 1 16 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 256 256 0 256 64 0 64 64 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:signed-vec-halving_add (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:signed-vec-halving_add (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:signed-vec-max (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:signed-vec-max (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:signed-vec-min (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:signed-vec-min (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:signed-vec-mod (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:signed-vec-mod (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-absd (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-absd (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-max (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-max (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-max (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-max (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-max (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-shr (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-shr (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-mod (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:unsigned-vec-mod (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:vec-bwand (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-bwor_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:vec-bwand (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_or_epi32+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:vec-sub (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:vec-sub (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_mm_add_si64+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:signed-vec-min (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:signed-vec-max (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:signed-vec-max (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:signed-vec-halving_add (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:signed-vec-halving_add (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:signed-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:signed-vec-mod (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:signed-vec-sat-sub (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:unsigned-vec-absd (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:slice_vectors (lit (bv #x00000000000000000000000000000010 128)) 8 1 8 8 128) 32 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:slice_vectors (lit (bv #x00000000000000000000000000000013 128)) 4 1 4 16 128) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:unsigned-vec-max (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:unsigned-vec-min (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:unsigned-vec-mod (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:unsigned-vec-shr (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:vec-bwand (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_add_si64+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(typed:vec-sub (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(repair-saturate_dsl (typed:cast-int (reg (bv #x00 8)) 32 1 1 64) 64 16 64 #t)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 16 32 64 16 1 32 1 1 32 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:signed-vec-halving_add (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #t) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 16 32 64 16 1 32 1 1 32 64 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:signed-vec-halving_add (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) 8 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 0 16 1 0 16 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:signed-vec-min (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #t) 8 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 16 32 64 16 1 32 1 1 32 64 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:signed-vec-min (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 0 16 1 0 16 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:signed-vec-max (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 1 16 1 1 16 64 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:signed-vec-max (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) 16 16)",
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(repair-saturate_dsl (typed:signed-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32) 16 8 32 #f)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 0 16 1 0 16 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-absd (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (typed:unsigned-vec-absd (lit (bv #x0008 16)) (lit (bv #x0008 16)) 8 16) 8 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 1 16 1 1 16 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-div (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) (typed:unsigned-vec-div (lit (bv #x000b 16)) (lit (bv #x0006 16)) 16 16) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 0 16 1 0 16 64 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-div (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (typed:unsigned-vec-div (lit (bv #x0013 16)) (lit (bv #x0010 16)) 16 16) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 1 16 1 1 16 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) 8 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 0 16 1 0 16 64 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 1 16 1 1 16 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-min (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 0 16 1 0 16 64 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-min (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 1 16 1 1 16 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-max (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) 8 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 0 16 1 0 16 64 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-max (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 0 16 1 0 16 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-mod (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (typed:unsigned-vec-mod (lit (bv #x0012 16)) (lit (bv #x0009 16)) 8 16) 8 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 1 16 1 1 16 64 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-mod (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (typed:unsigned-vec-mod (lit (bv #x0014 16)) (lit (bv #x000a 16)) 16 16) 8 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 1 16 1 1 16 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 1 16 1 1 16 64 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 1 16 1 1 16 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:vec-bwand (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 0 16 1 0 16 64 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:vec-bwand (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 0 16 1 0 16 64 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:signed-vec-halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:signed-vec-halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:signed-vec-max (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:signed-vec-max (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:signed-vec-min (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:signed-vec-min (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:signed-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:signed-vec-rounding_mul_shift_right (lit (bv #x00000006 32)) (lit (bv #x00000005 32)) (lit (bv #x00000013 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:signed-vec-rounding_mul_shift_right (lit (bv #x00000011 32)) (lit (bv #x00000006 32)) (lit (bv #x00000011 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (lit (bv #x00000010 32)) (typed:signed-vec-rounding_mul_shift_right (lit (bv #x00000011 32)) (lit (bv #x00000007 32)) (lit (bv #x00000005 32)) 16 32) 32 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:slice_vectors (reg (bv #x00 8)) 1 1 1 32 64) (typed:slice_vectors (reg (bv #x00 8)) 0 1 2 16 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:unsigned-vec-absd (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-absd (lit (bv #x00000007 32)) (lit (bv #x00000007 32)) 32 32) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-div (lit (bv #x00000010 32)) (lit (bv #x00000013 32)) 32 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-div (lit (bv #x00000006 32)) (lit (bv #x00000012 32)) 32 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:unsigned-vec-max (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:unsigned-vec-max (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:unsigned-vec-min (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:unsigned-vec-min (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-mod (lit (bv #x0000000f 32)) (lit (bv #x0000000f 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-mod (lit (bv #x0000000e 32)) (lit (bv #x00000007 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:unsigned-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x00000005 32)) (lit (bv #x00000010 32)) (lit (bv #x00000012 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x00000011 32)) (lit (bv #x00000015 32)) (lit (bv #x00000012 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-sat-sub (lit (bv #x00000005 32)) (lit (bv #x00000010 32)) 16 32) 16 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-sat-sub (lit (bv #x00000008 32)) (lit (bv #x00000013 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-sat-sub (lit (bv #x00000011 32)) (lit (bv #x00000013 32)) 8 32) 32 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:vec-bwand (lit (bv #x0000000b 32)) (lit (bv #x00000014 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:vec-bwand (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:vec-shl (lit (bv #x00000005 32)) (lit (bv #x0000000e 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 16 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:vec-shl (lit (bv #x0000000f 32)) (lit (bv #x00000012 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(typed:vec-shl (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (typed:vec-shl (lit (bv #x00000015 32)) (lit (bv #x0000000f 32)) 8 32) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-halving_add (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:signed-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-halving_add (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x01 8)) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (typed:signed-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (reg (bv #x00 8)) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-min (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-mod (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-mod (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:signed-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-sat-add (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-sat-add (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-sat-add (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-sat-sub (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-sat-sub (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-shr (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:signed-vec-shr (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-absd (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-absd (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-absd (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:slice_vectors (lit (bv #x00000000000000000000000000000007 128)) 4 1 4 16 128) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:slice_vectors (lit (bv #x00000000000000000000000000000006 128)) 2 1 2 32 128) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:slice_vectors (lit (bv #x0000000000000000000000000000000e 128)) 4 1 4 16 128) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x00 8)) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-min (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-mod (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-mod (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (reg (bv #x00 8)) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-shr (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:unsigned-vec-shr (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:vec-add (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:vec-add (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:vec-add (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:vec-bwand (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-uabsd_dsl (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(repair-umax_dsl (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:vec-sub (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:vec-sub (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 0 0)"
            }
        }
    ],
    "_mm256_max_epu64+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:vec-shl (repair-umax_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_max_epu64",
                "output_expression": "(typed:vec-shl (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm256_max_epu64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-umul_dsl (repair-usat-sub_dsl (lit (bv #x00000007 32)) (lit (bv #x00000006 32)) 8 32) (typed:cast-int (reg (bv #x00 8)) 16 1 1 32) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:cast-int (repair-cast-uint_dsl (reg (bv #x00 8)) 16 64 16) 64 1 1 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:signed-vec-div (lit (bv #x00000009 32)) (lit (bv #x00000010 32)) 16 32) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-umul_dsl (typed:signed-vec-div (lit (bv #x00000015 32)) (lit (bv #x0000000e 32)) 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:signed-vec-div (lit (bv #x00000005 32)) (lit (bv #x00000012 32)) 32 32) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-div (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:signed-vec-div (lit (bv #x0000000c 32)) (lit (bv #x00000007 32)) 16 32) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-halving_add (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-halving_add (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-max (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-max (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-min (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-min (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-mod (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-usat-sub_dsl (lit (bv #x00000010 32)) (lit (bv #x00000012 32)) 16 32) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-umul_dsl (typed:signed-vec-mod (lit (bv #x00000011 32)) (lit (bv #x00000010 32)) 8 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:signed-vec-mod (lit (bv #x0000000b 32)) (lit (bv #x0000000b 32)) 16 32) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-mod (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:signed-vec-mod (lit (bv #x0000000d 32)) (lit (bv #x0000000d 32)) 8 32) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:signed-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-rounding_halving_add (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-rounding_halving_add (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:signed-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-umul_dsl (typed:signed-vec-rounding_mul_shift_right (lit (bv #x0000000a 32)) (lit (bv #x0000000d 32)) (lit (bv #x00000007 32)) 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:signed-vec-rounding_mul_shift_right (lit (bv #x00000009 32)) (lit (bv #x00000009 32)) (lit (bv #x0000000c 32)) 32 32) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-umul_dsl (lit (bv #x00000010 32)) (lit (bv #x00000014 32)) 16 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-usat-sub_dsl (lit (bv #x0000000b 32)) (lit (bv #x00000005 32)) 8 32) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (typed:signed-vec-rounding_mul_shift_right (lit (bv #x00000007 32)) (lit (bv #x00000006 32)) (lit (bv #x00000005 32)) 16 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:signed-vec-rounding_mul_shift_right (lit (bv #x0000000b 32)) (lit (bv #x00000014 32)) (lit (bv #x00000013 32)) 8 32) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:signed-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-usat-sub_dsl (lit (bv #x00000007 32)) (lit (bv #x0000000a 32)) 16 32) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-sat-add (repair-usat-sub_dsl (lit (bv #x0000000d 32)) (lit (bv #x00000012 32)) 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-sat-add (repair-usat-sub_dsl (lit (bv #x00000006 32)) (lit (bv #x00000008 32)) 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (typed:signed-vec-sat-sub (lit (bv #x00000005 32)) (lit (bv #x00000005 32)) 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-shr (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-usat-sub_dsl (lit (bv #x0000000a 32)) (lit (bv #x00000012 32)) 32 32) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:signed-vec-shr (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-usat-sub_dsl (lit (bv #x00000009 32)) (lit (bv #x0000000f 32)) 32 32) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:slice_vectors (lit (bv #x0000000000000007 64)) 1 1 1 32 64) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:slice_vectors (lit (bv #x0000000000000010 64)) 2 1 2 16 64) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (typed:slice_vectors (lit (bv #x000000000000000d 64)) 1 1 1 32 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:slice_vectors (lit (bv #x0000000000000007 64)) 4 1 4 8 64) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-absd (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-usat-sub_dsl (lit (bv #x00000009 32)) (lit (bv #x00000015 32)) 8 32) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (typed:unsigned-vec-absd (lit (bv #x00000009 32)) (lit (bv #x00000009 32)) 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-absd (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-usat-sub_dsl (lit (bv #x0000000c 32)) (lit (bv #x0000000d 32)) 16 32) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-umul_dsl (typed:unsigned-vec-div (lit (bv #x0000000b 32)) (lit (bv #x0000000a 32)) 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-umul_dsl (typed:unsigned-vec-div (lit (bv #x0000000b 32)) (lit (bv #x00000009 32)) 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (typed:unsigned-vec-div (lit (bv #x0000000f 32)) (lit (bv #x00000014 32)) 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-div (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:unsigned-vec-div (lit (bv #x0000000d 32)) (lit (bv #x00000007 32)) 16 32) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-max (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-max (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-min (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-min (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-mod (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-usat-sub_dsl (lit (bv #x00000005 32)) (lit (bv #x0000000d 32)) 16 32) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-mod (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-usat-sub_dsl (lit (bv #x00000007 32)) (lit (bv #x0000000f 32)) 8 32) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:unsigned-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x0000000b 32)) (lit (bv #x00000010 32)) (lit (bv #x0000000b 32)) 16 32) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x0000000c 32)) (lit (bv #x0000000a 32)) (lit (bv #x00000010 32)) 8 32) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x00000013 32)) (lit (bv #x00000010 32)) (lit (bv #x00000007 32)) 16 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x0000000b 32)) (lit (bv #x00000008 32)) (lit (bv #x00000006 32)) 16 32) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-usat-sub_dsl (lit (bv #x0000000b 32)) (lit (bv #x00000011 32)) 16 32) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-usat-sub_dsl (lit (bv #x0000000e 32)) (lit (bv #x00000011 32)) 16 32) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-usat-sub_dsl (lit (bv #x00000005 32)) (lit (bv #x00000008 32)) 16 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-usat-sub_dsl (lit (bv #x0000000a 32)) (lit (bv #x0000000b 32)) 16 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (typed:unsigned-vec-sat-sub (lit (bv #x0000000b 32)) (lit (bv #x00000012 32)) 16 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (typed:unsigned-vec-sat-sub (lit (bv #x00000006 32)) (lit (bv #x0000000a 32)) 16 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:unsigned-vec-sat-sub (lit (bv #x00000011 32)) (lit (bv #x00000012 32)) 16 32) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:unsigned-vec-sat-sub (lit (bv #x00000009 32)) (lit (bv #x0000000a 32)) 16 32) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-usat-sub_dsl (lit (bv #x00000012 32)) (lit (bv #x00000013 32)) 16 32) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:vec-add (repair-usat-sub_dsl (lit (bv #x00000005 32)) (lit (bv #x00000011 32)) 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:vec-add (repair-usat-sub_dsl (lit (bv #x0000000d 32)) (lit (bv #x00000010 32)) 8 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-umul_dsl (typed:vec-bwand (lit (bv #x00000011 32)) (lit (bv #x0000000b 32)) 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:vec-bwand (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (typed:vec-shl (lit (bv #x0000000a 32)) (lit (bv #x00000008 32)) 8 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:vec-shl (lit (bv #x00000007 32)) (lit (bv #x00000009 32)) 8 32) 8 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(repair-usat-add_dsl (typed:vec-shl (lit (bv #x0000000f 32)) (lit (bv #x00000010 32)) 8 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:vec-shl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (typed:vec-shl (lit (bv #x00000014 32)) (lit (bv #x00000011 32)) 32 32) 16 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
            }
        }
    ],
    "_mm_broadcastmb_epi64+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_broadcastmb_epi64",
                "output_expression": "(typed:vec-sub (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 16) (repair-usat-sub_dsl (lit (bv #x0000000f 32)) (lit (bv #x00000015 32)) 16 32) 32 32)",
                "synth_expression": "(_mm_broadcastmb_epi64_dsl (reg (bv #x00 8)) 16 16 0 64 16 32 1 0 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed:cast-int (reg (bv #x00 8)) 32 1 1 64) (repair-cast-int_dsl (reg (bv #x01 8)) 32 64 32) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) (typed:cast-int (reg (bv #x01 8)) 32 1 1 64) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed:cast-int (reg (bv #x01 8)) 32 1 1 64) (typed:cast-int (reg (bv #x00 8)) 32 1 1 64) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(repair-smul_dsl (typed:cast-uint (reg (bv #x01 8)) 32 1 1 64) (typed:cast-uint (reg (bv #x00 8)) 32 1 1 64) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 0 0 0)"
            }
        }
    ],
    "_mm256_mul_epi32+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed:signed-vec-mul (repair-cast-int_dsl (reg (bv #x01 8)) 32 64 32) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed:signed-vec-mul (repair-cast-int_dsl (reg (bv #x01 8)) 32 64 32) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)"
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
    "_mm256_mul_epi32+typed:unsigned-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed:unsigned-vec-mul (repair-cast-int_dsl (reg (bv #x01 8)) 32 64 32) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 128 32 64 1 1 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mul_epi32",
                "output_expression": "(typed:unsigned-vec-mul (repair-cast-int_dsl (reg (bv #x01 8)) 32 64 32) (repair-cast-int_dsl (reg (bv #x00 8)) 32 64 32) 64 64)",
                "synth_expression": "(_mm256_mul_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 128 32 64 1 1 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-div (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-halving_add (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-halving_add (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-max (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x01 8)) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-min (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-mod (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-mod (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:signed-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-sat-add (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-sat-add (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-usat-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-sat-add (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-sat-sub (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-sat-sub (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-shr (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:signed-vec-shr (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-usat-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:slice_vectors (lit (bv #x00000000000000000000000000000008 128)) 8 1 8 8 128) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:slice_vectors (lit (bv #x00000000000000000000000000000013 128)) 2 1 2 32 128) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:slice_vectors (lit (bv #x00000000000000000000000000000008 128)) 8 1 8 8 128) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-absd (repair-usat-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-absd (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-absd (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-div (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-div (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-max (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-max (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-max (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x01 8)) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-min (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-mod (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-mod (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-usat-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-usat-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-usat-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-shr (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:unsigned-vec-shr (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:vec-add (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:vec-add (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:vec-add (repair-usat-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x00 8)) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:vec-bwand (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:vec-shl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:vec-shl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-usat-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        }
    ],
    "_mm512_mulhi_epu16+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-add_dsl (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 64 0 0 128 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:vec-sub (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-usat-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 128 128 0 128 16 0 1 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(typed:vec-sub (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 64 0 0 128 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (typed:cast-uint (reg (bv #x01 8)) 32 1 1 64) (typed:cast-uint (reg (bv #x00 8)) 32 1 1 64) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (typed:cast-uint (reg (bv #x00 8)) 32 1 1 64) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 64 32) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 64 0 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(repair-umul_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (typed:cast-uint (reg (bv #x01 8)) 32 1 1 64) 64 64)",
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
        },
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed:unsigned-vec-mul (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 64 32) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-cast-uint_dsl (reg (bv #x01 8)) 32 64 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x0000000000000010 64)) (lit (bv #x000000000000000c 64)) (lit (bv #x000000000000000b 64)) 8 64) 64 64)",
                "synth_expression": "(_mm_mul_su32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 64 0 0 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_mul_su32",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 64 32) (repair-usat-sub_dsl (lit (bv #x000000000000000a 64)) (lit (bv #x000000000000000d 64)) 8 64) 64 64)",
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 4 (typed:cast-uint (reg (bv #x01 8)) 32 1 2 64) 32 128)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:signed-vec-div (lit (bv #x0000000c 32)) (lit (bv #x00000011 32)) 32 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed:signed-vec-halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 16 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed:signed-vec-halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed:signed-vec-max (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed:signed-vec-min (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:signed-vec-sat-sub (lit (bv #x00000009 32)) (lit (bv #x00000009 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-absd (lit (bv #x00000006 32)) (lit (bv #x00000006 32)) 32 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:slice_vectors (reg (bv #x00 8)) 4 1 4 8 64) (typed:slice_vectors (reg (bv #x00 8)) 0 1 2 16 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed:unsigned-vec-min (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed:unsigned-vec-max (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-mod (lit (bv #x00000010 32)) (lit (bv #x00000010 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-mod (lit (bv #x0000000e 32)) (lit (bv #x00000007 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-rounding_shift_right (lit (bv #x00000012 32)) (lit (bv #x0000000a 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-rounding_shift_right (lit (bv #x00000010 32)) (lit (bv #x00000009 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-sat-sub (lit (bv #x0000000a 32)) (lit (bv #x00000014 32)) 8 32) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-sat-sub (lit (bv #x00000009 32)) (lit (bv #x00000015 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:vec-bwand (lit (bv #x0000000a 32)) (lit (bv #x00000015 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed:vec-bwand (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-vector-reduce-add_dsl 2 (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:vec-shl (lit (bv #x00000005 32)) (lit (bv #x00000010 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:vec-shl (lit (bv #x00000008 32)) (lit (bv #x00000005 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 16 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed:vec-shl (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (typed:vec-shl (lit (bv #x00000005 32)) (lit (bv #x0000000e 32)) 8 32) 8 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:vec-sub (lit (bv #x00000005 32)) (lit (bv #x00000005 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) 16 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(typed:vec-sub (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) (typed:vec-sub (lit (bv #x00000006 32)) (lit (bv #x00000006 32)) 16 32) 8 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:signed-vec-halving_add (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:signed-vec-halving_add (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:signed-vec-max (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:signed-vec-max (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:signed-vec-min (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:signed-vec-min (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:signed-vec-mod (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:signed-vec-mod (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:signed-vec-shr (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-absd (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-absd (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:signed-vec-sat-sub (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:signed-vec-sat-sub (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-max (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-max (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-min (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-min (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-mod (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-shr (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:unsigned-vec-shr (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:vec-bwand (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:vec-bwand (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_sll_epi64+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:vec-sub (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sll_epi64",
                "output_expression": "(typed:vec-sub (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_sll_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:signed-vec-min (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:signed-vec-min (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:signed-vec-mod (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:signed-vec-mod (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:signed-vec-halving_add (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:signed-vec-halving_add (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:signed-vec-max (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:signed-vec-max (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:signed-vec-sat-sub (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:signed-vec-sat-sub (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-absd (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-absd (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-max (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-max (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-min (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-min (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-shr (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-shr (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:vec-bwand (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:vec-bwand (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:vec-sub (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:vec-sub (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)"
            }
        }
    ],
    "_mm_add_pi8+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-mod (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_pi8",
                "output_expression": "(typed:unsigned-vec-mod (repair-add_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_add_pi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hsub_pi32",
                "output_expression": "(repair-sub_dsl (typed:slice_vectors (reg (bv #x01 8)) 4 1 4 8 64) (typed:slice_vectors (reg (bv #x01 8)) 0 1 4 8 64) 32 32)",
                "synth_expression": "(_mm_hsub_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 32 0 0)"
            }
        }
    ],
    "_mm256_mask_cmpeq_epu8_mask+typed:signed-vec-le": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_mask_cmpeq_epu8_mask",
                "output_expression": "(typed:signed-vec-le (lit (bv #x0008 16)) (lit (bv #x0005 16)) 8 8)",
                "synth_expression": "(_mm256_mask_cmpeq_epu8_mask_dsl (reg (bv #x00 8)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x02 8)) (lit (bv #b0 1)) (lit (bv #b1 1)) (lit (bv #x00 8)) 8 8 0 4 1 1 64 1 4)"
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
    "_mm512_or_epi32+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_or_epi32",
                "output_expression": "(typed:signed-vec-sat-sub (repair-bwor_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_or_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 0)"
            }
        }
    ],
    "_m_packssdw+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:signed-vec-div (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (typed:signed-vec-div (lit (bv #x0014 16)) (lit (bv #x0010 16)) 16 16) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 1 16 1 1 16 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (typed:unsigned-vec-sat-sub (lit (bv #x0009 16)) (lit (bv #x000b 16)) 8 16) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 1 16 1 1 16 64 2 0)"
            }
        }
    ],
    "_m_packssdw+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_packssdw",
                "output_expression": "(typed:vec-shl (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) (typed:vec-shl (lit (bv #x0014 16)) (lit (bv #x0015 16)) 8 16) 16 16)",
                "synth_expression": "(_m_packssdw_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 32 8 32 64 8 0 16 1 0 16 64 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:signed-vec-div (lit (bv #x0000000c 32)) (lit (bv #x00000013 32)) 32 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi16+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi16",
                "output_expression": "(repair-add_dsl (typed:vec-sub (lit (bv #x0000000e 32)) (lit (bv #x0000000e 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm_hadd_pi16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 64 32 64 128 32 -1 2 32 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:signed-vec-mod (lit (bv #x00000015 32)) (lit (bv #x00000015 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32 0 32 32 -1 -1 0 32 0)"
            }
        }
    ],
    "_mm_hadd_pi32+typed:unsigned-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_hadd_pi32",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x00000015 32)) (lit (bv #x00000012 32)) (lit (bv #x0000000d 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x01 8)) 32 64) 32 32)",
                "synth_expression": "(_mm_hadd_pi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32 0 32 32 -1 -1 0 32 0)"
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
    "_mm512_cmplt_epi32_mask+typed:vec-eq": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cmplt_epi32_mask",
                "output_expression": "(typed:vec-eq (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm512_cmplt_epi32_mask_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x01 8)) (reg (bv #x00 8)) 8 8 0 8 1 1 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cmplt_epi32_mask",
                "output_expression": "(typed:vec-eq (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm512_cmplt_epi32_mask_dsl (lit (bv #b0 1)) (lit (bv #b1 1)) (reg (bv #x00 8)) (reg (bv #x01 8)) 8 8 0 8 1 1 64 1 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:signed-vec-halving_add (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 512 512 0 512 16 0 16 16 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:signed-vec-min (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 512 512 0 512 32 0 32 32 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:signed-vec-max (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 512 512 0 512 64 0 64 64 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:signed-vec-mod (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 512 512 0 512 16 0 16 16 0)"
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
    "_mm512_sllv_epi16+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:unsigned-vec-absd (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 512 512 0 512 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 512 512 0 512 32 0 32 32 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:signed-vec-sat-sub (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 512 512 0 512 32 0 32 32 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-shl_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 512 512 0 512 16 0 16 16 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:unsigned-vec-max (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 512 512 0 512 64 0 64 64 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:unsigned-vec-min (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 512 512 0 512 16 0 16 16 0)"
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
    "_mm512_sllv_epi16+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 512 512 0 512 64 0 64 64 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 512 512 0 512 32 0 32 32 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:unsigned-vec-mod (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 512 512 0 512 32 0 32 32 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:unsigned-vec-shr (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 512 512 0 512 16 0 16 16 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:vec-bwand (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 512 512 0 512 64 0 64 64 0)"
            }
        }
    ],
    "_mm512_sllv_epi16+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_sllv_epi16",
                "output_expression": "(typed:vec-sub (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_sllv_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 512 512 0 512 16 0 16 16 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed:signed-vec-halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed:signed-vec-max (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed:signed-vec-min (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:signed-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed:signed-vec-rounding_shift_right (lit (bv #x00000008 32)) (lit (bv #x00000013 32)) 8 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
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
    "_mm256_hadd_epi32+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed:unsigned-vec-div (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-div (lit (bv #x00000008 32)) (lit (bv #x00000005 32)) 32 32) 32 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed:unsigned-vec-max (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-mod (lit (bv #x00000012 32)) (lit (bv #x00000006 32)) 32 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:unsigned-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x00000010 32)) (lit (bv #x00000009 32)) (lit (bv #x00000010 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-sat-sub (lit (bv #x00000015 32)) (lit (bv #x00000015 32)) 8 32) 32 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed:vec-bwand (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed:vec-bwand (lit (bv #x00000008 32)) (lit (bv #x00000011 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed:vec-shl (lit (bv #x00000009 32)) (lit (bv #x00000014 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 32 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(typed:vec-shl (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (typed:vec-shl (lit (bv #x00000007 32)) (lit (bv #x00000015 32)) 8 32) 8 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm256_hadd_epi32+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm256_hadd_epi32",
                "output_expression": "(repair-add_dsl (typed:vec-sub (lit (bv #x0000000c 32)) (lit (bv #x0000000c 32)) 16 32) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)",
                "synth_expression": "(_mm256_hadd_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 128 0 64 32 64 128 32 -1 32 2 -1 128 96 2 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-halving_add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (reg (bv #x01 8)) (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:signed-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (reg (bv #x01 8)) (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-max (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (reg (bv #x01 8)) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-min (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-uabsd_dsl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-uabsd_dsl (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-mod (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-mod (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-mod (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-mod (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:signed-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-sat-add (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-sat-add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-sat-add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-sat-add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-sat-add (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-uabsd_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-uabsd_dsl (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-sat-sub (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-sat-sub (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-sat-sub (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-sat-sub (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-shr (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-shr (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:signed-vec-shr (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:slice_vectors (lit (bv #x00000000000000000000000000000007 128)) 8 1 8 8 128) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:slice_vectors (lit (bv #x0000000000000000000000000000000d 128)) 1 1 1 64 128) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-uabsd_dsl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:slice_vectors (lit (bv #x00000000000000000000000000000013 128)) 8 1 8 8 128) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-uabsd_dsl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-uabsd_dsl (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-absd (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-absd (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-absd (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-absd (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-absd (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-absd (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (reg (bv #x00 8)) (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (reg (bv #x01 8)) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-max (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-max (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-max (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-max (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-max (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (reg (bv #x01 8)) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-min (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-uabsd_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-uabsd_dsl (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-mod (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-mod (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-mod (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-mod (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (reg (bv #x00 8)) (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-uabsd_dsl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-uabsd_dsl (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-uabsd_dsl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-uabsd_dsl (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-shr (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-shr (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-shr (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:unsigned-vec-shr (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:vec-add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:vec-add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:vec-add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:vec-add (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:vec-add (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ],
    "_mm_sub_si64+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(repair-sub_dsl (reg (bv #x01 8)) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:vec-bwand (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
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
    "_mm_sub_si64+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:vec-shl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:vec-shl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64 0 64 64 -1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_sub_si64",
                "output_expression": "(typed:vec-shl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm_sub_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrawi",
                "output_expression": "(typed:signed-vec-shr (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 64 8) 64 64)",
                "synth_expression": "(_m_psrawi_dsl (reg (bv #x00 8)) (lit (bv #xffffffffffffffff 64)) (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #b1 1)) (lit (bv #x3f 8)) 8 8 0 32 8 0 8 0 64 1 1 1 0 8 0 0)"
            }
        }
    ],
    "_mm512_packs_epi32+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:signed-vec-max (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) 16 16)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 8 64 128 8 1 16 2 1 16 128 2 0)"
            }
        }
    ],
    "_mm512_packs_epi32+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:signed-vec-halving_add (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) 16 16)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 8 64 128 8 1 16 2 1 16 128 2 0)"
            }
        }
    ],
    "_mm512_packs_epi32+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:signed-vec-mod (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #t) (typed:signed-vec-mod (lit (bv #x000e 16)) (lit (bv #x000e 16)) 16 16) 8 16)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 16 64 128 16 1 32 2 1 32 128 2 0)"
            }
        }
    ],
    "_mm512_packs_epi32+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:signed-vec-min (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #t) 16 16)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 16 64 128 16 1 32 2 1 32 128 2 0)"
            }
        }
    ],
    "_mm512_packs_epi32+typed:signed-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (typed:signed-vec-rounding_mul_shift_right (lit (bv #x000c 16)) (lit (bv #x000b 16)) (lit (bv #x0007 16)) 8 16) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #f) (typed:signed-vec-rounding_mul_shift_right (lit (bv #x000f 16)) (lit (bv #x000f 16)) (lit (bv #x0015 16)) 8 16) 16 16)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 8 64 128 8 0 16 2 0 16 128 2 0)"
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
    "_mm512_packs_epi32+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #t) 16 16)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 16 64 128 16 1 32 2 1 32 128 2 0)"
            }
        }
    ],
    "_mm512_packs_epi32+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:unsigned-vec-max (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) 8 16)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 8 64 128 8 1 16 2 1 16 128 2 0)"
            }
        }
    ],
    "_mm512_packs_epi32+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #f) (repair-saturate_dsl (reg (bv #x00 8)) 32 16 32 #f) 16 16)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 16 64 128 16 0 32 2 0 32 128 2 0)"
            }
        }
    ],
    "_mm512_packs_epi32+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:vec-bwand (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) 16 16)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 8 64 128 8 1 16 2 1 16 128 2 0)"
            }
        }
    ],
    "_mm512_packs_epi32+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_packs_epi32",
                "output_expression": "(typed:vec-shl (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (typed:vec-shl (lit (bv #x0010 16)) (lit (bv #x0013 16)) 8 16) 8 16)",
                "synth_expression": "(_mm512_packs_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 128 0 64 8 64 128 8 1 16 2 1 16 128 2 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:signed-vec-halving_add (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:signed-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:signed-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (reg (bv #x01 8)) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:signed-vec-max (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (reg (bv #x01 8)) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:signed-vec-mod (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:signed-vec-mod (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:signed-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:signed-vec-sat-add (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:signed-vec-sat-add (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:signed-vec-sat-sub (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:signed-vec-sat-sub (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:signed-vec-shr (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 64 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-absd (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-absd (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-absd (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
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
    "_mm_min_epu16+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (reg (bv #x00 8)) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-max (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-max (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-max (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-mod (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-mod (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-shr (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:unsigned-vec-shr (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:vec-add (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:vec-add (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 8 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 64 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:vec-bwand (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 8 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(repair-smin_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 16 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:vec-shl (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)"
            }
        }
    ],
    "_mm_min_epu16+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:vec-sub (repair-smin_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 256 256 0 256 32 1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_min_epu16",
                "output_expression": "(typed:vec-sub (repair-smin_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_min_epu16_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 256 256 0 256 16 1 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:signed-vec-halving_add (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) 8 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:signed-vec-max (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 16 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:signed-vec-max (repair-usat-sub_dsl (lit (bv #x0000000000000009 64)) (lit (bv #x000000000000000f 64)) 16 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 32) 64 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:signed-vec-min (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 8 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:signed-vec-mod (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 32) (repair-umul_dsl (lit (bv #x0000000000000015 64)) (lit (bv #x000000000000000d 64)) 64 64) 16 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:signed-vec-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:signed-vec-mul (repair-usat-sub_dsl (lit (bv #x000000000000000c 64)) (lit (bv #x000000000000000b 64)) 16 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:signed-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:signed-vec-rounding_halving_add (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) 32 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:signed-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-uint_dsl (lit (bv #x00000010 32)) 8 64 8) (repair-usat-sub_dsl (lit (bv #x000000000000000e 64)) (lit (bv #x000000000000000a 64)) 8 64) 32 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:signed-vec-sat-add (repair-usat-sub_dsl (lit (bv #x000000000000000f 64)) (lit (bv #x0000000000000011 64)) 8 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) 32 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:signed-vec-shr (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) (repair-usat-sub_dsl (lit (bv #x000000000000000e 64)) (lit (bv #x0000000000000013 64)) 8 64) 16 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-absd (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) (repair-usat-sub_dsl (lit (bv #x0000000000000007 64)) (lit (bv #x0000000000000008 64)) 8 64) 16 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (lit (bv #x000000000000000c 64)) (lit (bv #x000000000000000c 64)) 64 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 32) 32 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-div (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) (typed:unsigned-vec-div (lit (bv #x0000000000000012 64)) (lit (bv #x000000000000000c 64)) 64 64) 64 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) 64 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-max (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) 32 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-mod (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 32) (repair-umul_dsl (lit (bv #x0000000000000015 64)) (lit (bv #x000000000000000e 64)) 16 64) 16 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-mod (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-usat-sub_dsl (lit (bv #x0000000000000013 64)) (lit (bv #x0000000000000014 64)) 16 64) 8 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 32) 64 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:unsigned-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-usat-sub_dsl (lit (bv #x0000000000000010 64)) (lit (bv #x000000000000000f 64)) 16 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-usat-sub_dsl (lit (bv #x0000000000000008 64)) (lit (bv #x0000000000000010 64)) 16 64) 64 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x000000000000000d 64)) (lit (bv #x000000000000000e 64)) (lit (bv #x0000000000000007 64)) 8 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) (repair-usat-sub_dsl (lit (bv #x0000000000000005 64)) (lit (bv #x0000000000000008 64)) 16 64) 64 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x000000000000000b 64)) (lit (bv #x0000000000000007 64)) (lit (bv #x0000000000000006 64)) 8 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x0000000000000011 64)) (lit (bv #x000000000000000f 64)) (lit (bv #x0000000000000009 64)) 64 64) 64 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-usat-sub_dsl (lit (bv #x0000000000000005 64)) (lit (bv #x0000000000000015 64)) 16 64) 32 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-usat-sub_dsl (lit (bv #x0000000000000011 64)) (lit (bv #x0000000000000013 64)) 16 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 32) 64 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) (typed:unsigned-vec-sat-sub (lit (bv #x0000000000000014 64)) (lit (bv #x0000000000000015 64)) 16 64) 64 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) (repair-usat-sub_dsl (lit (bv #x0000000000000007 64)) (lit (bv #x0000000000000007 64)) 16 64) 16 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:unsigned-vec-shr (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-usat-sub_dsl (lit (bv #x0000000000000012 64)) (lit (bv #x0000000000000013 64)) 16 64) 32 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:vec-add (repair-usat-sub_dsl (lit (bv #x0000000000000010 64)) (lit (bv #x0000000000000012 64)) 32 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 32 32) 8 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 32 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:vec-bwand (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 16 32) 16 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 16 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:vec-shl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-usat-sub_dsl (lit (bv #x0000000000000006 64)) (lit (bv #x0000000000000009 64)) 16 64) 64 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:vec-shl (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (typed:vec-shl (lit (bv #x0000000000000009 64)) (lit (bv #x000000000000000b 64)) 8 64) 32 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        }
    ],
    "_mm512_cvtepu8_epi32+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtepu8_epi32",
                "output_expression": "(typed:vec-sub (repair-cast-uint_dsl (reg (bv #x00 8)) 32 64 32) (repair-usat-sub_dsl (lit (bv #x000000000000000c 64)) (lit (bv #x000000000000000f 64)) 32 64) 8 64)",
                "synth_expression": "(_mm512_cvtepu8_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 64 1 0 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:signed-vec-halving_add (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32) 16 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:signed-vec-max (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 32) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 32 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
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
    "_mm512_and_epi32+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:signed-vec-min (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 16 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:signed-vec-mod (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:signed-vec-sat-sub (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32) 32 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-absd (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32) 8 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32) (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 16 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (reg (bv #x00 8)) 32 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 32 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32) (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32) 8 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 8 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
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
    "_mm512_and_epi32+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-max (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) 8 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 32) 8 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-mod (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 32) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32) 16 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:unsigned-vec-shr (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_and_epi32+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_and_epi32",
                "output_expression": "(typed:vec-sub (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32) 32 32)",
                "synth_expression": "(_mm512_and_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_m_pslld+typed:cast-int": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000014 64)) 8 16 16) (typed:cast-int (lit (bv #x000f 16)) 8 1 2 16) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:cast-int (lit (bv #x000a 16)) 8 1 2 16) (typed:cast-int (lit (bv #x0013 16)) 8 1 2 16) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:cast-int (lit (bv #x0012 16)) 16 1 1 32) (repair-cast-uint_dsl (lit (bv #x000000000000000b 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000006 64)) 8 32 8) (typed:cast-int (lit (bv #x000d 16)) 16 1 1 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:cast-int (reg (bv #x00 8)) 16 1 4 8) (typed:cast-int (reg (bv #x00 8)) 16 1 4 8) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:cast-int (reg (bv #x00 8)) 32 1 2 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 16 64) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:cast-uint": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000005 64)) 8 16 16) (typed:cast-uint (lit (bv #x000d 16)) 16 1 1 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:cast-uint (lit (bv #x0015 16)) 8 1 2 16) (typed:cast-uint (lit (bv #x0012 16)) 16 1 1 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:cast-uint (lit (bv #x000e 16)) 8 1 2 16) (repair-cast-uint_dsl (lit (bv #x0000000000000013 64)) 16 32 16) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:cast-uint (lit (bv #x000a 16)) 16 1 1 32) (repair-cast-uint_dsl (lit (bv #x0000000000000015 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x000000000000000e 64)) 8 16 16) (typed:cast-uint (lit (bv #x0014 16)) 8 1 2 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:cast-uint (lit (bv #x0006 16)) 8 1 2 16) (typed:cast-uint (lit (bv #x0010 16)) 8 1 2 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:concat_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:concat_vectors (lit (bv #x0014 16)) (lit (bv #x0011 16)) 8 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (reg (bv #x01 8)) (typed:concat_vectors (lit (bv #x0015 16)) (lit (bv #x0008 16)) 8 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:concat_vectors (lit (bv #x0006 16)) (lit (bv #x0013 16)) 8 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (lit (bv #x000000000000000f 64)) 8 32 8) (typed:concat_vectors (lit (bv #x0014 16)) (lit (bv #x0013 16)) 8 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:concat_vectors (lit (bv #x0006 16)) (lit (bv #x0009 16)) 8 16) (typed:concat_vectors (lit (bv #x000b 16)) (lit (bv #x0015 16)) 8 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000009 64)) 8 32 8) (typed:concat_vectors (lit (bv #x000b 16)) (lit (bv #x000c 16)) 8 16) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:concat_vectors (lit (bv #x0007 16)) (lit (bv #x0009 16)) 16 16) (typed:concat_vectors (lit (bv #x0009 16)) (lit (bv #x0011 16)) 16 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-cast-uint_dsl (typed:signed-vec-div (lit (bv #x0000000000000006 64)) (lit (bv #x000000000000000b 64)) 16 16) 8 16 16)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (reg (bv #x01 8)) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000006 64)) 8 32 8) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-div (repair-cast-uint_dsl (lit (bv #x000000000000000c 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x0000000000000014 64)) 8 16 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-mod (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-mod (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (reg (bv #x01 8)) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-mod (repair-cast-uint_dsl (reg (bv #x00 8)) 64 32 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 64 32 64) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-mod (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-mod (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:signed-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-cast-uint_dsl (typed:signed-vec-rounding_mul_shift_right (lit (bv #x000000000000000e 64)) (lit (bv #x0000000000000014 64)) (lit (bv #x0000000000000015 64)) 16 16) 8 16 16)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-cast-uint_dsl (lit (bv #x0000000000000013 64)) 16 32 16) (reg (bv #x01 8)) (repair-cast-uint_dsl (lit (bv #x000000000000000e 64)) 8 16 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-cast-uint_dsl (lit (bv #x0000000000000013 64)) 8 16 16) (repair-cast-uint_dsl (lit (bv #x000000000000000f 64)) 8 16 16) (repair-cast-uint_dsl (lit (bv #x0000000000000012 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (reg (bv #x01 8)) (repair-cast-uint_dsl (lit (bv #x000000000000000c 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-cast-uint_dsl (lit (bv #x0000000000000005 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x000000000000000c 64)) 8 32 8) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-cast-uint_dsl (lit (bv #x0000000000000006 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x000000000000000c 64)) 8 32 8) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x000000000000000e 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x0000000000000013 64)) 8 32 8) (repair-cast-uint_dsl (lit (bv #x0000000000000009 64)) 16 32 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (reg (bv #x01 8)) (repair-cast-uint_dsl (lit (bv #x0000000000000014 64)) 16 32 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x000000000000000e 64)) 16 32 16) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:signed-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-cast-uint_dsl (typed:signed-vec-rounding_shift_right (lit (bv #x0000000000000006 64)) (lit (bv #x000000000000000d 64)) 8 8) 8 32 8)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-cast-uint_dsl (lit (bv #x0000000000000012 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x0000000000000011 64)) 16 32 16) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-rounding_shift_right (typed:signed-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x000000000000000d 64)) 8 32 8) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-sat-sub (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-sat-sub (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-sat-sub (repair-cast-uint_dsl (reg (bv #x00 8)) 64 32 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 64 32 64) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-sat-sub (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-sat-sub (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-sat-sub (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-cast-uint_dsl (typed:signed-vec-shr (lit (bv #x0000000000000009 64)) (lit (bv #x000000000000000e 64)) 8 8) 8 32 8)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-umul_dsl (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-umul_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:signed-vec-shr (repair-cast-uint_dsl (lit (bv #x0000000000000010 64)) 8 16 16) (repair-cast-uint_dsl (lit (bv #x0000000000000014 64)) 8 16 16) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (reg (bv #x01 8)) (typed:signed-vec-widen-mul (lit (bv #x0015 16)) (lit (bv #x0013 16)) 8 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:signed-vec-widen-mul (lit (bv #x000f 16)) (lit (bv #x0005 16)) 8 16) (typed:signed-vec-widen-mul (lit (bv #x0008 16)) (lit (bv #x000e 16)) 8 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-widen-mul (lit (bv #x000a 16)) (lit (bv #x0011 16)) 8 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-widen-mul (lit (bv #x0008 16)) (lit (bv #x0012 16)) 8 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:signed-vec-widen-mul (lit (bv #x000f 16)) (lit (bv #x0009 16)) 16 16) (repair-cast-uint_dsl (lit (bv #x0000000000000014 64)) 8 32 8) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000006 64)) 16 32 16) (typed:signed-vec-widen-mul (lit (bv #x0008 16)) (lit (bv #x0006 16)) 8 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-widen-mul (lit (bv #x0006 16)) (lit (bv #x0014 16)) 8 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000010 64)) 8 32 8) (typed:signed-vec-widen-mul (lit (bv #x000a 16)) (lit (bv #x0012 16)) 16 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-widen-mul (lit (bv #x0011 16)) (lit (bv #x000d 16)) 8 16) (typed:signed-vec-widen-mul (lit (bv #x000f 16)) (lit (bv #x0013 16)) 8 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-cast-uint_dsl (typed:slice_vectors (lit (bv #x00000000000000000000000000000008 128)) 1 1 1 8 16) 8 32 8)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 64 32 64) (typed:slice_vectors (reg (bv #x00 8)) 0 1 2 16 64) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:slice_vectors (reg (bv #x00 8)) 0 1 2 16 64) (typed:slice_vectors (reg (bv #x00 8)) 0 1 2 16 64) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:slice_vectors (repair-cast-uint_dsl (reg (bv #x01 8)) 32 64 32) 2 1 2 16 64)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:slice_vectors (typed:slice_vectors (lit (bv #x00000000000000000000000000000011 128)) 2 1 2 32 128) 0 1 4 8 64)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:slice_vectors (reg (bv #x00 8)) 0 1 2 16 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 64 32 64) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-absd (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-absd (repair-cast-uint_dsl (reg (bv #x00 8)) 16 8 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 16 8 64) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-absd (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-absd (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-absd (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-absd (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (reg (bv #x01 8)) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 64 32 64) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000005 64)) 8 16 16) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-div (repair-cast-uint_dsl (lit (bv #x000000000000000a 64)) 8 16 16) (repair-cast-uint_dsl (lit (bv #x0000000000000010 64)) 8 16 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-div (repair-cast-uint_dsl (lit (bv #x0000000000000006 64)) 16 32 16) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-mod (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-mod (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-mod (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (reg (bv #x01 8)) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-mod (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-mod (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-mod (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:unsigned-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-cast-uint_dsl (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x0000000000000010 64)) (lit (bv #x0000000000000014 64)) (lit (bv #x0000000000000013 64)) 16 16) 8 16 16)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x000000000000000a 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-cast-uint_dsl (lit (bv #x000000000000000f 64)) 16 32 16) (reg (bv #x01 8)) (repair-cast-uint_dsl (lit (bv #x000000000000000f 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-cast-uint_dsl (lit (bv #x000000000000000a 64)) 16 32 16) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 16 64) (repair-cast-uint_dsl (lit (bv #x0000000000000014 64)) 8 32 8) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-cast-uint_dsl (lit (bv #x0000000000000015 64)) 8 32 8) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x0000000000000015 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x000000000000000f 64)) 8 32 8) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x0000000000000008 64)) 8 16 16) (repair-cast-uint_dsl (lit (bv #x0000000000000014 64)) 8 32 8) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x000000000000000e 64)) 8 16 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x0000000000000013 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x000000000000000a 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x0000000000000015 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 64 32 64) (repair-cast-uint_dsl (lit (bv #x0000000000000015 64)) 16 32 16) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (reg (bv #x01 8)) (repair-cast-uint_dsl (lit (bv #x000000000000000f 64)) 8 32 8) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-cast-uint_dsl (lit (bv #x000000000000000c 64)) 8 16 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-cast-uint_dsl (lit (bv #x000000000000000f 64)) 16 32 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-cast-uint_dsl (lit (bv #x0000000000000014 64)) 8 32 8) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x000000000000000e 64)) 8 32 8) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-cast-uint_dsl (typed:unsigned-vec-rounding_shift_right (lit (bv #x0000000000000005 64)) (lit (bv #x0000000000000014 64)) 8 8) 8 32 8)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-cast-uint_dsl (lit (bv #x0000000000000012 64)) 8 16 16) (repair-cast-uint_dsl (lit (bv #x0000000000000012 64)) 8 16 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x000000000000000a 64)) 8 32 8) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-cast-uint_dsl (typed:unsigned-vec-sat-sub (lit (bv #x000000000000000a 64)) (lit (bv #x0000000000000014 64)) 8 16) 16 32 16)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (reg (bv #x01 8)) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-cast-uint_dsl (reg (bv #x00 8)) 32 16 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 16 64) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-shr (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-shr (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-shr (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-shr (repair-cast-uint_dsl (lit (bv #x0000000000000005 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x0000000000000005 64)) 8 32 8) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-shr (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-shr (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-shr (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-shr (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-shr (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:unsigned-vec-shr (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (reg (bv #x01 8)) (typed:unsigned-vec-widen-mul (lit (bv #x000f 16)) (lit (bv #x0009 16)) 8 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-widen-mul (lit (bv #x000c 16)) (lit (bv #x000a 16)) 8 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (lit (bv #x000000000000000c 64)) 8 32 8) (typed:unsigned-vec-widen-mul (lit (bv #x0014 16)) (lit (bv #x000d 16)) 8 16) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-widen-mul (lit (bv #x0014 16)) (lit (bv #x000e 16)) 8 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:unsigned-vec-widen-mul (lit (bv #x000b 16)) (lit (bv #x000c 16)) 8 16) (typed:unsigned-vec-widen-mul (lit (bv #x000e 16)) (lit (bv #x0009 16)) 8 16) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:unsigned-vec-widen-mul (lit (bv #x0015 16)) (lit (bv #x0010 16)) 8 16) (repair-cast-uint_dsl (lit (bv #x0000000000000010 64)) 8 16 16) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-widen-mul (lit (bv #x0013 16)) (lit (bv #x0009 16)) 16 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-widen-mul (lit (bv #x000b 16)) (lit (bv #x000b 16)) 16 16) (typed:unsigned-vec-widen-mul (lit (bv #x0013 16)) (lit (bv #x0007 16)) 16 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000010 64)) 16 32 16) (typed:unsigned-vec-widen-mul (lit (bv #x0015 16)) (lit (bv #x0014 16)) 16 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:vec-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-cast-uint_dsl (typed:vec-bwand (lit (bv #x0000000000000010 64)) (lit (bv #x000000000000000b 64)) 8 16) 8 16 16)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:vec-bwand (repair-cast-uint_dsl (lit (bv #x0000000000000005 64)) 8 16 16) (repair-cast-uint_dsl (lit (bv #x000000000000000a 64)) 8 16 16) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:vec-bwand (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
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
    "_m_pslld+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-cast-uint_dsl (typed:vec-shl (lit (bv #x000000000000000f 64)) (lit (bv #x000000000000000b 64)) 8 16) 8 16 16)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:vec-shl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:vec-shl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:vec-shl (repair-cast-uint_dsl (lit (bv #x000000000000000f 64)) 8 16 16) (repair-cast-uint_dsl (lit (bv #x0000000000000010 64)) 8 32 8) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:vec-sub (repair-cast-uint_dsl (reg (bv #x00 8)) 64 32 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 64 32 64) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:vec-sub (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:vec-sub (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (reg (bv #x01 8)) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:vec-sub (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x00 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:vec-sub (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(typed:vec-sub (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        }
    ],
    "_m_pslld+typed:xBroadcast": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:xBroadcast (lit (bv #x0012 16)) 8 8 4) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:xBroadcast (lit (bv #x0009 16)) 8 8 4) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (reg (bv #x01 8)) (typed:xBroadcast (lit (bv #x000a 16)) 8 8 4) 32 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-cast-uint_dsl (lit (bv #x000000000000000a 64)) 8 32 8) (typed:xBroadcast (lit (bv #x0008 16)) 16 16 2) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (repair-shl_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:xBroadcast (lit (bv #x0015 16)) 16 16 2) 16 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-shl_dsl (typed:xBroadcast (lit (bv #x0013 16)) 8 8 4) (typed:xBroadcast (lit (bv #x0012 16)) 8 8 4) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000013 64)) 8 16 16) (typed:xBroadcast (lit (bv #x0014 16)) 16 16 2) 8 32)",
                "synth_expression": "(_m_pslld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000000f 64)) (reg (bv #x01 8)) 64 64 0 64 16 0 64 0 16 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_pslld",
                "output_expression": "(repair-usat-sub_dsl (typed:xBroadcast (lit (bv #x0009 16)) 8 8 4) (typed:xBroadcast (lit (bv #x000f 16)) 8 8 4) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_andnot_epi32",
                "output_expression": "(typed:signed-vec-sat-sub (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32) (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_andnot_epi32",
                "output_expression": "(typed:unsigned-vec-absd (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 32) (reg (bv #x00 8)) 16 32)",
                "synth_expression": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_andnot_epi32",
                "output_expression": "(typed:unsigned-vec-absd (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 32) (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 32) 16 32)",
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_andnot_epi32",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32) 32 32)",
                "synth_expression": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_andnot_epi32",
                "output_expression": "(typed:vec-bwand (repair-bwand_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 32) (repair-bwnot_dsl (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_mm512_andnot_epi32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_andnot_epi32",
                "output_expression": "(typed:vec-bwand (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 16 32) (repair-bwnot_dsl (reg (bv #x01 8)) 8 32) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_andnot_epi32",
                "output_expression": "(typed:vec-sub (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-bwand_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32) 8 32)",
                "synth_expression": "(_mm512_andnot_epi32_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-halving_add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 64 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-max (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-mod (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-mod (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-mod (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-mod (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (typed:signed-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-min (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:signed-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-sat-add (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-sat-add (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-sat-add (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-sat-add (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-sat-add (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-shr (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-shr (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:signed-vec-shr (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-absd (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-absd (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-absd (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-absd (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-absd (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-absd (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-max (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-max (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-max (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-max (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-max (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-min (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-mod (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-mod (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-mod (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-mod (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 8 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-shr (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-shr (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 32 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-shr (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-uabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:unsigned-vec-shr (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:vec-add (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:vec-add (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:vec-add (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:vec-add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sabsd_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 64 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:vec-add (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 64 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:vec-bwand (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 32 -1 0)"
            }
        }
    ],
    "_mm512_subs_epi8+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:vec-shl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 8 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 8 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:vec-shl (repair-sub_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-sabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 512 512 0 512 16 -1 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_subs_epi8",
                "output_expression": "(typed:vec-shl (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-uabsd_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_subs_epi8_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 512 512 0 512 16 -1 0)"
            }
        }
    ],
    "_m_psrld+typed:cast-int": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:cast-int (lit (bv #x0009 16)) 16 1 1 32) (repair-cast-uint_dsl (lit (bv #x0000000000000009 64)) 8 16 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000011 64)) 8 16 16) (typed:cast-int (lit (bv #x0014 16)) 16 1 1 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000011 64)) 16 32 16) (typed:cast-int (lit (bv #x000d 16)) 16 1 1 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:cast-int (lit (bv #x000c 16)) 8 1 2 16) (typed:cast-int (lit (bv #x000c 16)) 16 1 1 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:cast-int (lit (bv #x0009 16)) 16 1 1 32) (repair-cast-uint_dsl (lit (bv #x000000000000000d 64)) 8 32 8) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:cast-int (lit (bv #x000f 16)) 16 1 1 32) (typed:cast-int (lit (bv #x000b 16)) 8 1 2 16) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:cast-uint (reg (bv #x00 8)) 16 1 4 8) (typed:cast-uint (reg (bv #x00 8)) 16 1 4 8) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:cast-uint (lit (bv #x000d 16)) 16 1 1 32) (repair-cast-uint_dsl (lit (bv #x0000000000000011 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:cast-uint (lit (bv #x0011 16)) 8 1 2 16) (typed:cast-uint (lit (bv #x000d 16)) 16 1 1 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000015 64)) 8 16 16) (typed:cast-uint (lit (bv #x000c 16)) 8 1 2 16) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:cast-uint (reg (bv #x00 8)) 64 1 1 32) (repair-cast-uint_dsl (reg (bv #x00 8)) 64 32 64) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:concat_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x000000000000000b 64)) 16 32 16) (typed:concat_vectors (lit (bv #x0006 16)) (lit (bv #x000e 16)) 16 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (reg (bv #x01 8)) (typed:concat_vectors (lit (bv #x0008 16)) (lit (bv #x0007 16)) 8 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:concat_vectors (lit (bv #x0007 16)) (lit (bv #x0007 16)) 8 16) (typed:concat_vectors (lit (bv #x0012 16)) (lit (bv #x000f 16)) 8 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:concat_vectors (lit (bv #x0005 16)) (lit (bv #x0013 16)) 8 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-cast-uint_dsl (lit (bv #x000000000000000b 64)) 8 32 8) (typed:concat_vectors (lit (bv #x0006 16)) (lit (bv #x000b 16)) 8 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:concat_vectors (lit (bv #x0010 16)) (lit (bv #x000c 16)) 8 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:concat_vectors (lit (bv #x000c 16)) (lit (bv #x0012 16)) 8 16) (typed:concat_vectors (lit (bv #x0008 16)) (lit (bv #x0006 16)) 8 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000006 64)) 8 16 16) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (reg (bv #x01 8)) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-div (repair-cast-uint_dsl (lit (bv #x0000000000000007 64)) 8 32 8) (repair-cast-uint_dsl (lit (bv #x0000000000000011 64)) 8 32 8) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-div (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x0000000000000010 64)) 8 32 8) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-mod (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-mod (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-mod (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-mod (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-mod (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:signed-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-cast-uint_dsl (typed:signed-vec-rounding_mul_shift_right (lit (bv #x0000000000000009 64)) (lit (bv #x0000000000000007 64)) (lit (bv #x000000000000000e 64)) 8 8) 8 32 8)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-cast-uint_dsl (lit (bv #x000000000000000e 64)) 16 32 16) (reg (bv #x01 8)) (repair-cast-uint_dsl (lit (bv #x0000000000000015 64)) 8 16 16) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-cast-uint_dsl (lit (bv #x000000000000000e 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x000000000000000c 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x0000000000000010 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-cast-uint_dsl (lit (bv #x0000000000000009 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x0000000000000015 64)) 16 32 16) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-cast-uint_dsl (lit (bv #x000000000000000e 64)) 8 32 8) (repair-cast-uint_dsl (lit (bv #x000000000000000c 64)) 8 16 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x0000000000000014 64)) 8 32 8) (repair-cast-uint_dsl (lit (bv #x0000000000000010 64)) 16 32 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-cast-uint_dsl (lit (bv #x000000000000000c 64)) 8 32 8) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-rounding_mul_shift_right (typed:signed-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (reg (bv #x01 8)) (repair-cast-uint_dsl (lit (bv #x0000000000000015 64)) 8 16 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:signed-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-cast-uint_dsl (typed:signed-vec-rounding_shift_right (lit (bv #x0000000000000015 64)) (lit (bv #x0000000000000008 64)) 8 8) 8 32 8)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (typed:signed-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-cast-uint_dsl (lit (bv #x000000000000000b 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x000000000000000f 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-rounding_shift_right (typed:signed-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (lit (bv #x0000000000000005 64)) 8 32 8) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (reg (bv #x01 8)) (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-sat-sub (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-sat-sub (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-sat-sub (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-sat-sub (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-sat-sub (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-cast-uint_dsl (typed:signed-vec-shr (lit (bv #x0000000000000015 64)) (lit (bv #x000000000000000f 64)) 8 8) 8 32 8)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:signed-vec-shr (repair-cast-uint_dsl (lit (bv #x0000000000000008 64)) 8 32 8) (repair-cast-uint_dsl (lit (bv #x0000000000000012 64)) 8 16 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:signed-vec-widen-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-widen-mul (lit (bv #x0015 16)) (lit (bv #x000f 16)) 8 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (reg (bv #x01 8)) (typed:signed-vec-widen-mul (lit (bv #x000a 16)) (lit (bv #x0009 16)) 8 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x000000000000000c 64)) 8 32 8) (typed:signed-vec-widen-mul (lit (bv #x0007 16)) (lit (bv #x0014 16)) 8 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:signed-vec-widen-mul (lit (bv #x0010 16)) (lit (bv #x0013 16)) 8 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-widen-mul (lit (bv #x0014 16)) (lit (bv #x0005 16)) 8 16) (repair-cast-uint_dsl (lit (bv #x000000000000000d 64)) 16 32 16) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-cast-uint_dsl (lit (bv #x000000000000000d 64)) 8 32 8) (typed:signed-vec-widen-mul (lit (bv #x0009 16)) (lit (bv #x000e 16)) 16 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-widen-mul (lit (bv #x0011 16)) (lit (bv #x0011 16)) 8 16) (typed:signed-vec-widen-mul (lit (bv #x000d 16)) (lit (bv #x000d 16)) 8 16) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-cast-uint_dsl (typed:slice_vectors (lit (bv #x00000000000000000000000000000006 128)) 1 1 1 8 16) 8 32 8)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 64 32 64) (typed:slice_vectors (reg (bv #x00 8)) 0 1 2 16 64) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-absd (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-absd (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-absd (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-absd (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-absd (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-cast-uint_dsl (typed:unsigned-vec-div (lit (bv #x0000000000000005 64)) (lit (bv #x000000000000000b 64)) 8 8) 8 32 8)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (reg (bv #x01 8)) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000014 64)) 8 32 8) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 8 64) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-div (repair-cast-uint_dsl (lit (bv #x000000000000000f 64)) 8 32 8) (typed:unsigned-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-div (repair-cast-uint_dsl (lit (bv #x0000000000000005 64)) 8 32 8) (repair-cast-uint_dsl (lit (bv #x000000000000000d 64)) 16 32 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-mod (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-mod (repair-cast-uint_dsl (lit (bv #x000000000000000d 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x000000000000000d 64)) 8 32 8) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-mod (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-mod (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-mod (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-mul (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (reg (bv #x01 8)) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-cast-uint_dsl (lit (bv #x0000000000000011 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x000000000000000a 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x0000000000000009 64)) 16 32 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-cast-uint_dsl (lit (bv #x000000000000000e 64)) 16 32 16) (reg (bv #x01 8)) (repair-cast-uint_dsl (lit (bv #x0000000000000012 64)) 8 16 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (repair-cast-uint_dsl (lit (bv #x000000000000000c 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x0000000000000011 64)) 8 16 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (reg (bv #x01 8)) (repair-cast-uint_dsl (lit (bv #x0000000000000007 64)) 8 16 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:unsigned-vec-rounding_mul_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-cast-uint_dsl (lit (bv #x0000000000000009 64)) 8 16 16) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-cast-uint_dsl (lit (bv #x0000000000000013 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x000000000000000b 64)) 8 32 8) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x00 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (reg (bv #x01 8)) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-sat-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-cast-uint_dsl (lit (bv #x0000000000000009 64)) 8 16 16) (repair-cast-uint_dsl (lit (bv #x0000000000000015 64)) 16 32 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-shr (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-shr (reg (bv #x01 8)) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-shr (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (reg (bv #x01 8)) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-shr (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-shr (repair-cast-uint_dsl (lit (bv #x0000000000000007 64)) 16 32 16) (repair-cast-uint_dsl (lit (bv #x000000000000000f 64)) 8 16 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-shr (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-shr (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:unsigned-vec-shr (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:unsigned-vec-widen-mul": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (reg (bv #x01 8)) (typed:unsigned-vec-widen-mul (lit (bv #x0015 16)) (lit (bv #x0005 16)) 8 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000008 64)) 8 16 16) (typed:unsigned-vec-widen-mul (lit (bv #x000e 16)) (lit (bv #x0008 16)) 8 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-widen-mul (lit (bv #x000a 16)) (lit (bv #x0010 16)) 8 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:unsigned-vec-widen-mul (lit (bv #x0008 16)) (lit (bv #x0006 16)) 8 16) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:unsigned-vec-widen-mul (lit (bv #x0005 16)) (lit (bv #x0011 16)) 8 16) (typed:unsigned-vec-widen-mul (lit (bv #x0008 16)) (lit (bv #x0015 16)) 8 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000012 64)) 8 32 8) (typed:unsigned-vec-widen-mul (lit (bv #x0006 16)) (lit (bv #x0005 16)) 8 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-widen-mul (lit (bv #x000c 16)) (lit (bv #x0009 16)) 8 16) (typed:unsigned-vec-widen-mul (lit (bv #x0010 16)) (lit (bv #x000a 16)) 8 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-widen-mul (lit (bv #x0005 16)) (lit (bv #x0014 16)) 16 16) (repair-cast-uint_dsl (lit (bv #x000000000000000f 64)) 8 32 8) 16 32)",
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:vec-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:vec-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:vec-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:vec-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:vec-add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-cast-uint_dsl (typed:vec-bwand (lit (bv #x0000000000000015 64)) (lit (bv #x000000000000000a 64)) 16 16) 8 16 16)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:vec-bwand (repair-cast-uint_dsl (lit (bv #x0000000000000012 64)) 8 16 16) (repair-cast-uint_dsl (lit (bv #x0000000000000008 64)) 8 32 8) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-cast-uint_dsl (reg (bv #x00 8)) 16 8 64) (typed:vec-saturate (reg (bv #x00 8)) 16 1 4 8 #t) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:vec-saturate (reg (bv #x00 8)) 64 1 1 32 #f) (typed:vec-saturate (reg (bv #x00 8)) 64 1 1 32 #f) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-cast-uint_dsl (typed:vec-shl (lit (bv #x000000000000000d 64)) (lit (bv #x000000000000000b 64)) 8 16) 8 16 16)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:vec-shl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:vec-shl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:vec-shl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:vec-shl (repair-cast-uint_dsl (lit (bv #x0000000000000005 64)) 8 16 16) (repair-cast-uint_dsl (lit (bv #x000000000000000d 64)) 16 32 16) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:vec-sub (reg (bv #x01 8)) (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:vec-sub (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 32) (reg (bv #x01 8)) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:vec-sub (repair-cast-uint_dsl (reg (bv #x00 8)) 32 16 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 32 16 64) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:vec-sub (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(typed:vec-sub (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        }
    ],
    "_m_psrld+typed:xBroadcast": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000008 64)) 8 16 16) (typed:xBroadcast (lit (bv #x000f 16)) 8 8 4) 8 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-cast-uint_dsl (lit (bv #x0000000000000009 64)) 8 32 8) (typed:xBroadcast (lit (bv #x0007 16)) 8 8 4) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (reg (bv #x01 8)) (typed:xBroadcast (lit (bv #x0007 16)) 8 8 4) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-usat-sub_dsl (typed:xBroadcast (lit (bv #x0012 16)) 8 8 4) (typed:xBroadcast (lit (bv #x0015 16)) 16 16 2) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-umul_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:xBroadcast (lit (bv #x0012 16)) 16 16 2) 16 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (repair-usat-add_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 32) (typed:xBroadcast (lit (bv #x000d 16)) 8 8 4) 32 32)",
                "synth_expression": "(_m_psrld_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000 64)) (lit (bv #x000000000000001f 64)) (reg (bv #x01 8)) 64 64 0 64 32 0 64 0 32 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_m_psrld",
                "output_expression": "(repair-ushr_dsl (typed:xBroadcast (lit (bv #x0006 16)) 8 8 4) (typed:xBroadcast (lit (bv #x0008 16)) 8 8 4) 8 32)",
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srli_epi16",
                "output_expression": "(typed:unsigned-vec-shr (repair-cast-uint_dsl (reg (bv #x01 8)) 32 32 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 64 8) 64 64)",
                "synth_expression": "(_mm512_srli_epi16_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 128)) (lit (bv #x3f 8)) (reg (bv #x01 8)) 8 8 0 16 8 0 8 0 64 1 1 0 8 0 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:signed-vec-halving_add (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #f) (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #f) 8 32)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 0 64 1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:signed-vec-min (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #t) (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #t) 8 32)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 1 64 1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:signed-vec-max (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #t) (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #t) 8 32)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 1 64 1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:signed-vec-mod (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #t) (typed:signed-vec-mod (lit (bv #x00000012 32)) (lit (bv #x00000009 32)) 32 32) 8 32)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 1 64 1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:unsigned-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:unsigned-vec-div (repair-saturate_dsl (reg (bv #x00 8)) 16 8 64 #f) (typed:unsigned-vec-div (lit (bv #x00000013 32)) (lit (bv #x0000000a 32)) 32 32) 32 32)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 0 16 1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #f) (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #f) 16 32)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 0 64 1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #t) (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #t) 8 32)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 1 64 1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:unsigned-vec-max (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #t) (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #t) 8 32)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 1 64 1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #t) (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #t) 32 32)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 1 64 1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-saturate_dsl (reg (bv #x00 8)) 16 8 64 #t) (typed:unsigned-vec-sat-sub (lit (bv #x00000006 32)) (lit (bv #x00000014 32)) 16 32) 8 32)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 1 16 1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:unsigned-vec-rounding_mul_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_mul_shift_right (repair-saturate_dsl (reg (bv #x00 8)) 32 16 64 #t) (repair-saturate_dsl (lit (bv #x0000000000000008 64)) 16 16 32 #f) (typed:unsigned-vec-rounding_mul_shift_right (lit (bv #x0000000f 32)) (lit (bv #x0000000c 32)) (lit (bv #x00000006 32)) 16 32) 32 32)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 16 1 32 1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:vec-bwand (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #t) (repair-saturate_dsl (reg (bv #x00 8)) 64 32 64 #t) 8 32)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 32 1 64 1 0)"
            }
        }
    ],
    "_mm512_cvtusepi64_epi32+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_cvtusepi64_epi32",
                "output_expression": "(typed:vec-shl (repair-saturate_dsl (reg (bv #x00 8)) 16 8 64 #t) (typed:vec-shl (lit (bv #x00000011 32)) (lit (bv #x0000000b 32)) 8 32) 16 32)",
                "synth_expression": "(_mm512_cvtusepi64_epi32_dsl (reg (bv #x00 8)) 256 256 0 256 8 1 16 1 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_slli_epi16",
                "output_expression": "(typed:vec-shl (repair-cast-uint_dsl (reg (bv #x01 8)) 16 16 64) (repair-cast-uint_dsl (reg (bv #x00 8)) 8 64 8) 64 64)",
                "synth_expression": "(_mm512_slli_epi16_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x3f 8)) (reg (bv #x01 8)) 8 8 0 32 8 0 8 0 64 1 1 0 8 0 0)"
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
    "_mm512_srl_epi64+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:signed-vec-max (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:signed-vec-halving_add (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:signed-vec-min (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:signed-vec-mod (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:signed-vec-mod (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:signed-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:signed-vec-sat-add (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:signed-vec-sat-sub (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:signed-vec-sat-sub (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:signed-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:signed-vec-shr (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:signed-vec-shr (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-shr (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-absd (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 8 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-absd (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-max (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-min (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-min (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-min (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-min (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-min (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (reg (bv #x01 8)) 64 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-mod (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-mod (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-rounding_shift_right (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:vec-add (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
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
    "_mm512_srl_epi64+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:vec-bwand (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:vec-shl (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        }
    ],
    "_mm512_srl_epi64+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:vec-sub (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 16 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_srl_epi64",
                "output_expression": "(typed:vec-sub (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm512_srl_epi64_dsl (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) (lit (bv #x000000000000003f 64)) (reg (bv #x01 8)) 128 128 0 512 64 0 64 0 64 0 0)"
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
    "_mm_srlv_epi32+typed:signed-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:signed-vec-halving_add (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-umin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-umin_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 256 256 0 256 64 0 64 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (reg (bv #x00 8)) (typed:signed-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 256 256 0 256 64 0 64 64 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:signed-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-umin_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (reg (bv #x00 8)) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-umin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 256 256 0 256 64 0 64 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (typed:signed-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:signed-vec-max (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:signed-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-umin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (reg (bv #x00 8)) (typed:signed-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 256 256 0 256 64 0 64 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:signed-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) (repair-umin_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 256 256 0 256 64 0 64 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:signed-vec-min (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 256 256 0 256 64 0 64 64 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:signed-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:signed-vec-mod (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 256 256 0 256 64 0 64 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:signed-vec-mod (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:signed-vec-mod (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 256 256 0 256 16 0 16 16 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:signed-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:signed-vec-rounding_shift_right (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 256 256 0 256 32 0 32 32 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:signed-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:signed-vec-sat-add (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 256 256 0 256 32 0 32 32 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:signed-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:signed-vec-sat-sub (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 256 256 0 256 64 0 64 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:signed-vec-sat-sub (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:signed-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 256 256 0 256 16 0 16 16 0)"
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
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:signed-vec-shr (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 256 256 0 256 64 0 64 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:signed-vec-shr (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:signed-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 256 256 0 256 16 0 16 16 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:unsigned-vec-absd": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-absd (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-absd (typed:unsigned-vec-absd (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-absd (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-absd (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 256 256 0 256 32 0 32 32 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:slice_vectors": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:slice_vectors (lit (bv #x00000000000000000000000000000015 128)) 1 1 1 64 128) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:unsigned-vec-halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (repair-umin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (reg (bv #x01 8)) (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-halving_add (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 256 256 0 256 64 0 64 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-umin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 256 256 0 256 64 0 64 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (typed:unsigned-vec-halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:unsigned-vec-max": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (reg (bv #x01 8)) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-umin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-umin_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-max (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) 8 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 256 256 0 256 64 0 64 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-max (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-max (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:unsigned-vec-min": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (reg (bv #x01 8)) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 256 256 0 256 64 0 64 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-umin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 256 256 0 256 64 0 64 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (repair-umin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (reg (bv #x01 8)) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-umin_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-min (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-min (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-umin_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-min (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 256 256 0 256 64 0 64 64 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:unsigned-vec-mod": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-mod (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-mod (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 256 256 0 256 64 0 64 64 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:unsigned-vec-rounding_halving_add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (reg (bv #x01 8)) (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-umin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) (repair-umin_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (reg (bv #x00 8)) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_halving_add (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 256 256 0 256 32 0 32 32 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:unsigned-vec-rounding_shift_right": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-rounding_shift_right (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-rounding_shift_right (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) 8 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:unsigned-vec-sat-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-sat-add (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:unsigned-vec-sat-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) (typed:unsigned-vec-sat-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x01 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (typed:unsigned-vec-sat-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 256 256 0 256 16 0 16 16 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:unsigned-vec-sat-sub (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 16 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 256 256 0 256 16 0 16 16 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:vec-add": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:vec-add (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 16 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0010 16)) (reg (bv #x00 8)) 256 256 0 256 16 0 16 16 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:vec-bwand": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (reg (bv #x00 8)) 64 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x01 8)) 256 256 0 256 64 0 64 64 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (reg (bv #x01 8)) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 32 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-umin_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umin_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (typed:vec-bwand (reg (bv #x01 8)) (reg (bv #x01 8)) 32 64) (typed:vec-bwand (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:vec-bwand (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 8 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:vec-shl": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:vec-shl (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x00 8)) 16 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x00 8)) 256 256 0 256 32 0 32 32 0)"
            }
        }
    ],
    "_mm_srlv_epi32+typed:vec-sub": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(repair-ushr_dsl (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:vec-sub (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:vec-sub (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) (typed:vec-sub (reg (bv #x00 8)) (reg (bv #x00 8)) 64 64) 32 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x00 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x00000020 32)) (reg (bv #x01 8)) 256 256 0 256 32 0 32 32 0)"
            }
        },
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_srlv_epi32",
                "output_expression": "(typed:vec-sub (repair-ushr_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64) (repair-ushr_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 16 64)",
                "synth_expression": "(_mm_srlv_epi32_dsl (reg (bv #x01 8)) (lit (bv #x0000000000000000000000000000000000000000000000000000000000000000 256)) (lit (bv #x0000000000000040 64)) (reg (bv #x00 8)) 256 256 0 256 64 0 64 64 0)"
            }
        }
    ]
}
