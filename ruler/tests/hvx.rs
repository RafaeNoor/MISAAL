ruler::impl_hvx!(128);

#[path = "./recipes/bv4_fancy.rs"]
pub mod bv4_fancy;

#[cfg(test)]
pub mod test {
    use std::time::{Duration, Instant};

    use ruler::{
        enumo::{self, Filter, Metric, Ruleset, Workload},
        recipe_utils::{base_lang, iter_metric, recursive_rules, run_workload, Lang},
        Limits,
    };

    use crate::HvxLang;

    fn gen() -> (Ruleset<HvxLang>, Duration) {
        let start = Instant::now();
        /* let mut rules: Ruleset<HvxLang> = Ruleset::default();
        let lang = Lang::new(
            &["0", "1"],
            &["val_0", "val_1", "val_2"],
            &[&["vdeal", "vshuff"], &[]],
        );
        rules.extend(recursive_rules(
            enumo::Metric::Atoms,
            2,
            lang.clone(),
            Ruleset::default(),
        )); */

        println!("Generating vec rules!");
        let mut rules = Ruleset::default();
        let lang = Workload::new(["(vdeal EXPR)", "(vshuff EXPR)", "VAL"]);
        let depth3 = iter_metric(lang, "EXPR", Metric::Depth, 3)
            .plug("VAL", &Workload::new(["val_0", "val_1", "val_2"]));
        let get_rules = run_workload(
            depth3,
            rules.clone(),
            Limits::synthesis(),
            Limits::minimize(),
            true,
        );

        rules.extend(get_rules);
        let duration = start.elapsed();
        (rules, duration)
    }

    #[test]
    fn compare() {
        // let domain = "BV128";
        // Port the bv4 rules into domain
        // let actual_bv4_rules: Ruleset<_> = bv4_fancy_rules();
        // let ported_bv4_rules: Ruleset<Bv> = Ruleset::new(actual_bv4_rules.to_str_vec());

        // Generate the rules directly
        let (_gen, _gen_time): (Ruleset<HvxLang>, Duration) = gen();

        // logger::write_bv_derivability(domain, gen, gen_time, ported_bv4_rules)
    }
}
