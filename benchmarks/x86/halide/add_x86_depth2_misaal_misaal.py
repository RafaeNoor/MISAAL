from compiler.HydrideCompiler import HydrideCompiler
from utils.egg_config import EGG_PKG_PATH
from sema.hexsemantics_new import semantics as hvx_semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.halide_decomposed import halide_decomposed as halide_semantics
from sema.hvx_swizzles_decomposed import hvx_swizzles_decomposed as hvx_swizzles
from sema.x86_swizzles_decomposed import x86_swizzles_decomposed as x86_swizzles
from sema.arm_swizzles_decomposed import arm_swizzles_decomposed as arm_swizzles
from sema.ARMSema import arm_semantics
from sema.repairs_sema import repair_semantics
from utils.DSLInstructionUtils import parse_dict_with_bounded
import sys

misaal_input_patterns = []
from patterns.x86 import x86_patterns as misaal_output_patterns
misaal_patterns = misaal_input_patterns + misaal_output_patterns
halide_dsl_list = parse_dict_with_bounded(halide_semantics)
misaal_input = halide_dsl_list
inst_dict = parse_dict_with_bounded(x86_semantics)
swizzle_dict = parse_dict_with_bounded(x86_swizzles)
misaal_output = inst_dict + swizzle_dict
so_path = "/home/llvm-lab/MISAAL-test/submodule-test-MISAAL/Hydride/codegen-generator/tools/low-level-codegen/build//libx86LegalizerAllArgs.so"
llvm_flags = ["-x86-hydride-legalize"]
intrin = "/home/llvm-lab/MISAAL-test/submodule-test-MISAAL/Hydride/codegen-generator/tools/low-level-codegen/wrappers/x86_wrappers.c.ll"
HYDRIDE_ROOT = "/home/llvm-lab/MISAAL-test/submodule-test-MISAAL/Hydride"
# Defining Tests 
tests = []
test_0_name = "hydride.node.add_x86_depth2_misaal.0"
test_0_str ="""
 (typed:unsigned-vec-max
  (typed:unsigned-vec-min
   (reg (bv 0 8))
   (typed:xBroadcast (reg (bv 1 8))  8 8 64 ) 8 512)
  (typed:xBroadcast (reg (bv 2 8))  8 8 64 ) 8 512)
"""
tests.append((test_0_name,test_0_str))
test_1_name = "hydride.node.add_x86_depth2_misaal.1"
test_1_str ="""
 (typed:unsigned-vec-max
  (typed:unsigned-vec-min
   (reg (bv 0 8))
   (typed:xBroadcast (reg (bv 1 8))  8 8 64 ) 8 512)
  (typed:xBroadcast (reg (bv 2 8))  8 8 64 ) 8 512)
"""
tests.append((test_1_name,test_1_str))
if len(tests) == 0:
	sys.exit(0)
# Defining MISAAL Rewrite compiler
misaal_compiler = HydrideCompiler(misaal_patterns, src_dsl_list = misaal_input, target_dsl_list = misaal_output, run_iterations = 5, egg_pkg_path = EGG_PKG_PATH, tests = tests, llvm_so_path = so_path, llvm_flags =  llvm_flags, intrinsics_file =  intrin, hydride_root_path =  HYDRIDE_ROOT, llvm_out_file_name = "/tmp/add_x86_depth2_misaal")
# Invoke compiler and print stats
misaal_compiler.compile_hydride()
misaal_compiler.run_llvm_legalizer()
misaal_compiler.print_stats()
