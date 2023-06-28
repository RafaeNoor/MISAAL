
# Main driver for checking properites


from common.DSLParser import parse_dict

from properties.Commutative import *
from properties.Distributive import *
from properties.Associative import *

from sema.hexsemantics_new import semantics as hvx_semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HVX_SYNTH_DESC
import json

test_properties = [Associative, Commutative, Distributive]
test_properties = [Commutative]

TEST_TARGET = "hvx"

dsl_list = []
property_result_suffix = ""
synthesizer_desc = None

if TEST_TARGET == "x86":
    dsl_list = parse_dict(x86_semantics)
    property_result_suffix = "_x86_results"
    synthesizer_desc = X86_SYNTH_DESC
elif TEST_TARGET == "hvx":
    dsl_list = parse_dict(hvx_semantics)
    property_result_suffix = "_hvx_results"
    synthesizer_desc = HVX_SYNTH_DESC
    
#dsl_list = dsl_list[30:34]
for property in test_properties:
    PropertyInstance = property(dsl_list = dsl_list, synth_desc= synthesizer_desc)
    property_map = PropertyInstance.get_property()


    with open("{}.py".format(PropertyInstance.name+property_result_suffix), "w+") as DumpFile:
        DumpFile.write(json.dumps(property_map, indent = 4)) 
