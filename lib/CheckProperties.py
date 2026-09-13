
# Main driver for checking properites
import argparse


from common.DSLParser import parse_dict

from properties.RepairRelavance import RepairRelavance
from properties.RepairRelavanceV2 import RepairRelavanceV2
from properties.RepairRelavanceV3 import RepairRelavanceV3
from properties.RepairRelavanceV4 import RepairRelavanceV4
from properties.RepairRelavanceIntermediates import RepairRelavanceIntermediates
from properties.RepairRelavancePostProcess import RepairRelavancePostProcess
from properties.Commutative import *
from properties.Distributive import *
from properties.Associative import *
from properties.SimplifyingIdentity import SimplifyingIdentity
from properties.IdentifySwizzles import IdentifySwizzles
from properties.SwizzleTransferable import SwizzleTransferable
from properties.SynthSwizzleTransferable import SynthSwizzleTransferable
from properties.SynthSwizzleTransferableV2 import SynthSwizzleTransferableV2
from properties.FusedSwizzleTranslator import FusedSwizzleTranslator
from properties.Translator import Translator
from properties.ScaledTranslator import ScaledTranslator
from properties.EqualOnValues import EqualOnValues
from properties.EqualOnValuesDepth import EqualOnValuesDepth
from properties.LargeExpressionTranslator import LargeExpressionTranslator
from properties.EqClassEqualOnValuesDepth import EqClassEqualOnValuesDepth
from properties.EqClassEqualDepth import EqClassEqualDepth
from properties.EqClassEqualDepthV2 import EqClassEqualDepthV2
from properties.EqClassEqualDepthV3 import EqClassEqualDepthV3
from properties.EqClassEqualDepthV4 import EqClassEqualDepthV4
from properties.EqClassEqualDepthV4Full import EqClassEqualDepthV4Full
from properties.EqClassEqualDepthV3Synth import EqClassEqualDepthV3Synth
from properties.EqClassEqualDepthV4NoSwizzle import EqClassEqualDepthV4NoSwizzle
from properties.ExtractLaneSlice import ExtractLaneSlice
from properties.EnumeratePattern import EnumeratePattern
from properties.LowerSwizzles import LowerSwizzles
from properties.SwizzleTransferableV2 import SwizzleTransferableV2

from sema.hexsemantics_new import semantics as hvx_semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.halide_decomposed import halide_decomposed  as halide_semantics
#from sema.halide_folded_full import halide_folded_full as halide_folded
from sema.halide_full_pim import  halide_semantics as halide_folded
#from sema.hex_swizzles import hvx_swizzles
from sema.hvx_swizzles_decomposed import hvx_swizzles_decomposed as hvx_swizzles


#from sema.x86_swizzles import x86_swizzles
from sema.x86_swizzles_decomposed import x86_swizzles_decomposed as x86_swizzles
#from sema.arm_swizzles import arm_swizzles
from sema.arm_swizzles_decomposed import arm_swizzles_decomposed as arm_swizzles

#from sema.bitserial_fused_sema import bitserial_fused_sema
#from sema.pim_extend_dsl import pim_extended_dsl as bitserial_fused_sema
# TEMP
from sema.bitserial_fused_sema_v2 import bitserial_fused_sema_v2 as bitserial_fused_sema


from sema.ARMSema import arm_semantics
from sema.repairs_sema import repair_semantics
from sema.pim_extra import pim_extra
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HVX_SYNTH_DESC, HALIDE_HVX_SYNTH_DESC,ARM_SYNTH_DESC, create_synth_desc, HALIDE_SYNTH_DESC, HALIDE_X86_SYNTH_DESC, PIM_FUSED_SYNTH_DESC
from utils.DSLInstructionUtils import get_random_tempfile_name

import os

from properties.SimplifyingSwizzles import SimplifyingSwizzles

import json
import sys

import json

cleanup_files = [
    "property_time_log.txt"
]

for f in cleanup_files:
    if os.path.exists(f):
        os.remove(f)

parser = argparse.ArgumentParser(prog='CheckProperties', description='Run properties on targets',epilog='Text at the bottom of help')

parser.add_argument('-p', '--parallel',action='store_true', default = False)
parser.add_argument('--keep-temp-files',action='store_true', default = False)
parser.add_argument('--batch', type = int, default = 1024)
parser.add_argument('--pool', type = int, default = 16)
args = parser.parse_args()
PARALLEL = args.parallel
BATCH_SIZE = args.batch
POOL_SIZE = args.pool
KEEP_TEMP = args.keep_temp_files



TARGETS = [ "x86", "hvx", "halide_hvx", "arm"]
test_properties = [Commutative, Associative, Distributive, SimplifyingIdentity, IdentifySwizzles, SimplifyingSwizzles, SwizzleTransferable, SynthSwizzleTransferable, FusedSwizzleTranslator, Translator, ScaledTranslator, LargeExpressionTranslator]


x86_complex_instructions = None

arm_complex_instructions = [
    "vdotq_s32"
]

hvx_complex_instructions = [
    #"hexagon_V6_vasrh_acc_128B",
    #"hexagon_V6_interleave_2_128B",
    #"hexagon_V6_vmpabus_128B",
    #"hexagon_V6_vasrhv_128B",
    "hexagon_V6_vminuh_128B",
]


halide_complex_instructions = [
    'typed:signed-vec-rounding_mul_shift_right'
]


pim_complex_instructions = [
    #"test_enum_1_comb_1_fused_pim_op_5",
    #"test_enum_1_comb_8_fused_pim_op_1",
    "test_enum_1_comb_11_fused_pim_op_36",
] if False else None

TARGET_TO_COMPLEX_INSTS = {
    "x86": x86_complex_instructions,
    "hvx": hvx_complex_instructions,
    "arm": arm_complex_instructions,
    "pim_fused" : pim_complex_instructions,
    "pim_extra" : pim_complex_instructions,
    "hvx_swizzles": hvx_complex_instructions,
    "x86_swizzles": None,
    "arm_swizzles": None,
    "halide": halide_complex_instructions,
    "halide_folded": None
}


TARGET_TO_SEMA = {
    "x86": x86_semantics,
    "hvx": hvx_semantics,
    "halide_hvx": halide_semantics,
    "halide": halide_semantics,
    "halide_folded" : halide_folded,
    "arm" : arm_semantics,
    "pim_fused" : bitserial_fused_sema,
    "pim_extra" : pim_extra,
    "x86_swizzles":  x86_swizzles,
    "hvx_swizzles": hvx_swizzles,
    "arm_swizzles": arm_swizzles,
}


TARGET_TO_SWIZZLE = {
    "x86": x86_swizzles,
    "hvx": hvx_swizzles,
    "halide_hvx": {},
    "halide": {},
    "halide_folded": {},
    "arm" : arm_swizzles,
    "x86_swizzles":  {},
    "hvx_swizzles": {},
    "arm_swizzles": {},
    "pim_fused" : {},
    "pim_extra" : {},
}

TARGET_TO_SWIZZLE_DMAP = {
    "hvx": "hvx_swizzle_derivation_map.JSON",
    "arm": "arm_swizzle_derivation_map.JSON",
    "x86": "x86_swizzle_derivation_map.JSON",
    "halide" : "halide_swizzle_derivation_map.JSON",
    "halide_folded" : "halide_swizzle_derivation_map.JSON",
    "x86_swizzles": None,
    "hvx_swizzles": None,
    "arm_swizzles": None,
    "pim_fused" : None,
    "pim_extra" : None,
}


TARGET_TO_DESC = {
    "x86": X86_SYNTH_DESC,
    "hvx": HVX_SYNTH_DESC,
    "halide": HALIDE_HVX_SYNTH_DESC,
    "halide_folded": HALIDE_HVX_SYNTH_DESC,
    "halide_hvx": HALIDE_HVX_SYNTH_DESC,
    "arm": ARM_SYNTH_DESC,
    "x86_swizzles":  X86_SYNTH_DESC,
    "hvx_swizzles": HVX_SYNTH_DESC,
    "arm_swizzles": ARM_SYNTH_DESC,
    "pim_fused" : PIM_FUSED_SYNTH_DESC,
    "pim_extra" : PIM_FUSED_SYNTH_DESC,
}


commutative_path = "commutative_map.json"








TARGETS = ["x86",  "hvx", "arm"]

TARGETS = ["pim_fused"]
#TARGETS = ["halide_folded"]
#TARGETS = ["pim_extra"]







test_properties = [EqClassEqualDepthV4Full]
test_properties = [RepairRelavanceV4, RepairRelavanceIntermediates]

test_properties = [EqClassEqualDepthV4Full]

#test_properties = [Commutative]

#test_properties = [EnumeratePattern, EqClassEqualDepthV4Full]

test_properties = [EnumeratePattern]


for property in test_properties:
    for target in TARGETS:

        output_language = "halide"
        if "_swizzle" in target:
            output_language = target.split("_swizzle")[0]
        output_dsl_list = parse_dict_with_bounded(TARGET_TO_SEMA[output_language])
        output_synth_desc = TARGET_TO_DESC[output_language]

        dsl_list = parse_dict_with_bounded(TARGET_TO_SEMA[target], keep_duplicate = True)

        synthesizer_desc = TARGET_TO_DESC[target]
        property_result_suffix = "_{}_results".format(target)

        PropertyInstance = None
        if property is SwizzleTransferable:
            swizzle_synth_desc = create_synth_desc("{}-swizzles".format(target), True, TARGET_TO_DESC[target].target_vector_sizes, "/home/arnoor2/MISAAL/lib/sema/hex_swizzles.py","hvx_swizzles")
            PropertyInstance = property(dsl_list = dsl_list, synth_desc = swizzle_synth_desc, swizzles = parse_dict(hvx_swizzles))
        elif property is EnumeratePattern:
            commutative_path = "commutative_map.json"
            halide_dsl_list = parse_dict(halide_folded)
            swizzle_dict = TARGET_TO_SWIZZLE[target]
            swizzles = parse_dict(swizzle_dict)
            print("Total Swizzle classes: ", len(swizzles))
            swizzle_synth_desc = create_synth_desc("{}-enumerate_self".format(target), True, TARGET_TO_DESC[target].target_vector_sizes, "/home/arnoor2/MISAAL/lib/sema/hex_swizzles.py","hvx_swizzles")

            pattern_file = "/home/arnoor2/MISAAL/targets/pim_fused/pim_construction_rewrite_rules_templates_v2.py"
            #pattern_file = "./EqClassEqualDepthV4Fullself_to_self_halide_folded_halide_intermediate_results.py"
            #pattern_file= "EqClassEqualDepthV4Full_bi_map_v2_pim_intermediate_results.py"
            #pattern_file = "./EqClassEqualDepthV4Fullself_to_self_v2_pim_intermediate_results.py"
            #pattern_file = "/home/arnoor2/MISAAL/targets/pim_fused/pim_additional_ops_construction_v2.py"
            #pattern_file = "../targets/{}/EqClassEqualDepthV4_{}_intermediate_results.py".format(target, target)
            #pattern_file = "../targets/hvx/EqClassEqualDepthV4_vmpyh_hvx_intermediate_results.py"
            with open(pattern_file, "r") as PatternFile:
                input_patterns = json.load(PatternFile)

            # TEMP
            #input_patterns = {key : input_patterns[key] for key in input_patterns if "comb_21_fused_pim_op_1423" in key}
            PropertyInstance = property(dsl_list = dsl_list + swizzles+halide_dsl_list, synth_desc = swizzle_synth_desc, input_patterns_dict = input_patterns )
            #PropertyInstance.name += "_pim_self_to_self_v2"
            #PropertyInstance.name += "_halide_folded_self_to_self_v2"
            #PropertyInstance.name += "_pim_bi_map_v2"
            PropertyInstance.name += "_pim_construction_v2_select_fix"
        elif property is SimplifyingSwizzles:
            swizzle_dict = TARGET_TO_SWIZZLE[target]
            swizzles = parse_dict(swizzle_dict)
            print("Total Swizzle classes: ", len(swizzles))

            swizzle_synth_desc = create_synth_desc("{}-swizzles".format(target), True, TARGET_TO_DESC[target].target_vector_sizes, "/home/arnoor2/MISAAL/lib/sema/hex_swizzles.py","hvx_swizzles")
            PropertyInstance = SimplifyingSwizzles(dsl_list = swizzles, synth_desc = swizzle_synth_desc,input_depth = 2)

        elif property is SynthSwizzleTransferable:
            swizzle_synth_desc = create_synth_desc("{}-swizzles".format(target), True, TARGET_TO_DESC[target].target_vector_sizes, "/home/arnoor2/MISAAL/lib/sema/hex_swizzles.py","hvx_swizzles")
            PropertyInstance = property(dsl_list = dsl_list, synth_desc = swizzle_synth_desc, swizzles = parse_dict(hvx_swizzles))

        elif property is SynthSwizzleTransferableV2:

            commutative_path = "commutative_map.json"
            swizzle_synth_desc = create_synth_desc("{}-swizzles".format(target), True, TARGET_TO_DESC[target].target_vector_sizes, "/home/arnoor2/MISAAL/lib/sema/hex_swizzles.py","hvx_swizzles")
            PropertyInstance = property(dsl_list = dsl_list, swizzle_dsl_list = parse_dict(hvx_swizzles), input_depth = 2, output_depth = 2, depth_range = False, synth_desc = swizzle_synth_desc, commutative_map_path=  commutative_path)


        elif property is FusedSwizzleTranslator:
            swizzle_dict = TARGET_TO_SWIZZLE[target]
            swizzles = parse_dict(swizzle_dict)
            print("Total Swizzle classes: ", len(swizzles))
            halide_dsl_list = parse_dict(halide_semantics)
            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, target_dsl_list = halide_dsl_list, shuffle_deriviation_map_path=TARGET_TO_SWIZZLE_DMAP[target], swizzles = swizzles )

        elif property is ScaledTranslator:
            halide_dsl_list = parse_dict(halide_semantics)

            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, exhaustive = True, input_depth = 1, permute_limit = 1, scale_factor = 1, target_dsl_list = halide_dsl_list)


        elif property is Translator:
            halide_dsl_list = parse_dict(halide_semantics)

            #PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, exhaustive = True, input_depth = 2, permute_limit = 1)

            #reversed
            PropertyInstance = property(target_dsl_list = dsl_list, target_synth_desc = synthesizer_desc, source_synth_desc = HALIDE_HVX_SYNTH_DESC, dsl_list=halide_dsl_list, exhaustive = True, input_depth = 2, permute_limit = 1)
        elif property is EqualOnValues:
            halide_dsl_list = parse_dict(halide_semantics)
            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, target_dsl_list = halide_dsl_list)

        elif property is EqualOnValuesDepth:
            halide_dsl_list = parse_dict(halide_semantics)
            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, target_dsl_list = halide_dsl_list, output_depth = 2)

        elif property is EqClassEqualOnValuesDepth:
            halide_dsl_list = parse_dict(halide_semantics)
            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, target_dsl_list = halide_dsl_list, output_depth = 2)

            #PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = synthesizer_desc, target_dsl_list = dsl_list, output_depth = 2)

        elif property is RepairRelavance:
            repairs_sema = parse_dict(repair_semantics)
            halide_dsl_list = parse_dict(halide_semantics)
            PropertyInstance = property(dsl_list = dsl_list, synth_desc = synthesizer_desc, target_synth_desc = HALIDE_SYNTH_DESC, output_dsl_list = halide_dsl_list, repair_dsl_list = repairs_sema, target_start_depth = 1, target_depth = 4 )

        elif property is RepairRelavanceV2 or property is RepairRelavanceV3 :
            repair_memo_name = "RepairRelavanceV3_{}_d2_processed_results.json".format(target)


            if not os.path.exists(repair_memo_name):
                repair_memo_name = None
                assert False

            repairs_sema = parse_dict(repair_semantics)
            halide_dsl_list = parse_dict(halide_semantics)
            PropertyInstance = property(dsl_list = dsl_list, synth_desc = synthesizer_desc, target_synth_desc = HALIDE_SYNTH_DESC, output_dsl_list = halide_dsl_list, repair_dsl_list = repairs_sema, target_start_depth = 1, target_depth = 3, commutative_map_path = commutative_path, memo_path = repair_memo_name )

        elif property is RepairRelavanceV4:
            repair_memo_name = "RepairRelavanceIntermediates_{}_intermediate_results.py".format(target)
            if not os.path.exists(repair_memo_name):
                repair_memo_name = None
            repair_memo_name = None
            repairs_sema = parse_dict(repair_semantics)
            halide_dsl_list = parse_dict(halide_folded)
            PropertyInstance = property(dsl_list = dsl_list, synth_desc = synthesizer_desc, target_synth_desc = HALIDE_SYNTH_DESC, output_dsl_list = halide_dsl_list, repair_dsl_list = repairs_sema, target_start_depth = 1, target_depth = 2, commutative_map_path = commutative_path, memo_path = repair_memo_name )

        elif property is RepairRelavanceIntermediates:
            repair_memo_name = "RepairRelavanceIntermediates_{}_intermediate_results.py".format(target)
            if not os.path.exists(repair_memo_name):
                repair_memo_name = None
            repair_memo_name = None
            repairs_sema = parse_dict(repair_semantics)
            halide_dsl_list = parse_dict(halide_folded)
            PropertyInstance = property(dsl_list = dsl_list, synth_desc = synthesizer_desc, target_synth_desc = HALIDE_SYNTH_DESC, output_dsl_list = halide_dsl_list, repair_dsl_list = repairs_sema, target_start_depth = 1, target_depth = 2, commutative_map_path = commutative_path, memo_path = repair_memo_name )
        elif property is RepairRelavancePostProcess:
            version = "Intermediates"
            repair_memo_name = "RepairRelavance{}_{}_intermediate_results.py".format(version,target)

            if not os.path.exists(repair_memo_name):
                repair_memo_name = None
                assert False

            repairs_sema = parse_dict(repair_semantics)
            halide_dsl_list = parse_dict(halide_semantics)
            PropertyInstance = property(input_dsl_list = dsl_list ,output_dsl_list = halide_dsl_list, repair_dsl_list = repairs_sema, memo_path = repair_memo_name , target = target, base_name = "VERSION_{}".format(version))
        elif property is EqClassEqualDepth or property is EqClassEqualDepthV2:
            halide_dsl_list = parse_dict(halide_semantics)
            target_swizzles = parse_dict(TARGET_TO_SWIZZLE[target], keep_duplicate=True)
            #forward_path_name = "repair_forward_map_true.json"
            forward_path_name = "repair_forward_map_{}.json".format(target)
            swizzle_forward_path = TARGET_TO_SWIZZLE_DMAP[target]#"hvx_swizzle_derivation_map.JSON"
            commutative_path = "commutative_map.json"
            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, target_dsl_list = halide_dsl_list, output_depth = 2, forward_map_path = forward_path_name, swizzle_dsl_list = target_swizzles, swizzle_map_path = swizzle_forward_path, commutative_map_path=  commutative_path)

        elif property is EqClassEqualDepthV3:
            halide_dsl_list = parse_dict(halide_semantics)
            target_swizzles = parse_dict(TARGET_TO_SWIZZLE[target], keep_duplicate=True)
            forward_path_name = "repair_forward_map_{}.json".format(target)
            swizzle_forward_path = TARGET_TO_SWIZZLE_DMAP[target]
            commutative_path = "commutative_map.json"
            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, target_dsl_list = halide_dsl_list, output_depth = 4,input_depth = 2,  forward_map_path = forward_path_name, swizzle_dsl_list = target_swizzles, swizzle_map_path = swizzle_forward_path, commutative_map_path=  commutative_path, depth_range = True , use_canon_map = False)

        elif property is EqClassEqualDepthV3Synth:
            halide_dsl_list = parse_dict(halide_semantics)
            target_swizzles = parse_dict(TARGET_TO_SWIZZLE[target], keep_duplicate=True)
            #forward_path_name = "repair_forward_map_{}_{}.json".format(target, output_language)
            forward_path_name = "repair_forward_map_{}.json".format(target)

            filter_list = TARGET_TO_COMPLEX_INSTS[target]
            swizzle_forward_path = TARGET_TO_SWIZZLE_DMAP[target]
            commutative_path = "commutative_map.json"
            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = output_synth_desc, target_dsl_list = output_dsl_list, output_depth = 3,input_depth = 2,  forward_map_path = forward_path_name, swizzle_dsl_list = target_swizzles, swizzle_map_path = swizzle_forward_path, commutative_map_path=  commutative_path, depth_range = True , use_canon_map = False, filter_list = filter_list)

        elif property is EqClassEqualDepthV4 or property is LowerSwizzles:
            halide_dsl_list = parse_dict(halide_semantics)
            target_swizzles = parse_dict(TARGET_TO_SWIZZLE[target], keep_duplicate=True)
            forward_path_name = "repair_forward_map_{}.json".format(target)
            if not os.path.exists(forward_path_name):
                forward_path_name = None
            swizzle_forward_path = TARGET_TO_SWIZZLE_DMAP[target]
            commutative_path = "commutative_map.json"
            filter_list = TARGET_TO_COMPLEX_INSTS[target]
            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = output_synth_desc, target_dsl_list = output_dsl_list, output_depth = 4,input_depth = 4,  forward_map_path = forward_path_name, swizzle_dsl_list = target_swizzles, swizzle_map_path = swizzle_forward_path, commutative_map_path=  commutative_path, depth_range = True , use_canon_map = False, filter_list = filter_list)
            PropertyInstance.name = PropertyInstance.name +"_time"

        elif property is EqClassEqualDepthV4NoSwizzle :
            halide_dsl_list = parse_dict(halide_semantics)
            target_swizzles = parse_dict(TARGET_TO_SWIZZLE[target], keep_duplicate=True)
            forward_path_name = "repair_forward_map_{}.json".format(target)
            if not os.path.exists(forward_path_name):
                print("Unable to find forward path")
                forward_path_name = None
            swizzle_forward_path = TARGET_TO_SWIZZLE_DMAP[target]
            commutative_path = "commutative_map.json"
            filter_list = TARGET_TO_COMPLEX_INSTS[target]
            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = output_synth_desc, target_dsl_list = output_dsl_list, output_depth = 4,input_depth = 1,  forward_map_path = forward_path_name, swizzle_dsl_list = target_swizzles, swizzle_map_path = swizzle_forward_path, commutative_map_path=  commutative_path, depth_range = False , use_canon_map = False, filter_list = filter_list)

            PropertyInstance.name = PropertyInstance.name +"_arm_vdot"

        elif property is EqClassEqualDepthV4Full or property is SwizzleTransferableV2:
            halide_dsl_list = parse_dict(halide_folded)

            halide_dsl_list = [d for d in halide_dsl_list if "round" not in d.name]
            halide_dsl_list = [d for d in halide_dsl_list if "mul_shift" not in d.name]
            target_swizzles = parse_dict(TARGET_TO_SWIZZLE[target], keep_duplicate=True)
            swizzle_forward_path = None
            forward_path_name = None
            filter_list = TARGET_TO_COMPLEX_INSTS[target]
            commutative_path = "commutative_map.json"
            print("TARGET DSL LIST SRC", halide_dsl_list)
            print("SRC DSL LIST SRC", dsl_list)

            dsl_list = [d for d in dsl_list if "round" not in d.name]
            dsl_list = [d for d in dsl_list if "mul_shift" not in d.name]


            SELF_TO_SELF = True

            #dsl_list = [d for d in dsl_list if any([f in d.name for f in ["widen", "mul", "extend"]])]
            #dsl_list = [d for d in dsl_list if "round" not in d.name]

            if SELF_TO_SELF:
                PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = synthesizer_desc,  target_dsl_list = dsl_list, output_depth = 2,input_depth = 2,  forward_map_path = forward_path_name, swizzle_dsl_list = target_swizzles, swizzle_map_path = swizzle_forward_path, commutative_map_path=  commutative_path, depth_range = False, use_canon_map = False, filter_list = filter_list, bidirectional_test = False)
                PropertyInstance.name = PropertyInstance.name + "self_to_self_halide_folded_d2"
            else:
                PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, target_dsl_list = halide_dsl_list, output_depth = 2,input_depth = 1,  forward_map_path = forward_path_name, swizzle_dsl_list = target_swizzles, swizzle_map_path = swizzle_forward_path, commutative_map_path=  commutative_path, depth_range = True, use_canon_map = False, filter_list = filter_list, bidirectional_test = True)
                PropertyInstance.name = PropertyInstance.name +"_bi_map_v2"







        elif property is LargeExpressionTranslator:
            swizzle_dict = TARGET_TO_SWIZZLE[target]
            swizzles = parse_dict(swizzle_dict, keep_duplicate = True)
            print("Total Swizzle classes: ", len(swizzles))
            halide_dsl_list = parse_dict(halide_semantics)
            PropertyInstance = property(target_dsl_list = dsl_list, target_synth_desc = synthesizer_desc, source_synth_desc = HALIDE_HVX_SYNTH_DESC, dsl_list = halide_dsl_list, shuffle_deriviation_map_path="hvx_swizzle_derivation_map.JSON", swizzles = swizzles, context_deriviation_map_path = "backward_map.json", input_depth = 2)

        else:
            PropertyInstance = property(dsl_list = dsl_list, synth_desc= synthesizer_desc)
        PropertyInstance.parallel = PARALLEL
        PropertyInstance.POOL_SIZE = POOL_SIZE
        PropertyInstance.BATCH_SIZE = BATCH_SIZE
        PropertyInstance.keep_temp_files =  KEEP_TEMP
        PropertyInstance.notify_enabled = False
        property_map = PropertyInstance.get_property()


        property_label = target+"_"+PropertyInstance.name
        fname = "{}.py".format(PropertyInstance.name+property_result_suffix)

        if os.path.exists(fname):
            prepend = get_random_tempfile_name()
            # If file exists then append prefix
            #fname = prepend +"_"+fname
            #property_label = prepend + "_"+property_label
        with open(fname, "w+") as DumpFile:
            DumpFile.write(property_label + "=" + json.dumps(property_map, indent = 4))


        if "halide" in target:
            continue

        egg_log_name = property_label+"_egg.egg"

        seperator = ";" + "="*100

        with open(egg_log_name, "w+") as DumpFile:
            egg_rules = PropertyInstance.emit_property_to_egg(property_map)
            write_line = lambda x : DumpFile.write(x+"\n")
            write_line(";; Automatically generated rules")

            for rule in egg_rules:
                write_line(seperator)
                write_line(rule)


