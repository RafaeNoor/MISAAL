#![recursion_limit = "256"]

use cli_runner::{get_stderr, get_stdout, run};
use num::{ToPrimitive, Zero};
use rand::distributions::Alphanumeric;
use rand::{thread_rng, Rng};
use rayon::vec;
use ruler::*;
use std::env;
use std::fs::File;
use std::fs::OpenOptions;
use std::io::Write;
use std::iter;
use z3::ast::Ast;

type Constant = i32;

egg::define_language! {
    pub enum MISAALLang {       // Flat grammar, will contain both Halide and HVX terms for relevance sets
        Lit(Constant),          // Constants will be stored as i32, but interpreter will convert to BV of desired length
        "hexagon_V6_vasrhv_128B" = HexagonV6Vasrhv128b([Id;(2)]),
        "typed:cast-int" = Typed_cast_int(Id),
        "typed:cast-uint" = Typed_cast_uint(Id),
        "typed:vec-bwnot" = Typed_vec_bwnot(Id),
        "typed:signed-vec-mod" = Typed_signed_vec_mod([Id;(2)]),
        "typed:signed-vec-min" = Typed_signed_vec_min([Id;(2)]),
        "typed:vec-shl" = Typed_vec_shl([Id;(2)]),
        "typed:unsigned-vec-sat-sub" = Typed_unsigned_vec_sat_sub([Id;(2)]),
        "typed:unsigned-vec-max" = Typed_unsigned_vec_max([Id;(2)]),
        "typed:signed-vec-max" = Typed_signed_vec_max([Id;(2)]),
        "typed:unsigned-vec-mod" = Typed_unsigned_vec_mod([Id;(2)]),
        "typed:unsigned-vec-sat-add" = Typed_unsigned_vec_sat_add([Id;(2)]),
        "typed:signed-vec-shr" = Typed_signed_vec_shr([Id;(2)]),
        "typed:unsigned-vec-min" = Typed_unsigned_vec_min([Id;(2)]),
        "typed:vec-bwand" = Typed_vec_bwand([Id;(2)]),
        "hexagon_V6_vlsrwv_128B" = HexagonV6Vlsrwv128b([Id;(2)]),
        "typed:unsigned-vec-div" = Typed_unsigned_vec_div([Id;(2)]),
        "typed:unsigned-vec-shr" = Typed_unsigned_vec_shr([Id;(2)]),
        Var(Symbol),
    }
}

impl SynthLanguage for MISAALLang {
    fn is_halide_allowed_op(&self) -> bool {
        !matches!(
            self,
            MISAALLang::HexagonV6Vasrhv128b(_) | MISAALLang::HexagonV6Vlsrwv128b(_)
        )
    }

    fn is_hvx_allowed_op(&self) -> bool {
        matches!(
            self,
            MISAALLang::HexagonV6Vasrhv128b(_) | MISAALLang::HexagonV6Vlsrwv128b(_)
        )
    }

    type Constant = Constant;
    fn eval<'a, F>(&'a self, cvec_len: usize, mut get_cvec: F) -> CVec<Self>
    where
        F: FnMut(&'a Id) -> &'a CVec<Self>,
    {
        match self {
            MISAALLang::Lit(c) => vec![],
            MISAALLang::HexagonV6Vasrhv128b([a, b]) => vec![],
            MISAALLang::Typed_cast_int(a) => vec![],
            MISAALLang::Typed_cast_uint(a) => vec![],
            MISAALLang::Typed_vec_bwnot(a) => vec![],
            MISAALLang::Typed_signed_vec_mod([a, b]) => vec![],
            MISAALLang::Typed_signed_vec_min([a, b]) => vec![],
            MISAALLang::Typed_vec_shl([a, b]) => vec![],
            MISAALLang::Typed_unsigned_vec_sat_sub([a, b]) => vec![],
            MISAALLang::Typed_unsigned_vec_max([a, b]) => vec![],
            MISAALLang::Typed_signed_vec_max([a, b]) => vec![],
            MISAALLang::Typed_unsigned_vec_mod([a, b]) => vec![],
            MISAALLang::Typed_unsigned_vec_sat_add([a, b]) => vec![],
            MISAALLang::Typed_signed_vec_shr([a, b]) => vec![],
            MISAALLang::Typed_unsigned_vec_min([a, b]) => vec![],
            MISAALLang::Typed_vec_bwand([a, b]) => vec![],
            MISAALLang::HexagonV6Vlsrwv128b([a, b]) => vec![],
            MISAALLang::Typed_unsigned_vec_div([a, b]) => vec![],
            MISAALLang::Typed_unsigned_vec_shr([a, b]) => vec![],
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

        file_name = env::var("EXPR_DIR").unwrap().to_owned() + &file_name + ".expr";

        let mut data_file = File::create(&file_name).expect("creation failed");
        data_file = OpenOptions::new()
            .append(true)
            .open(&file_name)
            .expect("cannot open file");

        //print!("LHS expr:");
        let lexpr_str = egg_misaal_validator(&ctx, Self::instantiate(lhs).as_ref());
        //print!("RHS expr:");
        let rexpr_str = egg_misaal_validator(&ctx, Self::instantiate(rhs).as_ref());
        data_file
            .write(lexpr_str.as_bytes())
            .expect("Unable to write LHS to file");
        data_file
            .write("\n".as_bytes())
            .expect("Unable to write newline");
        data_file
            .write(rexpr_str.as_bytes())
            .expect("Unable to write RHS to file");

        let cmd = format!(
            // need to parallelize for it to be usable
            // "python3 /home/baronia3/new-MISAAL/MISAAL/test/double_synthesis/enumo_validator.py {}",
            "python3 /home/baronia3/new-MISAAL/MISAAL/test/double_synthesis/hex_pattern.py {}",
            file_name
        );

        // print!("cmd to run: {}\n", cmd);
        let output = run(&cmd);
        // assert!(output.status.success());
        let mut so = get_stdout(&output).to_string();
        so = so.trim().to_owned();
        if so.contains("ENUMO_SUCC") {
            println!("We have a success for in file {}", &file_name);
            ValidationResult::Valid
        } else {
            ValidationResult::Invalid
        }
    }
}

fn egg_misaal_validator<'a>(ctx: &'a z3::Context, expr: &[MISAALLang]) -> String {
    // let mut buf: Vec<z3::ast::Int> = vec![];
    let mut misaal_buf: Vec<String> = vec![];
    // let zero = z3::ast::Int::from_i64(ctx, 0);
    // let one = z3::ast::Int::from_i64(ctx, 1);
    for node in expr.as_ref().iter() {
        match node {
            MISAALLang::Lit(c) => {
                misaal_buf.push(format!("(reg (bv #x0{} 8)) ", c).to_string());
            }
            MISAALLang::HexagonV6Vasrhv128b([x, y]) => {
                let bv_code = format!(
                    " (hexagon_V6_vasrhv_128B {} (bv #x0000000000000000 16) {} 1024 1024 0 1024 16 1 0) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_cast_int(x) => {
                let bv_code = format!(
                    " (typed:cast-int {} 16 1 64 32) ",
                    &misaal_buf[usize::from(*x)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_cast_uint(x) => {
                let bv_code = format!(
                    " (typed:cast-uint {} 16 1 64 32) ",
                    &misaal_buf[usize::from(*x)]
                );
                misaal_buf.push(bv_code);
            }

            MISAALLang::Typed_vec_bwnot(x) => {
                let bv_code = format!(
                    " (typed:vec-bwnot {} 16 1024) ",
                    &misaal_buf[usize::from(*x)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_signed_vec_mod([x, y]) => {
                let bv_code = format!(
                    " (typed:signed-vec-mod {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_signed_vec_min([x, y]) => {
                let bv_code = format!(
                    " (typed:signed-vec-min {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_vec_shl([x, y]) => {
                let bv_code = format!(
                    " (typed:vec-shl {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_unsigned_vec_sat_sub([x, y]) => {
                let bv_code = format!(
                    " (typed:unsigned-vec-sat-sub {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_unsigned_vec_sat_add([x, y]) => {
                let bv_code = format!(
                    " (typed:unsigned-vec-sat-add {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }

            MISAALLang::Typed_unsigned_vec_max([x, y]) => {
                let bv_code = format!(
                    " (typed:unsigned-vec-max {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_unsigned_vec_min([x, y]) => {
                let bv_code = format!(
                    " (typed:unsigned-vec-min {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_unsigned_vec_mod([x, y]) => {
                let bv_code = format!(
                    " (typed:unsigned-vec-mod {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_signed_vec_max([x, y]) => {
                let bv_code = format!(
                    " (typed:signed-vec-max {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_signed_vec_shr([x, y]) => {
                let bv_code = format!(
                    " (typed:signed-vec-shr {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_vec_bwand([x, y]) => {
                let bv_code = format!(
                    " (typed:vec-bwand {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );

                misaal_buf.push(bv_code);
            }
            MISAALLang::HexagonV6Vlsrwv128b([x, y]) => {
                let bv_code = format!(
                    " (hexagon_V6_vlsrwv_128B {} (lit (bv #x00000000000000000000000000000000 (bitvector 32))) {} 1024 1024 0 1024 32 1 0) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_unsigned_vec_div([x, y]) => {
                let bv_code = format!(
                    " (typed:unsigned-vec-div {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }
            MISAALLang::Typed_unsigned_vec_shr([x, y]) => {
                let bv_code = format!(
                    " (typed:unsigned-vec-shr {} {} 16 1024) ",
                    &misaal_buf[usize::from(*x)],
                    &misaal_buf[usize::from(*y)]
                );
                misaal_buf.push(bv_code);
            }

            MISAALLang::Var(v) => match v.as_str() {
                "a" => misaal_buf.push("(reg (bv #x01 8)) ".to_string()),
                "b" => misaal_buf.push("(reg (bv #x00 8)) ".to_string()),
                "c" => misaal_buf.push("(reg (bv #x02 8)) ".to_string()),
                _ => misaal_buf.push("(reg (bv #x03 8)) ".to_string()),
            },
        }
    }
    misaal_buf.pop().unwrap().to_string()
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
        let depth = 2;

        let mut rules_34: Ruleset<MISAALLang> = Ruleset::default();

        let lang_34 = Lang::new(
            &["0", "1", "2", "3", "4", "5", "6", "7", "8"],
            &["a", "b", "c", "d", "e", "f", "g", "h", "i"],
            &[
                &[],
                &[
                    "typed:unsigned-vec-shr",
                    "typed:unsigned-vec-div",
                    "hexagon_V6_vlsrwv_128B",
                ],
            ],
        );

        let wkld_34 = iter_metric(base_lang(2), "EXPR", Metric::Depth, depth)
            .plug("VAR", &Workload::new(lang_34.vars))
            .plug("VAL", &Workload::empty())
            .plug("OP1", &Workload::new(lang_34.ops[0].clone()))
            .plug("OP2", &Workload::new(lang_34.ops[1].clone()));

        rules_34.extend(run_workload(
            wkld_34,
            rules_34.clone(),
            Limits::synthesis(),
            Limits::minimize(),
            true,
        ));
        println!("---- RULES for RELEVANCE SET 34 ----");
        rules_34.pretty_print();
        println!("------------------------------------");

        /* let mut rules_37: Ruleset<MISAALLang> = Ruleset::default();

        let lang_37 = Lang::new(
            &["0", "1", "2", "3", "4", "5", "6", "7", "8"],
            &["a", "b", "c", "d", "e", "f", "g", "h", "i"],
            &[
                &["typed:cast-uint", "typed:cast-int", "typed:vec-bwnot"],
                &[
                    "typed:signed-vec-mod",
                    "typed:signed-vec-min",
                    "typed:vec-shl",
                    "typed:unsigned-vec-sat-sub",
                    "typed:signed-vec-max",
                    "typed:unsigned-vec-mod",
                    "typed:unsigned-vec-shr",
                    "typed:vec-bwand",
                    "typed:unsigned-vec-min",
                    "typed:signed-vec-shr",
                    "typed:unsigned-vec-max",
                    "typed:unsigned-vec-sat-add",
                    "hexagon_V6_vasrhv_128B",
                ],
            ],
        );

        let wkld_37 = iter_metric(base_lang(2), "EXPR", Metric::Depth, depth)
            .plug("VAR", &Workload::new(lang_37.vars))
            .plug("VAL", &Workload::empty())
            .plug("OP1", &Workload::new(lang_37.ops[0].clone()))
            .plug("OP2", &Workload::new(lang_37.ops[1].clone()));

        rules_37.extend(run_workload(
            wkld_37,
            rules_37.clone(),
            Limits::synthesis(),
            Limits::minimize(),
            true,
        ));
        println!("---- RULES for RELEVANCE SET 37 ----");
        rules_37.pretty_print(); */
    }
}
