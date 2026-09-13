from compiler.Compiler import *
import concurrent.futures
import subprocess as sb
from compiler.EggLogCompiler import EggLogCompiler
from utils.DSLInstructionUtils import *
from utils.ReadDSL import read_string_to_dsl
from utils.EggLogUtils import *
import sys
import time
import os
import shutil
import pandas as pd


class PIMFusedCompiler(EggLogCompiler):

    def __init__(self, patterns, src_dsl_list = [], target_dsl_list = [], run_iterations = 10, egg_pkg_path = None, llvm_so_path = None, llvm_flags = [], tests = [],  intrinsics_file = None, hydride_root_path = None, llvm_out_file_name = "llvm.out", prune_patterns = False, parallel = True, skip_axioms = False, extended_dsl_list = [], output_file_path = "pim_fused_lowering.h", do_print_output_cost = True, cost_model_drop_poor_fusions = False):
        if "MISAAL_NO_FUSION" in os.environ:
            patterns = self.get_unfused_pim_patterns(patterns)

        super().__init__(patterns, src_dsl_list = src_dsl_list, target_dsl_list = target_dsl_list, run_iterations = run_iterations,  egg_pkg_path = egg_pkg_path, prune_patterns = prune_patterns, skip_axioms = skip_axioms)
        self.energy_optimize = False
        self.llvm_out_file_name = llvm_out_file_name
        self.llvm_so_path = llvm_so_path
        self.llvm_flags = llvm_flags
        self.output_file_path = output_file_path
        self.intrinsics_file = intrinsics_file
        self.hydride_root_path = hydride_root_path
        self.parallel = parallel
        self.input_tests = tests
        self.pool_size = 6
        self.measure_egglog_time = False
        self.egglog_results = []
        self.extended_dsl_list = extended_dsl_list
        self.cost_model_drop_poor_fusions = cost_model_drop_poor_fusions
        self.cost_dict = self.read_cost_dict_from_file(os.getenv("COST_FILE_CSV_NAME"))
        self.do_print_output_cost = do_print_output_cost
        self.used_pim_insts = set()
        sys.setrecursionlimit(5000)


    def update_used_pim_insts(self, expr):
        if isinstance(expr, Context):
            self.used_pim_insts.add(expr.name)

            for arg in expr.context_args:
                self.update_used_pim_insts(arg)

    def get_ifdef_command_pim_header(self):
        cmds = []
        for used_inst_name in self.used_pim_insts:
            used_inst_name = used_inst_name.split("_extended_size")[0]
            cmds.append(
                f"-Dinclude_{used_inst_name}"
            )

            if "comb" in used_inst_name:
                post_comb_name = used_inst_name.split("comb")[-1]
                cmds.append(
                    f"-Dinclude_comb{post_comb_name}"
                )
            if "test_enum_custom" in used_inst_name:
                post_comb_name = used_inst_name.split("test_enum_custom")[-1]
                cmds.append(
                    f"-Dinclude_test_enum_custom{post_comb_name}"
                )


        return cmds


    def print_output_cost(self, expr):

        def visitor(e):
            if not isinstance(e, Context):
                return 0

            child_sum = 0
            for child_e in e.context_args:
                child_sum += visitor(child_e)

            dsl_name = e.dsl_name.split("_dsl")[0]
            if dsl_name in self.cost_dict:
                return child_sum + self.cost_dict[dsl_name]
            else:
                return child_sum + 1

        if not isinstance(expr, Context):
            return

        total_cost = visitor(expr)


        print("Cost",total_cost, "for expr", expr.emit_context_expr_string())

    def get_unfused_pim_patterns(self, patterns):
        limited_patterns = []
        for pattern in patterns:
            exprs = [pattern.src_expr, pattern.target_expr]

            valid = True
            for expr in exprs:
                if not "typed-folded" in expr.emit_context_expr_string():
                    # check it's depth is one
                    if get_expr_depth(expr) != 1:
                        valid = False

            if valid:
                limited_patterns.append(pattern)
        print(f"Using {len(limited_patterns)} unfused patterns for PIM")
        return limited_patterns





    def get_reg_vector_type(self, reg):
        return "; (reg {}) <{} x i{}>".format(reg.index, reg.size // reg.precision,  reg.precision)


    def get_rosette_expression_str(self, input_expr ,output_expr, function_name):
        print("GET EXPRESSION STR ")
        expr_str = output_expr.emit_context_expr_string(add_output_type_info = True, use_reg_only = True, hydride_compatible = True)
        regs = get_unique_context_registers(input_expr)
        reg_type_info = [self.get_reg_vector_type(reg) for reg in regs]

        content = [
            "; "+ function_name,
        ]

        content += reg_type_info

        content += [expr_str]

        return "\n".join(content)


    def apply_rewrite(self, expr, compiler_functionality, reg_data_structures):

        if self.has_compiled_expr(expr):
            return get_compiled_expr(expr)

        key = expr.emit_context_expr_string()

        statements = []

        statements.append(compiler_functionality)
        statements += [defn for label, defn in reg_data_structures]

        num_regs = len(reg_data_structures)



        src_expr_name = "srcexpr"
        src_expr_egg = emit_expr_to_egg(expr)
        define_src_expr = emit_egg_define_var(src_expr_name, src_expr_egg)
        statements.append(define_src_expr)

        statements.append(emit_egg_run_iter(self.run_iterations))

        statements.append(emit_egg_extract_expr(src_expr_name))

        egg_file_name = get_random_tempfile_name() + ".egg"

        print("Creating egg file:\t", egg_file_name)

        with open(egg_file_name, "w+") as EggFile:
            EggFile.write("\n".join(statements))

        final_expression_str= self.execute_egglog_file(egg_file_name)

        print("EGG LOG PRODUCED", final_expression_str)
        output_expression = self.parse_egglog_output_expr(final_expression_str, num_regs)
        print("Post apply rewrite!")

        recompile_iter_count = 0
        while self.expr_contains_src_language(output_expression, "typed"):
            print("Expression contains src language, need additional eq sat")

            if isinstance(output_expression, Context):
                print(output_expression.emit_context_expr_string())

            if recompile_iter_count >= 3:
                print("Exceeded recompile iter count limit")
                sys.exit()
            output_expression = self.compile_expr(output_expression)
            recompile_iter_count +=1

        if self.do_print_output_cost:
            self.print_output_cost(output_expression)

        print("Adding rewriten expression to memo map")
        self.memo[key] = output_expression

        return output_expression







    def run_llvm_legalizer(self):
        # Does not actually use LLVM for legalization
        from PIM_API_UTILS import FusedPIMOpLegalizerHalide
        halide_legalizer_gen = FusedPIMOpLegalizerHalide(self.output_file_path, [], self.src_dsl_list + self.extended_dsl_list )


        lowered_progs = []

        for (input_expr, output_expr, function_name) in self.egglog_results:
            regs = get_unique_context_registers(input_expr)
            sizes = [reg.size for reg in regs]
            precs = [reg.precision for reg in regs]
            defn = halide_legalizer_gen.legalize(output_expr, function_name, sizes, precs)
            # WRAP IN PROFILE_COMPUTE
            compute_profile = f"#ifdef PROFILE_COMPUTE\n{defn}\n#endif"
            print(compute_profile)
            lowered_progs.append(compute_profile)

            defn = halide_legalizer_gen.legalize_profile_opt_data_movement(output_expr, function_name, sizes, precs)
            # WRAP IN PROFILE_COMPUTE
            data_movement_profile = f"#ifdef PROFILE_DATA_MOVEMENT\n{defn}\n#endif"
            print(data_movement_profile)
            lowered_progs.append(data_movement_profile)


        PIM_HEADER= """
/*
========================================================
This file is automatically generated, DO NOT EDIT!
========================================================
*/
        """

        with open(self.output_file_path, "w+") as CppHeader:
            CppHeader.write(PIM_HEADER+"\n")

            for prog in lowered_progs:
                CppHeader.write(prog+"\n")






    def compile_hydride(self):
        if len(self.input_tests) == 0:
            print("No expressions for MISAAL to compile")
            return

        #assert len(self.input_tests) != 0, "Expected Input tests"
        assert not self.output_file_path is None, "Expected Output file"


        # First preprocess all unique expressions in parallel to
        # overlap compilation of as many expressions as possible,
        # then compile expressions sequentially by memoizing

        PARALLEL = self.parallel

        start_time = time.time()
        unique_expressions = list(set([expr for (name, expr) in self.input_tests]))
        print(len(unique_expressions), "unique expressions to compile")

        def process_unique(i):
            print("PROCESS UNIQUE", i)
            input_expr_str = unique_expressions[i]
            print(input_expr_str)
            input_expr = read_string_to_dsl(input_expr_str, self.src_dsl_list)
            key = input_expr.emit_context_expr_string()
            output_expr = self.compile_expr(input_expr)


        if PARALLEL:
            pool = concurrent.futures.ThreadPoolExecutor(max_workers=self.pool_size)
            for i in range(len(unique_expressions)):
                pool.submit(process_unique, i)
            pool.shutdown(wait=True)
            print("Completed compiling pool...")
        else:
            print("Sequential Egg compilation")
            for i in range(len(unique_expressions)):
                process_unique(i)




        def process_test(i):
            print("PROCESS TEST", i)
            function_name , input_expr_str = self.input_tests[i]
            print(function_name)
            print(input_expr_str)
            input_expr = read_string_to_dsl(input_expr_str, self.src_dsl_list)
            key = input_expr.emit_context_expr_string()

            if self.has_compiled_expr(input_expr):
                print("Already compiled expression!")
                output_expr = self.get_compiled_expr(input_expr)
            else:
                print("Not compiled, need to compile!")
                output_expr = self.compile_expr(input_expr)

            output_type_def = (input_expr, output_expr, function_name) #self.get_rosette_expression_str(input_expr ,output_expr, function_name)
            print(output_type_def)

            results[i] = output_type_def

            self.update_used_pim_insts(output_expr)



        results = [0] * len(self.input_tests)

        for i in range(len(self.input_tests)):
            process_test(i)




        end_time = time.time()

        elapsed = end_time - start_time

        self.compile_times.append(("EggLogParallel", elapsed))

        print(results)
        self.egglog_results = results

        if False:
            cmds = self.get_ifdef_command_pim_header()
            print(cmds)
            print(" ".join(cmds))
            with open(f"{self.output_file_path}.defs", "w+") as DefFile:
                DefFile.write(" ".join(cmds))


        #with open(self.output_file_path, "w+") as LLVMInputFile:
        #    LLVMInputFile.write("\n".join(results))







    def parse_egglog_output_expr(self, expr_str, num_regs):

        expression_str = expr_str

        for i in range(num_regs):
            expression_str = expression_str.replace("(SYMBV {})".format(i), "(reg (bv {} 8))".format(i))

        print("expression_str", expression_str)
        # Use extended DSL LIST for compilation!
        output_expr = read_string_to_dsl(expression_str,  self.extended_dsl_list + self.src_dsl_list)
        print(output_expr.emit_context_expr_string())

        return output_expr

    def read_cost_dict_from_file(self, cost_file_csv_name):
        cost_dict = {}
        if os.environ.get("COST_FILE_CSV_NAME") is None:
            print("COST_FILE_CSV_NAME is not set, using default cost dict")
            return cost_dict
        else:
            print("COST_FILE_CSV_NAME is set, using cost dict from file")
            cost_file_csv_name = os.environ.get("COST_FILE_CSV_NAME")

        if not os.path.exists(cost_file_csv_name):
            print("Cost file does not exist, using default cost dict")
            assert False, "Cost file does not exist"
            return cost_dict


        with open(cost_file_csv_name, "r") as CostFile:
            df = pd.read_csv(CostFile)
            print(df)
            grouped = df.groupby('OP_NAME').agg({
                'Energy (mJ)_IMPROVEMENT': 'first',
                'Execution Time (ms)_IMPROVEMENT': 'first',
                'Energy (mJ)_FUSED': 'first',
                'Execution Time (ms)_FUSED': 'first',
                'Energy (mJ)_UNFUSED': 'first',
                'Execution Time (ms)_UNFUSED': 'first',
            }).reset_index()
            #     Column names: ['OP_NAME', 'Energy (mJ)_FUSED', 'Energy (mJ)_UNFUSED', 'Energy (mJ)_IMPROVEMENT', 'Execution Time (ms)_FUSED', 'Execution Time (ms)_UNFUSED', 'Execution Time (ms)_IMPROVEMENT', 'GOPS/W_FUSED', 'GOPS/W_UNFUSED', 'GOPS/W_IMPROVEMENT', '%R_FUSED', '%R_UNFUSED', '%R_IMPROVEMENT', '%W_FUSED', '%W_UNFUSED', '%W_IMPROVEMENT', '%L_FUSED', '%L_UNFUSED', '%L_IMPROVEMENT']
            # Convert to dictionary format
            METRIC_FIELD = ['Execution Time (ms)_FUSED', 'Energy (mJ)_FUSED'][1 if self.energy_optimize else 0]
            METRIC_IMPROVEMENT_FIELD = ['Execution Time (ms)_IMPROVEMENT', 'Energy (mJ)_IMPROVEMENT'][1 if self.energy_optimize else 0]
            print("Metric field:",METRIC_FIELD )
            for _, row in grouped.iterrows():
                op_name = f"test_enum_2_{row['OP_NAME']}"
                if op_name not in cost_dict:
                    cost_dict[op_name] = {}
                if self.cost_model_drop_poor_fusions and row[METRIC_IMPROVEMENT_FIELD] < 1.05:
                    # Discourague using fused variant if it does not provide significant improvements
                    # thus, only fusions which actually have some benefit will be targetted
                    cost_dict[op_name] = row[METRIC_FIELD] * 100
                else:
                    cost_dict[op_name] = row[METRIC_FIELD]
        # Now get the value of the smallest cost across all op_names and scale all op costs by 1/min_cost
        min_cost = min([v for v in cost_dict.values() if v != 0.0])
        #min_cost = 1.0
        print("Min cost value:", min_cost)
        for op_name in cost_dict:
            #cost_dict[op_name] = int(10* cost_dict[op_name] / min_cost)
            cost_dict[op_name] = int(1000* cost_dict[op_name] / min_cost)


        print("Pre Cost Dict")
        print(cost_dict)
        cost_dict = self.use_eq_class_min_cost(cost_dict)

        print("Cost Dict")
        print(cost_dict)
        print("Metric field:",METRIC_FIELD )
        return cost_dict

    def use_eq_class_min_cost_opt(self, cost_dict):
        updated_dict = {}
        for dsl_inst in self.src_dsl_list + self.target_dsl_list:
            if dsl_inst.name not in cost_dict:
                continue

            dsl_inst_name = dsl_inst.name


            MIN_INIT = 1000000000
            min_cost = MIN_INIT
            for ctx in dsl_inst.contexts:
                if ctx.name not in cost_dict or cost_dict[ctx.name] == 0:
                    continue
                elif not (ctx.in_precision == 32 or ctx.out_precision == 32):
                    continue
                else:
                    # TEMP
                    min_cost = min(min_cost, cost_dict[ctx.name])

            if min_cost == MIN_INIT:
                for ctx in dsl_inst.contexts:
                    if ctx.name not in cost_dict or cost_dict[ctx.name] == 0:
                        continue
                    else:
                        # TEMP
                        min_cost = min(min_cost, cost_dict[ctx.name])

            #if "scaled" in dsl_inst.name:
            #    min_cost = 1

            #for ctx in dsl_inst.contexts:
            #    updated_dict[ctx.name] = min_cost
            updated_dict[dsl_inst.name] = min_cost


        return updated_dict


    def use_eq_class_min_cost(self, cost_dict):
        return self.use_eq_class_min_cost_opt(cost_dict)
        visited_eq_classes = set()
        updated_dict = {}

        def get_eq_class(op):
            #print("Get eq_class for ",op)
            for dsl_inst in self.src_dsl_list + self.target_dsl_list:
                #print("-> Compare with", dsl_inst.name)
                if op == dsl_inst.name:
                    return dsl_inst
                for ctx in dsl_inst.contexts:

                    #print("--> Compare with", ctx.name)
                    if op == ctx.name:
                        return dsl_inst
            return None



        for key, value in cost_dict.items():


            dsl_inst = get_eq_class(key)


            if dsl_inst is None:
                continue
            dsl_inst_name = dsl_inst.name

            if dsl_inst_name in visited_eq_classes:
                continue
            visited_eq_classes.add(dsl_inst_name)

            #min_cost = 1000000000
            min_cost = 0.0
            for ctx in dsl_inst.contexts:
                if ctx.name not in cost_dict or cost_dict[ctx.name] == 0:
                    continue
                else:
                    # TEMP
                    min_cost = max(min_cost, cost_dict[ctx.name])

            #if "scaled" in dsl_inst.name:
            #    min_cost = 1

            #for ctx in dsl_inst.contexts:
            #    updated_dict[ctx.name] = min_cost
            updated_dict[dsl_inst.name] = min_cost

        return updated_dict






    def emit_pattern_matching_based_compiler(self, expr, swizzle_cost = 1):

        max_cost_dict = max([v for k,v in self.cost_dict.items()])+1

        egglog_decls = emit_egg_datatypes_two_dsl_variable_cost(self.src_dsl_list, self.target_dsl_list, input_cost = max(self.input_cost,max_cost_dict), output_cost = self.output_cost, swizzle_cost = swizzle_cost, cost_dict = self.cost_dict )

        test_patterns = self.patterns
        if self.prune_patterns:
            reachable_patterns = self.get_reachable_patterns_only(expr)

            print("Pruned patterns for expression ... # Patterns reduced from ", len(test_patterns), "to", len(reachable_patterns))
            test_patterns = reachable_patterns

        egglog_patterns = []
        for pattern in test_patterns:
            rewrite = emit_rewrite_expr(pattern.src_expr, pattern.target_expr, bidirectional = pattern.bidirectional)
            egglog_patterns.append(rewrite)


        axioms = ""
        if not self.skip_axioms:
            # Read in axioms file:
            with open(self.axioms_file, "r") as AxiomFile:
                axioms = AxiomFile.read()


        egg_log_desc = "\n".join([egglog_decls, axioms] + egglog_patterns)
        return egg_log_desc

