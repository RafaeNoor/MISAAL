#include "misaal.h"
#include <tvm/tir/expr.h>
#include <tvm/tir/builtin.h>

namespace tvm {
namespace tir {
namespace misaal {
    
#define BASIC_VECTORIZABLE_OP(Op) \
bool IsVectorizable(const tir::Op##Node* op){ \
    return op->dtype.is_vector(); \
};

#define ALWAYS_VECTORIZABLE_OP(Op) \
bool IsVectorizable(const tir::Op##Node* op){ \
    return true; \
};


#define DEFINE_NOT_VECTORIZABLE_OP(Op)           \
bool IsVectorizable(const tir::Op##Node* op){ \
    return false;                            \
};

BASIC_VECTORIZABLE_OP(Sub);
BASIC_VECTORIZABLE_OP(Mul);
DEFINE_NOT_VECTORIZABLE_OP(Div);
DEFINE_NOT_VECTORIZABLE_OP(Mod);
BASIC_VECTORIZABLE_OP(Min);
BASIC_VECTORIZABLE_OP(Max);
DEFINE_NOT_VECTORIZABLE_OP(LT);
DEFINE_NOT_VECTORIZABLE_OP(LE);
DEFINE_NOT_VECTORIZABLE_OP(GT);
DEFINE_NOT_VECTORIZABLE_OP(GE);
DEFINE_NOT_VECTORIZABLE_OP(EQ);
DEFINE_NOT_VECTORIZABLE_OP(NE); // No semantics implemented
BASIC_VECTORIZABLE_OP(Add);
BASIC_VECTORIZABLE_OP(Cast);
// ALWAYS_VECTORIZABLE_OP(Ramp);
// ALWAYS_VECTORIZABLE_OP(Shuffle);
// ALWAYS_VECTORIZABLE_OP(Broadcast);

// DEFINE_NOT_VECTORIZABLE_OP(Cast);
DEFINE_NOT_VECTORIZABLE_OP(Ramp);
DEFINE_NOT_VECTORIZABLE_OP(Shuffle);
DEFINE_NOT_VECTORIZABLE_OP(Broadcast);

DEFINE_NOT_VECTORIZABLE_OP(And);
DEFINE_NOT_VECTORIZABLE_OP(Or);
DEFINE_NOT_VECTORIZABLE_OP(Var);
DEFINE_NOT_VECTORIZABLE_OP(IntImm);
DEFINE_NOT_VECTORIZABLE_OP(FloatImm);
DEFINE_NOT_VECTORIZABLE_OP(StringImm);
DEFINE_NOT_VECTORIZABLE_OP(Not);
DEFINE_NOT_VECTORIZABLE_OP(Select);
DEFINE_NOT_VECTORIZABLE_OP(Let);
DEFINE_NOT_VECTORIZABLE_OP(BufferLoad);

    bool IsVectorizable(const tir::CallNode* op){
        if (op->op.same_as(builtin::bitwise_or())){
            return false;
        } else if (op->op.same_as(builtin::bitwise_and())){
            return true;
        }
        return false;
    }

    void MisaalCompiler::add_expression_to_compile(std::string expr, std::string name){
        CompilerQuery Task(expr, name);
        Expressions.push_back(Task);
    }

    void MisaalCompiler::compile_expression(std::string output_bitcode_path, std::string benchmark){
        std::string python_content = emit_python_rewrite_file(output_bitcode_path, benchmark);
        std::string python_file_name = benchmark + "_misaal.py";
        write_to_file(python_file_name, python_content);

        execute_python_file(python_file_name);
    }

    bool MisaalCompiler::execute_python_file(std::string fname){
        std::string cmd = "python " + fname;
        auto start = std::chrono::system_clock::now();
        int ret_code = system(cmd.c_str());


        auto end = std::chrono::system_clock::now();

        std::chrono::duration<double> elapsed_seconds = end - start;
        std::cout << "Compilation took "<< elapsed_seconds.count() << " seconds ...\n";

        if(ret_code != 0){
            std::cerr << "MISAAL Unsuccessful";
            return false;
        }
        return true;
    }

    void MisaalCompiler::write_to_file(std::string fname, std::string content){
        std::cout << "Writing to " << fname << " ...\n";
        std::ofstream myfile;
        myfile.open (fname);
        myfile << content << "\n";
        myfile.close();
    }


    std::string MisaalCompiler::get_compiler_python_import(){
        std::string imports = "\
from compiler.HydrideCompiler import HydrideCompiler\n\
from utils.egg_config import EGG_PKG_PATH\n\
from sema.hexsemantics_new import semantics as hvx_semantics\n\
from sema.x86SemanticsAllArgs import semantcs as x86_semantics\n\
from sema.halide_decomposed import halide_decomposed as halide_semantics\n\
from sema.hvx_swizzles_decomposed import hvx_swizzles_decomposed as hvx_swizzles\n\
from sema.x86_swizzles_decomposed import x86_swizzles_decomposed as x86_swizzles\n\
from sema.arm_swizzles_decomposed import arm_swizzles_decomposed as arm_swizzles\n\
from sema.ARMSema import arm_semantics\n\
from sema.repairs_sema import repair_semantics\n\
from utils.DSLInstructionUtils import parse_dict_with_bounded\n\
import sys\n";
        return imports;

    }

    std::string MisaalCompiler::parse_dict(std::string output_name, std::string dict_name){
        return output_name + " = parse_dict_with_bounded(" +  dict_name + ")"; 
    }

    std::string MisaalCompiler::join(std::vector<std::string>& statements, std::string join_on){
        std::string joined = "";

        
        for(int i =0; i < statements.size(); i++){
            auto str = statements[i];
            if (i == statements.size() - 1){
                joined = joined +  str;
            } else {
                joined = joined +  str + join_on;

            }
        }

        return joined;


    }

    std::string MisaalCompiler::get_input_dsl_list_definition(std::string input_dsl_name){
        std::vector<std::string> statements;
        std::string parse_halide_dict = parse_dict("halide_dsl_list", "halide_semantics");
        statements.push_back(parse_halide_dict);
        statements.push_back(input_dsl_name + " = halide_dsl_list");

        return join(statements, "\n");
    }


    std::string MisaalCompiler::get_output_dsl_list_definition(std::string output_dsl_name){
        std::string swizzle_dsl_name;
        std::string inst_dsl_name;

        switch(target){
            case x86:
                inst_dsl_name = "x86_semantics";
                swizzle_dsl_name = "x86_swizzles";
                break;
            // case HVX:
            //     inst_dsl_name = "hvx_semantics";
            //     swizzle_dsl_name = "hvx_swizzles";
            //     break;
            // case ARM:
            //     inst_dsl_name = "arm_semantics";
            //     swizzle_dsl_name = "arm_swizzles";
            //     break;
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
            // case HVX:
            //     partial_import = "from patterns.HVX import HVX_patterns";
            //     break;
            // case ARM:
            //     partial_import = "from patterns.ARM import arm_patterns";
            //     break;
        };

        return partial_import + " as " + pattern_alias;
    }


    std::string MisaalCompiler::get_llvm_so_path(){
        std::string path;
        switch(target){
            case x86:
                path = "\"/u/is16/526/Hydride/codegen-generator/tools/low-level-codegen/build/libX86LegalizerAllArgs.so\"";
                break;
            // case HVX:
            //     path = "\"/shared/hydride/LLVMHVXLegalizer.so\"";
            //     break;
            // case ARM:
            //     path = "\"/shared/hydride/LLVMARMLegalizer.so\"";
            //     break;
        };
        return path;
    }

    std::string MisaalCompiler::get_llvm_so_flags(){
        std::string flag;
        switch(target){
            case x86:
                flag = "\"-x86-hydride-legalize\"";
                break;
            // case HVX:
            //     flag = "\"-hex-hydride-legalize\"";
            //     break;
            // case ARM:
            //     flag = "\"-arm-hydride-legalize\"";
            //     break;
        };
        return flag;
    }


    std::string MisaalCompiler::get_llvm_intrinsic_wrapper(){
        std::string wrapper;
        switch(target){
            case x86:
                // wrapper = "\"/shared/hydride/x86_wrappers.c.ll\"";
                // CHANGE THIS - SUN
                wrapper = "\"/u/is16/526/Hydride/codegen-generator/targets/x86/x86_wrappers.c.ll\"";
                break;
            // case HVX:
            //     wrapper = "\"/shared/hydride/hvx_wrappers.ll\"";
            //     break;
            // case ARM:
            //     wrapper = "\"/shared/hydride/arm_wrappers.ll\""; 
            //     break;
        };
        return wrapper;
    }


    std::string MisaalCompiler::emit_python_rewrite_file(std::string output_path ,std::string base_name){

        std::vector<std::string> statements;

        // Python Headers for required objects
        std::string common_imports  = get_compiler_python_import();
        statements.push_back(common_imports);

        std::string pattern_alias_input = "misaal_input_patterns";
        if(import_frontend_patterns){
            std::string pattern_imports_input = "from patterns.Halide import Halide_patterns as "+pattern_alias_input;
            statements.push_back(pattern_imports_input);
        } else {
            std::string pattern_imports_input = pattern_alias_input + " = []";
            statements.push_back(pattern_imports_input);
        }

        std::string pattern_alias_output = "misaal_output_patterns";
        std::string pattern_imports_output = get_patterns_import(pattern_alias_output);
        statements.push_back(pattern_imports_output);
        std::string pattern_alias = "misaal_patterns";

        statements.push_back(pattern_alias + " = " + pattern_alias_input + " + " + pattern_alias_output );

        // Parse Input and Output DSL Lists

        std::string input_dsl_name = "misaal_input";
        std::string output_dsl_name = "misaal_output";

        std::string input_dsl_defn = get_input_dsl_list_definition(input_dsl_name);
        std::string output_dsl_defn = get_output_dsl_list_definition(output_dsl_name);

        statements.push_back(input_dsl_defn);
        statements.push_back(output_dsl_defn);


        // LLVM Flags
        std::string wrapper = "so_path = " + get_llvm_so_path();
        std::string flags = "llvm_flags = [" + get_llvm_so_flags() + "]";
        std::string intrinsics = "intrin = " + get_llvm_intrinsic_wrapper();

        statements.push_back(wrapper);
        statements.push_back(flags);
        statements.push_back(intrinsics);

        // Hydride Root 
        statements.push_back("HYDRIDE_ROOT = \""+HYDRIDE_ROOT + "\"");

        std::string test_name = "tests";
        std::string tests_desc = prepare_rewrite_specs(test_name);
        statements.push_back(tests_desc);

        // Exit if no tests to compile
        std::string early_exit = "if len("+test_name+") == 0:\n\tsys.exit(0)";
        statements.push_back(early_exit);
        std::string compiler_name = "misaal_compiler";

        std::string compiler_def = define_misaal_compiler(compiler_name, test_name,  input_dsl_name, output_dsl_name, pattern_alias, output_path);
        statements.push_back(compiler_def);





        return join(statements, "\n");



    };

    std::string MisaalCompiler::define_misaal_compiler(std::string compiler_name, std::string test_name, std::string input_dsl_name, std::string output_dsl_name, std::string pattern_alias, std::string output_path){
        std::vector<std::string> statements;
        statements.push_back("# Defining MISAAL Rewrite compiler");

        std::vector<std::string> params;

        params.push_back(pattern_alias);
        params.push_back("src_dsl_list = " + input_dsl_name);
        params.push_back("target_dsl_list = " + output_dsl_name);
        params.push_back("run_iterations = " + std::to_string(rewrite_iterations));
        params.push_back("egg_pkg_path = EGG_PKG_PATH");
        params.push_back("tests = " + test_name);
        params.push_back("llvm_so_path = so_path");
        params.push_back("llvm_flags =  llvm_flags");
        params.push_back("intrinsics_file =  intrin");
        params.push_back("hydride_root_path =  HYDRIDE_ROOT");
        params.push_back("llvm_out_file_name = \"" + output_path + "\"");

        std::string compiler_defn = compiler_name + " = HydrideCompiler(" + join(params, ", ") + ")"; 

        statements.push_back(compiler_defn);

        // Invoke compiler and print stats
        statements.push_back("# Invoke compiler and print stats");
        statements.push_back(compiler_name + ".compile_hydride()");
        statements.push_back(compiler_name + ".run_llvm_legalizer()");
        statements.push_back(compiler_name + ".print_stats()");

        return join(statements ,"\n");


    }

    std::string MisaalCompiler::prepare_rewrite_specs(std::string test_name){
        std::vector<std::string> statements;
        
        statements.push_back("# Defining Tests ");
        statements.push_back(test_name + " = []");

        for(int i = 0; i < Expressions.size() ; i++){
            std::string base_name = "test_"+std::to_string(i);
            auto CQ = Expressions[i];

            std::string func_name = base_name+"_name";
            std::string func_defn_name = base_name+"_str";

            std::string name_def = func_name + " = \"" + CQ.name +"\"";
            std::string func_def = func_defn_name + " =\"\"\"\n" + CQ.expr + "\n\"\"\"";

            statements.push_back(name_def);
            statements.push_back(func_def);

            statements.push_back(test_name+ ".append((" + func_name + "," + func_defn_name + "))");
        }
        return join(statements, "\n");
    }
}
}
}