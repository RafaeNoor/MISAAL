from compiler.EggLogCompiler import EggLogCompiler
from compiler.Pattern import Pattern, parse_pattern_from_string
from sema.hexsemantics_new import semantics as hvx_semantics
from sema.halide_sema import halide_semantics
from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
from egg_config import EGG_PKG_PATH


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


egg_log_compiler = EggLogCompiler([pattern], src_dsl_list = halide_dsl_list, target_dsl_list = hvx_dsl_list, run_iterations = 1, egg_file_name = f"{current_file_base}.egg", egg_pkg_path = EGG_PKG_PATH)


egg_log_compiler.compile_expr(src_expr)


