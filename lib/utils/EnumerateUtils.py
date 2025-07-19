from utils.DSLInstructionUtils import *
from utils.ConcretizeUtils import *






def create_exhaustive_expressions_generator_helper_v2(dsl_list,  expr_depth = 1, max_leaves = None):


    copy_fn = copy.deepcopy

    if expr_depth == 0:
        yield copy_fn(Reg("0_placeholder", 8, 8))
    else:
        relavent_ctx = []
        for dsl_inst in dsl_list:


            accounted_for = []
            inst_relavent_ctx = []
            LEGACY = True
            if LEGACY:
                for ctx in dsl_inst.contexts:
                    num_args = get_num_symbolic_args(ctx)
                    if num_args in accounted_for:
                        continue
                    else:
                        accounted_for.append(num_args)
                        inst_relavent_ctx.append(ctx)
            else:
                for ctx in dsl_inst.contexts:
                    num_args = get_num_symbolic_args(ctx)
                    same_inputs = len(set([arg.size for arg in ctx.context_args if isinstance(arg,BitVector)])) == 1
                    key = (num_args, same_inputs)
                    if key in accounted_for:
                        continue
                    else:
                        accounted_for.append(key)
                        inst_relavent_ctx.append(ctx)

            relavent_ctx += inst_relavent_ctx
        relavent_ctx = sorted(relavent_ctx, key = lambda x : get_num_symbolic_args(x))


        # TEMP Moving down
        yield copy_fn(Reg("1_placeholder", 8, 8))

        def is_expr_valid(expr):
            if max_leaves is None:
                return True
            else:
                # Using non-unique registers count as register number
                # isn't aassigned yet
                return len(get_context_registers(expr)) <= max_leaves


        for rctx in relavent_ctx:
            get_arg = lambda j : rctx.context_args[j]
            symbolic_indices = []
            generators = []

            rctx_input_sizes = get_possible_input_sizes_of_eq_class(rctx, dsl_list)

            for idx, c_arg in enumerate(rctx.context_args):
                if isinstance(c_arg, BitVector):
                    symbolic_indices.append(idx)


            if len(symbolic_indices) == 5:

                generator_0 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)
                for expr0 in generator_0:

                    expr0_out_sizes = get_possible_output_sizes_of_eq_class(expr0, dsl_list)
                    # Short circuit any expressions which can't be bound together anyways
                    if not isinstance(expr0, Reg) and len(expr0_out_sizes.intersection(rctx_input_sizes)) == 0:
                        continue

                    if not is_expr_valid(expr0):
                        continue


                    generator_1 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)
                    for expr1 in generator_1:


                        expr1_out_sizes = get_possible_output_sizes_of_eq_class(expr1, dsl_list)
                        # Short circuit any expressions which can't be bound together anyways
                        if not isinstance(expr1, Reg) and len(expr1_out_sizes.intersection(rctx_input_sizes)) == 0:
                            continue

                        if not is_expr_valid(expr1):
                            continue



                        generator_2 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)
                        for expr2 in generator_2:

                            expr2_out_sizes = get_possible_output_sizes_of_eq_class(expr2, dsl_list)
                            # Short circuit any expressions which can't be bound together anyways
                            if not isinstance(expr2, Reg) and  len(expr2_out_sizes.intersection(rctx_input_sizes)) == 0:
                                continue

                            if not is_expr_valid(expr2):
                                continue

                            generator_3 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)
                            for expr3 in generator_3:

                                expr3_out_sizes = get_possible_output_sizes_of_eq_class(expr3, dsl_list)
                                # Short circuit any expressions which can't be bound together anyways
                                if not isinstance(expr3, Reg) and  len(expr3_out_sizes.intersection(rctx_input_sizes)) == 0:
                                    continue

                                if not is_expr_valid(expr3):
                                    continue

                                generator_4 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)
                                for expr4 in generator_4:

                                    expr4_out_sizes = get_possible_output_sizes_of_eq_class(expr4, dsl_list)
                                    # Short circuit any expressions which can't be bound together anyways
                                    if not isinstance(expr4, Reg) and  len(expr3_out_sizes.intersection(rctx_input_sizes)) == 0:
                                        continue

                                    if not is_expr_valid(expr4):
                                        continue

                                    copied_rctx = copy_fn(rctx)
                                    copied_rctx.context_args[symbolic_indices[0]] = expr0
                                    copied_rctx.context_args[symbolic_indices[1]] = expr1
                                    copied_rctx.context_args[symbolic_indices[2]] = expr2
                                    copied_rctx.context_args[symbolic_indices[3]] = expr3
                                    copied_rctx.context_args[symbolic_indices[4]] = expr4
                                    yield copied_rctx
            elif len(symbolic_indices) == 4:

                generator_0 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)
                for expr0 in generator_0:

                    expr0_out_sizes = get_possible_output_sizes_of_eq_class(expr0, dsl_list)
                    # Short circuit any expressions which can't be bound together anyways
                    if not isinstance(expr0, Reg) and len(expr0_out_sizes.intersection(rctx_input_sizes)) == 0:
                        continue

                    if not is_expr_valid(expr0):
                        continue


                    generator_1 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)
                    for expr1 in generator_1:


                        expr1_out_sizes = get_possible_output_sizes_of_eq_class(expr1, dsl_list)
                        # Short circuit any expressions which can't be bound together anyways
                        if not isinstance(expr1, Reg) and len(expr1_out_sizes.intersection(rctx_input_sizes)) == 0:
                            continue

                        if not is_expr_valid(expr1):
                            continue



                        generator_2 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)
                        for expr2 in generator_2:

                            expr2_out_sizes = get_possible_output_sizes_of_eq_class(expr2, dsl_list)
                            # Short circuit any expressions which can't be bound together anyways
                            if not isinstance(expr2, Reg) and  len(expr2_out_sizes.intersection(rctx_input_sizes)) == 0:
                                continue

                            if not is_expr_valid(expr2):
                                continue

                            generator_3 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)
                            for expr3 in generator_3:

                                expr3_out_sizes = get_possible_output_sizes_of_eq_class(expr3, dsl_list)
                                # Short circuit any expressions which can't be bound together anyways
                                if not isinstance(expr3, Reg) and  len(expr3_out_sizes.intersection(rctx_input_sizes)) == 0:
                                    continue

                                if not is_expr_valid(expr3):
                                    continue



                                copied_rctx = copy_fn(rctx)
                                copied_rctx.context_args[symbolic_indices[0]] = expr0
                                copied_rctx.context_args[symbolic_indices[1]] = expr1
                                copied_rctx.context_args[symbolic_indices[2]] = expr2
                                copied_rctx.context_args[symbolic_indices[3]] = expr3
                                yield copied_rctx
            elif len(symbolic_indices) == 3:

                generator_0 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)
                for expr0 in generator_0:

                    expr0_out_sizes = get_possible_output_sizes_of_eq_class(expr0, dsl_list)
                    # Short circuit any expressions which can't be bound together anyways
                    if not isinstance(expr0, Reg) and len(expr0_out_sizes.intersection(rctx_input_sizes)) == 0:
                        continue

                    if not is_expr_valid(expr0):
                        continue


                    generator_1 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)
                    for expr1 in generator_1:

                        expr1_out_sizes = get_possible_output_sizes_of_eq_class(expr1, dsl_list)
                        # Short circuit any expressions which can't be bound together anyways
                        if not isinstance(expr1, Reg) and len(expr1_out_sizes.intersection(rctx_input_sizes)) == 0:
                            continue

                        if not is_expr_valid(expr1):
                            continue

                        generator_2 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)

                        for expr2 in generator_2:

                            expr2_out_sizes = get_possible_output_sizes_of_eq_class(expr2, dsl_list)
                            # Short circuit any expressions which can't be bound together anyways
                            if not isinstance(expr2, Reg) and len(expr2_out_sizes.intersection(rctx_input_sizes)) == 0:
                                continue

                            if not is_expr_valid(expr2):
                                continue


                            copied_rctx = copy_fn(rctx)
                            copied_rctx.context_args[symbolic_indices[0]] = expr0
                            copied_rctx.context_args[symbolic_indices[1]] = expr1
                            copied_rctx.context_args[symbolic_indices[2]] = expr2
                            yield copied_rctx

            elif len(symbolic_indices) == 2:

                generator_0 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)

                for expr0 in generator_0:

                    expr0_out_sizes = get_possible_output_sizes_of_eq_class(expr0, dsl_list)
                    # Short circuit any expressions which can't be bound together anyways
                    if not isinstance(expr0, Reg) and len(expr0_out_sizes.intersection(rctx_input_sizes)) == 0:
                        continue

                    if not is_expr_valid(expr0):
                        continue

                    generator_1 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)
                    for expr1 in generator_1:


                        expr1_out_sizes = get_possible_output_sizes_of_eq_class(expr1, dsl_list)
                        # Short circuit any expressions which can't be bound together anyways
                        if not isinstance(expr1, Reg) and len(expr1_out_sizes.intersection(rctx_input_sizes)) == 0:
                            continue

                        if not is_expr_valid(expr1):
                            continue

                        copied_rctx = copy_fn(rctx)
                        copied_rctx.context_args[symbolic_indices[0]] = expr0
                        copied_rctx.context_args[symbolic_indices[1]] = expr1
                        yield copied_rctx

            elif len(symbolic_indices) == 1:
                generator_0 = create_exhaustive_expressions_generator_helper_v2(dsl_list,   expr_depth = expr_depth - 1, max_leaves = max_leaves)
                for expr0 in generator_0:

                    expr0_out_sizes = get_possible_output_sizes_of_eq_class(expr0, dsl_list)
                    # Short circuit any expressions which can't be bound together anyways
                    if not isinstance(expr0, Reg) and len(expr0_out_sizes.intersection(rctx_input_sizes)) == 0:
                        continue

                    if not is_expr_valid(expr0):
                        continue

                    copied_rctx = copy_fn(rctx)
                    copied_rctx.context_args[symbolic_indices[0]] = expr0
                    yield copied_rctx
            else:
                print(len(symbolic_indices))
                print(rctx.name)
                print(rctx.emit_context_expr_string())
                assert False, "Unsupported"




def create_exhaustive_expressions_generator_v2(dsl_list, expr_depth, output_size = None, max_leaves = None):
    assert not output_size is None, "Require passing it output size for version 2 generator"
    depth_expressions_generator = create_exhaustive_expressions_generator_helper_v2(dsl_list, expr_depth = expr_depth, max_leaves = max_leaves)

    for expr in depth_expressions_generator:
        copied_expr = expr
        new_expr, discard = set_reg_names_exprs_helper(copied_expr, 0)

        if isinstance(expr, Context):
            #print("NEW EPXR")
            #print("\n\n",new_expr.emit_context_expr_string())
            pass




        if does_valid_concretization_exist(new_expr, output_size, dsl_list):
            #valid_conc = get_valid_concretization(new_expr, output_size, dsl_list)
            #assert not valid_conc is None, "Valid concretization should exist"
            #yield valid_conc

            yield new_expr
