
#include "llvm/IR/PassManager.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Instructions.h"
#include "llvm/Pass.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/IRBuilder.h"

using namespace llvm;

namespace {
    struct FusedBitSIMDLegalizer : public ModulePass {
        static char ID;
        FusedBitSIMDLegalizer() : ModulePass(ID) {}

        std::vector<CallInst*> ToErase;

        bool runOnModule(Module &M) override {
            for (Function &F : M) {
                for (BasicBlock &BB : F) {
                    for (Instruction &I : BB) {
                        if (auto *Call = dyn_cast<CallInst>(&I)) {
                            visitCallInst(Call);
                        }
                    }
                }
            }
            for(CallInst* CI : ToErase){
                CI->eraseFromParent();
            }
            return true; // Return true if the pass modifies the IR
        }

        void visitCallInst(CallInst *CI) {
            errs() << "Found call to: ";
            if (Function *CalledFunc = CI->getCalledFunction()) {
                errs() << CalledFunc->getName() << "\n";
                PIMLegalize(CI);

            } else {
                errs() << "Indirect call or intrinsic\n";
            }
        }



        void PIMLegalize(CallInst* CI){
            IRBuilder<> Builder(CI);
            LLVMContext &Context = CI->getContext();
            if((CI->getName() == "test_enum_1_comb_9_fused_pim_op_127")){
                if(((dyn_cast<ConstantInt>(CI->getArgOperand(8))->getSExtValue() == 8) 
                            && (dyn_cast<ConstantInt>(CI->getArgOperand(8))->getSExtValue() == 8))){
                    Builder.SetInsertPoint(CI);
                    Value* v0 = CI->getArgOperand(0);
                    Value* v1 = CI->getArgOperand(1);
                    Value* v2 = CI->getArgOperand(2);
                    Value* v3 = CI->getArgOperand(3);
                    // Creating allocations for vectors
                    AllocaInst *AllocaV0 = Builder.CreateAlloca(v0->getType(), nullptr);
                    // Store v0 into AllocaV0
                    Builder.CreateStore(v0, AllocaV0);
                    Value *Bitcast_AllocaV0 = Builder.CreateBitCast(AllocaV0, Type::getInt8PtrTy(Context));
                    int num_elem_v0 = dyn_cast<FixedVectorType>(v0->getType())->getNumElements();
                    AllocaInst *AllocaV1 = Builder.CreateAlloca(v1->getType(), nullptr);
                    // Store v1 into AllocaV1
                    Builder.CreateStore(v1, AllocaV1);
                    Value *Bitcast_AllocaV1 = Builder.CreateBitCast(AllocaV1, Type::getInt8PtrTy(Context));
                    int num_elem_v1 = dyn_cast<FixedVectorType>(v1->getType())->getNumElements();
                    AllocaInst *AllocaV2 = Builder.CreateAlloca(v2->getType(), nullptr);
                    // Store v2 into AllocaV2
                    Builder.CreateStore(v2, AllocaV2);
                    Value *Bitcast_AllocaV2 = Builder.CreateBitCast(AllocaV2, Type::getInt8PtrTy(Context));
                    int num_elem_v2 = dyn_cast<FixedVectorType>(v2->getType())->getNumElements();
                    AllocaInst *AllocaV3 = Builder.CreateAlloca(v3->getType(), nullptr);
                    // Store v3 into AllocaV3
                    Builder.CreateStore(v3, AllocaV3);
                    Value *Bitcast_AllocaV3 = Builder.CreateBitCast(AllocaV3, Type::getInt8PtrTy(Context));
                    int num_elem_v3 = dyn_cast<FixedVectorType>(v3->getType())->getNumElements();
                    AllocaInst *AllocaV4 = Builder.CreateAlloca(CI->getType(), nullptr);
                    // Store CI into AllocaV4
                    Builder.CreateStore(CI, AllocaV4);
                    Value *Bitcast_AllocaV4 = Builder.CreateBitCast(AllocaV4, Type::getInt8PtrTy(Context));
                    int num_elem_CI = dyn_cast<FixedVectorType>(CI->getType())->getNumElements();
                    // Creating Function Types
                    FunctionType* PimFuncTy = FunctionType::get(Type::getVoidTy(Context), {
                            Type::getInt8PtrTy(Context),
                            Type::getInt64Ty(Context),
                            Type::getInt8PtrTy(Context),
                            Type::getInt64Ty(Context)}, false);
                    Function* PimFunc = CI->getModule()->getFunction("op_func_name");
                    if(!PimFunc)
                        PimFunc = Function::Create(PimFuncTy, Function::ExternalLinkage , "test_enum_1_comb_9_fused_pim_op_127" , CI->getModule());
                    // Generating PIM Call
                    std::vector<Value*> CallParams = {
                        Bitcast_AllocaV0,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v0),
                        Bitcast_AllocaV1,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v1),
                        Bitcast_AllocaV2,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v2),
                        Bitcast_AllocaV3,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v3),
                        Bitcast_AllocaV4,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_CI)};
                    CallInst::Create(PimFunc, CallParams, "pimInst", CI);
                    Value *return_bitcast = Builder.CreateBitCast(Bitcast_AllocaV4, CI->getType());
                    Value *VecValue = Builder.CreateLoad(CI->getType(), return_bitcast);
                    CI->replaceAllUsesWith(VecValue);
                    ToErase.push_back(CI);
                }
                if(((dyn_cast<ConstantInt>(CI->getArgOperand(8))->getSExtValue() == 16) 
                            && (dyn_cast<ConstantInt>(CI->getArgOperand(8))->getSExtValue() == 16))){
                    Builder.SetInsertPoint(CI);
                    Value* v0 = CI->getArgOperand(0);
                    Value* v1 = CI->getArgOperand(1);
                    Value* v2 = CI->getArgOperand(2);
                    Value* v3 = CI->getArgOperand(3);
                    // Creating allocations for vectors
                    AllocaInst *AllocaV0 = Builder.CreateAlloca(v0->getType(), nullptr);
                    // Store v0 into AllocaV0
                    Builder.CreateStore(v0, AllocaV0);
                    Value *Bitcast_AllocaV0 = Builder.CreateBitCast(AllocaV0, Type::getInt8PtrTy(Context));
                    int num_elem_v0 = dyn_cast<FixedVectorType>(v0->getType())->getNumElements();
                    AllocaInst *AllocaV1 = Builder.CreateAlloca(v1->getType(), nullptr);
                    // Store v1 into AllocaV1
                    Builder.CreateStore(v1, AllocaV1);
                    Value *Bitcast_AllocaV1 = Builder.CreateBitCast(AllocaV1, Type::getInt8PtrTy(Context));
                    int num_elem_v1 = dyn_cast<FixedVectorType>(v1->getType())->getNumElements();
                    AllocaInst *AllocaV2 = Builder.CreateAlloca(v2->getType(), nullptr);
                    // Store v2 into AllocaV2
                    Builder.CreateStore(v2, AllocaV2);
                    Value *Bitcast_AllocaV2 = Builder.CreateBitCast(AllocaV2, Type::getInt8PtrTy(Context));
                    int num_elem_v2 = dyn_cast<FixedVectorType>(v2->getType())->getNumElements();
                    AllocaInst *AllocaV3 = Builder.CreateAlloca(v3->getType(), nullptr);
                    // Store v3 into AllocaV3
                    Builder.CreateStore(v3, AllocaV3);
                    Value *Bitcast_AllocaV3 = Builder.CreateBitCast(AllocaV3, Type::getInt8PtrTy(Context));
                    int num_elem_v3 = dyn_cast<FixedVectorType>(v3->getType())->getNumElements();
                    AllocaInst *AllocaV4 = Builder.CreateAlloca(CI->getType(), nullptr);
                    // Store CI into AllocaV4
                    Builder.CreateStore(CI, AllocaV4);
                    Value *Bitcast_AllocaV4 = Builder.CreateBitCast(AllocaV4, Type::getInt8PtrTy(Context));
                    int num_elem_CI = dyn_cast<FixedVectorType>(CI->getType())->getNumElements();
                    // Creating Function Types
                    FunctionType* PimFuncTy = FunctionType::get(Type::getVoidTy(Context), {
                            Type::getInt8PtrTy(Context),
                            Type::getInt64Ty(Context),
                            Type::getInt8PtrTy(Context),
                            Type::getInt64Ty(Context)}, false);
                    Function* PimFunc = CI->getModule()->getFunction("op_func_name");
                    if(!PimFunc)
                        PimFunc = Function::Create(PimFuncTy, Function::ExternalLinkage , "test_enum_1_comb_7_fused_pim_op_207" , CI->getModule());
                    // Generating PIM Call
                    std::vector<Value*> CallParams = {
                        Bitcast_AllocaV0,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v0),
                        Bitcast_AllocaV1,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v1),
                        Bitcast_AllocaV2,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v2),
                        Bitcast_AllocaV3,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v3),
                        Bitcast_AllocaV4,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_CI)};
                    CallInst::Create(PimFunc, CallParams, "pimInst", CI);
                    Value *return_bitcast = Builder.CreateBitCast(Bitcast_AllocaV4, CI->getType());
                    Value *VecValue = Builder.CreateLoad(CI->getType(), return_bitcast);
                    CI->replaceAllUsesWith(VecValue);
                    ToErase.push_back(CI);
                }
                if(((dyn_cast<ConstantInt>(CI->getArgOperand(8))->getSExtValue() == 32) 
                            && (dyn_cast<ConstantInt>(CI->getArgOperand(8))->getSExtValue() == 32))){
                    Builder.SetInsertPoint(CI);
                    Value* v0 = CI->getArgOperand(0);
                    Value* v1 = CI->getArgOperand(1);
                    Value* v2 = CI->getArgOperand(2);
                    Value* v3 = CI->getArgOperand(3);
                    // Creating allocations for vectors
                    AllocaInst *AllocaV0 = Builder.CreateAlloca(v0->getType(), nullptr);
                    // Store v0 into AllocaV0
                    Builder.CreateStore(v0, AllocaV0);
                    Value *Bitcast_AllocaV0 = Builder.CreateBitCast(AllocaV0, Type::getInt8PtrTy(Context));
                    int num_elem_v0 = dyn_cast<FixedVectorType>(v0->getType())->getNumElements();
                    AllocaInst *AllocaV1 = Builder.CreateAlloca(v1->getType(), nullptr);
                    // Store v1 into AllocaV1
                    Builder.CreateStore(v1, AllocaV1);
                    Value *Bitcast_AllocaV1 = Builder.CreateBitCast(AllocaV1, Type::getInt8PtrTy(Context));
                    int num_elem_v1 = dyn_cast<FixedVectorType>(v1->getType())->getNumElements();
                    AllocaInst *AllocaV2 = Builder.CreateAlloca(v2->getType(), nullptr);
                    // Store v2 into AllocaV2
                    Builder.CreateStore(v2, AllocaV2);
                    Value *Bitcast_AllocaV2 = Builder.CreateBitCast(AllocaV2, Type::getInt8PtrTy(Context));
                    int num_elem_v2 = dyn_cast<FixedVectorType>(v2->getType())->getNumElements();
                    AllocaInst *AllocaV3 = Builder.CreateAlloca(v3->getType(), nullptr);
                    // Store v3 into AllocaV3
                    Builder.CreateStore(v3, AllocaV3);
                    Value *Bitcast_AllocaV3 = Builder.CreateBitCast(AllocaV3, Type::getInt8PtrTy(Context));
                    int num_elem_v3 = dyn_cast<FixedVectorType>(v3->getType())->getNumElements();
                    AllocaInst *AllocaV4 = Builder.CreateAlloca(CI->getType(), nullptr);
                    // Store CI into AllocaV4
                    Builder.CreateStore(CI, AllocaV4);
                    Value *Bitcast_AllocaV4 = Builder.CreateBitCast(AllocaV4, Type::getInt8PtrTy(Context));
                    int num_elem_CI = dyn_cast<FixedVectorType>(CI->getType())->getNumElements();
                    // Creating Function Types
                    FunctionType* PimFuncTy = FunctionType::get(Type::getVoidTy(Context), {
                            Type::getInt8PtrTy(Context),
                            Type::getInt64Ty(Context),
                            Type::getInt8PtrTy(Context),
                            Type::getInt64Ty(Context)}, false);
                    Function* PimFunc = CI->getModule()->getFunction("op_func_name");
                    if(!PimFunc)
                        PimFunc = Function::Create(PimFuncTy, Function::ExternalLinkage , "test_enum_1_comb_11_fused_pim_op_211" , CI->getModule());
                    // Generating PIM Call
                    std::vector<Value*> CallParams = {
                        Bitcast_AllocaV0,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v0),
                        Bitcast_AllocaV1,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v1),
                        Bitcast_AllocaV2,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v2),
                        Bitcast_AllocaV3,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v3),
                        Bitcast_AllocaV4,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_CI)};
                    CallInst::Create(PimFunc, CallParams, "pimInst", CI);
                    Value *return_bitcast = Builder.CreateBitCast(Bitcast_AllocaV4, CI->getType());
                    Value *VecValue = Builder.CreateLoad(CI->getType(), return_bitcast);
                    CI->replaceAllUsesWith(VecValue);
                    ToErase.push_back(CI);
                }
            }

            if((CI->getName() == "test_enum_1_comb_7_fused_pim_op_487")){
                if(((dyn_cast<ConstantInt>(CI->getArgOperand(6))->getSExtValue() == 8) 
                            && (dyn_cast<ConstantInt>(CI->getArgOperand(7))->getSExtValue() == 16))){
                    Builder.SetInsertPoint(CI);
                    Value* v0 = CI->getArgOperand(0);
                    Value* v1 = CI->getArgOperand(1);
                    // Creating allocations for vectors
                    AllocaInst *AllocaV0 = Builder.CreateAlloca(v0->getType(), nullptr);
                    // Store v0 into AllocaV0
                    Builder.CreateStore(v0, AllocaV0);
                    Value *Bitcast_AllocaV0 = Builder.CreateBitCast(AllocaV0, Type::getInt8PtrTy(Context));
                    int num_elem_v0 = dyn_cast<FixedVectorType>(v0->getType())->getNumElements();
                    AllocaInst *AllocaV1 = Builder.CreateAlloca(v1->getType(), nullptr);
                    // Store v1 into AllocaV1
                    Builder.CreateStore(v1, AllocaV1);
                    Value *Bitcast_AllocaV1 = Builder.CreateBitCast(AllocaV1, Type::getInt8PtrTy(Context));
                    int num_elem_v1 = dyn_cast<FixedVectorType>(v1->getType())->getNumElements();
                    AllocaInst *AllocaV2 = Builder.CreateAlloca(CI->getType(), nullptr);
                    // Store CI into AllocaV2
                    Builder.CreateStore(CI, AllocaV2);
                    Value *Bitcast_AllocaV2 = Builder.CreateBitCast(AllocaV2, Type::getInt8PtrTy(Context));
                    int num_elem_CI = dyn_cast<FixedVectorType>(CI->getType())->getNumElements();
                    // Creating Function Types
                    FunctionType* PimFuncTy = FunctionType::get(Type::getVoidTy(Context), {
                            Type::getInt8PtrTy(Context),
                            Type::getInt64Ty(Context),
                            Type::getInt8PtrTy(Context),
                            Type::getInt64Ty(Context)}, false);
                    Function* PimFunc = CI->getModule()->getFunction("op_func_name");
                    if(!PimFunc)
                        PimFunc = Function::Create(PimFuncTy, Function::ExternalLinkage , "test_enum_1_comb_7_fused_pim_op_487" , CI->getModule());
                    // Generating PIM Call
                    std::vector<Value*> CallParams = {
                        Bitcast_AllocaV0,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v0),
                        Bitcast_AllocaV1,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v1),
                        Bitcast_AllocaV2,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_CI)};
                    CallInst::Create(PimFunc, CallParams, "pimInst", CI);
                    Value *return_bitcast = Builder.CreateBitCast(Bitcast_AllocaV2, CI->getType());
                    Value *VecValue = Builder.CreateLoad(CI->getType(), return_bitcast);
                    CI->replaceAllUsesWith(VecValue);
                    ToErase.push_back(CI);
                }
                if(((dyn_cast<ConstantInt>(CI->getArgOperand(6))->getSExtValue() == 16) 
                            && (dyn_cast<ConstantInt>(CI->getArgOperand(7))->getSExtValue() == 32))){
                    Builder.SetInsertPoint(CI);
                    Value* v0 = CI->getArgOperand(0);
                    Value* v1 = CI->getArgOperand(1);
                    // Creating allocations for vectors
                    AllocaInst *AllocaV0 = Builder.CreateAlloca(v0->getType(), nullptr);
                    // Store v0 into AllocaV0
                    Builder.CreateStore(v0, AllocaV0);
                    Value *Bitcast_AllocaV0 = Builder.CreateBitCast(AllocaV0, Type::getInt8PtrTy(Context));
                    int num_elem_v0 = dyn_cast<FixedVectorType>(v0->getType())->getNumElements();
                    AllocaInst *AllocaV1 = Builder.CreateAlloca(v1->getType(), nullptr);
                    // Store v1 into AllocaV1
                    Builder.CreateStore(v1, AllocaV1);
                    Value *Bitcast_AllocaV1 = Builder.CreateBitCast(AllocaV1, Type::getInt8PtrTy(Context));
                    int num_elem_v1 = dyn_cast<FixedVectorType>(v1->getType())->getNumElements();
                    AllocaInst *AllocaV2 = Builder.CreateAlloca(CI->getType(), nullptr);
                    // Store CI into AllocaV2
                    Builder.CreateStore(CI, AllocaV2);
                    Value *Bitcast_AllocaV2 = Builder.CreateBitCast(AllocaV2, Type::getInt8PtrTy(Context));
                    int num_elem_CI = dyn_cast<FixedVectorType>(CI->getType())->getNumElements();
                    // Creating Function Types
                    FunctionType* PimFuncTy = FunctionType::get(Type::getVoidTy(Context), {
                            Type::getInt8PtrTy(Context),
                            Type::getInt64Ty(Context),
                            Type::getInt8PtrTy(Context),
                            Type::getInt64Ty(Context)}, false);
                    Function* PimFunc = CI->getModule()->getFunction("op_func_name");
                    if(!PimFunc)
                        PimFunc = Function::Create(PimFuncTy, Function::ExternalLinkage , "test_enum_1_comb_8_fused_pim_op_478" , CI->getModule());
                    // Generating PIM Call
                    std::vector<Value*> CallParams = {
                        Bitcast_AllocaV0,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v0),
                        Bitcast_AllocaV1,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_v1),
                        Bitcast_AllocaV2,
                        ConstantInt::get(Type::getInt64Ty(Context), num_elem_CI)};
                    CallInst::Create(PimFunc, CallParams, "pimInst", CI);
                    Value *return_bitcast = Builder.CreateBitCast(Bitcast_AllocaV2, CI->getType());
                    Value *VecValue = Builder.CreateLoad(CI->getType(), return_bitcast);
                    CI->replaceAllUsesWith(VecValue);
                    ToErase.push_back(CI);
                }
            }

        }

    };
} // namespace

char FusedBitSIMDLegalizer::ID = 0;

// Register the pass with LLVM so it can be invoked with `opt`
static RegisterPass<FusedBitSIMDLegalizer>
X("pim-fuse-legalize", "Lower Fused PIM operations to invoke the implementation of fused in PIMEval", false, false);



