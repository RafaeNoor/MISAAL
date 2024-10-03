
class TestObj:
    def __init__(self, name, expr, expected_result, label):
        self.name = name
        self.expr = expr
        self.expected_result = expected_result
        self.label = label
    def get_name(self):
        return self.name

    def get_expr(self):
        return self.expr

    def get_expected_result(self):
        return self.expected_result

    def get_label(self):
        return self.label



def test_generator_helper(desc, expected_result):
    label = [k for k in desc][0]
    test_name = label.split("+")[-1]
    expr = desc[label][0]['property']['output_expression']
    return TestObj(test_name, expr, expected_result, label)




tests = []


# Condition 3
cond_3_name = "typed:vec-add"
cond_3_expr = "(typed:vec-add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)"
cond_3_expected_result = False
cond_3_label ="_mm_sub_si64+typed:vec-add"

cond3 = TestObj(cond_3_name, cond_3_expr, cond_3_expected_result, cond_3_label)

tests.append(cond3)



# Should pass Max
max_name = "typed:signed-vec-max"
max_expr = "(typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)"
max_expected_result = True
max_label = "_mm256_max_epu64+typed:signed-vec-max"
max_test = TestObj(max_name, max_expr, max_expected_result, max_label)
tests.append(max_test)

not_name = "typed:vec-bwnot"
not_expr = "(repair-sub_dsl (typed:vec-bwnot (reg (bv #x00 8)) 64 64) (typed:vec-bwnot (reg (bv #x01 8)) 8 64) 64 64)"
not_expected_result = True
not_label = "_mm_sub_si64+typed:vec-bwnot"
not_test = TestObj(not_name, not_expr, not_expected_result, not_label)
tests.append(not_test)


pack_and_name = "typed:vec-bwand"
pack_and_expr = "(typed:vec-bwand (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) (repair-saturate_dsl (reg (bv #x00 8)) 16 8 32 #t) 16 16)"
pack_and_expected_result = False
pack_and_label = "_mm512_packs_epi32+typed:vec-bwand"

pack_and_test = TestObj(pack_and_name, pack_and_expr, pack_and_expected_result, pack_and_label)
tests.append(pack_and_test)


halving_add_name = "typed:signed-vec-halving_add"
halving_add_expr = "(typed:signed-vec-halving_add (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) (repair-vector-reduce-add_dsl 2 (reg (bv #x00 8)) 32 64) 8 32)"
halving_add_expected_result = False
halving_add_label = "_mm_hadd_pi16+typed:signed-vec-halving_add"
halving_add_test = TestObj(halving_add_name, halving_add_expr, halving_add_expected_result, halving_add_label)

tests.append(halving_add_test)



cast_int_test_name = "typed:cast-int"
cast_int_expr = "(typed:cast-int (reg (bv #x00 8)) 8 1 4 16)"
cast_int_expected_result = True
cast_int_label = "_mm512_cvtepu8_epi32+typed:cast-int"
cast_int_test = TestObj(cast_int_test_name, cast_int_expr, cast_int_expected_result, cast_int_label)

tests.append(cast_int_test)


max_rnd_shr_test_name = "typed:unsigned-vec-rounding_shift_right"
max_rnd_shr_expr = "(repair-umax_dsl (typed:unsigned-vec-rounding_shift_right (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (repair-umax_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 32 64) 32 64)"
max_rnd_shr_expected_result = True # Interestingly this is for the case where rounding shift right 1 by 1 returns 1 but shifting any > 1 value returns usually 0 so this is infact a meaningful example
max_rnd_shr_label = "_mm256_max_epu64+typed:unsigned-vec-rounding_shift_right"

max_rnd_shr_test = TestObj(max_rnd_shr_test_name, max_rnd_shr_expr, max_rnd_shr_expected_result, max_rnd_shr_label)
tests.append(max_rnd_shr_test)


max_rnd_halving_add_test_name = "typed:unsigned-vec-rounding_halving_add"
max_rnd_halving_add_expr = "(repair-umax_dsl (typed:unsigned-vec-rounding_halving_add (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) (typed:unsigned-vec-rounding_halving_add (reg (bv #x00 8)) (reg (bv #x00 8)) 8 64) 8 64)"
max_rnd_halving_add_expected_result = False
max_rnd_halving_add_label = "_mm256_max_epu64+typed:unsigned-vec-rounding_halving_add"
max_rnd_halving_add_test = TestObj( max_rnd_halving_add_test_name, max_rnd_halving_add_expr, max_rnd_halving_add_expected_result, max_rnd_halving_add_label)

tests.append(max_rnd_halving_add_test)




mulhi_div_test_desc = {
    "_mm512_mulhi_epu16+typed:signed-vec-div": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm512_mulhi_epu16",
                "output_expression": "(repair-umul_dsl (repair-umul_dsl (reg (bv #x00 8)) (reg (bv #x01 8)) 32 64) (typed:signed-vec-div (reg (bv #x01 8)) (reg (bv #x01 8)) 64 64) 64 64)",
                "synth_expression": "(_mm512_mulhi_epu16_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 128 128 0 128 32 0 0 64 0 0)"
            }
        }
    ]
}

# Division operation formal semantics has a special case conditional for handling when the division is by 0. This
# causes the result to be non-concrete and therefore becomes a meaningful usage
mulhi_div_test = test_generator_helper(mulhi_div_test_desc, True)


tests.append(mulhi_div_test)


add_shr_test_desc = {
"_mm_add_si64+typed:unsigned-vec-shr": [
        {
            "property_name": "RepairRelavanceV3",
            "property": {
                "candidate": "_mm_add_si64",
                "output_expression": "(repair-add_dsl (repair-add_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x01 8)) 8 64) 8 64)",
                "synth_expression": "(_mm_add_si64_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 64 -1 0 0)"
            }
        }
    ]

}

add_shr_test = test_generator_helper(add_shr_test_desc, False)
tests.append(add_shr_test)



pslld_vec_mul_desc = {
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
    ]

}


pslld_vec_mul_test = test_generator_helper(pslld_vec_mul_desc, True)
tests.append(pslld_vec_mul_test)
