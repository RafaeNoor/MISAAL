// ruler/tests/misaal.rs

use num::{ToPrimitive, Zero};
use ruler::*;
use z3::ast::Ast;
use std::io::BufReader;
use std::io::BufRead;
use std::process::Stdio;

use cli_runner::{run, get_stdout, get_stderr};

use ruler::{
    enumo::{Filter, Metric, Ruleset, Workload},
    recipe_utils::{iter_metric, recursive_rules, run_workload, Lang},
    Limits,
};

type Constant = i64;
egg::define_language! {
    pub enum Pred {
        BVLit(Constant),
        "vec_d" = vec_d(Id),
        "vec_s" = vec_s(Id),
        Var(Symbol),
    }
}

impl SynthLanguage for Pred {
    type Constant = Constant;

    fn eval<'a, F>(&'a self, cvec_len: usize, mut get_cvec: F) -> CVec<Self>
    where
        F: FnMut(&'a Id) -> &'a CVec<Self>,
    {
        match self {
            Pred::BVLit(v0) => {
                println!("Interpreting BVlit");
                vec![Some(v0.clone()); cvec_len]
            }
            Pred::vec_d(x) => {
                println!("interpreting vec_d");
                map!(get_cvec, x =>
                Some(x.clone())
                )
            }
            Pred::vec_s(x) => {
                println!("interpreting vec_s");
                map!(get_cvec, x =>
                Some(x.clone())

                )
            }
            Pred::Var(_) => vec![],
        }
    }

    fn initialize_vars(egraph: &mut EGraph<Self, SynthAnalysis>, vars: &[String]) {
        let consts = vec![Some(1.to_i64().unwrap())];
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
        matches!(self, Pred::BVLit(_))
    }

    fn mk_constant(c: Self::Constant, _egraph: &mut EGraph<Self, SynthAnalysis>) -> Self {
        Pred::BVLit(c)
    }

    fn validate(lhs: &Pattern<Self>, rhs: &Pattern<Self>) -> ValidationResult {

        fn egg_to_rosette(expr: &[Pred]) -> std::string::String {
            let mut buf = "".to_string();
            let mut inner_str = "";
            for node in expr.as_ref().iter() {
                // terminal is guaranteed to be a BV
                match node {
                    Pred::Var(v) => {

                        let bv_code = "i";
                        print!("var found {}\n", v);
                        buf.push_str(&bv_code);

                    }, 
                    Pred::BVLit(c) => {
                        let mut nums_str = c.to_string();
                        let nums_init = nums_str
                            .trim()
                            .split_whitespace()
                            .flat_map(str::parse::<i128>)
                            .collect::<Vec<_>>();
                        /* let mut bv_code = "(concat ".to_string();
                        for i in nums_init {
                            bv_code.push_str("(integer->bitvector ");
                            bv_code.push_str(&i.to_string());
                            bv_code.push_str(" (bitvector 128)) ");
                        }
                        bv_code.push_str(")"); */
                        let bv_code = "i";
                        print!("bvlit found {}\n", c);
                        buf.push_str(&bv_code);
                    }
                    Pred::vec_d(a) => {
                        let bv_code = format!(
                            "(hexagon_V6_vdealb_128B {} 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0)",
                            buf
                        );
                        // buf.push_str(&bv_code);
                        buf = bv_code;
                    }
                    Pred::vec_s(a) => {
                        let bv_code =
                            format!("(hexagon_V6_vshuffh_128B {} 1024 16 0 16 8 16 8 0)", buf);
                        // buf.push_str(&bv_code);
                        buf = bv_code;
                    }
                }
            }
            return buf;
        }
        let lexpr = egg_to_rosette(Self::instantiate(lhs).as_ref());
        let rexpr = egg_to_rosette(Self::instantiate(rhs).as_ref());

        let rkt_code = (&format!(
            r#"'
                (require hydride/utils/bvops)
                (require hydride/utils/misc)
                (require hydride/ir/hvx/semantics)
                (define-symbolic i (bitvector 1024))
                (verify (assert (bveq {} {})))
                '
                "#,
            lexpr, rexpr
        ));
        let cmd = format!("/home/baronia3/bin/racket -I rosette -e {}", rkt_code);
        print!("cmd to run: {}\n", cmd);
        let output = run(&cmd); //assert!(output.status.success());
        let mut so = get_stdout(&output).to_string();
        so = so.trim().to_owned();
        print!("output of cmd = {}", &so);

        match so.as_ref() {
            "(unsat)" => ValidationResult::Valid,
            _ => ValidationResult::Invalid,
        }
    }

    /* fn validate(lhs: &Pattern<Self>, rhs: &Pattern<Self>) -> ValidationResult {
        let lexpr = egg_to_external_prog(Self::instantiate(lhs).as_ref());
        let rexpr = egg_to_external_prog(Self::instantiate(rhs).as_ref());
        println!("LEFT EXPRESSION");
        println!("{}", lexpr);
        println!("RIGHT EXPRESSION");
        println!("{}", rexpr);
        ValidationResult::Valid
    } */
}

/* fn egg_to_external_prog<'a>(expr: &[Pred]) -> String {
    let mut buf: Vec<String> = vec![];
    for node in expr.as_ref().iter() {
        match node {
            Pred::BVLit(v0) => {
                //buf.push("(lits)".to_string())
                buf.push(format!("{}", v0))
            }
            Pred::Var(v0) => {
                //buf.push("(vars)".to_string())

                buf.push(format!("{}", v0))
            }
            Pred::vec_d(x) => buf.push(format!("(vec_d_dsl {})", &buf[usize::from(*x)])),
            Pred::vec_s(x) => buf.push(format!("(vec_s_dsl {})", &buf[usize::from(*x)])),
        }
    }
    buf.pop().unwrap()
} */

#[cfg(test)]
#[path = "./recipes/misaal.rs"]
mod vec;

mod test {
    use crate::vec::vec_rules;
    use crate::Pred;
    use std::time::{Duration, Instant};

    use ruler::{
        enumo::{Filter, Metric, Ruleset, Workload},
        logger,
        recipe_utils::{iter_metric, recursive_rules, run_workload, Lang},
        Limits,
    };

    #[test]
    fn run() {
        let start = Instant::now();
        // Runs the actual search
        let all_rules = vec_rules();
        let duration = start.elapsed();
    }

    /* #[test]
    fn wkld_test() {
        let lang = Workload::new(["(vec_d EXPR)", "(vec_s EXPR)", "VAL"]);
        let depth3 = iter_metric(lang, "EXPR", Metric::Depth, 3)
            .plug("VAL", &Workload::new(["val_0", "val_1", "val_2"]));
        depth3.pretty_print();
    } */
}
