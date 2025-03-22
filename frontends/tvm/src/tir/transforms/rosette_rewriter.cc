
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
#include "../../contrib/misaal/misaal.h"
#include "rosette_rewriter.h"

namespace tvm {
namespace tir {

    std::string RosetteRewriter::print_binary_op(std::string op, std::string a, std::string b, size_t lanes, size_t bits){
        return "(" + op + "\n" + a + "\n" + b + "\n" + std::to_string(bits) + "\n" + std::to_string(bits * lanes) + ")";
    }
    #define REWRITE_BASIC_BINOP(Op, RosetteOp) \
    std::string RosetteRewriter::Rewrite(const Op##Node* op){ \
        DataType dtype = op->dtype; \
        return print_binary_op(#RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits()); \
    }

    REWRITE_BASIC_BINOP(Add, "vec-add");
    REWRITE_BASIC_BINOP(Sub, "vec-sub");
    REWRITE_BASIC_BINOP(Mul, "vec-mul");
    REWRITE_BASIC_BINOP(Div, "vec-div");
    REWRITE_BASIC_BINOP(Mod, "vec-mod");
    REWRITE_BASIC_BINOP(Min, "vec-min");
    REWRITE_BASIC_BINOP(Max, "vec-max");
    REWRITE_BASIC_BINOP(EQ, "vec-eq");
    REWRITE_BASIC_BINOP(LT, "vec-lt");
    REWRITE_BASIC_BINOP(NE, "vec-ne");
    REWRITE_BASIC_BINOP(LE, "vec-le");
    REWRITE_BASIC_BINOP(GT, "vec-gt");
    REWRITE_BASIC_BINOP(GE, "vec-ge");
    REWRITE_BASIC_BINOP(And, "vec-and");
    REWRITE_BASIC_BINOP(Or, "vec-or");



    #define DEFINE_REWRITE_NOT_IMPLEMENTED(Op)                           \
    std::string RosetteRewriter::Rewrite(const Op##Node* op){            \
        ICHECK(false) << "Rewrite rule for " << #Op << " is not implemented"; \  
        return ""; \
    };

    DEFINE_REWRITE_NOT_IMPLEMENTED(Var);
    DEFINE_REWRITE_NOT_IMPLEMENTED(Cast);
    DEFINE_REWRITE_NOT_IMPLEMENTED(IntImm);
    DEFINE_REWRITE_NOT_IMPLEMENTED(FloatImm);
    DEFINE_REWRITE_NOT_IMPLEMENTED(StringImm);
    DEFINE_REWRITE_NOT_IMPLEMENTED(Not);
    DEFINE_REWRITE_NOT_IMPLEMENTED(Select);
    DEFINE_REWRITE_NOT_IMPLEMENTED(Let);
    DEFINE_REWRITE_NOT_IMPLEMENTED(BufferLoad);
    DEFINE_REWRITE_NOT_IMPLEMENTED(Call);
    DEFINE_REWRITE_NOT_IMPLEMENTED(Ramp);
    DEFINE_REWRITE_NOT_IMPLEMENTED(Shuffle);
    DEFINE_REWRITE_NOT_IMPLEMENTED(Broadcast);


    // Rewrite op if it is vectorizable, otherwise stop rewriting.
    #define DEFINE_REWRITE_OP(Op)                                       \
        std::string RosetteRewriter::VisitExpr_(const Op##Node* op){    \
            if (misaal::IsVectorizable(op)){                              \
                return Rewrite(op);                                     \
            } else {                                                    \
                std::string arg_name = fresh_arg_name();                \
                args.push_back(GetRef<PrimExpr>(op));                   \
                return arg_name;                                        \
            }                                                           \
        }

    DEFINE_REWRITE_OP(Var);
    DEFINE_REWRITE_OP(Cast);
    DEFINE_REWRITE_OP(IntImm);
    DEFINE_REWRITE_OP(FloatImm);
    DEFINE_REWRITE_OP(StringImm);
    DEFINE_REWRITE_OP(Sub);
    DEFINE_REWRITE_OP(Mul);
    DEFINE_REWRITE_OP(Div);
    DEFINE_REWRITE_OP(Mod);
    DEFINE_REWRITE_OP(Min);
    DEFINE_REWRITE_OP(Max);
    DEFINE_REWRITE_OP(LT);
    DEFINE_REWRITE_OP(LE);
    DEFINE_REWRITE_OP(GT);
    DEFINE_REWRITE_OP(GE);
    DEFINE_REWRITE_OP(EQ);
    DEFINE_REWRITE_OP(NE);
    DEFINE_REWRITE_OP(And);
    DEFINE_REWRITE_OP(Or);
    DEFINE_REWRITE_OP(Not);
    DEFINE_REWRITE_OP(Select);
    DEFINE_REWRITE_OP(Let);
    DEFINE_REWRITE_OP(BufferLoad);
    DEFINE_REWRITE_OP(Call);
    DEFINE_REWRITE_OP(Add);
    DEFINE_REWRITE_OP(Ramp);
    DEFINE_REWRITE_OP(Shuffle);
    DEFINE_REWRITE_OP(Broadcast);

    PrimExpr RosetteRewriter::result(DataType result_dtype){
        return Call(result_dtype, builtin::call_extern(), args);
    }

}  // namespace tir
} // namespace tvm
