use ruler::{
    enumo::{Filter, Metric, Ruleset, Workload},
    recipe_utils::{recursive_rules, run_workload, Lang,iter_metric},
    Limits,
};

use crate::Pred;
fn iter_grammar(n: usize) -> Workload {
    let lang = Workload::new([
        "EXPR_1024",
    ]);
    let EXPR_1024 : &[&str] = &[
        "(hexagon_V6_vdealb_128B EXPR_1024 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0)",
        "(hexagon_V6_vdealb_128B EXPR_1024 1024 1024 0 512 16 0 512 16 2 32 16 2 16 0)",
        "(hexagon_V6_vshuffh_128B EXPR_1024 1024 32 0 32 16 32 2 0)",
        "(hexagon_V6_vshuffh_128B EXPR_1024 1024 16 0 16 8 16 8 0)",
        "regs"
    ];
    iter_metric(lang, "EXPR_1024", Metric::Depth, n)
        .plug("EXPR_1024", &EXPR_1024.into())
        .plug("regs", &Workload::new(&["reg_0", "reg_1", "reg_2"]))


}

pub fn misaal_rules() -> Ruleset<Pred> {
    println!("Generating misaal rules!");
    let mut all = Ruleset::default();
    let canon = iter_grammar(2);
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
