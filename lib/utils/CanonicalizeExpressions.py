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

        if self.commutative_map_path != "" and not self.commutative_map_path  is None:
            with open(self.commutative_map_path, "r") as JSONFile:
                self.commutative_map = json.load(JSONFile)

        self.print_canon_map()

    def print_canon_map(self):
        print("Commutative Map")
        print(json.dumps(self.commutative_map, indent = 4))

    def canonicalize(self, expr):
        canonical_expression = copy.deepcopy(expr)

        self.canonicalize_helper(canonical_expression)

        return canonical_expression

    def is_expr_commutable(self, expr):
        return expr.dsl_name.split("_dsl")[0] in self.commutative_map

    def get_commutable_indices(self, expr):
        key = expr.dsl_name.split("_dsl")[0]
        return self.commutative_map[key]



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


    def isCanonical(self, expr, canonical_expr):
        if isinstance(expr, Context) and not isinstance(canonical_expr, Context):
            return False

        if not isinstance(expr, Context) and isinstance(canonical_expr, Context):
            return False

        if isinstance(expr, Reg) and not isinstance(canonical_expr, Reg):
            return False

        if not isinstance(expr, Reg) and isinstance(canonical_expr, Reg):
            return False

        if isinstance(expr, Reg) and  isinstance(canonical_expr, Reg):
            return True

        if isinstance(expr, ConstBitVector) and  not isinstance(canonical_expr, ConstBitVector):
            return False

        if not isinstance(expr, ConstBitVector) and   isinstance(canonical_expr, ConstBitVector):
            return False


        if isinstance(expr, Context) and isinstance(canonical_expr, Context):
            same_name = expr.dsl_name == canonical_expr.dsl_name

            if not same_name:
                return False

            condition = True

            for idx in range(len(expr.context_args)):
                arg = expr.context_args[idx]
                canon_arg = canonical_expr.context_args[idx]


                if isinstance(arg, Reg):
                    condition = condition and self.isCanonical(arg, canon_arg)

                if isinstance(canon_arg, Reg):
                    condition = condition and self.isCanonical(arg, canon_arg)

                if isinstance(arg, Context):
                    condition = condition and self.isCanonical(arg, canon_arg)

                if isinstance(canon_arg, Context):
                    condition = condition and self.isCanonical(arg, canon_arg)

            return condition

        if isinstance(expr, Context) and not isinstance(canonical_expr, Context):
            return False

        if not isinstance(expr, Context) and isinstance(canonical_expr, Context):
            return False

        return True

    def canonicalize_helper(self, expr):

        if isinstance(expr, Reg):
            return

        args = self.get_sym_or_ctx_args(expr)

        if (not self.is_expr_commutable(expr)):
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

            lhs_name = ""
            if isinstance(lhs_term, Context):
                lhs_name = lhs_term.name

            rhs_name = ""
            if isinstance(rhs_term, Context):
                rhs_name = rhs_term.name

            if num_rhs_terms > num_lhs_terms:
                # Swap terms
                expr.context_args[rhs_idx] = lhs_term
                expr.context_args[lhs_idx] = rhs_term
            elif num_rhs_terms == num_lhs_terms and len(rhs_name) > len(lhs_name):
                # Use context name to break tie
                # Swap terms
                expr.context_args[rhs_idx] = lhs_term
                expr.context_args[lhs_idx] = rhs_term






        elif len(args) == 3 and self.is_expr_commutable(expr):
            # Count number of nodes on both sides and then set accordingly. Recursively
            # canoncialize operands
            commutable_indices = self.get_commutable_indices(expr)
            lhs_idx, lhs_term = args[commutable_indices[0]]
            rhs_idx, rhs_term = args[commutable_indices[1]]
            num_lhs_terms = self.count_terms(lhs_term)
            num_rhs_terms = self.count_terms(rhs_term)

            self.canonicalize_helper(lhs_term)
            self.canonicalize_helper(rhs_term)

            lhs_name = ""
            if isinstance(lhs_term, Context):
                lhs_name = lhs_term.name

            rhs_name = ""
            if isinstance(rhs_term, Context):
                rhs_name = rhs_term.name

            if num_rhs_terms > num_lhs_terms:
                # Swap terms
                expr.context_args[rhs_idx] = lhs_term
                expr.context_args[lhs_idx] = rhs_term
            elif num_rhs_terms == num_lhs_terms and len(rhs_name) > len(lhs_name):
                # Use context name to break tie
                # Swap terms
                expr.context_args[rhs_idx] = lhs_term
                expr.context_args[lhs_idx] = rhs_term








