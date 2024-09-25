use num::{ToPrimitive, Zero};
use ruler::*;
use z3::ast::Ast;
use cli_runner::{run, get_stdout, get_stderr};

type Constant = i32; // Set this to desired precision; can extend i32 to BV of given size (1024 for initial experiments)

egg::define_language! {
    pub enum MISAALLang {       // Flat grammar, will contain both Halide and HVX terms for relevance sets
        Lit(Constant),          // Constants will be stored as i32, but interpreter will convert to BV of desired length
        "hexagon_V6_vminuh_128B" = HVXMin([Id;2]),            
        "typed:unsigned-vec-sat-sub" = HalideVecSatSub([Id;2]),              // 10 - 12 is one relevance set                                    
        "typed:unsigned-vec-min" = HalideVecMin([Id;2]),
        /*"hexagon_V6_vandvrt_128B" = HVXAvg([Id;2]),
        "typed:unsigned-vec-shr" = HalideVecShr([Id;2]),                        // 13 - 15 is one relevance set
        "typed:unsigned-vec-div" = HalideVecDiv([Id;2]), */
        Var(Symbol),
    }
}

impl SynthLanguage for MISAALLang {
    type Constant = Constant;
    fn eval<'a, F>(&'a self, cvec_len: usize, mut get_cvec: F) -> CVec<Self>
    where
        F: FnMut(&'a Id) -> &'a CVec<Self>,
    {
        match self {
            MISAALLang::Lit(c) => vec![Some(c.clone()); cvec_len],
            MISAALLang::HVXMin([x, y]) => {
                map!(get_cvec, x, y => 
                    {
                        let mut bv_x = format!("(integer->bitvector {} (bitvector 1024))", x);
                        let mut bv_y = format!("(integer->bitvector {} (bitvector 1024))", y);
                        println!("x for HVXMin is {:?}", bv_x);
                        println!("y for HVXMin is {:?}", bv_y);
                        Some(x.min(y).clone())
                    }
                )
            }

            MISAALLang::HalideVecMin([x, y]) => {
                map!(get_cvec, x, y => 
                    {
                        let mut bv_x = format!("(integer->bitvector {} (bitvector 1024))", x);
                        let mut bv_y = format!("(integer->bitvector {} (bitvector 1024))", y);
                        println!("x for HalideVecMin is {:?}", bv_x);
                        println!("y for HalideVecMin is {:?}", bv_y);
                        Some(x.min(y).clone())
                    }
                )
            }

            MISAALLang::HalideVecSatSub([x, y]) => {
                map!(get_cvec, x, y => 
                    {
                        let mut bv_x = format!("(integer->bitvector {} (bitvector 1024))", x);
                        let mut bv_y = format!("(integer->bitvector {} (bitvector 1024))", y);
                        println!("x for HalideVecSatSub is {:?}", bv_x);
                        println!("y for HalideVecSatSub is {:?}", bv_y);
                        x.checked_sub(*y)
                    }
                )
            }
            MISAALLang::Var(_) => vec![],
        }
    }

    fn initialize_vars(egraph: &mut EGraph<Self, SynthAnalysis>, vars: &[String]) {
        let consts = vec![
            Some((-10).to_i32().unwrap()),
            Some((-1).to_i32().unwrap()),
            Some(0.to_i32().unwrap()),
            Some(1.to_i32().unwrap()),
            Some(2.to_i32().unwrap()),
            Some(5.to_i32().unwrap()),
            Some(100.to_i32().unwrap()),
        ];
        let cvecs = self_product(&consts, vars.len());

        egraph.analysis.cvec_len = cvecs[0].len();

        for (i, v) in vars.iter().enumerate() {
            let id = egraph.add(MISAALLang::Var(Symbol::from(v.clone())));
            let cvec = cvecs[i].clone();
            egraph[id].data.cvec = cvec;
        }
    }

    fn to_var(&self) -> Option<Symbol> {
        if let MISAALLang::Var(sym) = self {
            Some(*sym)
        } else {
            None
        }
    }

    fn mk_var(sym: Symbol) -> Self {
        MISAALLang::Var(sym)
    }

    fn is_constant(&self) -> bool {
        matches!(self, MISAALLang::Lit(_))
    }

    fn mk_constant(c: Self::Constant, _egraph: &mut EGraph<Self, SynthAnalysis>) -> Self {
        MISAALLang::Lit(c)
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

fn egg_to_z3<'a>(ctx: &'a z3::Context, expr: &[MISAALLang]) -> z3::ast::Int<'a> {
    let mut buf: Vec<z3::ast::Int> = vec![];
    let zero = z3::ast::Int::from_i64(ctx, 0);
    let one = z3::ast::Int::from_i64(ctx, 1);
    for node in expr.as_ref().iter() {
        match node {
            MISAALLang::Lit(c) => buf.push(z3::ast::Int::from_i64(ctx, c.to_i64().unwrap())),
            MISAALLang::HVXMin([x, y]) => {
                let l = &buf[usize::from(*x)];
                let r = &buf[usize::from(*y)];
                buf.push(z3::ast::Bool::ite(&z3::ast::Int::le(l, r), l, r))
            }
            MISAALLang::HalideVecMin([x, y]) => {
                let l = &buf[usize::from(*x)];
                let r = &buf[usize::from(*y)];
                buf.push(z3::ast::Bool::ite(&z3::ast::Int::le(l, r), l, r))
            }
            MISAALLang::HalideVecSatSub([x, y]) => buf.push(z3::ast::Int::sub(
                ctx,
                &[&buf[usize::from(*x)], &buf[usize::from(*y)]],
            )),
            MISAALLang::Var(v) => buf.push(z3::ast::Int::new_const(ctx, v.to_string())),
        }
    }
    buf.pop().unwrap()
}

#[cfg(test)]

mod test {
    use crate::MISAALLang;
    use std::time::{Duration, Instant};

    use ruler::{
        enumo::{Filter, Metric, Ruleset, Workload},
        logger,
        recipe_utils::{recursive_rules, run_workload, Lang},
        Limits,
    };

    #[test]
    fn run() {

        let mut all_rules = Ruleset::<MISAALLang>::default();
        let rat_only = recursive_rules(
            Metric::Atoms,
            5,
            Lang::new(
                &["-1", "0", "1"],
                &["a", "b", "c"],
                &[&[""], &["hexagon_V6_vminuh_128B", "typed:unsigned-vec-sat-sub", "typed:unsigned-vec-min"]],
            ),
            all_rules.clone(),
        );
        all_rules.extend(rat_only.clone());
        let nested_bops_full = Workload::new(&["(bop e e)", "v"])
        .plug("e", &Workload::new(&["(bop v v)", "v"]))
        .plug(
            "bop",
            &Workload::new(&["hexagon_V6_vminuh_128B", "typed:unsigned-vec-sat-sub", "typed:unsigned-vec-min"]),
        )
        .plug("v", &Workload::new(&["a", "b", "c"]))
        .filter(Filter::Canon(vec![
            "a".to_string(),
            "b".to_string(),
            "c".to_string(),
        ]));

    let new = run_workload(
        nested_bops_full,
        all_rules.clone(),
        Limits::synthesis(),
        Limits::minimize(),
        true,
    );
    all_rules.extend(new.clone());

    }
}
