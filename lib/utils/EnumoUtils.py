import common.Types
import time
import copy
import sys
from common.Types import *
from  common.Instructions import Context
import subprocess
import os
import tempfile
import glob


def define_enumo_language(dsl_list):
    clauses = []
    clauses.append("BVLit(Symbol, i64)")
    for dsl_inst in dsl_list:
        name = dsl_inst.name
        num_args = len(dsl_inst.contexts[0].context_args)
        clauses.append("\"{}\" = {}([Id;{}])".format(name,name,num_args))

    clauses.append("Var(Symbol)")
    definition = "egg::define_language!{\n"
    definition += "pub enum Pred {\n"
    definition += ",\n".join(clauses)
    definition += "}\n}\n"
    return definition

def emit_enumo_interpret_clause(dsl_inst):
    ctx = dsl_inst.contexts[0]
    num_args = len(ctx.context_args)
    src_args = ",".join(["v{}".format(i) for i in range(num_args)])
    src = "Pred::{}[{}]".format(dsl_inst.name, src_args)
    arrow = "=>"
    dst = "{" + "map!(get_cvec, {} => Some(apply_{}({}))) ".format(src_args, dsl_inst.name, src_args) + "}"

    return "{} {} {}".format(src,arrow,dst)


def define_enumo_grammar_clauses(dsl_list):
    out_vect_sizes = []
    for expr in dsl_list:
        for ctx in expr.contexts:
            out_vect_sizes.append(ctx.out_vectsize)

    unique_sizes = sorted(list(set(out_vect_sizes)))

    def CLAUSE_NAME(size):
        return "EXPR_{}".format(size)

    size_to_grammar_map = {}
    for size in unique_sizes:
        size_to_grammar_map[size] = []

        for dsl_inst in dsl_list:
            for ctx in dsl_inst.contexts:

                if ctx.out_vectsize != size:
                    continue
                clause = [dsl_inst.name]

                for arg in ctx.context_args:
                    if isinstance(arg, BitVector):
                        clause.append(CLAUSE_NAME(arg.size))
                    elif isinstance(arg,ConstBitVector):
                        clause.append("BVLit(\"{}\",{})".format(arg.value, arg.size))
                    else:
                        clause.append(str(arg.value))

                clause = "\"(" + " ".join(clause) +")\""

                size_to_grammar_map[size].append(clause)

    lang = "let lang = Workload::new([\n"
    for size in size_to_grammar_map:
        lang += "\"{}\",\n".format(CLAUSE_NAME(size))

    lang += "\);"


    definitions = [lang]
    for size in size_to_grammar_map:
        clauses = (",\n".join(size_to_grammar_map[size]))
        define_size = "let {} : &[&str] = &[\n".format(CLAUSE_NAME(size))
        define_size += clauses
        define_size += "];"
        definitions.append(define_size)


    # Plug in definitions
    iter_metric = "iter_metric(lang, \"{}\", Metric::Depth, n)\n".format(CLAUSE_NAME(unique_sizes[-1]))

    for size in size_to_grammar_map:
        iter_metric += ".plug(\"{}\", &{}.into())\n".format(CLAUSE_NAME(size), CLAUSE_NAME(size))



    function_prototype = "fn iter_grammar(n: usize) -> Workload {"

    function = [function_prototype, "\n".join(definitions), iter_metric, "}\n"]

    return "\n".join(function)







def emit_enumo_emit_clause_to_rosette(dsl_inst):
    ctx = dsl_inst.contexts[0]
    num_args = len(ctx.context_args)
    src_args = ",".join(["v{}".format(i) for i in range(num_args)])
    src = "Pred::{}[{}]".format(dsl_inst.name, src_args)
    arrow = "=>"
    dst = "{" + "map!(get_cvec, {} => Some(apply_{}({}))) ".format(src_args, dsl_inst.name, src_args) + "}"

    expr_to_string = "("+dsl_inst.name+"_dsl "

    rust_fmt = []
    for idx, arg in enumerate(ctx.context_args):
        # Rust will format it later
        expr_to_string += "{} "
        rust_fmt.append(
            "&buf[usize::from(*{})]".format("v"+str(idx))
        )

    expr_to_string += ")"
    dst =  "{"+ "buf.push(format!(\"{}\", {}))".format(expr_to_string, ", ".join(rust_fmt)) + "}"

    return "{} {} {}".format(src,arrow,dst)


def define_enumo_egg_to_rosette(dsl_list):

    for dsl_inst in dsl_list:
        print(emit_enumo_emit_clause_to_rosette(dsl_inst))
