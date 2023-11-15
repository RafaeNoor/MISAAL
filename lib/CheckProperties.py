
# Main driver for checking properites


from common.DSLParser import parse_dict

from properties.Commutative import *
from properties.Distributive import *
from properties.Associative import *
from properties.SimplifyingIdentity import SimplifyingIdentity
from properties.IdentifySwizzles import IdentifySwizzles
from properties.SwizzleTransferable import SwizzleTransferable

from sema.hexsemantics_new import semantics as hvx_semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.halide_sema import halide_semantics
from sema.hex_swizzles import hvx_swizzles
from sema.x86_swizzles import x86_swizzles
from sema.ARMSema import arm_semantics
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HVX_SYNTH_DESC, HALIDE_HVX_SYNTH_DESC,ARM_SYNTH_DESC
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HVX_SYNTH_DESC, HALIDE_HVX_SYNTH_DESC,ARM_SYNTH_DESC, create_synth_desc

from properties.SimplifyingSwizzles import SimplifyingSwizzles

import json
import sys

import json

TARGETS = [ "x86", "hvx", "halide_hvx", "arm"]
test_properties = [Commutative, Associative, Distributive, SimplifyingIdentity, IdentifySwizzles, SimplifyingSwizzles, SwizzleTransferable]




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
test_properties = [SimplifyingSwizzles]


for property in test_properties:
    for target in TARGETS:
        dsl_list = parse_dict(TARGET_TO_SEMA[target])
        synthesizer_desc = TARGET_TO_DESC[target]
        property_result_suffix = "_{}_results".format(target)

        PropertyInstance = None
        if property is SwizzleTransferable:
            PropertyInstance = property(dsl_list = dsl_list, synth_desc = synthesizer_desc, swizzles = parse_dict(hvx_swizzles))
        elif property is SimplifyingSwizzles:
            swizzle_dict = TARGET_TO_SWIZZLE[target]
            swizzles = parse_dict(swizzle_dict)
            print("Total Swizzle classes: ", len(swizzles))
            swizzles = swizzles[:2]

            swizzle_synth_desc = create_synth_desc("{}-swizzles".format(target), True, TARGET_TO_DESC[target].target_vector_sizes)
            PropertyInstance = SimplifyingSwizzles(dsl_list = swizzles, synth_desc = swizzle_synth_desc,input_depth = 2)

        else:
            PropertyInstance = property(dsl_list = dsl_list, synth_desc= synthesizer_desc)
        PropertyInstance.parallel = False
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


