from compiler.Pattern import Pattern, parse_pattern_from_string
import concurrent.futures
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils
from utils.DSLInstructionUtils import *
from utils.ConcretizeUtils import get_valid_concretization_generator
from common.Types import *


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
