int8x16_t foo(int8x16_t reg_0, int8x8_t reg_1, int8x8_t reg_2, int8x16_t reg_3, int8x16_t reg_4, int8x16_t reg_5){
	int16x8_t var_0;
	test_enum_1_comb_10_fused_pim_op_487(reg_1.data(), 8, reg_2.data(), 8, var_0.data(), 8);
	int8x16_t return_vec;
	test_enum_1_comb_9_fused_pim_op_127(reg_0.data(), 16, var_0.data(), 8, reg_3.data(), 16, reg_4.data(), 16, return_vec.data(), 16);
	return return_vec;
}



