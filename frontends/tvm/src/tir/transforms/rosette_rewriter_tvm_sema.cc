
/*!
 *  Extract vectorized code and replace it with an external function call.
 * \file lower_intrin.cc
 */
#include <tvm/runtime/registry.h>
#include <tvm/target/target.h>
#include <tvm/tir/expr.h>
#include <tvm/tir/op.h>
#include <tvm/tir/transform.h>
#include <tvm/tir/builtin.h>

#include <limits>
#include <unordered_set>

#include "../../arith/ir_mutator_with_analyzer.h"
#include "../../arith/pattern_match.h"
#include "../../contrib/misaal/misaal.h"
#include "rosette_rewriter_tvm_sema.h"

namespace tvm {
namespace tir {

    std::string RosetteRewriterTVMSema::print_signed_binary_op(std::string op, std::string a, std::string b, size_t lanes, size_t bits, int sign){
        return "(" + op + "\n" + a + "\n" + b + "\n" + std::to_string(bits) + "\n" + std::to_string(bits * lanes) + "\n" + std::to_string(sign) + ")";
    }

    std::string RosetteRewriterTVMSema::print_binary_op(std::string op, std::string a, std::string b, size_t lanes, size_t bits){
        return "(" + op + "\n" + a + "\n" + b + "\n" + std::to_string(bits) + "\n" + std::to_string(bits * lanes) + ")";
    }

    #define REWRITE_SIGNED_BINOP(Op, RosetteOp) \
    std::string RosetteRewriterTVMSema::Rewrite(const Op##Node* op){ \
        DataType dtype = op->dtype; \
        if (dtype.is_uint()){ \
            return print_signed_binary_op(RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits(), 0); \
        } else if (dtype.is_int()){ \
            return print_signed_binary_op(RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits(), 1); \
        } else { \
            ICHECK(false) << "Trying to rewrite an operation with an unsupported datatype."; \
            exit(0); \
            return ""; \
        } \
    }

    // Addsub has sign -1 and 1 for signed saturating and 0 for unsigned saturating.
    #define REWRITE_ADDSUB(Op, RosetteOp) \
    std::string RosetteRewriterTVMSema::Rewrite(const Op##Node* op){ \
        DataType dtype = op->dtype; \
        return print_signed_binary_op(RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits(), -1); \
    }

    // For comparison ops, use the left child dtype as the input to the s-exp
    #define REWRITE_SIGNED_COMP_BINOP(Op, RosetteOp) \
    std::string RosetteRewriterTVMSema::Rewrite(const Op##Node* op){ \
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
    std::string RosetteRewriterTVMSema::Rewrite(const Op##Node* op){ \
        DataType dtype = op->a->dtype; \
        return print_binary_op(#RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits()); \
    }

    #define REWRITE_BASIC_BINOP(Op, RosetteOp) \
    std::string RosetteRewriterTVMSema::Rewrite(const Op##Node* op){ \
        DataType dtype = op->dtype; \
        return print_binary_op(#RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits()); \
    }

    REWRITE_ADDSUB(Add, "typed-folded:vec-add");
    REWRITE_ADDSUB(Sub, "typed-folded:vec-sub");
    REWRITE_SIGNED_BINOP(Mul, "typed-folded:vec-mul");
    REWRITE_SIGNED_BINOP(Div, "typed-folded:vec-div");
    REWRITE_SIGNED_BINOP(Mod, "typed-folded:vec-mod");
    REWRITE_SIGNED_BINOP(Min, "typed-folded:vec-min");
    REWRITE_SIGNED_BINOP(Max, "typed-folded:vec-max");
    REWRITE_COMP_BINOP(EQ, "typed-folded:vec-eq");
    REWRITE_SIGNED_COMP_BINOP(LT, "typed-folded:vec-lt");
    REWRITE_COMP_BINOP(NE, "typed-folded:vec-ne");
    REWRITE_SIGNED_COMP_BINOP(LE, "typed-folded:vec-le");
    REWRITE_SIGNED_COMP_BINOP(GT, "typed-folded:vec-gt");
    REWRITE_SIGNED_COMP_BINOP(GE, "typed-folded:vec-ge");
    REWRITE_BASIC_BINOP(And, "typed-folded:vec-bwand");

    // Rules for special ops
    std::string RosetteRewriterTVMSema::Rewrite(const CastNode* op){ 
        DataType output_dtype = op->dtype; 
        DataType input_dtype = op->value->dtype;
        size_t iprec = input_dtype.bits();
        size_t isize = iprec * input_dtype.lanes();
        size_t oprec = output_dtype.bits();

        std::string suffix = oprec > iprec ? "-extend" : "-truncate";

        std::string output_str = "(typed-folded:cast" + suffix + " " + MakeString(op->value) + " " +
            std::to_string(iprec) + " " + std::to_string(isize) + " " + std::to_string(oprec) + " ";
        if (oprec > iprec){
            if (input_dtype.is_int()){
                output_str += "1";
            } else if (input_dtype.is_uint()){
                output_str += "0";
            } else {
                ICHECK(false) << "Trying to rewrite an operation with an unsupported datatype."; \
                exit(0); \
                return ""; \
            }
        }
        output_str += ")";
        return output_str;
    }

    std::string RosetteRewriterTVMSema::Rewrite(const RampNode* op){ 
        DataType dtype = op->dtype;
        size_t iprec = dtype.bits();
        size_t osize = dtype.bits() * dtype.lanes();

        // base, stride, iprec, osize
        return "(typed-folded:ramp " + MakeString(op->base) + " " + MakeString(op->stride) + " " + std::to_string(iprec) + " " + std::to_string(osize) + ")";
    }

    std::string RosetteRewriterTVMSema::Rewrite(const BroadcastNode* op){ 
        DataType dtype = op->dtype;
        return "(typed-folded:broadcast " + MakeString(op->value) + " " + std::to_string(dtype.bits()) + " " + std::to_string(dtype.lanes()) + ")";
    }

    // std::string RosetteRewriterTVMSema::CallNodeRewriteHelper(const CallNode* op, std::string RosetteOp){
    //     DataType dtype = op->dtype;
    //     if (dtype.is_uint()){ 
    //         return print_signed_binary_op(RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits(), 0); 
    //     } else if (dtype.is_int()){ 
    //         return print_signed_binary_op(RosetteOp, MakeString(op->a), MakeString(op->b), dtype.lanes(), dtype.bits(), 1); 
    //     } else { 
    //         ICHECK(false) << "Trying to rewrite an operation with an unsupported datatype."; 
    //         exit(0); 
    //         return ""; 
    // }

    std::string RosetteRewriterTVMSema::Rewrite(const CallNode* op) {  
        DataType dtype = op->dtype;
        if (op->op.same_as(builtin::bitwise_or())) {
            return print_binary_op("typed-folded:vec-bwor", MakeString(op->args[0]), MakeString(op->args[1]), dtype.lanes(), dtype.bits());
        } else if (op->op.same_as(builtin::bitwise_and())) {
            return print_binary_op("typed-folded:vec:bwand", MakeString(op->args[0]), MakeString(op->args[1]), dtype.lanes(), dtype.bits());
        } else {
            ICHECK(false) << "Tried to rewrite an unsupported call node."; 
            exit(0);
            return "";
        }
    }

    #define DEFINE_REWRITE_NOT_IMPLEMENTED(Op)                           \
    std::string RosetteRewriterTVMSema::Rewrite(const Op##Node* op){            \
        ICHECK(false) << "Rewrite rule for " << #Op << " is not implemented"; \
        return ""; \
    };

    DEFINE_REWRITE_NOT_IMPLEMENTED(Var);
    DEFINE_REWRITE_NOT_IMPLEMENTED(Or);
    DEFINE_REWRITE_NOT_IMPLEMENTED(IntImm);
    DEFINE_REWRITE_NOT_IMPLEMENTED(FloatImm);
    DEFINE_REWRITE_NOT_IMPLEMENTED(StringImm);
    DEFINE_REWRITE_NOT_IMPLEMENTED(Not);
    DEFINE_REWRITE_NOT_IMPLEMENTED(Select);
    DEFINE_REWRITE_NOT_IMPLEMENTED(Let);
    DEFINE_REWRITE_NOT_IMPLEMENTED(BufferLoad);
    DEFINE_REWRITE_NOT_IMPLEMENTED(Shuffle);

    // Rewrite op if it is vectorizable, otherwise stop rewriting.
    #define DEFINE_VISIT_OP(Op)                                       \
        std::string RosetteRewriterTVMSema::VisitExpr_(const Op##Node* op){    \
            if (misaal::IsVectorizable(op)){                              \
                return Rewrite(op);                                     \
            } else {                                                    \
                std::string arg_name = fresh_arg_name(op->dtype.bits());                \
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

    PrimExpr RosetteRewriterTVMSema::result(DataType result_dtype){
        return Call(result_dtype, builtin::call_pure_extern(), args);
    }

    // bits is the size of the dtype, not the vector
    std::string RosetteRewriterTVMSema::fresh_arg_name(size_t bits){
        return "(reg (bv " + std::to_string(arg_count_++) + " " + std::to_string(bits) + "))";
    }

}  // namespace tir
} // namespace tvm
