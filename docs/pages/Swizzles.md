[\[<< Concretization Grammar\]](./Grammar.md) [\[Overview\]](../Overview.md)  [\[>> Rewrite Rule Representation\]](./Patterns.md)
# Semantics Analysis to Generate and Abstract Swizzles


## Analyzing the Access Patterns

<tt>MISAAL</tt> analyzes the bitvector access patterns of target ISA instructions, represented in `Rosette` and generates artificial swizzle operations. Swizzle operations are a type of vector manipulation operation commonly used in graphics programming which reorder, replicate, or extract components of a vector. We refer to specific swizzle transformations as swizzle patterns (often described by a shuffle/swizzle mask. See [LLVM Shuffle Vector](https://llvm.org/docs/LangRef.html#id192) for reference). The property which identifies these swizzles is called `IdentifySwizzles`. This property executes the instructions and creates a stream of bitvector slices accessed when producing the output value for each vector lane. This stream is often refered to as `bv_stream` in the code for this property. 

Broadly <tt>MISAAL</tt> generates two categories of swizzles. One category is swizzles derived from a single vector operand. These swizzles are often needed to correct the layout of vector operands and/or result for operations which read/write elements to a non-uniform index. Instructions such as Qualcomm's HVX operation `VMPYBV` operations require such 'corrective' swizzles.  The specific function in `IdentifySwizzles` which identfies these swizzles is `generate_inter_iteration_access_swizzle`. The comments of this function further help in visualizing these kinds of swizzles:
```Python
    def generate_inter_iteration_access_swizzle(self, var_to_size_map, streams, max_distinct_inputs, target_vector_sizes, input_prec, output_prec, output_size, combine_slices = False ):
        """SIMD operations which access non-contigous slices across iterations. For example:

        op [a0, a1, a2, a3] = [fn[a0], fn[a2], fn[a1], fn[a3]]

        In such cases we can derive two different swizzles:
        1. Reorder the input such that the output is produced in a contigous manner:
            swizzle_operand([a0, a1, a2, a3]) => [a0, a2 , a1, a3]
            op[ a0, a2, a1, a3 ]  =[fn[a0], fn[a1], fn[a2], fn[a3]]

        2. Reorder the output such that operation is applied on elements
            in a contigous manner

            ;output index:    0        1       2       3           0       2       1       3
            swizzle_output([fn[a0], fn[a2], fn[a1], fn[a3]]) => [fn[a0], fn[a1], fn[a2], fn[a3]]

        We find such relations across operands and outputs. Currently, we limit ourselves
        to those operands and outputs which contain the same number of elements (but the element-bitwidth
        can be different, and in most of these cases is).
        """
```


The second category of swizzles <tt>MISAAL</tt> generates are for cross-lane vector operations which access multiple operand indices when producing a single vector output lane value. These kinds of instructions often rely on packing vector elements from multiple operands. An example of the kinds of target instructions which require these 'packing' swizzles are x86 dot-product operations, `dpwssd`, which horizontally reduce pairs of neighboring elements. The function in `IdentifySwizzles` which produces these packing swizzles is called `generate_intra_iteration_access_swizzle`. This takes as parameters the number of vector operands to pack from, and their sizes. Depending on such parameters, the `packing` may sample either all elements of the vector operands or some subset of them. In case the number of elements sampled from the vector operands is less than the total number of the vector operands, <tt>MISAAL</tt> generates different swizzles for each `chunk`. For example, pack the first half of two vector elements or pack the second half of two vector operands. 


## Swizzle Access Pattern Representation as Property Result
The `IdentifySwizzle` does not directly produce the formal semantics of the swizzles. The result of this property is a python dictionary describing the swizzles as a shuffle vector mask. Below is the example for the packing swizzle in x86:

```Python
   "_mm512_dpwssd_epi32": [
         {
             "property_name": "IdentifySwizzles",
             "property": {
                 "candidate": "_mm256_maddubs_epi16",
                 "num_sources": 2,
                 "contexts": [
                     {
                         "swizzle_args": [
                             [
                                 0,
                                 0
                             ],
                             [
                                 1,
                                 16
                             ],
                             [
                                 0,
                                 1
                             ],
                             [
                                 1,
                                 17
                             ],
                             [
                                 0,
                                 2
                             ],
                             [
                                 1,
                                 18
                             ],
                             # ... Truncated for space
                                            }                       "result_size": 512,
                         "operand_size": 256,
                         "prec": 16,
                         "num_sources": 2,
                         "output_prec": 32
                     }
                 ]
             }
         },
```

The dictionary entries provide the details such as the number of vector operands from which the swizzle is derived, the result and operands bitvector sizes, the `prec` or element-bitwdith. The swizzle args describe the swizzle mask using an ordered list of `(operand_index, absolute_index)`. `operand_index` provides the index into which vector operand we're referring to. In the example above it takes the values `0` and `1` as there are 2 `num_sources`. The `absolute_index` refers to the index into the concatenated vector of all operands. This notation is directly inspired by `LLVM`'s representation of shufflevector masks. This representation is then later processed into another intermediate representation before finally generating pseudo-code for the swizzles to convert into formal semantics and then converted into AutoLLVM IR.


## Swizzle Access Pattern Processing in SwizzleUtils
The results of `IdentifySwizzles` are processed into `Swizzle` objects described in [SwizzleUtils](../../lib/utils/SwizzleUtils.py). This class represents the intermediate swizzles as objects in Python. It provides utilities to visualize the swizzles, which is very helpful for debugging purposes, but importantly it provides two important utilites.
The first is that it de-duplicates swizzles masks which are **identical** to reduce duplication. For example, the x86 horizontal 2-point dot-product and the x86 horizontal 2-point add actually have identical access patterns (for fixed vector sizes and element-bitwidths). The swizzles are then merged, and meta-data is also merged which keeps track of which target instructions were used in deriving the specific swizzle pattern.

The second purpose this property serves is that it produces the pseudocode of the swizzle as an unrolled sequence of operations which stores the corresponding bitvector slices into the resultant indices. For simplicity, we target the same pseudo-code description as for x86 to reuse as much of the parsing code to generate AutoLLVM IR. Below is the example of the structure of the generated pseudocode, structured in `xml`.

```xml
<intrinsics_list>
     <intrinsic tech="AVX2" name="x86_swizzle_861">
         <type>Integer</type>
         <CPUID>AVX2</CPUID>
         <category>Swizzle</category>
         <return type="__m512i" varname="dst" etype="UI16"/>
         <parameter type="__m256i" varname="v0" etype="UI8"/>
         <parameter type="__m256i" varname="v1" etype="UI8"/>
         <description>Automatically generated swizzle.</description>
         <operation>
             dst[7:0] := v0[7:0]
             dst[15:8] := v1[7:0]
             dst[23:16] := v0[15:8]
             dst[31:24] := v1[15:8]
             dst[39:32] := v0[23:16]
             dst[47:40] := v1[23:16]
             dst[55:48] := v0[31:24]
             dst[63:56] := v1[31:24]
             ...
        </operation>
                 <instruction name="x86_swizzle_861" form="ymm, ymm, ymm" xed="VPUNPCKLBW_YMMqq_YMMqq_YMMqq"/>
         <header>immintrin.h</header>
     </intrinsic>
     # Other Intrinsics ... 
</intrinsics_list>
```

This set of operation pseudocodes are then parsed into <tt>Hydride</tt>'s intermediate representation after which they generate the Python dictionary representation of AutoLLVM IR representation as described in [AutoLLVM IR Representation](./AutoLLVM.md). The result of these are fully formally specified and automatically generated swizzle operations ready for synthesis! 

