from Ops import *
from Canonical import is_expression_canonical
from TOMLEmitter import emit_toml_str
from PIM_API_UTILS import PIM_PROG
import sys
import pickle

def legalize_template_registers(expr_template):
    regs = expr_template.get_registers()
    for idx, reg in enumerate(regs):
        reg.set_index(idx)


def legalize_template_IDs(expr_template):
    opnd_list = expr_template.get_nested_operands()

    for idx, opnd in enumerate(opnd_list):
        opnd.ID = idx




def enumerate_expr(output_size, output_bitwidth, depth, base_name):

    valid_counter = 0

    visited = set()
    for expr_template in enumerate_expr_helper(output_size, output_bitwidth, depth):
        #if expr_template.get_depth() != depth:
        if expr_template.get_depth() < depth:
            continue

        if not is_expression_canonical(expr_template):
            continue

        regs = expr_template.get_registers()

        MAX_REGS = 5
        if len(regs) > MAX_REGS:
            continue

        expr_str = expr_template.print_op()

        if expr_str in visited:
            continue
        visited.add(expr_str)

        function_name = f"{base_name}_fused_pim_op_{valid_counter}"
        loop = LoopOp(0, expr_template)
        func_wrapper = FunctionOp(0, function_name, loop)

        legalize_template_registers(func_wrapper)
        legalize_template_IDs(func_wrapper)

        yield func_wrapper

        valid_counter += 1








def enumerate_expr_helper(output_size, output_bitwidth, depth):
    assert output_bitwidth in [1,8,16,32,64], f"Unsupported output bitwidth! Size {output_size}, bitwidth {output_bitwidth}"

    if output_size < 8 or (output_size % 2 != 0):
        return []

    comparison_op_classes = [LTOp, EQOp] if True else []
    select_op_classes = [SelectOp] if True else []
    binary_op_classes = [AddOp, SubOp, MulOp, DivOp, MaxOp, MinOp, AndOp, OrOp, XorOp] if True else []
    unary_op_classes = [BroadcastOp, ZeroExtendOp, SignExtendOp, TruncateOp, NotOp] if True else []
    shift_op_classes = [RightShiftOp, LeftShiftOp] if True else []

    # We will set the ID and index seperately
    place_holder_reg = Register(0, 0, bitwidth=output_bitwidth, size = output_size)

    BROADCAST_LEAF = False
    if depth == 0:
        yield place_holder_reg
        if BROADCAST_LEAF and output_size // output_bitwidth != 1  :
            scalar_reg = Register(0, 0, bitwidth=output_bitwidth, size = output_bitwidth)
            factor = output_size // output_bitwidth
            yield BroadcastOp(0, scalar_reg , factor)
        return
    else:
        yield place_holder_reg


    for unary_op_cls in unary_op_classes:
        if output_bitwidth == 1:
            break
        if not unary_op_cls.supports_scalar_ops() and output_size // output_bitwidth == 1:
            continue
        required_input_sizes = unary_op_cls.get_input_sizes_for_output_size(output_size, output_bitwidth)
        required_bitwidths = unary_op_cls.get_input_bitwidth_for_output_bitwidth(output_size, output_bitwidth)

        if required_bitwidths[0] not in [8,16,32,64]:
            continue
        for opnd_option_A in enumerate_expr_helper(required_input_sizes[0], required_bitwidths[0], depth -1):
            if unary_op_cls is  BroadcastOp:
                factor = output_size // output_bitwidth
                yield unary_op_cls(0, opnd_option_A, factor)
            # Avoid double negation
            elif unary_op_cls is NotOp  and isinstance(opnd_option_A, NotOp) :
                continue
            # Avoid extend then truncate
            elif unary_op_cls is TruncateOp  and isinstance(opnd_option_A, ExtendOp) :
                continue
            elif unary_op_cls is ZeroExtendOp or unary_op_cls is SignExtendOp or unary_op_cls is TruncateOp:
                yield unary_op_cls(0, opnd_option_A)
            else:
                yield unary_op_cls(0, opnd_option_A)

    for shift_op_cls in shift_op_classes:
        if output_bitwidth == 1:
            break
        if not shift_op_cls.supports_scalar_ops() and output_size // output_bitwidth == 1:
            continue
        required_input_sizes = shift_op_cls.get_input_sizes_for_output_size(output_size, output_bitwidth)
        required_bitwidths = shift_op_cls.get_input_bitwidth_for_output_bitwidth(output_size, output_bitwidth)



        for opnd_option_A in enumerate_expr_helper(required_input_sizes[0], required_bitwidths[0], depth -1):
            for opnd_option_B in enumerate_expr_helper(required_input_sizes[1], required_bitwidths[1], depth -1):
                yield shift_op_cls(0, opnd_option_A, opnd_option_B)



    for binary_op_cls in binary_op_classes:
        if output_bitwidth == 1:
            break
        if not binary_op_cls.supports_scalar_ops() and output_size // output_bitwidth == 1:
            continue
        required_input_sizes = binary_op_cls.get_input_sizes_for_output_size(output_size, output_bitwidth)
        required_bitwidths = binary_op_cls.get_input_bitwidth_for_output_bitwidth(output_size, output_bitwidth)



        for opnd_option_A in enumerate_expr_helper(required_input_sizes[0], required_bitwidths[0], depth -1):
            for opnd_option_B in enumerate_expr_helper(required_input_sizes[1], required_bitwidths[1], depth -1):
                yield binary_op_cls(0, opnd_option_A, opnd_option_B)

    for select_op_cls in select_op_classes:
        if output_bitwidth == 1:
            break
        if not select_op_cls.supports_scalar_ops() and output_size // output_bitwidth == 1:
            continue
        required_input_sizes = select_op_cls.get_input_sizes_for_output_size(output_size, output_bitwidth)
        required_bitwidths = select_op_cls.get_input_bitwidth_for_output_bitwidth(output_size, output_bitwidth)




        for opnd_option_A in enumerate_expr_helper(required_input_sizes[0], required_bitwidths[0], depth -1):
            for opnd_option_B in enumerate_expr_helper(required_input_sizes[1], required_bitwidths[1], depth -1):
                for opnd_option_C in enumerate_expr_helper(required_input_sizes[2], required_bitwidths[2], depth -1):
                    yield select_op_cls(0, opnd_option_A, opnd_option_B, opnd_option_C)

    for comparison_op_cls in comparison_op_classes:

        if not comparison_op_cls.supports_scalar_ops() and output_size // output_bitwidth == 1:
            continue

        if output_bitwidth != ComparisonBinaryOp.comp_bitwidth:
            continue

        lanes = output_size // output_bitwidth

        valid_comp_bw = [8,16,32]

        for bw in valid_comp_bw:
            required_input_sizes = [int(lanes * bw)] * 2
            required_bitwidths = [bw, bw]

            for opnd_option_A in enumerate_expr_helper(required_input_sizes[0], required_bitwidths[0], depth -1):
                for opnd_option_B in enumerate_expr_helper(required_input_sizes[1], required_bitwidths[1], depth -1):
                    yield comparison_op_cls(0, opnd_option_A, opnd_option_B)


    return






def test_enumeration():



    depths = [1,2]
    vector_sizes = [64, 128]
    bitwidths = [1, 8, 16, 32]


    combinations = []

    for depth in depths:
        for vsize in vector_sizes:
            for bw in bitwidths:
                if vsize // bw == 1:
                    continue
                combinations.append((depth,vsize, bw))

    generators = []

    for idx, comb in enumerate(combinations):
        base_name = f"comb_{idx}"
        test_depth = comb[0]
        vsize = comb[1]
        bw = comb[2]

        gen = enumerate_expr(vsize, bw, test_depth, base_name)
        generators.append(gen)



    context = {"loop_index_var": "idx"}

    collection_name = "test_enum_1"
    with open("auto.toml", "w+") as TomlFile:
        TomlFile.write(f"[{collection_name}]\n")

    with open("fused_lower.cpp", "w+") as CppFile:
        CppFile.write("// Automatically generated file\n")
        CppFile.write("#include \"libpimeval.h\"\n")
        CppFile.write("#include <cstdio>\n")
        CppFile.write("#ifndef VF \n")
        CppFile.write("#define VF 0\n")
        CppFile.write("#endif \n ")

    with open("unfused_lower.cpp", "w+") as CppFile:
        CppFile.write("// Automatically generated file\n")
        CppFile.write("#include \"libpimeval.h\"\n")
        CppFile.write("#include <cstdio>\n")
        CppFile.write("#ifndef VF \n")
        CppFile.write("#define VF 0\n")
        CppFile.write("#endif  \n")

    with open("get_perf_stats.cpp", "w+") as CppFile:
        CppFile.write("// Automatically generated file\n")
        CppFile.write("#include \"libpimeval.h\"\n")
        CppFile.write("void get_perf(){\n")

    with open("rewrite_rules.txt", "w+") as TxtFile:
        pass
    from itertools import chain

    count = 0
    operators = []
    op_map = {}
    for expr in chain(*generators):
        count +=1




        print("# =================")
        #defns, context = expr.emit_semantics_pseudocode(context)
        print(expr.print_op())
        prog = PIM_PROG(expr, func_name = expr.name)

        with open("unfused_lower.cpp", "a+") as CppFile:
            CppFile.write("\n\n/*\n")
            CppFile.write(expr.print_op())
            CppFile.write("*/\n")
            CppFile.write(prog.emit_pim_unfused_prog_cpp()+"\n")
            CppFile.write(prog.emit_benchmark_method()+"\n")

        with open("fused_lower.cpp", "a+") as CppFile:
            CppFile.write("\n\n/*\n")
            CppFile.write(expr.print_op())
            CppFile.write("*/\n")
            CppFile.write(prog.emit_pim_fused_prog_cpp()+"\n")
            CppFile.write(prog.emit_benchmark_method()+"\n")

        with open("rewrite_rules.txt", "a+") as TxtFile:
            try:
                rewrite_rule = prog.emit_rewrite_rule_by_construction(expr, op_map, root = True)
                if rewrite_rule is not None:
                    TxtFile.write(rewrite_rule)
                    TxtFile.write("\n")
            except Exception as e:
                pass

        with open("get_perf_stats.cpp", "a+") as CppFile:
            CppFile.write(f"{prog.get_bench_name()}();\n")
        #print(defns[0])
        toml_str = emit_toml_str(expr, collection_name)
        with open("auto.toml", "a+") as TomlFile:
            TomlFile.write(toml_str+"\n")

        operators.append(expr)
        if False and  count == 100:
            #sys.exit()
            break
        #print(toml_str)


    # MANUAL

    MANUAL_EXPRESSIONS = []

    for vectsize in [128, 256]:
        for prec in [8,16,32]:
            name = f"test_enum_custom_scaled_add_i{prec}_s{vectsize}"
            factor = vectsize // prec
            SCALED_ADD_I8 = AddOp(0,
                                  MulOp(1,
                                        Register(2, 0, bitwidth = prec, size = vectsize),
                                        BroadcastOp(3,
                                                Register(4, 1, bitwidth = prec, size = prec),
                                                factor
                                                    )
                                        ),
                                  Register(5, 2, bitwidth = prec, size = vectsize)
                                  )
            Loop = LoopOp(
                6, SCALED_ADD_I8
            )

            Func = FunctionOp(7, name, Loop)
            MANUAL_EXPRESSIONS.append(Func)

    combinations = []

    for depth in depths:
        for vsize in vector_sizes+[512, 1024]:
            for bw in bitwidths:
                if vsize // bw == 1:
                    continue
                combinations.append((depth,vsize, bw))


    generators = []

    for idx, comb in enumerate(combinations):
        base_name = f"manual_comb_{idx}"
        test_depth = comb[0]
        vsize = comb[1]
        bw = comb[2]

        gen = enumerate_expr(vsize, bw, test_depth, base_name)
        generators.append(gen)

    def select_32bit(Op):
        if not isinstance(Op, SelectOp):
            return False
        return Op.operands[1].bitwidth == 32

    for expr in chain(*generators):
        if OpBoolVisitor(expr, select_32bit):
            str_ = expr.print_op()
            print(str_)
            MANUAL_EXPRESSIONS.append(expr)






    for expr in MANUAL_EXPRESSIONS:
        count +=1




        print("# =================")
        #defns, context = expr.emit_semantics_pseudocode(context)
        print(expr.print_op())
        prog = PIM_PROG(expr, func_name = expr.name)

        with open("unfused_lower.cpp", "a+") as CppFile:
            CppFile.write("\n\n/*\n")
            CppFile.write(expr.print_op())
            CppFile.write("*/\n")
            CppFile.write(prog.emit_pim_unfused_prog_cpp()+"\n")
            CppFile.write(prog.emit_benchmark_method()+"\n")

        with open("fused_lower.cpp", "a+") as CppFile:
            CppFile.write("\n\n/*\n")
            CppFile.write(expr.print_op())
            CppFile.write("*/\n")
            CppFile.write(prog.emit_pim_fused_prog_cpp()+"\n")
            CppFile.write(prog.emit_benchmark_method()+"\n")

        with open("rewrite_rules.txt", "a+") as TxtFile:
            try:
                rewrite_rule = prog.emit_rewrite_rule_by_construction(expr, op_map, root = True)
                if rewrite_rule is not None:
                    TxtFile.write(rewrite_rule)
                    TxtFile.write("\n")
            except Exception as e:
                pass

        with open("get_perf_stats.cpp", "a+") as CppFile:
            CppFile.write(f"{prog.get_bench_name()}();\n")
        #print(defns[0])
        toml_str = emit_toml_str(expr, collection_name)
        with open("manual_auto.toml", "a+") as TomlFile:
            TomlFile.write(toml_str+"\n")

        operators.append(expr)
        #print(toml_str)


    # =============




    with open("get_perf_stats.cpp", "a+") as CppFile:
        CppFile.write("}")


    print(f"Wrote total {count}")
    with open('fused_ops.pickle', 'wb') as handle:
        pickle.dump(operators, handle, protocol=pickle.HIGHEST_PROTOCOL)


def test_enumeration_repeat():



    depths = [1,2]
    vector_sizes = [64, 128, 256, 512 ]
    bitwidths = [1, 8, 16, 32]


    combinations = []

    for depth in depths:
        for vsize in vector_sizes:
            for bw in bitwidths:
                if vsize // bw == 1:
                    continue
                combinations.append((depth,vsize, bw))

    generators = []

    for idx, comb in enumerate(combinations):
        base_name = f"comb_{idx}"
        test_depth = comb[0]
        vsize = comb[1]
        bw = comb[2]

        gen = enumerate_expr(vsize, bw, test_depth, base_name)
        generators.append(gen)



    context = {"loop_index_var": "idx"}

    collection_name = "test_enum_2"
    with open("auto.toml", "w+") as TomlFile:
        TomlFile.write(f"[{collection_name}]\n")

    with open("fused_lower.cpp", "w+") as CppFile:
        CppFile.write("// Automatically generated file\n")
        CppFile.write("#include \"libpimeval.h\"\n")
        CppFile.write("#include <cstdio>\n")
        CppFile.write("#ifndef VF \n")
        CppFile.write("#define VF 0\n")
        CppFile.write("#endif \n ")

    with open("unfused_lower.cpp", "w+") as CppFile:
        CppFile.write("// Automatically generated file\n")
        CppFile.write("#include \"libpimeval.h\"\n")
        CppFile.write("#include <cstdio>\n")
        CppFile.write("#ifndef VF \n")
        CppFile.write("#define VF 0\n")
        CppFile.write("#endif  \n")

    with open("get_perf_stats.cpp", "w+") as CppFile:
        CppFile.write("// Automatically generated file\n")
        CppFile.write("#include \"libpimeval.h\"\n")
        CppFile.write("void get_perf(){\n")

    with open("rewrite_rules.txt", "w+") as TxtFile:
        pass
    from itertools import chain

    count = 0
    operators = []
    op_map = {}
    for expr in chain(*generators):
        count +=1




        print("# =================")
        #defns, context = expr.emit_semantics_pseudocode(context)
        print(expr.print_op())
        prog = PIM_PROG(expr, func_name = expr.name)

        with open("unfused_lower.cpp", "a+") as CppFile:
            CppFile.write("\n\n/*\n")
            CppFile.write(expr.print_op())
            CppFile.write("*/\n")
            CppFile.write(prog.emit_pim_unfused_prog_cpp()+"\n")
            CppFile.write(prog.emit_benchmark_method()+"\n")

        with open("fused_lower.cpp", "a+") as CppFile:
            CppFile.write("\n\n/*\n")
            CppFile.write(expr.print_op())
            CppFile.write("*/\n")
            CppFile.write(prog.emit_pim_fused_prog_cpp()+"\n")
            CppFile.write(prog.emit_benchmark_method()+"\n")

        with open("rewrite_rules.txt", "a+") as TxtFile:
            try:
                rewrite_rule = prog.emit_rewrite_rule_by_construction(expr, op_map, root = True)
                if rewrite_rule is not None:
                    TxtFile.write(rewrite_rule)
                    TxtFile.write("\n")
            except Exception as e:
                pass

        with open("get_perf_stats.cpp", "a+") as CppFile:
            CppFile.write(f"{prog.get_bench_name()}();\n")
        #print(defns[0])
        toml_str = emit_toml_str(expr, collection_name)
        with open("auto.toml", "a+") as TomlFile:
            TomlFile.write(toml_str+"\n")

        operators.append(expr)
        if False and  count == 100:
            #sys.exit()
            break
        #print(toml_str)


    # MANUAL

    MANUAL_EXPRESSIONS = []

    for vectsize in [128, 256]:
        for prec in [8,16,32]:
            name = f"test_enum_custom_scaled_add_i{prec}_s{vectsize}"
            factor = vectsize // prec
            SCALED_ADD_I8 = AddOp(0,
                                  MulOp(1,
                                        Register(2, 0, bitwidth = prec, size = vectsize),
                                        BroadcastOp(3,
                                                Register(4, 1, bitwidth = prec, size = prec),
                                                factor
                                                    )
                                        ),
                                  Register(5, 2, bitwidth = prec, size = vectsize)
                                  )
            Loop = LoopOp(
                6, SCALED_ADD_I8
            )

            Func = FunctionOp(7, name, Loop)
            MANUAL_EXPRESSIONS.append(Func)








    for expr in MANUAL_EXPRESSIONS:
        count +=1

        print("# =================")
        #defns, context = expr.emit_semantics_pseudocode(context)
        print(expr.print_op())
        prog = PIM_PROG(expr, func_name = expr.name)

        with open("unfused_lower.cpp", "a+") as CppFile:
            CppFile.write("\n\n/*\n")
            CppFile.write(expr.print_op())
            CppFile.write("*/\n")
            CppFile.write(prog.emit_pim_unfused_prog_cpp()+"\n")
            CppFile.write(prog.emit_benchmark_method()+"\n")

        with open("fused_lower.cpp", "a+") as CppFile:
            CppFile.write("\n\n/*\n")
            CppFile.write(expr.print_op())
            CppFile.write("*/\n")
            CppFile.write(prog.emit_pim_fused_prog_cpp()+"\n")
            CppFile.write(prog.emit_benchmark_method()+"\n")

        with open("rewrite_rules.txt", "a+") as TxtFile:
            try:
                rewrite_rule = prog.emit_rewrite_rule_by_construction(expr, op_map, root = True)
                if rewrite_rule is not None:
                    TxtFile.write(rewrite_rule)
                    TxtFile.write("\n")
            except Exception as e:
                pass

        with open("get_perf_stats.cpp", "a+") as CppFile:
            CppFile.write(f"{prog.get_bench_name()}();\n")
        #print(defns[0])
        toml_str = emit_toml_str(expr, collection_name)
        with open("auto.toml", "a+") as TomlFile:
            TomlFile.write(toml_str+"\n")

        operators.append(expr)
        #print(toml_str)


    # =============




    with open("get_perf_stats.cpp", "a+") as CppFile:
        CppFile.write("}")


    print(f"Wrote total {count}")
    with open('fused_ops.pickle', 'wb') as handle:
        pickle.dump(operators, handle, protocol=pickle.HIGHEST_PROTOCOL)
if __name__ == "__main__":
    #test_enumeration()
    test_enumeration_repeat()
