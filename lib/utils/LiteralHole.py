import common.Types
from common.Types import *
from  common.Instructions import Context, DSLInstruction



LiteralHoleSemantics = [
    "(define (LiteralHole bv-hole-param bw vsize)",
    "(define bv-hole (sign-extend bv-hole-param (bitvector bw)))",
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

def is_literal_hole(expr):
    if not isinstance(expr, Context):
        return False
    return "LiteralHole" in expr.name


def convert_concreate_lit_hole_to_lit(expr):
    assert is_literal_hole(expr)

    bv_arg = expr.context_args[0]
    assert isinstance(expr, ConstBitVector)

    lit_hole_value =  expr.value
    print("Literal Hole value:", lit_hole_value)


def legalize_concrete_literal_holes(expr):
    if not isinstance(expr, Context):
        return expr

    if is_literal_hole(expr):
        return convert_concreate_lit_hole_to_lit(expr)

    for idx, arg in enumerate(expr.context_args):
        expr.context_args[idx] = legalize_concrete_literal_holes(arg)

    return expr



LiteralHole = create_literal_hole()

