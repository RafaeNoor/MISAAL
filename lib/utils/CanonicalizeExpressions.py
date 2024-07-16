import common.Types
import sys
import time
import copy
import sys
from common.Types import *
from  common.Instructions import Context
import subprocess
import os
import tempfile
import glob
import numpy as np
import concurrent.futures
import json


# Rough canonicalization of expressions so that we don't enumerate repeated expressions modulo
# commutativity. Canonical form prefers expressions to be 'left heavy', i.e. if an expression OP is commutative then the operand 0 of the canonical form of OP would have more nodes in it's sub-expression than operand 1 of the canonical form of OP.

class CanonicalizeExpression:

    def __init__(self, commutative_map_path = ""):
        self.commutative_map_path = commutative_map_path
        self.commutative_map = {}

        if self.commutative_map_path != "":
            with open(self.commutative_map_path, "r") as JSONFile:
                self.commutative_map = json.load(JSONFile)


    def canonicalize(self, expr):
        canonical_expression = copy.deepcopy(expr)

        self.canonicalize_helper(canonical_expression)

        return canonical_expression

    def is_expr_commutable(self, expr):
        return expr.dsl_name in self.commutative_map



    def get_sym_or_ctx_args(self, ctx):
        return ([(idx, arg) for idx, arg in enumerate(ctx.context_args) if isinstance(arg, BitVector) or isinstance(arg, Context) or isinstance(arg, Reg)])


    def count_terms(self, expr):
        if isinstance(expr, Reg):
            return 1

        if isinstance(expr, Context):
            count = 1

            for arg in expr.context_args:
                count += self.count_terms(arg)
            return count

        return 0

    def get_max_reg_index(self, expr):
        if isinstance(expr, Reg):
            return int(expr.index)

        if isinstance(expr, Context):
            max_reg = -1

            for arg in expr.context_args:
                max_reg  = max(self.count_terms(arg), max_reg)
            return max_reg

        return -1

    def canonicalize_helper(self, expr):

        if isinstance(expr, Reg):
            return

        args = self.get_sym_or_ctx_args(expr)

        if len(args) != 2 or (not self.is_expr_commutable(expr)):
            for idx, arg in args:
                self.canonicalize_helper(arg)
        elif len(args) == 2 and self.is_expr_commutable(expr):
            # Count number of nodes on both sides and then set accordingly. Recursively
            # canoncialize operands
            lhs_idx, lhs_term = args[0]
            rhs_idx, rhs_term = args[1]
            num_lhs_terms = self.count_terms(lhs_term)
            num_rhs_terms = self.count_terms(rhs_term)

            self.canonicalize_helper(lhs_term)
            self.canonicalize_helper(rhs_term)

            if num_rhs_terms > num_lhs_terms:
                # Swap terms
                expr.context_args[rhs_idx] = lhs_term
                expr.context_args[lhs_idx] = rhs_term

            if (num_rhs_terms == num_lhs_terms):
                # Get maximum register count on both sides, then set the maximum register count on the left hand side expression
                """
                lhs_max_reg_index = self.get_max_reg_index(lhs_term)
                rhs_max_reg_index = self.get_max_reg_index(rhs_term)

                if rhs_max_reg_index > lhs_max_reg_index:
                    expr.context_args[rhs_idx] = lhs_term
                    expr.context_args[lhs_idx] = rhs_term
                """







