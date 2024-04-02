from common.Types import *
from common.Instructions import *
from  utils.DSLInstructionUtils import *

import math




class EqClassExpandGenerator:

    def __init__(self, dsl_list = [], output_bitwidth = None, input_sizes = [], input_precs = []):
        self.dsl_list = dsl_list
        self.output_bitwidth = output_bitwidth
        self.input_sizes = input_sizes
        self.grammar_clause_map = {}
        self.use_buffer_id = True
        self.input_precs = input_precs


    def emit_choose_buffer(self, reg_id, precision = 8, signedness = True):


        type_str = "int"

        prefix = "'"
        if not signedness:
            prefix = "'u"

        size_str = str(precision)

        type_str = prefix + type_str+size_str

        return "(buffer-index {} {} {})".format(reg_id, type_str, self.input_sizes[reg_id])

    def emit_choose_reg(self, reg_id, precision = 8, signedness = True):
        if self.use_buffer_id:
            return self.emit_choose_buffer(reg_id, precision = precision, signedness = signedness)

        reg_bv = "(bv {} (bitvector 8))".format(reg_id)
        return "(reg  {})".format(reg_bv)

    def get_eq_class(self, eq_class_name):
        eq_class_name = eq_class_name.split("_dsl")[0]
        for dsl_inst in self.dsl_list:
            if dsl_inst.name == eq_class_name:
                return dsl_inst
        print("Unable to find", eq_class_name)
        assert False,"Unreachable"

    def get_layer_name(self, eq_class, parent_name, layer_idx, output_size):
        return "_".join([parent_name, eq_class.name,"layer" ,str(layer_idx), "bv", str(output_size) ])


    def add_zero_imm(self, current_layer_name):
        self.add_clause_to_layer_context(current_layer_name,"'()")

    def process_ctx(self, f_ctx, ref_ctx, current_layer_name, layer_index):

        clause_tokens = [f_ctx.dsl_name]
        for idx, f_arg in enumerate(f_ctx.context_args):
            ref_arg = ref_ctx.context_args[idx]

            if isinstance(ref_arg, Reg) and isinstance(f_arg, ConstBitVector):
                return
            elif isinstance(ref_arg, Reg) and f_arg.size != ref_arg.size:
                return
            elif isinstance(ref_arg, Reg):
                assert isinstance(f_arg, BitVector), "Corresponding argument must be a symbolic parameter"
                sign = True

                if not f_ctx.signedness is None:
                    sign = [False, True][f_ctx.signedness]

                clause_tokens.append(self.emit_choose_reg(int(ref_arg.index), precision = f_ctx.in_precision, signedness = sign))

            elif isinstance(ref_arg, Context) and isinstance(f_arg, ConstBitVector):
                return

            elif isinstance(ref_arg, ConstBitVector) and isinstance(f_arg, BitVector):
                return

            elif isinstance(ref_arg, Context) :
                assert isinstance(f_arg, BitVector), "Corresponding argument must be a symbolic parameter"
                param_eq_arg = self.get_eq_class(ref_arg.dsl_name)

                updated_parent_name = "_".join([current_layer_name, "arg", str(idx)])
                child_name =  self.get_layer_name(param_eq_arg, updated_parent_name, layer_index+1, f_arg.size)
                self.initialize_layer_context(child_name, updated_parent_name,  f_arg.size, param_eq_arg, ref_arg, layer_index+1)

                clause_tokens.append("({})".format(child_name))
            else:
                clause_str = f_arg.get_dsl_value() +"\t\t\t\t"+f_arg.get_rkt_comment()
                clause_tokens.append(clause_str)


        clause = "({}\n)".format("\n".join(clause_tokens))
        self.add_clause_to_layer_context(current_layer_name, clause)




    def add_clause_to_layer_context(self, layer_name, clause):
        assert layer_name in self.grammar_clause_map, "Must be pre-initialized"
        self.grammar_clause_map[layer_name]["clauses"].append(clause)






    def initialize_layer_context(self, layer_name, parent_name,  output_size, eq_class, ref_expr, layer_index):
        if layer_name not in self.grammar_clause_map:
            self.grammar_clause_map[layer_name] = {"output_size": output_size, "clauses": [], "child_layer_names": [], "visited": False, "eq_class": eq_class, "ref_expr": ref_expr, "parent_name": parent_name, "layer_idx": layer_index}

    def set_layer_context_visited(self, layer_name):
        assert layer_name in self.grammar_clause_map, "Must be pre-initialized"
        self.grammar_clause_map[layer_name]["visited"] = True

    def get_layer_context_visited(self, layer_name):
        assert layer_name in self.grammar_clause_map, "Must be pre-initialized"
        return self.grammar_clause_map[layer_name]["visited"]


    def print_all_layer_contexts(self):
        for key in self.grammar_clause_map:
            self.print_layer_context(key)


    def print_layer_context(self, layer_name):
        assert layer_name in self.grammar_clause_map, "Must be pre-initialized"
        print("========================")
        print("Printing Layer Contexts for:", layer_name)

        layer_ctx = self.grammar_clause_map[layer_name]
        print("\n".join(layer_ctx['clauses']))
        print("Visited:", layer_ctx['visited'])


    def emit_all_layer_contexts(self):
        defs = []
        for key in self.grammar_clause_map:
            definition = self.emit_layer_context(key)
            defs.append(definition)
        return "\n".join(defs)


    def emit_layer_context(self, layer_name):
        assert layer_name in self.grammar_clause_map, "Must be pre-initialized"
        layer_ctx = self.grammar_clause_map[layer_name]
        definition = "(define ({}) \n(choose* \n{}\n)\n)".format(layer_name, "\n".join(layer_ctx['clauses']))
        return definition

    def visit_expr(self, ctx, parent_name, layer_idx, output_size):
        eq_class = self.get_eq_class(ctx.dsl_name)
        #print("Visting ", eq_class.name, " with output size: ", output_size)

        current_layer_name = self.get_layer_name(eq_class, parent_name, layer_idx, output_size)
        self.initialize_layer_context(current_layer_name, parent_name, output_size, eq_class, ctx, layer_idx)

        #print("Current layer name: ", current_layer_name)

        feasible_ctxs = []
        for e_ctx in eq_class.contexts:
            if e_ctx.out_vectsize == output_size:
                feasible_ctxs.append(e_ctx)


        #print("Number of feasible contexts: ", len(feasible_ctxs))

        for f_ctx in feasible_ctxs:
            self.process_ctx(f_ctx, ctx, current_layer_name, layer_idx)

        if len(feasible_ctxs) == 0:
            self.add_zero_imm(current_layer_name)


        self.set_layer_context_visited(current_layer_name)
        return current_layer_name








    def emit_grammar(self, ref_expr):
        output_expr_name = self.visit_expr(ref_expr, "output", 0, self.output_bitwidth)


        #print("First state of layer contexts")
        #self.print_all_layer_contexts()
        #input()
        Terminate = False

        iteration = 0
        while not Terminate:
            #print("Iteration", iteration)
            iteration += 1
            layer_keys = [key for key in self.grammar_clause_map]
            for key in layer_keys:
                visited = self.get_layer_context_visited(key)

                if not visited:
                    #print(key,"not visited!")
                    layer_ctx = self.grammar_clause_map[key]
                    #print(layer_ctx)
                    #self.visit_expr(layer_ctx['ref_expr'], layer_ctx['parent_name'], layer_ctx['layer_idx'], layer_ctx['ref_expr'].out_vectsize)

                    self.visit_expr(layer_ctx['ref_expr'], layer_ctx['parent_name'], layer_ctx['layer_idx'], layer_ctx['output_size'])



            layer_keys = [key for key in self.grammar_clause_map]
            Terminate = all([(self.get_layer_context_visited(key)) for key in layer_keys])
            #input()


        # self.print_all_layer_contexts()
        defs = self.emit_all_layer_contexts()

        #with open("Check.rkt", "w+") as WriteFile:
        #    WriteFile.write(HYDRIDE_HEADER+"\n")
        #    WriteFile.write(defs+"\n")
        #    WriteFile.write(";"+output_expr_name)
        #print("Took",iteration, "iterations...")

        return output_expr_name , defs




