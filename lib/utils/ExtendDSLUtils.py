from common.Types import *
import copy
from utils.WriteDSL import convert_dsl_list_to_dict, write_dsl_dict_to_file
#from sema.bitserial_fused_sema import bitserial_fused_sema
from sema.bitserial_fused_sema_v2 import bitserial_fused_sema_v2 as bitserial_fused_sema
from common.DSLParser import parse_dict
import numpy as np


# Class to create Contexts for given DSLInstructions artificially
# for a given output vector size and element bitwitdths.
class ExtendDSLUtils:

    def __init__(self, extend_to_sizes = [], extend_to_bw = [], output_file_name = "pim_extend_dsl.py", write_to_file = True):
        self.extend_to_sizes = extend_to_sizes
        self.extend_to_bw = extend_to_bw
        self.output_file_name = output_file_name
        self.write_to_file = write_to_file



    def extend(self, dsl_list):

        # First sanatize existing equivlance classes before extending
        dsl_list = self.sanatize_eq_classes(dsl_list)


        # Extend
        dsl_list = self.extend_eq_classes(dsl_list)


        if self.write_to_file:
            dict_form = convert_dsl_list_to_dict(dsl_list)
            write_dsl_dict_to_file(dict_form , self.output_file_name, "pim_extended_dsl", indent = True)


    def get_eq_class_ctx(self, dsl_inst, output_size, bitwidth):

        for ctx in dsl_inst.contexts:
            if ctx.out_vectsize != output_size:
                continue

            if ctx.out_precision != bitwidth:
                continue

            return ctx


        return None



    def add_context(self, dsl_inst, output_size, output_bitwidth):

        print("Here", dsl_inst.name, output_size, output_bitwidth)
        # To extend we first find a parameterization with with
        # the  required output_bitwidth

        valid_ctxs = [ctx for ctx in dsl_inst.contexts if ctx.out_precision == output_bitwidth]
        #assert len(valid_ctxs) != 0, f"Unable to find valid contexts for {dsl_inst.name} at output_precision {output_bitwidth}"
        if len(valid_ctxs) == 0:
            # Possibly extending instructions
            print("Return early no valid context")
            return

        # Next we find a context with at least 128-bit vector sizes to
        # reduce any confusion between parameters which correspond to size
        # and lanes / precisions

        valid_ctxs = [ctx for ctx in valid_ctxs if ctx.out_vectsize >= 64]

        print("Len valid contexts start:", len(valid_ctxs))
        valid_match_prec = [ctx for ctx in valid_ctxs if ctx.out_precision == output_bitwidth]
        invalid_match_prec = [ctx for ctx in valid_ctxs if ctx.out_precision != output_bitwidth]

        valid_ctxs = valid_match_prec + invalid_match_prec
        print("Len valid contexts:", len(valid_ctxs))


        #assert len(valid_ctxs) != 0 , f"Unable to find valid contexts for {dsl_inst.name} at output_precision {output_bitwidth} at output size {128}"

        for ctx_idx, sample_ctx in enumerate(valid_ctxs):
            in_vect_size_matches = True

            io_ratio = sample_ctx.out_vectsize / sample_ctx.in_vectsize
            print(f"IO Ratio:\t{io_ratio}")

            for idx, ctx in enumerate(dsl_inst.contexts):
                bv_args = [arg for arg in ctx.context_args if isinstance(arg, BitVector)]# and arg.size != ctx.in_precision] # Leave the 'scalar' bitvector sizes as is
                ctx_input_sizes = [arg.size for arg in bv_args]
                #print("ctx_input_sizes", ctx_input_sizes, "in_precision:", ctx.in_precision, "comparing to",ctx.in_vectsize)
                if ctx_input_sizes == []:
                    # I.e. has only scalar operands
                    break
                else:
                    in_vect_size_matches = in_vect_size_matches and any([ctx.in_vectsize == size for size in ctx_input_sizes])


            if False and not in_vect_size_matches:
                print(f"Unable to extend {dsl_inst.name} for size {output_size}, bitwidth {output_bitwidth} with ctx {sample_ctx.name}")
                continue
            else:
                bv_sizes = [arg.size for arg in ctx.context_args if isinstance(arg, BitVector)]
                valid_ = False
                for b in bv_sizes:
                    for c in ctx_input_sizes:
                        valid_ = valid_ or (b == c)
                if not valid_:
                    print("not valid_")
                    continue
                print(f"Found match!")




            #extended_name = f"{dsl_inst.name}_extended_size_{output_size}_bw_{output_bitwidth}_ctx_{ctx_idx}"

            new_ctx_args = copy.deepcopy(sample_ctx.unparsed_args)

            valid = True

            for idx, arg in enumerate(new_ctx_args):
                # If it's a constant value (usually bit 1 or 0 keep as is)
                if arg in ["(bv #b1 1)" , "(bv #b0 1)"]:
                    continue

                if "SYMBOLIC_BV_" in arg:
                    arg_size = int(arg.split("SYMBOLIC_BV_")[-1])

                    if arg_size in [8,16,32]:
                        new_arg_size = arg_size
                        # For broadcast like instructions just use the same size
                        if sample_ctx.in_precision >= arg_size:
                            # If really scalar then continue
                            print("Is scalar")
                            continue

                    io_ratio = sample_ctx.out_vectsize / arg_size



                    #new_arg_size = output_size / io_ratio
                    new_arg_size = output_size / io_ratio
                    print("new_arg_size",new_arg_size, "not integer:", not new_arg_size.is_integer())

                    if not new_arg_size.is_integer():
                        print("Setting invalid because value isnt integer")
                        valid = False
                        break
                    new_arg_size = int(new_arg_size)
                    bv_str = f"SYMBOLIC_BV_{new_arg_size}"
                    print(f"idx: {idx}, io_ratio: {io_ratio}, result size: {new_arg_size}")

                    new_ctx_args[idx] = bv_str
                    continue

                bw_idxs = [sample_ctx.in_precision_index, sample_ctx.out_precision_index]



                if idx in bw_idxs:
                    print(f"{idx} is is bw_idxs {bw_idxs}")
                    continue

                lane_size_idxs = [sample_ctx.in_lanesize_index, sample_ctx.out_lanesize_index]



                if idx in lane_size_idxs:
                    lane_size_val = int(arg)

                    if lane_size_val == sample_ctx.in_precision:
                        continue

                    if lane_size_val == sample_ctx.out_precision:
                        continue

                    # Need to get lane_size ratio

                    lane_size_ratio = sample_ctx.out_vectsize / lane_size_val
                    new_lane_size = output_size / lane_size_ratio
                    new_ctx_args[idx] = str(int(new_lane_size))
                    continue




                # At this point, we would've adjusted the the lane size and bw idxs already
                adjusted_idxs = bw_idxs + lane_size_idxs
                print("Adjusted idxs:", adjusted_idxs)


                integer_val = None
                try:
                    integer_val = int(arg)
                except:
                    print(arg)
                    print("Invalid Non integer type val")
                    valid = False
                    break

                if integer_val < 8:
                    # Possibly  controlling parameters, keep as is
                    continue

                # If value is constant across all contexts
                idx_arg_vals = self.get_arg_value_by_index(dsl_inst, idx)
                idx_arg_vals = np.array(idx_arg_vals)

                out_sizes = self.get_dsl_inst_out_vectsizes(dsl_inst)
                in_sizes = self.get_dsl_inst_in_vectsizes(dsl_inst)

                # If always equal to in_vectsize, then set it accordingly
                if (np.array(in_sizes) == idx_arg_vals).all():
                    print("Always in_sizes out sizes")
                    # Need to identify corresponding arg size to choose from

                    match_idx = None
                    for orig_idx, orig_arg in enumerate(sample_ctx.context_args):
                        if isinstance(orig_arg, BitVector) and orig_arg.size == sample_ctx.in_vectsize:
                            match_idx = orig_idx
                            break


                    #new_ctx_args[idx] = str(new_arg_size)

                    assert match_idx is not None
                    assert "SYMBOLIC_BV" in new_ctx_args[match_idx]
                    new_size = new_ctx_args[match_idx].split("_")[-1]

                    new_ctx_args[idx] = new_size
                    continue

                # If always equal to out_vectsize, then set it accordingly
                if (np.array(out_sizes) == idx_arg_vals).all():
                    print("Always equal out sizes")
                    new_ctx_args[idx] = str(output_size)
                    continue

                out_precs = self.get_dsl_inst_out_precisions(dsl_inst)
                in_precs = self.get_dsl_inst_in_precisions(dsl_inst)

                # If always equal to out_precision, then set it accordingly
                if (np.array(out_precs) == idx_arg_vals).all():
                    print("Always equal out precs")
                    new_ctx_args[idx] = str(output_bitwidth)
                    continue

                out_precs = self.get_dsl_inst_out_precisions(dsl_inst)
                #If always a ratio of out_precision
                ratio = idx_arg_vals / idx_arg_vals
                contains_inf = np.isinf(ratio).any()
                contains_nan = np.isnan(ratio).any()

                if (not contains_inf)  and (not contains_nan):
                    unique_values, counts = np.unique(ratio , return_counts=True)
                    if len(counts) == 1:
                        print("Always ratio of output_bitwidth!")
                        new_ctx_args[idx] = str(int(unique_values[0] * output_bitwidth))
                        continue






                print("IDX ARG VALS: ", idx_arg_vals)
                print("UNIQUE:", set(idx_arg_vals))
                if len(set(idx_arg_vals)) == 1:
                    continue

                print(f"Need to find ratio where consistent for idx {idx}")

                found_unique = False
                print("new_ctx_args", new_ctx_args)
                #  ['SYMBOLIC_BV_4096', 'SYMBOLIC_BV_4096', 'SYMBOLIC_BV_4096', 'SYMBOLIC_BV_32', '32', '32', '0', '128', '32', '1', '0', '1', '64', '1', '0']
                for inner_arg_idx in range(len(new_ctx_args)):
                    sample_arg = sample_ctx.unparsed_args[inner_arg_idx]
                    if "BV" in sample_arg:
                        continue
                    if "bv" in sample_arg:
                        continue
                    if inner_arg_idx == idx:
                        continue

                    #if inner_arg_idx in adjusted_idxs:
                    #    continue

                    inner_idx_arg_vals = self.get_arg_value_by_index(dsl_inst, inner_arg_idx)
                    inner_idx_arg_vals = np.array(inner_idx_arg_vals)
                    print("==========================")
                    print("outer", idx)
                    print("outer_idx_arg_vals", idx_arg_vals)
                    print("inner_arg_idx", inner_arg_idx)
                    print("inner_idx_arg_vals", inner_idx_arg_vals)

                    ratio = idx_arg_vals / inner_idx_arg_vals
                    print("ratio", ratio)
                    # Check for any inf or nan

                    contains_inf = np.isinf(ratio).any()
                    contains_nan = np.isnan(ratio).any()

                    if contains_inf or contains_nan:
                        continue

                    unique_values, counts = np.unique(ratio , return_counts=True)



                    print("Unique values", unique_values)
                    if len(counts) != 1:
                        continue

                    found_unique = True

                    new_val =  int(sample_arg) * int(unique_values[0])
                    new_ctx_args[idx] = str(int(new_val))
                    #new_ctx_args[inner_arg_idx] = str(int(new_val))

                    break


                if not found_unique:
                    print("Not found unique")
                    valid = False
                    break


            if not valid:
                print(f"UNABLE TO Scale {dsl_inst.name} to {output_size} size and {output_bitwidth} bitwidth")
                print("Original CTX", sample_ctx.name)
                print("Original Args:", sample_ctx.unparsed_args)
                print("New Args:", new_ctx_args)
                print("Not Valid")
                assert False
                continue

            print(f"Scale to {output_size} size and {output_bitwidth} bitwidth")
            print("ORIGINAL CTX", sample_ctx.name)
            print("Original Args:", sample_ctx.unparsed_args)
            extended_name = f"{sample_ctx.name}_extended_size_{output_size}_bw_{output_bitwidth}_ctx_{ctx_idx}"
            print("New Args:", new_ctx_args)
            dsl_inst.add_context(name = extended_name,
                                 in_vectsize = new_arg_size,
                                 out_vectsize = output_size,
                                 lane_size = int(new_ctx_args[sample_ctx.in_lanesize_index]) if sample_ctx.in_lanesize_index is not None else int(new_ctx_args[sample_ctx.in_precision_index]),
                                 in_precision = int(new_ctx_args[sample_ctx.in_precision_index]),
                                 out_precision = output_bitwidth,
                                 args = new_ctx_args,
                                 in_precision_index = sample_ctx.in_precision_index,
                                 out_precision_index = sample_ctx.out_precision_index,
                                 permutation = sample_ctx.permutation
                                 )
            return

















    def extend_eq_classes(self, dsl_list):

        for output_size in self.extend_to_sizes:
            for bitwidth in self.extend_to_bw:
                for dsl_inst in dsl_list:
                    ctx = self.get_eq_class_ctx(dsl_inst, output_size, bitwidth)
                    if not ctx is None:
                        print(f"Trying to extend {dsl_inst.name} to {output_size} size and {bitwidth} bitwidth failed")
                        # If specific context exists
                        continue

                    self.add_context(dsl_inst, output_size, bitwidth)




        return dsl_list





    def sanatize_eq_classes(self, dsl_list):
        dsl_list = self.set_parameter_indices(dsl_list)
        return dsl_list




    def get_parameter_value_ctx_by_name(self, inst, param_name):
        vals = []
        for ctx in inst.contexts:
            vals.append(getattr(ctx, param_name))
        return vals

    def set_parameter_value_ctx_by_name(self, inst, param_name, val):
        for ctx in inst.contexts:
            setattr(ctx, param_name, val)

    def get_arg_value_by_index(self, inst, idx):
        vals = []
        for ctx in inst.contexts:
            ctx_arg = ctx.context_args[idx]
            val = None
            if isinstance(ctx_arg, Integer):
                val = ctx_arg.value
            elif isinstance(ctx_arg, Precision):
                val = ctx_arg.value
            elif isinstance(ctx_arg, LaneSize):
                val = ctx_arg.value
            else:
                assert False, "Unsupported type"

            vals.append(val)

        return vals

    def get_dsl_inst_out_vectsizes(self, inst):
        vals = []
        for ctx in inst.contexts:
            vals.append(ctx.out_vectsize)
        return vals

    def get_dsl_inst_in_vectsizes(self, inst):
        vals = []
        for ctx in inst.contexts:
            vals.append(ctx.in_vectsize)
        return vals

    def get_dsl_inst_out_precisions(self, inst):
        vals = []
        for ctx in inst.contexts:
            vals.append(ctx.out_precision)
        return vals

    def get_dsl_inst_in_precisions(self, inst):
        vals = []
        for ctx in inst.contexts:
            vals.append(ctx.in_precision)
        return vals

    def is_arg_numeric_at_arg_idx(self, inst, idx):
        sample_ctx = inst.contexts[0]
        ctx_arg = sample_ctx.context_args[idx]
        valid_args_types = [LaneSize, Precision, Integer]
        return any([isinstance(ctx_arg, valid_ty) for valid_ty in valid_args_types])


    # For instructions where the vect_size indices are not
    # set, explicilty set them by doing an analysis for
    def set_parameter_indices(self, dsl_list):
        attrs = ["in_vectsize_index", "out_vectsize_index",
                  "in_precision_index", "out_precision_index"]





        legalized_eq_classes = set()
        for dsl_inst in dsl_list:
            for attr in attrs:
                value_param_name = attr.split("_index")[0]

                value_across_ctxs = self.get_parameter_value_ctx_by_name(dsl_inst, value_param_name)

                index_value_across_ctxs = self.get_parameter_value_ctx_by_name(dsl_inst, attr)

                if all([not v is None for v in index_value_across_ctxs]):
                    continue


                num_ctx_args = len(dsl_inst.contexts[0].context_args)

                for arg_idx in range(num_ctx_args):
                    if not self.is_arg_numeric_at_arg_idx(dsl_inst , arg_idx):
                        continue
                    arg_values = self.get_arg_value_by_index(dsl_inst, arg_idx)

                    if arg_values == value_across_ctxs:
                        print(f"Values at index {arg_idx} for eq_class {dsl_inst.name} all correspond to {value_param_name}. Set {attr} to {arg_idx} ...")
                        self.set_parameter_value_ctx_by_name(dsl_inst, attr, int(arg_idx))
                        legalized_eq_classes.add(dsl_inst.name)

        print("Legalized Equivlance CLASSES: ", legalized_eq_classes)
        return dsl_list









pim_dsl_list = parse_dict(bitserial_fused_sema)
filter_names = [
    #"test_enum_1_comb_13_fused_pim_op_59",
    #"test_enum_1_comb_13_fused_pim_op_951",
    #"test_enum_1_comb_2_fused_pim_op_0",
    #"test_enum_1_comb_13_fused_pim_op_59"
    #"test_enum_1_comb_12_fused_pim_op_191"
    "test_enum_2_comb_3_fused_pim_op_2",

]
pim_dsl_list = [d for d in pim_dsl_list if d.name in filter_names]

#pim_dsl_list = [d for d in pim_dsl_list]
print("Sample dsl_list:", pim_dsl_list)
#DSLExtender = ExtendDSLUtils(extend_to_sizes = [pow(2, i) for i in range(8, 34+1)], extend_to_bw = [1,8, 16, 32])

DSLExtender = ExtendDSLUtils(extend_to_sizes = [pow(2, i) for i in range(8, 34+1)], extend_to_bw = [32])
pim_dsl_list[0].contexts = [pim_dsl_list[0].contexts[0]]


DSLExtender.extend(pim_dsl_list)




