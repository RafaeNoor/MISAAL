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


from sema.hex_swizzles import hvx_swizzles

import os

halide_dsl_list = parse_dict(halide_semantics)
hvx_dsl_list = parse_dict(hvx_semantics)
hvx_swizzles_dsl_list = parse_dict(hvx_swizzles)

current_file_base = os.path.basename(__file__).split(".")[0]

props = [
    #hvx_EqClassEqualDepth,
    hvx_FusedSwizzleTranslator,
    #hvx_SimplifyingSwizzles,
]

patterns = []

for prop in props:
    for key, value in prop.items():
        src_key_name = 'src'
        if src_key_name not in value[0]['property']:
            src_key_name = 'candidate'

        dst_key_name = 'dst'
        if dst_key_name not in value[0]['property']:
            dst_key_name = 'simplified'

        hvx_expr = value[0]['property'][src_key_name]
        halide_expr = value[0]['property'][dst_key_name]

        pattern = parse_pattern_from_string(halide_expr, hvx_expr, halide_dsl_list + hvx_swizzles_dsl_list, hvx_dsl_list + hvx_swizzles_dsl_list, src_language = "halide", target_language = "hvx", bidirectional = False)

        patterns.append(pattern)






test_expr = """
(typed:vec-add ; typed:vec-add_p16_s2048_signed_None
		 (typed:signed-vec-widen-mul ; typed:signed-vec-widen-mul_p8_s1024_signed_1
			(buffer-index  1 'uint8 8) ; < 1 x i8> False
			(buffer-index  2 'uint8 8) ; < 1 x i8> False
			8
			1024
		 )
		 (reg (bv 0 (bitvector 8))) ; < 1 x i8> False
		16
		2048
	 )
"""






src_expr = read_string_to_dsl(test_expr, halide_dsl_list)

patterns = patterns[4:5]

egg_log_compiler = EggLogCompiler(patterns, src_dsl_list = halide_dsl_list + hvx_swizzles_dsl_list, target_dsl_list = hvx_dsl_list, run_iterations = 5, egg_file_name = f"{current_file_base}.egg", egg_pkg_path = EGG_PKG_PATH)


print("Number of Patterns:\t", len(patterns))
egg_log_compiler.compile_expr(src_expr)


