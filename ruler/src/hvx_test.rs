#[feature(core_intrinsics)]
use std::fmt;
use std::ops::*;

use rand::prelude::Distribution;
use rand::Rng;
use serde::Deserialize;
use serde::Serialize;

// General bitvector implementation
#[derive(Copy, Clone, Hash, PartialOrd, Ord, PartialEq, Eq, Serialize, Deserialize)]
#[serde(transparent)]
pub struct BV<const N: Inner>(pub Inner);

type Inner = u128;
const INNER_N: Inner = (core::mem::size_of::<Inner>() * 8) as Inner;

pub struct HVXVec<const N: Inner>(Vec<BV<N>>);
type BV16 = BV<16>;
pub struct HVXVec16x16(Vec<BV16>);

// pub type HVXVec<const N : u32> = Vec<BV<N>>;

impl<const N: Inner> BV<N> {
    pub const ZERO: Self = Self(0);
    pub const ALL_ONES: Self = Self((!(0)) >> (1024 - N));
    pub const NEG_ONE: Self = Self::ALL_ONES;
    pub const MIN: Self = Self(1 << (N - 1));
    pub const MAX: Self = Self(Self::ALL_ONES.0 >> 1);

    pub fn new(n: impl Into<Inner>) -> Self {
        print!("New BV of length {}: {:b}\n", &N, Self::ALL_ONES.0);
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

impl<const N: Inner> Not for BV<N> {
    type Output = Self;

    fn not(self) -> Self::Output {
        Self::new(self.0.not())
    }
}

impl<const N: Inner> BitAnd for BV<N> {
    type Output = Self;

    fn bitand(self, rhs: Self) -> Self::Output {
        Self::new(self.0.bitand(rhs.0))
    }
}

impl<const N: Inner> BitOr for BV<N> {
    type Output = Self;

    fn bitor(self, rhs: Self) -> Self::Output {
        Self::new(self.0.bitor(rhs.0))
    }
}

impl<const N: Inner> BitXor for BV<N> {
    type Output = Self;

    fn bitxor(self, rhs: Self) -> Self::Output {
        Self::new(self.0.bitxor(rhs.0))
    }
}

impl<const N: Inner> fmt::Debug for BV<N> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        fmt::Display::fmt(&self.0, f)
    }
}

impl<const N: Inner> fmt::Display for BV<N> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        fmt::Display::fmt(&self.0, f)
    }
}

impl<const N: Inner> fmt::Binary for BV<N> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        fmt::Binary::fmt(&self.0, f)
    }
}

impl<const N: Inner> Distribution<BV<N>> for rand::distributions::Standard {
    fn sample<R: Rng + ?Sized>(&self, rng: &mut R) -> BV<N> {
        let inner: Inner = rng.gen();
        inner.into()
    }
}

impl<const N: Inner> std::str::FromStr for BV<N> {
    type Err = std::num::ParseIntError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        if let Some(stripped) = s.strip_prefix("#b") {
            let i = Inner::from_str_radix(stripped, 2).unwrap();
            return Ok(Self::new(i));
        }
        s.parse::<Inner>().map(Self::new)
    }
}

impl<const N: Inner> From<Inner> for BV<N> {
    fn from(v: Inner) -> Self {
        Self::new(v)
    }
}

impl HVXVec16x16 {
    // pub const NEG_ONE: Self = Self::ALL_ONES;
    // pub const MIN: Self = Self(1 << (N - 1));
    // pub const MAX: Self = Self(Self::ALL_ONES.0 >> 1);

    pub fn new(n: impl Into<Inner>) -> Self {
        Self(vec![BV16::new(n); 16])
    }

    pub fn wrapping_add(self, rhs: Self) -> Self {
        let mut res = HVXVec16x16::new(16 as u128);
        for i in 0..16 {
            res.0[i] = self.0[i].wrapping_add(rhs.0[i]);
        }
        res
    }

    pub fn wrapping_sub(self, rhs: Self) -> Self {
        let mut res = HVXVec16x16::new(16 as u128);
        for i in 0..16 {
            res.0[i] = self.0[i].wrapping_sub(rhs.0[i]);
        }
        res
    }

    pub fn wrapping_mul(self, rhs: Self) -> Self {
        let mut res = HVXVec16x16::new(16 as u128);
        for i in 0..16 {
            res.0[i] = self.0[i].wrapping_mul(rhs.0[i]);
        }
        res
    }

    pub fn wrapping_neg(self) -> Self {
        let mut res = HVXVec16x16::new(16 as u128);
        for i in 0..16 {
            res.0[i] = self.0[i].wrapping_neg();
        }
        res
    }

    pub fn my_shl(self, rhs: Self) -> Self {
        let mut res = HVXVec16x16::new(16 as u128);
        for i in 0..16 {
            res.0[i] = self.0[i].my_shl(rhs.0[i]);
        }
        res
    }

    pub fn my_shr(self, rhs: Self) -> Self {
        let mut res = HVXVec16x16::new(16 as u128);
        for i in 0..16 {
            res.0[i] = self.0[i].my_shr(rhs.0[i]);
        }
        res
    }
}

impl Not for HVXVec16x16 {
    type Output = Self;

    fn not(self) -> Self::Output {
        let mut res = HVXVec16x16::new(16 as u128);
        for i in 0..16 {
            res.0[i] = self.0[i].not();
        }
        res
    }
}

impl BitAnd for HVXVec16x16 {
    type Output = Self;

    fn bitand(self, rhs: Self) -> Self::Output {
        let mut res = HVXVec16x16::new(16 as u128);
        for i in 0..16 {
            res.0[i] = self.0[i].bitand(rhs.0[i]);
        }
        res
    }
}

impl BitOr for HVXVec16x16 {
    type Output = Self;

    fn bitor(self, rhs: Self) -> Self::Output {
        let mut res = HVXVec16x16::new(16 as u128);
        for i in 0..16 {
            res.0[i] = self.0[i].bitor(rhs.0[i]);
        }
        res
    }
}

impl BitXor for HVXVec16x16 {
    type Output = Self;

    fn bitxor(self, rhs: Self) -> Self::Output {
        let mut res = HVXVec16x16::new(16 as u128);
        for i in 0..16 {
            res.0[i] = self.0[i].bitxor(rhs.0[i]);
        }
        res
    }
}

impl From<Inner> for HVXVec16x16 {
    fn from(v: Inner) -> Self {
        Self::new(v)
    }
}

// Macro for specializing BV to different sized bitvectors
#[macro_export]
macro_rules! impl_bv {
    ($n:literal) => {
        use $crate::*;

        use rand::prelude::*;
        use rand_pcg::Pcg64;
        use serde::{Deserialize, Serialize};
        use std::fmt;
        use std::ops::*;

        pub type BV = $crate::BV::<$n>;

        egg::define_language! {
          pub enum Bv {
                  "+" = Add([Id; 2]),
                  "--" = Sub([Id; 2]),
                  "*" = Mul([Id; 2]),
                  "-" = Neg(Id),
                  "~" = Not(Id),
                  "<<" = Shl([Id; 2]),
                  ">>" = Shr([Id; 2]),
                  "&" = And([Id; 2]),
                  "|" = Or([Id; 2]),
                  "^" = Xor([Id; 2]),
                  Lit(BV),
                  Var(egg::Symbol),
              }
        }

        impl SynthLanguage for Bv {
            type Constant = BV;

            fn eval<'a, F>(&'a self, cvec_len: usize, mut get_cvec: F) -> CVec<Self>
            where
                F: FnMut(&'a Id) -> &'a CVec<Self>,
            {
                match self {
                    Bv::Neg(a) => map!(get_cvec, a => {Some(a.wrapping_neg())}),
                    Bv::Not(a) => map!(get_cvec, a => {print!("BVNot a: {:016b}\n", a); Some(a.not())}),

                    Bv::Add([a, b]) => map!(get_cvec, a, b => Some(a.wrapping_add(*b))),
                    Bv::Sub([a, b]) => map!(get_cvec, a, b => Some(a.wrapping_sub(*b))),
                    Bv::Mul([a, b]) => map!(get_cvec, a, b => Some(a.wrapping_mul(*b))),

                    Bv::Shl([a, b]) => map!(get_cvec, a, b => Some(a.my_shl(*b))),
                    Bv::Shr([a, b]) => map!(get_cvec, a, b => Some(a.my_shr(*b))),

                    Bv::And([a, b]) => map!(get_cvec, a, b => Some(*a & *b)),
                    Bv::Or([a, b]) => map!(get_cvec, a, b => Some(*a | *b)),
                    Bv::Xor([a, b]) => map!(get_cvec, a, b => Some(*a ^ *b)),

                    Bv::Lit(n) => vec![Some(n.clone()); cvec_len],
                    Bv::Var(_) => vec![],
                }
            }

            fn mk_interval<'a, F>(&'a self, mut get_interval: F) -> Interval<Self::Constant>
            where
                F: FnMut(&'a Id) -> &'a Interval<Self::Constant>,
            {
                match self {
                    Bv::Lit(c) => Interval::new(Some(*c), Some(*c)),
                    // Todo- proper interval analysis. For now it's just constant folding
                    _ => Interval::default()
                }
            }

            fn to_var(&self) -> Option<Symbol> {
                if let Bv::Var(sym) = self {
                    Some(*sym)
                } else {
                    None
                }
            }

            fn mk_var(sym: Symbol) -> Self {
                Bv::Var(sym)
            }

            fn is_constant(&self) -> bool {
                matches!(self, Bv::Lit(_))
            }

            fn mk_constant(c: Self::Constant, _egraph: &mut EGraph<Self, SynthAnalysis>) -> Self {
                Bv::Lit(c)
            }

            fn initialize_vars(egraph: &mut EGraph<Self, SynthAnalysis>, vars: &[String]) {
                //   let mut consts: Vec<Option<BV>> = (0..1u64 << $n).map(|i| Some((i as u32).into())).collect();
                let mut consts = vec![];

                for i in 0..2 {
                    let i = BV::from(i);
                    consts.push(Some(BV::MIN.wrapping_add(i)));
                    consts.push(Some(BV::MAX.wrapping_sub(i)));
                    consts.push(Some(i));
                    consts.push(Some(i.wrapping_neg()));
                }
                consts.sort();
                consts.dedup();

                let mut cvecs = self_product(&consts, vars.len());

                egraph.analysis.cvec_len = cvecs[0].len();

                for (i, v) in vars.iter().enumerate() {
                    let id = egraph.add(Bv::Var(Symbol::from(v.clone())));
                    egraph[id].data.cvec = cvecs[i].clone()
                }
            }

            fn validate(
                lhs: &Pattern<Self>,
                rhs: &Pattern<Self>,
            ) -> ValidationResult {
                use z3::{*, ast::Ast};

                fn egg_to_z3<'a>(ctx: &'a z3::Context, expr: &[Bv]) -> z3::ast::BV<'a> {
                    let mut buf: Vec<z3::ast::BV> = vec![];
                    for node in expr.as_ref().iter() {
                        match node {
                            Bv::Var(v) => buf.push(z3::ast::BV::new_const(&ctx, v.to_string(), $n)),
                            Bv::Lit(c) => buf.push(z3::ast::BV::from_u64(&ctx, c.0 as u64, $n)),
                            Bv::Add([a, b]) => buf.push(buf[usize::from(*a)].bvadd(&buf[usize::from(*b)])),
                            Bv::Sub([a, b]) => buf.push(buf[usize::from(*a)].bvsub(&buf[usize::from(*b)])),
                            Bv::Mul([a, b]) => buf.push(buf[usize::from(*a)].bvmul(&buf[usize::from(*b)])),
                            Bv::Shl([a, b]) => buf.push(buf[usize::from(*a)].bvshl(&buf[usize::from(*b)])),
                            Bv::Shr([a, b]) => buf.push(buf[usize::from(*a)].bvlshr(&buf[usize::from(*b)])),
                            Bv::And([a, b]) => buf.push(buf[usize::from(*a)].bvand(&buf[usize::from(*b)])),
                            Bv::Or([a, b]) => buf.push(buf[usize::from(*a)].bvor(&buf[usize::from(*b)])),
                            Bv::Xor([a, b]) => buf.push(buf[usize::from(*a)].bvxor(&buf[usize::from(*b)])),
                            Bv::Not(a) => buf.push(buf[usize::from(*a)].bvnot()),
                            Bv::Neg(a) => buf.push(buf[usize::from(*a)].bvneg()),
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
                }
            }
        }
    };
}

#[macro_export]
macro_rules! impl_hvx_vec {
    ($n:literal) => {
        use $crate::*;

        use rand::prelude::*;
        use rand_pcg::Pcg64;
        use serde::{Deserialize, Serialize};
        use std::fmt;
        use std::ops::*;

        pub type BV = $crate::BV::<$n>;

        egg::define_language! {
          pub enum HVXLang {
                  "+" = Add([Id; 2]),
                  "--" = Sub([Id; 2]),
                  "*" = Mul([Id; 2]),
                  "-" = Neg(Id),
                  "~" = Not(Id),
                  "vdeal" = VDeal(Id),
                  "vshuff" = VShuff(Id),
                  "<<" = Shl([Id; 2]),
                  ">>" = Shr([Id; 2]),
                  "&" = And([Id; 2]),
                  "|" = Or([Id; 2]),
                  "^" = Xor([Id; 2]),
                  LitVec(HVXVec16x16),
                  Var(egg::Symbol),
              }
        }

        impl SynthLanguage for HVXLang {
            type Constant = BV;

            fn eval<'a, F>(&'a self, cvec_len: usize, mut get_cvec: F) -> CVec<Self>
            where
                F: FnMut(&'a Id) -> &'a CVec<Self>,
            {
                match self {
                    HVXLang::Neg(a) => map!(get_cvec, a => Some(a.wrapping_neg())),
                    HVXLang::Not(a) => map!(get_cvec, a => Some(a.not())),
                    HVXLang::VDeal(a) => map!(get_cvec, a => {
                        let mut res = HVXVec16x16::new(16 as u128);
                        for i in 0..16 {
                            let mut high = BV16::from(0);
                            high = (*a[i].my_shr(BV<16>::from(8))) & BV<16>::from(255);
                            let mut low = BV16::from(0);
                            low = *a[i] & BV<16>::from(255);
                            res.0[i] = high & low;
                        }
                        Some(res)}
                    )
                    HVXLang::Add([a, b]) => map!(get_cvec, a, b => Some(a.wrapping_add(*b))),
                    HVXLang::Sub([a, b]) => map!(get_cvec, a, b => Some(a.wrapping_sub(*b))),
                    HVXLang::Mul([a, b]) => map!(get_cvec, a, b => Some(a.wrapping_mul(*b))),

                    HVXLang::Shl([a, b]) => map!(get_cvec, a, b => Some(a.my_shl(*b))),
                    HVXLang::Shr([a, b]) => map!(get_cvec, a, b => Some(a.my_shr(*b))),

                    HVXLang::And([a, b]) => map!(get_cvec, a, b => Some(*a & *b)),
                    HVXLang::Or([a, b]) => map!(get_cvec, a, b => Some(*a | *b)),
                    HVXLang::Xor([a, b]) => map!(get_cvec, a, b => Some(*a ^ *b)),

                    HVXLang::Lit(n) => Some(n.clone()),
                    HVXLang::Var(_) => vec![],
                }
            }

            fn mk_interval<'a, F>(&'a self, mut get_interval: F) -> Interval<Self::Constant>
            where
                F: FnMut(&'a Id) -> &'a Interval<Self::Constant>,
            {
                match self {
                    Bv::Lit(c) => Interval::new(Some(*c), Some(*c)),
                    // Todo- proper interval analysis. For now it's just constant folding
                    _ => Interval::default()
                }
            }

            fn to_var(&self) -> Option<Symbol> {
                if let Bv::Var(sym) = self {
                    Some(*sym)
                } else {
                    None
                }
            }

            fn mk_var(sym: Symbol) -> Self {
                Bv::Var(sym)
            }

            fn is_constant(&self) -> bool {
                matches!(self, Bv::Lit(_))
            }

            fn mk_constant(c: Self::Constant, _egraph: &mut EGraph<Self, SynthAnalysis>) -> Self {
                Bv::Lit(c)
            }

            fn initialize_vars(egraph: &mut EGraph<Self, SynthAnalysis>, vars: &[String]) {
                //   let mut consts: Vec<Option<BV>> = (0..1u64 << $n).map(|i| Some((i as u32).into())).collect();
                let mut consts = vec![];

                for i in 0..2 {
                    let i = BV::from(i);
                    consts.push(Some(BV::MIN.wrapping_add(i)));
                    consts.push(Some(BV::MAX.wrapping_sub(i)));
                    consts.push(Some(i));
                    consts.push(Some(i.wrapping_neg()));
                }
                consts.sort();
                consts.dedup();

                let mut cvecs = self_product(&consts, vars.len());

                egraph.analysis.cvec_len = cvecs[0].len();

                for (i, v) in vars.iter().enumerate() {
                    let id = egraph.add(Bv::Var(Symbol::from(v.clone())));
                    egraph[id].data.cvec = cvecs[i].clone()
                }
            }

            fn validate(
                lhs: &Pattern<Self>,
                rhs: &Pattern<Self>,
            ) -> ValidationResult {
                use z3::{*, ast::Ast};

                fn egg_to_z3<'a>(ctx: &'a z3::Context, expr: &[Bv]) -> z3::ast::BV<'a> {
                    let mut buf: Vec<z3::ast::BV> = vec![];
                    for node in expr.as_ref().iter() {
                        match node {
                            Bv::Var(v) => buf.push(z3::ast::BV::new_const(&ctx, v.to_string(), $n)),
                            Bv::Lit(c) => buf.push(z3::ast::BV::from_u64(&ctx, c.0 as u64, $n)),
                            Bv::Add([a, b]) => buf.push(buf[usize::from(*a)].bvadd(&buf[usize::from(*b)])),
                            Bv::Sub([a, b]) => buf.push(buf[usize::from(*a)].bvsub(&buf[usize::from(*b)])),
                            Bv::Mul([a, b]) => buf.push(buf[usize::from(*a)].bvmul(&buf[usize::from(*b)])),
                            Bv::Shl([a, b]) => buf.push(buf[usize::from(*a)].bvshl(&buf[usize::from(*b)])),
                            Bv::Shr([a, b]) => buf.push(buf[usize::from(*a)].bvlshr(&buf[usize::from(*b)])),
                            Bv::And([a, b]) => buf.push(buf[usize::from(*a)].bvand(&buf[usize::from(*b)])),
                            Bv::Or([a, b]) => buf.push(buf[usize::from(*a)].bvor(&buf[usize::from(*b)])),
                            Bv::Xor([a, b]) => buf.push(buf[usize::from(*a)].bvxor(&buf[usize::from(*b)])),
                            Bv::Not(a) => buf.push(buf[usize::from(*a)].bvnot()),
                            Bv::Neg(a) => buf.push(buf[usize::from(*a)].bvneg()),
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
                }
            }
        }
    };
}

#[cfg(test)]
pub mod tests {
    use super::*;
    type BV4 = BV<4>;

    #[test]
    fn test_bv() {
        assert_eq!(BV4::ALL_ONES.0, 0b1111);
        assert_eq!(BV4::MAX.0, 0b0111);
        assert_eq!(BV4::MIN.0, 0b1000);

        let one = BV4::from(1);

        assert_eq!(BV4::MAX.wrapping_add(one), BV::MIN);
        assert_eq!(BV4::NEG_ONE.wrapping_neg(), one);
        assert_eq!(BV4::MIN.wrapping_mul(BV::NEG_ONE), BV::MIN);
        assert_eq!(BV4::MIN.wrapping_neg(), BV::MIN);
    }
}

fn initialize<T>(count: usize, f: fn(usize) -> T) -> Vec<T> {
    (1..count).map(f).collect()
}

fn main() {
    type BV16 = BV<16>;
    type BV32 = BV<32>;
    type BV4 = BV<4>;
    assert_eq!(BV4::ALL_ONES.0, 0b1111);
    // let _hvxvec16 : HVXVec<16> = vec![BV16::from(0); 16];
    // let HVXVec32 = vec![BV32::from(0); 32];
    let my_vector = HVXVec16x16::from(4);
    let my_vector2 = HVXVec16x16::from(7);
    let mut res = my_vector.wrapping_add(my_vector2);
    for e in &res.0 {
        println!("{:b}", e);
    }
    res = res.not();
    for e in &res.0 {
        println!("{:b}", e);
    }
    let bv1 = BV16::from(4);
    let bv2 = BV16::from(7);
    print!("BVmul res {:?}", &bv1.wrapping_mul(bv2));
}
