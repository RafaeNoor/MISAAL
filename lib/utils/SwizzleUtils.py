import string



class Swizzle:
    def __init__(self, num_sources = None, result_size = None, input_prec = None, output_prec = None, operand_size = None, swizzle_args = [], derived_from = ""):

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

            index = idx

        return index


    def merge_swizzle_context(self, swizzle):
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





def parse_swizzle_object(ctx, class_name):

    if 'prec' in ctx:
        return Swizzle(num_sources = ctx['num_sources'],
                   result_size = ctx['result_size'],
                   operand_size = ctx['operand_size'],
                   input_prec = ctx['prec'],
                   output_prec = ctx['output_prec'],
                   swizzle_args = ctx['swizzle_args'],
                   derived_from = class_name)
    else:
        return Swizzle(num_sources = ctx['num_sources'],
                   result_size = ctx['result_size'],
                   operand_size = ctx['operand_size'],
                   input_prec = ctx['input_prec'],
                   output_prec = ctx['output_prec'],
                   swizzle_args = ctx['swizzle_args'],
                   derived_from = class_name)



def summarize_distinct_swizzles(swizzle_analysis_result):

    swizzles = []


    for key, props  in swizzle_analysis_result.items():
        for prop in props:
            ctxs = prop['property']['contexts']

            for ctx in ctxs:
                swizzle_ctx = parse_swizzle_object(ctx, key)

                existing_match_index = swizzle_ctx.get_matching_swizzle_context_index(swizzles)

                if existing_match_index == -1:
                    swizzles.append(swizzle_ctx)
                else:
                    swizzles[existing_match_index].merge_swizzle_context(swizzle_ctx)



    print("Number of Distinct Swizzle Classes: ", len(swizzles))

    for swizzle in swizzles:
        swizzle.interpret_swizzle_context()




