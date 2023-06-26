
# Main driver for checking properites


from common.DSLParser import parse_dict

from properties.Commutative import *
from properties.Distributive import *

from sema.hexsemantics_new import semantics as hvx_semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC
import json

test_properties = [Distributive]



dsl_list = parse_dict(x86_semantics)



for property in test_properties:
    PropertyInstance = property(dsl_list = dsl_list, synth_desc= X86_SYNTH_DESC)
    property_map = PropertyInstance.get_property()


    with open("{}.py".format(PropertyInstance.name+"_results"), "w+") as DumpFile:
        DumpFile.write(json.dumps(property_map, indent = 4)) 
