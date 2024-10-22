; ModuleID = 'llvm.out.linked.ll'
source_filename = "llvm-link"
target triple = "unknown-unknown-unknown"

define <64 x i32> @hydride.node.test_func(<256 x i8> %arg, <256 x i8> %arg.1) {
entry:
  %0 = bitcast <256 x i8> %arg to <64 x i32>
  %1 = bitcast <256 x i8> %arg.1 to <64 x i32>
  %2 = call <64 x i32> @llvm.hexagon.V6.vaddw.dv.128B(<64 x i32> %0, <64 x i32> %1)
  ret <64 x i32> %2
}

; Function Attrs: nounwind readnone
declare <64 x i32> @llvm.hexagon.V6.vaddw.dv.128B(<64 x i32>, <64 x i32>) #0

attributes #0 = { nounwind readnone }
