from Ops import *


def is_expression_canonical(expr):

    if expr.commutative:
        
        # Left Heavy Nodes are canonical
        num_nodes_left = len(expr.operands[0].get_nested_operands())
        num_nodes_right = len(expr.operands[1].get_nested_operands())

        if num_nodes_left < num_nodes_right:
            return False

    return all([is_expression_canonical(opnd) for opnd in expr.operands])

