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
from patterns.ARM import arm_patterns as misaal_output_patterns
misaal_patterns = misaal_input_patterns + misaal_output_patterns
halide_dsl_list = parse_dict_with_bounded(halide_semantics)
misaal_input = halide_dsl_list
inst_dict = parse_dict_with_bounded(arm_semantics)
swizzle_dict = parse_dict_with_bounded(arm_swizzles)
misaal_output = inst_dict + swizzle_dict
so_path = "/shared/hydride/LLVMARMLegalizer.so"
llvm_flags = ["-arm-hydride-legalize"]
intrin = "/shared/hydride/arm_wrappers.ll"
HYDRIDE_ROOT = "/home/baronia3/new-MISAAL/Hydride"
# Defining Tests 
tests = []
test_0_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.0"
test_0_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_0_name,test_0_str))
test_1_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.1"
test_1_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_1_name,test_1_str))
test_2_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.2"
test_2_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_2_name,test_2_str))
test_3_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.3"
test_3_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_3_name,test_3_str))
test_4_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.4"
test_4_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_4_name,test_4_str))
test_5_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.5"
test_5_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_5_name,test_5_str))
test_6_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.6"
test_6_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_6_name,test_6_str))
test_7_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.7"
test_7_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_7_name,test_7_str))
test_8_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.8"
test_8_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_8_name,test_8_str))
test_9_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.9"
test_9_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_9_name,test_9_str))
test_10_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.10"
test_10_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_10_name,test_10_str))
test_11_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.11"
test_11_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_11_name,test_11_str))
test_12_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.12"
test_12_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_12_name,test_12_str))
test_13_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.13"
test_13_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_13_name,test_13_str))
test_14_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.14"
test_14_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_14_name,test_14_str))
test_15_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.15"
test_15_str ="""
 (typed:vec-add
  (typed:signed-vec-widen-mul
   (reg (bv 0 8))
   (reg (bv 1 8))  16 64)
  (reg (bv 2 8)) 32 128)
"""
tests.append((test_15_name,test_15_str))
test_16_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.16"
test_16_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_16_name,test_16_str))
test_17_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.17"
test_17_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_17_name,test_17_str))
test_18_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.18"
test_18_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_18_name,test_18_str))
test_19_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.19"
test_19_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_19_name,test_19_str))
test_20_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.20"
test_20_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_20_name,test_20_str))
test_21_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.21"
test_21_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_21_name,test_21_str))
test_22_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.22"
test_22_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_22_name,test_22_str))
test_23_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.23"
test_23_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_23_name,test_23_str))
test_24_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.24"
test_24_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_24_name,test_24_str))
test_25_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.25"
test_25_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_25_name,test_25_str))
test_26_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.26"
test_26_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_26_name,test_26_str))
test_27_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.27"
test_27_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_27_name,test_27_str))
test_28_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.28"
test_28_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_28_name,test_28_str))
test_29_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.29"
test_29_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_29_name,test_29_str))
test_30_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.30"
test_30_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_30_name,test_30_str))
test_31_name = "hydride.node.matmul_256_32bit_bias_add_arm_depth2_misaal.31"
test_31_str ="""
 (typed:vec-add
  (reg (bv 0 8))
  (reg (bv 1 8)) 32 128)
"""
tests.append((test_31_name,test_31_str))
if len(tests) == 0:
	sys.exit(0)
# Defining MISAAL Rewrite compiler
misaal_compiler = HydrideCompiler(misaal_patterns, src_dsl_list = misaal_input, target_dsl_list = misaal_output, run_iterations = 5, egg_pkg_path = EGG_PKG_PATH, tests = tests, llvm_so_path = so_path, llvm_flags =  llvm_flags, intrinsics_file =  intrin, hydride_root_path =  HYDRIDE_ROOT, llvm_out_file_name = "/tmp/matmul_256_32bit_bias_add_arm_depth2_misaal")
# Invoke compiler and print stats
misaal_compiler.compile_hydride()
misaal_compiler.run_llvm_legalizer()
misaal_compiler.print_stats()
