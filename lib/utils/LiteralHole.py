import common.Types
from common.Types import *
from  common.Instructions import Context, DSLInstruction



LiteralHoleSemantics = [
    "(define (LiteralHole bv-hole bw vsize)",
    "(cond [(not (concrete? bv-hole)) (assert (not (equal? bv-hole (bv 0 bw))))   (assert (bvule bv-hole (bv 8 bw)))])",
    "(define num-elems (/ vsize bw))",
    "(apply",
    "concat",
    "(for/list ([i (range 0 num-elems)])",
    "bv-hole",
    ")",
    ")",
    ")",
]



def create_literal_hole():
    LiteralHole = DSLInstruction(name = "LiteralHole", simd=False, operation=False, semantics = LiteralHoleSemantics)

    bitwidths = [8, 16, 32]
    #bitwidths = [32]
    vect_sizes = [pow(2,i) for i in range(3, 12)]

    print(bitwidths)
    print(vect_sizes)

    for bw in bitwidths:
        for vsize in vect_sizes:
            if vsize % bw != 0:
                continue
            ctx_name = f"LiteralHole_bw{bw}_size{vsize}"
            LiteralHole.add_context(
                name = ctx_name,
                in_vectsize = vsize,
                out_vectsize = vsize,
                lane_size = bw,
                in_precision = bw,
                out_precision = bw,
                args = [f"CONST_HOLE_BV_{bw}",str(bw), str(vsize)]
            )


    return LiteralHole


LiteralHole = create_literal_hole()

