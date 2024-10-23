from compiler.HydrideCompiler import HydrideCompiler
from compiler.Pattern import Pattern, parse_pattern_from_string
from sema.hexsemantics_new import semantics as hvx_semantics
from sema.halide_sema import halide_semantics
from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
from utils.egg_config import EGG_PKG_PATH


import os

halide_dsl_list = parse_dict(halide_semantics)
hvx_dsl_list = parse_dict(hvx_semantics)

current_file_base = os.path.basename(__file__).split(".")[0]



pattern_str_from = """
(typed:vec-add
(reg (bv 0 4))
(reg (bv 1 4))
32
2048
)
"""


pattern_str_to = """
(hexagon_V6_vaddhsat_128B_dsl
(reg (bv 0 4))
(reg (bv 1 4))
2048
2048
0
2048
32
-1
0
)

"""



pattern = parse_pattern_from_string(pattern_str_from, pattern_str_to, halide_dsl_list, hvx_dsl_list, src_language = "halide", target_language = "hvx")
pattern.print_pattern()

src_expr = read_string_to_dsl(pattern_str_from, halide_dsl_list)




src_expr_file_path = "test.src"
output_file_path = "test.output"

if os.path.exists(src_expr_file_path):
    os.remove(src_expr_file_path)

if os.path.exists(output_file_path):
    os.remove(output_file_path)


# Write src expression to file
with open(src_expr_file_path, "w+") as SrcFile:
    SrcFile.write(src_expr.emit_context_expr_string(use_reg_only = False)+"\n")


hvx_flags = ["-hex-hydride-legalize"]
hvx_legalizer_file_so = "/shared/hydride/LLVMHVXLegalizer.so"
hvx_intrinsics_file = "/shared/hydride/hvx_wrappers.ll"

HYDRIDE_ROOT = "/home/arnoor2/Hydride/Hydride/"


hydride_compiler = HydrideCompiler([pattern], src_dsl_list = halide_dsl_list, target_dsl_list = hvx_dsl_list, run_iterations = 1, egg_file_name = f"{current_file_base}.egg", egg_pkg_path = EGG_PKG_PATH, function_name = "hydride.node.test_func", input_file_path = src_expr_file_path, output_file_path = output_file_path,
                                   llvm_so_path = hvx_legalizer_file_so,
                                   llvm_flags = hvx_flags,
                                   intrinsics_file = hvx_intrinsics_file,
                                   hydride_root_path = HYDRIDE_ROOT
                                   )


hydride_compiler.compile_hydride()

hydride_compiler.run_llvm_legalizer()

hydride_compiler.print_stats()


if os.path.exists(src_expr_file_path):
    os.remove(src_expr_file_path)

if os.path.exists(output_file_path):
    os.remove(output_file_path)
