import string
import copy
import json
import os

from utils.WriteDSL import write_dsl_dict_to_file, convert_dsl_list_to_dict


class Swizzle:
    def __init__(self, num_sources = None, result_size = None, input_prec = None, output_prec = None, operand_size = None, swizzle_args = [], derived_from = "", name = ""):

        self.name = name
        self.num_sources = num_sources
        self.result_size = result_size
        self.input_prec = input_prec
        self.output_prec = output_prec
        self.operand_size = operand_size
        self.swizzle_args = [swizzle_args]
        self.names = [derived_from]

    def get_matching_swizzle_context_index(self, list_of_swizzles):
        index = -1

        for idx, swizzle in enumerate(list_of_swizzles):
            if swizzle.num_sources != self.num_sources:
                continue
            if swizzle.result_size != self.result_size:
                continue
            if swizzle.input_prec != self.input_prec:
                continue
            if swizzle.operand_size != self.operand_size:
                continue
            if swizzle.output_prec != self.output_prec:
                continue

            # TODO: Should we check if masks are the same?
            if swizzle.swizzle_args[0] != self.swizzle_args[0]:
                continue


            index = idx

        return index


    def is_valid(self):
        # Currently, the way we interpret swizzles may emit an incomplete mask which is unable to generate
        # the required size. TODO:

        # The number of bits which the shuffle mask provides should be equal to the number of the result bits. Otherwise the swizzle is ambigous.
        bits_accounted_for = 0

        assert len(self.swizzle_args) == 1, "Expecting single swizzle args context"

        shuffle_mask = self.swizzle_args[0]

        for operand_index, total_index in shuffle_mask:
            bits_accounted_for += self.input_prec


        return bits_accounted_for == self.result_size

    def merge_swizzle_context(self, swizzle):
        print("Merging swizzle ", self.name , "with", swizzle.name)
        combined_names = self.names + swizzle.names
        self.names = list(set(combined_names))

        combined_swizzle_args = self.swizzle_args

        for args in swizzle.swizzle_args:
            if args not in combined_swizzle_args:
                combined_swizzle_args.append(args)

        self.swizzle_args = combined_swizzle_args



    def create_inputs(self, num_inputs, elem_bw, input_size):
        alphabets = list(string.ascii_lowercase)
        operands = []
        for i in range(num_inputs):
            alphabet = alphabets[i]
            operand = ["{}{}".format(alphabet, j) for j in range(input_size // elem_bw)]
            operands.append(operand)
        return operands


    def apply_shuffle_vector(self,shuffle_vector_args, operands):
        result = []

        for operand_index, total_index in shuffle_vector_args:
            operand = operands[operand_index]

            intra_operand_index = total_index - (operand_index * len(operand))

            result.append(operand[intra_operand_index])

        return result


    def interpret_swizzle_context(self):

        print("X"* 100)

        num_inputs = self.num_sources
        elem_bw = self.input_prec
        output_bw = self.output_prec
        input_size = self.operand_size
        result_size = self.result_size

        print("Number of Operands:", num_inputs)
        print("Element Bitwidth:", elem_bw)
        print("Output Bitwidth:", output_bw)
        print("Input Size:", input_size)
        print("Result Size:", result_size)

        print("Following Swizzle is valid for:")

        for name in self.names:
            print("***", name)
        for swizzle_patterns in self.swizzle_args:
            print("=" * 50)
            shuffle_vector_args = swizzle_patterns


            operands = self.create_inputs(num_inputs, elem_bw, input_size)

            for idx, op in enumerate(operands):
                print("Operand {}:\n{}".format(idx, op))

            result = self.apply_shuffle_vector(shuffle_vector_args, operands)
            print("Result:\n{}".format(result))

            print("XML:")
            print(self.create_xml_for_swizzle())


    def get_xml_type_string(self, param_size):
        type_string = ""

        if param_size == 64:
            type_string = "__m64"
        elif param_size == 32:
            type_string = "int"
        else:
            type_string = "__m{}i".format(param_size)
        return type_string

    def create_xml_parameter(self, param_name, param_size, param_prec):
        type_string = self.get_xml_type_string(param_size)

        return '<parameter type="{}" varname="{}" etype="UI{}"/>'.format(type_string, param_name, param_prec)

    def create_xml_for_swizzle(self):
        parameters = []

        for i in range(self.num_sources):
            param_name = "v{}".format(i)
            parameter = self.create_xml_parameter( param_name, self.operand_size, self.input_prec)
            parameters.append(parameter)
        parameters = "\n".join(parameters)

        template = copy.deepcopy("""
<intrinsic tech="AVX2" name="{}">
	<type>Integer</type>
	<CPUID>AVX2</CPUID>
	<category>Swizzle</category>
	<return type="{}" varname="dst" etype="UI{}"/>
        {}
	<description>Automatically generated swizzle.</description>
	<operation>
        {}

	</operation>
	<instruction name="{}" form="ymm, ymm, ymm" xed="VPUNPCKLBW_YMMqq_YMMqq_YMMqq"/>
	<header>immintrin.h</header>
</intrinsic>
        """).format(self.name, self.get_xml_type_string(self.result_size),
                   self.output_prec, parameters, self.emit_swizzle_to_pseudocode(), self.name )

        return template


    def emit_swizzle_to_pseudocode(self):
        """
        We currently emit to x86 syntax to leverage the existing x86 parser

        """

        statements = []
        shuffle_vector_args = self.swizzle_args[0]

        for idx, (operand_index, total_index) in enumerate(shuffle_vector_args):
            operand_name = "v{}".format(operand_index)

            local_index = total_index - (operand_index * (self.operand_size // self.input_prec))

            local_slice_low = local_index * self.input_prec
            local_slice_high = local_slice_low + self.input_prec - 1 # inclusive indexing

            #output_slice_low = idx * self.output_prec
            #output_slice_high = output_slice_low + self.output_prec -1

            output_slice_low = idx * self.input_prec
            output_slice_high = output_slice_low + self.input_prec -1

            statement = "dst[{}:{}] := {}[{}:{}]".format(output_slice_high,
                                                         output_slice_low,
                                                         operand_name,
                                                         local_slice_high,
                                                         local_slice_low)

            statements.append(statement)
        return "\n".join(statements)











def parse_swizzle_object(ctx, class_name, swizzle_name):

    if 'prec' in ctx:
        return Swizzle(num_sources = ctx['num_sources'],
                   result_size = ctx['result_size'],
                   operand_size = ctx['operand_size'],
                   input_prec = ctx['prec'],
                   output_prec = ctx['output_prec'],
                   swizzle_args = ctx['swizzle_args'],
                   derived_from = class_name, name = swizzle_name)
    else:
        return Swizzle(num_sources = ctx['num_sources'],
                   result_size = ctx['result_size'],
                   operand_size = ctx['operand_size'],
                   input_prec = ctx['input_prec'],
                   output_prec = ctx['output_prec'],
                   swizzle_args = ctx['swizzle_args'],
                   derived_from = class_name, name = swizzle_name)



def summarize_distinct_swizzles(swizzle_analysis_result, target_name = "misaal"):

    swizzles = []


    sid = 0
    for key, props  in swizzle_analysis_result.items():
        for prop in props:
            ctxs = prop['property']['contexts']
            class_name = prop['property']['candidate']

            for ctx in (ctxs):
                swizzle_name = "{}_swizzle_{}".format(target_name, sid)
                sid+= 1
                #swizzle_ctx = parse_swizzle_object(ctx, key, swizzle_name)
                swizzle_ctx = parse_swizzle_object(ctx, class_name, swizzle_name)

                if not swizzle_ctx.is_valid():
                    print(swizzle_name, "is in valid!")
                    continue

                existing_match_index = swizzle_ctx.get_matching_swizzle_context_index(swizzles)

                if existing_match_index == -1:
                    swizzles.append(swizzle_ctx)
                else:
                    swizzles[existing_match_index].merge_swizzle_context(swizzle_ctx)



    print("Number of Distinct Swizzle Classes: ", len(swizzles))

    derivation_map = {}

    intrins = []
    for swizzle in swizzles:
        derivation_map[swizzle.name] = swizzle.names
        swizzle.interpret_swizzle_context()
        intrins.append(swizzle.create_xml_for_swizzle())


    with open(target_name+"_"+"swizzle_derivation_map.JSON","w+") as JSONFile:
        JSONFile.write(json.dumps(derivation_map, indent = 4))


    with open(target_name+"_"+"swizzles.xml", "w+") as XMLFile:
        XMLFile.write("<intrinsics_list>\n")
        XMLFile.write("\n".join(intrins) +"\n")
        XMLFile.write("</intrinsics_list>\n")






def get_swizzle_derivation_eq_class(swizzle_map_path, swizzle_dsl_list, target_dsl_list):

    assert os.path.exists(swizzle_map_path), "Swizzle map path does not exist"

    def get_eq_class(ctx_name, dsl_list):
        for dsl_inst in dsl_list:
            for ctx in dsl_inst.contexts:
                if ctx.name == ctx_name:
                    return dsl_inst

        print(ctx_name)
        assert False, "Unreachable"

    with open(swizzle_map_path, "r") as SwFile:
        swizzle_entry_data = json.load(SwFile)

    eq_class_summary = {}

    changed = True

    while changed:
        changed = False

        for swizzle_ctx_name in swizzle_entry_data:
            swizzle_eq_class = get_eq_class(swizzle_ctx_name, swizzle_dsl_list)



            for target_ctx_name in swizzle_entry_data[swizzle_ctx_name]:
                target_eq_class = get_eq_class(target_ctx_name,  target_dsl_list)

                if target_eq_class.name not in eq_class_summary:
                    changed = True
                    eq_class_summary[target_eq_class.name] = []

                if swizzle_eq_class.name not in eq_class_summary[target_eq_class.name]:
                    changed = True
                    eq_class_summary[target_eq_class.name].append(swizzle_eq_class.name)
    return eq_class_summary





# After converting swizzles to equivlance classes, Hydride may fold
# target specific swizzles into the same classes which have similar behavior
# but have different typing behavior. For instance, the same equivlance class
# may have swizzles which take in smaller inputs to construct larger inputs, take in
# larger inputs to produce smaller inputs, take in equal size inputs and produce
# same size inputs. This functio seperates these classes into these different categories
# or (others) to aid when enumerating
def split_swizzle_eq_class_by_size_behavior(dsl_list, output_dsl_name, output_path):



    def create_updated_swizzles(ctx_classes, parent_dsl):
        if len(ctx_classes) == 0:
            return None

        orig_name = parent_dsl.name

        if len(ctx_classes) == len(parent_dsl.contexts):
            return parent_dsl

        dsl_inst_copy = copy.deepcopy(parent_dsl)

        ctx_0 = ctx_classes[0]

        dsl_inst_copy.name = ctx_0.name
        dsl_inst_copy.contexts = []

        for ctx in ctx_classes:
            ctx_copy = copy.deepcopy(ctx)
            ctx_copy.dsl_name = dsl_inst_copy.name +"_dsl"
            ctx_copy.semantics[0].replace(parent_dsl.name, ctx_0.name)
            dsl_inst_copy.contexts.append(ctx_copy)
        if ctx_0.extensions != None and 'halide' not in ctx_0.extensions:
            pass
        else:
            # Updated semantic function def according to ctx_0 name
            print("=====")
            print("ORIG NAME", parent_dsl.name, "should become", ctx_0.name)
            print("PRE",dsl_inst_copy.semantics[0])
            dsl_inst_copy.semantics[0] = dsl_inst_copy.semantics[0].replace(parent_dsl.name, ctx_0.name)
            print("POST",dsl_inst_copy.semantics[0])
        return dsl_inst_copy


    updated_dsl_list = []

    for dsl_inst in dsl_list:

        same_size_ctxs = []
        increase_size_ctxs = []
        decrease_size_ctxs = []

        for ctx in dsl_inst.contexts:

            if ctx.in_vectsize > ctx.out_vectsize:
                decrease_size_ctxs.append(ctx)
            elif ctx.in_vectsize < ctx.out_vectsize:
                increase_size_ctxs.append(ctx)
            elif ctx.in_vectsize == ctx.out_vectsize:
                same_size_ctxs.append(ctx)

        test_variants = [ same_size_ctxs, increase_size_ctxs, decrease_size_ctxs]

        for variant in test_variants:
            new_inst  = create_updated_swizzles(variant, dsl_inst)
            if not new_inst is None:
                updated_dsl_list.append(new_inst)


    write_dsl_dict_to_file(convert_dsl_list_to_dict(updated_dsl_list),output_dsl_name, output_path)


    return updated_dsl_list






# For frontends such as Halide, we often have to split vectors and concatenate vectors at different stages
# of the expression. To create the identities required to do so, we first create an identity repair map
# with expressions which extract/ concat slices and the operations themselves. This repair map can be used to derive
# such properties
def create_swizzle_identity_map(dsl_list):
    legal_bv_ops = ["extract", "concat"]
    extract_concat_dsl_list = []

    for dsl_inst in dsl_list:
        dsl_ops = dsl_inst.get_semantics_ops_list()

        valid = True
        for op in dsl_ops:
            if op not in legal_bv_ops:
                valid = False
                break

        if valid:
            sample_ctx = dsl_inst.get_sample_context()
            extract_concat_dsl_list.append(sample_ctx)

    swizzle_map = {}

    for extract_op in extract_concat_dsl_list:
        swizzle_map[extract_op.name] = []

        for dsl_inst in dsl_list:
            sample_ctx = dsl_inst.get_sample_context()
            swizzle_map[extract_op.name].append(sample_ctx.name)

    return swizzle_map


