use core::arch;

use ruler::{
    enumo::{Filter, Metric, Ruleset, Workload},
    recipe_utils::{
        base_lang, iter_metric, recursive_rules, run_fast_forwarding, run_fast_forwarding_misaal,
        run_workload, Lang,
    },
    Limits,
};

use crate::MISAAL;

fn iter_pos(n: usize) -> Workload {
    iter_metric(base_lang(2), "EXPR", Metric::Atoms, n)
        .filter(Filter::Contains("VAR".parse().unwrap()))
        .plug("VAL", &Workload::new(["0", "1", "2"]))
        .plug("VAR", &Workload::new(["a", "b", "c"]))
        .plug("OP1", &Workload::new([""]))
        .plug(
            "OP2",
            &Workload::new([
                "halide_+", "hvx_+", "hvx_*",
            ]),
        )
}
pub fn halide_hvx_rules() -> Ruleset<MISAAL> {
    let mut all_rules = Ruleset::default();

    /* let misaal_rules = Workload::new(&[
           "(halide_bop halide_e halide_e)",
           "(hvx_bop hvx_e hvx_e)",
           "v",
       ])
       .plug("halide_e", &Workload::new(&["(halide_bop v v)", "v"]))
       .plug(
           "halide_bop",
           &Workload::new(&["halide_+", "halide_-", "halide_*", "halide_/"]),
       )
       .plug("hvx_e", &Workload::new(&["(hvx_bop v v)", "v"]))
       .plug(
           "hvx_bop",
           &Workload::new(&["hvx_+", "hvx_-", "hvx_*", "hvx_/"]),
       )
       .plug("v", &Workload::new(&["a", "b", "c"]))
       .filter(Filter::Canon(vec![
           "a".to_string(),
           "b".to_string(),
           "c".to_string(),
       ]));
    */

    let misaal_rules = Workload::new(&["(bop e e)", "v"])
        .plug("e", &Workload::new(&["(bop v v)", "v"]))
        .plug(
            "bop",
            &Workload::new(&[
                "halide_+", "hvx_+", "hvx_*" 
            ]),
        )
        .plug("v", &Workload::new(&["a", "b", "c"]))
        .filter(Filter::Canon(vec![
            "a".to_string(),
            "b".to_string(),
            "c".to_string(),
        ]));

    let consts = Workload::new(["0", "1", "2"]);

    let limits = Limits {
        iter: 3,
        node: 2000000,
        match_: 200_000,
    };

    let wkld = Workload::Append(vec![misaal_rules, consts]);

    let atoms4 = iter_pos(4);

    let new_misaal = run_fast_forwarding_misaal(wkld, all_rules.clone(), limits, limits);

    // println!("new_misaal rules : {:?}", new_misaal);

    /* all_rules.extend(new_misaal);

    let atoms6 = iter_pos(6);

    let newer_misaal = run_fast_forwarding_misaal(atoms6, all_rules.clone(), limits, limits);

    all_rules.extend(newer_misaal); */

    all_rules
}
