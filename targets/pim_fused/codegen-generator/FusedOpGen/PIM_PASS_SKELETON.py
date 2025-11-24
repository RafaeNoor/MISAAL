LOWERING_PASS_SKELETON_TOP = """
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
      errs() << CalledFunc->getName() << "\\n";
      PIMLegalize(CI);

    } else {
      errs() << "Indirect call or intrinsic\\n";
    }
  }


"""



LOWERING_PASS_SKELETON_BOTTOM = """
};
} // namespace

char FusedBitSIMDLegalizer::ID = 0;

// Register the pass with LLVM so it can be invoked with `opt`
static RegisterPass<FusedBitSIMDLegalizer>
    X("pim-fuse-legalize", "Lower Fused PIM operations to invoke the implementation of fused in PIMEval", false, false);



"""
