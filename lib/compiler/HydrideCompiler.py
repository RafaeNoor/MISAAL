from compiler.Compiler import *
import subprocess as sb
from compiler.EggLogCompiler import EggLogCompiler
from utils.ReadDSL import read_string_to_dsl
import sys


class HydrideCompiler(EggLogCompiler):

    def __init__(self, patterns, src_dsl_list = [], target_dsl_list = [], run_iterations = 10, egg_file_name = None, egg_pkg_path = None, llvm_so_path = None, llvm_flags = [], input_file_path = None, output_file_path = None, function_name = None, intrinsics_file = None):
        super().__init__(patterns, src_dsl_list = src_dsl_list, target_dsl_list = target_dsl_list, run_iterations = run_iterations, egg_file_name = egg_file_name, egg_pkg_path = egg_pkg_path)
        self.llvm_so_path = llvm_so_path
        self.llvm_flags = llvm_flags
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.function_name = function_name
        self.intrinsics_file = intrinsics_file

    def get_reg_vector_type(self, reg):
        return "; (reg {}) <{} x i{}>".format(reg.index, reg.size // reg.precision,  reg.precision)

    def compile_expr_to_rosette(self, input_expr ,output_expr, function_name, output_file):
        expr_str = output_expr.emit_context_expr_string(add_output_type_info = True, use_reg_only = True, hydride_compatible = True)
        regs = get_unique_context_registers(input_expr)
        reg_type_info = [self.get_reg_vector_type(reg) for reg in regs]

        content = [
            "; "+ function_name,
        ]

        content += reg_type_info

        content += [expr_str]

        print("Writing expression to output file: ", output_file)
        with open(output_file, "a+") as AppendFile:
            AppendFile.write("\n".join(content)+"\n")











    def compile_hydride(self):
        #assert not self.llvm_so_path is None, "Unable to find LLVM target shared object file"
        #assert not len(self.llvm_flags) != 0, "Expected at least one LLVM flag"
        assert not self.input_file_path is None, "Expected Input file"
        assert not self.output_file_path is None, "Expected Output file"

        input_expr_str = None
        with open(self.input_file_path, "r") as InputFile:
            input_expr_str = InputFile.read()

        input_expr = read_string_to_dsl(input_expr_str, self.src_dsl_list)
        output_expr = self.compile_expr(input_expr)

        assert not self.function_name is None , "Expected function name"

        self.compile_expr_to_rosette(input_expr, output_expr, self.function_name, self.output_file_path)









