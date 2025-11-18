#============================== Hydride File =================================
#
# Part of the Hydride Compiler Infrastructure. 
# <Placeholder for license information> 
#
#=============================================================================
#
# Do NOT modify this file. It is automatically generated. 
#
#=============================================================================




semantcs = {

            "x86_swizzle_1" : {
              "target_instructions" : {
                "x86_swizzle_1" : {
                  "args" : ["SYMBOLIC_BV_512","SYMBOLIC_BV_512","256","256","0","128","32","32","256","2","0"],
                  "in_vectsize" : 512,
                  "out_vectsize" : 256,
                  "lanesize" : 256,
                  "in_precision" : 32,
                  "out_precision" : 32,
                  "in_vectsize_index" : 2,
                  "out_vectsize_index" : 2,
                  "lanesize_index" : 3,
                  "in_precision_index" : 6,
                  "out_precision_index" : 6,
                  "arg_permute_map" : [0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  "Signedness" : None,
                  "Cost" : "[{'Icelake': {'l': '1', 't': '0.5'}}, {'Skylake': {'l': '1', 't': '1'}}]",
                  "SIMD" : "True",
                  "Extensions" : "['avx2']",
      },
          
                "x86_swizzle_0" : {
                  "args" : ["SYMBOLIC_BV_512","SYMBOLIC_BV_512","256","256","0","128","32","32","384","2","0"],
                  "in_vectsize" : 512,
                  "out_vectsize" : 256,
                  "lanesize" : 256,
                  "in_precision" : 32,
                  "out_precision" : 32,
                  "in_vectsize_index" : 2,
                  "out_vectsize_index" : 2,
                  "lanesize_index" : 3,
                  "in_precision_index" : 6,
                  "out_precision_index" : 6,
                  "arg_permute_map" : [0,1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                  "Signedness" : None,
                  "Cost" : "[{'Icelake': {'l': '1', 't': '0.5'}}, {'Skylake': {'l': '1', 't': '1'}}]",
                  "SIMD" : "True",
                  "Extensions" : "['avx2']",
      },
          },
              "semantics" : ['"(define (x86_swizzle_1  v0 v1 %vectsize0 %outerlanesize0 %innerlaneoffset0 %innerlanesize0 %elemsize0 %arg0 %arg1 %arg2 %arg3 )"', '"(define dst"', '"(apply"', '"concat"', '"(for/list ([%outer.it (reverse (range 0 %vectsize0 %outerlanesize0))])"', '" (apply"', '" concat"', '" (for/list ([iterator.0.new (reverse (range %innerlaneoffset0 %innerlanesize0 %elemsize0))])"', '"  (define iterator.0.new.mul (*  iterator.0.new  %arg2))"', '"  (define %low.offset0 (+  iterator.0.new  %arg1))"', '"  (define %lastidx1 (-  %elemsize0  1))"', '"  (define %high.offset0 (+  %low.offset0  %lastidx1))"', '"  (define %0 (extract  %high.offset0 %low.offset0 v0))"', '"  (define %1 (extract  %high.offset0 %low.offset0 v1))"', '"(concat %1 %0)"', '" )"', '" )"', '")"', '")"', '")"', '"(bvpadhighbits  dst %arg3)"', '")"', '""'],
        },
          
            "x86_swizzle_4" : {
              "target_instructions" : {
                "x86_swizzle_4" : {
                  "args" : ["SYMBOLIC_BV_128","SYMBOLIC_BV_128","128","128","0","128","32","32","2","0"],
                  "in_vectsize" : 128,
                  "out_vectsize" : 256,
                  "lanesize" : 128,
                  "in_precision" : 32,
                  "out_precision" : 32,
                  "in_vectsize_index" : 2,
                  "out_vectsize_index" : 2,
                  "lanesize_index" : 3,
                  "in_precision_index" : 6,
                  "out_precision_index" : 6,
                  "arg_permute_map" : [0,1,-1,-1,-1,-1,-1,-1,-1,-1],
                  "Signedness" : None,
                  "Cost" : "[{'Icelake': {'l': '1', 't': '0.5'}}, {'Skylake': {'l': '1', 't': '1'}}]",
                  "SIMD" : "True",
                  "Extensions" : "['avx2']",
      },
          
                "x86_swizzle_163" : {
                  "args" : ["SYMBOLIC_BV_64","SYMBOLIC_BV_64","64","64","0","64","32","32","2","0"],
                  "in_vectsize" : 64,
                  "out_vectsize" : 128,
                  "lanesize" : 64,
                  "in_precision" : 32,
                  "out_precision" : 32,
                  "in_vectsize_index" : 2,
                  "out_vectsize_index" : 2,
                  "lanesize_index" : 3,
                  "in_precision_index" : 6,
                  "out_precision_index" : 6,
                  "arg_permute_map" : [0,1,-1,-1,-1,-1,-1,-1,-1,-1],
                  "Signedness" : None,
                  "Cost" : "[{'Icelake': {'l': '1', 't': '0.5'}}, {'Skylake': {'l': '1', 't': '1'}}]",
                  "SIMD" : "True",
                  "Extensions" : "['avx2']",
      },
          },
              "semantics" : ['"(define (x86_swizzle_4  v0 v1 %vectsize0 %outerlanesize0 %innerlaneoffset0 %innerlanesize0 %elemsize0 %arg0 %arg1 %arg2 )"', '"(define dst"', '"(apply"', '"concat"', '"(for/list ([%outer.it (reverse (range 0 %vectsize0 %outerlanesize0))])"', '" (apply"', '" concat"', '" (for/list ([iterator.0.new (reverse (range %innerlaneoffset0 %innerlanesize0 %elemsize0))])"', '"  (define iterator.0.new.mul (*  iterator.0.new  %arg1))"', '"  (define %lastidx1 (-  %elemsize0  1))"', '"  (define %high.offset0 (+  iterator.0.new  %lastidx1))"', '"  (define %0 (extract  %high.offset0 iterator.0.new v0))"', '"  (define %1 (extract  %high.offset0 iterator.0.new v1))"', '"(concat %1 %0)"', '" )"', '" )"', '")"', '")"', '")"', '"(bvpadhighbits  dst %arg2)"', '")"', '""'],
        },
          }
