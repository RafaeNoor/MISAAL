from compiler.Compiler import *
from utils.DSLInstructionUtils import *
from utils.EggLogUtils import *
import os
import copy
import subprocess as sb
import psutil
from utils.ReadDSL import read_string_to_dsl
import time

# Compiler using the EggLog DSL for applying rewrites

class EggLogCompiler(CompilerBase):

    def __init__(self, patterns, src_dsl_list = [], target_dsl_list = [], run_iterations = 10, egg_pkg_path = None, prune_patterns = False):
        super().__init__(patterns, src_dsl_list = src_dsl_list, target_dsl_list = target_dsl_list)
        self.egg_pkg_path = egg_pkg_path
        self.egg_manifest_path = os.path.join(self.egg_pkg_path, "Cargo.toml")
        self.egglog_bin = os.path.join(self.egg_pkg_path, "target","debug","egglog")
        self.input_cost = 100
        self.prune_patterns = prune_patterns
        self.output_cost = 1
        self.run_iterations = run_iterations
        self.compile_times = []
        self.memory_usages = []
        self.measure_egglog_time = True
        self.memo = {}


    def remove_concat_slice_only_patterns(self):
        # Remove all patterns which have just slices and concats only
        pruned_patterns = []

        for pattern in self.patterns:
            ops = pattern.get_pattern_eq_classes()
            test_ops = ['typed:concat_vectors', 'typed:slice_vectors']

            if len(test_ops) != len(ops):
                pruned_patterns.append(pattern)
                continue


            skip = all([op in ops for op in test_ops])

            if not skip:
                pruned_patterns.append(pattern)


        self.patterns = pruned_patterns



    def get_reachable_patterns_only(self, expr):
        self.remove_concat_slice_only_patterns()


        reachable_patterns = []
        reachable_dsl_names = get_ctx_expr_dsl_names(expr, self.src_dsl_list + self.target_dsl_list)
        while True:
            num_reachable = len(reachable_patterns)

            for i in range(len(self.patterns)):
                if i in reachable_patterns:
                    continue

                pi = self.patterns[i]

                if pi.does_pattern_contain_eq_class(reachable_dsl_names):
                    reachable_patterns.append(i)
                    reachable_dsl_names += pi.get_pattern_eq_classes()
                    reachable_dsl_names = list(set(reachable_dsl_names))

            num_reachable_end = len(reachable_patterns)

            if num_reachable_end == num_reachable:
                break

        return [self.patterns[i] for i in range(len(self.patterns))  if i in reachable_patterns ]





    def initialize_class_map(self):
        pass

    def initialize_lit_class(self):
        pass

    def initialize_reg_class(self):
        pass


    def emit_pattern_matching_based_compiler(self, expr, swizzle_cost = 1):
        egglog_decls = emit_egg_datatypes_two_dsl(self.src_dsl_list, self.target_dsl_list, input_cost = self.input_cost, output_cost = self.output_cost, swizzle_cost = swizzle_cost )

        test_patterns = self.patterns
        if self.prune_patterns:
            reachable_patterns = self.get_reachable_patterns_only(expr)

            print("Pruned patterns for expression ... # Patterns reduced from ", len(test_patterns), "to", len(reachable_patterns))
            test_patterns = reachable_patterns

        egglog_patterns = []
        for pattern in test_patterns:
            rewrite = emit_rewrite_expr(pattern.src_expr, pattern.target_expr, bidirectional = pattern.bidirectional)
            egglog_patterns.append(rewrite)


        egg_log_desc = "\n".join([egglog_decls] + egglog_patterns)
        return egg_log_desc


    def convert_reg_to_compiler_datastructure(self, expr_regs):
        return [emit_egg_define_reg(reg) for reg in expr_regs]

    def execute_cmd(self, cmd, cur_dir = None):
        output_stream_name= "egg.out.txt"+get_random_tempfile_name()


        with open(output_stream_name, "w+") as OutStream:
            if cur_dir is None:
                print("$[ Egg Compiler ]: "," ".join(cmd))

                proc = sb.Popen(cmd, start_new_session=True, stdout = OutStream, stderr = OutStream)
                process = psutil.Process(proc.pid)
                mem_info = process.memory_info()
                proc.wait()
                rss = mem_info.rss
                vms = mem_info.vms
                self.memory_usages.append((rss,vms))
                #sb.run(" ".join(cmd), shell = True, stdout = OutStream, stderr = OutStream)
            else:
                print("$[ Egg Compiler: {} ]: ".format(cur_dir)," ".join(cmd))
                sb.run(" ".join(cmd), shell = True, cwd = cur_dir, stdout = OutStream, stderr = OutStream)


        content = ""
        if os.path.exists(output_stream_name):
            with open(output_stream_name, "r") as StreamFile:
                content =  StreamFile.read()
            os.remove(output_stream_name)

        return content


    def execute_egglog_file(self, fname):




        exec_cmd = [self.egglog_bin ,fname]

        start_time = time.time()

        egg_log_stream = self.execute_cmd(exec_cmd)

        elapsed = time.time() - start_time
        if self.measure_egglog_time:
            self.compile_times.append(("EggLog", elapsed))

        final_expression_str = egg_log_stream.strip().split("\n")[-1]
        return final_expression_str


    def has_compiled_expr(self, expr):
        key = expr.emit_context_expr_string()
        return key in self.memo

    def get_compiled_expr(self,expr):
        key = expr.emit_context_expr_string()
        return copy.deepcopy(self.memo[key])

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

        if expr_contains_swizzles(output_expression, self.target_dsl_list):
            # Emit another swizzle pass to lower swizzle expressions
            print("Expression contains swizzles, need to lower swizzles")
            output_expression = self.run_swizzle_lowering_pipeline(output_expression, num_regs)


        self.memo[key] = output_expression

        return output_expression

    def parse_egglog_output_expr(self, expr_str, num_regs):

        expression_str = expr_str

        for i in range(num_regs):
            expression_str = expression_str.replace("(SYMBV {})".format(i), "(reg (bv {} 8))".format(i))

        output_expr = read_string_to_dsl(expression_str, self.target_dsl_list)

        return output_expr




    def print_stats(self):
        print("=======", "Compile Times", "=======")
        total = 0
        for category, secs in self.compile_times:
            print(category,":\t",  secs, "seconds")
            total += secs

        print("=="*20)
        print("Total", ":", total)

        print("=======", "Virtual Memory", "=======")
        peak_vms = -1
        for rss, vms in self.memory_usages:
            peak_vms = max(peak_vms, vms)
            MB = vms / (1024 * 1024)
            print("-", MB, "Megabytes")
        print("=="*20)
        print("Peak", ":", peak_vms / (1024 * 1024), "Megabytes")

        print("=======", "Physical Memory", "=======")
        peak_rss = -1
        for rss, vms in self.memory_usages:
            peak_rss = max(peak_rss, rss)
            MB = rss / (1024 * 1024)
            print("-", MB, "Megabytes")
        print("=="*20)
        print("Peak", ":", peak_rss / (1024 * 1024), "Megabytes")

    def run_swizzle_lowering_pipeline(self, expr):
        expr_regs = get_context_registers(expr)
        expr_regs = self.get_unique_registers(expr_regs)

        reg_data_structures = self.convert_reg_to_compiler_datastructure(expr_regs)
        compiler_functionality = self.emit_pattern_matching_based_compiler(expr, swizzle_cost = min(self.input_cost, self.output_cost * 10))

        statements = []

        statements.append(compiler_functionality)
        statements += [defn for label, defn in reg_data_structures]

        num_regs = len(reg_data_structures)

        src_expr_name = "swizzleexpr"
        src_expr_egg = emit_expr_to_egg(expr)
        define_src_expr = emit_egg_define_var(src_expr_name, src_expr_egg)
        statements.append(define_src_expr)

        statements.append(emit_egg_run_iter(self.run_iterations))
        statements.append(emit_egg_extract_expr(src_expr_name))
        egg_file_name = get_random_tempfile_name() + ".egg"

        print("Creating swizzle egg file:\t", egg_file_name)

        with open(egg_file_name, "w+") as EggFile:
            EggFile.write("\n".join(statements))

        final_expression_str= self.execute_egglog_file(egg_file_name)

        print("EGG LOG PRODUCED", final_expression_str)
        output_expression = self.parse_egglog_output_expr(final_expression_str, num_regs)
        return output_expression



