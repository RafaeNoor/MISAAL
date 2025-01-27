from compiler.Pattern import Pattern, parse_pattern_from_string
import concurrent.futures
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils
from utils.DSLInstructionUtils import *
from utils.ConcretizeUtils import get_valid_concretization_generator
from utils.CanonicalizeExpressions import CanonicalizeExpression
from utils.ReadDSL import read_string_to_dsl
from sema.integer_arith_sema import integer_arith_sema_dict
from common.Types import *
from collections import defaultdict
import copy
import json
from graphlib import TopologicalSorter, CycleError


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
    def __init__(self, patterns, dsl_list, examples_limit = None):
        self.patterns = patterns
        self.dsl_list = dsl_list
        self.equality_checker = CanonicalizeExpression()
        self.integer_arith_sema = parse_dict(integer_arith_sema_dict)
        self.examples_limit = examples_limit


    def emit_create_param_abstract_spec(self, input_values, output_value):
        return "(TESTS {} (vector {}))".format(output_value, " ".join([str(v) for v in input_values]))

    def emit_synthesize_query(self, test_cases, depth = 2, num_src_regs = 2, exclude_regs = []):
        return "(synthesize-param-expression {} {} {} (list {}))".format(test_cases, depth, num_src_regs - 1, " ".join([str(reg) for reg in exclude_regs]))

    def generate_param_expr(self, src_param_map, dst_param_map, dst_param_name, depth = 2, only_src_params = False, exclude_regs = []):


        statements = []

        assert dst_param_name in dst_param_map, "Expected {} in dst_param_map".format(dst_param_name)

        num_test_cases = len(dst_param_map[dst_param_name])
        if not self.examples_limit is None:
            num_test_cases = min(num_test_cases, self.examples_limit)
        test_cases_def = []
        for tc in range(num_test_cases):
            values = []

            target_value = dst_param_map[dst_param_name][tc]

            for src_val_name, src_vals in src_param_map.items():
                values.append(src_vals[tc])

            if not only_src_params:
                # Do not include other target pattern params if
                # want to synthesize in terms of src numeric parameters
                # only
                for dst_val_name, dst_vals in dst_param_map.items():
                    if dst_val_name == dst_param_name:
                        continue
                    values.append(dst_vals[tc])
            test_case = self.emit_create_param_abstract_spec(values, target_value)
            test_cases_def.append(test_case)

        test_def = "(define param-test-cases (list \n{}\n))".format("\n".join(test_cases_def))
        statements.append(test_def)

        synthesis_query = self.emit_synthesize_query("param-test-cases", depth = depth,  num_src_regs = len([key for key in src_param_map]), exclude_regs = exclude_regs)

        synthesis_result = "(define-values (sat? expr) {})".format(synthesis_query)
        statements.append(synthesis_result)

        sat_cond = "sat?"
        unsat_cond = "else"


        read_out_fname = next(tempfile._get_candidate_names()) + ".temp"
        sat_case = "(write-str-to-file (~v {}) \"{}\") (exit 0)".format("expr", read_out_fname)
        unsat_case = "(exit 1)"

        handler = emit_racket_cond([sat_cond, unsat_cond] , [sat_case, unsat_case])
        statements.append(handler)

        result = execute_racket_file(statements)

        success = result.returncode == 0

        simplified_expr = None
        if success:
            with open(read_out_fname, "r") as ReadFile:
                simplified_expr = ReadFile.read()
                if REMOVE_RKT_FILES:
                    subprocess.call("rm -f {}".format(read_out_fname), shell = True)
        return success, simplified_expr





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

        #test_bucket = self.swap_patterns(buckets[0])
        test_bucket = (buckets[0])
        self.abstract_pattern_bucket(test_bucket, dsl_list)


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

        if any([isinstance(expr, ty) for ty in [LaneSize, Precision, Integer, Variable]]):
            iterator = ContextNumericIter(outer_context, outer_args_idx, expr)
            return [iterator]

        if isinstance(expr, Context) and expr.extensions != None and 'integer_arith' in expr.extensions:
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


    def increment_regs(self, expr, geq = 0):

        if isinstance(expr, Reg):

            if int(expr.index) >= geq:
                return Reg(int(expr.index)+1, expr.precision, expr.size, signed = expr.signed)
            else:
                return expr
        elif isinstance(expr, Context):
            for idx, arg in enumerate(expr.context_args):
                expr.context_args[idx] = self.increment_regs(arg, geq = geq)
            return expr
        else:
            return expr


    def graph_has_cycle(self, graph):
        try:
            ts = TopologicalSorter(graph)
            ts.prepare()  # Raises CycleError if a cycle is detected
            return False
        except CycleError:
            return True

    def should_exclude_reg(self, graph, current_index, index_to_consider):
        graph_copy = copy.deepcopy(graph)
        graph_copy[str(current_index)].append(str(index_to_consider))
        print("Graph Copy, index to consider", index_to_consider)
        print(json.dumps(graph_copy))

        has_cycle = self.graph_has_cycle(graph_copy)
        print("Has cycle:", has_cycle)
        return has_cycle


    def peel_symbolic_parameters(self, symbolic_pattern_params, src_position_map, dst_position_map, nodes_to_peel):

        peeled_params = [symbolic_pattern_params]
        num_src_regs = len([key for key in src_position_map])
        num_dst_regs = len([key for key in dst_position_map])

        for node in nodes_to_peel:
            node = int(node)
            peeled_params_iter = []
            for param_version in peeled_params:

                param = param_version[node]
                concrete_values = []
                if int(node) < num_src_regs:
                    # Belonging to src parameters
                    concrete_values = src_position_map[node]
                else:
                    dst_index = int(node) - num_src_regs
                    concrete_values = dst_position_map[dst_index]

                concrete_values = list(set(concrete_values))

                print("concrete_values", concrete_values)
                for conc_val in concrete_values:
                    param_copy = copy.deepcopy(param_version)
                    param_copy[node] = Integer("peel", value = conc_val)
                    peeled_params_iter.append(param_copy)
            peeled_params = peeled_params_iter
        return peeled_params





    def inline_symbolic_references(self, symbolic_pattern_params, num_src_params):




        # Now that the register indices are adjusted correctly,
        # we replace all register references to expressions within
        # updated expressions. The ordering of update implies that
        # a reverse topological sorted ordering would require only
        # a single update

        graph = {}
        for idx, expr in enumerate(symbolic_pattern_params):
            expr_name = str(idx)

            if expr_name not in graph:
                graph[expr_name] = []

            expr_regs = get_unique_context_registers(expr)

            for reg in expr_regs:
                reg_name = str(reg.index)

                #if reg_name not in  graph:
                #    graph[reg_name] = []
                #graph[reg_name].append(expr_name)
                graph[expr_name].append(reg_name)

        ts = TopologicalSorter(graph)
        # Perform topological sort
        topological_order = ts.static_order()
        for i in topological_order:
            index = int(i)
            sym_expr = symbolic_pattern_params[index]

            if isinstance(sym_expr, Variable):
                continue
            elif isinstance(sym_expr, Reg):
                reg_index = int(sym_expr.index)
                symbolic_pattern_params[index] = symbolic_pattern_params[reg_index]
            elif isinstance(sym_expr, Context):
                expr_regs = get_unique_context_registers(sym_expr)
                for reg in expr_regs:
                    reg_index = int(reg.index)
                    sym_expr = bind_expr_to_reg(sym_expr, reg_index, symbolic_pattern_params[reg_index])
                symbolic_pattern_params[index] = sym_expr


        for idx, expr in enumerate(symbolic_pattern_params):
            print("#",idx)
            if isinstance(expr, Context):
                print(expr.emit_context_expr_string())
            else:
                print(expr.get_rkt_value())
        return symbolic_pattern_params

    def replace_parameters_with_symbolic_exprs(self, pattern_template, symbolic_params_versions, num_src_params):

        patterns = []
        for symbolic_params in symbolic_params_versions:

            src_copy = copy.deepcopy(pattern_template.src_expr)
            dst_copy = copy.deepcopy(pattern_template.target_expr)
            for idx, param in enumerate(symbolic_params):

                if idx < num_src_params:
                    self.set_expr_numeric_position(src_copy, idx, param)
                else:
                    dst_idx = idx - num_src_params
                    self.set_expr_numeric_position(dst_copy, dst_idx, param)
            pattern = Pattern(src_copy, dst_copy, src_dsl_list = pattern_template.src_dsl_list,target_dsl_list =  pattern_template.target_dsl_list, name = pattern_template.name, src_language = pattern_template.src_language, target_language = pattern_template.target_language, bidirectional = pattern_template.bidirectional)
            patterns.append(pattern)
        return patterns


    def swap_patterns(self, bucket):
        for p in bucket:
            p.swap()
        return bucket

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


        src_position_map = {}
        dst_position_map = {}

        for pattern in bucket:
            src_expr = pattern.src_expr
            dst_expr = pattern.target_expr


            src_iters = self.get_expr_numeric_positions(src_expr)
            dst_iters = self.get_expr_numeric_positions(dst_expr)

            for idx, si in enumerate(src_iters):
                if idx not in src_position_map:
                    src_position_map[idx] = []
                src_position_map[idx].append(si.value.value)

            for idx, di in enumerate(dst_iters):
                if idx not in dst_position_map:
                    dst_position_map[idx] = []
                dst_position_map[idx].append(di.value.value)





        print("Src")
        print(json.dumps(src_position_map, indent = 4))

        print("Dst")
        print(json.dumps(dst_position_map, indent = 4))




        symbolic_pattern_params = []

        for src_param_name, values in src_position_map.items():
            symbolic_pattern_params.append(Variable("sym{}".format(src_param_name)))

        num_src_params = len(symbolic_pattern_params)
        num_dst_params = len([key for key in dst_position_map])

        graph = {str(k) : [] for k in src_position_map}
        for idx, key in enumerate(dst_position_map):
            absolute_index = idx + num_src_params
            node_name = str(absolute_index)
            if node_name not in graph:
                graph[node_name] = []


        for idx, key in enumerate((dst_position_map)):
            print("Iteration", idx)
            print(json.dumps(graph))

            absolute_index = key + num_src_params
            node_name = str(absolute_index)

            exclude_regs = []


            print("=*"*40)
            print("Testing Dst Key:", key, "absolute index:", absolute_index)
            print("Exclude regs:", exclude_regs)


            success, expr = self.generate_param_expr(src_position_map, dst_position_map, key, only_src_params = True, exclude_regs = exclude_regs, depth = 2)

            # Extend to include other dst expression parameters as well
            if not success:
                success, expr = self.generate_param_expr(src_position_map, dst_position_map, key, only_src_params = False, exclude_regs = exclude_regs, depth = 2)

            # Extend to include other dst expression parameters as well
            if not success:
                success, expr = self.generate_param_expr(src_position_map, dst_position_map, key, only_src_params = False, exclude_regs = exclude_regs, depth = 3)

            if success:
                print("Success for key", key)
                print(expr)
                parsed_expression = read_string_to_dsl(expr, self.integer_arith_sema)
                # Increment before storing
                # First adjust the references to 'regs' to reflect ordering according
                # to the actual position iterators. Recall, that for each position,
                # when we're synthesizing the index expression, we exclude the constant
                # value at that specific position as part of the synthesis query (it is made into
                # the target of the synthesis query). As such, the general algorithm for adjusting the
                # indicies is defined as follows. For each expr at index position pi, all registers
                # with register >= pi are incremented by 1 in the expression .
                parsed_expression = self.increment_regs(parsed_expression, geq = absolute_index)

                if isinstance(parsed_expression, Context):
                    print(parsed_expression.emit_context_expr_string())
                else:
                    print(parsed_expression.get_rkt_value())
                symbolic_pattern_params.append(parsed_expression)

                expr_regs = get_unique_context_registers(parsed_expression)

                for reg in expr_regs:
                    graph[node_name].append(str(reg.index))

            else:
                print("Unable to synthesize for key", key)
                return False, None


        print("Graph after param synthesis")
        print(json.dumps(graph))
        print(self.find_node_in_most_cycles(graph), "is part of most cycles")


        # The graph containing cycle implies circular definitions for the abstracted pattern. We break these
        # cycles by 'peeling' out nodes in the graph and replacing them with the constant values they take in the
        # concretely derived rewrites. We repeat this until the graph contains no cycles. We use a greedy algorithm
        # to identify the node which is part of the most cycles and 'peel' that.

        peeled_graph = copy.deepcopy(graph)
        nodes_to_peel = []

        while self.graph_has_cycle(peeled_graph):
            to_peel, count = self.find_node_in_most_cycles(peeled_graph)
            nodes_to_peel.append(to_peel)
            peeled_graph.pop(to_peel, None)
            for node in peeled_graph:
                peeled_graph[node] = [value for value in peeled_graph[node] if value != to_peel]

        print("To Peel!:", nodes_to_peel)

        # Peel out nodes creating possibly multiple versions of parameterizations
        updated_symbolic_params = self.peel_symbolic_parameters(symbolic_pattern_params, src_position_map, dst_position_map, nodes_to_peel)
        updated_symbolic_params = [self.inline_symbolic_references(params, num_src_params) for params in updated_symbolic_params]
        print(len(updated_symbolic_params))


        abstract_patterns = self.replace_parameters_with_symbolic_exprs(bucket[0], updated_symbolic_params, num_src_params)

        for idx, abs_pat in enumerate(abstract_patterns):
            print("Abstract pattern", idx)
            abs_pat.print_pattern()
        return abstract_patterns













    def find_cycles(self, graph):
        """
        Function to find all cycles in a directed graph using DFS.
        Returns a list of cycles, where each cycle is a list of nodes.
        """
        def dfs(node, path, visited, all_cycles):
            if node in path:  # Found a cycle
                cycle_index = path.index(node)
                cycle = path[cycle_index:]  # Extract the cycle from the path
                all_cycles.append(cycle)
                return

            if node in visited:  # Skip already processed nodes
                return

            visited.add(node)
            path.append(node)

            # Recursively visit each neighbor
            for neighbor in graph.get(node, []):
                dfs(neighbor, path, visited, all_cycles)

            path.pop()  # Backtrack

        all_cycles = []
        visited = set()
        for node in graph:
            if node not in visited:
                dfs(node, [], visited, all_cycles)

        return all_cycles

    # Code obtained by ChatGPT!
    def find_node_in_most_cycles(self, graph):
        # Find all cycles in the graph
        cycles = self.find_cycles(graph)

        # Dictionary to count how many times each node appears in a cycle
        node_cycle_count = {}

        for cycle in cycles:
            for node in cycle:
                node_cycle_count[node] = node_cycle_count.get(node, 0) + 1

        # Find the node that appears in the most cycles
        most_cycles_node = max(node_cycle_count, key=node_cycle_count.get, default=None)

        return most_cycles_node, node_cycle_count.get(most_cycles_node, 0)



