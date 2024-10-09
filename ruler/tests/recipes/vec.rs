use ruler::{
    enumo::{Filter, Metric, Ruleset, Workload},
    recipe_utils::{iter_metric, recursive_rules, run_workload, Lang},
    Limits,
};

use crate::HvxLang;
fn iter_grammar(n: usize) -> Workload {
    let lang = Workload::new(["(vdeal EXPR)", "(vshuff EXPR)", "VAL"]);
    let depth3 = iter_metric(lang, "EXPR", Metric::Depth, 3)
        .plug("VAL", &Workload::new(["reg_0_1024", "reg_1_1024"]));
    depth3
}

pub fn vec_rules() -> Ruleset<HvxLang> {
    println!("Generating vec rules!");
    let mut all = Ruleset::default();
    let canon = iter_grammar(3);
    let get_rules = run_workload(
        canon,
        all.clone(),
        Limits::synthesis(),
        Limits::minimize(),
        true,
    );

    all.extend(get_rules);
    all
}
