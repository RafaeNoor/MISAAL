
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

    std::string RosetteRewriter::print_signed_binary_op(std::string op, std::string a, std::string b, size_t lanes, size_t bits, int sign){
        return "(" + op + "\n" + a + "\n" + b + "\n" + std::to_string(bits) + "\n" + std::to_string(bits * lanes) + "\n" + std::to_string(sign) + ")";
    }

    std::string RosetteRewriter::print_binary_op(std::string op, std::string a, std::string b, size_t lanes, size_t bits){
        return "(" + op + "\n" + a + "\n" + b + "\n" + std::to_string(bits) + "\n" + std::to_string(bits * lanes) + ")";
    }

    #define REWRITE_SIGNED_BINOP(Op, RosetteOp) \
    std::string RosetteRewriter::Rewrite(const Op##Node* op){ \
        DataType dtype = op->dtype; \
        if (dtype.is_uint()){ \
            return print_signed_binary_op(#RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits(), 0); \
        } else if (dtype.is_int()){ \
            return print_signed_binary_op(#RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits(), 1); \
        } else { \
            ICHECK(false) << "Trying to rewrite an operation with an unsupported datatype."; \
            exit(0); \
            return ""; \
        } \
    }

    // For comparison ops, use the left child dtype as the input to the s-exp
    #define REWRITE_SIGNED_COMP_BINOP(Op, RosetteOp) \
    std::string RosetteRewriter::Rewrite(const Op##Node* op){ \
        DataType dtype = op->a->dtype; \
        if (dtype.is_uint()){ \
            return print_signed_binary_op(#RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits(), 0); \
        } else if (dtype.is_int()){ \
            return print_signed_binary_op(#RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits(), 1); \
        } else { \
            ICHECK(false) << "Trying to rewrite an operation with an unsupported datatype."; \
            exit(0); \
            return ""; \
        } \
    }

    // For comparison ops, use the left child dtype as the input to s-exp
    #define REWRITE_COMP_BINOP(Op, RosetteOp) \
    std::string RosetteRewriter::Rewrite(const Op##Node* op){ \
        DataType dtype = op->a->dtype; \
        return print_binary_op(#RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits()); \
    }

    #define REWRITE_BASIC_BINOP(Op, RosetteOp) \
    std::string RosetteRewriter::Rewrite(const Op##Node* op){ \
        DataType dtype = op->dtype; \
        return print_binary_op(#RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits()); \
    }

    REWRITE_SIGNED_BINOP(Add, "vec-add");
    REWRITE_SIGNED_BINOP(Sub, "vec-sub");
    REWRITE_SIGNED_BINOP(Mul, "vec-mul");
    REWRITE_SIGNED_BINOP(Div, "vec-div");
    REWRITE_SIGNED_BINOP(Mod, "vec-mod");
    REWRITE_SIGNED_BINOP(Min, "vec-min");
    REWRITE_SIGNED_BINOP(Max, "vec-max");
    REWRITE_COMP_BINOP(EQ, "vec-eq");
    REWRITE_SIGNED_COMP_BINOP(LT, "vec-lt");
    REWRITE_COMP_BINOP(NE, "vec-ne");
    REWRITE_SIGNED_COMP_BINOP(LE, "vec-le");
    REWRITE_SIGNED_COMP_BINOP(GT, "vec-gt");
    REWRITE_SIGNED_COMP_BINOP(GE, "vec-ge");
    REWRITE_BASIC_BINOP(And, "vec-bwand");
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
    #define DEFINE_VISIT_OP(Op)                                       \
        std::string RosetteRewriter::VisitExpr_(const Op##Node* op){    \
            if (misaal::IsVectorizable(op)){                              \
                return Rewrite(op);                                     \
            } else {                                                    \
                std::string arg_name = fresh_arg_name();                \
                args.push_back(GetRef<PrimExpr>(op));                   \
                return arg_name;                                        \
            }                                                           \
        }

    DEFINE_VISIT_OP(Var);
    DEFINE_VISIT_OP(Cast);
    DEFINE_VISIT_OP(IntImm);
    DEFINE_VISIT_OP(FloatImm);
    DEFINE_VISIT_OP(StringImm);
    DEFINE_VISIT_OP(Sub);
    DEFINE_VISIT_OP(Mul);
    DEFINE_VISIT_OP(Div);
    DEFINE_VISIT_OP(Mod);
    DEFINE_VISIT_OP(Min);
    DEFINE_VISIT_OP(Max);
    DEFINE_VISIT_OP(LT);
    DEFINE_VISIT_OP(LE);
    DEFINE_VISIT_OP(GT);
    DEFINE_VISIT_OP(GE);
    DEFINE_VISIT_OP(EQ);
    DEFINE_VISIT_OP(NE);
    DEFINE_VISIT_OP(And);
    DEFINE_VISIT_OP(Or);
    DEFINE_VISIT_OP(Not);
    DEFINE_VISIT_OP(Select);
    DEFINE_VISIT_OP(Let);
    DEFINE_VISIT_OP(BufferLoad);
    DEFINE_VISIT_OP(Call);
    DEFINE_VISIT_OP(Add);
    DEFINE_VISIT_OP(Ramp);
    DEFINE_VISIT_OP(Shuffle);
    DEFINE_VISIT_OP(Broadcast);

    PrimExpr RosetteRewriter::result(DataType result_dtype){
        return Call(result_dtype, builtin::call_pure_extern(), args);
    }

}  // namespace tir
} // namespace tvm
