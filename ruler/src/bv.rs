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

impl<const N: Inner> BV<N> {
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
                  "vdeal" = VDeal(Id),
                  "vshuff" = VShuff(Id),
                  "<<" = Shl([Id; 2]),
                  ">>" = Shr([Id; 2]),
                  "&" = And([Id; 2]),
                  "|" = Or([Id; 2]),
                  "^" = Xor([Id; 2]),
                  Lit(BV),
                  Var(egg::Symbol),
              }
        }

        use cli_runner::{run, get_stdout, get_stderr};

        impl SynthLanguage for Bv {
            type Constant = BV;

            fn eval<'a, F>(&'a self, cvec_len: usize, mut get_cvec: F) -> CVec<Self>
            where
                F: FnMut(&'a Id) -> &'a CVec<Self>,
            {
                match self {
                    Bv::Neg(a) => map!(get_cvec, a => Some(a.wrapping_neg())),
                    Bv::Not(a) => map!(get_cvec, a => Some(a.not())),

                    Bv::Add([a, b]) => map!(get_cvec, a, b => Some(a.wrapping_add(*b))),
                    Bv::Sub([a, b]) => map!(get_cvec, a, b => Some(a.wrapping_sub(*b))),
                    Bv::Mul([a, b]) => map!(get_cvec, a, b => Some(a.wrapping_mul(*b))),

                    Bv::Shl([a, b]) => map!(get_cvec, a, b => Some(a.my_shl(*b))),
                    Bv::Shr([a, b]) => map!(get_cvec, a, b => Some(a.my_shr(*b))),

                    Bv::And([a, b]) => map!(get_cvec, a, b => Some(*a & *b)),
                    Bv::Or([a, b]) => map!(get_cvec, a, b => Some(*a | *b)),
                    Bv::Xor([a, b]) => map!(get_cvec, a, b => Some(*a ^ *b)),
                    Bv::VDeal(a) => map!(get_cvec, a => {
                        /* let mut bv_code = format!("(integer->bitvector ");
                        bv_code.push_str(&a.to_string());
                        bv_code.push_str(&format!(" (bitvector {}))", $n));
                        let rkt_code = (&format!(r#"'
                        (require hydride/utils/bvops)
                        (require hydride/utils/misc)
                        (require hydride/ir/hvx/semantics)
                        (bitvector->integer (bvadd {} {}))'"#, bv_code, bv_code));
                        // let cmd = format!("/home/baronia3/bin/racket -I rosette -e {}", rkt_code);
                        let cmd = format!(r#"/home/baronia3/bin/racket -e '(+ {} {})'"#, a, a);
                        print!("cmd to run: {}\n", cmd);
                        let output = run(&cmd);
                        //assert!(output.status.success());
                        let mut so = get_stdout(&output).to_string();
                        let len = so.len();
                        so.truncate(len - 1);
                        assert!(!so.is_empty());
                        // print!("{:?}  \n", so);
                        let ret = so.parse::<i128>().unwrap();
                        print!("ret {:?}\n\n\n", ret); */
                        let tets_ret = a.0 as u128;
                        Some(BV::from(tets_ret + tets_ret))
                        }),
                        Bv::VShuff(a) => map!(get_cvec, a => {
                            /* let mut bv_code = format!("((integer->bitvector ");
                            bv_code.push_str(&a.to_string());
                            bv_code.push_str(&format!(" (bitvector {}))", $n));
                            let rkt_code = (&format!(r#"'
                            (require hydride/utils/bvops)
                            (require hydride/utils/misc)
                            (require hydride/ir/hvx/semantics)
                            (bitvector->integer (bvmul {} (bitvector 2 {})))'"#, bv_code, $n));
                            let cmd = format!("/home/baronia3/bin/racket -I rosette -e {}", rkt_code);
                            let output = run(&cmd);
                            //assert!(output.status.success());
                            let mut so = get_stdout(&output).to_string();
                            let len = so.len();
                            so.truncate(len - 1);
                            assert!(!so.is_empty());
                            print!("{:?}", so);
                            let ret = so.parse::<i128>().unwrap();
                            print!("ret {:?}\n", ret); */
                            let tets_ret = a.0 as u128;
                            Some(BV::from(tets_ret * 2))

                        }),
                    /* Bv::VDeal(a) => map!(get_cvec, a => {
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
                        Some(BV::from(ret as u128))
                        }),
                        Bv::VShuff(a) => map!(get_cvec, a => {
                            let mut bv_code = format!("((integer->bitvector ");
                            bv_code.push_str(&a.to_string());
                            bv_code.push_str(" (bitvector 128))");
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
                            Some(BV::from(ret as u128))

                        }), */

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
                            Bv::VDeal(a) => buf.push(buf[usize::from(*a)].bvadd(&buf[usize::from(*a)])),
                            Bv::VShuff(a) => buf.push(buf[usize::from(*a)].bvmul(&buf[usize::from(*a)])),
                            // Bv::VDeal(a) => buf.push(buf[usize::from(*a)].bvadd(&buf[usize::from(*a)])),
                            // Bv::VShuff(a) => buf.push(buf[usize::from(*a)].bvmul(&buf[2 as usize])),
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


                /* fn egg_to_rostte(expr: &[Bv]) -> String {
                    let mut buf: Vec<> = vec![];
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
                } */

                /* match ret.as_string() {
                    "#t" => ValidationResult::Invalid,
                    "#f" => ValidationResult::Valid,
                    _ => ValidationResult::Unknown
                } */

                match solver.check() {
                    SatResult::Sat => ValidationResult::Invalid,
                    SatResult::Unsat => ValidationResult::Valid,
                    SatResult::Unknown => ValidationResult::Unknown
                }
                // ValidationResult::Valid
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
