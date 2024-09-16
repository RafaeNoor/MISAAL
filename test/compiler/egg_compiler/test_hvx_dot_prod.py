from compiler.EggLogCompiler import EggLogCompiler
from compiler.Pattern import Pattern, parse_pattern_from_string
from sema.hexsemantics_new import semantics as hvx_semantics
from sema.halide_sema import halide_semantics
from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
from egg_config import EGG_PKG_PATH

from EqClassEqualDepth_hvx_results import hvx_EqClassEqualDepth
from SimplifyingSwizzles_hvx_results import hvx_SimplifyingSwizzles
from FusedSwizzleTranslator_hvx_results import hvx_FusedSwizzleTranslator
from SwizzleTransfer_hvx_results import hvx_SwizzleTransfer
from SynthSwizzleTransfer_hvx_results import hvx_SynthSwizzleTransfer


from sema.hex_swizzles import hvx_swizzles

import os

halide_dsl_list = parse_dict(halide_semantics)
hvx_dsl_list = parse_dict(hvx_semantics)
hvx_swizzles_dsl_list = parse_dict(hvx_swizzles)

current_file_base = os.path.basename(__file__).split(".")[0]

props = [
    hvx_EqClassEqualDepth,
    hvx_FusedSwizzleTranslator,
    hvx_SimplifyingSwizzles,
    hvx_SwizzleTransfer,
    hvx_SynthSwizzleTransfer,
]

src_key_names = ['src', 'candidate', 'input_expression']
dst_key_names = ['dst', 'simplified', 'output_expression']

patterns = []

for idx, prop in enumerate(props):
    for key, value in prop.items():
        src_key_name = "src"
        for src_key in src_key_names:
            if src_key in value[0]['property']:
                src_key_name = src_key

        dst_key_name = 'dst'
        for dst_key in dst_key_names:
            if dst_key  in value[0]['property']:
                dst_key_name = dst_key

        input_expr = value[0]['property'][src_key_name]
        output_expr = value[0]['property'][dst_key_name]


        pattern = parse_pattern_from_string(input_expr, output_expr, halide_dsl_list + hvx_dsl_list +hvx_swizzles_dsl_list, halide_dsl_list + hvx_dsl_list + hvx_swizzles_dsl_list, src_language = "halide", target_language = "hvx", bidirectional = True)

        patterns.append(pattern)


test_expr = """
(typed:vec-add
		 (typed:signed-vec-widen-mul
			(buffer-index  1 'int8 1024)
			(buffer-index  2 'int8 1024)
		        8
			1024
		 )
		 (reg (bv 0 (bitvector 8)))
	        16
		2048
	 )
"""


src_expr = read_string_to_dsl(test_expr, halide_dsl_list)


egg_log_compiler = EggLogCompiler(patterns, src_dsl_list = halide_dsl_list + hvx_swizzles_dsl_list, target_dsl_list = hvx_dsl_list, run_iterations = 5, egg_file_name = f"{current_file_base}.egg", egg_pkg_path = EGG_PKG_PATH)


print("Number of Patterns:\t", len(patterns))
egg_log_compiler.compile_expr(src_expr)


