from compiler.HydrideCompiler import HydrideCompiler
from compiler.Pattern import Pattern, parse_pattern_from_string
from sema.hexsemantics_new import semantics as hvx_semantics
from sema.halide_sema import halide_semantics
from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
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

HVX_patterns = [pattern]
