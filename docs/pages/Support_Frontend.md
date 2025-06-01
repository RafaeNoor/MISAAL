[\[<< Pass Pipeline Framework\]](./PassPipeline.md)  [\[Overview\]](../Overview.md) [\[>> Support Backend\]](./Support_Backend.md)

# Supporting New Frontends in MISAAL

This guide describes how to integrate a new compiler frontend with MISAAL. The integration process involves implementing IR semantics in Rosette and creating a pass to emit expressions in MISAAL's s-expression format.

## Overview

To integrate a new frontend with MISAAL, you need to:

1. Implement formal semantics of your frontend's IR in Rosette
2. Create a pass to generate s-expressions for synthesis
3. Link with libmisaal for compilation

## Step 1: Implementing IR Semantics

The first step is to implement the formal semantics of your frontend's IR in Rosette using MISAAL's dictionary format.

### Example: Halide IR Semantics

Halide's IR semantics are implemented in `lib/sema/halide_decomposed.py`. The semantics are defined as a Python dictionary that maps IR operations to their formal specifications:

```python
halide_decomposed = {
    "typed:cast-int-extend": {
        "target_instructions": {
            "typed:cast-int_1_ip16_is2048_op32_os4096_signed_1": {
                "in_vectsize": 2048,
                "out_vectsize": 4096,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 32,
                # ... other properties
            }
        }
    }
    # ... other operations
}
```

### Guidelines for IR Semantics

1. Define each IR operation with its complete semantic specification
2. Include all relevant properties:
   - Input/output vector sizes
   - Precision information
   - Signedness
   - Cost metrics
   - SIMD support
   - Required extensions

## Step 2: Expression Generation Pass

Create a pass that converts your IR into MISAAL's s-expression format for synthesis.

### Key Components

1. **Expression Visitor**: Implement a visitor pattern to traverse your IR
2. **S-Expression Generation**: Convert IR nodes to equivalent s-expressions
3. **Type Handling**: Map your IR types to MISAAL's type system
4. **Variable Management**: Handle variable scoping and let-bindings

### Example: Halide's Implementation

Halide's implementation in `frontends/halide/src/Rosette.cpp` demonstrates:

1. IR node visitors (`ExprPrinter` class)
2. Type conversion (`type_to_rake_type`)
3. Expression generation (`expr_to_racket`)
4. Variable encoding (`InferVarEncodings`)

```cpp
class ExprPrinter : public VariadicVisitor<ExprPrinter, std::string, std::string> {
    // Visitor implementation for each IR node type
    std::string visit(const Add *op) {
        // Generate s-expression for addition
    }
    // ... other node visitors
};
```

## Step 3: Integration with libmisaal

MISAAL provides a C++ interface library (`libmisaal`) for frontend integration. This library handles the complex task of interfacing between your frontend and MISAAL's synthesis engine.

### Architecture Overview

The libmisaal library serves as a bridge between:
1. Your frontend's IR and expression generation
2. MISAAL's synthesis engine
3. Target-specific code generation

### Key Components of libmisaal

1. **Compiler Interface**
```cpp
namespace misaal {
    class MisaalCompiler {
        public:
            // Initialize compiler for specific target
            MisaalCompiler(TARGET t);
            
            // Queue expression for compilation
            void add_expression_to_compile(std::string expr, std::string name);
            
            // Compile all queued expressions
            void compile_expression(std::string output_bitcode_path, 
                                  std::string benchmark);
    };
}
```

2. **Target Architecture Support**
```cpp
enum TARGET {
    x86,
    HVX,
    ARM,
    Halide
};
```

3. **Environment Configuration**
- Required Environment Variables:
  ```bash
  MISAAL_SRC=/path/to/misaal/source
  HYDRIDE_ROOT=/path/to/hydride
  PYTHONPATH=/path/to/code-synthesizer:/path/to/codegen-generator
  ```
- Optional Configuration:
  ```bash
  # Disable frontend-specific rewrite patterns
  MISAAL_DISABLE_FRONTEND_PATTERNS=1
  
  # Configure number of rewrite iterations
  MISAAL_EQ_SAT_ITERS=5
  ```

### Detailed Integration Process

1. **Initialization**
```cpp
// Create compiler instance for your target
misaal::MisaalCompiler compiler(misaal::TARGET::YourTarget);
```

2. **Expression Compilation Pipeline**
```cpp
// Add expressions to compile
for (auto& expr : your_expressions) {
    // Convert your IR to s-expression format
    std::string s_expr = convert_to_sexpr(expr);
    
    // Add to compilation queue with unique name
    compiler.add_expression_to_compile(s_expr, 
                                     generate_unique_name(expr));
}

// Compile all expressions
compiler.compile_expression("/path/to/output.bc", "benchmark_name");
```

3. **Internal Workflow**
When `compile_expression` is called, libmisaal:
   - Generates a Python compilation script
   - Sets up DSL lists for input and output
   - Configures target-specific patterns
   - Initializes LLVM backend components
   - Manages compilation process

### Target-Specific Considerations

1. **Pattern Management**
```cpp
// Pattern loading sequence
frontend_patterns = load_frontend_patterns()  // Optional
target_patterns = load_target_patterns()      // Required
combined_patterns = frontend_patterns + target_patterns
```

2. **DSL Configuration**
```python
# Input DSL (your frontend's IR)
input_dsl = parse_dict_with_bounded(your_frontend_semantics)

# Output DSL (target architecture)
inst_dict = parse_dict_with_bounded(target_semantics)
swizzle_dict = parse_dict_with_bounded(target_swizzles)
output_dsl = inst_dict + swizzle_dict
```

3. **LLVM Integration**
Each target requires specific LLVM components:
- Legalizer shared library
- Target-specific flags
- Intrinsic wrappers

### Error Handling and Debugging

1. **Environment Validation**
```cpp
const char* MISAAL_PATH = std::getenv("MISAAL_SRC");
assert(MISAAL_PATH && "MISAAL_SRC path not defined");

const char* HYDRIDE_PATH = std::getenv("HYDRIDE_ROOT");
assert(HYDRIDE_PATH && "HYDRIDE_ROOT path not defined");
```

2. **Compilation Monitoring**
```cpp
// Timing information is automatically logged
auto start = std::chrono::system_clock::now();
// ... compilation ...
auto end = std::chrono::system_clock::now();
std::chrono::duration<double> elapsed_seconds = end - start;
std::cout << "Compilation took " << elapsed_seconds.count() 
          << " seconds ...\n";
```

3. **Error Checking**
```cpp
int ret_code = system(cmd.c_str());
if(ret_code != 0) {
    assert(false && "Error while running compilation script");
}
```

### Best Practices for libmisaal Integration

1. **Expression Management**
   - Generate unique names for expressions
   - Batch related expressions together
   - Clean up temporary files after compilation

2. **Resource Management**
   - Set up environment variables in build system
   - Validate all paths before compilation
   - Handle cleanup of generated files

3. **Performance Optimization**
   - Batch expressions when possible
   - Reuse compiler instance
   - Configure appropriate iteration counts

4. **Debugging Support**
   - Add logging for expression generation
   - Monitor compilation progress
   - Preserve intermediate files when needed

### Common Issues and Solutions

1. **Environment Setup**
   - Problem: Missing environment variables
   - Solution: Add validation in your build system

2. **Pattern Loading**
   - Problem: Incorrect pattern application
   - Solution: Use `MISAAL_DISABLE_FRONTEND_PATTERNS` for debugging

3. **Compilation Failures**
   - Problem: Synthesis timeout
   - Solution: Adjust `MISAAL_EQ_SAT_ITERS`

4. **Integration Testing**
   - Problem: Difficult to verify correctness
   - Solution: Add unit tests for s-expression generation

## Best Practices

1. **IR Semantics**
   - Document all operation semantics thoroughly
   - Include test cases for semantic verification
   - Handle edge cases and type variations

2. **Expression Generation**
   - Maintain type safety during conversion
   - Handle all IR node types
   - Implement proper error handling
   - Add logging for debugging

3. **Integration**
   - Set up proper build system integration
   - Add tests for the integration
   - Document environment requirements
   - Handle resource cleanup

## See Also
- [Pass Pipeline Framework](./PassPipeline.md)
- [AutoLLVM IR](./AutoLLVM.md)
- [Property Base Class](./Property.md)