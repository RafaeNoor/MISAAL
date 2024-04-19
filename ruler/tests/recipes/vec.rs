use ruler::{
    enumo::{Filter, Metric, Ruleset, Workload},
    recipe_utils::{recursive_rules, run_workload, Lang,iter_metric},
    Limits,
};

use crate::Pred;
fn iter_grammar(n: usize) -> Workload {
    let lang = Workload::new(["(vec_d EXPR)", "(vec_s EXPR)", "VAL"]);
    let depth3 = iter_metric(lang, "EXPR", Metric::Depth, 3)
                       .plug("VAL", &Workload::new(["val_0", "val_1", "val_2"]));


}

pub fn vec_rules() -> Ruleset<Pred> {
    println!("Generating vec rules!");
    let mut all = Ruleset::default();
    let canon = iter_grammar(3);
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
