[\[<< Support Frontend\]](./Support_Frontend.md)  [\[Overview\]](../Overview.md) [\[>> AutoLLVM IR\]](./AutoLLVM.md)

# Supporting New Backends in MISAAL

This guide describes how to add support for a new target architecture in MISAAL. The process involves providing formal semantics for your target's instructions and integrating with MISAAL's compilation pipeline.

## Overview

Adding a new backend requires:
1. Implementing formal semantics for your target architecture
2. Converting semantics to AutoLLVM IR format
3. Integrating with MISAAL's compilation pipeline
4. Implementing target-specific LLVM passes

## Step 1: Implementing Target Semantics

You can provide target semantics in two formats:

### 1. Pseudocode Format
```python
# Example: x86 horizontal add instruction (_mm_hadds_epi16)
def horizontal_add_sat_i16(a, b):
    result = []
    # Process 128-bit vectors with 16-bit elements
    for outer in range(0, 128, 128):
        # Process second operand
        for i in range(64, 128, 16):
            low = extract_bits(b, i, i+15)
            high = extract_bits(b, i-16, i-1)
            result.append(saturating_add(low, high))
        # Process first operand
        for i in range(0, 64, 16):
            low = extract_bits(a, i, i+15)
            high = extract_bits(a, i+16, i+31)
            result.append(saturating_add(low, high))
    return concat(result)
```

### 2. Python Dictionary Format
```python
{
    "_mm_hadd_pi16": {
        "target_instructions": {
            "_mm_hadds_epi16": {
                "args": ["SYMBOLIC_BV_128", "SYMBOLIC_BV_128", "128", "128", "0", 
                        "64", "16", "64", "128", "16", "1", "2", "16", "1", 
                        "128", "112", "2", "0"],
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 128,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 2,
                "out_vectsize_index": 2,
                "in_lanesize_index": 8,
                "out_lanesize_index": 3,
                "in_precision_index": 9,
                "out_precision_index": 9,
                "arg_permute_map": [0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                "Signedness": 1,
                "Cost": "[{'Skylake': {'l': '3', 't': '2'}}]",
                "SIMD": "True",
                "Extensions": "['ssse3']"
            }
        }
    }
}
```

## Step 2: AutoLLVM IR Generation

The target semantics need to be converted to AutoLLVM IR format. This involves:

1. **Function Representation**
```lisp
(define (_mm_hadd_pi16 a b %vectsize0 %outerlanesize0 %innerlaneoffset0 
                       %innerlanesize0 %elemsize0 %innerlaneoffset1 
                       %innerlanesize1 %elemsize1 %arg0 %alpha.arg0 %arg1 
                       %arg2 %arg3 %arg4 %arg5 %arg6)
  (define dst
    (apply
      concat
      (for/list ([%outer.it (reverse (range 0 %vectsize0 %outerlanesize0))])
        (concat 
          (apply
            concat
            (for/list ([iterator.1 (reverse (range %innerlaneoffset1 
                                                  %innerlanesize1 %elemsize1))])
              (define %low.cofactor2 (*  iterator.1  %arg5))
              (define %low.offset1.new0 (-  %low.cofactor2  %arg4))
              (define %lastidx5 (-  %elemsize1  1))
              (define %high.offset3 (+  %low.offset1.new0  %lastidx5))
              (define %6 (extract  %high.offset3 %low.offset1.new0 b))
              (define %low.offset2.new0 (-  %low.cofactor2  %arg3))
              (define %lastidx4 (-  %elemsize1  1))
              (define %high.offset4 (+  %low.offset2.new0  %lastidx4))
              (define %7 (extract  %high.offset4 %low.offset2.new0 b))
              (define %8.ab0 (bvaddnw %6 %7 %elemsize1 %arg2))
              %8.ab0))
          (apply
            concat
            (for/list ([iterator.0 (reverse (range %innerlaneoffset0 
                                                  %innerlanesize0 %elemsize0))])
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
              (define %2.ab0 (bvaddnw %0 %1 %elemsize0 %arg0))
              %2.ab0)))))
  (bvpadhighbits dst %arg6))
```

2. **Parameter Specification**
- Vector sizes
- Lane sizes
- Precision information
- Signedness
- Cost metrics
- Required extensions

For detailed information about AutoLLVM IR format, refer to the [AutoLLVM IR documentation](./AutoLLVM.md).

## Step 3: MISAAL Integration

Once the semantics are defined, MISAAL automatically generates abstracted rewrite rules mapping frontend IR to your target's AutoLLVM IR. This is handled by MISAAL's pass pipeline infrastructure.

### Automated Rewrite Rule Generation

After providing the target semantics, MISAAL's pass pipeline will:
1. Analyze the semantics to identify instruction patterns
2. Generate abstracted rewrite rules
3. Create mappings between frontend IR and target AutoLLVM IR
4. Optimize the rewrite rules for the target architecture

This process is automatic and requires no manual intervention once the semantics are correctly specified. The pass pipeline handles:
- Pattern identification
- Semantic equivalence checking
- Cost-based optimization
- Rule verification

For more details on the pass pipeline, see the [Pass Pipeline Framework](./PassPipeline.md).

### Configuration Steps

1. **Add Target Enum**
```cpp
// In interface/libmisaal/include/misaal.h
enum TARGET {
    x86,
    HVX,
    ARM,
    YourTarget  // Add your target here
};
```

2. **Define Target-Specific Components**
```cpp
// In interface/libmisaal/src/misaal.cpp
case YourTarget:
    inst_dsl_name = "your_target_semantics";
    swizzle_dsl_name = "your_target_swizzles";
    break;
```

3. **Add Pattern Support**
```cpp
// In patterns/YourTarget/
from patterns.base import Pattern

class YourTargetPatterns(Pattern):
    def __init__(self):
        super().__init__()
        # Define target-specific patterns
```

## Step 4: LLVM Backend Integration

MISAAL generates concretely parameterized AutoLLVM IR that maps 1:1 to target instructions. The backend needs to:

1. **Implement LLVM Intrinsics**
```llvm
declare <8 x i16> @llvm.yourtarget.vadd.v8i16(<8 x i16>, <8 x i16>)
```

2. **Create Target-Specific Pass**
```cpp
class YourTargetLegalizer : public llvm::FunctionPass {
public:
    static char ID;
    YourTargetLegalizer() : FunctionPass(ID) {}

    bool runOnFunction(Function &F) override {
        // Convert AutoLLVM IR to target intrinsics
    }
};
```

3. **Register Pass in libmisaal**
```cpp
std::string MisaalCompiler::get_llvm_so_path() {
    switch(target) {
        case YourTarget:
            return "\"/path/to/LLVMYourTargetLegalizer.so\"";
        // ... other targets
    }
}
```

## Important Notes

1. **Backend Requirements**
   - Register allocation is handled by the backend
   - Instruction scheduling is handled by the backend
   - MISAAL focuses on instruction selection quality

2. **LLVM Integration**
   - Target instructions should be available as LLVM intrinsics
   - Use Hydride compilation flow for generating LLVM passes
   - Ensure correct pass invocation for your target

3. **Performance Considerations**
   - Define accurate cost models in semantics
   - Consider SIMD capabilities
   - Document required extensions

## Best Practices

1. **Semantics Definition**
   - Document all instruction variants
   - Include edge cases and constraints
   - Provide comprehensive test cases

2. **AutoLLVM IR**
   - Follow existing patterns for similar instructions
   - Validate IR generation
   - Test with different parameter combinations

3. **Backend Integration**
   - Follow LLVM coding guidelines
   - Add debug logging
   - Document pass dependencies

## See Also
- [AutoLLVM IR](./AutoLLVM.md)
- [Support Frontend](./Support_Frontend.md)
- [Pass Pipeline Framework](./PassPipeline.md)
- [Hydride Paper](https://hydride.cs.illinois.edu/files/2024/05/Hydride.pdf)