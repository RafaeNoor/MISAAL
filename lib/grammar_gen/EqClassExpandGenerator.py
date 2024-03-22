from common.Types import *
from common.Instructions import *
import math




class EqClassExpandGenerator:

    def __init__(self, dsl_list = [], output_bitwidth = None, input_sizes = []):
        self.dsl_list = dsl_list
        self.output_bitwidth = output_bitwidth
        self.input_sizes = input_sizes
        self.grammar_clause_map = {}


    def get_eq_class(self, eq_class_name):
        eq_class_name = eq_class_name.split("_dsl")[0]
        for dsl_inst in self.dsl_list:
            if dsl_inst.name == eq_class_name:
                return dsl_inst
        print("Unable to find", eq_class_name)
        assert False,"Unreachable"

    def get_layer_name(self, eq_class, parent_name, layer_idx, output_size):
        return "_".join([parent_name, eq_class.name,"layer" ,str(layer_idx), str(output_size) ])


    def process_ctx(self, f_ctx, ref_ctx, current_layer_name, layer_index):

        clause_tokens = [f_ctx.dsl_name]
        for idx, f_arg in enumerate(f_ctx.context_args):
            ref_arg = ref_ctx.context_args[idx]

            if isinstance(ref_arg, Reg) and isinstance(f_arg, ConstBitVector):
                return
            elif isinstance(ref_arg, Reg):
                assert isinstance(f_arg, BitVector), "Corresponding argument must be a symbolic parameter"
                clause_tokens.append(ref_arg.get_rkt_value())

            elif isinstance(ref_arg, Context) and isinstance(f_arg, ConstBitVector):
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



    def visit_expr(self, ctx, parent_name, layer_idx, output_size):
        eq_class = self.get_eq_class(ctx.dsl_name)

        current_layer_name = self.get_layer_name(eq_class, parent_name, layer_idx, output_size)
        self.initialize_layer_context(current_layer_name, parent_name, output_size, eq_class, ctx, layer_idx)

        feasible_ctxs = []
        for e_ctx in eq_class.contexts:
            if e_ctx.out_vectsize == output_size:
                feasible_ctxs.append(e_ctx)



        for f_ctx in feasible_ctxs:
            self.process_ctx(f_ctx, ctx, current_layer_name, layer_idx)

        self.set_layer_context_visited(current_layer_name)








    def emit_grammar(self, ref_expr):
        self.visit_expr(ref_expr, "output", 0, self.output_bitwidth)


        Terminate = False

        iteration = 0
        while not Terminate:
            print("Iteration", iteration)
            iteration += 1
            layer_keys = [key for key in self.grammar_clause_map]
            for key in layer_keys:
                visited = self.get_layer_context_visited(key)

                if not visited:
                    print(key,"not visited!")
                    layer_ctx = self.grammar_clause_map[key]
                    self.visit_expr(layer_ctx['ref_expr'], layer_ctx['parent_name'], layer_ctx['layer_idx'], layer_ctx['ref_expr'].out_vectsize)



            layer_keys = [key for key in self.grammar_clause_map]
            Terminate = all([(self.get_layer_context_visited(key)) for key in layer_keys])


        self.print_all_layer_contexts()




