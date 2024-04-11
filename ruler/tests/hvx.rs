ruler::impl_hvx!(128);

#[path = "./recipes/bv4_fancy.rs"]
pub mod bv4_fancy;

#[cfg(test)]
pub mod test {
    use std::time::{Duration, Instant};

    use ruler::{
        enumo::{self, Filter, Metric, Ruleset, Workload},
        recipe_utils::{base_lang, recursive_rules, run_workload, Lang,iter_metric},
        Limits
    };

    use crate::HvxLang;

    fn gen() -> (Ruleset<HvxLang>, Duration) {
        let start = Instant::now();
        let mut rules: Ruleset<HvxLang> = Ruleset::default();
        let lang = Lang::new(
            &["0", "1"],
            &["reg_0", "reg_1", "reg_2"],
            &[&["vdeal", "vshuff"], &[]],
        );
        rules.extend(recursive_rules(
            enumo::Metric::Atoms,
            2,
            lang.clone(),
            Ruleset::default(),
        ));

        // too slow for 128
        let a6_canon = iter_metric(base_lang(2), "EXPR", enumo::Metric::Atoms, 6)
            .plug("VAR", &Workload::new(lang.vars))
            .plug("VAL", &Workload::empty())
            .plug("OP", &Workload::new(lang.ops[0].clone()))
            .filter(Filter::Canon(vec![
                "a".to_string(),
                "b".to_string(),
                "c".to_string(),
            ]));
        let consts = Workload::new(["0", "1"]);
        let wkld = Workload::Append(vec![a6_canon, consts]);
        rules.extend(run_workload(
            wkld,
            rules.clone(),
            Limits::synthesis(),
            Limits::minimize(),
            true,
        ));

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
