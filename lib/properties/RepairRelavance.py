from properties.Property import *
from properties.IdentifySwizzles import IdentifySwizzles
from  utils.DSLInstructionUtils import *
import copy
from  common.Types import *

class RepairRelavance(IdentifySwizzles):



    def __init__(self, dsl_list = [], synth_desc = None, output_dsl_list = [], repair_dsl_list = [], target_synth_desc = None):

        super().__init__(dsl_list = dsl_list, synth_desc = synth_desc)
        self.name = "RepairRelavance"
        self.is_candidate_generator = True
        self.repair_dsl_list = []
        self.output_dsl_list = output_dsl_list
        self.input_dsl_list = dsl_list
        self.target_synth_desc = target_synth_desc

        self.output_dsl_list = self.output_dsl_list[:1]

        self.input_dsl_list = [d for d in self.input_dsl_list if d.name == "hexagon_V6_vrmpybv_128B"]




    def get_property_desc(self):
        return "Test if a given output dsl instruction may be used to generate target expression"

    def generate_candidates(self):
        for input_dsl in self.input_dsl_list:
            for output_dsl in self.output_dsl_list:
                yield (input_dsl, output_dsl)
                return
        return



    def get_reducing_factor(self, dsl_inst):
        # TODO: implement functionality
        return 4



    def create_prepare_repair_env_func(self, name, slices):
        create_extract = lambda x: "(extract {} {} arg)".format(x[0], x[1])

        concat_expr = "(concat \n{}\n)".format("\n".join([create_extract(s) for s in slices]))

        env_func = "(define ({} arg)\n{}\n)".format(name, concat_expr)

        return env_func




    def create_prepare_repair_env_funcs(self, stream):
        prep_arg_slices = {}

        for line in stream:
            tokens = line.strip().split()
            arg_name = tokens[-1]

            if arg_name not in prep_arg_slices:
                prep_arg_slices[arg_name] = []

            high = tokens[1]
            low = tokens[2]
            prep_arg_slices[arg_name].append((high,low))

        funcs = {}

        for arg in prep_arg_slices:
            funcs[arg] = self.create_prepare_repair_env_func(arg, prep_arg_slices[arg])

        return funcs

    def create_repair_env_function(self, dsl_inst):
        # Once we've identified the bitslices being extracted in a single iteration we have to create a Rosette function which given the original synthesis env creates the spliced env for the repair

        return False

    def emit_prepare_repair_env(self, slice_stream, modified_sema, input_dsl_inst):
        funcs = self.create_prepare_repair_env_funcs(slice_stream)

        prototype = modified_sema.split("\n")[0].strip().split("(define")[-1].strip().split()
        print(prototype)

        sorted_args = []

        for arg in prototype:
            if arg in funcs:
                sorted_args.append(arg)





        prepare_clauses = []

        for idx , arg in enumerate(sorted_args):
            clause = "({} (vector-ref env {}))".format(arg, idx)
            prepare_clauses.append(clause)

        env_function_clauses = [defs for arg, defs in funcs.items()]
        env_function_clauses.append("(vector {})".format(" ".join(prepare_clauses)))

        return "(define (prepare-env env)\n{}\n)".format("\n".join(env_function_clauses))




    def property_holds_on_candidate(self, candidate):
        input_dsl_inst = candidate[0]
        modified_sema = self.get_instrumented_semantics(input_dsl_inst)

        sample_context = input_dsl_inst.contexts[0]
        bv_streams = self.get_bv_streams(input_dsl_inst, modified_sema, 0, sample_context)
        streams = bv_streams.split("STORE")
        stream_0 = streams[0].strip().split("\n")

        modified_env_func = self.emit_prepare_repair_env(stream_0, modified_sema, input_dsl_inst)
        print(modified_env_func)


        output_dsl_inst = candidate[1]




        key = self.serialize_candidate(candidate)
        return True



    def serialize_candidate(self, candidate):
        return candidate[0].name + candidate[1].name

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        return {"candidate": candidate[0].name, "output_expression" : candidate[1].name }








    def emit_property_to_egg(self, property_map):
        return []








