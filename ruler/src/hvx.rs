use std;
use std::fmt;
use std::ops::*;
use std::str;

use rand::prelude::Distribution;
use rand::Rng;
use rayon::vec;
use serde::Deserialize;
use serde::Serialize;

// General bitvector implementation
#[derive(Copy, Clone, Hash, PartialOrd, Ord, PartialEq, Eq, Serialize, Deserialize)]
#[serde(transparent)]
pub struct HVXVec<const N: Inner>(pub Inner);

type BV128 = HVXVec<128>;
pub struct HVXVec8_128([BV128; 8]);

type Inner = u128;
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
    pub const ALL_ONES: Self = Self([BV128::ALL_ONES;8]);
    pub const NEG_ONE: Self = Self::ALL_ONES;
    // pub const MIN: Self = Self(vec![HVXVec::from(1 << (N - 1)); 8]);
    // pub const MAX: Self = Self(vec![HVXVec::from(HVXVec::ALL_ONES.0 >> 1); 8]);

    pub fn new(n: impl Into<Inner>) -> Self {
        Self([BV128::from(n.into());8])
    }
}

/* impl<const N: Inner> Not for HVXVec8_128<N> {
    type Output = Self;

    fn not(self) -> Self::Output {
        Self::new(self.0.not())
    }
}

impl<const N: Inner> BitAnd for HVXVec8_128<N> {
    type Output = Self;

    fn bitand(self, rhs: Self) -> Self::Output {
        Self::new(self.0.bitand(rhs.0))
    }
}

impl<const N: Inner> BitOr for HVXVec8_128<N> {
    type Output = Self;

    fn bitor(self, rhs: Self) -> Self::Output {
        Self::new(self.0.bitor(rhs.0))
    }
}

impl<const N: Inner> BitXor for HVXVec8_128<N> {
    type Output = Self;

    fn bitxor(self, rhs: Self) -> Self::Output {
        Self::new(self.0.bitxor(rhs.0))
    }
} */

/* impl<const N: Inner> fmt::Debug for HVXVec8_128<N> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        fmt::Display::fmt(&self.0, f)
    }
}

impl<const N: Inner> fmt::Display for HVXVec8_128<N> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        fmt::Display::fmt(&self.0, f)
    }
}

impl<const N: Inner> fmt::Binary for HVXVec8_128<N> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        fmt::Binary::fmt(&self.0, f)
    }
}

impl<const N: Inner> fmt::LowerHex for HVXVec8_128<N> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        fmt::LowerHex::fmt(&self.0, f)
    }
}

impl<const N: Inner> Distribution<HVXVec8_128<N>> for rand::distributions::Standard {
    fn sample<R: Rng + ?Sized>(&self, rng: &mut R) -> HVXVec8_128<N> {
        let inner: Inner = rng.gen();
        inner.into()
    }
}

impl<const N: Inner> std::str::FromStr for HVXVec8_128<N> {
    type Err = std::num::ParseIntError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        if let Some(stripped) = s.strip_prefix("#b") {
            let i = Inner::from_str_radix(stripped, 2).unwrap();
            return Ok(Self::new(i));
        }
        s.parse::<Inner>().map(Self::new)
    }
} */

impl From<Inner> for HVXVec8_128 {
    fn from(v: Inner) -> Self {
        Self::new(v)
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

        pub type HVXVec = $crate::HVXVec::<$n>;

        egg::define_language! {
          pub enum HvxLang {
                  "vdeal" = VDeal(Id),
                  "vshuff" = VShuff(Id),
                  Lit(HVXVec),
                  Var(egg::Symbol),
              }
        }

        use std::io::BufReader;
        use std::io::BufRead;
        use std::process::Stdio;

        use cli_runner::{run, get_stdout, get_stderr};

        impl SynthLanguage for HvxLang {
            type Constant = HVXVec;

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
                    let rkt_code = (&format!(r#"'
                    (require hydride/utils/bvops)
                    (require hydride/utils/misc)
                    (require hydride/ir/hvx/semantics)
                    (bitvector->integer (hexagon_V6_vdealb_128B {} 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0))'"#, bv_code));
                    let cmd = format!("/home/baronia3/bin/racket -I rosette -e {}", rkt_code);
                    print!("cmd to run: {}\n", cmd);
                    let output = run(&cmd);
                    //assert!(output.status.success());
                    let mut so = get_stdout(&output).to_string();
                    let len = so.len();
                    so.truncate(len - 1);
                    assert!(!so.is_empty());
                    // print!("{:?}  \n", so);
                    let ret = so.parse::<i128>().unwrap();
                    print!("ret {:?}\n\n\n", ret);
                    Some(HVXVec::from(ret as u128))
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
                        (bitvector->integer (hexagon_V6_vshuffh_128B {} 1024 16 0 16 8 16 8 0))'"#, bv_code));
                        let cmd = format!("/home/baronia3/bin/racket -I rosette -e {}", rkt_code);
                        let output = run(&cmd);
                        //assert!(output.status.success());
                        let mut so = get_stdout(&output).to_string();
                        let len = so.len();
                        so.truncate(len - 1);
                        assert!(!so.is_empty());
                        print!("{:?}", so);
                        let ret = so.parse::<i128>().unwrap();
                        print!("ret {:?}\n", ret);
                        Some(HVXVec::from(ret as u128))

                    }),
                    HvxLang::Lit(n) => vec![Some(n.clone()); cvec_len],
                    HvxLang::Var(_) => vec![],
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

            fn initialize_vars(egraph: &mut EGraph<Self, SynthAnalysis>, vars: &[String]) {
                //   let mut consts: Vec<Option<HVXVec>> = (0..1u64 << $n).map(|i| Some((i as u32).into())).collect();
                let mut consts = vec![];

                for i in 0..2 {
                    let i = HVXVec::from(i);
                    consts.push(Some(HVXVec::MIN.wrapping_add(i)));
                    consts.push(Some(HVXVec::MAX.wrapping_sub(i)));
                    consts.push(Some(i));
                    consts.push(Some(i.not()));
                }
                consts.sort();
                consts.dedup();

                let mut cvecs = self_product(&consts, vars.len());

                egraph.analysis.cvec_len = cvecs[0].len();

                for (i, v) in vars.iter().enumerate() {
                    let id = egraph.add(HvxLang::Var(Symbol::from(v.clone())));
                    egraph[id].data.cvec = cvecs[i].clone()
                }
            }

            fn validate(
                lhs: &Pattern<Self>,
                rhs: &Pattern<Self>,
            ) -> ValidationResult {
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
