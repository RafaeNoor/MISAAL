[\[<< Rewrite Rule Representation\]](./Patterns.md) [\[Overview\]](../Overview.md) [\[>> Supporting new frontends in MISAAL\]](./Support_Frontend.md)

# Term Rewriting System
<tt>MISAAL</tt> provides online compilation support using the derived [Patterns](./Patterns.md) using another python class [CompilerBase](../../lib/compiler/Compiler.py). The `CompilerBase` is an abstract class with functions define to compile an input expression described using `Context` into the target language. As such it takes the AutoLLVM representations of the source and target language as well as a `List[Pattern]` to perform the term rewriting. 

## Abstract Term Rewriting System Class
The following member functions need to be defined for any class inheriting from `CompilerBase`:

```python
    def initialize_class_map(self):
        raise NotImplementedError()

    def initialize_lit_class(self):
        raise NotImplementedError()

    def initialize_reg_class(self):
        raise NotImplementedError()

    def emit_pattern_matching_based_compiler(self, expr, swizzle_cost = 1):
        raise NotImplementedError()

    def convert_reg_to_compiler_datastructure(self, expr_regs):
        raise NotImplementedError()

    def apply_rewrite(self, expr, compiler_functionality, reg_data_structures):
        raise NotImplementedError()
```

* `initialize_{class,reg,lit}_map` describe any preprocessing which needs to be done when lowering `DSLInstruction`, `Reg`, `ConstBitVector` types. (We currently do not need any for our `egg` based flows).

* `emit_pattern_matching_based_compiler` is used to create the any data structures according to the input expression that we want to compile `expr`. In <tt>MISAAL</tt> unless lowering swizzles, we include all rewrite rules so the `expr` is ignored here. However other term rewriting systems can use this function to selectively include rewrite rules if needed. It is also assumed that the datastructure to represent the rewrite rules in this function includes the `cost` associated with each rewrite rule. This function takes an additional parameter `swizzle_cost` to specify the `cost` of swizzle operations. We will explain the reason for this later below.


* `convert_reg_to_compiler_datastructure` takes a list of `Reg` objects and creates their definitions in the term rewriting system. This often includes declaring the terminals of the leaves of the input expression, defining their element types and vector sizes, etc.

* `apply_rewrite` performs the rewriting. `compiler_functionality` is the return data structures from `emit_pattern_matching_based_compiler` and `reg_data_structures` are from `convert_reg_to_compiler_datastructure`. This function should return the output expression after term rewriting is completed in terms of `Context`.


## EggLog Compiler 
The [EggLogCompiler](../../lib/compiler/EggLogCompiler.py) inherits from `CompilerBase` to implement a term rewriting system using `EggLog`. The implementation of this class is best understood by reading the code. Importantly it takes the number of iterations of equality saturation as input. It also uses the `swizzle_cost` parameter to ensure that the AutoLLVM IR swizzles are fully legalized to target supported AutoLLVM IR operations. 

As <tt>MISAAL</tt> uses <tt>Hydride</tt>'s code generation support for lowering the parameterized AutoLLVM IR operations to intrinsics in `LLVM`, the [HydrideCompiler](../../lib/compiler/HydrideCompiler.py) inherits from the `EggLogCompiler` class to further support the lowering of output expression into `LLVM` functions.



## C++ libmisaal
Compilation flows wanting to compile using the <tt>MISAAL</tt> term rewriting system are required to generate the python code with the appropriate class and patterns. As many compilers are implemented in `C++`, we provide an extensible `C++` library which can be linked into compilers to facilitate generating these codes. The [libmisaal](../../interface/libmisaal/) is currently limited to supporting three targets and one frontend, namely:

```c++
 enum TARGET {
        x86,
        HVX,
        ARM,
        Halide
    };
```

The high level flow of this library essentially comes down to first collecting all the expressions which need to be compiled in terms of `string` using the following method:

```c++
void add_expression_to_compile(std::string expr, std::string name);
```
Once all expressions are collected, they need to be 'compiled' using the term rewriting system. 
```c++
void compile_expression(std::string output_bitcode_path, std::string benchmark);
```
This function currently generates the python script to import the frontend and target specific patterns, invoke the `HydrideCompiler` and writing the result after legalization to `output_bitcode_path` which would be an `.ll` filepath.
