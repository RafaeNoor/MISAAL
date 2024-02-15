
# Main driver for checking properites


from common.DSLParser import parse_dict

from properties.Commutative import *
from properties.Distributive import *
from properties.Associative import *
from properties.SimplifyingIdentity import SimplifyingIdentity
from properties.IdentifySwizzles import IdentifySwizzles
from properties.SwizzleTransferable import SwizzleTransferable
from properties.Translator import Translator

from sema.hexsemantics_new import semantics as hvx_semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.halide_sema import halide_semantics
from sema.hex_swizzles import hvx_swizzles
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HVX_SYNTH_DESC, HALIDE_HVX_SYNTH_DESC
import json

test_properties = [Commutative, Associative, Distributive, SimplifyingIdentity, IdentifySwizzles]
#test_properties = [ SimplifyingIdentity]
test_properties = [Commutative, Associative, Distributive, IdentifySwizzles]
test_properties = [SwizzleTransferable]




TARGET_TO_SEMA = {
    "x86": x86_semantics,
    "hvx": hvx_semantics,
    "halide_hvx": halide_semantics,
}


TARGET_TO_DESC = {
    "x86": X86_SYNTH_DESC,
    "hvx": HVX_SYNTH_DESC,
    "halide_hvx": HALIDE_HVX_SYNTH_DESC,
}





TARGETS = [ "x86", "hvx", "halide_hvx"]
TARGETS = ["hvx"]


# Halide to HVX synthesis

dsl_list = parse_dict(halide_semantics)

output_list = parse_dict(hvx_semantics)

with open("Boiler.egg", "w+") as WriteFile:
    WriteFile.write(emit_egg_datatypes(dsl_list, cost = 10000))

    WriteFile.write(emit_egg_datatypes(output_list))
