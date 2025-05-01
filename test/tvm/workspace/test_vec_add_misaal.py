from compiler.HydrideCompiler import HydrideCompiler
from utils.egg_config import EGG_PKG_PATH
from sema.hexsemantics_new import semantics as hvx_semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.tvm_folded import tvm_folded as tvm_semantics
from sema.halide_decomposed import halide_decomposed as halide_semantics
from sema.hvx_swizzles_decomposed import hvx_swizzles_decomposed as hvx_swizzles
from sema.x86_swizzles_decomposed import x86_swizzles_decomposed as x86_swizzles
from sema.arm_swizzles_decomposed import arm_swizzles_decomposed as arm_swizzles
from sema.ARMSema import arm_semantics
from sema.repairs_sema import repair_semantics
from utils.DSLInstructionUtils import parse_dict_with_bounded
import sys

from patterns.TVM import TVM_patterns as misaal_input_patterns
from patterns.x86 import x86_patterns as misaal_output_patterns
misaal_patterns = misaal_input_patterns + misaal_output_patterns
tvm_dsl_list = parse_dict_with_bounded(tvm_semantics)
halide_dsl_list = parse_dict_with_bounded(halide_semantics)
misaal_input = tvm_dsl_list + halide_dsl_list
inst_dict = parse_dict_with_bounded(x86_semantics)
swizzle_dict = parse_dict_with_bounded(x86_swizzles)
misaal_output = inst_dict + swizzle_dict
so_path = "/u/is16/526/Hydride/codegen-generator/tools/low-level-codegen/build/libX86Legalizer.so"
llvm_flags = ["-x86-hydride-legalize"]
intrin = "/u/is16/526/Hydride/codegen-generator/targets/x86/x86_wrappers.c.ll"
HYDRIDE_ROOT = "/u/is16/526/Hydride"
# Defining Tests 
tests = []
test_0_name = "hydride.node.misaal_func_0"
test_0_str ="""
(typed-folded:vec-add
(reg (bv 1 8))
(reg (bv 0 8))
16
64
1)
"""
tests.append((test_0_name,test_0_str))
if len(tests) == 0:
	sys.exit(0)
# Defining MISAAL Rewrite compiler
misaal_compiler = HydrideCompiler(misaal_patterns, src_dsl_list = misaal_input, target_dsl_list = misaal_output, run_iterations = 5, egg_pkg_path = EGG_PKG_PATH, tests = tests, llvm_so_path = so_path, llvm_flags =  llvm_flags, intrinsics_file =  intrin, hydride_root_path =  HYDRIDE_ROOT, llvm_out_file_name = "/u/is16/526/MISAAL/test/tvm/workspace/test_vec_add_misaal_temp_file")
# Invoke compiler and print stats
misaal_compiler.compile_hydride()
misaal_compiler.run_llvm_legalizer()
misaal_compiler.print_stats()
