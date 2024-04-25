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
    clauses.append("\"BVLit\" = BVLit([Id;2])")
    clauses.append("Int(Constant)")
    for dsl_inst in dsl_list:
        name = dsl_inst.name
        num_args = len(dsl_inst.contexts[0].context_args)
        clauses.append("\"{}\" = {}([Id;{}])".format(name,name,num_args))

    clauses.append("Var(Symbol),")
    definition = "type Constant = i64;"
    definition += "\negg::define_language!{\n"
    definition += "pub enum Pred {\n"
    definition += ",\n".join(clauses)
    definition += "\n}\n}\n"
    return definition

def emit_enumo_interpret_clause(dsl_inst):
    ctx = dsl_inst.contexts[0]
    num_args = len(ctx.context_args)
    src_args = ",".join(["v{}".format(i) for i in range(num_args)])
    src = "Pred::{}([{}])".format(dsl_inst.name, src_args)
    arrow = "=>"
    #dst = "{" + "map!(get_cvec, {} => Some(apply_{}({}))) ".format(src_args, dsl_inst.name, src_args) + "}"

    dst = "{" + "map!(get_cvec, {} => Some({}.clone())) ".format(src_args, "v0") + "}"

    return "{} {} {}".format(src,arrow,dst)


def emit_enumo_eval(dsl_list):
    clauses = []

    BVLitClause = "Pred::BVLit([x0,x1]) => { map!(get_cvec, x0, x1 => Some(x1.clone())) }"

    IntClause = "Pred::Int(v0) => { vec![Some(v0.clone()); cvec_len]}"

    clauses += [BVLitClause, IntClause]
    for dsl_inst in dsl_list:
        clauses.append(emit_enumo_interpret_clause(dsl_inst))

    function_prototype = """fn eval<'a, F>(&'a self, cvec_len: usize, mut get_cvec: F) -> CVec<Self>
    where
        F: FnMut(&'a Id) -> &'a CVec<Self>,
    """

    function_body = "match self {"+ "\n {}\n".format("\n".join(clauses)) +"}"

    function_body = "vec![]"

    return function_prototype +"{\n" + function_body + "\n}"


RUN_FIXED = """
#[cfg(test)]
#[path = "./recipes/misaal_recipe.rs"]
mod misaal;

mod test {
    use crate::misaal::vec_rules;
    use crate::Pred;
    use std::time::{Duration, Instant};

    use ruler::{
        enumo::{Filter, Metric, Ruleset, Workload},
        logger,
        recipe_utils::{recursive_rules, run_workload, Lang},
        Limits,
    };

    #[test]
    fn run() {
        // Skip this test in github actions
        if std::env::var("CI").is_ok() && std::env::var("SKIP_RECIPES").is_ok() {
            return;
        }

        let start = Instant::now();
        // Runs the actual search
        let all_rules = vec_rules();
        let duration = start.elapsed();


    }
}
"""

SYNTH_LANG_TOP = """
impl SynthLanguage for Pred {
    type Constant = Constant;

"""
SYNTH_LANG_BOTTOM = """
    fn initialize_vars(egraph: &mut EGraph<Self, SynthAnalysis>, vars: &[String]) {
        let consts = vec![
            Some(1.to_i64().unwrap()),
        ];
        let cvecs = self_product(&consts, vars.len());

        egraph.analysis.cvec_len = cvecs[0].len();

        for (i, v) in vars.iter().enumerate() {
            let id = egraph.add(Pred::Var(Symbol::from(v.clone())));
            let cvec = cvecs[i].clone();
            egraph[id].data.cvec = cvec;
        }
    }

    fn to_var(&self) -> Option<Symbol> {
        if let Pred::Var(sym) = self {
            Some(*sym)
        } else {
            None
        }
    }

    fn mk_var(sym: Symbol) -> Self {
        Pred::Var(sym)
    }

    fn is_constant(&self) -> bool {
        matches!(self, Pred::Int(_))
    }

    fn mk_constant(c: Self::Constant, _egraph: &mut EGraph<Self, SynthAnalysis>) -> Self {
        //Pred::BVLit(c)
        Pred::Int(c)
    }


    fn validate(lhs: &Pattern<Self>, rhs: &Pattern<Self>) -> ValidationResult {
        let lexpr = egg_to_rosette(Self::instantiate(lhs).as_ref());
        let rexpr = egg_to_rosette(Self::instantiate(rhs).as_ref());
        println!("LEFT EXPRESSION");
        println!("{}",lexpr);
        println!("RIGHT EXPRESSION");
        println!("{}",rexpr);
        ValidationResult::Invalid
    }
}
"""



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
                        clause.append("(BVLit {} {})".format(int(arg.value[2:],16), arg.size))
                    else:
                        clause.append(str(arg.value))

                clause = "\"(" + " ".join(clause) +")\""

                size_to_grammar_map[size].append(clause)


    definitions = []


    for size in size_to_grammar_map:
        clauses = (",\n".join(size_to_grammar_map[size]))
        define_size = "let {} : &[&str] = &[\n".format(CLAUSE_NAME(size))
        define_size += clauses
        define_size += ", \"REG_{}\"".format(size)
        define_size += "\n];"
        definitions.append(define_size)

    for size in unique_sizes:
        lang = "\nlet lang_{}= Workload::new(".format(size)
        lang += CLAUSE_NAME(size)

        #lang += ",\"REG_{}\"".format(size)

        lang += ");"
        definitions.append(lang)

        # Plug in definitions
        iter_metric = "let exprs_{} = iter_metric(lang_{}, \"{}\", Metric::Depth, n)".format(size, size, CLAUSE_NAME(size))
        iter_metric += "\n\t.plug(\"REG_{}\", &Workload::new([\"val_0\", \"val_1\", \"val_2\"]));".format(size)
        definitions.append(iter_metric)


    """
    # Plug in definitions
    iter_metric = "iter_metric(lang, \"{}\", Metric::Depth, n)\n".format(CLAUSE_NAME(unique_sizes[-1]))

    for size in size_to_grammar_map:
        iter_metric += ".plug(\"{}\", &{}.into())\n".format(CLAUSE_NAME(size), CLAUSE_NAME(size))


    #depth_n = "let depth_n = iter_metric(lang, \"\")"


    function_prototype = "fn iter_grammar(n: usize) -> Workload {"

    function = [function_prototype, "\n".join(definitions), iter_metric, "}\n"]

    """

    function_prototype = "fn iter_grammar(n: usize) -> Workload {"

    function = [function_prototype, "\n".join(definitions), "}\n"]
    return "\n".join(function)







def emit_enumo_emit_clause_to_rosette(dsl_inst):
    ctx = dsl_inst.contexts[0]
    num_args = len(ctx.context_args)
    src_args = ",".join(["v{}".format(i) for i in range(num_args)])
    src = "Pred::{}([{}])".format(dsl_inst.name, src_args)
    arrow = "=>"
    #dst = "{" + "map!(get_cvec, {} => Some(apply_{}({}))) ".format(src_args, dsl_inst.name, src_args) + "}"

    dst = "{" + "map!(get_cvec, {} => Some({})) ".format(src_args, "v0") + "}"

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

    prototype = "fn egg_to_rosette<'a>(expr: &[Pred]) ->  String {\n"
    buffer_def = "let mut buf: Vec<String> = vec![];\n"
    match_stmt = "for node in expr.as_ref().iter() { \n match node {\n"

    emit_clauses = [emit_enumo_emit_clause_to_rosette(dsl_inst) for dsl_inst in dsl_list]

    BVLitClause = "Pred::BVLit([x0,x1]) => { buf.push(format!(\"BVLit {} {}\", &buf[usize::from(*x0)], &buf[usize::from(*x1)]))}"
    IntClause = "Pred::Int(v0) => { buf.push(format!(\"{}\", v0))}"
    VarClause = "Pred::Var(v0) => { buf.push(format!(\"{}\", v0))}"

    emit_clauses +=[BVLitClause, IntClause, VarClause]


    function = prototype + buffer_def + match_stmt + "\n".join(emit_clauses) + " }\n}\n"
    function += "buf.pop().unwrap()\n}\n"

    return function



MAIN_HEADER  = """
use num::{ToPrimitive, Zero};
use ruler::*;
use z3::ast::Ast;
"""

RECIPE_HEADER = """
use ruler::{
    enumo::{Filter, Metric, Ruleset, Workload},
    recipe_utils::{recursive_rules, run_workload, Lang,iter_metric},
    Limits,
};

use crate::Pred;

"""


RECIPE_FIXED = """
pub fn vec_rules() -> Ruleset<Pred> {
    println!("Generating vec rules!");
    let mut all = Ruleset::default();
    let canon = iter_grammar(3);
    let get_rules = run_workload(
        canon,
        all.clone(),
        Limits::synthesis(),
        Limits::minimize(),
        true
    );

    all.extend(get_rules);
    all
}
"""

def emit_enumo_files(dsl_list, main_file_name = "misaal.rs", recipe_file_name = "misaal_recipe.rs"):
    main_file_contents = []
    recipe_file_contents = []

    def add_to_main(x):
        main_file_contents.append("\n")
        main_file_contents.append(x)

    def add_to_recipe(x):
        recipe_file_contents.append("\n")
        recipe_file_contents.append(x)

    main_file_fns = [define_enumo_language, define_enumo_egg_to_rosette]
    recipe_file_fns = [define_enumo_grammar_clauses]

    add_to_main(MAIN_HEADER)


    eval_fn = emit_enumo_eval(dsl_list)

    for m in main_file_fns:
        add_to_main(m(dsl_list))

    SynthLang = SYNTH_LANG_TOP + eval_fn + SYNTH_LANG_BOTTOM

    add_to_main(SynthLang)

    add_to_recipe(RECIPE_HEADER)

    for m in recipe_file_fns:
        add_to_recipe(m(dsl_list))


    add_to_recipe(RECIPE_FIXED)
    add_to_main(RUN_FIXED)


    with open(main_file_name, "w+") as MainFile:
        MainFile.write("\n".join(main_file_contents))

    with open(recipe_file_name, "w+") as MainFile:
        MainFile.write("\n".join(recipe_file_contents))



