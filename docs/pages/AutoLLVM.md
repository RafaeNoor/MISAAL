[\[<< Overview\]](../Overview.md)   [\[>> MISAAL Semantic Property\]](./Property.md)

# AutoLLVM Intermediate Representation
<tt>MISAAL</tt> uses the formal semantics representation of target ISA operations as defined in <tt>Hydride</tt>. The formal semantics are represented using functions defined in the solver-aided programming language [Rosette](https://docs.racket-lang.org/rosette-guide/index.html).

A collection of instructions with _similar_ (**but not equivalent**) semantics are categorized into equivalence classes referred to as **AutoLLVM IR**. 

The AutoLLVM IR is a formal representation of this equivlance class is described similarly by a Rosette functional implementation with additional parameterizations. Note that the term AutoLLVM IR and equivalance class is often used interchangeably. For example, below is the representation of the AutoLLVM IR representation of the horizontal add instructions in x86. 

## Rosette Representation

```lisp
(define (_mm_hadd_pi16  a b %vectsize0 %outerlanesize0 %innerlaneoffset0 %innerlanesize0 %elemsize0 %innerlaneoffset1 %innerlanesize1 %elemsize1 %arg0 %alpha.arg0 %arg1 %arg2 %arg3 %arg4 %arg5 %arg6 )
  (define dst
    (apply
      concat
      (for/list ([%outer.it (reverse (range 0 %vectsize0 %outerlanesize0))])
                (concat 
                  (apply
                    concat
                    (for/list ([iterator.1 (reverse (range %innerlaneoffset1 %innerlanesize1 %elemsize1))])
                              (define %low.cofactor2 (*  iterator.1  %arg5))
                              (define %low.offset1.new0 (-  %low.cofactor2  %arg4))
                              (define %lastidx5 (-  %elemsize1  1))
                              (define %high.offset3 (+  %low.offset1.new0  %lastidx5))
                              (define %6 (extract  %high.offset3 %low.offset1.new0 b))
                              (define %low.offset2.new0 (-  %low.cofactor2  %arg3))
                              (define %lastidx4 (-  %elemsize1  1))
                              (define %high.offset4 (+  %low.offset2.new0  %lastidx4))
                              (define %7 (extract  %high.offset4 %low.offset2.new0 b))
                              (define %8.ab0 (bvaddnw %6 %7 %elemsize1 %arg2 ))
                              %8.ab0
                              )
                    )
                  (apply
                    concat
                    (for/list ([iterator.0 (reverse (range %innerlaneoffset0 %innerlanesize0 %elemsize0))])
                              (define %factor0 (/  %elemsize0  %elemsize0))
                              (define %factor1 (*  %alpha.arg0  %factor0))
                              (define %low.cofactor0 (*  iterator.0  %factor1))
                              (define %low.offset0 (+  %low.cofactor0  %arg1))
                              (define %lastidx2 (-  %elemsize0  1))
                              (define %high.offset0 (+  %low.offset0  %lastidx2))
                              (define %0 (extract  %high.offset0 %low.offset0 a))
                              (define %lastidx1 (-  %elemsize0  1))
                              (define %high.offset1 (+  %low.cofactor0  %lastidx1))
                              (define %1 (extract  %high.offset1 %low.cofactor0 a))
                              (define %2.ab0 (bvaddnw %0 %1 %elemsize0 %arg0 ))
                              %2.ab0
                              )
                    )
                  )
                )
      )
    )
  (bvpadhighbits  dst %arg6)
  )
```

Interpretting these functions is difficult, let alone converting them into a formal semantics for synthesis and verification. Fortunately, Rosette maps the definition of these functions into a formal semantics automatically and allows constructs such as `synthesize` and `verify` to create semantics driven tools around. 

The arguments to this function are of various types:

* `a` and `b` are bitvector types (in Rosette) and correspond to the individual bits of the vector registers for these x86 instructions.

* `%vectsize0`, `%outerlanesize0`, `%innerlaneoffset0` (and similarly the `1` variants) control the loop structure to index into these vectors and produce the results. They reason about complex offsets into these vectors which occur in cross-lane vector instructions such as horizontal addition.

* `%arg1`, `%arg2`, `%arg3`, `%arg4`, `%arg5`,`%arg6` control the variant of bitvector operations to use. For example the `bvaddnw` in `(define %2.ab0 (bvaddnw %0 %1 %elemsize0 %arg0 ))` actually behaves as following. For more details on such instructions refer to the [defintion of the abstracted bitvector ops](https://github.com/akothen/Hydride/blob/main/code-synthesizer/hydride/utils/bvops.rkt): 

```python
    if %arg0 == 1:
        # do signed saturating accumulation
    else if %arg0 == 0:
        # do unsigned saturating accumulation
    otherwise:
        # do regular accumulation
```

* `%elemsize0` and `%elemsize1` correspond to the individual element bitwidth of the operands in the vector registers. For example, 16-bit elements in 256-bit vector registers, so `elemsize0` would be 16. As such these parameters are used to control the loop structure as well as indexing bitvector slices into the vector registers.


## Python Dictionary Representation

Different parameterization of AutoLLVM IR functions correspond to different target specific instructions. In the example of the horizontal-add equivalance classes

**_mm_hadds_epi16** corresponds to the following parameterization:
```lisp
(_mm_hadd_pi16 a b 128 128 0 64 16 64 128 16 1 2 16 1 128 112 2 0)
```
This instruction takes as input 2x 128-bit vector registers with 16-bit elements and does a signed-saturating horizontal addition producing 128-bit vector with itself 16-bit elements. We encode this information to be saved in file as a Python dictionary generated by <tt>Hydride</tt> after it's similar instruction analysis completes. The structure of this dictionary is described in the following snippet:


```python
          # Name of the AutoLLVM IR representation
          "_mm_hadd_pi16" : {
            "target_instructions" : {
            # Other parameterizations ...
              "_mm_hadds_epi16" : {
                  "args" : ["SYMBOLIC_BV_128","SYMBOLIC_BV_128","128","128","0","64","16","64","128","16","1","2","16","1","128","112","2","0"],
                  "in_vectsize" : 128,
                  "out_vectsize" : 128,
                  "lanesize" : 128,
                  "in_precision" : 16,
                  "out_precision" : 16,
                  "in_vectsize_index" : 2,
                  "out_vectsize_index" : 2,
                  "in_lanesize_index" : 8,
                  "out_lanesize_index" : 3,
                  "in_precision_index" : 9,
                  "out_precision_index" : 9,
                  "arg_permute_map" : [0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  "Signedness" : 1,
                  "Cost" : "[{'Skylake': {'l': '3', 't': '2'}}]",
                  "SIMD" : "True",
                  "Extensions" : "['ssse3']",
        },
      },
            "semantics" : ['"(define (_mm_hadd_pi16  a b %vectsize0 %outerlanesize0 %innerlaneoffset0 %innerlanesize0 %elemsize0 %innerlaneoffset1 %innerlanesize1 %elemsize1 %arg0 %alpha.arg0 %arg1 %arg2 %arg3 %arg4 %arg5 %arg6 )"', '"(define dst"', '"(apply"', '"concat"', '"(for/list ([%outer.it (reverse (range 0 %vectsize0 %outerlanesize0))])"', '" (concat "', '"  (apply"', '"  concat"', '"  (for/list ([iterator.1 (reverse (range %innerlaneoffset1 %innerlanesize1 %elemsize1))])"', '"   (define %low.cofactor2 (*  iterator.1  %arg5))"', '"   (define %low.offset1.new0 (-  %low.cofactor2  %arg4))"', '"   (define %lastidx5 (-  %elemsize1  1))"', '"   (define %high.offset3 (+  %low.offset1.new0  %lastidx5))"', '"   (define %6 (extract  %high.offset3 %low.offset1.new0 b))"', '"   (define %low.offset2.new0 (-  %low.cofactor2  %arg3))"', '"   (define %lastidx4 (-  %elemsize1  1))"', '"   (define %high.offset4 (+  %low.offset2.new0  %lastidx4))"', '"   (define %7 (extract  %high.offset4 %low.offset2.new0 b))"', '"   (define %8.ab0 (bvaddnw %6 %7 %elemsize1 %arg2 ))"', '"   %8.ab0"', '"  )"', '"  )"', '"  (apply"', '"  concat"', '"  (for/list ([iterator.0 (reverse (range %innerlaneoffset0 %innerlanesize0 %elemsize0))])"', '"   (define %factor0 (/  %elemsize0  %elemsize0))"', '"   (define %factor1 (*  %alpha.arg0  %factor0))"', '"   (define %low.cofactor0 (*  iterator.0  %factor1))"', '"   (define %low.offset0 (+  %low.cofactor0  %arg1))"', '"   (define %lastidx2 (-  %elemsize0  1))"', '"   (define %high.offset0 (+  %low.offset0  %lastidx2))"', '"   (define %0 (extract  %high.offset0 %low.offset0 a))"', '"   (define %lastidx1 (-  %elemsize0  1))"', '"   (define %high.offset1 (+  %low.cofactor0  %lastidx1))"', '"   (define %1 (extract  %high.offset1 %low.cofactor0 a))"', '"   (define %2.ab0 (bvaddnw %0 %1 %elemsize0 %arg0 ))"', '"   %2.ab0"', '"  )"', '"  )"', '" )"', '")"', '")"', '")"', '"(bvpadhighbits  dst %arg6)"', '")"', '""'],
          }
```

There are many parameters described here for which are not worth describing in detail for all of them. However, we can describe the overall structure. The target instructions are described in a nested python dictionary format. The outer most keys are the name of the specific AutoLLVM equivlance classes (which are often just the name of any one member, since naming is hard!). Within those dictionary there is the key `target_instructions` which contains the dictionary entries for individual target specific instructions. We refer to these as `Contexts` which we will elabore more on why later. The `semantics` field simply describes the textual Rosette semantics of the AutoLLVM IR instruction as a python `List[str]`.


Some important details of the `Context` for **_mm_hadds_epi16**:
* `args`: Describes the specific argument types for this instruction. `SYMBOLIC_BV_{n}` corresponds to vector registers with `n`-bits. 

* `in_vectsize`, `out_vectsize`, `in_precision`, `out_precision` correspond to the number of bits for the input bitvectors, output bitvector, input bitvector element bitwidth and output bitvector element-bitwidth respectively.

* The `{param}_index` parameters refer to the argument index into the `args` list corresponding to the value of the `{param}` parameter. For example `in_vectsize_index`: 2 corresponds to `"128"` in `args` which is equivalent to the `in_vectsize` value of this instruction.

While this description is useful for distributing semantics, it is not the cleanest representation for reasoning about and manipulating AutoLLVM instructions. 
As such this dictionary format is parsed into appropriate Python classes which are described in the following section.


## Python Classes for AutoLLVM IR

The above dictionary formats are parsed into various python classes for Equivalence Classes, Target Specific Parameterization of AutoLLVM IRs, and different argument types for these AutoLLVM IR operations.

### Argument Types
This section describes the implementation of various argument types. The code for which can be found [here](https://github.com/akothen/Hydride/blob/bitserial/code-synthesizer/dsl-ir/common/Types.py).
* `BitVector` : Corresponding to vector / scalar registers for target instructions.

* `ConstBitVector`: Compile Time constant values used in the semantics of the AutoLLVM representation. These are usually added when constant values in the semantics of a specific target instructions are lifted to function parameters.

* `Precision`, `LaneSize`, `Integer`: Correspond to numeric parameters corresponding to Element-Bitwidths, Vector Lane Sizes, and other integer parameters (such as loop bounds) respectively. 

* `Bool`: Corresponding to Rosette boolean values. Depending on the instructions the boolean values may be represented using `i1` bitvector type of `boolean` type in Rosette.

* `Reg`: Corresponds to vector / scalar operands as part of an expression expressed using AutoLLVM IR operations. For example `Reg(0)` corresponds to formal parameter 0 of the full expression. These are used to relate operands across parameters.

### Instruction Representations
This section describes the representation of AutoLLVM IR operations in Python used by <tt>MISAAL</tt>. The code for which can be found [here](https://github.com/akothen/Hydride/blob/bitserial/code-synthesizer/dsl-ir/common/Instructions.py).

* `DSLInstruction`: Corresponds to the AutoLLVM IR / Equivalence classes. This object contains a list of `Context`'s objects corresponding to individual parameterizations.

* `Context`: Corresponds to specific parameterizations of AutoLLVM instructions. The same parameters and descriptions described in the python dictionary representation are also described here. This class has further functionality including the ability to 'scale' semantics as described in Hydride. This representation is also used to describe expressions for enumeration in <tt>MISAAL</tt> which consists of multiple `Contexts` and other argument types.
