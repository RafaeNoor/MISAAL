

tests = []


# Condition 3
cond_3_name = "typed:vec-add"
cond_3_expr = "(typed:vec-add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)"
cond_3_expected_result = False
cond_3_label ="_mm_sub_si64+typed:vec-add"

# tests.append([cond_3_name, cond_3_expr, cond_3_expected_result, cond_3_label])



# Should pass

max_name = "typed:signed-vec-max"
max_expr = "(typed:signed-vec-max (reg (bv #x00 8)) (reg (bv #x01 8)) 64 64)"
max_expected_result = True
max_label = "_mm256_max_epu64+typed:signed-vec-max"
tests.append([max_name, max_expr, max_expected_result, max_label])
