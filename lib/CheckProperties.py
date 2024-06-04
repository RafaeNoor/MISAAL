
# Main driver for checking properites
import argparse


from common.DSLParser import parse_dict

from properties.RepairRelavance import RepairRelavance
from properties.Commutative import *
from properties.Distributive import *
from properties.Associative import *
from properties.SimplifyingIdentity import SimplifyingIdentity
from properties.IdentifySwizzles import IdentifySwizzles
from properties.SwizzleTransferable import SwizzleTransferable
from properties.SynthSwizzleTransferable import SynthSwizzleTransferable
from properties.FusedSwizzleTranslator import FusedSwizzleTranslator
from properties.Translator import Translator
from properties.ScaledTranslator import ScaledTranslator
from properties.EqualOnValues import EqualOnValues
from properties.EqualOnValuesDepth import EqualOnValuesDepth
from properties.LargeExpressionTranslator import LargeExpressionTranslator
from properties.EqClassEqualOnValuesDepth import EqClassEqualOnValuesDepth
from properties.EqClassEqualDepth import EqClassEqualDepth
from properties.ExtractLaneSlice import ExtractLaneSlice

from sema.hexsemantics_new import semantics as hvx_semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.halide_sema import halide_semantics
from sema.hex_swizzles import hvx_swizzles
from sema.x86_swizzles import x86_swizzles
from sema.ARMSema import arm_semantics
from sema.repairs_sema import repair_semantics
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HVX_SYNTH_DESC, HALIDE_HVX_SYNTH_DESC,ARM_SYNTH_DESC
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HVX_SYNTH_DESC, HALIDE_HVX_SYNTH_DESC,ARM_SYNTH_DESC, create_synth_desc

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
args = parser.parse_args()
PARALLEL = args.parallel


TARGETS = [ "x86", "hvx", "halide_hvx", "arm"]
test_properties = [Commutative, Associative, Distributive, SimplifyingIdentity, IdentifySwizzles, SimplifyingSwizzles, SwizzleTransferable, SynthSwizzleTransferable, FusedSwizzleTranslator, Translator, ScaledTranslator, LargeExpressionTranslator]




TARGET_TO_SEMA = {
    "x86": x86_semantics,
    "hvx": hvx_semantics,
    "halide_hvx": halide_semantics,
    "arm" : arm_semantics,
}


TARGET_TO_SWIZZLE = {
    "x86": x86_swizzles,
    "hvx": hvx_swizzles,
    "halide_hvx": {},
    "arm" : {},
}


TARGET_TO_DESC = {
    "x86": X86_SYNTH_DESC,
    "hvx": HVX_SYNTH_DESC,
    "halide_hvx": HALIDE_HVX_SYNTH_DESC,
    "arm": ARM_SYNTH_DESC,
}










TARGETS = ["hvx"]
test_properties = [Translator, SimplifyingSwizzles, SwizzleTransferable, SynthSwizzleTransferable, FusedSwizzleTranslator]
#test_properties = [SimplifyingSwizzles, FusedSwizzleTranslator]

test_properties = [EqualOnValues, ScaledTranslator]
test_properties = [LargeExpressionTranslator]
test_properties = [SimplifyingSwizzles , SwizzleTransferable, SynthSwizzleTransferable ,EqualOnValuesDepth][2:]
test_properties = [EqClassEqualOnValuesDepth]


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

        elif property is FusedSwizzleTranslator:
            swizzle_dict = TARGET_TO_SWIZZLE[target]
            swizzles = parse_dict(swizzle_dict)
            print("Total Swizzle classes: ", len(swizzles))
            halide_dsl_list = parse_dict(halide_semantics)
            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, target_dsl_list = halide_dsl_list, shuffle_deriviation_map_path="hvx_swizzle_derivation_map.JSON", swizzles = swizzles )

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
            PropertyInstance = property(dsl_list = dsl_list, synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, output_dsl_list = halide_dsl_list, repair_dsl_list = repairs_sema)
        elif property is EqClassEqualDepth:
            halide_dsl_list = parse_dict(halide_semantics)
            target_swizzles = parse_dict(TARGET_TO_SWIZZLE[target])
            forward_path_name = "repair_forward_map.json"
            swizzle_forward_path = "hvx_swizzle_derivation_map.JSON"
            PropertyInstance = property(dsl_list = dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, target_dsl_list = halide_dsl_list, output_depth = 2, forward_map_path = forward_path_name, swizzle_dsl_list = target_swizzles, swizzle_map_path = swizzle_forward_path)

        elif property is LargeExpressionTranslator:
            swizzle_dict = TARGET_TO_SWIZZLE[target]
            swizzles = parse_dict(swizzle_dict, keep_duplicate = True)
            print("Total Swizzle classes: ", len(swizzles))
            halide_dsl_list = parse_dict(halide_semantics)
            PropertyInstance = property(target_dsl_list = dsl_list, target_synth_desc = synthesizer_desc, source_synth_desc = HALIDE_HVX_SYNTH_DESC, dsl_list = halide_dsl_list, shuffle_deriviation_map_path="hvx_swizzle_derivation_map.JSON", swizzles = swizzles, context_deriviation_map_path = "backward_map.json", input_depth = 2)

        else:
            PropertyInstance = property(dsl_list = dsl_list, synth_desc= synthesizer_desc)
        PropertyInstance.parallel = PARALLEL
        property_map = PropertyInstance.get_property()


        property_label = target+"_"+PropertyInstance.name
        with open("{}.py".format(PropertyInstance.name+property_result_suffix), "w+") as DumpFile:
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


