use num::{ToPrimitive, Zero};
use ruler::*;
use z3::ast::Ast;

type Constant = i64;
egg::define_language!{
    pub enum Pred {
        BVLit(Constant),
        "hexagon_V6_vdealb_128B" = hexagon_V6_vdealb_128B([Id;15]),
        "hexagon_V6_vshuffh_128B" = hexagon_V6_vshuffh_128B([Id;9]),
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
                Pred::hexagon_V6_vdealb_128B([v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14]) => {
                    println!("interpreting hexagon_V6_vdealb_128B");
                    //map!(get_cvec, v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14 => 
                    map!(get_cvec, v0 => 
                        Some(v0.clone())
                        ) 
                }
                Pred::hexagon_V6_vshuffh_128B([v0,v1,v2,v3,v4,v5,v6,v7,v8]) => {
                    println!("interpreting hexagon_V6_vshuffh_128B");
                    //map!(get_cvec, v0, v1, v2, v3, v4, v5, v6, v7,v8 => 
                    map!(get_cvec, v0 => 
                        Some(v0.clone())
                        
                        ) 
                }
                Pred::Var(_) => vec![],
            }
        }


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
        matches!(self, Pred::BVLit(_))
    }

    fn mk_constant(c: Self::Constant, _egraph: &mut EGraph<Self, SynthAnalysis>) -> Self {
        Pred::BVLit(c)
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

fn egg_to_rosette<'a>(expr: &[Pred]) ->  String {
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
            Pred::hexagon_V6_vdealb_128B([v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14]) => {buf.push(format!("(hexagon_V6_vdealb_128B_dsl {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} )", &buf[usize::from(*v0)], &buf[usize::from(*v1)], &buf[usize::from(*v2)], &buf[usize::from(*v3)], &buf[usize::from(*v4)], &buf[usize::from(*v5)], &buf[usize::from(*v6)], &buf[usize::from(*v7)], &buf[usize::from(*v8)], &buf[usize::from(*v9)], &buf[usize::from(*v10)], &buf[usize::from(*v11)], &buf[usize::from(*v12)], &buf[usize::from(*v13)], &buf[usize::from(*v14)]))}
            Pred::hexagon_V6_vshuffh_128B([v0,v1,v2,v3,v4,v5,v6,v7,v8]) => {buf.push(format!("(hexagon_V6_vshuffh_128B_dsl {} {} {} {} {} {} {} {} {} )", &buf[usize::from(*v0)], &buf[usize::from(*v1)], &buf[usize::from(*v2)], &buf[usize::from(*v3)], &buf[usize::from(*v4)], &buf[usize::from(*v5)], &buf[usize::from(*v6)], &buf[usize::from(*v7)], &buf[usize::from(*v8)]))}
        }
    }
    buf.pop().unwrap()
}


#[cfg(test)]
#[path = "./recipes/misaal.rs"]
mod misaal;

mod test {
    use crate::misaal::misaal_rules;
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
        let all_rules = misaal_rules();
        let duration = start.elapsed();


    }
}
