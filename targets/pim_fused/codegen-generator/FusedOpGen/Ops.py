from abc import ABC, abstractmethod
from enum import IntEnum
import string

class Signedness(IntEnum):
    NOSIGN = -1
    SIGNED = 1
    UNSIGNED = 0




class BaseOp(ABC):
    def __init__(self, ID):
        super().__init__()
        self.ID = ID
        self.name = "BaseOp"
        self.commutative = False
        self.operands = []
        self.bitwidth = None
        self.output_size = None
        self.signedness = None
        self.is_root = False


    @classmethod
    def get_pim_api_name(cls):
        return ""


    @classmethod
    def supports_scalar_ops(cls):
        return False

    @classmethod
    def get_output_size_for_operand_sizes(cls, operands_size, operands_bitwidth):
        pass

    @classmethod
    def get_input_sizes_for_output_size(cls, output_size, output_bw):
        pass

    @classmethod
    def get_input_bitwidth_for_output_bitwidth(cls, output_size, output_bw):
        pass

    @abstractmethod
    def print_op(self, indent_level = 0):
        pass

    @abstractmethod
    def emit_semantics_pseudocode(self, context):
        pass

    def get_loop_index_var_name(self, context):
        return context["loop_index_var"]

    def get_loop_iterations(self):
        return self.output_size // self.bitwidth

    def get_registers(self):
        if isinstance(self, Register):
            return [self]
        else:
            regs = []
            for opnd in self.operands:
                regs += opnd.get_registers()
            return regs

    def set_bitwidth(self, bw):
        self.bitwidth = bw

    def set_signedness(self, s):
        self.signedness = s

    def set_is_root(self, b):
        self.is_root = b

    def get_depth(self):
        if len(self.operands) == 0:
            return 0
        else:
            return 1 + max([opnd.get_depth() for opnd in self.operands])

    def get_nested_operands(self):
        opnd_list = []
        for opnd in self.operands:
            opnd_list += opnd.get_nested_operands()
        opnd_list += [self]

        return opnd_list




class Register(BaseOp):
    def __init__(self, ID, index, bitwidth = 8, size = 1024):
        super().__init__(ID)
        self.name = string.ascii_lowercase[index]
        self.index = index
        self.commutative = False
        self.operands = []
        self.bitwidth = bitwidth
        self.signedness = Signedness.NOSIGN
        self.output_size = size


    def get_num_elements(self):
        return self.output_size // self.bitwidth

    def set_index(self, index):
        self.index = index
        self.name = string.ascii_lowercase[index]

    def print_op(self, indent_level = 0):
        return ("\t" * indent_level) + f"({self.name} {self.bitwidth} {self.output_size})\n"

    @classmethod
    def get_output_size_for_operand_sizes(cls, operands_size, operands_bitwidth):
        return operands_size[0]

    @classmethod
    def get_input_bitwidth_for_output_bitwidth(cls, output_size, output_bw):
        return [output_bw]

    @classmethod
    def get_input_sizes_for_output_size(cls, output_size, output_bw):
        return [output_size]


    def emit_semantics_pseudocode(self, context):
        loop_idx = self.get_loop_index_var_name(context)
        end_offset = self.bitwidth - 1

        low_offset_name = f"var_{self.ID}_low"
        if self.bitwidth == self.output_size:
            low_offset = f"{low_offset_name} = {0} * {self.bitwidth}"
            usage = f"{self.name}[{low_offset_name}+{end_offset}:{low_offset_name}]"
        else:
            low_offset = f"{low_offset_name} = {loop_idx} * {self.bitwidth}"
            usage = f"{self.name}[{low_offset_name}+{end_offset}:{low_offset_name}]"
        definitions = [low_offset]
        context[self.ID] = usage
        return definitions, context




class BroadcastOp(BaseOp):
    def __init__(self, ID, Opnd, factor):
        super().__init__(ID)
        self.name = "BroadcastOp"
        assert isinstance(Opnd, Register), "Broadcast currently only supports scalars"
        self.operands = [Opnd]
        self.factor = factor
        self.bitwidth = Opnd.bitwidth
        self.output_size = self.factor * Opnd.bitwidth
        self.signedness = Opnd.signedness


    @classmethod
    def get_pim_api_name(cls):
        return "pimBroadcastInt"

    @classmethod
    def supports_scalar_ops(cls):
        return False

    @classmethod
    def get_output_size_for_operand_sizes(cls, operands_size, operands_bitwidth):
        assert False, "Can only know output size based on object instance"
        return operands_size[0]

    @classmethod
    def get_input_bitwidth_for_output_bitwidth(cls, output_size, output_bw):
        return [output_bw]

    @classmethod
    def get_input_sizes_for_output_size(cls, output_size, output_bw):
        return [output_bw]


    def print_op(self, indent_level = 0):
        print_opnd = self.operands[0].print_op(indent_level=indent_level+1)
        return ("\t" * indent_level) + f"({self.name} {print_opnd} {self.factor})\n"

    def emit_semantics_pseudocode(self, context):
        loop_idx = self.get_loop_index_var_name(context)
        end_offset = self.bitwidth - 1

        Opnd = self.operands[0]
        usage = f"{Opnd.name}[{end_offset}:0]"
        if isinstance(Opnd, Register):
            context[self.ID] = usage

        op_definitions = []

        if self.is_root:
            low_offset_name = f"var_{self.ID}_low"
            low_offset = f"{low_offset_name} = {loop_idx} * {self.bitwidth}"
            output_name = f"dst[{low_offset_name}+{end_offset}:{low_offset_name}]"
            stmt = f"{output_name} = {usage}"
            op_definitions = [low_offset, stmt]


        return op_definitions, context



class ExtendOp(BaseOp):
    def __init__(self, ID, Opnd, is_sign_extend = False):
        super().__init__(ID)
        self.name = "ExtendOp"
        self.operands = [Opnd]
        self.bitwidth = Opnd.bitwidth * 2
        self.output_size =  Opnd.output_size * 2
        self.signedness = Signedness.SIGNED if is_sign_extend else Signedness.UNSIGNED
        self.is_sign_extend = is_sign_extend



    @classmethod
    def get_pim_api_name(cls):
        return "pimConvertType"

    @classmethod
    def supports_scalar_ops(cls):
        return False

    @classmethod
    def get_output_size_for_operand_sizes(cls, operands_size, operands_bitwidth):
        assert False, "Can only know output size based on object instance"
        return operands_size[0] * 2

    @classmethod
    def get_input_bitwidth_for_output_bitwidth(cls, output_size, output_bw):
        return [output_bw // 2]

    @classmethod
    def get_input_sizes_for_output_size(cls, output_size, output_bw):
        return [output_size // 2]


    def print_op(self, indent_level = 0):
        print_opnd = self.operands[0].print_op(indent_level=indent_level+1)
        return ("\t" * indent_level) + f"({self.name} {print_opnd})\n"

    def emit_semantics_pseudocode(self, context):
        loop_idx = self.get_loop_index_var_name(context)
        end_offset = self.bitwidth - 1
        defns_opnd_A, context_A = self.operands[0].emit_semantics_pseudocode(context)

        A_usage = context_A[self.operands[0].ID]

        extend_op_base = "SignExtend" if self.is_sign_extend else "ZeroExtend"
        extend_op = f"{extend_op_base}{self.bitwidth}"


        op_definitions = []

        if self.is_root:
            low_offset_name = f"var_{self.ID}_low"
            low_offset = f"{low_offset_name} = {loop_idx} * {self.bitwidth}"
            op_definitions = [low_offset]
            output_name = f"dst[{low_offset_name}+{end_offset}:{low_offset_name}]"
        else:
            output_name = f"var_{self.ID}"

        defn = f"{output_name} = {extend_op}({A_usage})"
        op_definitions += [defn]

        context_A[self.ID] = output_name

        definitions = defns_opnd_A +  op_definitions

        return definitions, context_A


class ZeroExtendOp(ExtendOp):
    def __init__(self, ID, Opnd):
        super().__init__(ID, Opnd, is_sign_extend = False)
        self.name = "ZeroExtendOp"

class SignExtendOp(ExtendOp):
    def __init__(self, ID, Opnd):
        super().__init__(ID, Opnd, is_sign_extend = True)
        self.name = "SignExtendOp"




class TruncateOp(BaseOp):
    def __init__(self, ID, Opnd):
        super().__init__(ID)
        self.name = "TruncateOp"
        self.operands = [Opnd]
        self.bitwidth = Opnd.bitwidth // 2
        self.output_size =  Opnd.output_size //  2
        self.signedness = Signedness.NOSIGN

    @classmethod
    def get_pim_api_name(cls):
        return "pimConvertType"

    @classmethod
    def supports_scalar_ops(cls):
        return False

    @classmethod
    def get_output_size_for_operand_sizes(cls, operands_size, operands_bitwidth):
        assert False, "Can only know output size based on object instance"
        return operands_size[0] // 2

    @classmethod
    def get_input_bitwidth_for_output_bitwidth(cls, output_size, output_bw):
        return [output_bw * 2]

    @classmethod
    def get_input_sizes_for_output_size(cls, output_size, output_bw):
        return [output_size * 2]


    def print_op(self, indent_level = 0):
        print_opnd = self.operands[0].print_op(indent_level=indent_level+1)
        return ("\t" * indent_level) + f"({self.name} {print_opnd})\n"

    def emit_semantics_pseudocode(self, context):
        loop_idx = self.get_loop_index_var_name(context)
        end_offset = self.bitwidth - 1
        defns_opnd_A, context_A = self.operands[0].emit_semantics_pseudocode(context)

        A_usage = context_A[self.operands[0].ID]

        extend_op_base = "Truncate"
        extend_op = f"{extend_op_base}{self.bitwidth}"


        op_definitions = []

        if self.is_root:
            low_offset_name = f"var_{self.ID}_low"
            low_offset = f"{low_offset_name} = {loop_idx} * {self.bitwidth}"
            op_definitions = [low_offset]
            output_name = f"dst[{low_offset_name}+{end_offset}:{low_offset_name}]"
        else:
            output_name = f"var_{self.ID}"

        defn = f"{output_name} = {extend_op}({A_usage})"
        op_definitions += [defn]

        context_A[self.ID] = output_name

        definitions = defns_opnd_A +  op_definitions

        return definitions, context_A




class SelectOp(BaseOp):
    def __init__(self, ID, OpndA, OpndB, OpndC):
        super().__init__(ID)
        self.name = "SelectOp"
        self.operands = [OpndA, OpndB, OpndC]
        self.bitwidth = OpndB.bitwidth
        self.output_size = OpndB.output_size
        self.signedness = Signedness.NOSIGN

    @classmethod
    def get_pim_api_name(cls):
        return "pimCondSelect"


    def print_op(self, indent_level = 0):
        return ("\t" * indent_level) + f"({self.name}\n{self.operands[0].print_op(indent_level = indent_level+1)} {self.operands[1].print_op(indent_level = indent_level+1)}  {self.operands[2].print_op(indent_level = indent_level+1)}   )\n"


    @classmethod
    def get_output_size_for_operand_sizes(cls, operands_size, operands_bitwidth):
        return (operands_size[1])


    @classmethod
    def get_operator(cls):
        return None
    @classmethod
    def get_operator_is_function(cls):
        return None

    @classmethod
    def get_input_bitwidth_for_output_bitwidth(cls, output_size, output_bw):
        return [ComparisonBinaryOp.comp_bitwidth, output_bw, output_bw]

    @classmethod
    def get_input_sizes_for_output_size(cls, output_size, output_bw):
        lanes = output_size // output_bw

        return [int(ComparisonBinaryOp.comp_bitwidth) * lanes] + [output_size, output_size]

    def emit_semantics_pseudocode(self, context):
        loop_idx = self.get_loop_index_var_name(context)
        end_offset = self.bitwidth - 1
        defns_opnd_A, context_A = self.operands[0].emit_semantics_pseudocode(context)
        defns_opnd_B, context_B = self.operands[1].emit_semantics_pseudocode(context_A)
        defns_opnd_C, context_C = self.operands[2].emit_semantics_pseudocode(context_B)

        A_usage = context_C[self.operands[0].ID]
        B_usage = context_C[self.operands[1].ID]
        C_usage = context_C[self.operands[2].ID]


        op_definitions = []

        if self.is_root:
            low_offset_name = f"var_{self.ID}_low"
            low_offset = f"{low_offset_name} = {loop_idx} * {self.bitwidth}"
            op_definitions = [low_offset]
            output_name = f"dst[{low_offset_name}+{end_offset}:{low_offset_name}]"
        else:
            output_name = f"var_{self.ID}"

        defn = f"{output_name} = ({A_usage} == 1) ? {B_usage} : {C_usage}"
        op_definitions += [defn]
        context_C[self.ID] = output_name

        definitions = defns_opnd_A + defns_opnd_B + defns_opnd_C +op_definitions

        return definitions, context_C


class ShiftOp(BaseOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID)
        self.name = "ShiftOp"
        self.operands = [OpndA, OpndB]
        self.bitwidth = OpndA.bitwidth
        self.output_size = OpndA.output_size
        self.signedness = OpndA.signedness

    @classmethod
    def get_pim_api_name(cls):
        return "pimShift"


    def print_op(self, indent_level = 0):
        return ("\t" * indent_level) + f"({self.name}\n{self.operands[0].print_op(indent_level = indent_level+1)} {self.operands[1].print_op(indent_level = indent_level+1)}     )\n"


    @classmethod
    def get_output_size_for_operand_sizes(cls, operands_size, operands_bitwidth):
        return (operands_size[1])


    @classmethod
    def get_operator(cls):
        return None
    @classmethod
    def get_operator_is_function(cls):
        return None

    @classmethod
    def get_input_bitwidth_for_output_bitwidth(cls, output_size, output_bw):
        return [output_bw, output_bw]

    @classmethod
    def get_input_sizes_for_output_size(cls, output_size, output_bw):
        return [output_size] + [output_bw]

    def emit_semantics_pseudocode(self, context):
        loop_idx = self.get_loop_index_var_name(context)
        end_offset = self.bitwidth - 1
        defns_opnd_A, context_A = self.operands[0].emit_semantics_pseudocode(context)
        defns_opnd_B, context_B = self.operands[1].emit_semantics_pseudocode(context_A)

        A_usage = context_B[self.operands[0].ID]
        B_usage = context_B[self.operands[1].ID]


        op_definitions = []

        if self.is_root:
            low_offset_name = f"var_{self.ID}_low"
            low_offset = f"{low_offset_name} = {loop_idx} * {self.bitwidth}"
            op_definitions = [low_offset]
            output_name = f"dst[{low_offset_name}+{end_offset}:{low_offset_name}]"
        else:
            output_name = f"var_{self.ID}"


        operator = self.get_operator()

        defn = f"{output_name} = {A_usage} {operator} {B_usage}"
        op_definitions += [defn]
        context_B[self.ID] = output_name

        definitions = defns_opnd_A + defns_opnd_B +op_definitions

        return definitions, context_B

class LeftShiftOp(ShiftOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID, OpndA, OpndB)
        self.name = "LeftShiftOp"

    @classmethod
    def get_pim_api_name(cls):
        return "pimShiftBitsLeft"

    @classmethod
    def get_operator(cls):
        return "<<"
    @classmethod
    def get_operator_is_function(cls):
        return False

class RightShiftOp(ShiftOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID, OpndA, OpndB)
        self.name = "RightShiftOp"

    @classmethod
    def get_pim_api_name(cls):
        return "pimShiftBitsRight"

    @classmethod
    def get_operator(cls):
        return ">>"
    @classmethod
    def get_operator_is_function(cls):
        return False

class ComparisonBinaryOp(BaseOp):
    comp_bitwidth = 1

    def __init__(self, ID, OpndA, OpndB, operator = "+"):
        super().__init__(ID)
        self.name = "ComparisonBinaryOp"
        self.operands = [OpndA, OpndB]
        self.bitwidth = ComparisonBinaryOp.comp_bitwidth
        self.output_size = (OpndA.output_size // OpndA.bitwidth) * self.bitwidth
        self.operator = operator


    def print_op(self, indent_level = 0):
        return ("\t" * indent_level) + f"({self.name}\n{self.operands[0].print_op(indent_level = indent_level+1)} {self.operands[1].print_op(indent_level = indent_level+1)})\n"


    @classmethod
    def get_output_size_for_operand_sizes(cls, operands_size, operands_bitwidth):
        return (operands_size[0] // operands_bitwidth) * ComparisonBinaryOp.comp_bitwidth


    @classmethod
    def get_operator(cls):
        return None
    @classmethod
    def get_operator_is_function(cls):
        return None

    @classmethod
    def get_input_bitwidth_for_output_bitwidth(cls, output_size, output_bw):
        return None

    @classmethod
    def get_input_sizes_for_output_size(cls, output_size, output_bw):
        return None

    def emit_semantics_pseudocode(self, context):
        loop_idx = self.get_loop_index_var_name(context)
        end_offset = self.bitwidth - 1
        defns_opnd_A, context_A = self.operands[0].emit_semantics_pseudocode(context)
        defns_opnd_B, context_B = self.operands[1].emit_semantics_pseudocode(context_A)

        A_usage = context_B[self.operands[0].ID]
        B_usage = context_B[self.operands[1].ID]


        op_definitions = []

        if self.is_root:
            low_offset_name = f"var_{self.ID}_low"
            low_offset = f"{low_offset_name} = {loop_idx} * {self.bitwidth}"
            op_definitions = [low_offset]
            output_name = f"dst[{low_offset_name}+{end_offset}:{low_offset_name}]"
        else:
            output_name = f"var_{self.ID}"

        defn = f"{output_name} = ({A_usage} {self.operator} {B_usage}) ? 1 : 0"
        op_definitions += [defn]
        context_B[self.ID] = output_name

        definitions = defns_opnd_A + defns_opnd_B + op_definitions

        return definitions, context_B


class LTOp(ComparisonBinaryOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID, OpndA, OpndB, operator = "<")
        self.name = "LTOp"
        self.signedness = Signedness.SIGNED

    @classmethod
    def get_pim_api_name(cls):
        return "pimLT"

class EQOp(ComparisonBinaryOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID, OpndA, OpndB, operator = "==")
        self.name = "EQOp"
        self.signedness = Signedness.NOSIGN
        self.commutative = True

    @classmethod
    def get_pim_api_name(cls):
        return "pimEQ"

class UniformBinaryOp(BaseOp):
    def __init__(self, ID, OpndA, OpndB, operator = "+", operator_is_function = False):
        super().__init__(ID)
        self.name = "UniformBinaryOp"
        self.operands = [OpndA, OpndB]
        self.bitwidth = OpndA.bitwidth
        self.output_size = OpndA.output_size
        self.operator = operator
        self.operator_is_function = operator_is_function


    def print_op(self, indent_level = 0):
        return ("\t" * indent_level) + f"({self.name}\n{self.operands[0].print_op(indent_level = indent_level+1)} {self.operands[1].print_op(indent_level = indent_level+1)})\n"


    @classmethod
    def get_output_size_for_operand_sizes(cls, operands_size, operands_bitwidth):
        return operands_size[0]


    @classmethod
    def get_operator(cls):
        return None
    @classmethod
    def get_operator_is_function(cls):
        return None

    @classmethod
    def get_input_bitwidth_for_output_bitwidth(cls, output_size, output_bw):
        return [output_bw, output_bw]

    @classmethod
    def get_input_sizes_for_output_size(cls, output_size, output_bw):
        return [output_size, output_size]

    def emit_semantics_pseudocode(self, context):
        loop_idx = self.get_loop_index_var_name(context)
        end_offset = self.bitwidth - 1
        defns_opnd_A, context_A = self.operands[0].emit_semantics_pseudocode(context)
        defns_opnd_B, context_B = self.operands[1].emit_semantics_pseudocode(context_A)

        A_usage = context_B[self.operands[0].ID]
        B_usage = context_B[self.operands[1].ID]


        op_definitions = []

        if self.is_root:
            low_offset_name = f"var_{self.ID}_low"
            low_offset = f"{low_offset_name} = {loop_idx} * {self.bitwidth}"
            op_definitions = [low_offset]
            output_name = f"dst[{low_offset_name}+{end_offset}:{low_offset_name}]"
        else:
            output_name = f"var_{self.ID}"

        if self.operator_is_function:
            defn = f"{output_name} = {self.operator}({A_usage}, {B_usage})"
        else:
            defn = f"{output_name} = {A_usage} {self.operator} {B_usage}"
        op_definitions += [defn]
        context_B[self.ID] = output_name

        definitions = defns_opnd_A + defns_opnd_B + op_definitions

        return definitions, context_B


class UniformUnaryOp(BaseOp):
    def __init__(self, ID, OpndA,  operator = "~", operator_is_function = False):
        super().__init__(ID)
        self.name = "UniformBinaryOp"
        self.operands = [OpndA]
        self.bitwidth = OpndA.bitwidth
        self.output_size = OpndA.output_size
        self.operator = operator
        self.operator_is_function = operator_is_function


    def print_op(self, indent_level = 0):
        return ("\t" * indent_level) + f"({self.name}\n{self.operands[0].print_op(indent_level = indent_level+1)} )\n"


    @classmethod
    def get_output_size_for_operand_sizes(cls, operands_size, operands_bitwidth):
        return operands_size[0]


    @classmethod
    def get_operator(cls):
        return None
    @classmethod
    def get_operator_is_function(cls):
        return None

    @classmethod
    def get_input_bitwidth_for_output_bitwidth(cls, output_size, output_bw):
        return [output_bw]

    @classmethod
    def get_input_sizes_for_output_size(cls, output_size, output_bw):
        return [output_size]

    def emit_semantics_pseudocode(self, context):
        loop_idx = self.get_loop_index_var_name(context)
        end_offset = self.bitwidth - 1
        defns_opnd_A, context_A = self.operands[0].emit_semantics_pseudocode(context)

        A_usage = context_A[self.operands[0].ID]


        op_definitions = []

        if self.is_root:
            low_offset_name = f"var_{self.ID}_low"
            low_offset = f"{low_offset_name} = {loop_idx} * {self.bitwidth}"
            op_definitions = [low_offset]
            output_name = f"dst[{low_offset_name}+{end_offset}:{low_offset_name}]"
        else:
            output_name = f"var_{self.ID}"

        if self.operator_is_function:
            defn = f"{output_name} = {self.operator}({A_usage})"
        else:
            defn = f"{output_name} = {self.operator}{A_usage}"
        op_definitions += [defn]
        context_A[self.ID] = output_name

        definitions = defns_opnd_A +  op_definitions

        return definitions, context_A

class NotOp(UniformUnaryOp):

    def __init__(self, ID, OpndA):
        super().__init__(ID, OpndA, operator = "~", operator_is_function = False)
        self.name = "NotOp"
        self.signedness = OpndA.signedness

    @classmethod
    def get_operator(cls):
        return "~"
    @classmethod
    def get_operator_is_function(cls):
        return False

    @classmethod
    def get_pim_api_name(cls):
        return "pimNot"

class OrOp(UniformBinaryOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID, OpndA, OpndB, operator = "|", operator_is_function = False)
        self.name = "OrOp"
        self.commutative = True
        self.signedness = Signedness.NOSIGN

    @classmethod
    def get_operator(cls):
        return "|"
    @classmethod
    def get_operator_is_function(cls):
        return False

    @classmethod
    def get_pim_api_name(cls):
        return "pimOr"


class AndOp(UniformBinaryOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID, OpndA, OpndB, operator = "&", operator_is_function = False)
        self.name = "AndOp"
        self.commutative = True
        self.signedness = Signedness.NOSIGN


    @classmethod
    def get_pim_api_name(cls):
        return "pimAnd"

    @classmethod
    def get_operator(cls):
        return "&"
    @classmethod
    def get_operator_is_function(cls):
        return False

class XorOp(UniformBinaryOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID, OpndA, OpndB, operator = "XOR", operator_is_function = False)
        self.name = "XorOp"
        self.commutative = True
        self.signedness = Signedness.NOSIGN

    @classmethod
    def get_pim_api_name(cls):
        return "pimXor"

    @classmethod
    def get_operator(cls):
        return "XOR"
    @classmethod
    def get_operator_is_function(cls):
        return False


class AddOp(UniformBinaryOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID, OpndA, OpndB, operator = "+", operator_is_function = False)
        self.name = "AddOp"
        self.commutative = True
        self.signedness = Signedness.NOSIGN

    @classmethod
    def get_pim_api_name(cls):
        return "pimAdd"

    @classmethod
    def get_operator(cls):
        return "+"
    @classmethod
    def get_operator_is_function(cls):
        return False



class SubOp(UniformBinaryOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID, OpndA, OpndB, operator = "-", operator_is_function = False)
        self.name = "SubOp"
        self.commutative = False
        self.signedness = Signedness.NOSIGN
    @classmethod
    def get_operator(cls):
        return "-"
    @classmethod
    def get_operator_is_function(cls):
        return False

    @classmethod
    def get_pim_api_name(cls):
        return "pimSub"

class DivOp(UniformBinaryOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID, OpndA, OpndB, operator = "/", operator_is_function = False)
        self.name = "DivOp"
        self.commutative = False
        self.signedness = Signedness.SIGNED
    @classmethod
    def get_operator(cls):
        return "/"
    @classmethod
    def get_operator_is_function(cls):
        return False

    @classmethod
    def get_pim_api_name(cls):
        return "pimDiv"

class MulOp(UniformBinaryOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID, OpndA, OpndB, operator = "*", operator_is_function = False)
        self.name = "MulOp"
        self.commutative = True
        self.signedness = Signedness.SIGNED
    @classmethod
    def get_operator(cls):
        return "*"
    @classmethod
    def get_operator_is_function(cls):
        return False

    @classmethod
    def get_pim_api_name(cls):
        return "pimMul"

class MaxOp(UniformBinaryOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID, OpndA, OpndB, operator = "MAX", operator_is_function = True)
        self.name = "MaxOp"
        self.commutative = True
        self.signedness = Signedness.SIGNED

    @classmethod
    def get_operator(cls):
        return "MAX"
    @classmethod
    def get_operator_is_function(cls):
        return True

    @classmethod
    def get_pim_api_name(cls):
        return "pimMax"

class MinOp(UniformBinaryOp):
    def __init__(self, ID, OpndA, OpndB):
        super().__init__(ID, OpndA, OpndB, operator = "MIN", operator_is_function = True)
        self.name = "MinOp"
        self.commutative = True
        self.signedness = Signedness.SIGNED


    @classmethod
    def get_pim_api_name(cls):
        return "pimMin"

    @classmethod
    def get_operator(cls):
        return "MIN"
    @classmethod
    def get_operator_is_function(cls):
        return True

class LoopOp(BaseOp):
    def __init__(self, ID, BodyExpr):
        super().__init__(ID)
        self.name = "LoopOp"
        self.operands = [BodyExpr]
        self.bitwidth = BodyExpr.bitwidth
        self.output_size = BodyExpr.output_size
        self.signedness = BodyExpr.signedness

        self.body_expr = BodyExpr
        self.body_expr.set_is_root(True)


    def print_op(self, indent_level = 0):
        return ("\t" * indent_level) +f"({self.name}\n{self.operands[0].print_op(indent_level = indent_level+1)})\n"

    def get_output_size_for_operand_sizes(self, operands_size, operands_bitwidth):
        return self.body_expr.get_output_size_for_operand_sizes(operands_size, operands_bitwidth)


    def get_input_bitwidth_for_output_bitwidth(self, output_size, output_bw):
        return self.body_expr.get_input_bitwidth_for_output_bitwidth(output_size, output_bw)

    def get_input_sizes_for_output_size(self, output_size, output_bw):
        return self.body_expr.get_input_bitwidth_for_output_bitwidth(output_size, output_bw)

    def emit_semantics_pseudocode(self, context):
        defns , context = self.body_expr.emit_semantics_pseudocode(context)
        loop_idx = self.get_loop_index_var_name(context)

        num_iters = self.body_expr.get_loop_iterations()
        usage = f"FOR {loop_idx} IN RANGE({0}, {num_iters}, {1}):\n"
        usage += "\n".join(defns)
        usage += "\nENDFOR"
        context[self.ID] = usage
        return [usage], context


class FunctionOp(BaseOp):
    def __init__(self, ID, name , BodyExpr):
        super().__init__(ID)
        self.name = name
        self.operands = [BodyExpr]
        self.bitwidth = BodyExpr.bitwidth
        self.output_size = BodyExpr.output_size
        self.signedness = BodyExpr.signedness
        self.body_expr = BodyExpr

    def print_op(self, indent_level = 0):
        return ("\t" * indent_level) + f"({self.name}\n{self.operands[0].print_op(indent_level = indent_level + 1)} )\n"

    def get_output_size_for_operand_sizes(self, operands_size, operands_bitwidth):
        return self.body_expr.get_output_size_for_operand_sizes(operands_size, operands_bitwidth)

    def get_input_bitwidth_for_output_bitwidth(self, output_size, output_bw):
        return self.body_expr.get_input_bitwidth_for_output_bitwidth( output_size, output_bw)

    def get_input_sizes_for_output_size(self, output_size, output_bw):
        return self.body_expr.get_input_bitwidth_for_output_bitwidth(output_size, output_bw)

    def get_prototype(self):
        registers = self.body_expr.get_registers()
        opnds = ", ".join([reg.name for reg in registers])
        prototype = f"DEFINE {self.name}({opnds}):"
        return prototype

    def emit_semantics_pseudocode(self, context):
        prototype = self.get_prototype()
        body_defs, context = self.body_expr.emit_semantics_pseudocode(context)
        defn = "\n".join([prototype] + body_defs)
        context[self.ID] = defn
        return [defn], context






def OpBoolVisitor(Op, func):
    assert isinstance(Op, BaseOp)
    if func(Op):
        return True

    else:
        return any([OpBoolVisitor(Opnd, func) for Opnd in Op.operands])



