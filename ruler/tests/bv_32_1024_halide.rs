use cli_runner::{get_stderr, get_stdout, run};
use num::{ToPrimitive, Zero};
use rand::distributions::Alphanumeric;
use rand::{thread_rng, Rng};
use rayon::vec;
use ruler::*;
use std::fs::File;
use std::fs::OpenOptions;
use std::io::Write;
use std::iter;
use z3::ast::Ast;

type Constant = i32; // Set this to desired precision; can extend i32 to BV of given size (1024 for initial experiments)

egg::define_language! {
    pub enum MISAALLang {       // Flat grammar, will contain both Halide and HVX terms for relevance sets
        Lit(Constant),          // Constants will be stored as i32, but interpreter will convert to BV of desired length
        "hexagon_V6_vminuh_128B" = HVXMin([Id;2]),
        "typed:unsigned-vec-min" = HalideVecMin([Id;2]),
        /* "hexagon_V6_vltuh_128B" = HVXLt([Id;2]),
        "typed:unsigned-vec-lt" = HalideVecLt([Id;2]),
        "typed:unsigned-vec-sat-sub" = HalideVecSatSub([Id;2]), */              // 10 - 12 is one relevance set
        /*"hexagon_V6_vandvrt_128B" = HVXAvg([Id;2]),
        "typed:unsigned-vec-shr" = HalideVecShr([Id;2]),                        // 13 - 15 is one relevance set
        "typed:unsigned-vec-div" = HalideVecDiv([Id;2]), */
        Var(Symbol),
    }
}

impl SynthLanguage for MISAALLang {
    fn is_halide_allowed_op(&self) -> bool {
        matches!(self, MISAALLang::HalideVecMin(_)) && !matches!(self, MISAALLang::HVXMin(_))
    }

    fn is_hvx_allowed_op(&self) -> bool {
        matches!(self, MISAALLang::HVXMin(_)) && !(matches!(self, MISAALLang::HalideVecMin(_)))
    }

    type Constant = Constant;
    fn eval<'a, F>(&'a self, cvec_len: usize, mut get_cvec: F) -> CVec<Self>
    where
        F: FnMut(&'a Id) -> &'a CVec<Self>,
    {
        let one = 1.to_i32().unwrap();
        let zero = 0.to_i32().unwrap();
        match self {
            MISAALLang::Lit(c) => vec![],
            MISAALLang::HVXMin([x, y]) => {
                /*  map!(get_cvec, x, y =>
                    {
                        // let mut bv_x = format!("(integer->bitvector {} (bitvector 1024))", x);
                        // let mut bv_y = format!("(integer->bitvector {} (bitvector 1024))", y);
                        // // println!("x for HVXMin is {:?}", bv_x);
                        // // println!("y for HVXMin is {:?}", bv_y);
                        // Some(x.clone().min(y).clone())
                        // vec!{Some(x.clone()), Some(y.clone())}
                        vec![]
                    }
                ) */
                vec![]
            }

            MISAALLang::HalideVecMin([x, y]) => {
                /*  map!(get_cvec, x, y =>
                    {
                        let mut bv_x = format!("(integer->bitvector {} (bitvector 1024))", x);
                        let mut bv_y = format!("(integer->bitvector {} (bitvector 1024))", y);
                        // println!("x for HalideVecMin is {:?}", bv_x);
                        // println!("y for HalideVecMin is {:?}", bv_y);
                        // Some(x.clone().min(y).clone())
                        // vec!{Some(x.clone()), Some(y.clone())}
                        vec![]
                    }
                ) */
                vec![]
            }

            /* MISAALLang::HVXLt([x, y]) => {
                map!(get_cvec, x, y =>
                    {
                        let mut bv_x = format!("(integer->bitvector {} (bitvector 1024))", x);
                        let mut bv_y = format!("(integer->bitvector {} (bitvector 1024))", y);
                        // println!("x for HVXMin is {:?}", bv_x);
                        // println!("y for HVXMin is {:?}", bv_y);
                        //if x < y {Some(one.clone())} else {Some(zero.clone())}
                        Some(x.clone())

                    }
                )
            }

            MISAALLang::HalideVecLt([x, y]) => {
                map!(get_cvec, x, y =>
                    {
                        // let mut bv_x = format!("(integer->bitvector {} (bitvector 1024))", x);
                        // let mut bv_y = format!("(integer->bitvector {} (bitvector 1024))", y);
                        //  if x < y {Some(one.clone())} else {Some(zero.clone())}
                        Some(x.clone())
                    }
                )
            }

            MISAALLang::HalideVecSatSub([x, y]) => {
                map!(get_cvec, x, y =>
                    {
                        // let mut bv_x = format!("(integer->bitvector {} (bitvector 1024))", x);
                        // let mut bv_y = format!("(integer->bitvector {} (bitvector 1024))", y);
                        // // println!("x for HalideVecSatSub is {:?}", bv_x);
                        // // println!("y for HalideVecSatSub is {:?}", bv_y);
                        // x.checked_sub(*y)
                        Some(x.clone())
                    }
                )
            } */
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
        //println!("================================");
        let mut rng = thread_rng();
        let mut file_name: String = iter::repeat(())
            .map(|()| rng.sample(Alphanumeric))
            .map(char::from)
            .take(8)
            .collect();

        file_name = "/home/llvm-lab/Downloads/MISAAL/ruler/tests/misaal_exprs/".to_owned()
            + &file_name
            + ".expr";

        let mut data_file = File::create(&file_name).expect("creation failed");
        data_file = OpenOptions::new()
            .append(true)
            .open(&file_name)
            .expect("cannot open file");

        //print!("LHS expr:");
        let (lexpr, lexpr_str) = egg_to_z3(&ctx, Self::instantiate(lhs).as_ref());
        //print!("RHS expr:");
        let (rexpr, rexpr_str) = egg_to_z3(&ctx, Self::instantiate(rhs).as_ref());
        data_file
            .write(lexpr_str.as_bytes())
            .expect("Unable to write LHS to file");
        data_file
            .write("\n".as_bytes())
            .expect("Unable to write newline");
        data_file
            .write(rexpr_str.as_bytes())
            .expect("Unable to write RHS to file");
        // println!("================================");
        solver.assert(&lexpr._eq(&rexpr).not());
        match solver.check() {
            z3::SatResult::Unsat => ValidationResult::Valid,
            z3::SatResult::Unknown => ValidationResult::Unknown,
            z3::SatResult::Sat => ValidationResult::Invalid,
        }
    }
}

fn egg_to_z3<'a>(ctx: &'a z3::Context, expr: &[MISAALLang]) -> (z3::ast::Int<'a>, String) {
    let mut buf: Vec<z3::ast::Int> = vec![];
    let mut misaal_buf: Vec<String> = vec![];
    let zero = z3::ast::Int::from_i64(ctx, 0);
    let one = z3::ast::Int::from_i64(ctx, 1);
    for node in expr.as_ref().iter() {
        match node {
            MISAALLang::Lit(c) => {
                match c {
                    1 => misaal_buf.push("(reg (bv #x01 8)) ".to_string()),
                    0 => misaal_buf.push("(reg (bv #x00 8)) ".to_string()),
                    _ => misaal_buf.push("(reg (bv #x02 8)) ".to_string()),
                }
                buf.push(z3::ast::Int::from_i64(ctx, c.to_i64().unwrap()))
            }
            MISAALLang::HVXMin([x, y]) => {
                // push expression to buffer, run through double_synthesis_grammar
                // if synthesis is successful, the rule is valid
                // the function checks for a given concretization, we have to specify output sizes
                let l = &buf[usize::from(*x)];
                let r = &buf[usize::from(*y)];

                let bv_code = format!(
                    " (hexagon_V6_vminuh_128B {} {} 1024 1024 0 1024 16 0 0) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
                buf.push(z3::ast::Bool::ite(&z3::ast::Int::le(l, r), l, r))
            }
            MISAALLang::HalideVecMin([x, y]) => {
                let l = &buf[usize::from(*x)];
                let r = &buf[usize::from(*y)];
                let bv_code = format!(
                    " (typed:unsigned-vec-min {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
                buf.push(z3::ast::Bool::ite(&z3::ast::Int::le(l, r), l, r))
            }
            MISAALLang::Var(v) => {
                match v.as_str() {
                    "a" => misaal_buf.push("(reg (bv #x01 8)) ".to_string()),
                    "b" => misaal_buf.push("(reg (bv #x00 8)) ".to_string()),
                    _ => misaal_buf.push("(reg (bv #x02 8)) ".to_string()),
                }
                buf.push(z3::ast::Int::new_const(ctx, v.to_string()))
            }
        }
    }
    (buf.pop().unwrap(), misaal_buf.pop().unwrap().to_string())
}

#[cfg(test)]

mod test {
    use crate::MISAALLang;
    use std::time::{Duration, Instant};

    use env_logger::filter;
    use ruler::{
        enumo::{Filter, Metric, Ruleset, Workload},
        logger,
        recipe_utils::{base_lang, iter_metric, recursive_rules, run_workload, Lang},
        Limits,
    };

    #[test]
    fn run() {
        let mut rules: Ruleset<MISAALLang> = Ruleset::default();
        /* let lang = Lang::new(
            &["0", "1", "-1", "2"],
            &["a", "b", "c"],
            &[
                &[],
                &[
                    "hexagon_V6_vminuh_128B",
                    // "hexagon_V6_vltuh_128B",
                    //"typed:unsigned-vec-sat-sub",
                    "typed:unsigned-vec-min",
                    // "typed:unsigned-vec-lt",
                ],
            ],
        );
        rules.extend(recursive_rules(
            Metric::Atoms,
            10,
            lang.clone(),
            Ruleset::default(),
        )); */

        /* let wkld = Workload::new(&["(bop e e)", "v"])
        .plug("e", &Workload::new(&["(bop v v)", "v"]))
        .plug(
            "bop",
            &Workload::new(&[
                "hexagon_V6_vminuh_128B",
                // "hexagon_V6_vltuh_128B",
                // "typed:unsigned-vec-sat-sub",
                "typed:unsigned-vec-min",
                // "typed:unsigned-vec-lt",
            ]),
        )
        .plug("v", &Workload::new(&["a", "b"]))
        .filter(Filter::Canon(vec!["a".to_string(), "b".to_string()])); */
        let lang = Lang::new(
            &["0", "1", "-1", "2"],
            &["a", "b", "c"],
            &[
                &[],
                &[
                    "hexagon_V6_vminuh_128B",
                    // "hexagon_V6_vltuh_128B",
                    //"typed:unsigned-vec-sat-sub",
                    "typed:unsigned-vec-min",
                    // "typed:unsigned-vec-lt",
                ],
            ],
        );
        // n is depth
        let wkld = iter_metric(base_lang(2), "EXPR", Metric::Depth, 3)
            .plug("VAR", &Workload::new(lang.vars))
            .plug("VAL", &Workload::empty())
            .plug("OP1", &Workload::new(lang.ops[0].clone()))
            .plug("OP2", &Workload::new(lang.ops[1].clone()))
            .filter(Filter::Canon(vec![
                "a".to_string(),
                "b".to_string(),
                "c".to_string(),
            ]));

        rules.extend(run_workload(
            wkld,
            rules.clone(),
            Limits::synthesis(),
            Limits::minimize(),
            true,
        ));
        println!("---- OUR FINAL RULES ----");
        rules.pretty_print();
    }
}
