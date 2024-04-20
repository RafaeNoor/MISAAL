use num::{ToPrimitive, Zero};
use ruler::*;
use rand::prelude::Distribution;
use rand::Rng;
use std::io::BufReader;
use std::io::BufRead;
use std::process::Stdio;
use rand::prelude::*;
use rand_pcg::Pcg64;
use serde::{Deserialize, Serialize};
use std::fmt;
use std::ops::*;
use cli_runner::{run, get_stdout, get_stderr};

#[derive(Copy, Clone, Hash, PartialOrd, Ord, PartialEq, Eq, Serialize, Deserialize)]
#[serde(transparent)]
pub struct HVXVec<const N: Inner>(pub Inner);

type Inner = i128;
const INNER_N: Inner = (core::mem::size_of::<Inner>() * 8) as Inner;

type BV128 = HVXVec<128>;


impl<const N: Inner> HVXVec<N> {
    pub const ZERO: Self = Self(0);
    pub const ALL_ONES: Self = Self((!(0)) >> (INNER_N - N));
    pub const NEG_ONE: Self = Self::ALL_ONES;
    pub const MIN: Self = Self(1 << (N - 1));
    pub const MAX: Self = Self(Self::ALL_ONES.0 >> 1);

    pub fn new(n: impl Into<Inner>) -> Self {
        Self(n.into() & Self::ALL_ONES.0)
    }

    pub fn wrapping_add(self, rhs: Self) -> Self {
        Self::new(self.0.wrapping_add(rhs.0))
    }

    pub fn wrapping_sub(self, rhs: Self) -> Self {
        Self::new(self.0.wrapping_sub(rhs.0))
    }

    pub fn wrapping_mul(self, rhs: Self) -> Self {
        Self::new(self.0.wrapping_mul(rhs.0))
    }

    pub fn wrapping_neg(self) -> Self {
        Self::new(self.0.wrapping_neg())
    }

    pub fn my_shl(self, rhs: Self) -> Self {
        if rhs.0 >= N {
            Self::ZERO
        } else {
            Self::new(self.0 << rhs.0)
        }
    }

    pub fn my_shr(self, rhs: Self) -> Self {
        if rhs.0 >= N {
            Self::ZERO
        } else {
            Self::new(self.0 >> rhs.0)
        }
    }
}

impl<const N: Inner> Not for HVXVec<N> {
    type Output = Self;

    fn not(self) -> Self::Output {
        Self::new(self.0.not())
    }
}

impl<const N: Inner> BitAnd for HVXVec<N> {
    type Output = Self;

    fn bitand(self, rhs: Self) -> Self::Output {
        Self::new(self.0.bitand(rhs.0))
    }
}

impl<const N: Inner> BitOr for HVXVec<N> {
    type Output = Self;

    fn bitor(self, rhs: Self) -> Self::Output {
        Self::new(self.0.bitor(rhs.0))
    }
}

impl<const N: Inner> BitXor for HVXVec<N> {
    type Output = Self;

    fn bitxor(self, rhs: Self) -> Self::Output {
        Self::new(self.0.bitxor(rhs.0))
    }
}

impl<const N: Inner> fmt::Debug for HVXVec<N> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        fmt::Display::fmt(&self.0, f)
    }
}

impl<const N: Inner> fmt::Display for HVXVec<N> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        fmt::Display::fmt(&self.0, f)
    }
}

impl<const N: Inner> fmt::Binary for HVXVec<N> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        fmt::Binary::fmt(&self.0, f)
    }
}

impl<const N: Inner> fmt::LowerHex for HVXVec<N> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        fmt::LowerHex::fmt(&self.0, f)
    }
}

impl<const N: Inner> Distribution<HVXVec<N>> for rand::distributions::Standard {
    fn sample<R: Rng + ?Sized>(&self, rng: &mut R) -> HVXVec<N> {
        let inner: Inner = rng.gen();
        inner.into()
    }
}

impl<const N: Inner> std::str::FromStr for HVXVec<N> {
    type Err = std::num::ParseIntError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        print!("Here is the string: {}", s);
        if let Some(stripped) = s.strip_prefix("#b") {
            let i = Inner::from_str_radix(stripped, 2).unwrap();
            return Ok(Self::new(i));
        }
        s.parse::<Inner>().map(Self::new)
    }
}

impl<const N: Inner> From<Inner> for HVXVec<N> {
    fn from(v: Inner) -> Self {
        Self::new(v)
    }
}

#[derive(Copy, Clone, Hash, PartialOrd, Ord, PartialEq, Eq, Serialize, Deserialize)]
#[serde(transparent)]
pub struct HVXVec8_128([BV128; 8]);


impl HVXVec8_128 {
    pub const ZERO: Self = Self([BV128::ZERO; 8]);
    pub const ALL_ONES: Self = Self([BV128::ALL_ONES; 8]);
    pub const NEG_ONE: Self = Self::ALL_ONES;
    pub const MIN: Self = Self([BV128::MIN; 8]);
    pub const MAX: Self = Self([BV128::MAX; 8]);

    /* pub fn new(n: impl Into<Inner>) -> Self {
        Self([BV128::from(n.into());8])
    } */
    pub fn new(from_arr: [Inner; 8]) -> Self {
        let mut array: [BV128; 8] = Self::ZERO.0;
        for (pos, &e) in from_arr.iter().enumerate() {
            array[pos] = BV128::from(e);
        }
        Self(array)
    }

    pub fn new_from_vec(from_vec: Vec<Inner>) -> Self {
        let mut array: [BV128; 8] = Self::ZERO.0;
        for (pos, &e) in from_vec.iter().enumerate() {
            array[pos] = BV128::from(e);
        }
        Self(array)
    }
}

impl fmt::Debug for HVXVec8_128 {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        for v in &self.0 {
            write!(f, "\t{}", v)?;
        }
        Ok(())
    }
}

impl fmt::Display for HVXVec8_128 {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        for v in &self.0 {
            write!(f, "\t{}", v)?;
        }
        Ok(())
    }
}

impl std::str::FromStr for HVXVec8_128 {
    type Err = std::num::ParseIntError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        print!("Here is the string: {}\n", s);
        let mut s = s.replace(&['(', ')', ',', '\"', '.', ';', ':', '\''][..], "");
        let len = s.len();
        s.truncate(len - 1);
        Ok(HVXVec8_128::new_from_vec(
            s.trim()
                .split(' ')
                .flat_map(str::parse::<i128>)
                .collect::<Vec<_>>(),
        ))
    }
}

impl From<[Inner; 8]> for HVXVec8_128 {
    fn from(arr: [Inner; 8]) -> Self {
        Self::new(arr)
    }
}

egg::define_language! {
    pub enum HvxLang {
            "vdeal" = VDeal(Id),
            "vshuff" = VShuff(Id),
            Lit(HVXVec8_128),
            // Lit(HVXVec),
            Var(egg::Symbol),
        }
  }



impl SynthLanguage for HvxLang {
    type Constant = HVXVec8_128;

    fn eval<'a, F>(&'a self, cvec_len: usize, mut get_cvec: F) -> CVec<Self>
    where
        F: FnMut(&'a Id) -> &'a CVec<Self>,
    {
        match self {
            HvxLang::VDeal(a) => map!(get_cvec, a => {
            /* let mut bv_code = format!("(integer->bitvector ");
            bv_code.push_str(&a.to_string());
            bv_code.push_str(" (bitvector 128))");
            let rkt_code = (&format!(r#"'(bitvector->integer (bvadd {} {}))'"#, bv_code, bv_code));
            let cmd = format!("/home/baronia3/bin/racket -I rosette -e {}", rkt_code);
            let output = run(&cmd);
            assert!(output.status.success());
            let mut so = get_stdout(&output).to_string();
            let len = so.len();
            so.truncate(len - 1);
            assert!(!so.is_empty());
            print!("{:?}", so);
            let ret = so.parse::<i32>().unwrap();
            print!("ret {:?}\n", ret); */
            let mut bv_code = format!("(integer->bitvector ");
            bv_code.push_str(&a.to_string());
            bv_code.push_str(" (bitvector 1024))");
            let rkt_code = &format!(r#"'
            (require hydride/utils/bvops)
            (require hydride/utils/misc)
            (require hydride/ir/hvx/semantics)
            (for/list ([%i (range 0 8 1)]) 
                (bitvector->integer (extract (* (+ %i 1) 127) (* %i 128) (hexagon_V6_vdealb_128B {} 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0)))
            )'
            "#, bv_code);
            let cmd = format!("/home/baronia3/bin/racket -I rosette -e {}", rkt_code);
            print!("cmd to run: {}\n", cmd);
            let output = run(&cmd);
            //assert!(output.status.success());
            let so = get_stdout(&output).to_string();
            let len = so.len();
            print!("so unfilterd {:?}", so);

            let mut so = so.replace(&['(', ')', ',', '\"', '.', ';', ':', '\''][..], "");
            so.truncate(len - 1);
            assert!(!so.is_empty());
            print!("cmd {:?}  \n", so);
            let nums = so.trim().split(' ').flat_map(str::parse::<i128>).collect::<Vec<_>>();
            /* for num in nums {
                println!("num from bv {}", num);
            } */
            // let ret = so.parse::<i128>().unwrap();
            // print!("ret {:?}\n\n\n", ret);
            // Some(HVXVec::from(5 as i128))
            Some(HVXVec8_128::new_from_vec(nums))
            }),
            HvxLang::VShuff(a) => map!(get_cvec, a => {

                /* let mut bv_code = format!("(integer->bitvector ");
                bv_code.push_str(&a.to_string());
                bv_code.push_str(" (bitvector 128))");
                let rkt_code = (&format!(r#"'(bitvector->integer (bvmul {} (bv 2 128)))'"#, bv_code));
                let cmd = format!("/home/baronia3/bin/racket -I rosette -e {}", rkt_code);
                let output = run(&cmd);
                assert!(output.status.success());
                let mut so = get_stdout(&output).to_string();
                let len = so.len();
                so.truncate(len - 1);
                assert!(!so.is_empty());
                print!("{:?}", so);
                let ret = so.parse::<i32>().unwrap();
                print!("ret {:?}\n", ret); */
                let mut bv_code = format!("((integer->bitvector ");
                bv_code.push_str(&a.to_string());
                bv_code.push_str(" (bitvector 1024))");
                let rkt_code = (&format!(r#"'
                (require hydride/utils/bvops)
                (require hydride/utils/misc)
                (require hydride/ir/hvx/semantics)
                (for/list ([%i (range 0 8 1)]) 
                    (bitvector->integer (extract (* (+ %i 1) 127) (* %i 128) (hexagon_V6_vshuffh_128B {} 1024 16 0 16 8 16 8 0)))
                )'
                "#, bv_code));
                let cmd = format!("/home/baronia3/bin/racket -I rosette -e {}", rkt_code);
                let output = run(&cmd);
                //assert!(output.status.success());
                let mut so = get_stdout(&output).to_string();
                let len = so.len();
                let mut so = so.replace(&['(', ')', ',', '\"', '.', ';', ':', '\''][..], "");
                so.truncate(0);
                assert!(!so.is_empty());
                print!("cmd {:?}", so);
                let nums = so.trim().split(' ').flat_map(str::parse::<i128>).collect::<Vec<_>>();
                // let ret = so.parse::<i128>().unwrap();
                // print!("ret {:?}\n", ret);
                Some(HVXVec8_128::new_from_vec(nums))

            }),
            HvxLang::Lit(n) => vec![Some(n.clone()); cvec_len],
            HvxLang::Var(_) => vec![]
        }
    }

    fn initialize_vars(egraph: &mut EGraph<Self, SynthAnalysis>, vars: &[String]) {
        let mut consts = vec![];
        println!("vars vec {:?}", vars);

        for i in 0..2 {
            /* let i = HVXVec::from(i);
            consts.push(Some(HVXVec::MIN.wrapping_add(i)));
            consts.push(Some(HVXVec::MAX.wrapping_sub(i)));
            consts.push(Some(i));
            consts.push(Some(i.not())); */
            let i_1 = HVXVec8_128::from([i;8]);
            let i_2 = HVXVec8_128::from([i.not();8]);
            let i_3 = HVXVec8_128::from([i128::MIN + 1;8]);
            let i_4 = HVXVec8_128::from([i128::MAX - 1;8]);
            // consts.push(Some(HVXVec::MIN.wrapping_add(i)));
            // consts.push(Some(HVXVec::MAX.wrapping_sub(i)));
            consts.push(Some(i_1));
            consts.push(Some(i_2));
            consts.push(Some(i_3));
            consts.push(Some(i_4));
        }

        let cvecs = self_product(&consts, vars.len());

        egraph.analysis.cvec_len = cvecs[0].len();

        for (i, v) in vars.iter().enumerate() {
            let id = egraph.add(HvxLang::Var(Symbol::from(v.clone())));
            let cvec = cvecs[i].clone();
            egraph[id].data.cvec = cvec;
        }
    }

    fn to_var(&self) -> Option<Symbol> {
        if let HvxLang::Var(sym) = self {
            Some(*sym)
        } else {
            None
        }
    }

    fn mk_var(sym: Symbol) -> Self {
        HvxLang::Var(sym)
    }

    fn is_constant(&self) -> bool {
        matches!(self, HvxLang::Lit(_))
    }

    fn mk_constant(c: Self::Constant, _egraph: &mut EGraph<Self, SynthAnalysis>) -> Self {
        HvxLang::Lit(c)
    }


    fn validate(lhs: &Pattern<Self>, rhs: &Pattern<Self>) -> ValidationResult {
        let lexpr = egg_to_external_prog(Self::instantiate(lhs).as_ref());
        let rexpr = egg_to_external_prog(Self::instantiate(rhs).as_ref());
        println!("LEFT EXPRESSION");
        println!("{}",lexpr);
        println!("RIGHT EXPRESSION");
        println!("{}",rexpr);
        // ValidationResult::Invalid
        ValidationResult::Valid
    }
}

fn egg_to_external_prog<'a>(expr: &[HvxLang]) ->  String {
    let mut buf: Vec<String> = vec![];
    for node in expr.as_ref().iter() {
        match node {
            HvxLang::Lit(v0) => {
                //buf.push("(lits)".to_string())
                buf.push(format!("{}", v0))
            }
            HvxLang::Var(v0) => {
                //buf.push("(vars)".to_string())

                buf.push(format!("{}", v0))
            }
            HvxLang::VDeal(x) => {buf.push(format!("(vdeal {})", &buf[usize::from(*x)]))},
            HvxLang::VShuff(x) => {buf.push(format!("(vshuff {})", &buf[usize::from(*x)]))},
        }
    }
    buf.pop().unwrap()
}


#[cfg(test)]
#[path = "./recipes/vec.rs"]
mod vec;

mod test {
    use crate::vec::vec_rules;
    use crate::HvxLang;
    use std::time::{Duration, Instant};

    use ruler::{
        enumo::{Filter, Metric, Ruleset, Workload},
        logger,
        recipe_utils::{recursive_rules, run_workload, Lang},
        Limits,
    };

    #[test]
    fn run() {
        let start = Instant::now();
        // Runs the actual search
        let _all_rules = vec_rules();
        let duration = start.elapsed();


    }
}
