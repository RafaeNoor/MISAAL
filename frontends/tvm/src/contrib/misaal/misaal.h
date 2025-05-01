#ifndef MISAAL_H_
#define MISAAL_H_

#include <tvm/tir/expr.h>
#include <iostream>
#include <vector>
#include <stdlib.h>
#include <assert.h>

namespace tvm {
namespace tir {
namespace misaal {

bool IsVectorizable(const tir::SubNode* op);
bool IsVectorizable(const tir::MulNode* op);
bool IsVectorizable(const tir::DivNode* op);
bool IsVectorizable(const tir::ModNode* op);
bool IsVectorizable(const tir::MinNode* op);
bool IsVectorizable(const tir::MaxNode* op);
bool IsVectorizable(const tir::LTNode* op);
bool IsVectorizable(const tir::LENode* op);
bool IsVectorizable(const tir::GTNode* op);
bool IsVectorizable(const tir::GENode* op);
bool IsVectorizable(const tir::EQNode* op);
bool IsVectorizable(const tir::NENode* op);
bool IsVectorizable(const tir::OrNode* op);
bool IsVectorizable(const tir::AndNode* op);
bool IsVectorizable(const tir::AddNode* op);
bool IsVectorizable(const tir::VarNode* op);
bool IsVectorizable(const tir::CastNode* op);
bool IsVectorizable(const tir::IntImmNode* op);
bool IsVectorizable(const tir::FloatImmNode* op);
bool IsVectorizable(const tir::StringImmNode* op);
bool IsVectorizable(const tir::NotNode* op);
bool IsVectorizable(const tir::SelectNode* op);
bool IsVectorizable(const tir::LetNode* op);
bool IsVectorizable(const tir::BufferLoadNode* op);
bool IsVectorizable(const tir::CallNode* op);
bool IsVectorizable(const tir::RampNode* op);
bool IsVectorizable(const tir::ShuffleNode* op);
bool IsVectorizable(const tir::BroadcastNode* op);

    enum TARGET {
        x86,
        // Not supported
        // HVX,
        // ARM,
        // Halide
    };

    struct CompilerQuery {
        std::string expr;
        std::string name;
        CompilerQuery(std::string e, std::string n) : expr(e), name(n) {}

    };

    class MisaalCompiler {
        public:

            MisaalCompiler(TARGET t) : target(t) {
                const char* MISAAL_PATH = std::getenv("MISAAL_SRC");
                assert(MISAAL_PATH && "MISAAL_SRC path not defined");
                const char* HYDRIDE_PATH = std::getenv("HYDRIDE_ROOT");
                assert(HYDRIDE_PATH && "HYDRIDE_ROOT path not defined");
                MISAAL_ROOT = MISAAL_PATH;
                HYDRIDE_ROOT = HYDRIDE_PATH;

                const char* MISAAL_DISABLE_FRONTEND_PATTERNS = std::getenv("MISAAL_DISABLE_FRONTEND_PATTERNS");  
                import_frontend_patterns = !(MISAAL_DISABLE_FRONTEND_PATTERNS);
                const char* MISAAL_EQ_SAT_ITERS = std::getenv("MISAAL_EQ_SAT_ITERS");  
                if(MISAAL_EQ_SAT_ITERS){
                    rewrite_iterations = std::stoi(MISAAL_EQ_SAT_ITERS);
                }

            }
            void add_expression_to_compile(std::string expr, std::string name);
            void compile_expression(std::string output_bitcode_path, std::string benchmark);



        private:

            void execute_python_file(std::string fname);
            std::string get_compiler_python_import();
            std::string parse_dict(std::string output_name, std::string dict_name);
            std::string join(std::vector<std::string>& statements, std::string join_on);
            std::string get_input_dsl_list_definition(std::string input_dsl_name);
            std::string get_output_dsl_list_definition(std::string output_dsl_name);
            std::string get_patterns_import(std::string pattern_alias);
            std::string get_llvm_so_path();
            std::string get_llvm_so_flags();
            std::string get_llvm_intrinsic_wrapper();
            std::string emit_python_rewrite_file(std::string output_path, std::string base_name);
            void write_to_file(std::string fname, std::string content);

            std::string prepare_rewrite_specs(std::string test_name);
            std::string define_misaal_compiler(std::string compiler_name, std::string test_name, std::string input_dsl_name, std::string output_dsl_name, std::string pattern_alias, std::string output_path);


            TARGET target;
            std::string MISAAL_ROOT;
            std::string HYDRIDE_ROOT;

            std::vector<CompilerQuery> Expressions;

            int rewrite_iterations = 5;

            bool import_frontend_patterns = true;


    };
}
}
}

#endif