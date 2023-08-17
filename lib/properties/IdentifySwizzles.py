from properties.Property import Property
from  utils.DSLInstructionUtils import *
import copy
from  common.Types import *

class IdentifySwizzles(Property):


    def __init__(self, dsl_list = [], synth_desc = None,  profile_prefix = "_prof", num_input_sources = [2, 4]):
        super().__init__(name = "IdentifySwizzles" ,dsl_list = dsl_list, synth_desc = synth_desc)
        self.profile_prefix  = profile_prefix
        self.num_input_sources = num_input_sources
        self.swizzle_context_map = {}




    def get_property_desc(self):
        return "Instruments DSL instructions to identify the required swizzles to use cross-lane operations"

    def generate_candidates(self):
        """Generates a list of DSL Instructions (i.e. equivalence classes for which we will attempt to identify the swizzle sequence).
        Currently we're attemping to find those cases where cross-lane behavior is observed in the form of reductions. More general
        swizzles can be extended later.

        For those instructions where we can observe reductions, we instrument the code to emit the bitvector slices being extracted
        so that we may infer the required shuffles.

        Returns:
            [(DSL_Instruction, InstrumentedSemantics, num_sources, target_vector_size)]
        """


        candidates = []
        for dsl_inst in self.dsl_list:
            if "mask" in dsl_inst.name:
                continue
            if self.instruction_may_access_cross_lane(dsl_inst):
                for num_sources in self.num_input_sources:
                    for target_size in self.synth_desc.get_target_vector_sizes():
                        candidates.append((dsl_inst, self.get_instrumented_semantics(dsl_inst), num_sources, target_size))


        #candidates = [cand for cand in candidates if "_mm256_hadd_epi32" in cand[0].name]

        print("Candidates:")
        for cand in candidates:
            print(cand[0].name, "num_sources: ", cand[2],"target_size", cand[3])




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

    def handle_profile_extract(self, extract_call):

        operands = extract_call.split("extract")[-1].split(")")[0].strip().split()

        hi = operands[0]
        lo = operands[1]
        arg = operands[2]

        return "(printf \"EXTRACT ~a ~a FROM ~a \\n\" {} {} \"{}\")".format(hi, lo, arg)


    def is_store_line(self, line):
        not_include  = ["define", "bvpadhighbits", "for/list", "cond"]
        include  = ["%"]


        not_include_cond = all([word not in line for word in not_include])
        include_cond = all([word in line for word in include])

        return not_include_cond and include_cond

    def get_instrumented_semantics(self, dsl_inst):
        new_sema = []

        apply_cond = False
        for line in dsl_inst.semantics:
            if "apply" in line:
                apply_cond = True

            if "cond" in line:
                apply_cond = True

            if dsl_inst.name in line:
                new_sema.append(line.replace(dsl_inst.name, self.get_profiling_name(dsl_inst)).replace("\"", ""))
            elif "extract" in line:
                profile_call = self.handle_profile_extract(line)
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





    def property_holds_on_candidate(self, candidate):
        print("Processing Candidate: ", candidate[0].name, "with sources", candidate[2])

        dsl_inst = candidate[0]
        modified_sema = candidate[1]
        num_sources = candidate[2]
        target_size = candidate[3]

        sample_context = None

        for ctx in dsl_inst.contexts:
            if "mask" not in  ctx.name:
                sample_context = ctx
                break


        if sample_context == None:
            return False

        print("Sample context name: ", sample_context.name)
        bv_streams = self.get_bv_streams(dsl_inst, modified_sema, num_sources, sample_context)

        print(bv_streams)

        arg_map = self.get_dsl_inst_formal_arg_to_size_map(dsl_inst, sample_context)

        swizzle_contexts = self.identify_swizzles(bv_streams, target_vector_sizes = [target_size], max_distinct_inputs = num_sources, var_to_size_map = arg_map, prec = sample_context.in_precision)


        self.swizzle_context_map[dsl_inst.name] = swizzle_contexts


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
            else:
                args.append(str(arg.value))



        prof_name = self.get_profiling_name(dsl_inst)

        call_method = " ".join(["(", prof_name] + args + [")"])

        bind_to_var = "(define result {})".format(call_method)

        statements.append(bind_to_var)

        fname_prefix = get_random_tempfile_name()


        output_log = execute_racket_file_and_read_from_file(statements, fname_prefix)


        return output_log













    def get_dsl_inst_formal_arg_to_size_map(self,dsl_inst, sample_context):

        func_prototype =  dsl_inst.semantics[0]

        # Operands are ordered in the order they appear in the prototype
        formal_args = func_prototype.strip().split("(")[-1].split(")")[0].strip().split(" ")[1:]

        formal_args = [arg for arg in formal_args if arg != '']



        print(formal_args)
        arg_to_size_map = {}

        for idx, arg in enumerate(sample_context.context_args):
            if isinstance(arg, BitVector) or isinstance(arg, ConstBitVector):
                arg_to_size_map[formal_args[idx]] = arg.size

        return arg_to_size_map

    def identify_swizzles(self, bv_streams, target_vector_sizes = [], max_distinct_inputs = None, var_to_size_map = {}, prec = 16):

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

        shuffle_contexts += self.generate_intra_iteration_access_swizzle_old(var_to_size_map, streams,  max_distinct_inputs, target_vector_sizes, prec)

        return shuffle_contexts


    def identify_stream_precision(self, stream):
        for idx, a_iter in enumerate(stream):
            for src_idx, rng in enumerate(a_iter):
                hi = int(rng.split(" ")[0])
                lo = int(rng.split(" ")[1])
                prec = hi - lo + 1
                return prec



    def generate_intra_iteration_access_swizzle_old(self, var_to_size_map, streams, max_distinct_inputs, target_vector_sizes, prec ):

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





                    #if len(a_iter) != num_a_sources:
                    #    break

                    for src_idx, rng in enumerate(a_iter):
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
                        #slice_range = (((index_modulo * base_vect_size) + (iteration * step_size)) // prec) + (starts[index_modulo] )
                        #print("Slice left:", (((index_modulo * base_vect_size) + (iteration * step_size)) // prec))
                        #print("Slice Right:", (starts[index_modulo] ))

                        source_lowest_index = index_modulo * (base_vect_size // prec)# lowest address of index_modulo arg
                        slice_range = starts[index_modulo] + source_lowest_index

                        print("Slice_Range:", slice_range)
                        shuffle_vector_args.append((index_modulo,slice_range))
                        starts[index_modulo] -= 1

                print("Shuffle vector arguments")
                shuffle_vector_args = self.blocked_reverse(shuffle_vector_args, num_a_sources)
                print(shuffle_vector_args)

                datum = (shuffle_vector_args,  {"result_size": a_size, "operand_size": base_vect_size, "prec": prec, "num_sources": num_a_sources})

                # Different streams may identify the same swizzle patterns
                if datum not in intra_shuffle_contexts:
                    print(datum)
                    intra_shuffle_contexts.append(datum)


        return intra_shuffle_contexts



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
        return candidate[0].name

    def get_property_on_candidate(self, candidate):
        return {"candidate": candidate[0].name ,"num_sources": candidate[2] ,"swizzle_args": self.swizzle_context_map[candidate[0].name], "operand_size": candidate[3]}

















