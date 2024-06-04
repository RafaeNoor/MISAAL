from properties.Property import *
from  utils.DSLInstructionUtils import *
import copy
from  common.Types import *

class IdentifySwizzles(Property):


    def __init__(self, dsl_list = [], synth_desc = None,  profile_prefix = "_prof", num_input_sources = [2, 4]):
        super().__init__(name = "IdentifySwizzles" ,dsl_list = dsl_list, synth_desc = synth_desc)
        self.profile_prefix  = profile_prefix
        self.num_input_sources = num_input_sources
        self.swizzle_context_map = {}
        self.profile_only_params = True
        self.elem_bitwidths = [8, 16, 32]




    def get_property_desc(self):
        return "Instruments DSL instructions to identify the required swizzles to use cross-lane operations"

    def generate_candidates(self):
        """Generates a list of DSL Instructions (i.e. equivalence classes for which we will attempt to identify the swizzle sequence).
        Currently we're attemping to find those cases where cross-lane behavior is observed in the form of reductions. More general
        swizzles can be extended later.

        For those instructions where we can observe reductions, we instrument the code to emit the bitvector slices being extracted
        so that we may infer the required shuffles.

        Returns:
            [(DSL_Instruction, InstrumentedSemantics, num_sources, target_vector_size, ctx)]
        """


        candidates = []
        for dsl_inst in self.dsl_list:
            if "mask" in dsl_inst.name:
                continue
            if dsl_inst.has_bounded_behavior():
                dsl_inst = convert_bounded_dsl_inst_to_multiple_contexts(dsl_inst)
            #if dsl_inst.name not in ["vdotq_s32"]:
            #    continue

            if self.instruction_may_access_cross_lane(dsl_inst) or True:
                for num_sources in self.num_input_sources:
                    for target_size in self.synth_desc.get_target_vector_sizes():
                        for ctx in dsl_inst.contexts:
                            candidates.append((dsl_inst, self.get_instrumented_semantics(dsl_inst), num_sources, target_size, ctx))

        #candidates = [cand for cand in candidates if "unpack" in cand[0].name ]



        #for cand in candidates:
        #    print(cand[0].name, "num_sources: ", cand[2],"target_size", cand[3], cand[4].name)




        return candidates


    def instruction_may_access_cross_lane(self, dsl_inst):
        sema = dsl_inst.get_semantics()

        # Explicitly performs a reduction
        if ".red" in sema:
            return True

        # Another possibility for cross lane access may come
        # in the form of multiple accesses from the same input
        # vector operand for a single iteration of deriving the
        # output.

        operand_access_counter = {}

        for line in dsl_inst.semantics:
            if "extract" in line:
                source = line.split("extract")[-1].split(")")[0].strip().split()[2]
                hi = line.split("extract")[-1].split(")")[0].strip().split()[0]
                lo = line.split("extract")[-1].split(")")[0].strip().split()[1]

                if source not in operand_access_counter:
                    operand_access_counter[source] = {"count": 0, "slice": []}

                operand_access_counter[source]["count"] += 1
                operand_access_counter[source]["slice"] += [(hi,lo)]


        if "sign" in dsl_inst.name:
            print(operand_access_counter)
        for source, access_desc in operand_access_counter.items():
            # Accesses must check number of distinct slices accessed, repeated access
            # to the same addresses do not count.
            if access_desc['count'] > 1 and len(list(set(access_desc['slice']))) > 1:
                return True
        return False



    def get_profiling_name(self, dsl_inst):
        return dsl_inst.name + self.profile_prefix

    def handle_profile_extract(self, extract_call, formal_params):

        operands = extract_call.split("extract")[-1].split(")")[0].strip().split()

        hi = operands[0]
        lo = operands[1]
        arg = operands[2]


        if self.profile_only_params and arg not in formal_params:
            return ""
        return "(printf \"EXTRACT ~a ~a FROM ~a \\n\" {} {} \"{}\")".format(hi, lo, arg)


    def is_store_line(self, line):
        not_include  = ["define", "bvpadhighbits", "for/list", "cond"]
        include  = ["%"]


        not_include_cond = all([word not in line for word in not_include])
        include_cond = all([word in line for word in include])

        return not_include_cond and include_cond

    def get_instrumented_semantics(self, dsl_inst):
        new_sema = []


        original_sema = dsl_inst.semantics

        arg_map = self.get_dsl_inst_formal_arg_to_size_map(dsl_inst, dsl_inst.contexts[0])
        formal_params = [key for key in arg_map]
        try:
            # Pre-processing
            dsl_inst.semantics = inline_nested_extracts_in_sema(dsl_inst.semantics)
            dsl_inst.semantics = remove_redundant_extracts(dsl_inst.semantics, arg_map)
        except:
            dsl_inst.semantics = original_sema

        apply_cond = False
        for line_idx, line in enumerate(dsl_inst.semantics):
            if "apply" in line:
                next_line = dsl_inst.semantics[line_idx+1]
                if "concat" not in next_line:
                    apply_cond = True

            if "cond" in line:
                apply_cond = True

            if dsl_inst.name in line:
                new_sema.append(line.replace(dsl_inst.name, self.get_profiling_name(dsl_inst)).replace("\"", ""))
            elif "extract" in line:
                profile_call = self.handle_profile_extract(line, formal_params)
                new_sema.append(profile_call)
                new_sema.append(line.replace("\"",""))
                pass
            elif self.is_store_line(line):
                if apply_cond:
                    new_sema.append(line.replace("\"", ""))
                    apply_cond = False
                else:
                    new_sema.append('(printf \"STORE\\n\")')
                    new_sema.append(line.replace("\"", ""))
            else:
                new_sema.append(line.replace("\"", ""))

        return "\n".join(new_sema)



    def does_inst_sema_combine_slices(self, dsl_inst):
        apply_cond = False
        for line_idx, line in enumerate(dsl_inst.semantics):
            if "apply" in line:
                next_line = dsl_inst.semantics[line_idx+1]
                if "concat" not in next_line:
                    apply_cond = True

            if "cond" in line:
                apply_cond = True

            if dsl_inst.name in line:
                continue
            elif "extract" in line:
                continue
            elif self.is_store_line(line):
                if apply_cond:
                    apply_cond = False
                else:
                    return True
            else:
                continue


        return False





    def property_holds_on_candidate(self, candidate):
        print("Processing Candidate: ", candidate[0].name, "with sources", candidate[2])

        dsl_inst = candidate[0]
        modified_sema = candidate[1]
        num_sources = candidate[2]
        target_size = candidate[3]
        sample_context = candidate[4]

        if sample_context.in_precision is None:
            return False


        if sample_context.out_precision is None:
            return False


        print("Sample context name: ", sample_context.name)
        swizzle_contexts = []
        bv_streams = self.get_bv_streams(dsl_inst, modified_sema, num_sources, sample_context)

        print(bv_streams)

        arg_map = self.get_dsl_inst_formal_arg_to_size_map(dsl_inst, sample_context)

        swizzle_contexts = self.identify_swizzles(dsl_inst, bv_streams, target_vector_sizes = [target_size], max_distinct_inputs = num_sources, var_to_size_map = arg_map, input_prec = sample_context.in_precision, output_prec = sample_context.out_precision, output_size = sample_context.out_vectsize)


        self.swizzle_context_map[sample_context.name] = swizzle_contexts


        return swizzle_contexts != []


    def get_bv_streams(self, dsl_inst, modified_sema, num_sources, sample_context):

        # declare modified semantics
        statements = [modified_sema]

        args = []

        print(dsl_inst.name, ": ", sample_context)

        for arg in sample_context.context_args:
            if isinstance(arg, BitVector):
                args.append("(bv 0 {})".format(arg.size))
            elif isinstance(arg, ConstBitVector):
                args.append(arg.get_rkt_value())
            elif isinstance(arg, Reg):
                print(sample_context.emit_context_expr_string())
                assert False, "Unreachable"
            else:
                args.append(str(arg.value))



        prof_name = self.get_profiling_name(dsl_inst)

        call_method = " ".join(["(", prof_name] + args + [")"])

        bind_to_var = "(define result {})".format(call_method)

        statements.append(bind_to_var)

        fname_prefix = get_random_tempfile_name()


        output_log = execute_racket_file_and_read_from_file(statements, fname_prefix)


        return output_log






    def is_inst_swizzle(self, dsl_inst):

        # We consider an instruction to be a swizzle instruction
        # if it purely performs extraction and concatenations only.

        sample_ctx = dsl_inst.get_sample_context()

        bv_ops = sample_ctx.get_bv_ops()

        op_cond = all([op in ["extract", "concat"] for op in bv_ops])



        return op_cond










    def get_dsl_inst_formal_arg_to_size_map(self,dsl_inst, sample_context):

        func_prototype =  dsl_inst.semantics[0]

        # Operands are ordered in the order they appear in the prototype
        formal_args = func_prototype.strip().split("(")[-1].split(")")[0].strip().split(" ")[1:]

        formal_args = [arg for arg in formal_args if arg != '']



        #print(formal_args)
        arg_to_size_map = {}

        for idx, arg in enumerate(sample_context.context_args):
            if isinstance(arg, BitVector) or isinstance(arg, ConstBitVector):
                arg_to_size_map[formal_args[idx]] = arg.size

        return arg_to_size_map

    def identify_swizzles(self, dsl_inst,  bv_streams, target_vector_sizes = [], max_distinct_inputs = None, var_to_size_map = {}, input_prec = 16, output_prec = 16, output_size = 256):

        data = bv_streams.strip().split("STORE")
        iterations = []

        target_vector_sizes.sort()

        for iter in data:
            iterations.append(iter.strip().split("\n"))


        streams = {}
        for iter in iterations:
            iter_stream  = {}
            for extract in iter:
                if "EXTRACT" not in extract:
                    continue

                src = extract.split("FROM")[-1].strip()

                if src not in iter_stream:
                    iter_stream[src] = []

                ranges = extract.split('EXTRACT')[-1].split('FROM')[0].strip()

                # Only include unique accesses
                if ranges not in iter_stream[src]:
                    iter_stream[src].append(ranges)

            for key in iter_stream:
                if key not in streams:
                    streams[key] = []

                streams[key].append(iter_stream[key])


        print(streams)


        shuffle_contexts = []

        #TEMP UNCOMMENT
        shuffle_contexts += self.generate_intra_iteration_access_swizzle(var_to_size_map, streams,  max_distinct_inputs, target_vector_sizes, input_prec, output_prec)

        combine_slices = self.does_inst_sema_combine_slices(dsl_inst)

        shuffle_contexts += self.generate_inter_iteration_access_swizzle(var_to_size_map, streams,  max_distinct_inputs, target_vector_sizes, input_prec, output_prec, output_size, combine_slices = combine_slices)

        return shuffle_contexts


    def identify_stream_precision(self, stream):
        for idx, a_iter in enumerate(stream):
            for src_idx, rng in enumerate(a_iter):
                hi = int(rng.split(" ")[0])
                lo = int(rng.split(" ")[1])
                prec = hi - lo + 1
                return prec



    def generate_inter_iteration_access_swizzle(self, var_to_size_map, streams, max_distinct_inputs, target_vector_sizes, input_prec, output_prec, output_size, combine_slices = False ):
        """SIMD operations which access non-contigous slices across iterations. For example:

        op [a0, a1, a2, a3] = [fn[a0], fn[a2], fn[a1], fn[a3]]

        In such cases we can derive two different swizzles:
        1. Reorder the input such that the output is produced in a contigous manner:
            swizzle_operand([a0, a1, a2, a3]) => [a0, a2 , a1, a3]
            op[ a0, a2, a1, a3 ]  =[fn[a0], fn[a1], fn[a2], fn[a3]]

        2. Reorder the output such that operation is applied on elements
            in a contigous manner

            ;output index:    0        1       2       3           0       2       1       3
            swizzle_output([fn[a0], fn[a2], fn[a1], fn[a3]]) => [fn[a0], fn[a1], fn[a2], fn[a3]]

        We find such relations across operands and outputs. Currently, we limit ourselves
        to those operands and outputs which contain the same number of elements (but the element-bitwidth
        can be different, and in most of these cases is).
        """

        inter_shuffle_contexts = []


        for test_key in list(streams.keys()):
            a_streams = streams[test_key]
            a_size = var_to_size_map[test_key]
            base_vect_size = None

            # For HVX and other targets, operands actually take mixed precision, so we should
            # determine the specific prec being used for a given stream

            input_prec = self.identify_stream_precision(a_streams)
            print("Stream precision identified to be: ", input_prec, "for ", a_streams[0])


            num_input_elems = a_size // input_prec
            num_output_elems = output_size // output_prec

            if num_input_elems != num_output_elems:
                continue


            base_vect_size = None
            for target_size in target_vector_sizes:
                if target_size >= a_size and target_size % a_size == 0:
                    print("Using Target Size:", target_size)
                    base_vect_size = target_size
                    break


            if base_vect_size == None:
                print("Unable to split ", a_size ,"into", target_vector_sizes)
                continue


            # Each element of access pair is defined as:
            # (input_idx, output_idx)
            access_pair = []

            range_map = {}
            for idx, a_iter in enumerate(reversed(a_streams)):

                # Only those instructions which access a single element for at-least one operand per iteration to calculate the outut are considered in this method. Multiple accesses for an operand within a single iteration are handled seperately.
                if len(a_iter) != 1:
                    break


                input_slice = a_iter[0]


                if input_slice in range_map:
                    memo_entry = range_map[input_slice]
                    memo_result = (memo_entry[0], idx)

                    access_pair.append(memo_result)
                    continue


                hi = int(input_slice.split(" ")[0])
                lo = int(input_slice.split(" ")[1])

                input_idx = lo // input_prec

                datum = (input_idx, idx)

                range_map[input_slice] = datum

                access_pair.append(datum)


            # Check if regular access

            regular_access = True
            for input_idx, output_idx in access_pair:

                if input_idx != output_idx:
                    regular_access = False
                    break
            if regular_access:
                # Check the other operand
                continue


            print("Found Inter-Iteration swizzle candidate")
            print(access_pair)

            # Swizzle operand for ordering
            shuffle_vector_operands = sorted(access_pair, key = lambda x : x[1])


            # Swizzle result according to operand ordering
            shuffle_vector_result = sorted(access_pair, key = lambda x : x[0])

            print("Access Pair Shuffled according to operands")
            print(shuffle_vector_operands)


            print("Access Pair Shuffled according to Result")
            print(shuffle_vector_result)




            shuffle_vector_operands = [(0, input_idx) for (input_idx, output_idx) in shuffle_vector_operands]

            shuffle_vector_result = [(0, output_idx) for (input_idx, output_idx) in shuffle_vector_result]

            operand_datum = {"swizzle_args": shuffle_vector_operands, "result_size": a_size, "operand_size": a_size, "prec": input_prec, "num_sources": 1, "output_prec": input_prec}






            result_datum = {}


            result_datum = {"swizzle_args": shuffle_vector_result, "result_size": output_size, "operand_size": output_size, "prec": output_prec, "num_sources": 1, "output_prec": output_prec}

            if combine_slices:
                result_datum['result_size'] = len(shuffle_vector_result) * input_prec
                result_datum['prec'] = input_prec



            if operand_datum not in inter_shuffle_contexts and self.is_swizzle_datum_legal(operand_datum):
                inter_shuffle_contexts.append(operand_datum)


            if result_datum not in inter_shuffle_contexts  and self.is_swizzle_datum_legal(result_datum) :
                inter_shuffle_contexts.append(result_datum)


            # Adding doubling of precision (and register bitwidth)
            DOUBLE_KEYS = ['result_size', 'prec', 'operand_size', 'output_prec']

            if input_prec * 2 in self.elem_bitwidths:
                doubled_operand_datum = copy.deepcopy(operand_datum)
                for key in DOUBLE_KEYS:
                    doubled_operand_datum[key] = operand_datum[key] * 2

                if doubled_operand_datum not in inter_shuffle_contexts and self.is_swizzle_datum_legal(doubled_operand_datum):
                    inter_shuffle_contexts.append(doubled_operand_datum)


            if output_prec * 2 in self.elem_bitwidths:
                doubled_result_datum = copy.deepcopy(result_datum)
                for key in DOUBLE_KEYS:
                    doubled_result_datum[key] = result_datum[key] * 2

                if doubled_result_datum not in inter_shuffle_contexts and self.is_swizzle_datum_legal(doubled_result_datum):
                    inter_shuffle_contexts.append(doubled_result_datum)



        return inter_shuffle_contexts











    def generate_intra_iteration_access_swizzle(self, var_to_size_map, streams, max_distinct_inputs, target_vector_sizes, prec, output_prec ):

        intra_shuffle_contexts = []

        for test_key in list(streams.keys()):
            a_streams = streams[test_key]
            print(var_to_size_map)
            a_size = var_to_size_map[test_key]

            base_vect_size = None

            num_a_sources = min(len(a_streams[0]), max_distinct_inputs)

            if num_a_sources != max_distinct_inputs:
                continue

            #TEMP:
            print(a_streams[0])
            print("Num Sources: ", max_distinct_inputs)

            if num_a_sources == 1:
                print("Single source case, skipping ... ")

                continue

            # For HVX and other targets, operands actually take mixed precision, so we should
            # determine the specific prec being used for a given stream

            prec = self.identify_stream_precision(a_streams)
            print("Stream precision identified to be: ", prec, "for ", a_streams[0])



            input_slice_size =  a_size // num_a_sources
            print("Input Slice Size: ", input_slice_size)
            num_shuffle_iterations = 1



            for target_size in target_vector_sizes:
                if target_size >= input_slice_size and target_size % input_slice_size == 0:
                    num_shuffle_iterations = target_size //  input_slice_size # 4
                    print("Using Target Size:", target_size)

                    base_vect_size = target_size

                    break


            if base_vect_size == None:
                print("Unable to split ", input_slice_size,"into", target_vector_sizes)
                continue


            step_size = base_vect_size // (num_shuffle_iterations )# * num_a_sources)
            print("Step Size: ", step_size, ", prec: ", prec)
            print("Num Shuffle iterations: ", num_shuffle_iterations)

            indices_per_source = base_vect_size // prec
            indices_per_step = indices_per_source // num_shuffle_iterations

            print("Indices_per_source:" , indices_per_source, "indices_per_step", indices_per_step)
            for iteration in range(num_shuffle_iterations):


                #starts = [((step_size  // prec))-1] * num_a_sources
                starts = [indices_per_source - (iteration * indices_per_step  ) - 1 ]  * num_a_sources

                print("Starts", starts)


            # Each iteration you should sort each stream of extract in descending order

                shuffle_vector_args = []

                print("a_stream:",a_streams)
                for idx, a_iter in enumerate(a_streams):


                    # In HVX, the same slices of the scalar Register are
                    # accessed repeatedly. Hence we only account for the stream
                    # till we have enough indices to produce the shuffle vector
                    if prec * len(shuffle_vector_args) == a_size:
                        break



                    # Within iteration access, must have at-least 2 different accesses

                    if len(a_iter) <= 1:
                        continue

                    print("a_iter:",a_iter)







                    # Maping of ranges to the specific shuffle offset, in case where
                    # the same slice is accessed across iterations.
                    range_map = {}
                    for src_idx, rng in enumerate(a_iter):

                        if rng in range_map:
                            shuffle_vector_args.append((index_modulo,slice_range))
                            continue

                        hi = int(rng.split(" ")[0])
                        lo = int(rng.split(" ")[1])


                        new_prec = hi - lo + 1

                        if new_prec != prec:
                            print("PREC CHANGED! from", prec,"to", new_prec)
                        prec = new_prec
                        print("PREC:", prec)
                        print("Source index:", src_idx)


                        # Index Module selects which source to index from
                        index_modulo = src_idx % num_a_sources
                        print("Index Modulo:", index_modulo)

                        source_lowest_index = index_modulo * (base_vect_size // prec)# lowest address of index_modulo arg
                        slice_range = starts[index_modulo] + source_lowest_index

                        print("Slice_Range:", slice_range)

                        datum = (index_modulo,slice_range)


                        range_map[rng] = datum


                        shuffle_vector_args.append((index_modulo,slice_range))
                        starts[index_modulo] -= 1

                print("Shuffle vector arguments")
                shuffle_vector_args = self.blocked_reverse(shuffle_vector_args, num_a_sources)
                print(shuffle_vector_args)

                datum =  {"swizzle_args": shuffle_vector_args,"result_size": a_size, "operand_size": base_vect_size, "prec": prec, "num_sources": num_a_sources, "output_prec": output_prec}

                # Different streams may identify the same swizzle patterns
                if datum not in intra_shuffle_contexts and self.is_swizzle_datum_legal(datum):
                    print(datum)
                    intra_shuffle_contexts.append(datum)


        return intra_shuffle_contexts

    def is_swizzle_datum_legal(self, datum):
        result_size = datum['result_size']

        if result_size not in self.synth_desc.target_vector_sizes:
            return False

        operand_size = datum['operand_size']

        if operand_size not in self.synth_desc.target_vector_sizes:
            return False

        return True



    # Traces are executed from MSB to LSB, where MSB is the largest bit index.
    # However for ease of readability, in Hydride we say the MSB is 0. Hence this
    # reverse the indices in blocked fashion to respect that convention
    def blocked_reverse(self, shuffle_indices, block_size):

        assert len(shuffle_indices) % block_size == 0 , "Blocked reverse must be applied when we can evenly divide in block sizes"

        ordered_indices = []

        for i in reversed(range(0, len(shuffle_indices), block_size)):
            ordered_indices += shuffle_indices[i:i+block_size]

        return ordered_indices







    def serialize_candidate(self, candidate):
        return candidate[4].name

    def get_property_on_candidate(self, candidate):

        swizzle_prop = self.swizzle_context_map[candidate[4].name]
        return {"candidate": candidate[0].name ,"num_sources": candidate[2] ,"contexts": self.swizzle_context_map[candidate[4].name]}


    def emit_property_to_egg(self, property_map):
        # Does not apply to this property
        return []















