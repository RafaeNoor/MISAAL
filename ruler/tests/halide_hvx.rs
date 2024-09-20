use num::{ToPrimitive, Zero};
use ruler::*;
use z3::ast::Ast;
use ruler::{enumo::Ruleset, *};


type Constant = i64;

egg::define_language! {
  pub enum MISAAL {
    Lit(Constant),
    "halide_add" = HalideAdd([Id; 2]),
    "halide_-" = HalideSub([Id; 2]),
    "halide_*" = HalideMul([Id; 2]),
    "halide_/" = HalideDiv([Id; 2]),
    "hvx_+" = HVXAdd([Id; 2]),
    "hvx_-" = HVXSub([Id; 2]),
    "hvx_*" = HVXMul([Id; 2]),
    "hvx_/" = HVXDiv([Id; 2]),
    Var(Symbol),
  }
}

impl SynthLanguage for MISAAL {
    type Constant = Constant;

    fn is_fast_forwarding() -> bool {
        true
    }

    fn get_exploratory_rules() -> Ruleset<Self> {
        Ruleset::new(&[
        "(halide_+ ?a ?b) <==> (hvx_+ ?a ?b)",
        "(halide_- ?a ?b) <==> (hvx_- ?a ?b)",
        //"(halide_* ?a ?b) ==> (hvx_* ?a ?b)",
        //"(halide_/ ?a ?b) ==> (hvx_/ ?a ?b)",
        ])
    }

    fn is_halide_allowed_op(&self) -> bool {
        matches!(self, MISAAL::HalideAdd(_) | MISAAL::HalideDiv(_) | MISAAL::HalideMul(_) | MISAAL::HalideSub(_)) && !matches!(self, MISAAL::HVXAdd(_) | MISAAL::HVXDiv(_) | MISAAL::HVXMul(_) | MISAAL::HVXSub(_))
    }

    fn is_hvx_allowed_op(&self) -> bool {
        !matches!(self, MISAAL::HalideAdd(_) | MISAAL::HalideDiv(_) | MISAAL::HalideMul(_) | MISAAL::HalideSub(_)) && matches!(self, MISAAL::HVXAdd(_) | MISAAL::HVXDiv(_) | MISAAL::HVXMul(_) | MISAAL::HVXSub(_))
    }

    fn eval<'a, F>(&'a self, cvec_len: usize, mut get_cvec: F) -> CVec<Self>
    where
        F: FnMut(&'a Id) -> &'a CVec<Self>,
    {
        /* let one = 1.to_i64().unwrap();
        let zero = 0.to_i64().unwrap();
        match self {
            MISAAL::Lit(c) => vec![Some(c.clone()); cvec_len],
            MISAAL::HalideAdd([x, y]) => map!(get_cvec, x, y => x.checked_add(*y)),
            MISAAL::HalideSub([x, y]) => map!(get_cvec, x, y => x.checked_sub(*y)),
            MISAAL::HalideMul([x, y]) => map!(get_cvec, x, y => x.checked_mul(*y)),
            MISAAL::HalideDiv([x, y]) => map!(get_cvec, x, y => {
              if y.is_zero() {
                Some(zero.clone())
              } else {
                x.checked_div(*y)
              }
            }),
            MISAAL::HVXAdd([x, y]) => map!(get_cvec, x, y => x.checked_add(*y)),
            MISAAL::HVXSub([x, y]) => map!(get_cvec, x, y => x.checked_sub(*y)),
            MISAAL::HVXMul([x, y]) => map!(get_cvec, x, y => x.checked_mul(*y)),
            MISAAL::HVXDiv([x, y]) => map!(get_cvec, x, y => {
              if y.is_zero() {
                Some(zero.clone())
              } else {
                x.checked_div(*y)
              }
            }),
            MISAAL::Var(_) => vec![],
        } */
       vec![]
    }

    /* fn initialize_vars(egraph: &mut EGraph<Self, SynthAnalysis>, vars: &[String]) {
        let consts = vec![
            Some((-10).to_i64().unwrap()),
            Some((-1).to_i64().unwrap()),
            Some(0.to_i64().unwrap()),
            Some(1.to_i64().unwrap()),
            Some(2.to_i64().unwrap()),
            Some(5.to_i64().unwrap()),
            Some(100.to_i64().unwrap()),
        ];
        let cvecs = self_product(&consts, vars.len());

        egraph.analysis.cvec_len = cvecs[0].len();

        for (i, v) in vars.iter().enumerate() {
            let id = egraph.add(MISAAL::Var(Symbol::from(v.clone())));
            let cvec = cvecs[i].clone();
            egraph[id].data.cvec = cvec;
        }
    } */

    fn initialize_vars(_egraph: &mut EGraph<Self, SynthAnalysis>, _vars: &[String]) {}

    fn to_var(&self) -> Option<Symbol> {
        if let MISAAL::Var(sym) = self {
            Some(*sym)
        } else {
            None
        }
    }

    fn mk_var(sym: Symbol) -> Self {
        MISAAL::Var(sym)
    }

    fn is_constant(&self) -> bool {
        matches!(self, MISAAL::Lit(_))
    }

    fn mk_constant(c: Self::Constant, _egraph: &mut EGraph<Self, SynthAnalysis>) -> Self {
        MISAAL::Lit(c)
    }

    fn validate(lhs: &Pattern<Self>, rhs: &Pattern<Self>) -> ValidationResult {
        let mut cfg = z3::Config::new();
        cfg.set_timeout_msec(1000);
        let ctx = z3::Context::new(&cfg);
        let solver = z3::Solver::new(&ctx);
        let lexpr = egg_to_z3(&ctx, Self::instantiate(lhs).as_ref());
        let rexpr = egg_to_z3(&ctx, Self::instantiate(rhs).as_ref());
        solver.assert(&lexpr._eq(&rexpr).not());
        match solver.check() {
            z3::SatResult::Unsat => ValidationResult::Valid,
            z3::SatResult::Unknown => ValidationResult::Unknown,
            z3::SatResult::Sat => ValidationResult::Invalid,
        }
    }
}

fn egg_to_z3<'a>(ctx: &'a z3::Context, expr: &[MISAAL]) -> z3::ast::Int<'a> {
    let mut buf: Vec<z3::ast::Int> = vec![];
    let zero = z3::ast::Int::from_i64(ctx, 0);
    let one = z3::ast::Int::from_i64(ctx, 1);
    for node in expr.as_ref().iter() {
        match node {
            MISAAL::Lit(c) => buf.push(z3::ast::Int::from_i64(ctx, c.to_i64().unwrap())),
            MISAAL::HalideAdd([x, y]) => buf.push(z3::ast::Int::add(
                ctx,
                &[&buf[usize::from(*x)], &buf[usize::from(*y)]],
            )),
            MISAAL::HalideSub([x, y]) => buf.push(z3::ast::Int::sub(
                ctx,
                &[&buf[usize::from(*x)], &buf[usize::from(*y)]],
            )),
            MISAAL::HalideMul([x, y]) => buf.push(z3::ast::Int::mul(
                ctx,
                &[&buf[usize::from(*x)], &buf[usize::from(*y)]],
            )),
            MISAAL::HalideDiv([x, y]) => {
                let l = &buf[usize::from(*x)];
                let r = &buf[usize::from(*y)];
                buf.push(z3::ast::Bool::ite(
                    &r._eq(&zero),
                    &zero,
                    &z3::ast::Int::div(l, r),
                ))
            },
            MISAAL::HVXAdd([x, y]) => buf.push(z3::ast::Int::add(
                ctx,
                &[&buf[usize::from(*x)], &buf[usize::from(*y)]],
            )),
            MISAAL::HVXSub([x, y]) => buf.push(z3::ast::Int::sub(
                ctx,
                &[&buf[usize::from(*x)], &buf[usize::from(*y)]],
            )),
            MISAAL::HVXMul([x, y]) => buf.push(z3::ast::Int::mul(
                ctx,
                &[&buf[usize::from(*x)], &buf[usize::from(*y)]],
            )),
            MISAAL::HVXDiv([x, y]) => {
                let l = &buf[usize::from(*x)];
                let r = &buf[usize::from(*y)];
                buf.push(z3::ast::Bool::ite(
                    &r._eq(&zero),
                    &zero,
                    &z3::ast::Int::div(l, r),
                ))
            },
            MISAAL::Var(v) => buf.push(z3::ast::Int::new_const(ctx, v.to_string())),
        }
    }
    buf.pop().unwrap()
}

#[cfg(test)]
#[path = "./recipes/halide_hvx.rs"]
mod halide_hvx;

mod test {
    use crate::halide_hvx::halide_hvx_rules;
    use crate::MISAAL;
    use std::{path::MAIN_SEPARATOR, time::{Duration, Instant}};

    use recipe_utils::run_fast_forwarding_misaal;
    use ruler::{
        enumo::{Filter, Metric, Ruleset, Workload, Scheduler},
        logger,
        recipe_utils::{base_lang, iter_metric, recursive_rules, run_workload, run_fast_forwarding, Lang},
        Limits,
    };

    use super::*;

    fn iter_pos(n: usize) -> Workload {
        iter_metric(base_lang(2), "EXPR", Metric::Atoms, n)
            .filter(Filter::Contains("VAR".parse().unwrap()))
            .plug("VAL", &Workload::new([""]))
            .plug("VAR", &Workload::new(["a", "b", "c"]))
            .plug("OP1", &Workload::new([""]))
            .plug("OP2", &Workload::new(["halide_+", "halide_*", "halide_/", "halide_-", "hvx_+", "hvx_*", "hvx_/", "hvx_-" ]))

    }

    
    #[test]

    fn run() {

        // let start = Instant::now();
        // let all_rules = halide_hvx_rules();
        // let duration = start.elapsed();
        /* let init_rules = [
            "(halide_+ ?b ?a) ==> (hvx_+ ?a ?b)",
            "(halide_* ?b ?a) ==> (hvx_* ?a ?b)",
        ];

        let mut prior= Ruleset::new(&init_rules); */

        let misaal_wkld = Workload::new(&[
            "(bop e e)",
            "v",
        ])
        .plug("e", &Workload::new(&["(bop v v)", "v"]))
        .plug(
            "bop",
            &Workload::new(&["halide_+", "halide_-", "halide_*", "halide_/", "hvx_+", "hvx_-", "hvx_*", "hvx_/"]),
        )
        .plug("v", &Workload::new(&["a", "b", "c"]))
        .filter(Filter::Canon(vec![
            "a".to_string(),
            "b".to_string(),
            "c".to_string(),
        ]));
    
        let limits = Limits {
            iter: 3,
            node: 2000000,
            match_: 200_000,
        };

        let init = MISAAL::get_exploratory_rules();

        let mut all_rules = Ruleset::default();
        all_rules.extend(init);

        let atoms3 = iter_pos(8);
        // let rules_out = run_fast_forwarding_misaal(misaal_wkld, all_rules.clone(), limits, limits);
        let rules_out = run_fast_forwarding_misaal(atoms3, all_rules.clone(), limits, limits);
        all_rules.extend(rules_out);

        for r in all_rules.0.values() {
            println!("{}", r.name)
        } 

       /*  let eg_init = misaal_wkld.to_egraph();
        // println!("EG INIT for misaal {:?}", eg_init);
        // Allowed rules: run on clone, apply unions, no candidates
        let (allowed, _) = prior.partition(|eq| MISAAL::is_allowed_misaal_rewrite(&eq.lhs, &eq.rhs));

        let eg_allowed = Scheduler::Compress(limits).run(&eg_init, &allowed);

        // Translation rules: grow egraph, extract candidates, assert!(saturated)
        let lifting_rules = MISAAL::get_exploratory_rules();
        let eg_denote = Scheduler::Simple(limits).run(&eg_allowed, &lifting_rules);
        let mut candidates = Ruleset::extract_candidates(&eg_allowed, &eg_denote);

        // All rules: clone/no clone doesn't matter, extract candidates
        let mut all_rules = prior;
        all_rules.extend(lifting_rules);
        let eg_final = Scheduler::Compress(limits).run(&eg_denote, &all_rules);
        candidates.extend(Ruleset::extract_candidates(&eg_denote, &eg_final));

        let rules = candidates;
        for r in rules.0.values() {
            println!("{}", r.name)
        } */


    }
}
