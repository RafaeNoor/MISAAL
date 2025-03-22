/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

/*!
 * \file codegen_x86_64.cc
 * \brief X86-64 specific code generator
 */
#ifdef TVM_LLVM_VERSION

#include <llvm/IR/DerivedTypes.h>
#include <llvm/IR/Function.h>
#include <llvm/IR/Intrinsics.h>
#if TVM_LLVM_VERSION >= 100
#include <llvm/IR/IntrinsicsX86.h>
#endif
#include <llvm/Support/Casting.h>
#include <tvm/runtime/registry.h>

#include <string>
#include <vector>

#include "codegen_cpu.h"
#include "llvm_instance.h"

namespace tvm {
namespace codegen {

class CodeGenMISAAL final : public CodeGenCPU {
 public:
  // llvm::Value* VisitExpr_(const VarNode* op) override;
  // llvm::Value* VisitExpr_(const CastNode* op) override;
  // llvm::Value* VisitExpr_(const IntImmNode* op) override;
  // llvm::Value* VisitExpr_(const FloatImmNode* op) override;
  // llvm::Value* VisitExpr_(const StringImmNode* op) override;
  // llvm::Value* VisitExpr_(const AddNode* op) override;
  // llvm::Value* VisitExpr_(const SubNode* op) override;
  // llvm::Value* VisitExpr_(const MulNode* op) override;
  // llvm::Value* VisitExpr_(const DivNode* op) override;
  // llvm::Value* VisitExpr_(const ModNode* op) override;
  // llvm::Value* VisitExpr_(const MinNode* op) override;
  // llvm::Value* VisitExpr_(const MaxNode* op) override;
  // llvm::Value* VisitExpr_(const LTNode* op) override;
  // llvm::Value* VisitExpr_(const LENode* op) override;
  // llvm::Value* VisitExpr_(const GTNode* op) override;
  // llvm::Value* VisitExpr_(const GENode* op) override;
  // llvm::Value* VisitExpr_(const EQNode* op) override;
  // llvm::Value* VisitExpr_(const NENode* op) override;
  // llvm::Value* VisitExpr_(const AndNode* op) override;
  // llvm::Value* VisitExpr_(const OrNode* op) override;
  // llvm::Value* VisitExpr_(const NotNode* op) override;
  // llvm::Value* VisitExpr_(const SelectNode* op) override;
  // llvm::Value* VisitExpr_(const LetNode* op) override;
  // llvm::Value* VisitExpr_(const BufferLoadNode* op) override;
  // llvm::Value* VisitExpr_(const CallNode* op) override;
  // llvm::Value* VisitExpr_(const RampNode* op) override;
  // llvm::Value* VisitExpr_(const ShuffleNode* op) override;
  // llvm::Value* VisitExpr_(const BroadcastNode* op) override;

 private:
};

// llvm::Value* CodeGenMISAAL::VisitExpr_(const AddNode* op){
//   llvm::Value* a_val = MakeValue(op->a);
//   llvm::Value* b_val = MakeValue(op->b);

//   if (op->dtype.is_vector()){
//     std::cerr << "( add "; 
//     std::cerr << std::endl;
//     a_val->dump(); 
//     std::cerr << std::endl;
//     b_val->print(llvm::errs()); 
//     std::cerr << std::endl;
//     std::cerr << ")\n" ; 
//   }

//   return CodeGenCPU::CreateAdd(op->dtype, a_val, b_val);
// }

// llvm::Value* CodeGenMISAAL::VisitExpr_(const VarNode* op){
//   if (op->dtype.is_vector()){
//     std::cerr << "Visiting var: " << op->name_hint << std::endl;
//   }

//   return CodeGenCPU::VisitExpr_(op);
// }

// VISIT_EXPR(VarNode);
// VISIT_EXPR(CastNode);
// VISIT_EXPR(IntImmNode);
// VISIT_EXPR(FloatImmNode);
// VISIT_EXPR(StringImmNode);
// VISIT_EXPR(AddNode);
// VISIT_EXPR(SubNode);
// VISIT_EXPR(MulNode);
// VISIT_EXPR(DivNode);
// VISIT_EXPR(ModNode);
// VISIT_EXPR(MinNode);
// VISIT_EXPR(MaxNode);
// VISIT_EXPR(LTNode);
// VISIT_EXPR(LENode);
// VISIT_EXPR(GTNode);
// VISIT_EXPR(GENode);
// VISIT_EXPR(EQNode);
// VISIT_EXPR(NENode);
// VISIT_EXPR(AndNode);
// VISIT_EXPR(OrNode);
// VISIT_EXPR(NotNode);
// VISIT_EXPR(SelectNode);
// VISIT_EXPR(LetNode);
// VISIT_EXPR(BufferLoadNode);
// VISIT_EXPR(CallNode);
// VISIT_EXPR(RampNode);
// VISIT_EXPR(ShuffleNode);
// VISIT_EXPR(BroadcastNode);


// llvm::Value* CodeGenMISAAL::VisitExpr_(const VarNode* op){
//   if (op->dtype.is_vector()){
//     std::cerr << "Op: " << op->dtype << std::endl;
//   }
//   return CodeGenCPU::VisitExpr_(op);
// }
// llvm::Value* CodeGenMISAAL::CreateAdd(DataType t, llvm::Value* a, llvm::Value* b) { 
//   if (t.is_int()) {                                                               
//     if (t.bits() >= 32) {                                                         
//       return builder_->CreateNSWAdd(a, b);                                        
//     } else {                                                                      
//       return builder_->CreateAdd(a, b);                                           
//     }                                                                             
//   } else if (t.is_uint()) {                                                       
//     if (t.bits() >= 32) {                                                         
//       return builder_->CreateNUWAdd(a, b);                                        
//     } else {                                                                      
//       return builder_->CreateAdd(a, b);                                           
//     }                                                                             
//   } else {                                                                        
//     ICHECK(t.is_float());                                                         
//     return builder_->CreateFAdd(a, b);                                            
//   }                                                                               
// }                                                                                 

// llvm::Value* CodeGenMISAAL::VisitExpr_(const AddNode* op){
//   std::cerr << "Visiting addnode" << std::endl;
//   std::cerr << op->dtype << std::endl;
//   std::cerr << op->a.dtype() << std::endl;
//   std::cerr << op->b.dtype() << std::endl;
//   llvm::Value* left_val = MakeValue(op->a);
//   llvm::Value* right_val = MakeValue(op->b);
//   std::cerr << "Left llvm val: ";
//   left_val->print(llvm::errs());
//   std::cerr << "Right llvm val: ";
//   right_val->print(llvm::errs());
//   std::cerr << std::endl;
//   return CreateAdd(op->dtype, left_val, right_val);
// }

TVM_REGISTER_GLOBAL("tvm.codegen.llvm.misaal")
    .set_body([](const TVMArgs& targs, TVMRetValue* rv) {
      *rv = static_cast<void*>(new CodeGenMISAAL());
    });

}  // namespace codegen
}  // namespace tvm

#endif  // TVM_LLVM_VERSION
