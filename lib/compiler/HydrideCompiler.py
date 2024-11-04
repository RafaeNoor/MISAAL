from compiler.Compiler import *
import concurrent.futures
import subprocess as sb
from compiler.EggLogCompiler import EggLogCompiler
from utils.ReadDSL import read_string_to_dsl
import sys
import time
import os
import shutil


class HydrideCompiler(EggLogCompiler):

    def __init__(self, patterns, src_dsl_list = [], target_dsl_list = [], run_iterations = 10, egg_pkg_path = None, llvm_so_path = None, llvm_flags = [], tests = [],  intrinsics_file = None, hydride_root_path = None, llvm_out_file_name = "llvm.out", prune_patterns = False):
        super().__init__(patterns, src_dsl_list = src_dsl_list, target_dsl_list = target_dsl_list, run_iterations = run_iterations,  egg_pkg_path = egg_pkg_path, prune_patterns = prune_patterns)
        self.llvm_out_file_name = llvm_out_file_name
        self.llvm_so_path = llvm_so_path
        self.llvm_flags = llvm_flags
        self.output_file_path = "test.out"
        self.intrinsics_file = intrinsics_file
        self.hydride_root_path = hydride_root_path
        self.input_tests = tests
        self.pool_size = 8
        self.measure_egglog_time = False


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









    def run_llvm_legalizer(self):

        assert not self.llvm_so_path is None, "Unable to find LLVM target shared object file"
        assert not self.intrinsics_file is None, "Unable to find LLVM intrinsic file"
        assert len(self.llvm_flags) != 0, "Expected at least one LLVM flag"
        assert not self.hydride_root_path is None , "Hydride Root must be defined"

        start_time = time.time()

        low_level_gen_script = os.path.join(self.hydride_root_path, "codegen-generator", "tools","low-level-codegen","RoseLowLevelCodeGen.py")
        llvm_out_file =  self.llvm_out_file_name
        cmd = ["python3", low_level_gen_script, self.output_file_path, self.llvm_so_path, self.intrinsics_file, " ".join(self.llvm_flags), llvm_out_file]

        cmd_str = " ".join(cmd)
        print(cmd_str)
        sb.run(cmd_str, shell = True)
        elapsed = time.time() - start_time

        self.compile_times.append(("LLVM Legalize", elapsed))

        # Copy the final generated bitcode to the desired location
        final_bitcode_name = llvm_out_file + ".legalize.ll"
        copy_destination = llvm_out_file + ".ll"

        if os.path.exists(final_bitcode_name):
            shutil.copyfile(final_bitcode_name, copy_destination)





    def compile_hydride(self):
        if len(self.input_tests) == 0:
            print("No expressions for MISAAL to compile")
            return

        #assert len(self.input_tests) != 0, "Expected Input tests"
        assert not self.output_file_path is None, "Expected Output file"


        # First preprocess all unique expressions in parallel to
        # overlap compilation of as many expressions as possible,
        # then compile expressions sequentially by memoizing

        PARALLEL = True

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
                output_expr = self.compile_expr(input_expr)

            output_type_def = self.get_rosette_expression_str(input_expr ,output_expr, function_name)
            print(output_type_def)

            results[i] = output_type_def



        results = [0] * len(self.input_tests)

        for i in range(len(self.input_tests)):
            process_test(i)



        end_time = time.time()

        elapsed = end_time - start_time

        self.compile_times.append(("EggLogParallel", elapsed))

        print(results)


        with open(self.output_file_path, "w+") as LLVMInputFile:
            LLVMInputFile.write("\n".join(results))













