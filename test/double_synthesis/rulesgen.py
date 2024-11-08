#from Pattern import *
import multiprocessing
import itertools
import sys

from utils.ReadDSL import read_string_to_dsl
from common.DSLParser import parse_dict
from common.Instructions import *
from utils.DSLInstructionUtils import keep_temporary_files
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils


class GeneralizedContext:
  def __init__(self, ctx : Context):
    self.org_ctx = ctx
    self.args = list()
    # Concrete values of abstracted constants are kept track of here
    self.arg_names_to_val = dict()

  def __eq__(self, ctx):
    if not isinstance(ctx, GeneralizedContext):
      return False
    if len(self.args) != len(ctx.args):
      return False
    for arg1, arg2 in zip(self.args, ctx.args):
      if type(arg1) != type(arg2):
        return False
      if not isinstance(arg1, Reg):
        if arg1 != arg2:
          return False
    return True

  def __ne__(self, ctx):
    return not self.__eq__(ctx)

  def print(self):
    # self.org_ctx.print_context()
    # print("self.args:")
    # for arg in self.args:
    #   if isinstance(arg, GeneralizedContext):
    #     arg.print()
    #   elif type(arg) != str:
    #     arg.print_operand()
    #   else:
    #     print(arg)
    # print(self.args)
    # print("self.arg_names_to_val:")
    # print(self.arg_names_to_val)
    print(self.emit_context_expr_string())

  def emit_context_expr_string(self, prefix=""):
    string = ("{} ({} ; {}".format(prefix, self.org_ctx.dsl_name, self.org_ctx.name))
    for arg in self.args:
      if isinstance(arg, Context):
        string += "\n" + arg.emit_context_expr_string(prefix=prefix + "\t")
      elif isinstance(arg, Reg) \
        and self.org_ctx.extensions != None \
        and 'halide' in self.org_ctx.extensions:
        string += "\n" + (prefix + "\t" + arg.get_halide_dsl_value())
      elif isinstance(arg, str):
        string += "\n" + (prefix + "\t" + arg)
      elif isinstance(arg, GeneralizedContext):
        if isinstance(arg.org_ctx, Reg):
          string += "\n" + (prefix + "\t" + arg.org_ctx.get_rkt_value())
        else:
          string += "\n" + arg.emit_context_expr_string(prefix=prefix + "\t")
      else:
        string += "\n" + (prefix + "\t" + arg.get_dsl_value())
    string += "\n" + ("{} )".format(prefix))
    return string


class GeneralizedPattern:
  def __init__(self):
    self.lhs_generalized_ctxs = None
    self.rhs_generalized_ctxs = None


# Just make sure that a given expression is consistent with a given list
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


# Get all possible concrete output sizes for an expression
def get_output_sizes(expr : Context, dsl_list : list):
  assert isinstance(expr, Context) == True
  output_sizes = set()
  for dsl_inst in dsl_list:
    assert isinstance(dsl_inst, DSLInstruction) == True
    dsl_inst_name = get_barename(dsl_inst.name)
    expr_name = get_barename(expr.dsl_name)
    if expr_name == dsl_inst_name:
      for ctx in dsl_inst.contexts:
        output_sizes.add(ctx.out_vectsize)
      break
  return list(output_sizes)


# Get all possible concrete input sizes for an expression
def get_input_sizes(expr : Context, dsl_list : list):
  assert isinstance(expr, Context) == True
  print("\nget_input_sizes")
  print(expr.emit_context_expr_string())
  for dsl_inst in dsl_list:
    assert isinstance(dsl_inst, DSLInstruction) == True
    dsl_inst_name = get_barename(dsl_inst.name)
    expr_name = get_barename(expr.dsl_name)
    if expr_name == dsl_inst_name:
      acc_size_lists = list()
      for ctx in dsl_inst.contexts:
        partial_size_lists = [list()]
        for arg in expr.context_args:
          if isinstance(arg, Context):
            size_lists = get_input_sizes(arg, dsl_list)
            print("size_lists:")
            print(size_lists)
            temp_lists = list()
            for size_list in size_lists:
              for idx in range(len(partial_size_lists)):
                temp_lists.append(partial_size_lists[idx] + size_list)
            partial_size_lists = temp_lists
          elif isinstance(arg, Reg):
            for idx in range(len(partial_size_lists)):
              partial_size_lists[idx].append(ctx.in_vectsize)
        acc_size_lists.extend(partial_size_lists)
      return acc_size_lists
  return None


# Generate new patterns using double synthesis
def pattern_gen(output_size, input_sizes_list, lhs_expr, lhs_dsl_list,
                rhs_dsl_list, rhs_expr, lhs_to_rhs_patterns, synthesizer):
  for input_sizes in input_sizes_list:
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
        src_expr = read_string_to_dsl(src_expr_str, lhs_dsl_list)
        dst_expr = read_string_to_dsl(dst_expr_str, rhs_dsl_list)
        lhs_to_rhs_patterns[src_expr] = dst_expr
    else:
        print("FAILURE!")


# Function to check if two expressions are the same
def are_exprs_equal(expr1 : Context, expr2 : Context):
  if len(expr1.context_args) != len(expr2.context_args):
    return False
  for arg1, arg2 in zip(expr1.context_args, expr2.context_args):
    if type(arg1) != type(arg2):
      return False
    if isinstance(arg1, Context):
      if are_exprs_equal(arg1, arg2) == False:
        return False
    elif isinstance(arg1, Reg):
      if arg1.index != arg2.index:
        return False
    else:
      if arg1.value != arg2.value:
        return False
  return True


# Generates different candidate rules
def generate_candidates(lhs_expr : Context, lhs_dsl_list : list,
                        rhs_expr : Context, rhs_dsl_list : list):
  print("\n\nGENERATE CANDIDATES")
  verify_expression(lhs_expr, lhs_dsl_list)
  verify_expression(rhs_expr, rhs_dsl_list)
  output_sizes = get_output_sizes(lhs_expr, lhs_dsl_list)
  print("output_sizes:")
  print(output_sizes)
  input_sizes = get_input_sizes(lhs_expr, lhs_dsl_list)
  input_sizes.sort()
  input_sizes = list(k for k, _ in itertools.groupby(input_sizes))
  print("input_sizes:")
  print(input_sizes)
  #num_lhs_inputs = get_symbolic_bvs(lhs_expr)
  #num_rhs_inputs = get_symbolic_bvs(rhs_expr)
  synthesizer = DoubleGrammarSynthesisUtils(lhs_dsl_list, rhs_dsl_list)
  # Launch multiple threads to generate patterns
  if len(output_sizes) != 1:
    manager = multiprocessing.Manager()
    lhs_to_rhs_patterns = manager.dict()
    process_list = list()
    for output_size in output_sizes:
      process = multiprocessing.Process(target=pattern_gen, \
                                        args=(output_size, input_sizes, lhs_expr, lhs_dsl_list, \
                                          rhs_dsl_list, rhs_expr, lhs_to_rhs_patterns, synthesizer))
      process_list.append(process)
    for process in process_list:
      process.start()
    for process in process_list:
      process.join()
    for src_expr, dst_expr in lhs_to_rhs_patterns.items():
      if are_exprs_equal(src_expr, lhs_expr) and are_exprs_equal(dst_expr, rhs_expr):
        print("EQUAL EXPRS")
        return lhs_to_rhs_patterns
    lhs_to_rhs_patterns[lhs_expr] = rhs_expr
    return lhs_to_rhs_patterns
  else:
    assert len(output_sizes) == 1
    lhs_to_rhs_patterns = dict()
    pattern_gen(output_sizes[0], input_sizes, lhs_expr, lhs_dsl_list, \
                  rhs_dsl_list, rhs_expr, lhs_to_rhs_patterns, synthesizer)
    for src_expr, dst_expr in lhs_to_rhs_patterns.items():
      if are_exprs_equal(src_expr, lhs_expr) and are_exprs_equal(dst_expr, rhs_expr):
        print("EQUAL EXPRS")
        return lhs_to_rhs_patterns
    lhs_to_rhs_patterns[lhs_expr] = rhs_expr
    return lhs_to_rhs_patterns


def update_prefix_counter(string : str, prefixes_to_counters : dict):
  if string not in prefixes_to_counters:
    prefixes_to_counters[string] = 0
  else:
    prefixes_to_counters[string] += 1
  return prefixes_to_counters


def generalize_expr(expr : Context, prefixes_to_counters : dict = None):
  # Extract information such as precision, length, etc.
  if prefixes_to_counters == None:
    prefixes_to_counters = dict()
  generalized_expr = GeneralizedContext(expr)
  for idx, arg in enumerate(expr.context_args):
    if isinstance(arg, Context):
      generalized_expr.args.append(generalize_expr(arg, prefixes_to_counters))
    elif isinstance(arg, Reg):
      generalized_expr.args.append(arg)
    else:
      if idx == expr.in_vectsize_index:
        prefixes_to_counters = update_prefix_counter("in_vectsize", prefixes_to_counters)
        new_arg = "in_vectsize_" + str(prefixes_to_counters["in_vectsize"])
      elif idx == expr.out_vectsize_index:
        prefixes_to_counters = update_prefix_counter("out_vectsize", prefixes_to_counters)
        new_arg = "out_vectsize_" + str(prefixes_to_counters["out_vectsize"])
      elif idx == expr.in_lanesize_index:
        prefixes_to_counters = update_prefix_counter("in_lanesize", prefixes_to_counters)
        new_arg = "in_lanesize_" + str(prefixes_to_counters["in_lanesize"])
      elif idx == expr.out_lanesize_index:
        prefixes_to_counters = update_prefix_counter("out_lanesize", prefixes_to_counters)
        new_arg = "out_lanesize_" + str(prefixes_to_counters["out_lanesize"])
      elif idx == expr.in_precision_index:
        prefixes_to_counters = update_prefix_counter("in_precision", prefixes_to_counters)
        new_arg = "in_precision_" + str(prefixes_to_counters["in_precision"])
      elif idx == expr.out_precision_index:
        prefixes_to_counters = update_prefix_counter("out_precision", prefixes_to_counters)
        new_arg = "out_precision_" + str(prefixes_to_counters["out_precision"])
      else:
        generalized_expr.args.append(arg)
        continue
      generalized_expr.args.append(new_arg)
      generalized_expr.arg_names_to_val[new_arg] = arg
  return generalized_expr


def generalize_args(reg : Reg, ref_expr : GeneralizedContext):
  for ref_arg in ref_expr.args:
    if isinstance(ref_arg, GeneralizedContext):
      arg_names_to_val = generalize_args(reg, ref_arg)
      if arg_names_to_val != None:
        return arg_names_to_val
    elif isinstance(ref_arg, Reg):
      if ref_arg == reg:
        return ref_expr.arg_names_to_val
  return None


def get_generalized_arg_and_val(prefix : str, arg_names_to_val : dict):
  for key in arg_names_to_val.keys():
    if prefix in key:
      return key, arg_names_to_val[key]
  return None, None


def get_expr_to_arg_names_dict_for(expr : Context, reference_expr : GeneralizedContext,
                                   expr_to_arg_names_dict = dict()):
  for arg in expr.context_args:
    if isinstance(arg, Context):
      expr_to_arg_names_dict = get_expr_to_arg_names_dict_for(arg, reference_expr,\
                                                            expr_to_arg_names_dict)
    if isinstance(arg, Reg):
      arg_names_to_val = generalize_args(arg, reference_expr)
      if arg_names_to_val == None:
        continue
      expr_to_arg_names_dict[expr] = arg_names_to_val
  return expr_to_arg_names_dict


# Generalize an expression with respect to a given equivalent generalized expression
def generalize_expr_based_on_ref(expr : Context, reference_expr : GeneralizedContext,
                                 prefixes_to_counters : dict = None):
  # Extract information such as precision, length, etc. based on reference
  generalized_expr = GeneralizedContext(expr)
  print(expr.emit_context_expr_string())
  expr_to_arg_names_dict = get_expr_to_arg_names_dict_for(expr, reference_expr)
  print("expr_to_arg_names_dict:")
  print(expr_to_arg_names_dict)
  # Reiterate over context args recursively
  for idx, arg in enumerate(expr.context_args):
    if isinstance(arg, Context):
      generalized_expr.args.append(generalize_expr_based_on_ref(arg, reference_expr, \
                                                                prefixes_to_counters))
    elif isinstance(arg, Reg):
      generalized_expr.args.append(arg)
    else:
      if expr in expr_to_arg_names_dict.keys():
        arg_names_to_val = expr_to_arg_names_dict[expr]
        if idx == expr.in_vectsize_index:
          print("---in_vectsize")
          new_arg, val = get_generalized_arg_and_val("in_vectsize", arg_names_to_val)
          if new_arg == None and val == None:
            prefixes_to_counters = update_prefix_counter("in_vectsize", prefixes_to_counters)
            new_arg = "in_vectsize_" + str(prefixes_to_counters["in_vectsize"])
        elif idx == expr.out_vectsize_index:
          print("---out_vectsize")
          new_arg, val = get_generalized_arg_and_val("out_vectsize", arg_names_to_val)
          if new_arg == None and val == None:
            prefixes_to_counters = update_prefix_counter("out_vectsize", prefixes_to_counters)
            new_arg = "out_vectsize_" + str(prefixes_to_counters["out_vectsize"])
        elif idx == expr.in_lanesize_index:
          print("---in_lanesize")
          new_arg, val = get_generalized_arg_and_val("in_lanesize", arg_names_to_val)
          if new_arg == None and val == None:
            prefixes_to_counters = update_prefix_counter("in_lanesize", prefixes_to_counters)
            new_arg = "in_lanesize_" + str(prefixes_to_counters["in_lanesize"])
        elif idx == expr.out_lanesize_index:
          print("---out_lanesize")
          new_arg, val = get_generalized_arg_and_val("out_lanesize", arg_names_to_val)
          if new_arg == None and val == None:
            prefixes_to_counters = update_prefix_counter("out_lanesize", prefixes_to_counters)
            new_arg = "out_lanesize_" + str(prefixes_to_counters["out_lanesize"])
        elif idx == expr.in_precision_index:
          print("---in_precision")
          new_arg, val = get_generalized_arg_and_val("in_precision", arg_names_to_val)
          if new_arg == None and val == None:
            prefixes_to_counters = update_prefix_counter("in_precision", prefixes_to_counters)
            new_arg = "in_precision_" + str(prefixes_to_counters["in_precision"])
        elif idx == expr.out_precision_index:
          print("---out_precision")
          new_arg, val = get_generalized_arg_and_val("out_precision", arg_names_to_val)
          if new_arg == None and val == None:
            prefixes_to_counters = update_prefix_counter("out_precision", prefixes_to_counters)
            new_arg = "out_precision_" + str(prefixes_to_counters["out_precision"])
        else:
          generalized_expr.args.append(arg)
          continue
        print("new_arg:")
        print(new_arg)
        print("val:")
        print(val)
        print("arg:")
        print(arg)
        print("idx:")
        print(idx)
        if val != None:
          print("val.value:")
          print(val.value)
          print("arg.value:")
          print(arg.value)
          if val.value != arg.value:
            split_prefix = new_arg[::-1].split("_", 1)
            print("split_prefix:")
            print(split_prefix)
            prefix = split_prefix[1][::-1]
            print("prefix:")
            print(prefix)
            prefixes_to_counters = update_prefix_counter(prefix, prefixes_to_counters)
            new_arg = prefix + "_" + str(prefixes_to_counters[prefix])
        print("new_arg:")
        print(new_arg)
        print("arg.value:")
        print(arg.value)
        generalized_expr.args.append(new_arg)
        generalized_expr.arg_names_to_val[new_arg] = arg
      else:
        if idx == expr.in_vectsize_index:
          prefixes_to_counters = update_prefix_counter("in_vectsize", prefixes_to_counters)
          new_arg = "in_vectsize_" + str(prefixes_to_counters["in_vectsize"])
        elif idx == expr.out_vectsize_index:
          prefixes_to_counters = update_prefix_counter("out_vectsize", prefixes_to_counters)
          new_arg = "out_vectsize_" + str(prefixes_to_counters["out_vectsize"])
        elif idx == expr.in_lanesize_index:
          prefixes_to_counters = update_prefix_counter("in_lanesize", prefixes_to_counters)
          new_arg = "in_lanesize_" + str(prefixes_to_counters["in_lanesize"])
        elif idx == expr.out_lanesize_index:
          prefixes_to_counters = update_prefix_counter("out_lanesize", prefixes_to_counters)
          new_arg = "out_lanesize_" + str(prefixes_to_counters["out_lanesize"])
        elif idx == expr.in_precision_index:
          prefixes_to_counters = update_prefix_counter("in_precision", prefixes_to_counters)
          new_arg = "in_precision_" + str(prefixes_to_counters["in_precision"])
        elif idx == expr.out_precision_index:
          prefixes_to_counters = update_prefix_counter("out_precision", prefixes_to_counters)
          new_arg = "out_precision_" + str(prefixes_to_counters["out_precision"])
        else:
          generalized_expr.args.append(arg)
          continue
        print("new_arg:")
        print(new_arg)
        print("arg.value:")
        print(arg.value)
        generalized_expr.args.append(new_arg)
        generalized_expr.arg_names_to_val[new_arg] = arg
  return generalized_expr


# Generalize expressions on the same side
def generalize_same_side_exprs(exprs : list, prefixes_to_counters : dict = dict()):
  print("generalize_same_side_exprs")
  if len(exprs) < 2:
    return False
  expr_args_list = list()
  for expr in exprs:
    expr_args_list.append(expr.args)
  expr_args_tuple = tuple(expr_args_list)
  for arg_idx, args in enumerate(zip(*expr_args_tuple)):
    for idx in range(1, len(args)):
      if type(args[idx - 1]) != type(args[idx]):
        return False
    if isinstance(args[0], Reg):
      #for idx in range(1, len(args)):
      #  if args[idx - 1].index != args[idx].index:
      #    return False
      continue
    if isinstance(args[0], str):
      for idx in range(1, len(args)):
        if args[idx - 1] != args[idx]:
          return False
      continue
    if isinstance(args[0], GeneralizedContext):
      if generalize_same_side_exprs(list(args), prefixes_to_counters) == False:
        return False
      continue
    assert isinstance(args[0], Integer) == True
    args_are_equal = False
    for idx in range(1, len(args)):
      if args_are_equal == True:
        if args[idx - 1].value != args[idx].value:
          args_are_equal = False
          break
      else:
        if args[idx - 1].value == args[idx].value:
          args_are_equal = True
    if args_are_equal == True:
      # Abstract away these constants
      update_prefix_counter("arg", prefixes_to_counters)
      new_arg_name = "arg_" + str(prefixes_to_counters["arg"])
      for expr in exprs:
        expr.arg_names_to_val[new_arg_name] = expr.args[arg_idx]
        expr.args[arg_idx] = new_arg_name
      continue
    # Compare this constant relative to other known abstracted constants
    assert len(args) == len(exprs)
    var_to_arg_ratio = dict()
    excluded_vars = set()
    for idx in range(len(args)):
      expr = exprs[idx]
      for arg_names, val in expr.arg_names_to_val.items():
        if isinstance(val, str):
          continue
        if arg_names in excluded_vars:
          continue
        if "/" in arg_names:
          excluded_vars.add(arg_names)
          continue
        print("arg_names:")
        print(arg_names)
        print("val:")
        print(val.value)
        if arg_names not in var_to_arg_ratio:
          if val.value >= args[idx].value:
            if args[idx].value == 0:
              excluded_vars.add(arg_names)
              continue
            var_to_arg_ratio[arg_names] = int(val.value / args[idx].value)
          else:
            if val.value == 0:
              excluded_vars.add(arg_names)
              continue
            var_to_arg_ratio[arg_names] =  int(args[idx].value / val.value)
        if val.value >= args[idx].value:
          if args[idx].value == 0:
            excluded_vars.add(arg_names)
            del var_to_arg_ratio[arg_names]
            continue
          if var_to_arg_ratio[arg_names] != int(val.value / args[idx].value):
            excluded_vars.add(arg_names)
            del var_to_arg_ratio[arg_names]
        else:
          if val.value == 0:
            excluded_vars.add(arg_names)
            del var_to_arg_ratio[arg_names]
            continue
          if var_to_arg_ratio[arg_names] != int(args[idx].value / val.value):
            excluded_vars.add(arg_names)
            del var_to_arg_ratio[arg_names]
    # Abstract away the constant if some relationship is established
    for idx in range(len(args)):
      expr = exprs[idx]
      for var, arg_ratio in var_to_arg_ratio.items():
        if arg_ratio == 1:
          if isinstance(expr.args[arg_idx], str):
            new_arg_name = expr.args[arg_idx]
          else:
            new_arg_name = var
        else:
          new_arg_name = "(/ " + var + " " + str(arg_ratio) + ")"
        expr.arg_names_to_val[new_arg_name] = expr.args[arg_idx]
        expr.args[arg_idx] = new_arg_name
    # Abstract away constants and express them in terms of two arguments.
    # First create pairs of tuples that are worth trying
    tuple_list = list()
    for idx in range(len(args)):
      expr = exprs[idx]
      if idx == 0:
        arg_names = expr.arg_names_to_val.keys()
        for idx in range(len(arg_names)):
          if "/" in arg_names[idx]:
            continue
          for check_idx in range(len(arg_names)):
            if check_idx == idx:
              continue
            if "/" in arg_names[check_idx]:
              continue
            if expr.arg_names_to_val[arg_names[idx]].value \
              > expr.arg_names_to_val[arg_names[check_idx]].value:
              if expr.arg_names_to_val[arg_names[check_idx]].value == 0:
                continue
              tuple_list.append((arg_names[idx], arg_names[check_idx]))
            elif expr.arg_names_to_val[arg_names[idx]].value \
              < expr.arg_names_to_val[arg_names[check_idx]].value:
              if expr.arg_names_to_val[arg_names[idx]].value == 0:
                continue
              tuple_list.append((arg_names[check_idx], arg_names[idx]))
        break
    print("tuple_list:")
    print(tuple_list)
    tuple_to_arg_ratio = dict()
    excluded_tuples = set()
    for idx in range(len(args)):
      expr = exprs[idx]
      for arg_tuple in tuple_list:
        if arg_tuple in excluded_tuples:
          continue
        val = int(expr.arg_names_to_val[arg_tuple[0]].value \
                / expr.arg_names_to_val[arg_tuple[1]].value)
        if val == 1:
          excluded_tuples.add(arg_tuple)
          continue
        if arg_tuple not in tuple_to_arg_ratio:
          if val >= args[idx].value:
            if args[idx].value == 0:
              excluded_tuples.add(arg_tuple)
              continue
            tuple_to_arg_ratio[arg_tuple] = int(val / args[idx].value)
          else:
            if val == 0:
              excluded_tuples.add(arg_tuple)
              continue
            tuple_to_arg_ratio[arg_tuple] =  int(args[idx].value / val)
        if val >= args[idx].value:
          if args[idx].value == 0:
            excluded_tuples.add(arg_tuple)
            del tuple_to_arg_ratio[arg_tuple]
            continue
          if tuple_to_arg_ratio[arg_tuple] != int(val / args[idx].value):
            excluded_tuples.add(arg_tuple)
            del tuple_to_arg_ratio[arg_tuple]
        else:
          if val == 0:
            excluded_tuples.add(arg_tuple)
            del tuple_to_arg_ratio[arg_tuple]
            continue
          if tuple_to_arg_ratio[arg_tuple] != int(args[idx].value / val):
            excluded_tuples.add(arg_tuple)
            del tuple_to_arg_ratio[arg_tuple]
    # Abstract away constants and express them in terms of two arguments.
    for idx in range(len(args)):
      expr = exprs[idx]
      for arg_tuple, arg_ratio in tuple_to_arg_ratio.items():
        new_arg_name = "(/ " + arg_tuple[0] + " " + arg_tuple[1] + ")"
        if arg_ratio != 1:
          new_arg_name = "(/ " + new_arg_name + " " + str(arg_ratio) + ")"
        expr.arg_names_to_val[new_arg_name] = expr.args[arg_idx]
        expr.args[arg_idx] = new_arg_name
  return True


# Function to check if two generalized expressions are equivalent.
def are_generalized_exprs_equal(expr1 : GeneralizedContext, expr2 : GeneralizedContext):
  if len(expr1.args) != len(expr2.args):
    return False
  for arg1, arg2 in zip(expr1.args, expr2.args):
    if type(arg1) != type(arg2):
      return False
    if isinstance(arg1, Context):
      if are_exprs_equal(arg1, arg2) == False:
        return False
    elif isinstance(arg1, Reg):
      if arg1.index != arg2.index:
        return False
    elif isinstance(arg1, Integer):
      if arg1.value != arg2.value:
        return False
    else:
      if arg1 != arg2:
        return False
  return True


# Redundant generalized expressions can be removed
def remove_redundant_rules(exprs1 : list, exprs2 : list):
  print("REMOVE REDUNDANT RULES")
  # Find redudant rules
  remove_list = set()
  assert len(exprs1) == len(exprs2)
  for idx in range(len(exprs1)):
    if idx in remove_list:
      continue
    for check_idx in range(len(exprs1)):
      if check_idx in remove_list:
        continue
      if idx == check_idx:
        continue
      if are_generalized_exprs_equal(exprs1[idx], exprs1[check_idx]) == True:
        if are_generalized_exprs_equal(exprs2[idx], exprs2[check_idx]) == True:
          remove_list.add(check_idx)
  # Remove redundant rules
  new_exprs1 = list()
  new_exprs2 = list()
  for idx in range(len(exprs1)):
     if idx in remove_list:
       continue
     new_exprs1.append(exprs1[idx])
     new_exprs2.append(exprs2[idx])
  return new_exprs1, new_exprs2


def generalize_rule(lhs_to_rhs_patterns : dict):
  print("GENERALIZING RULE")
  print("lhs_to_rhs_patterns:")
  print(lhs_to_rhs_patterns)
  for lhs_expr, rhs_expr in lhs_to_rhs_patterns.items():
    print(lhs_expr.emit_context_expr_string())
    print(rhs_expr.emit_context_expr_string())
  print("\n\n--------------------------")
  # Generalize lhs first and then rhs vis-a-vis the lhs
  generalized_lhs_exprs = list()
  generalized_rhs_exprs = list()
  for lhs_expr, rhs_expr in lhs_to_rhs_patterns.items():
    print(lhs_expr.emit_context_expr_string())
    print(rhs_expr.emit_context_expr_string())
    prefixes_to_counters = dict()
    generalized_lhs_expr = generalize_expr(lhs_expr, prefixes_to_counters)
    generalized_lhs_exprs.append(generalized_lhs_expr)
    print("\ngeneralized_lhs_expr:")
    generalized_lhs_expr.print()
    generalized_rhs_expr = generalize_expr_based_on_ref(rhs_expr, generalized_lhs_expr, \
                                                        prefixes_to_counters)
    generalized_rhs_exprs.append(generalized_rhs_expr)
    print("generalized_rhs_expr:")
    generalized_rhs_expr.print()
  # Generalize across generalized same side expressions
  generalize_same_side_exprs(generalized_lhs_exprs)
  generalize_same_side_exprs(generalized_rhs_exprs)
  print("\n\n\n\n\ngeneralized_lhs_exprs:")
  for expr in generalized_lhs_exprs:
    expr.print()
  print("\n\n\n\ngeneralized_rhs_exprs:")
  for expr in generalized_rhs_exprs:
    expr.print()
  # Remove redundant expressions
  generalized_lhs_exprs, generalized_rhs_exprs = \
    remove_redundant_rules(generalized_lhs_exprs, generalized_rhs_exprs)
  print("\n\n\n\n\ngeneralized_lhs_exprs:")
  for expr in generalized_lhs_exprs:
    expr.print()
  print("\n\n\n\ngeneralized_rhs_exprs:")
  for expr in generalized_rhs_exprs:
    expr.print()
  return generalized_lhs_exprs, generalized_rhs_exprs


def generalize_rules(lhs_expr : Context, lhs_dsl_list : list,
                      rhs_expr : Context, rhs_dsl_list : list):
  assert isinstance(rhs_expr, Context) == True
  assert isinstance(lhs_expr, Context) == True
  print("len(lhs_dsl_list):")
  print(len(lhs_dsl_list))
  print("len(rhs_dsl_list):")
  print(len(rhs_dsl_list))
  lhs_to_rhs_patterns = generate_candidates(lhs_expr, lhs_dsl_list, rhs_expr, rhs_dsl_list)
  generalized_lhs_exprs, generalized_rhs_exprs = generalize_rule(lhs_to_rhs_patterns)
  # Zip results to get list of lhs and rhs of rules
  return zip(generalized_lhs_exprs, generalized_rhs_exprs)


#def generalize_pattern(pattern : Pattern):
#  rhs_expr = pattern.src_expr
#  lhs_expr = pattern.target_expr
#  #generalize_rules(lhs_expr, rhs_expr)


def test1():
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


def test2():
  from sema.hex_swizzles_v3 import hvx_swizzles
  from sema.hexsemantics import hvx_semantics

  # Uncomment below line to keep intermediate racket files
  #keep_temporary_files()

  # Parse the dictionay into a list of DSLInstruction types
  #joint_dict = hvx_swizzles | hvx_semantics
  joint_dict = {**hvx_swizzles, **hvx_semantics}
  hvx_dsl_list = parse_dict(joint_dict)

  rhs_expr_str = "(hvx_swizzle_43 (hexagon_V6_vpackwuh_sat_128B (reg (bv #x00 8)) (reg (bv #x01 8)) \
                  1024 1024 0 512 16 0 512 16 0 32 1 32 0 32 1 16 0) 1024 32 0 32 16 32 2 0)"
  lhs_expr_str = "(hexagon_V6_vsathub_128B (reg (bv #x00 8)) (reg (bv #x01 8)) \
                  1024 1024 0 512 16 16 0 32 1 0 0)"

  lhs_expr_ctx = read_string_to_dsl(lhs_expr_str, hvx_dsl_list)
  rhs_expr_ctx = read_string_to_dsl(rhs_expr_str, hvx_dsl_list)

  print("="*5, "Pretty Printing Expressions", "="*5)
  print(lhs_expr_ctx.emit_context_expr_string())
  print(rhs_expr_ctx.emit_context_expr_string())

  generalize_rules(lhs_expr_ctx, hvx_dsl_list, rhs_expr_ctx, hvx_dsl_list)


def test3():
  from sema.hex_swizzles_v3 import hvx_swizzles
  from sema.hexsemantics_new import semantics as hvx_semantics

  # Uncomment below line to keep intermediate racket files
  #keep_temporary_files()

  # Parse the dictionay into a list of DSLInstruction types
  #joint_dict = hvx_swizzles | hvx_semantics
  joint_dict = {**hvx_swizzles, **hvx_semantics}
  hvx_dsl_list = parse_dict(joint_dict)

  lhs_expr_str = "(hvx_swizzle_43 (hexagon_V6_vpackwuh_sat_128B (reg (bv #x00 8)) (reg (bv #x01 8)) \
                  1024 1024 0 512 16 0 512 16 0 32 1 32 0 32 1 16 0) 1024 32 0 32 16 32 2 0)"
  rhs_expr_str = "(hexagon_V6_vsathub_128B (reg (bv #x00 8)) (reg (bv #x01 8)) \
                  1024 1024 0 512 16 16 0 32 1 0 0)"

  lhs_expr_ctx = read_string_to_dsl(lhs_expr_str, hvx_dsl_list)
  rhs_expr_ctx = read_string_to_dsl(rhs_expr_str, hvx_dsl_list)

  print("="*5, "Pretty Printing Expressions", "="*5)
  print(lhs_expr_ctx.emit_context_expr_string())
  print(rhs_expr_ctx.emit_context_expr_string())

  generalize_rules(lhs_expr_ctx, hvx_dsl_list, rhs_expr_ctx, hvx_dsl_list)



def test_halide():
  from sema.halide_decomposed import halide_decomposed as halide_semantics

  # Uncomment below line to keep intermediate racket files
  keep_temporary_files()

  # Parse the dictionay into a list of DSLInstruction types
  halide_dsl_list = parse_dict(halide_semantics)

  # This rule is for splitting vector add on large vectors into concatenation of
  # smaller vector adds using slice vector.
  src_halide_str = "(typed:vec-add (reg (bv #x00 8)) (reg (bv #x01 8)) 64 1024)"
  dst_halide_str = "(typed:concat_vectors (typed:vec-add (typed:slice_vectors (reg (bv #x00 8)) 8 1 8 64 1024) (typed:slice_vectors (reg (bv #x01 8)) 8 1 8 64 1024) 64 512) (typed:vec-add (typed:slice_vectors (reg (bv #x00 8)) 0 1 8 64 1024) (typed:slice_vectors (reg (bv #x01 8)) 0 1 8 64 1024) 64 512) 64 512)"

  src_expr_ctx = read_string_to_dsl(src_halide_str, halide_dsl_list)
  dst_expr_ctx = read_string_to_dsl(dst_halide_str, halide_dsl_list)

  print("="*5, "Pretty Printing Expressions", "="*5)
  print(src_expr_ctx.emit_context_expr_string())
  print(dst_expr_ctx.emit_context_expr_string())

  generalize_rules(src_expr_ctx, halide_dsl_list, dst_expr_ctx, halide_dsl_list)


if __name__ == "__main__":
  test_halide()
  print("\n\n\n\n\n\n\n")
  sys.exit()
  test1()
  print("\n\n\n\n\n\n\n")
  test2()
  print("\n\n\n\n\n\n\n")
  test3()
  
