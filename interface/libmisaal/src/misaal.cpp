#include <iostream>
#include <vector>
#include <stdlib.h>
#include "misaal.h"



namespace misaal {

    void MisaalCompiler::add_expression_to_compile(std::string expr, std::string name){
        CompilerQuery Task(expr, name);
        Expressions.push_back(Task);
    }

    void MisaalCompiler::compile_expression(std::string output_bitcode_path){

    }


    std::string MisaalCompiler::get_compiler_python_import(){
        std::string imports = " \
                               from compiler.HydrideCompiler import HydrideCompiler \
                               from egg_config import EGG_PKG_PATH \
                               from sema.hexsemantics_new import semantics as hvx_semantics \
                               from sema.x86SemanticsAllArgs import semantcs as x86_semantics \
                               from sema.halide_sema import halide_semantics \
                               from sema.hex_swizzles import hvx_swizzles \
                               from sema.x86_swizzles import x86_swizzles \
                               from sema.arm_swizzles import arm_swizzles \
                               from sema.ARMSema import arm_semantics \
                               from sema.repairs_sema import repair_semantics \
                               from common.DSLParser import parse_dict \
                               ";

        return imports;

    }

    std::string MisaalCompiler::parse_dict(std::string output_name, std::string dict_name){
        return output_name + " = parse_dict(" +  dict_name + ")"; 
    }

    std::string MisaalCompiler::join(std::vector<std::string> statements, std::string join_on){
        std::string joined = "";

        for(auto str : statements){
            joined = joined +  str + join_on;
        }

        return joined;


    }

    std::string MisaalCompiler::get_input_dsl_list_definition(std::string input_dsl_name){
        std::string parse_inst_dict = parse_dict("halide_dsl_list", "halide_semantics");
        return input_dsl_name + " = halide_dsl_list";
    }


    std::string MisaalCompiler::get_output_dsl_list_definition(std::string output_dsl_name){
        std::string swizzle_dsl_name;
        std::string inst_dsl_name;

        switch(target){
            case x86:
                inst_dsl_name = "x86_semantics";
                swizzle_dsl_name = "x86_swizzles";
                break;
            case HVX:
                inst_dsl_name = "hvx_semantics";
                swizzle_dsl_name = "hvx_swizzles";
                break;
            case ARM:
                inst_dsl_name = "arm_semantics";
                swizzle_dsl_name = "arm_swizzles";
                break;
        };

        std::string parse_inst_dict = parse_dict("inst_dict", inst_dsl_name);
        std::string parse_swizzle_dict = parse_dict("swizzle_dict", swizzle_dsl_name);

        std::vector<std::string> statements;

        statements.push_back(parse_inst_dict);
        statements.push_back(parse_swizzle_dict);

        std::string output_list = output_dsl_name + " = inst_dict + swizzle_dict"; 
        statements.push_back(output_list);
        return join(statements, "\n");

    }

    std::string  MisaalCompiler::get_patterns_import(std::string pattern_alias){

        std::string partial_import = "";

        switch(target){
            case x86:
                partial_import = "from patterns.x86 import x86_patterns";
                break;
            case HVX:
                partial_import = "from patterns.HVX import HVX_patterns";
                break;
            case ARM:
                partial_import = "from patterns.ARM import ARM_patterns";
                break;
        };

        return partial_import + " as " + pattern_alias;
    }


    std::string MisaalCompiler::get_llvm_so_path(){
        std::string path;
        switch(target){
            case x86:
                path = "\"/shared/hydride/LLVMx86Legalizer.so\"";
                break;
            case HVX:
                path = "\"/shared/hydride/LLVMHVXLegalizer.so\"";
                break;
            case ARM:
                path = "\"/shared/hydride/LLVMARMLegalizer.so\"";
                break;
        };
        return path;
    }

    std::string MisaalCompiler::get_llvm_so_flags(){
        std::string flag;
        switch(target){
            case x86:
                flag = "\"-x86-hydride-legalize\"";
                break;
            case HVX:
                flag = "\"-hex-hydride-legalize\"";
                break;
            case ARM:
                flag = "\"-arm-hydride-legalize\"";
                break;
        };
        return flag;
    }


    std::string MisaalCompiler::get_llvm_intrinsic_wrapper(){
        std::string wrapper;
        switch(target){
            case x86:
                wrapper = "\"/shared/hydride/x86_wrappers.c.ll\"";
                break;
            case HVX:
                wrapper = "\"/shared/hydride/hvx_wrappers.ll\"";
                break;
            case ARM:
                wrapper = "\"/shared/hydride/arm_wrappers.ll\""; 
                break;
        };
        return wrapper;
    }

    std::string MisaalCompiler::emit_python_rewrite_file(std::string base_name){

        std::vector<std::string> statements;

        // Python Headers for required objects
        std::string common_imports  = get_compiler_python_import();
        statements.push_back(common_imports);

        std::string pattern_imports = get_patterns_import("misaal_patterns");
        statements.push_back(pattern_imports);

        // Parse Input and Output DSL Lists

        std::string input_dsl_name = "misaal_input";
        std::string output_dsl_name = "misaal_output";

        std::string input_dsl_defn = get_input_dsl_list_definition(input_dsl_name);
        std::string output_dsl_defn = get_output_dsl_list_definition(output_dsl_name);

        statements.push_back(input_dsl_defn);
        statements.push_back(output_dsl_defn);

        std::string wrapper = "so_path = " + get_llvm_so_path();
        std::string flags = "llvm_flags = [" + get_llvm_so_flags() + "]";
        std::string intrinsics = "intrin = " + get_llvm_intrinsic_wrapper();

        statements.push_back(wrapper);
        statements.push_back(flags);
        statements.push_back(intrinsics);

        return join(statements, "\n");



    };


}
