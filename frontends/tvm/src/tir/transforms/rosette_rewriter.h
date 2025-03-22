
/*!
 *  Extract vectorized code and replace it with an external function call.
 * \file lower_intrin.cc
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

namespace tvm {
namespace tir {

    class RosetteRewriter : public ExprFunctor<std::string(const PrimExpr&)> {
        public:
        RosetteRewriter(std::string func_name): args({StringImm(func_name)}){};

        PrimExpr result(DataType result_dtype);
        std::string MakeString(const PrimExpr& e) { return VisitExpr(e); };


        private:
        std::string VisitExpr_(const VarNode* op) override;
        std::string VisitExpr_(const CastNode* op) override;
        std::string VisitExpr_(const IntImmNode* op) override;
        std::string VisitExpr_(const FloatImmNode* op) override;
        std::string VisitExpr_(const StringImmNode* op) override;
        std::string VisitExpr_(const AddNode* op) override;
        std::string VisitExpr_(const SubNode* op) override;
        std::string VisitExpr_(const MulNode* op) override;
        std::string VisitExpr_(const DivNode* op) override;
        std::string VisitExpr_(const ModNode* op) override;
        std::string VisitExpr_(const MinNode* op) override;
        std::string VisitExpr_(const MaxNode* op) override;
        std::string VisitExpr_(const LTNode* op) override;
        std::string VisitExpr_(const LENode* op) override;
        std::string VisitExpr_(const GTNode* op) override;
        std::string VisitExpr_(const GENode* op) override;
        std::string VisitExpr_(const EQNode* op) override;
        std::string VisitExpr_(const NENode* op) override;
        std::string VisitExpr_(const AndNode* op) override;
        std::string VisitExpr_(const OrNode* op) override;
        std::string VisitExpr_(const NotNode* op) override;
        std::string VisitExpr_(const SelectNode* op) override;
        std::string VisitExpr_(const LetNode* op) override;
        std::string VisitExpr_(const BufferLoadNode* op) override;
        std::string VisitExpr_(const CallNode* op) override;
        std::string VisitExpr_(const RampNode* op) override;
        std::string VisitExpr_(const ShuffleNode* op) override;
        std::string VisitExpr_(const BroadcastNode* op) override;

        std::string Rewrite(const VarNode* op);
        std::string Rewrite(const CastNode* op);
        std::string Rewrite(const IntImmNode* op);
        std::string Rewrite(const FloatImmNode* op);
        std::string Rewrite(const StringImmNode* op);
        std::string Rewrite(const AddNode* op);
        std::string Rewrite(const SubNode* op);
        std::string Rewrite(const MulNode* op);
        std::string Rewrite(const DivNode* op);
        std::string Rewrite(const ModNode* op);
        std::string Rewrite(const MinNode* op);
        std::string Rewrite(const MaxNode* op);
        std::string Rewrite(const LTNode* op);
        std::string Rewrite(const LENode* op);
        std::string Rewrite(const GTNode* op);
        std::string Rewrite(const GENode* op);
        std::string Rewrite(const EQNode* op);
        std::string Rewrite(const NENode* op);
        std::string Rewrite(const AndNode* op);
        std::string Rewrite(const OrNode* op);
        std::string Rewrite(const NotNode* op);
        std::string Rewrite(const SelectNode* op);
        std::string Rewrite(const LetNode* op);
        std::string Rewrite(const BufferLoadNode* op);
        std::string Rewrite(const CallNode* op);
        std::string Rewrite(const RampNode* op);
        std::string Rewrite(const ShuffleNode* op);
        std::string Rewrite(const BroadcastNode* op);

        std::string print_binary_op(std::string op, std::string a, std::string b, size_t lanes, size_t bits);
        std::string fresh_arg_name(){
            return "arg_" + std::to_string(++arg_count_);
        }

        /*! \brief maps arguments in the generated function call to prim exprs*/
        Array<PrimExpr> args;

        int arg_count_ = 0;
    };

}  // namespace tir
} // namespace tvm
