
/*!
 *  Extract vectorized code and replace it with an external function call.
 * \file inject_misaal.cc
 */
#include <tvm/runtime/registry.h>
#include <tvm/target/target.h>
#include <tvm/tir/expr.h>
#include <tvm/tir/op.h>
#include <tvm/tir/transform.h>

#include <limits>
#include <unordered_set>

#include "../../arith/ir_mutator_with_analyzer.h"
#include "../../arith/pattern_match.h"
#include "../../contrib/misaal/misaal.h"
#include "rosette_rewriter.h"

namespace tvm {
namespace tir {

class MisaalInjecter : public tvm::arith::IRMutatorWithAnalyzer {
    public:
    using IRMutatorWithAnalyzer::VisitExpr_;
    using IRMutatorWithAnalyzer::VisitStmt_;

    MisaalInjecter(arith::Analyzer* analyzer, std::string target, std::string mtriple)
        : IRMutatorWithAnalyzer(analyzer) {
        // ICHECK(!mtriple.empty()) << "mtriple not specified.";
        // ICHECK(mtriple.find("x86") != std::string::npos) << "Misaal implemented only for target x86";
    }

    #define DEFINE_OP(Op) \
    PrimExpr VisitExpr_(const Op##Node* op) override { \
        if (misaal::IsVectorizable(op)){ \
            std::string func_id = generate_fresh_func_id(); \
            RosetteRewriter rewriter(func_id); \
            rosette_funcs_[func_id] = rewriter(GetRef<PrimExpr>(op)); \
            return rewriter.result(op->dtype); \
        } \
        return IRMutatorWithAnalyzer::VisitExpr_(op); \
    }

    DEFINE_OP(Var);
    DEFINE_OP(Cast);
    DEFINE_OP(IntImm);
    DEFINE_OP(FloatImm);
    DEFINE_OP(StringImm);
    DEFINE_OP(Add);
    DEFINE_OP(Sub);
    DEFINE_OP(Mul);
    DEFINE_OP(Div);
    DEFINE_OP(Mod);
    DEFINE_OP(Min);
    DEFINE_OP(Max);
    DEFINE_OP(LT);
    DEFINE_OP(LE);
    DEFINE_OP(GT);
    DEFINE_OP(GE);
    DEFINE_OP(EQ);
    DEFINE_OP(NE);
    DEFINE_OP(And);
    DEFINE_OP(Or);
    DEFINE_OP(Not);
    DEFINE_OP(Select);
    DEFINE_OP(Let);
    DEFINE_OP(BufferLoad);
    DEFINE_OP(Call);
    DEFINE_OP(Ramp);
    DEFINE_OP(Shuffle);
    DEFINE_OP(Broadcast);

    void PrintGeneratedFunctions(){
        for (auto& pair : rosette_funcs_){
            std::cout << "==\n" << pair.first << ":\n" << pair.second << std::endl;
        }
    }

    private: 
    int func_counter_ = 0;

    std::string generate_fresh_func_id(){
        return "misaal_func_" + std::to_string(func_counter_++);
    }

    /*! \brief Maps function identifiers to rosette expressions */
    std::map<std::string, std::string> rosette_funcs_;

};

namespace transform {

Pass InjectMisaal() {
    auto pass_func = [](PrimFunc f, IRModule m, PassContext ctx){
        auto* n = f.CopyOnWrite();
        auto target = f->GetAttr<Target>(tvm::attr::kTarget);
        ICHECK(target.defined()) << "InjectMisaal: Require the target attribute";
        arith::Analyzer analyzer;
        auto mtriple = target.value()->GetAttr<runtime::String>("mtriple", "");
        MisaalInjecter misaal_injecter(&analyzer, target.value()->kind->name, mtriple.value());
        n->body = misaal_injecter(std::move(n->body));
        misaal_injecter.PrintGeneratedFunctions();
        return f;
    };
    return CreatePrimFuncPass(pass_func, 0, "misaal.InjectMisaal", {});
}

TVM_REGISTER_GLOBAL("tir.transform.InjectMisaal").set_body_typed(InjectMisaal);

}


}  // namespace tir
} // namespace tvm
