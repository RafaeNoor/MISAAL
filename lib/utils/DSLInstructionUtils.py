import common.Types
from  common.Instructions import Context
import subprocess
import os
import tempfile
import glob


HYDRIDE_HEADER =  """
        #lang rosette
        (require rosette/lib/synthax)
        (require rosette/lib/angelic)
        (require racket/pretty)
        (require data/bit-vector)
        (require rosette/lib/destruct)
        (require rosette/solver/smt/boolector)
        (require hydride)

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

    dsl_name = dsl_inst.name + "_dsl"
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



def execute_racket_file(statements):

    filename = next(tempfile._get_candidate_names()) + ".rkt"
    with open(filename, "w+") as WriteFile:
        def write_line(line):
            WriteFile.write(line + "\n")

        write_line(HYDRIDE_HEADER)

        for statement in statements:
            write_line(statement)

    result = subprocess.run(["racket {}".format(filename)], shell=True)

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


def check_if_contexts_equal(ctx1, ctx2, dsl_inst1, dsl_inst2,vector_sizes, code_synthesizer_desc):
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

    create_expr_1 = "(define expr_1 {})".format(emit_context_expr(ctx1, dsl_inst1))
    create_expr_2 = "(define expr_2 {})".format(emit_context_expr(ctx2, dsl_inst2))

    result_expr_1 = code_synthesizer_desc.interpret_expr("expr_1", "env")
    result_expr_2 = code_synthesizer_desc.interpret_expr("expr_2", "env")

    cex = "(define cex {})".format(emit_verify_equal(result_expr_1, result_expr_2))

    print_cex = ";(println cex)"

    cex_unsat_check = "(unsat? cex)"

    handler = emit_racket_cond([cex_unsat_check, "else"], ["(displayln \"PROPERTY HOLDS!\") (exit 0)",
    "(displayln \"PROPERTY DOES NOT HOLD!\") (exit 1)"])


    statements = [create_env, create_expr_1, create_expr_2, cex, print_cex, handler]



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

        #subprocess.call("rm -f {}".format(read_out_fname), shell = True)

    return (is_simplified, simplified_expr)


def cleanup_tmp_files():
    tmp_files = glob.glob("/tmp/base_*")
    print("Cleaning up {} tmp files ...".format(len(tmp_files)))
    for f in tmp_files:
        subprocess.call("rm -f {}".format(f), shell = True)

