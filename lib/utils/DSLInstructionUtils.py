import common.Types
import sys
import time
import copy
import sys
from common.Types import *
from  common.Instructions import Context
import subprocess
import os
import tempfile
import glob
import numpy as np
import concurrent.futures

REMOVE_RKT_FILES = True
HYDRIDE_HEADER =  """
        #lang rosette
        (require rosette/lib/synthax)
        (require rosette/lib/angelic)
        (require racket/pretty)
        (require rosette/lib/destruct)
        (require hydride)
        (require misaal)

        ;; Uncomment the line below to enable verbose logging
        (enable-debug)
        (custodian-limit-memory (current-custodian) (* 10000 1024 1024))
        (current-bitwidth 16)
        """


def get_symbolic_bitvector_indices_for_ctx(dsl_inst):
    """Returns a list of list of indices which specfies the symbolic bitvector argument indices for contexts

    Args:
        dsl_inst (DSLInstruction): Hydride's DSLInstruction Type
    """

    indices = []
    for context in dsl_inst.contexts:
        context_indices = [i for i in range(0, len(context.args)) if isinstance(context.args[i], BitVector)]
        indices.append(context_indices)

    return indices


def get_concrete_bitvector_indices_for_ctx(dsl_inst):
    """Returns a list of list of indices which specfies the concrete bitvector argument indices for contexts

    Args:
        dsl_inst (DSLInstruction): Hydride's DSLInstruction Type
    """

    indices = []
    for context in dsl_inst.contexts:
        context_indices = [i for i in range(0, len(context.args)) if isinstance(context.args[i], ConstBitVector)]
        indices.append(context_indices)

    return indices




def emit_context_expr(ctx, dsl_inst):
    """Return the string representation of the context in Rosette

    Args:
        ctx (_type_): _description_
        dsl_inst (_type_): _description_
    """

    dsl_name = ctx.dsl_name + ctx.dsl_name_suffix()
    terms = ["(", dsl_name]
    for arg in ctx.context_args:
        if isinstance(arg, Context):
            terms.append(emit_context_expr(arg,arg))
        else:
            terms.append(arg.get_dsl_value())

    terms.append(")")

    return "\n".join(terms)


def emit_verify_equal(v1, v2):
    return "(verify (assert (equal? {} {})))".format(v1, v2)



def get_random_tempfile_name():
    return next(tempfile._get_candidate_names())


class HelperCompletedProcess:
    def __init__(self, returncode = 1):
        self.returncode = returncode

def execute_racket_file(statements):

    filename = next(tempfile._get_candidate_names()) + ".rkt"
    print("Executing file:\t", filename)
    with open(filename, "w+") as WriteFile:
        def write_line(line):
            WriteFile.write(line + "\n")

        write_line(HYDRIDE_HEADER)

        for statement in statements:
            write_line(statement)

    # Timeout for repair should be 20 minutes, timeout for eqclass equal depth should be much smaller
    TIMEOUT = int(2 * 60) # 20 mins
    result = None
    try:
        result = subprocess.run(["racket", "{}".format(filename)],
                                stdout = subprocess.DEVNULL,
                                stderr = subprocess.DEVNULL,
                                timeout = TIMEOUT
                                )

    except KeyboardInterrupt:
        sys.exit()
    except subprocess.TimeoutExpired:
        print("File Timedout:\t", filename)
        result = HelperCompletedProcess(returncode = 1)
    except :
        print("Unknown error for", filename, ":\t")
        sys.exit()
        result = HelperCompletedProcess(returncode = 1)




    print("Completed executing file:\t", filename)
    if REMOVE_RKT_FILES:
        subprocess.run(["rm {}".format(filename)], shell = True)
    return result





def emit_racket_cond(clauses, cases):

    cond = ["(cond"]

    for i in range(len(clauses)):
        if i == len(clauses) - 1 and len(clauses) != 1:
            cond.append("[else {}]".format(cases[i]))
        else:
            cond.append("[{} {}]".format(clauses[i], cases[i]))

    cond.append(")")

    return "\n".join(cond)


def check_if_contexts_equal(ctx1, ctx2, dsl_inst1, dsl_inst2,vector_sizes, code_synthesizer_desc, dsl_list = []):
    """Symbollically verifies that ctx1 and ctx2 are equal for provided vector sizes

    Args:
        ctx1 (Context): _description_
        ctx2 (Context): _description_
        dsl_inst1 (Context): _description_
        dsl_inst2 (Context): _description_
        vector_sizes ([int]): _description_
        code_synthesizer_desc (CodeSynthesizerDesc): Descriptions of Code Synthesizer utilities
    """


    env_elements = ["(?? (bitvector {}))".format(size) for size in vector_sizes]

    create_env = "(define env (vector {}))".format(" ".join(env_elements))

    statements = [create_env]


    if code_synthesizer_desc.emit_interpreter:
        statements.append(code_synthesizer_desc.emit_interpreter_framework(dsl_list))


    create_expr_1 = "(define expr_1 {})".format(ctx1.emit_context_expr_string())
    create_expr_2 = "(define expr_2 {})".format(ctx2.emit_context_expr_string())

    result_expr_1 = code_synthesizer_desc.interpret_expr("expr_1", "env")
    result_expr_2 = code_synthesizer_desc.interpret_expr("expr_2", "env")

    cex = "(define cex {})".format(emit_verify_equal(result_expr_1, result_expr_2))

    print_cex = ";(println cex)"

    cex_unsat_check = "(unsat? cex)"

    handler = emit_racket_cond([cex_unsat_check, "else"], ["(displayln \"PROPERTY HOLDS!\") (exit 0)",
    "(displayln \"PROPERTY DOES NOT HOLD!\") (exit 1)"])


    statements += [create_expr_1, create_expr_2, cex, print_cex, handler]



    return execute_racket_file(statements)


def simplify_expression(dsl_expr, code_synthesizer_desc, input_sizes, input_precs):
    """Issues synthesis query to test if the DSLExpression dsl_expr can be simplfied
    into a simpler expression.

    Args:
        dsl_expr (DSLInstruction): _description_
        code_synthesizer_desc (_type_): _description_
    """


    is_simplified = False
    simplified_expr = None

    statements = []

    define_input_expr = "(define hydride-expr {})".format(dsl_expr.emit_context_expr_string())
    statements.append(define_input_expr)


    define_input_size = "(define input-sizes (list {}))".format(" ".join(input_sizes))
    define_input_precs = "(define input-precs (list {}))".format(" ".join(input_precs))

    statements.append(define_input_size)
    statements.append(define_input_precs)

    statements.append("(define output-hash-name \"inst.combine.expr.2\")")

    define_out_expr = "(define output-expr (inst-combine hydride-expr #t #f 'z3 input-sizes input-precs \"{}\" 'regular \"\"  output-hash-name \"\" \"out_hash\" 1))".format(code_synthesizer_desc.target_name)
    statements.append(define_out_expr)



    check_simplified = "(not (equal? hydride-expr output-expr))"

    # Check if lower cost
    check_simplified = "(> ({} hydride-expr) ({} output-expr))".format(code_synthesizer_desc.cost_name, code_synthesizer_desc.cost_name)

    # Write simplified expression to file
    # TEMPORARY
    serialize_output = "({} output-expr)".format(code_synthesizer_desc.printer_name)

    serialize_input = "({} hydride-expr)".format(code_synthesizer_desc.printer_name)

    serialize_expr = "(string-append {} \"\\n\" {})".format(serialize_input, serialize_output)

    serialize_expr = serialize_output


    read_out_fname = next(tempfile._get_candidate_names()) + ".temp"
    write_to_file  = "(write-str-to-file {} \"{}\")".format(serialize_expr, read_out_fname)


    if_simplified = "(begin (displayln \"Simplfied!!\") (pretty-print hydride-expr) (pretty-print output-expr) {}  (exit 0))".format(write_to_file)
    handler = emit_racket_cond([check_simplified, "else"], [if_simplified ,
    "(displayln \"Unable to simplify!\") (exit 1)"])
    statements.append(handler)


    is_simplified = execute_racket_file(statements).returncode == 0

    if is_simplified:
        with open(read_out_fname, "r") as ReadFile:
            simplified_expr = ReadFile.read()

        if REMOVE_RKT_FILES:
            subprocess.call("rm -f {}".format(read_out_fname), shell = True)

    return (is_simplified, simplified_expr)



def execute_racket_file_and_read_from_file(statements, fname_prefix):

    racket_file = fname_prefix + ".rkt"

    with open(racket_file, "w+") as WriteFile:
        WriteFile.write(HYDRIDE_HEADER + "\n")
        WriteFile.write("\n".join(statements))

    print("Check racket_file:", racket_file)

    log_file = fname_prefix + ".log"

    with open(log_file, "w+") as LogFile:
        result = subprocess.run(["racket {}".format(racket_file)], shell=True, stdout = LogFile, stderr = LogFile)



    output = ""
    with open(log_file, "r") as LogFile:
        output = LogFile.read()



    if REMOVE_RKT_FILES:
        subprocess.run(["rm {}".format(racket_file)], shell = True)
        subprocess.run(["rm {}".format(log_file)], shell = True)

    return output






def cleanup_tmp_files():
    tmp_files = glob.glob("/tmp/base_*")
    print("Cleaning up {} tmp files ...".format(len(tmp_files)))

    subprocess.call("rm -f /tmp/base_* /tmp/dict_*", shell = True)


    tmp_files = glob.glob("/tmp/base_*")
    for f in tmp_files:
        subprocess.call("rm -f {}".format(f), shell = True)


def ordered_deduplicate(ls):
    deduplicated = list(set(ls))

    deduplicated.sort(key = lambda x : ls.index(x))

    return deduplicated


def translate_expression(input_expr, src_language_desc, target_language_desc, input_sizes, input_precs, optimize = True, symbolic = False, src_language_dsl = [], target_language_dsl = []):

    is_simplified = False
    simplified_expr = None

    statements = []



    define_input_size = "(define input-sizes (list {}))".format(" ".join(input_sizes))
    define_input_precs = "(define input-precs (list {}))".format(" ".join(input_precs))

    statements.append(define_input_size)
    statements.append(define_input_precs)

    language_to_symbol = {"hvx": "'hvx",
                          "x86": "'x86",
                          "halide": "'halide" ,
                          "halide_hvx": "'halide",
                          "halide_x86": "'halide",
                          }

    assert src_language_desc.target_name in language_to_symbol or src_language_desc.emit_interpreter, "Src language must be in supported languages"

    assert target_language_desc.target_name in language_to_symbol or target_language_desc.emit_interpreter, "Target language must be in supported languages"

    if src_language_desc.emit_interpreter:
        statements.append(src_language_desc.emit_interpreter_framework(src_language_dsl))


    if target_language_desc.emit_interpreter and src_language_desc.target_name != target_language_desc.target_name:
        statements.append(target_language_desc.emit_interpreter_framework(target_language_dsl))

    #statements.append("(define src-language {})".format(language_to_symbol[src_language_desc.target_name]))

    if target_language_desc.emit_interpreter:
        statements.append("(define target-language {})".format("'"+target_language_desc.target_name))
    else:
        statements.append("(define target-language {})".format(language_to_symbol[target_language_desc.target_name]))


    #(src-interpreter src-cost-fn src-visitor src-length-fn src-prec-fn src-get-ops)

    statements.append("(define src-language-desc (target-desc {} {} {} {} {} {} \"{}\" \"{}\"))".format(src_language_desc.interpreter_name, src_language_desc.cost_name, src_language_desc.visitor_name, src_language_desc.get_length_name, src_language_desc.get_prec_name, src_language_desc.get_ops_name, src_language_desc.sema_path,  src_language_desc.dict_name))

    statements.append("(define target-language-desc (target-desc {} {} {} {} {} {} \"{}\" \"{}\"))".format(target_language_desc.interpreter_name, target_language_desc.cost_name, target_language_desc.visitor_name, target_language_desc.get_length_name, target_language_desc.get_prec_name, target_language_desc.get_ops_name, target_language_desc.sema_path, target_language_desc.dict_name))

    # Set global flags for target
    if target_language_desc.target_name in language_to_symbol:
        statements.append(target_language_desc.set_target_name)

    define_input_expr = "(define hydride-expr {})".format(input_expr.emit_context_expr_string())
    statements.append(define_input_expr)

    symbolic_flag = ["#f", "#t"][int(symbolic)]
    opt_flag = ["#f", "#t"][int(optimize)]
    define_out_expr = "(define-values (solved? output-expr elapsed) (misaal-rewrite-ir hydride-expr 1 2 {} {} 'z3 input-sizes input-precs 1 src-language-desc target-language-desc 'regular target-language))".format(opt_flag , symbolic_flag)
    statements.append(define_out_expr)



    # Hacky fix!
    check_simplified = "(and solved? (not (equal? (pretty-format hydride-expr) (pretty-format output-expr))))"


    # Write simplified expression to file
    serialize_output = "({} output-expr)".format(target_language_desc.printer_name)

    serialize_input = "({} hydride-expr)".format(src_language_desc.printer_name)

    serialize_expr = "(string-append {} \"\\n\" {})".format(serialize_input, serialize_output)

    serialize_expr = serialize_output


    read_out_fname = next(tempfile._get_candidate_names()) + ".temp"
    write_to_file  = "(write-str-to-file {} \"{}\")".format(serialize_expr, read_out_fname)


    if_simplified = "(begin (displayln \"Simplfied!!\") (pretty-print hydride-expr) (pretty-print output-expr) {}  (exit 0))".format(write_to_file)
    handler = emit_racket_cond([check_simplified, "else"], [if_simplified ,
    "(displayln \"Unable to simplify!\") (exit 1)"])
    statements.append(handler)


    is_simplified = execute_racket_file(statements).returncode == 0

    if is_simplified:
        print("Simplied expression!")
        with open(read_out_fname, "r") as ReadFile:
            simplified_expr = ReadFile.read()

        print(input_expr.emit_context_expr_string())
        print("to")
        print(simplified_expr)

        if REMOVE_RKT_FILES:
            #subprocess.call("rm -f {}".format(read_out_fname), shell = True)
            pass

    return (is_simplified, simplified_expr)



def get_context_registers(ctx):

    if isinstance(ctx, Reg):
        return [ctx]

    if not isinstance(ctx, Context):
        return []

    regs = []

    for arg in ctx.context_args:
        regs += get_context_registers(arg)
    return regs






# For architectures like ARM do extracts on extract
#, this pass inlines those extracts.
def inline_nested_extracts_in_sema(sema):

    lines = sema

    slice_map = {}

    new_statements_counter = 0

    updated_lines = []

    dead_statements = []

    for line in lines:
        if "(extract" in line:
            result_name = str(line.split("(extract")[0].strip().split(" ")[-1])

            from_var = line.split("(extract")[-1].lstrip().split(" ")[-1].replace(")","").replace("\"","")
            high_slice = line.split("(extract")[-1].lstrip().split(" ")[0].replace(")","").replace("(","")

            low_slice = line.split("(extract")[-1].lstrip().split(" ")[1].replace(")","").replace("(","")



            if from_var in slice_map:

                # i.e. from_var is itself generated from something which is an extract statement
                new_low_slice_name = "new.{}".format(new_statements_counter)
                new_statements_counter += 1

                new_low_slice_stmt = "(define {} (+ {} {}))".format(new_low_slice_name, slice_map[from_var][2], low_slice)


                new_high_slice_name = "new.{}".format(new_statements_counter)
                new_statements_counter += 1

                new_high_slice_stmt = "(define {} (+ {} {}))".format(new_high_slice_name,high_slice, slice_map[from_var][2])

                dead_statements.append(from_var)

                from_var = slice_map[from_var][0]
                new_extract_statement = "(define {}  (extract {} {} {}))".format(result_name, new_high_slice_name, new_low_slice_name, from_var)

                updated_lines.append(new_low_slice_stmt)
                updated_lines.append(new_high_slice_stmt)
                updated_lines.append(new_extract_statement)

                high_slice = new_high_slice_name
                low_slice = new_low_slice_name

            else:
                updated_lines.append(line)


            slice_map[result_name] = (from_var, high_slice, low_slice)


        else:
            updated_lines.append(line)

    pruned_lines = []

    # Remove dead statements
    #print("DEAD:", dead_statements)
    for line in updated_lines:
        prune_line = False
        for name in dead_statements:
            if name+" " in line or name+")" in line:
                prune_line = True

        if not prune_line:
            pruned_lines.append(line)
        else:
            print("PRUNING LINE:[",line,"]")


    return (pruned_lines)



# Remove any extracts which are extracting the entire
# bitvector. Simply return the bitvector operand. Only
# works for constant parameter slices
def remove_redundant_extracts(lines, arg_size_map):

    replace_list = []

    updated_lines = []
    for line in lines:
        if "(extract" in line:
            result_name = str(line.split("(extract")[0].strip().split(" ")[-1])

            from_var = line.split("(extract")[-1].lstrip().split(" ")[-1].replace(")","").replace("\"","")
            high_slice = line.split("(extract")[-1].lstrip().split(" ")[0].replace(")","").replace("(","")

            low_slice = line.split("(extract")[-1].lstrip().split(" ")[1].replace(")","").replace("(","")

            if low_slice.isnumeric() and high_slice.isnumeric() and from_var in arg_size_map:
                total_size = int(high_slice) - int(low_slice) + 1
                if arg_size_map[from_var] == total_size:
                    replace_list.append(result_name)


            if result_name in replace_list:
                new_line = "(define {} {})".format(result_name, from_var)
                updated_lines.append(new_line)
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)


    return (updated_lines)



def create_exhaustive_expressions_generator(dsl_list, expr_depth, use_eq_class = False, output_size = None):
    depth_expressions_generator = create_exhaustive_expressions_generator_helper(dsl_list, expr_depth = expr_depth, return_size = output_size, return_prec = 8, use_eq_class = use_eq_class)

    for expr in depth_expressions_generator:
        new_expr, discard = set_reg_names_exprs_helper(expr, 0)
        yield new_expr


def create_exhaustive_expressions(dsl_list, expr_depth, use_eq_class = False):

    print("create_exhaustive_expressions with depth", expr_depth)
    # Creates exhaustively all expression up to given depth, however
    # the name of the registers would contain a place-holder name which would
    # need to be set correctly later.
    memo = {}
    start_time = time.time()

    USE_GENERATOR = False

    depth_expressions = []
    if USE_GENERATOR:
        depth_expressions_generator = create_exhaustive_expressions_generator_helper(dsl_list, expr_depth = expr_depth, return_size = None,return_prec = None, use_eq_class = use_eq_class)

        for expr in depth_expressions_generator:
            if isinstance(expr, Context):
                depth_expressions.append(expr)
    else:
        depth_expressions = create_exhaustive_expressions_helper(dsl_list, expr_depth = expr_depth, return_size = None,return_prec = None, memo = memo, use_eq_class = use_eq_class)

    print("DEBUG")
    for idx, expr in enumerate(depth_expressions):
        break
        print(idx)
        if isinstance(expr, Context):
            print(expr.emit_context_expr_string_compact())
            print(expr.emit_context_expr_string())
        else:
            print(expr.get_rkt_value())

    print("Setting Register Names")

    reg_set_expressions = set_reg_names_exprs(depth_expressions)

    end_time = time.time()
    elapsed = end_time - start_time

    print("Elapsed time: ", elapsed)

    return reg_set_expressions



def get_num_symbolic_args(ctx):
    return len([arg for arg in ctx.context_args if isinstance(arg, BitVector)])


def create_exhaustive_expressions_helper(dsl_list, expr_depth = 1,  return_size = None, return_prec = None, memo = {}, use_eq_class = False):

    USE_LOOSE = True

    key = str((expr_depth, return_size, return_prec))

    if USE_LOOSE:
        key = str((expr_depth, return_size))



    if expr_depth == 0:
        assert (return_size != None) and (return_prec != None), "Invalid invokation of create_exhaustive_expressions_helper with 0 depth"
        return [Reg("placeholder", return_prec, return_size)]


    copy_fn = copy.deepcopy
    #copy_fn = lambda x : x

    if key in memo:
        print("Memo Hit:", key, len(memo[key]))
        return copy_fn(memo[key])
    else:
        #print("Memo Miss:", key)
        pass



    relavent_ctx = []
    for dsl_inst in dsl_list:
        inst_relavent_ctx = []
        if return_size == None:
            inst_relavent_ctx += dsl_inst.contexts
        else:
            for ctx in dsl_inst.contexts:
                loose_condition = ctx.get_output_size() == return_size
                tight_condition = ctx.get_output_size() == return_size and ctx.in_precision == return_prec
                if USE_LOOSE and loose_condition:
                    inst_relavent_ctx.append(ctx)
                elif not USE_LOOSE and tight_condition:
                    inst_relavent_ctx.append(ctx)


        if use_eq_class and len(inst_relavent_ctx) != 0:
            arg_max = np.argmax([get_num_symbolic_args(ctx) for ctx in inst_relavent_ctx])
            eq_candidate = inst_relavent_ctx[arg_max]
            print("Reduced {} relavent contexts to 1".format(len(inst_relavent_ctx)))
            inst_relavent_ctx = [eq_candidate]


        relavent_ctx += inst_relavent_ctx



    return_expressions = []
    for rctx in relavent_ctx:
        partial_expressions = [copy_fn(rctx)]
        for idx, rctx_arg in enumerate(rctx.context_args):
            if isinstance(rctx_arg, BitVector):
                child_exprs = create_exhaustive_expressions_helper(dsl_list, expr_depth = expr_depth -1, return_size = rctx_arg.size, return_prec = rctx.in_precision, memo = memo, use_eq_class = use_eq_class)
                copied_expressions = []


                print("Relavent contexts at ", key, ": ", len(relavent_ctx))
                print(key)
                print("Making deep copies for ", len(child_exprs) ,  len(partial_expressions))
                PARALLEL = False

                if PARALLEL:
                    POOL_SIZE = 4
                    pool = concurrent.futures.ThreadPoolExecutor(max_workers=POOL_SIZE)
                    results = [0] * len(child_exprs)
                    def worker(idx):
                        results[idx] = copy_fn(partial_expressions)

                    for i in range(len(child_exprs)):
                        pool.submit(worker, i)

                    pool.shutdown(wait=True)
                    for res in results:
                        copied_expressions += res

                else:
                    for i in range(len(child_exprs)):
                        copied_expressions += copy_fn(partial_expressions)
                print("Done Making deep copies")

                print("Binding arguments")
                for i in range(len(child_exprs)):
                    child_expr = child_exprs[i]
                    for j in range(len(partial_expressions)):
                        actual_index = i * len(partial_expressions) + j
                        copied_expressions[actual_index].context_args[idx] = child_expr

                print("Done Binding arguments")

                partial_expressions = copied_expressions
        return_expressions += partial_expressions

    if return_size != None:
        return_expressions += [copy_fn(Reg("placeholder", return_prec, return_size))]

    memo[key] = return_expressions

    return return_expressions

class CountItemsWrapper:
    def __init__(self, items):
        self.items = iter(items)
        self.count = 0

    def __next__(self):
        res = next(self.items)
        self.count += 1
        return res

    def __iter__(self):
        return self



def get_eq_class_relavent_contexts(possible_contexts, tight = True):

    if tight:
        arg_max = np.argmax([get_num_symbolic_args(ctx) for ctx in possible_contexts])
        eq_candidate = possible_contexts[arg_max]
        return [eq_candidate]
    else:
        # Include minimal number of contexts covering input sizes

        # First sort contexts according to most number of symbolic arguments
        sorted_ctxs = sorted(possible_contexts, key = lambda x : get_num_symbolic_args(x))

        accounted_for = []
        candidates = []
        for ctx in sorted_ctxs:
            include = False
            for arg in ctx.context_args:
                if isinstance(arg, BitVector) and arg.size not in accounted_for:
                    include = True
                    accounted_for.append(arg.size)
            if include:
                candidates.append(ctx)
        return candidates






def create_exhaustive_expressions_generator_helper(dsl_list,  expr_depth = 1,  return_size = None, return_prec = None, use_eq_class = False):


    USE_LOOSE = True

    key = str((expr_depth, return_size, return_prec))

    if USE_LOOSE:
        key = str((expr_depth, return_size))


    copy_fn = copy.deepcopy

    if expr_depth == 0:
        assert (return_size != None) and (return_prec != None), "Invalid invokation of create_exhaustive_expressions_helper with 0 depth"
        yield copy_fn(Reg("0_placeholder", return_prec, return_size))
    else:
        relavent_ctx = []
        for dsl_inst in dsl_list:
            inst_relavent_ctx = []
            if return_size == None:
                inst_relavent_ctx += dsl_inst.contexts
            else:
                for ctx in dsl_inst.contexts:
                    loose_condition = ctx.get_output_size() == return_size
                    tight_condition = ctx.get_output_size() == return_size and ctx.in_precision == return_prec
                    if USE_LOOSE and loose_condition:
                        inst_relavent_ctx.append(ctx)
                    elif not USE_LOOSE and tight_condition:
                        inst_relavent_ctx.append(ctx)


            if use_eq_class and len(inst_relavent_ctx) != 0:
                #arg_max = np.argmax([get_num_symbolic_args(ctx) for ctx in inst_relavent_ctx])
                #eq_candidate = inst_relavent_ctx[arg_max]
                #inst_relavent_ctx = [eq_candidate]

                inst_relavent_ctx = get_eq_class_relavent_contexts(inst_relavent_ctx, tight = False)


            relavent_ctx += inst_relavent_ctx


        if return_size != None:
            yield copy_fn(Reg("1_placeholder", return_prec, return_size))

        for rctx in relavent_ctx:
            get_arg = lambda j : rctx.context_args[j]
            symbolic_indices = []
            generators = []

            for idx, c_arg in enumerate(rctx.context_args):
                if isinstance(c_arg, BitVector):
                    corresponding_exprs = create_exhaustive_expressions_generator_helper(dsl_list,   expr_depth = expr_depth - 1,  return_size = c_arg.size, return_prec = rctx.in_precision, use_eq_class = use_eq_class)
                    symbolic_indices.append(idx)
                    gen = CountItemsWrapper(corresponding_exprs)
                    generators.append(gen)

            if len(symbolic_indices) == 3:

                generator_0 = create_exhaustive_expressions_generator_helper(dsl_list,   expr_depth = expr_depth - 1,  return_size = get_arg(symbolic_indices[0]).size, return_prec = rctx.in_precision, use_eq_class = use_eq_class)
                for expr0 in generator_0:

                    generator_1 = create_exhaustive_expressions_generator_helper(dsl_list,   expr_depth = expr_depth - 1,  return_size = get_arg(symbolic_indices[1]).size, return_prec = rctx.in_precision, use_eq_class = use_eq_class)
                    for expr1 in generator_1:

                        generator_2 = create_exhaustive_expressions_generator_helper(dsl_list,   expr_depth = expr_depth - 1,  return_size = get_arg(symbolic_indices[2]).size, return_prec = rctx.in_precision, use_eq_class = use_eq_class)
                        for expr2 in generator_2:
                            copied_rctx = copy.deepcopy(rctx)
                            copied_rctx.context_args[symbolic_indices[0]] = expr0
                            copied_rctx.context_args[symbolic_indices[1]] = expr1
                            copied_rctx.context_args[symbolic_indices[2]] = expr2
                            yield copied_rctx

            elif len(symbolic_indices) == 2:

                generator_0 = create_exhaustive_expressions_generator_helper(dsl_list,   expr_depth = expr_depth - 1,  return_size = get_arg(symbolic_indices[0]).size, return_prec = rctx.in_precision, use_eq_class = use_eq_class)

                for expr0 in generator_0:
                    generator_1 = create_exhaustive_expressions_generator_helper(dsl_list,   expr_depth = expr_depth - 1,  return_size = get_arg(symbolic_indices[1]).size, return_prec = rctx.in_precision, use_eq_class = use_eq_class)
                    for expr1 in generator_1:
                        copied_rctx = copy.deepcopy(rctx)
                        copied_rctx.context_args[symbolic_indices[0]] = expr0
                        copied_rctx.context_args[symbolic_indices[1]] = expr1
                        yield copied_rctx

            elif len(symbolic_indices) == 1:
                for expr0 in generators[0]:
                    copied_rctx = copy.deepcopy(rctx)
                    copied_rctx.context_args[symbolic_indices[0]] = expr0
                    yield copied_rctx
            else:
                print(len(symbolic_indices))
                print(rctx.name)
                print(rctx.emit_context_expr_string())
                assert False, "Unsupported"










def set_reg_names_exprs(expressions):

    results = []
    for expr in expressions:
        new_expr, discard = set_reg_names_exprs_helper(expr, 0)
        results.append(new_expr)

    return results




def set_reg_names_exprs_helper(expr, counter = 0):
    if isinstance(expr, Reg):
        new_Reg = Reg(str(counter), expr.precision, expr.size)

        return new_Reg, counter + 1

    if not isinstance(expr, Context):
        return expr, counter


    for idx, arg in enumerate(expr.context_args):
        updated_arg, updated_counter = set_reg_names_exprs_helper(arg, counter)
        counter = updated_counter
        expr.context_args[idx] = updated_arg


    return expr, counter



def get_max_symbolic_args(dsl_inst):
    max_sym_args = 0

    for ctx in dsl_inst.contexts:
        max_sym_args = max(max_sym_args, len([arg for arg in ctx.context_args if isinstance(arg, BitVector)]))

    return max_sym_args


def convert_bounded_dsl_inst_to_multiple_contexts(dsl_inst):
    assert dsl_inst.has_bounded_behavior(), "Instruction must be bounded"

    ctx = dsl_inst.contexts[0]
    precs = [int(k) for k in ctx.in_bound_map]

    new_ctxs = []
    for prec in precs:
        ctx_copy = copy.deepcopy(ctx)
        ctx_copy.specialize_context_bounded(prec)
        new_ctxs.append(ctx_copy)

    updated_inst = copy.deepcopy(dsl_inst)
    updated_inst.contexts = new_ctxs

    return updated_inst


def get_expr_intermediate_sizes(dsl_expr):

    assert isinstance(dsl_expr, Context), "Expected context type "

    sizes = [dsl_expr.out_vectsize]
    for arg in dsl_expr.context_args:
        if isinstance(arg, Context):
            sizes += get_expr_intermediate_sizes(arg)
        elif isinstance(arg, BitVector):
            sizes.append(arg.size)
    return sizes

def get_expr_depth(dsl_expr):

    if isinstance(dsl_expr, Context):
        return 1 + max([get_expr_depth(arg) for arg in dsl_expr.context_args])

    else:
        return 0



def print_dsl_list_summary(dsl_list):
    num_eq_classes = len(dsl_list)
    num_ctxs = sum([len(inst.contexts) for inst in dsl_list])

    print("="*50)
    print("Number of Eq Classes:\t", num_eq_classes)
    print("Number of Target Contexts:\t", num_ctxs)
    print("="*50)

