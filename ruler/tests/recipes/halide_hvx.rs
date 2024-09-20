use ruler::{
    enumo::{Filter, Metric, Ruleset, Workload},
    recipe_utils::{recursive_rules, run_fast_forwarding, run_workload, Lang},
    Limits,
};

use crate::MISAAL;

pub fn halide_hvx_rules() -> Ruleset<MISAAL> {
    let mut all_rules = Ruleset::default();

    let misaal_rules = Workload::new(&[
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

    let limits = Limits {
        iter: 3,
        node: 2000000,
        match_: 200_000,
    };

    let new_misaal = run_fast_forwarding(misaal_rules.clone(), all_rules.clone(), limits, limits);

    // println!("new_misaal rules : {:?}", new_misaal);

    all_rules.extend(new_misaal);

    all_rules
}
