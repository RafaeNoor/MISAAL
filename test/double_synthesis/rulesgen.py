#from Pattern import *
from common.Instructions import *
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils


def verify_expression(expr : Context, dsl_inst_list : list):
  assert isinstance(expr, Context) == True
  for dsl_inst in dsl_inst_list:
    assert isinstance(dsl_inst, DSLInstruction) == True
    if expr.name == dsl_inst.name:
      for ctx in dsl_inst.contexts:
        assert isinstance(ctx, Context) == True
        assert len(expr.context_args) == len(ctx.context_args)
        found_match = False
        for lhs_arg, arg in zip(expr.context_args, ctx.context_args):
          if isinstance(lhs_arg, Context):
            verify_expression(arg, dsl_inst_list)
          elif isinstance(lhs_arg, Reg):
            assert isinstance(lhs_arg, Reg) == True
          elif found_match == True:
            if lhs_arg != arg:
              found_match = False
          else:
            if lhs_arg == arg:
              found_match = True
        assert found_match == True


def get_symbolic_bvs(expr : Context):
  assert isinstance(expr, Context) == True
  symbolic_args = list()
  for arg in expr.context_args:
    if isinstance(arg, Context):
      symbolic_args.extend(get_symbolic_bvs(arg))
    elif isinstance(arg, Reg):
      symbolic_args.append(arg)
  return symbolic_args


def get_barename(name : str):
  if "dsl" in name:
    name = name.split("_dsl")[0]
  if "typed:" in name:
    name = name.split("typed:")[1]
  if "p_" in name[::-1]:
    name_rev = name[::-1].split("p_")[1]
    name = name_rev[::-1]
  return name


def get_output_sizes(expr : Context, dsl_list : list):
  assert isinstance(expr, Context) == True
  output_sizes = set()
  for dsl_inst in dsl_list:
    assert isinstance(dsl_inst, DSLInstruction) == True
    dsl_inst_name = get_barename(dsl_inst.name)
    expr_name = get_barename(expr.name)
    if expr_name == dsl_inst_name:
      for ctx in dsl_inst.contexts:
        output_sizes.add(ctx.out_vectsize)
      break
  return list(output_sizes)


def get_input_sizes(expr : Context, dsl_list : list, 
                    input_sizes_dict : dict = dict()):
  assert isinstance(expr, Context) == True
  dict_idx = -1
  if len(input_sizes_dict.keys()) == 0:
    dict_idx = 0
  for dsl_inst in dsl_list:
    assert isinstance(dsl_inst, DSLInstruction) == True
    dsl_inst_name = get_barename(dsl_inst.name)
    expr_name = get_barename(expr.name)
    if expr_name == dsl_inst_name:
      for ctx_idx, ctx in enumerate(dsl_inst.contexts):
        if dict_idx == 0:
          input_sizes_dict[ctx_idx] = list()
        for arg in expr.context_args:  
          if isinstance(arg, Context):
            input_sizes_dict = get_input_sizes(arg, dsl_list, input_sizes_dict)
          elif isinstance(arg, Reg):
            input_sizes_dict[ctx_idx].append(ctx.in_vectsize)
      break
  # Get rid of duplicate entries
  result = {}
  for key, value in input_sizes_dict.items():
    if value not in result.values():
        result[key] = value
  input_sizes_dict = result
  return input_sizes_dict


def generate_candidates(lhs_expr : Context, lhs_dsl_list : list,
                        rhs_expr : Context, rhs_dsl_list : list):
  print("\n\nGENERATE CANDIDATES")
  lhs_to_rhs_patterns = dict()
  verify_expression(lhs_expr, lhs_dsl_list)
  output_sizes = get_output_sizes(lhs_expr, lhs_dsl_list)
  print("output_sizes:")
  print(output_sizes)
  input_sizes_dict = get_input_sizes(lhs_expr, lhs_dsl_list)
  print("input_sizes_dict:")
  print(input_sizes_dict)
  #num_lhs_inputs = get_symbolic_bvs(lhs_expr)
  #num_rhs_inputs = get_symbolic_bvs(rhs_expr)
  synthesizer = DoubleGrammarSynthesisUtils(lhs_dsl_list, rhs_dsl_list)
  for output_size in output_sizes:
    for _, input_sizes in input_sizes_dict.items():
      print("===========================")
      print("output_size:")
      print(output_size)
      print("input_sizes:")
      print(input_sizes)
      success, src_expr_str, dst_expr_str = synthesizer.double_grammar_synthesis(
                                                            lhs_expr, rhs_expr,
                                                            custom_src_output_size = output_size,
                                                            custom_dst_output_size = output_size,
                                                            custom_src_input_sizes = input_sizes,
                                                            custom_target_input_sizes = input_sizes)
      if success:
          print("SUCCESS at output size {}!".format(output_size))
          print("Corresponding LHS concretization:")
          print(src_expr_str)
          print("Corresponding RHS concretization:")
          print(dst_expr_str)
      else:
          print("FAILURE!") 
        

def generalize_rules(lhs_expr : Context, lhs_dsl_list : list,
                      rhs_expr : Context, rhs_dsl_list : list):
  assert isinstance(rhs_expr, Context) == True
  assert isinstance(lhs_expr, Context) == True
  print("len(lhs_dsl_list):")
  print(len(lhs_dsl_list))
  print("len(rhs_dsl_list):")
  print(len(rhs_dsl_list))
  generate_candidates(lhs_expr, lhs_dsl_list, \
                      rhs_expr, rhs_dsl_list)


#def generalize_pattern(pattern : Pattern):
#  rhs_expr = pattern.src_expr
#  lhs_expr = pattern.target_expr
#  #generalize_rules(lhs_expr, rhs_expr)


from utils.ReadDSL import read_string_to_dsl
from common.DSLParser import parse_dict
from sema.ARMSema import arm_semantics
from sema.halide_sema import halide_semantics

# Uncomment below line to keep intermediate racket files
#keep_temporary_files()

# Parse the dictionay into a list of DSLInstruction types
arm_dsl_list = parse_dict(arm_semantics)
halide_dsl_list = parse_dict(halide_semantics)

arm_expr_str = "(vhadd_s32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 -1 0 16 0 16)"
halide_expr_str = "(typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32)"

arm_expr_ctx = read_string_to_dsl(arm_expr_str, arm_dsl_list)
halide_expr_ctx = read_string_to_dsl(halide_expr_str, halide_dsl_list)

print("="*5, "Pretty Printing Expressions", "="*5)
print(arm_expr_ctx.emit_context_expr_string())
print(halide_expr_ctx.emit_context_expr_string())

generalize_rules(halide_expr_ctx, halide_dsl_list, arm_expr_ctx, arm_dsl_list)

