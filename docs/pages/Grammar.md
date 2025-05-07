[\[<< Semantic Properties in MISAAL\]](./MISAAL_Properties.md)   [\[>> Swizzle Generation\]](./Swizzles.md)

# Concretization Grammar
<tt>MISAAL</tt> uses a novel form of Syntax Guided Synthesis specifically designed for AutoLLVM IR. 

The objective of the synthesis problem, given two AutoLLVM IR expression `R` and `L` with symbolic parameterizations, find any concrete parameterization of `R` and `L`, denoted by
```
R' = Concretization(R)
L' = Concretization(L)
```
, such that `R' ≡ L'`. 

To find such `R'` and `L'`, the synthesis problem in <tt>MISAAL</tt> proposes the notion of a **Concretization Grammar**, where the operations in the grammar are structured according to the AutoLLVM IR equivalence class of `R` and `L`, but the choice of which parameterizations, i.e. concretizations, to use are expressed as symbolic choices. 

This concretization grammar is implemented using the [choose*](https://docs.racket-lang.org/rosette-guide/sec_rosette-libs.html#%28def._%28%28lib._rosette%2Flib%2Fangelic..rkt%29._choose%2A%29%29) construct in `Rosette`. We have built a `Python` utility to automatically emit the concretization grammar in Rosette. The class which implements this functionality is `EqClassExpandGenerator` in [{MISAAL_ROOT/lib/grammar_gen/EqClassExpandGenerator}](../../lib/grammar_gen/EqClassExpandGenerator.py).

The constructor for this object takes in a list of `DSLInstruction`, ordered input bitvector sizes, and a boolean parameter `use_any_reg`. If `use_any_reg` is enabled then the choice of which `Reg` to use in the terminals of `L` and `R` also becomes a symbolic choice in the grammar, otherwise the register index is fixed. 

Once a `EqClassExpandGenerator` object is created, its member function `emit_grammar` returns the generated Rosette concretization grammar according to a `ref_expr`, which is a expression template represented using expressions of `Context` types. The `emit_grammar` is invoked for both `L` and `R` expressions to create the concretization grammar. Once this is done, a synthesis / verification problem can be created around these grammars as needed. Many of the properties in <tt>MISAAL</tt> use this concretization grammar.