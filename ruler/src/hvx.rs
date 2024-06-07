use std;
use std::fmt;
use std::num::IntErrorKind;
use std::num::ParseIntError;
use std::ops::*;
use std::str;

use num::traits::ConstZero;
use rand::prelude::Distribution;
use rand::Rng;
use serde::Deserialize;
use serde::Serialize;

// General bitvector implementation
#[derive(Copy, Clone, Hash, PartialOrd, Ord, PartialEq, Eq, Serialize, Deserialize)]
#[serde(transparent)]
pub struct HVXVec<const N: Inner>(pub Inner);

type BV128 = HVXVec<128>;

#[derive(Copy, Clone, Hash, PartialOrd, Ord, PartialEq, Eq, Serialize, Deserialize)]
#[serde(transparent)]
pub struct HVXVec8_128([BV128; 8]);

type Inner = i128;
const INNER_N: Inner = (core::mem::size_of::<Inner>() * 8) as Inner;

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

    pub fn new_from_hvx_vec(bv128: BV128) -> Self {
        let mut array: [BV128; 8] = [bv128; 8];
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
    // is this for val or var?

    // workload.rs L58 says that e-graph construction will crash if terms are not parsable in the domain
    // this function faulty, but not sure if we need parsing for consts like (  1       1       1       1       1       1       1       1)
    // or vars like bv_val_0

    // current idea -> bv_val_0 should output a HVXVec8_128 of all 0s
    // bv_val_1 should output a HVXVec8_128 of all 1s, etc.
    // TODO: try printing FromStr for bv

    // conclusion: correct hypothesis, instantiate HVXVec8_128 from int32 consts
    // create map of strs

    // workload.rs L74 is where FromStr is used in parse()

    // enode is constant, var is variable for enumeration

    type Err = std::num::ParseIntError;
    // fn from_str(s: &str) -> Result<Self, Self::Err> {
    //     print!("Here is the string: {}\n", s);
    //     let num: i128 = s.parse().unwrap();
    //     print!("Here is the num {}", num);
    //     let mut s = s.replace(&['(', ')', ',', '\"', '.', ';', ':', '\''][..], "");
    //     let len = s.len();
    //     s.truncate(len - 1);
    //     Ok(HVXVec8_128::new_from_vec(
    //         s.trim()
    //             .split(' ')
    //             .flat_map(str::parse::<i128>)
    //             .collect::<Vec<_>>(),
    //     ))
    // }

    // type ParseErr = std::num::ParseIntError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        print!("Here is the string: {}\n", s);
        let res = s.parse::<Inner>().map(HVXVec::new);
        match res {
            Ok(i_128) => {
                // print!("Here is the I: {}", i_128);
                Ok(HVXVec8_128::new_from_hvx_vec(i_128))
                /* match i_128 {
                    0 => Ok(Self::new([0; 8])),
                    1 => Ok(Self::new([1; 8])),
                    _ => Ok(Self::new([2; 8])),
                } */
            }
            Err(e) => {
                // Ok(Self::new([2; 8]))
                Err(e)
            }
        }
        //s.parse::<Inner>().map(Self::new)
    }
}

impl From<[Inner; 8]> for HVXVec8_128 {
    fn from(arr: [Inner; 8]) -> Self {
        Self::new(arr)
    }
}

// Macro for specializing HVXVec to different sized bitvectors
#[macro_export]
macro_rules! impl_hvx {
    ($n:literal) => {
        use $crate::*;

        use rand::prelude::*;
        use rand_pcg::Pcg64;
        use serde::{Deserialize, Serialize};
        use std::fmt;
        use std::ops::*;

        // pub type HVXVec = $crate::HVXVec::<$n>;

        egg::define_language! {
          pub enum HvxLang {
                  "vdeal" = VDeal(Id),
                  "vshuff" = VShuff(Id),
                  Lit(HVXVec8_128),
                  // Lit(HVXVec),
                  Var(egg::Symbol),
              }
        }

        use std::io::BufReader;
        use std::io::BufRead;
        use std::process::Stdio;

        use cli_runner::{run, get_stdout, get_stderr};

        impl SynthLanguage for HvxLang {
            // type Constant = HVXVec;
            type Constant = HVXVec8_128;

            fn eval<'a, F>(&'a self, cvec_len: usize, mut get_cvec: F) -> CVec<Self>
            where
                F: FnMut(&'a Id) -> &'a CVec<Self>,
            {
                match self {
                    HvxLang::VDeal(a) => map!(get_cvec, a => {

                    print!("The value of a for VDeal is {}\n", a.to_string());
                    let mut nums_str = a.to_string();
                    // let len_nums = nums_str.len();
                    // nums_str.truncate(len_nums - 1);
                    let nums_init = nums_str.trim().split_whitespace().flat_map(str::parse::<i128>).collect::<Vec<_>>();
                    print!("nums_init vdeal {:?}\n\n", nums_init);

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

                    // instead of integer->bitvector, figure out a way to wrangle
                    // our textual bv representation into a rosette bit

                    let mut bv_code = format!("(concat ");
                    for i in nums_init {
                        bv_code.push_str("(integer->bitvector ");
                        bv_code.push_str(&i.to_string());
                        bv_code.push_str(" (bitvector 128)) ");
                    }

                    bv_code.push_str(")");


                    let rkt_code = (&format!(r#"'
                    (require hydride/utils/bvops)
                    (require hydride/utils/misc)
                    (require hydride/ir/hvx/semantics)
                    (for/list ([%i (range 0 8 1)]) 
                        (bitvector->integer (extract (* (+ %i 1) 127) (* %i 128) (hexagon_V6_vdealb_128B {} 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0)))
                    )'
                    "#, bv_code));
                    let cmd = format!("/home/baronia3/bin/racket -I rosette -e {}", rkt_code);
                    print!("cmd to run: {}\n", cmd);
                    let output = run(&cmd);
                    //assert!(output.status.success());
                    let mut so = get_stdout(&output).to_string();
                    let len = so.len();
                    let mut so = so.replace(&['(', ')', ',', '\"', '.', ';', ':', '\''][..], "");
                    so.truncate(len - 1);
                    assert!(!so.is_empty());
                    print!("{:?}  \n", so);
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


                        print!("The value of a for VShuff is {}\n", a.to_string());
                        let mut nums_str = a.to_string();
                        // let len_nums = nums_str.len();
                        // nums_str.truncate(len_nums - 1);
                        let nums_init = nums_str.trim().split_whitespace().flat_map(str::parse::<i128>).collect::<Vec<_>>();
                        print!("nums_init vshuff {:?}\n\n", nums_init);


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
                        let mut bv_code = format!("(concat ");
                        for i in nums_init {
                            bv_code.push_str("(integer->bitvector ");
                            bv_code.push_str(&i.to_string());
                            bv_code.push_str(" (bitvector 128)) ");
                        }

                        bv_code.push_str(")");

                        let rkt_code = (&format!(r#"'
                        (require hydride/utils/bvops)
                        (require hydride/utils/misc)
                        (require hydride/ir/hvx/semantics)
                        (for/list ([%i (range 0 8 1)]) 
                            (bitvector->integer (extract (* (+ %i 1) 127) (* %i 128) (hexagon_V6_vshuffh_128B {} 1024 16 0 16 8 16 8 0)))
                        )'
                        "#, bv_code));
                        let cmd = format!("/home/baronia3/bin/racket -I rosette -e {}", rkt_code);
                        print!("cmd to run: {}\n", cmd);
                        let output = run(&cmd);                        //assert!(output.status.success());
                        let mut so = get_stdout(&output).to_string();
                        let len = so.len();
                        let mut so = so.replace(&['(', ')', ',', '\"', '.', ';', ':', '\''][..], "");
                        so.truncate(len - 1);
                        assert!(!so.is_empty());
                        print!("{:?}", so);
                        let nums = so.trim().split(' ').flat_map(str::parse::<i128>).collect::<Vec<_>>();
                        // let ret = so.parse::<i128>().unwrap();
                        // print!("ret {:?}\n", ret);
                        Some(HVXVec8_128::new_from_vec(nums))

                    }),
                    HvxLang::Lit(n) => vec![Some(n.clone()); cvec_len],
                    HvxLang::Var(_) => vec![]
                }
            }

            fn mk_interval<'a, F>(&'a self, mut get_interval: F) -> Interval<Self::Constant>
            where
                F: FnMut(&'a Id) -> &'a Interval<Self::Constant>,
            {
                match self {
                    HvxLang::Lit(c) => Interval::new(Some(*c), Some(*c)),
                    // Todo- proper interval analysis. For now it's just constant folding
                    _ => Interval::default()
                }
            }

            fn to_var(&self) -> Option<Symbol> {
                if let HvxLang::Var(sym) = self {
                    println!("to_var {:?}", *sym);
                    Some(*sym)
                } else {
                    None
                }
            }

            fn mk_var(sym: Symbol) -> Self {
                println!("mk_var {:?}", sym);
                HvxLang::Var(sym)
            }

            fn is_constant(&self) -> bool {
                matches!(self, HvxLang::Lit(_))
            }

            fn mk_constant(c: Self::Constant, _egraph: &mut EGraph<Self, SynthAnalysis>) -> Self {
                HvxLang::Lit(c)
            }

            fn initialize_vars(egraph: &mut EGraph<Self, SynthAnalysis>, vars: &[String]) {
                //   let mut consts: Vec<Option<HVXVec>> = (0..1u64 << $n).map(|i| Some((i as u32).into())).collect();
                println!("vars vec {:?}", vars);
                let mut consts = vec![];

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

                for i in &consts {
                    print!("elem in constvec {:?}\n\n", i);
                }

                consts.sort();
                consts.dedup();

                let mut cvecs = self_product(&consts, vars.len());
                // let mut cvecs = &consts;

                print!("cvecs {:?}\n", cvecs);
                print!("vars len {:?}\n", vars.len());


                egraph.analysis.cvec_len = cvecs[0].len();

                for (i, v) in vars.iter().enumerate() {
                    print!("i in vars {}\n", i);
                    let id = egraph.add(HvxLang::Var(Symbol::from(v.clone())));
                    egraph[id].data.cvec = cvecs[i].clone();
                    print!("elem in egraph {:?}\n\n", &egraph[id].data.cvec);
                }
            }

            fn validate(
                lhs: &Pattern<Self>,
                rhs: &Pattern<Self>,
            ) -> ValidationResult {

                // TODO: Add calls to Rosette

                print!("lhs expr {}\n", lhs);
                print!("rhs expr {}\n", rhs);

                /* use z3::{*, ast::Ast};

                fn egg_to_z3<'a>(ctx: &'a z3::Context, expr: &[HvxLang]) -> z3::ast::HVXVec<'a> {
                    let mut buf: Vec<z3::ast::HVXVec> = vec![];
                    for node in expr.as_ref().iter() {
                        match node {
                            HvxLang::Var(v) => buf.push(z3::ast::HVXVec::new_const(&ctx, v.to_string(), $n)),
                            HvxLang::Lit(c) => buf.push(z3::ast::HVXVec::from_u64(&ctx, c.0 as u64, $n)),
                            HvxLang::VDeal(a) => buf.push(buf[usize::from(*a)].bvadd(&buf[usize::from(*a)])),
                            HvxLang::VShuff(a) => buf.push(buf[usize::from(*a)].bvsub(&buf[usize::from(*a)])),
                        }
                    }
                    buf.pop().unwrap()
                }

                let mut cfg = z3::Config::new();
                cfg.set_timeout_msec(1000);
                let ctx = z3::Context::new(&cfg);
                let solver = z3::Solver::new(&ctx);
                let lexpr = egg_to_z3(&ctx, Self::instantiate(lhs).as_ref());
                let rexpr = egg_to_z3(&ctx, Self::instantiate(rhs).as_ref());
                solver.assert(&lexpr._eq(&rexpr).not());
                match solver.check() {
                    SatResult::Sat => ValidationResult::Invalid,
                    SatResult::Unsat => ValidationResult::Valid,
                    SatResult::Unknown => ValidationResult::Unknown
                } */
                ValidationResult::Valid
            }
        }
    };
}

#[cfg(test)]
pub mod tests {
    use super::*;
    type BV1024 = HVXVec<4>;

    #[test]
    fn test_bv() {
        // assert_eq!(BV1024::ALL_ONES.0, 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF);
        // assert_eq!(BV1024::MAX.0, 0b0111);
        // assert_eq!(BV1024::MIN.0, 0b1000);
        // print!("BV1024 All Ones #x{:?}\n", BV1024::ALL_ONES.0);
        let one = BV1024::from(1);

        // assert_eq!(BV1024::MAX.wrapping_add(one), HVXVec::MIN);
        // assert_eq!(BV1024::NEG_ONE.wrapping_neg(), one);
        // assert_eq!(BV1024::MIN.wrapping_mul(HVXVec::NEG_ONE), HVXVec::MIN);
        // assert_eq!(BV1024::MIN.wrapping_neg(), HVXVec::MIN);
    }
}
