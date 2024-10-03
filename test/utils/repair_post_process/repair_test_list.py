
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
