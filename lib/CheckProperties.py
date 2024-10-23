
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
from properties.EqClassEqualDepthV3Synth import EqClassEqualDepthV3Synth
from properties.ExtractLaneSlice import ExtractLaneSlice

from sema.hexsemantics_new import semantics as hvx_semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.halide_sema import halide_semantics
from sema.hex_swizzles import hvx_swizzles
#from sema.x86_swizzles import x86_swizzles
from sema.x86_swizzles_decomposed import x86_swizzles_decomposed as x86_swizzles
from sema.arm_swizzles import arm_swizzles

from sema.ARMSema import arm_semantics
from sema.repairs_sema import repair_semantics
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HVX_SYNTH_DESC, HALIDE_HVX_SYNTH_DESC,ARM_SYNTH_DESC, create_synth_desc, HALIDE_SYNTH_DESC
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




TARGET_TO_SEMA = {
    "x86": x86_semantics,
    "hvx": hvx_semantics,
    "halide_hvx": halide_semantics,
    "arm" : arm_semantics,
    "x86_swizzles":  x86_swizzles,
    "hvx_swizzles": hvx_swizzles,
    "arm_swizzles": arm_swizzles,
}


TARGET_TO_SWIZZLE = {
    "x86": x86_swizzles,
    "hvx": hvx_swizzles,
    "halide_hvx": {},
    "arm" : arm_swizzles,
    "x86_swizzles":  {},
    "hvx_swizzles": {},
    "arm_swizzles": {},
}

TARGET_TO_SWIZZLE_DMAP = {
    "hvx": "hvx_swizzle_derivation_map.JSON",
    "arm": "arm_swizzle_derivation_map.JSON",
    "x86": "x86_swizzle_derivation_map.JSON",
}


TARGET_TO_DESC = {
    "x86": X86_SYNTH_DESC,
    "hvx": HVX_SYNTH_DESC,
    "halide_hvx": HALIDE_HVX_SYNTH_DESC,
    "arm": ARM_SYNTH_DESC,
    "x86_swizzles":  X86_SYNTH_DESC,
    "hvx_swizzles": HVX_SYNTH_DESC,
    "arm_swizzles": ARM_SYNTH_DESC,
}


commutative_path = "commutative_map.json"








TARGETS = ["arm"]



test_properties = [EqClassEqualDepthV4]
#test_properties = [Commutative]


for property in test_properties:
    for target in TARGETS:
        dsl_list = parse_dict(TARGET_TO_SEMA[target])

        synthesizer_desc = TARGET_TO_DESC[target]
        property_result_suffix = "_{}_results".format(target)

        PropertyInstance = None
        if property is SwizzleTransferable:
            swizzle_synth_desc = create_synth_desc("{}-swizzles".format(target), True, TARGET_TO_DESC[target].target_vector_sizes, "/home/arnoor2/MISAAL/lib/sema/hex_swizzles.py","hvx_swizzles")
            PropertyInstance = property(dsl_list = dsl_list, synth_desc = swizzle_synth_desc, swizzles = parse_dict(hvx_swizzles))
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
            halide_dsl_list = parse_dict(halide_semantics)
            PropertyInstance = property(dsl_list = dsl_list, synth_desc = synthesizer_desc, target_synth_desc = HALIDE_SYNTH_DESC, output_dsl_list = halide_dsl_list, repair_dsl_list = repairs_sema, target_start_depth = 1, target_depth = 2, commutative_map_path = commutative_path, memo_path = repair_memo_name )

        elif property is RepairRelavanceIntermediates:
            repair_memo_name = "RepairRelavanceIntermediates_{}_intermediate_results.py".format(target)
            if not os.path.exists(repair_memo_name):
                repair_memo_name = None
            repair_memo_name = None
            repairs_sema = parse_dict(repair_semantics)
            halide_dsl_list = parse_dict(halide_semantics)
            PropertyInstance = property(dsl_list = dsl_list, synth_desc = synthesizer_desc, target_synth_desc = HALIDE_SYNTH_DESC, output_dsl_list = halide_dsl_list, repair_dsl_list = repairs_sema, target_start_depth = 1, target_depth = 2, commutative_map_path = commutative_path, memo_path = repair_memo_name )
        elif property is RepairRelavancePostProcess:
            version = "Intermediates"
            #version = "V4"
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
            forward_path_name = "repair_forward_map_{}.json".format(target)
            swizzle_forward_path = TARGET_TO_SWIZZLE_DMAP[target]
            commutative_path = "commutative_map.json"
            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, target_dsl_list = halide_dsl_list, output_depth = 2,input_depth = 4,  forward_map_path = forward_path_name, swizzle_dsl_list = target_swizzles, swizzle_map_path = swizzle_forward_path, commutative_map_path=  commutative_path, depth_range = True , use_canon_map = False)

        elif property is EqClassEqualDepthV4:
            halide_dsl_list = parse_dict(halide_semantics)
            target_swizzles = parse_dict(TARGET_TO_SWIZZLE[target], keep_duplicate=True)
            forward_path_name = "repair_forward_map_{}.json".format(target)
            swizzle_forward_path = TARGET_TO_SWIZZLE_DMAP[target]
            commutative_path = "commutative_map.json"
            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, target_dsl_list = halide_dsl_list, output_depth = 2,input_depth = 2,  forward_map_path = forward_path_name, swizzle_dsl_list = target_swizzles, swizzle_map_path = swizzle_forward_path, commutative_map_path=  commutative_path, depth_range = True , use_canon_map = False)



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
        property_map = PropertyInstance.get_property()


        property_label = target+"_"+PropertyInstance.name
        fname = "{}.py".format(PropertyInstance.name+property_result_suffix)

        if os.path.exists(fname):
            prepend = get_random_tempfile_name()
            # If file exists then append prefix
            fname = prepend +"_"+fname
            property_label = prepend + "_"+property_label
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


