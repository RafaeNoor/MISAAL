from compiler.Pattern import Pattern, parse_pattern_from_string
import concurrent.futures
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils
from utils.DSLInstructionUtils import *
from utils.ConcretizeUtils import get_valid_concretization_generator
from utils.CanonicalizeExpressions import CanonicalizeExpression
from common.Types import *
import copy


def create_patterns(props, combined_dsl_list):
    src_key_names = ['src', 'candidate', 'input_expression']
    dst_key_names = ['dst', 'simplified', 'output_expression']

    patterns = []

    for idx, prop in enumerate(props):
        for key, value in prop.items():
            src_key_name = "src"
            for src_key in src_key_names:
                if src_key in value[0]['property']:
                    src_key_name = src_key

            dst_key_name = 'dst'
            for dst_key in dst_key_names:
                if dst_key  in value[0]['property']:
                    dst_key_name = dst_key

            input_expr = value[0]['property'][src_key_name]
            output_expr = value[0]['property'][dst_key_name]

            pattern = parse_pattern_from_string(input_expr, output_expr, combined_dsl_list, combined_dsl_list, src_language = "SRC", target_language = "TARGET", bidirectional = True)

            patterns.append(pattern)
    return patterns


def get_possible_output_sizes_for_eq_class(ctx, dsl_list):
    eq_class = get_eq_class_for_ctx(ctx, dsl_list)
    output_sizes = [ctx_.out_vectsize for ctx_ in eq_class.contexts]
    return list(set(output_sizes))



def deduplicate_patterns(patterns):
    unique_patterns = []
    for s_idx, pattern in enumerate(patterns):
        insert = True
        for j in range(s_idx + 1, len(patterns)):
            other_pattern = patterns[j]

            if other_pattern.equal_to(pattern):
                insert = False
                break
        if insert:
            unique_patterns.append(pattern)
    return unique_patterns


def deduplicate_patterns_parallel(patterns, pool_size = 8, parallel = True):

    mask = [False] * len(patterns)

    def worker(s_idx):
        insert = True
        pattern_i = patterns[s_idx]
        for j in range(s_idx + 1, len(patterns)):
            other_pattern = patterns[j]

            if other_pattern.equal_to(pattern_i):
                insert = False
                break
        mask[s_idx] =  insert

    if parallel:
        pool = concurrent.futures.ThreadPoolExecutor(max_workers=pool_size)
        for s_idx, pattern in enumerate(patterns):
            pool.submit(worker, s_idx)


        pool.shutdown(wait=True)
    else:
        for s_idx, pattern in enumerate(patterns):
            worker(s_idx)



    unique_patterns = []
    for idx, mask_val in enumerate(mask):
        if mask_val:
            unique_patterns.append(patterns)



    return unique_patterns




def can_pattern_be_abstracted_for_output_size(src_ctx, dst_ctx, combined_dsl_list,  output_size):
    # First do a quick check to test that both src and expression contexts
    # have some member which produces the required output size to side step
    # synthesis.
    src_supports_output_size = True
    if isinstance(src_ctx, Context):
        src_root_eq_class = get_eq_class_for_ctx(src_ctx, combined_dsl_list)
        src_supports_output_size = src_root_eq_class.supports_output_size(output_size)

    if not src_supports_output_size:
        return False

    dst_supports_output_size = True
    if isinstance(dst_ctx, Context):
        dst_root_eq_class = get_eq_class_for_ctx(dst_ctx, combined_dsl_list)
        dst_supports_output_size = dst_root_eq_class.supports_output_size(output_size)

    if not dst_supports_output_size:
        return False

    return True

def translate_pattern_for_output_size(src_ctx, dst_ctx, combined_dsl_list , output_size, required_src_ctx = None, required_dst_ctx = None):

    if  not can_pattern_be_abstracted_for_output_size(src_ctx, dst_ctx, combined_dsl_list,  output_size):
        print("Pattern can't be abstracted for given size")
        return False, "", ""

    if required_src_ctx is None or required_dst_ctx is None:
        return False, "", ""

    valid_src_conc = None
    valid_dst_conc = None

    if  src_ctx.name != required_src_ctx.name:
        valid_src_conc_gen = get_valid_concretization_generator(src_ctx, output_size, combined_dsl_list)
        if required_src_ctx is None:
            valid_src_conc = next(valid_src_conc_gen)
        else:
            for valid_src_conc in valid_src_conc_gen:
                if valid_src_conc.name == required_src_ctx.name:
                    break
            if valid_src_conc.name != required_src_ctx.name:
                print("No Valid src expr")
                return False, "", ""
    else:
        print("SRC CONTEXT ALREADY MATCHES")
        valid_src_conc = src_ctx

    if dst_ctx.name != required_dst_ctx.name:
        valid_dst_conc_gen = get_valid_concretization_generator(dst_ctx, output_size, combined_dsl_list)
        if required_dst_ctx is None:
            valid_dst_conc = next(valid_dst_conc_gen)
        else:
            for valid_dst_conc in valid_dst_conc_gen:
                if valid_dst_conc.name == required_dst_ctx.name:
                    break
            if valid_dst_conc.name != required_dst_ctx.name:
                print("No Valid dst expr")
                return False, "", ""
    else:
        print("DST CONTEXT ALREADY MATCHES")
        valid_dst_conc = dst_ctx









    synth_utils = DoubleGrammarSynthesisUtils(input_dsl_list = combined_dsl_list, output_dsl_list = combined_dsl_list, swizzle_dsl_list = [], auxilary_dsl_list = [], force_contains_all_regs = True, required_src_name = src_ctx.name, required_dst_name = dst_ctx.name)
    success, src_expr_str, dst_expr_str = synth_utils.double_grammar_synthesis(valid_src_conc, valid_dst_conc )

    return success, src_expr_str, dst_expr_str



def prune_redundant_patterns(patterns, dsl_list):
    useful_patterns = []

    for p in patterns:
        if is_redundant_pattern(p, dsl_list):
            continue

        useful_patterns.append(p)
    return useful_patterns



def is_redundant_pattern(pattern, dsl_list):
    src_names = get_ctx_expr_ctx_names(pattern.src_expr, dsl_list)
    dst_names = get_ctx_expr_ctx_names(pattern.target_expr, dsl_list)

    if len(src_names) == 0:
        return False

    if len(dst_names) == 0:
        return False

    pattern_names = set(src_names + dst_names)
    # Pattern is redundant if all context names are the same
    return len(pattern_names) == 1



class ContextNumericIter:
    def __init__(self, outer_context_ref, outer_context_arg_idx, value):
        self.outer_context_ref = outer_context_ref
        self.outer_context_arg_idx = outer_context_arg_idx
        self.value = value


class PatternAbstractor:
    def __init__(self, patterns, dsl_list):
        self.patterns = patterns
        self.dsl_list = dsl_list
        self.equality_checker = CanonicalizeExpression()

    def abstract_patterns(self, patterns, dsl_list):
        accounted_for_patterns_idxs = []

        # First partition the patterns into buckets
        # where all patterns in the given bucket have
        # the same AutoLLVM IR equivalance classes in the
        # same structure
        buckets = []
        for i in range(len(patterns)):
            if i in accounted_for_patterns_idxs:
                continue

            pat_i = patterns[i]
            bucket_i = [pat_i]
            for j in range(i+1, len(patterns)):
                pat_j = patterns[j]

                src_expr_equal = self.equality_checker.isCanonical(pat_i.src_expr, pat_j.src_expr)
                dst_expr_equal = self.equality_checker.isCanonical(pat_i.target_expr, pat_j.target_expr)

                if src_expr_equal and dst_expr_equal:
                    accounted_for_patterns_idxs.append(j)
                    bucket_i.append(pat_j)
            buckets.append(bucket_i)


        print("Total # patterns:", len(patterns))
        print("Total Number of buckets: ", len(buckets))
        print(buckets[0][0].src_expr.emit_context_expr_string())
        print(buckets[0][1].target_expr.emit_context_expr_string())

        self.abstract_pattern_bucket(buckets[0], dsl_list)


    def get_expr_num_numeric_positions(self, expr):

        if isinstance(expr, Context):

            num_positions = 0
            for arg in expr.context_args:
                num_positions += self.get_expr_num_numeric_positions(arg)
            return num_positions

        if any([isinstance(expr, ty) for ty in [LaneSize, Precision, Integer]]):
            return 1

        return 0


    def get_expr_numeric_positions(self, expr, outer_context = None, outer_args_idx = None):

        if isinstance(expr, Context):
            positions = []

            for idx, arg in enumerate(expr.context_args):
                sub_positions = self.get_expr_numeric_positions(arg, outer_context = expr, outer_args_idx = idx)

                if len(sub_positions) != 0:
                    positions += sub_positions

            return positions

        if any([isinstance(expr, ty) for ty in [LaneSize, Precision, Integer]]):
            iterator = ContextNumericIter(outer_context, outer_args_idx, expr)
            return [iterator]

        return []




    def set_expr_numeric_position(self, expr, position, value):
        iterators = self.get_expr_numeric_positions(expr)

        assert position < len(iterators), "Out of bounds numeric parameters access"
        pos_iter = iterators[position]

        # Update the outer handle in place
        assert not pos_iter.outer_context_ref is None, "Can Only update inplace for expressions with outer contexts defined"

        assert not pos_iter.outer_context_arg_idx is None, "Can only update inplace for expressions with relative context positions defined"


        outer_ctx = pos_iter.outer_context_ref
        ctx_arg_idx = pos_iter.outer_context_arg_idx

        assert ctx_arg_idx < len(outer_ctx.context_args), "Out of bounds access for context args"

        outer_ctx.context_args[ctx_arg_idx] = value








    def abstract_pattern_bucket(self, bucket, dsl_list):
        assert len(bucket) != 0, "Expecting at-least one pattern to abstract"

        template_expr_src = copy.deepcopy(bucket[0].src_expr)
        template_expr_dst = copy.deepcopy(bucket[0].target_expr)

        print(template_expr_src.emit_context_expr_string())
        print(template_expr_dst.emit_context_expr_string())
        print("Src positions ", self.get_expr_num_numeric_positions(template_expr_src))
        print("Dst positions ", self.get_expr_num_numeric_positions(template_expr_dst))

        src_vals = self.get_expr_numeric_positions(template_expr_src)
        print([iter_.value.value for iter_ in src_vals])

        dst_vals = self.get_expr_numeric_positions(template_expr_dst)
        print([iter_.value.value for iter_ in dst_vals])


        rand_val = Integer("random", value = 69)

        self.set_expr_numeric_position(template_expr_dst, 4, rand_val)

        print("Post modification")
        dst_vals = self.get_expr_numeric_positions(template_expr_dst)
        print([iter_.value.value for iter_ in dst_vals])




