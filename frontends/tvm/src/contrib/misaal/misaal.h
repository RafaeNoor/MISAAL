#ifndef MISAAL_H_
#define MISAAL_H_

#include <tvm/tir/expr.h>

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

}
}
}

#endif