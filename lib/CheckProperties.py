
# Main driver for checking properites


from common.DSLParser import parse_dict

from properties.Commutative import *
from properties.Distributive import *
from properties.Associative import *
from properties.SimplifyingIdentity import SimplifyingIdentity

from sema.hexsemantics_new import semantics as hvx_semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HVX_SYNTH_DESC
import json

test_properties = [Commutative, Associative, Distributive, SimplifyingIdentity]
test_properties = [ SimplifyingIdentity]

TARGET_TO_SEMA = {
    "x86": x86_semantics,
    "hvx": hvx_semantics
}


TARGET_TO_DESC = {
    "x86": X86_SYNTH_DESC,
    "hvx": HVX_SYNTH_DESC
}





TARGETS = ["x86", "hvx"]

for property in test_properties:
    for target in TARGETS:
        dsl_list = parse_dict(TARGET_TO_SEMA[target])
        synthesizer_desc = TARGET_TO_DESC[target]
        property_result_suffix = "_{}_results".format(target)

        PropertyInstance = property(dsl_list = dsl_list, synth_desc= synthesizer_desc)
        property_map = PropertyInstance.get_property()


        with open("{}.py".format(PropertyInstance.name+property_result_suffix), "w+") as DumpFile:
            DumpFile.write(json.dumps(property_map, indent = 4))
