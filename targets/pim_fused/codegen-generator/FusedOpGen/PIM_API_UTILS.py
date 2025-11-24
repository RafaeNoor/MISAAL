from enum import IntEnum
from Ops import *
from PIM_PASS_SKELETON import *
from common.Types import *
from  common.Instructions import Context
from utils.DSLInstructionUtils import *
import sys
import os
import pandas as pd

PIM_ALLOC_NAME = "pimAlloc"
PIM_ALIGNED_ALLOC_NAME = "pimAllocAssociated"
PIM_COPY_TO_DEVICE_NAME = "pimCopyHostToDevice"
PIM_COPY_TO_HOST_NAME = "pimCopyDeviceToHost"

class PimDeviceEnum(IntEnum):
    PIM_DEVICE_NONE = 0
    PIM_FUNCTIONAL = 1
    PIM_DEVICE_BITSIMD_V = 2
    PIM_DEVICE_BITSIMD_V_NAND = 3
    PIM_DEVICE_BITSIMD_V_MAJ = 4
    PIM_DEVICE_BITSIMD_V_AP = 5
    PIM_DEVICE_DRISA_NOR = 6
    PIM_DEVICE_DRISA_MIXED = 7
    PIM_DEVICE_SIMDRAM = 8
    PIM_DEVICE_BITSIMD_H = 9
    PIM_DEVICE_FULCRUM = 10
    PIM_DEVICE_BANK_LEVEL = 11
    PIM_DEVICE_AQUABOLT = 12

def get_device_type_name(device_type : PimDeviceEnum):


    if device_type == PimDeviceEnum.PIM_DEVICE_NONE:
        return "PIM_DEVICE_NONE"
    elif device_type == PimDeviceEnum.PIM_FUNCTIONAL:
        return "PIM_DEVICE_FUNCTIONAL"
    elif device_type == PimDeviceEnum.PIM_DEVICE_BITSIMD_V:
        return "PIM_DEVICE_BITSIMD_V"
    elif device_type == PimDeviceEnum.PIM_DEVICE_BITSIMD_V_NAND:
        return "PIM_DEVICE_BITSIMD_V_NAND"
    elif device_type == PimDeviceEnum.PIM_DEVICE_BITSIMD_V_MAJ:
        return "PIM_DEVICE_BITSIMD_V_MAJ"
    elif device_type == PimDeviceEnum.PIM_DEVICE_BITSIMD_V_AP:
        return "PIM_DEVICE_BITSIMD_V_AP"
    elif device_type == PimDeviceEnum.PIM_DEVICE_DRISA_NOR:
        return "PIM_DEVICE_DRISA_NOR"
    elif device_type == PimDeviceEnum.PIM_DEVICE_DRISA_MIXED:
        return "PIM_DEVICE_DRISA_MIXED"
    elif device_type == PimDeviceEnum.PIM_DEVICE_SIMDRAM:
        return "PIM_DEVICE_SIMDRAM"
    elif device_type == PimDeviceEnum.PIM_DEVICE_BITSIMD_H:
        return "PIM_DEVICE_BITSIMD_H"
    elif device_type == PimDeviceEnum.PIM_DEVICE_FULCRUM:
        return "PIM_DEVICE_FULCRUM"
    elif device_type == PimDeviceEnum.PIM_DEVICE_BANK_LEVEL:
        return "PIM_DEVICE_BANK_LEVEL"
    elif device_type == PimDeviceEnum.PIM_DEVICE_AQUABOLT:
        return "PIM_DEVICE_AQUABOLT"
    else:
        assert False, f"Invalid device type {device_type}"



class PimAllocEnum(IntEnum):
    PIM_ALLOC_AUTO = 0 # Auto determine vertical or horizontal layout based on device type
    PIM_ALLOC_V = 1        # V layout, multiple regions per core
    PIM_ALLOC_H = 2        # H layout, multiple regions per core
    PIM_ALLOC_V1 = 3       # V layout, at most 1 region per core
    PIM_ALLOC_H1 = 4       # H layout, at most 1 region per core


class PimDataType(IntEnum):
    PIM_BOOL = 0
    PIM_INT8 = 1
    PIM_INT16 = 2
    PIM_INT32 = 3
    PIM_INT64 = 4
    PIM_UINT8 = 5
    PIM_UINT16 = 6
    PIM_UINT32 = 7
    PIM_UINT6 = 8
    PIM_FP32 = 9
    PIM_FP16 = 10
    PIM_BF16 = 11
    PIM_FP8 = 12

elem_ty_to_enum = {
    1 : PimDataType.PIM_BOOL,
    8 : PimDataType.PIM_INT8,
    16 : PimDataType.PIM_INT16,
    32 : PimDataType.PIM_INT32,
    64 : PimDataType.PIM_INT64,
}


class PIM_PERF_RESULT:

    def __init__(self, op_name : str = None, is_fused : bool = True, energy : float = 0.0, time : float = 0.0,
                 gops_per_w : float = 0.0, read_percent : float = 0.0, write_percent : float = 0.0, l_percent : float = 0.0
                 ):
        self.op_name = op_name
        self.is_fused = is_fused
        self.energy = energy
        self.time = time
        self.gops_per_w = gops_per_w
        self.read_percent = read_percent
        self.write_percent = write_percent
        self.l_percent = l_percent

    def get_csv_header(self):
        fields = [
            "OP_NAME",
            "IS_FUSED",
            "Energy (mJ)",
            "Execution Time (ms)",
            "GOPS/W",
            "%R",
            "%W",
            "%L"
        ]

        return ",".join(fields)

    def get_field_value(self, field_name):
        if field_name == "OP_NAME":
            return self.op_name
        elif field_name == "IS_FUSED":
            return self.is_fused
        elif field_name == "Energy (mJ)":
            return self.energy
        elif field_name == "Execution Time (ms)":
            return self.time
        elif field_name == "GOPS/W":
            return self.gops_per_w
        elif field_name == "%R":
            return self.read_percent
        elif field_name == "%W":
            return self.write_percent
        elif field_name == "%L":
            return self.l_percent
        else:
            assert False, "Invalid field name"


    def get_csv_entry(self):
        values = [
            self.op_name,
            self.is_fused,
            self.energy,
            self.time,
            self.gops_per_w ,
            self.read_percent ,
            self.write_percent ,
            self.l_percent ,
        ]

        string_ = [str(v) for v in values]

        return ",".join(string_)


class PIM_CONFIG:
    def __init__(self,
                 device_type : PimDeviceEnum = PimDeviceEnum.PIM_DEVICE_BANK_LEVEL,
                 num_ranks : int = 1,
                 num_banks_per_rank : int = 1,
                 num_subarray_per_bank : int = 8,
                 num_rows : int =  1024,
                 num_cols : int = 8192,
                 vf : int = 1024,
                 config_file : str = None
                 ):
        self.config_file = config_file
        self.device_type = device_type
        if self.config_file is not None:
            self.config_name =  os.path.basename(config_file).split(".")[0]
            print("Performance for ",config_file, "at vf",vf, "base name", self.config_name)
        else:
            print("Performance for ",get_device_type_name(self.device_type))
        self.num_ranks = num_ranks
        self.num_banks_per_rank = num_banks_per_rank
        self.num_subarray_per_bank = num_subarray_per_bank
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.vf = vf

        self.pim_fused_perf_results = []
        self.pim_unfused_perf_results = []

        self.work_dir = "./"



    def set_work_dir(self, work_dir):
        self.work_dir = work_dir

    def get_perf_csv_name(self):

        name = "pim_perf_results"
        if self.config_file is not None:
            name += f"_config_{self.config_name}"
        else:
            name += f"_device{get_device_type_name(self.device_type)}"
            name += f"_rank{self.num_ranks}"
            name += f"_BPR{self.num_banks_per_rank}"
            name += f"_SPB{self.num_subarray_per_bank}"
            name += f"_rows{self.num_rows}"
            name += f"_cols{self.num_cols}"
        name += f"_vf{self.vf}"

        name += ".csv"
        return name

    def get_perf_csv_output_path(self):
        return os.path.join(self.work_dir, self.get_perf_csv_name())


    def get_op_perf_result(self, op_name, is_fused = True):
        perf_list = self.pim_fused_perf_results if is_fused else self.pim_unfused_perf_results
        for perf_result in perf_list:
            if perf_result.op_name == op_name:
                return perf_result
        assert False, f"Op {op_name} not found"
        return None

    def calculate_perf_improvement(self, op_name):
        fused_perf = self.get_op_perf_result(op_name, is_fused = True)
        unfused_perf = self.get_op_perf_result(op_name, is_fused = False)
        csv_header_fields = fused_perf.get_csv_header().split(",")

        new_header_fields = ["OP_NAME"]
        field_values = [op_name]

        for field in csv_header_fields:
            if field == "OP_NAME" or field == "IS_FUSED":
                continue
            unfused_value = float(unfused_perf.get_field_value(field))
            fused_value = float(fused_perf.get_field_value(field))
            improvement = unfused_value / fused_value if fused_value != 0.0 else "nan"



            new_header_fields.append(f"{field}_FUSED")
            new_header_fields.append(f"{field}_UNFUSED")
            new_header_fields.append(f"{field}_IMPROVEMENT")

            field_values.append(str(fused_value))
            field_values.append(str(unfused_value))
            field_values.append(str(improvement))

        new_header_fields = ",".join(new_header_fields)
        new_values = ",".join(field_values)

        return new_header_fields, new_values



    def generate_perf_csv(self, fused_stats_path = "fused_stats.txt", unfused_stats_path = "unfused_stats.txt"):
        self.process_perf_file(fused_stats_path, is_fused = True)
        self.process_perf_file(unfused_stats_path, is_fused = False)

        csv_header_fields = []
        csv_rows = []

        for idx, op_result in enumerate(self.pim_fused_perf_results):

            new_header_fields, new_values = self.calculate_perf_improvement(op_result.op_name)

            if idx == 0:
                csv_header_fields = new_header_fields.split(",")
            csv_rows.append(new_values.split(","))


        df = pd.DataFrame(csv_rows, columns=csv_header_fields)
        df.to_csv(os.path.join(self.work_dir,self.get_perf_csv_name()), index=False)







    def process_perf_file(self, fpath, is_fused = True):

        assert os.path.exists(fpath), f"File {fpath} does not exist"

        with open(fpath, "r") as PerfFile:
            file_data = PerfFile.read()


        # Skip device creation lines

        lines = file_data.split("\n")

        start_offset = 0
        for idx, line in enumerate(lines):
            if "Benchmarking" in line:
                start_offset = idx
                break

        lines = lines[start_offset:]

        op_name = None

        pim_command_stats = False
        perf_list = self.pim_fused_perf_results if is_fused else self.pim_unfused_perf_results


        for line in lines:
            if line.startswith("Benchmarking "):
                op_name = line.strip().split()[-1]
                continue
            if "PIM Command Stats" in line:
                pim_command_stats = True
                continue

            if pim_command_stats and "TOTAL" in line:
                assert not op_name is None
                line_split = line.strip().split()

                runtime = line_split[4]
                energy = line_split[5]
                gops_w = line_split[6]
                read_percent = line_split[7]
                write_percent = line_split[8]
                l_percent = line_split[9]


                perf_list.append(PIM_PERF_RESULT(op_name, is_fused, energy, runtime, gops_w, read_percent, write_percent, l_percent))
                op_name = None
                pim_command_stats = False














class PimObj:
    def __init__(self, pim_data_type : PimDataType, pim_vect_size : int, var_name = "v", aligned_to = None, alloc_type = PimAllocEnum.PIM_ALLOC_AUTO, host_memory_reference = None, vect_size_name = ""):
        assert isinstance(pim_data_type, PimDataType)
        self.pim_data_type = pim_data_type
        self.vect_size = pim_vect_size
        self.vect_size_name = vect_size_name
        self.var_name = var_name
        self.aligned_to = aligned_to
        self.alloc_type = alloc_type
        self.host_memory_reference = host_memory_reference
        self.num_elems = self.vect_size // self.get_element_bitwidth()

    def get_element_bitwidth(self):
        for k,v in elem_ty_to_enum.items():
            if v == self.pim_data_type:
                return int(k)
        assert False, "Unreachable"



    def set_var_name(self, var_name):
        self.var_name = var_name

    def set_aligned_to(self, obj):
        assert isinstance(obj, PimObj)
        assert obj.vect_size == self.vect_size
        self.aligned_to = aligned_to

    def set_alloc_type(self, alloc_ty):
        assert isinstance(alloc_ty, PimAllocEnum)
        self.alloc_type = alloc_ty


    def get_allocation_name(self):
        if self.aligned_to is None:
            return PIM_ALLOC_NAME
        else:
            return PIM_ALIGNED_ALLOC_NAME

    def emit_pim_allocation(self, use_cpp = True):
        if self.num_elems == 1:
            return f"// Do not need any allocation for {self.var_name}"

        # Temporary hack to get vect_size name if using intermediate values as root
        if self.vect_size_name == "":
            # Use reg_0 (which should be okay if no operations change number of elements)
            self.vect_size_name = "reg_0_num_elems"

        if use_cpp:
            if self.aligned_to is None:
                return f"PimObjId {self.var_name} = {self.get_allocation_name()}({self.alloc_type.name}, {self.vect_size_name}, {self.pim_data_type.name});"
            else:
                return f"PimObjId {self.var_name} = {self.get_allocation_name()}({self.aligned_to.var_name}, {self.pim_data_type.name});"
        else:
            assert False, "Not yet supported"

    def emit_pim_deallocation(self, use_cpp = True):

        if self.num_elems == 1:
            return f"// Do not need any deallocation for {self.var_name}"

        if use_cpp:
            return f"pimFree({self.var_name});"
        else:
            assert False, "Not yet supported"



    def emit_pim_copy_to_device(self, use_cpp = True, use_fused = True):
        if self.num_elems == 1:
            return f"// No need to copy scalar value {self.host_memory_reference} to PIM memory"
        #return f"{PIM_COPY_TO_DEVICE_NAME}((void*){self.host_memory_reference}, {self.var_name});"

        if use_fused:
            return f"prog.add({PIM_COPY_TO_DEVICE_NAME},(void*){self.host_memory_reference}, {self.var_name}, 0UL, 0UL);"
        else:
            return f"{PIM_COPY_TO_DEVICE_NAME}((void*){self.host_memory_reference}, {self.var_name}, 0UL, 0UL);"



    def emit_pim_copy_to_host(self, use_cpp = True, use_fused = True):
        #return f"{PIM_COPY_TO_HOST_NAME}({self.var_name},(void*){self.host_memory_reference});"
        if use_fused:
            return f"prog.add({PIM_COPY_TO_HOST_NAME},{self.var_name},(void*){self.host_memory_reference}, 0UL, 0UL);"
        else:
            return f"{PIM_COPY_TO_HOST_NAME}({self.var_name},(void*){self.host_memory_reference}, 0UL, 0UL);"




class PIM_PROG:
    def __init__(self, pim_expression, prog_name = "prog", func_name = "fused_op_defn"):
        assert isinstance(pim_expression, BaseOp)

        if isinstance(pim_expression, FunctionOp):
            pim_expression = pim_expression.body_expr

        if isinstance(pim_expression, LoopOp):
            pim_expression = pim_expression.body_expr

        self.func_name = func_name
        self.prog_name = prog_name
        self.pim_expr = pim_expression
        self.ordered_exprs = self.order_ops_in_expression(self.pim_expr)

        max_expr_idx = 0
        for i in range(0, len(self.ordered_exprs)):
            expr_i = self.ordered_exprs[i]
            expr_i_size = expr_i.output_size

            if self.ordered_exprs[max_expr_idx].output_size < expr_i_size:
                max_expr_idx = i

        if  False:
            root_expr_obj = self.create_pim_obj(self.ordered_exprs[0], var_name = "fuse_root", aligned_to = None)
            other_expr_objs = [self.create_pim_obj(self.ordered_exprs[i], var_name = f"fuse_expr_{i-1}", aligned_to = root_expr_obj) for i in range(1, len(self.ordered_exprs))]
            self.expr_objs_flat = [root_expr_obj] + other_expr_objs
        else:
            max_expr = self.ordered_exprs[max_expr_idx]
            root_expr_obj = self.create_pim_obj(max_expr, var_name = "fuse_root", aligned_to = None)
            #other_expr_objs = [self.create_pim_obj(self.ordered_exprs[i], var_name = f"fuse_expr_{i}", aligned_to = root_expr_obj) for i in range(0, len(self.ordered_exprs)) if i != max_expr_idx]
            self.expr_objs_flat =  [self.create_pim_obj(self.ordered_exprs[i], var_name = f"fuse_expr_{i}", aligned_to = root_expr_obj) for i in range(0, max_expr_idx)] + [root_expr_obj] + [self.create_pim_obj(self.ordered_exprs[i], var_name = f"fuse_expr_{i}", aligned_to = root_expr_obj) for i in range(max_expr_idx+1, len(self.ordered_exprs))]









        self.cpp_prototype_types = {}
        self.parse_types(pim_expression)


        self.return_var_name = "ret_vec"
        self.param_num_elem_name = {}

        self.expr_objs_dict = {}
        for idx, expr in enumerate(self.ordered_exprs):
            expr_obj = self.expr_objs_flat[idx]
            if isinstance(expr, Register):
                expr_obj.host_memory_reference = f'reg_{expr.index}'
                self.param_num_elem_name[expr.ID] = f"reg_{expr.index}_num_elems"
                expr_obj.vect_size_name = self.param_num_elem_name[expr.ID]
            if expr.is_root:
                expr_obj.host_memory_reference = self.return_var_name
                self.param_num_elem_name[expr.ID] = f"{self.return_var_name}_num_elems"
                expr_obj.vect_size_name = self.param_num_elem_name[expr.ID]



            self.expr_objs_dict[expr.ID] = expr_obj


        self.use_cpp = True
        self.num_return_elements = pim_expression.output_size // pim_expression.bitwidth

    def emit_rewrite_rule_by_construction(self, expr, op_map = {}, root = False):
        registers = expr.get_registers()
        all_operands_are_reg = all([isinstance(opnd, Register) for opnd in expr.operands])

        if isinstance(expr, LoopOp):
            return self.emit_rewrite_rule_by_construction(expr.body_expr, op_map, root = root)
        if isinstance(expr, FunctionOp):
            return self.emit_rewrite_rule_by_construction(expr.body_expr, op_map, root = root)



        if isinstance(expr, Register):
            return f"reg_{expr.index}"
        op_key = (expr.name, expr.bitwidth, expr.output_size)

        if all_operands_are_reg and root:
            op_map[op_key] = f"test_enum_2_{self.func_name}"
            return None

        op_name = op_map[op_key]



        opnd_strs = []
        for opnd in expr.operands:
            opnd_str = self.emit_rewrite_rule_by_construction(opnd, op_map, root = False)
            opnd_strs.append(opnd_str)

        op_str = f"({op_name} {' '.join(opnd_strs)})"


        if root:
            stmts = ["==========================="]
            stmts += ["SRC EXPR"]
            join_opnds = " ".join([f"reg_{reg.index}" for reg in registers])
            src_expr_str = f"(test_enum_2_{self.func_name} {join_opnds})"
            stmts += [src_expr_str]
            stmts += ["DST EXPR"]
            stmts += [op_str]

            return "\n".join(stmts)
        else:
            return op_str







    def parse_types(self, expr):
        num_elements = expr.output_size // expr.bitwidth

        if expr.is_root:
            if num_elements != 1:
                self.cpp_prototype_types['return'] = f"int{expr.bitwidth}x{num_elements}_t"
            else:
                self.cpp_prototype_types['return'] = f"int{expr.bitwidth}_t"
        elif isinstance(expr, Register):
            if num_elements != 1:
                self.cpp_prototype_types[f'reg_{expr.index}'] = f"int{expr.bitwidth}x{num_elements}_t"
            else:
                self.cpp_prototype_types[f'reg_{expr.index}'] = f"int{expr.bitwidth}_t"



        for opnd in expr.operands:
            self.parse_types(opnd)



    def order_ops_in_expression(self, expr):
        assert isinstance(expr, BaseOp)

        ordered = []
        for opnd in expr.operands:
            ordered += self.order_ops_in_expression(opnd)

        ordered = [expr] + ordered

        return ordered

    def create_pim_obj(self, pim_expr, var_name = "v" , aligned_to = None):
        if isinstance(pim_expr, Register):
            pim_obj = PimObj(elem_ty_to_enum[pim_expr.bitwidth], pim_expr.output_size, var_name = var_name, aligned_to = aligned_to, host_memory_reference = f"reg_{pim_expr.index}")
        else:
            pim_obj = PimObj(elem_ty_to_enum[pim_expr.bitwidth], pim_expr.output_size, var_name = var_name, aligned_to = aligned_to, host_memory_reference = None)


        return pim_obj


    def emit_allocations(self):
        allocs = ["// Emitting Allocations"]
        # First Handle the root allocation
        for objid in self.expr_objs_flat:
            if "_root" not in objid.var_name:
                continue
            num_elems = objid.vect_size // objid.get_element_bitwidth()
            if num_elems == 1:
                allocs.append(
                    f"// Scalar operand {objid.var_name} does not need pim allocation"
                )
                allocs.append(
                   f"auto {objid.var_name} = {objid.host_memory_reference};"
                )
            else:
                allocs.append(
                    objid.emit_pim_allocation(use_cpp = self.use_cpp)
                )
        for objid in self.expr_objs_flat:
            # Then handle all ohther allocations
            if "_root" in objid.var_name:
                continue
            num_elems = objid.vect_size // objid.get_element_bitwidth()
            if num_elems == 1:
                allocs.append(
                    f"// Scalar operand {objid.var_name} does not need pim allocation"
                )
                allocs.append(
                   f"auto {objid.var_name} = {objid.host_memory_reference};"
                )
            else:
                allocs.append(
                    objid.emit_pim_allocation(use_cpp = self.use_cpp)
                )
        return allocs

    def emit_deallocations(self):
        deallocs = ["// Emitting Deallocations"]
        for objid in self.expr_objs_flat:
            num_elems = objid.vect_size // objid.get_element_bitwidth()
            if num_elems == 1:
                deallocs.append(
                    f"// Scalar operand {objid.var_name} does not need pim deallocation"
                )
            else:
                deallocs.append(
                    objid.emit_pim_deallocation(use_cpp = self.use_cpp)
                )
        return deallocs


    def emit_copy_to_device(self, use_fused = True):
        copies = ["// Emitting Copy Host to Device"]
        for idx, objid in enumerate(self.expr_objs_flat):
            # Not needed for root expression (i.e. final return value)
            if idx == 0:
                continue
            if not objid.host_memory_reference is None :
                copies.append(
                    objid.emit_pim_copy_to_device(use_cpp = self.use_cpp, use_fused = use_fused)
                )
        return copies

    def emit_copy_to_host(self, use_fused = True):
        # Only needed for root expression
        return ["// Emitting Copy Device to Host", self.expr_objs_flat[0].emit_pim_copy_to_host(use_cpp = self.use_cpp, use_fused = use_fused)]



    def emit_pim_fuse_prog_compute(self, use_fused = True):
        stmts = ["// Creating PIM Fused Program",]

        for i in reversed(range(len(self.ordered_exprs))):
            expr = self.ordered_exprs[i]
            pim_obj = self.expr_objs_dict[expr.ID]

            # For registers, i.e. terminals of the expression
            # they would be defined using copy host to device
            if isinstance(expr, Register):
                continue

            if isinstance(expr, BroadcastOp):
                operand_obj = [self.expr_objs_dict[opnd.ID] for opnd in expr.operands][0]
                if use_fused:
                    stmt = f"{self.prog_name}.add({expr.get_pim_api_name()}, {pim_obj.var_name} ,{operand_obj.var_name});"
                else:
                    stmt = f"{expr.get_pim_api_name()}( {pim_obj.var_name} ,{operand_obj.var_name});"

                stmts.append(stmt)
                continue

            if isinstance(expr, ShiftOp):
                operand_obj = [self.expr_objs_dict[opnd.ID] for opnd in expr.operands]

                if use_fused:
                    stmt = f"{self.prog_name}.add({expr.get_pim_api_name()}, {operand_obj[0].var_name}, {pim_obj.var_name} , (unsigned) {operand_obj[1].var_name});"
                else:
                    stmt = f"{expr.get_pim_api_name()}( {operand_obj[0].var_name}, {pim_obj.var_name} , (unsigned) {operand_obj[1].var_name});"

                stmts.append(stmt)
                continue

            operand_objs = [self.expr_objs_dict[opnd.ID] for opnd in expr.operands]
            operand_params_str = ", ".join([opnd.var_name for opnd in operand_objs])
            if use_fused:
                stmt = f"{self.prog_name}.add({expr.get_pim_api_name()},{operand_params_str} , {pim_obj.var_name});"
            else:
                stmt = f"{expr.get_pim_api_name()}({operand_params_str} , {pim_obj.var_name});"

            stmts.append(stmt)

        #stmts.append(
        #    f"pimFuse({self.prog_name});"
        #)

        return stmts

    def emit_pim_fused_prog_cpp(self):
        registers = self.pim_expr.get_registers()
        return_type = self.cpp_prototype_types['return']
        parameter_Types = [self.cpp_prototype_types[f"reg_{reg.index}"] for reg in registers]

        opnd_prototype_decl = []

        for reg in registers:
            type_ = self.cpp_prototype_types[f'reg_{reg.index}']
            var_name = self.expr_objs_dict[reg.ID].host_memory_reference
            if self.expr_objs_dict[reg.ID].num_elems == 1:
                opnd_prototype_decl.append(f"int64_t {var_name}")
            else:
                opnd_prototype_decl.append(f"void* {var_name}")

            opnd_prototype_decl.append(f"int64_t {self.param_num_elem_name[reg.ID]}")

        # Add return type as the final operand
        opnd_prototype_decl.append(f"void* {self.return_var_name}")
        opnd_prototype_decl.append(f"int64_t {self.param_num_elem_name[self.pim_expr.ID]}")

        join_opnds = ", ".join(opnd_prototype_decl)



        prototype = f"void {self.func_name}({join_opnds})"

        stmts = ["", f"PimProg {self.prog_name};"]

        stmts += self.emit_allocations()
        stmts += self.emit_copy_to_device()
        stmts += self.emit_pim_fuse_prog_compute()
        stmts += self.emit_copy_to_host()
        stmts += [f"pimFuse({self.prog_name});"]
        stmts += self.emit_deallocations()

        add_ifdef = True

        if add_ifdef:
            ifdef_start = f"#if defined(include_{self.func_name}) || defined(include_all)"
            ifdef_end = f"#endif"
            body = prototype + "{\n" + "\n\t".join(stmts) +"\n}"
            return ifdef_start +"\n" + body + "\n" + ifdef_end + "\n"
        else:
            return prototype + "{\n" + "\n\t".join(stmts) +"\n}"


    def emit_pim_unfused_prog_cpp(self):
        registers = self.pim_expr.get_registers()
        return_type = self.cpp_prototype_types['return']
        parameter_Types = [self.cpp_prototype_types[f"reg_{reg.index}"] for reg in registers]

        opnd_prototype_decl = []

        for reg in registers:
            type_ = self.cpp_prototype_types[f'reg_{reg.index}']
            var_name = self.expr_objs_dict[reg.ID].host_memory_reference
            if self.expr_objs_dict[reg.ID].num_elems == 1:
                opnd_prototype_decl.append(f"int64_t {var_name}")
            else:
                opnd_prototype_decl.append(f"void* {var_name}")

            opnd_prototype_decl.append(f"int64_t {self.param_num_elem_name[reg.ID]}")

        # Add return type as the final operand
        opnd_prototype_decl.append(f"void* {self.return_var_name}")
        opnd_prototype_decl.append(f"int64_t {self.param_num_elem_name[self.pim_expr.ID]}")

        join_opnds = ", ".join(opnd_prototype_decl)



        prototype = f"void {self.func_name}({join_opnds})"

        stmts = [""]

        stmts += self.emit_allocations()
        stmts += self.emit_copy_to_device(use_fused = False)
        stmts += self.emit_pim_fuse_prog_compute(use_fused = False)
        stmts += self.emit_copy_to_host(use_fused = False)
        stmts += self.emit_deallocations()


        add_ifdef = True

        if add_ifdef:
            ifdef_start = f"#if defined(include_{self.func_name}) || defined(include_all)"
            ifdef_end = f"#endif"
            body =  prototype + "{\n" + "\n\t".join(stmts) +"\n}"
            return ifdef_start +"\n" + body + "\n" + ifdef_end + "\n"
        else:
            return prototype + "{\n" + "\n\t".join(stmts) +"\n}"

    def get_bench_name(self):
        bench_name = f"benchmark_{self.func_name}"
        return bench_name

    def emit_benchmark_method(self):
        bench_name = f"benchmark_{self.func_name}"


        registers = self.pim_expr.get_registers()
        return_type = self.cpp_prototype_types['return']
        parameter_Types = [self.cpp_prototype_types[f"reg_{reg.index}"] for reg in registers]

        def get_scalar_type(t):
            scalar_ty = None
            if "x" in t:
                # Vector type
                scalar_ty =  t.split("x")[0]+"_t"
            else:
                scalar_ty = t

            if scalar_ty == "int1_t":
                return "int8_t"
            elif scalar_ty.endswith("_t"):
                return scalar_ty
            else:
                return f"{scalar_ty}_t"

        scalar_param_types = [get_scalar_type(t) for t in parameter_Types]
        for scalar_type in scalar_param_types:
            if "_t_t" in scalar_type:
                assert False
        return_type = get_scalar_type(return_type)

        return_num_elems = str(self.num_return_elements)

        # Allocation arguments
        arg_names = [f"arg_{i}" for i in range(len(registers))]
        arg_num_elems = [str(reg.get_num_elements()) for reg in registers]




        cpp_cond = "VF == 0"


        # Use operations on VF
        func_decl = f"void {bench_name}()"
        opnd_decls = [f"{scalar_param_types[i]} {arg_names[i]}[{arg_num_elems[i]}]" if int(arg_num_elems[i]) != 1 else f"{scalar_param_types[i]} {arg_names[i]}" for i in range(len(registers))]

        ret_decl = [f"{return_type} ret_val[{return_num_elems}]"]

        stmts = []

        stmts += [f"printf(\"Benchmarking {self.func_name}\\n\")"]
        stmts += ["pimResetStats()"]


        then_stmts = []
        then_stmts += opnd_decls
        then_stmts += ret_decl

        arguments = []

        for idx, arg_name in enumerate(arg_names):
            num_elems = arg_num_elems[idx]
            arguments.append(arg_name)
            arguments.append(num_elems)

        arguments.append("ret_val")
        arguments.append(return_num_elems)

        joined = ", ".join(arguments)


        invoke_cmd = f"{self.func_name}({joined})"
        then_stmts += [invoke_cmd, ""]

        then_joined = ";\n".join(then_stmts)

        else_stmts = []
        # Use  VF macro
        USE_NEW = True # Heap memory allocation to reduce compilation times
        if USE_NEW:
            opnd_decls = [f"{scalar_param_types[i]}* {arg_names[i]} = new {scalar_param_types[i]}[VF]" if int(arg_num_elems[i]) != 1 else f"{scalar_param_types[i]} {arg_names[i]}" for i in range(len(registers))]
            ret_decl = [f"{return_type}* ret_val = new {return_type}[VF]"]
        else:
            opnd_decls = [f"{scalar_param_types[i]} {arg_names[i]}[VF]" if int(arg_num_elems[i]) != 1 else f"{scalar_param_types[i]} {arg_names[i]}" for i in range(len(registers))]
            ret_decl = [f"{return_type} ret_val[VF]"]
        else_stmts += opnd_decls
        else_stmts += ret_decl

        arguments = []

        for idx, arg_name in enumerate(arg_names):
            num_elems = arg_num_elems[idx]
            arguments.append(arg_name)
            arguments.append("VF")

        arguments.append("ret_val")
        arguments.append("VF")

        joined = ", ".join(arguments)


        invoke_cmd = f"{self.func_name}({joined})"
        else_stmts += [invoke_cmd]

        if USE_NEW:
            # Delete heap allocations
            opnd_free = [f"delete[] {arg_names[i]}"  for i in range(len(registers)) if  int(arg_num_elems[i]) != 1 ]
            ret_free = [f"delete[] ret_val"]
            else_stmts += opnd_free + ret_free


        else_stmts += [""]
        else_joined = ";\n".join(else_stmts)

        full_cond = f"if({cpp_cond}){{\n{then_joined}\n}} else {{\n {else_joined}\n}}"

        stmts += [full_cond]


        stmts += ["pimShowStats()" , ""]


        add_ifdef = True

        if add_ifdef:
            ifdef_start = f"#if defined(include_{self.func_name}) || defined(include_all)"
            ifdef_end = f"#endif"
            body =  func_decl + "{\n" + ";\n".join(stmts) + "}"
            return ifdef_start +"\n" + body + "\n" + ifdef_end + "\n"
        else:
            return func_decl + "{\n" + ";\n".join(stmts) + "}"











class FusedPIMOpLegalizerBase:
    def __init__(self, output_file_name, fused_expression_ops, pim_dsl_list):
        self.output_file_name = output_file_name
        self.fused_expression_ops = fused_expression_ops
        self.pim_dsl_list = pim_dsl_list




    def get_fused_op_by_ctx_name(self, ctx_name):
        for op in self.fused_expression_ops:
            if ctx_name in op.name:
                return op

    # Get those contexts which have differing pairs of input and output
    # bitwidths, so that we can conditionally switch to those
    # implementation
    def get_differing_bitwidth_ctxs(self, dsl_inst):
        io_pairs = []
        ctxs = []

        for ctx in dsl_inst.contexts:
            if ctx.in_precision_index is None:
                continue

            if ctx.out_precision_index is None:
                continue

            in_prec = ctx.in_precision
            out_prec = ctx.out_precision
            pair = (in_prec, out_prec)

            if pair in io_pairs:
                continue
            io_pairs.append(pair)
            ctxs.append(ctx)
        return ctxs



# Generates an LLVM Pass which rewrites the Module into another LLVM Module
class FusedPIMOpLegalizerLLVM(FusedPIMOpLegalizerBase):
    def __init__(self, output_file_name, fused_expression_ops, pim_dsl_list):
        super().__init__(output_file_name, fused_expression_ops, pim_dsl_list)

    def legalize(self):
        with open(self.output_file_name, "w+") as LLVMPass:
            LLVMPass.write(
                LOWERING_PASS_SKELETON_TOP + "\n"
            )

            LLVMPass.write(
                "void PIMLegalize(CallInst* CI){\n"
            )
            LLVMPass.write(
                "IRBuilder<> Builder(CI);\n"
            )
            LLVMPass.write(
                "LLVMContext &Context = CI->getContext();\n"
            )



        for eq_class in self.pim_dsl_list:
            stmt = self.emit_legalize_eq_class(eq_class)

            with open(self.output_file_name, "a+") as LLVMPass:
                LLVMPass.write(stmt+"\n")

        with open(self.output_file_name, "a+") as LLVMPass:
            LLVMPass.write("}\n")
            LLVMPass.write(LOWERING_PASS_SKELETON_BOTTOM)


    def emit_legalize_eq_class(self, dsl_inst):
        eq_class_name = dsl_inst.name

        stmts = []
        differing_ctxs = self.get_differing_bitwidth_ctxs(dsl_inst)
        assert len(differing_ctxs) != 0, "Expect atleast one unique valid context"
        for ctx in differing_ctxs:
            #op = self.get_fused_op_by_ctx_name(ctx.name)
            #ctx_stmts = "\n".join(self.legalize_ctx(op.name, ctx.permutation))

            ctx_stmts = "\n".join(self.legalize_ctx(ctx.name, ctx.permutation))

            def as_integer(val):
                return f"dyn_cast<ConstantInt>({val})->getSExtValue()"

            in_prec_arg_val = as_integer(f"CI->getArgOperand({ctx.in_precision_index})")
            out_prec_arg_val = as_integer(f"CI->getArgOperand({ctx.out_precision_index})")


            in_prec_condition = f"({in_prec_arg_val} == {ctx.in_precision})"
            out_prec_condition = f"({out_prec_arg_val} == {ctx.out_precision})"
            combined_condition = f"({in_prec_condition} \n&& {out_prec_condition})"
            execute_clause = f"if({combined_condition})" + "{\n"+f"{ctx_stmts}" +"\n}"
            stmts.append(execute_clause)



        cases = "\n".join(stmts)
        outer_condition = f"(CI->getName() == \"{dsl_inst.name}\")"

        eq_class_clause = f"if({outer_condition})" + "{\n" + cases + "\n}\n"

        return eq_class_clause



    def legalize_ctx(self,  op_func_name,   permutation):
        InstHandle = "CI"
        #match_condition = f"({InstHandle}->getName() == \"{eq_func_name}\")"

        llvm_ir_builder_name = "Builder"

        # Align operands according to permutation
        len_operands = len([1 for a in permutation if a != -1])
        vect_operands = [None] * len_operands
        for idx, perm in enumerate(permutation):
            if perm == -1:
                continue

            vect_operands[perm] = f"{InstHandle}->getArgOperand({idx})"


        stmts = [f"{llvm_ir_builder_name}.SetInsertPoint({InstHandle});"]
        vect_operands_handles = []

        for idx, op_ref in enumerate(vect_operands):
            handle_name = f"v{idx}"
            reference = f"Value* {handle_name} = {op_ref};"

            vect_operands_handles.append(handle_name)
            stmts.append(reference)

        # Return type is the final value in operands for the legalized function
        # so we append it here.
        vect_operands_handles.append(f"{InstHandle}")


        # Legalizer requires a memory allocation on the host for
        # the fused operands as well as the result operands. Here
        # we create allocations accordingly.


        void_type = "Type::getVoidTy(Context)"
        int8_ptr_type = "Type::getInt8PtrTy(Context)"
        int8_type = "Type::getInt8Ty(Context)"
        int64_type = "Type::getInt64Ty(Context)"

        allocations = []
        num_opnd_vect_elems = []
        stmts.append("// Creating allocations for vectors")
        for idx, vect_handle in enumerate(vect_operands_handles):
            alloca_name = f"AllocaV{idx}"
            alloca = f"AllocaInst *{alloca_name} = {llvm_ir_builder_name}.CreateAlloca({vect_handle}->getType(), nullptr);"
            stmts.append(alloca)

            stmts.append(f"// Store {vect_handle} into {alloca_name}")
            stmts.append(f"{llvm_ir_builder_name}.CreateStore({vect_handle}, {alloca_name});")

            bitcast_name = f"Bitcast_{alloca_name}"
            bitcast = f"Value *{bitcast_name} = {llvm_ir_builder_name}.CreateBitCast({alloca_name}, Type::getInt8PtrTy(Context));"
            stmts.append(bitcast)

            num_elems_decl = f"int num_elem_{vect_handle} = dyn_cast<FixedVectorType>({vect_handle}->getType())->getNumElements();"
            stmts.append(num_elems_decl)

            num_elems = f"ConstantInt::get({int64_type}, num_elem_{vect_handle})"
            num_opnd_vect_elems.append(num_elems)

            allocations.append(bitcast_name)


        return_allocation = allocations[-1]
        return_size = num_opnd_vect_elems[-1]

        combined_opnd = []

        for idx in range(len(allocations)):
            combined_opnd.append(allocations[idx])
            combined_opnd.append(num_opnd_vect_elems[idx])

        # Declare the function to be called
        func_decl_types = []
        for handle in vect_handle:
            func_decl_types.append(int8_ptr_type)
            func_decl_types.append(int64_type)

        joined_types = ",\n ".join(func_decl_types)
        joined_types = "{\n" + joined_types + "}"

        func_type = f"FunctionType* PimFuncTy = FunctionType::get({void_type}, {joined_types}, false);"

        stmts.append("// Creating Function Types")
        stmts.append(func_type)

        func_ref_exist = f"Function* PimFunc = {InstHandle}->getModule()->getFunction(\"op_func_name\");"
        stmts.append(func_ref_exist)

        func_ref_not_exist = f"if(!PimFunc)\nPimFunc = Function::Create(PimFuncTy, Function::ExternalLinkage , \"{op_func_name}\" , {InstHandle}->getModule());"

        stmts.append(func_ref_not_exist)

        joined_opnd = ",\n ".join(combined_opnd)
        joined_opnd = "{\n" + joined_opnd + "}"

        stmts.append("// Generating PIM Call")
        stmts.append(f"std::vector<Value*> CallParams = {joined_opnd};")

        insert_call = f"CallInst::Create(PimFunc, CallParams, \"pimInst\", {InstHandle});"
        stmts.append(insert_call)

        # After the call to the fused instruction is inserted then
        # we simply do a bitcast of the result allocation to the return type
        # add a load from that memory and replace all uses
        bit_cast_return_alloc  = f"Value *return_bitcast = {llvm_ir_builder_name}.CreateBitCast({return_allocation}, {InstHandle}->getType());"
        stmts.append(bit_cast_return_alloc)

        return_value = f"Value *VecValue = {llvm_ir_builder_name}.CreateLoad({InstHandle}->getType(), return_bitcast);"
        stmts.append(return_value)

        # Time to replace all uses of this value and erase it from parent
        stmts.append(f"{InstHandle}->replaceAllUsesWith(VecValue);")
        stmts.append(f"ToErase.push_back({InstHandle});")

        return stmts







# Generates an LLVM Pass which rewrites the Module into a C++ file which will be
# linked against the current module. It uses the Halide vector type descriptions
# to create object. Unlike FusedPIMOpLegalizer, FusedPIMOpLegalizerHalide directly
# rewrites the input expression into C++ invokations online
class FusedPIMOpLegalizerHalide(FusedPIMOpLegalizerBase):
    def __init__(self, output_file_name, fused_expression_ops, pim_dsl_list):
        super().__init__(output_file_name, fused_expression_ops, pim_dsl_list)
        self.counter = 0

    def get_halide_type(self, size, bitwidth):
        num_elems = size // bitwidth
        if num_elems != 1:
            return f"int{bitwidth}x{num_elems}_t"
        else:
            return f"int{bitwidth}_t"

    def get_fresh_name(self):
        var_name = f"var_{self.counter}"
        self.counter += 1
        return var_name

    def legalize(self, expr, func_name, leaves_sizes, leaves_bitwidth):

        self.counter = 0
        return_type_size = expr.out_vectsize
        return_type_bitwidth = expr.out_precision

        halide_return_type = self.get_halide_type(return_type_size, return_type_bitwidth)

        opnd_types = [self.get_halide_type(leaves_sizes[i] , leaves_bitwidth[i]) for i in range(len(leaves_bitwidth))]
        opnd_decls = [f"{opnd_types[i]} reg_{i}" for i in range(len(opnd_types))]
        joined_decls = ", ".join(opnd_decls)

        cpp_prototype = f"{halide_return_type} {func_name}({joined_decls})"


        var_map = {}

        stmts, ret_expr = self.legalize_helper(expr, is_root = True)

        stmts.append("return return_vec;")
        stmts = [""] + stmts

        return cpp_prototype +"{\n" + "\n\t".join(stmts) +"\n}"

    def legalize_profile_opt_data_movement(self, expr, func_name, leaves_sizes, leaves_bitwidth):

        self.counter = 0
        return_type_size = expr.out_vectsize
        return_type_bitwidth = expr.out_precision

        halide_return_type = self.get_halide_type(return_type_size, return_type_bitwidth)

        opnd_types = [self.get_halide_type(leaves_sizes[i] , leaves_bitwidth[i]) for i in range(len(leaves_bitwidth))]
        opnd_decls = [f"{opnd_types[i]} reg_{i}" for i in range(len(opnd_types))]
        joined_decls = ", ".join(opnd_decls)

        cpp_prototype = f"{halide_return_type} {func_name}({joined_decls})"


        var_map = {}

        stmts = self.legalize_helper_opt_data_movement(expr, is_root = True)

        stmts.append("return return_vec;")
        stmts = [""] + stmts

        return cpp_prototype +"{\n" + "\n\t".join(stmts) +"\n}"

    def get_pim_eq_class(self, ctx):
        for eq_class in self.pim_dsl_list:
            if ctx.dsl_name == eq_class.name:
                return eq_class

            for ctx_ in eq_class.contexts:
                if ctx_.name == ctx.name:
                    return eq_class
        return None


    def convert_to_int(self, expr):
        assert isinstance(expr, ConstBitVector)
        val = expr.value

        if val.startswith("#x"):
            # Hex value
            return int(val[2:], 16)
        elif val == "#b1":
            return "1"
        elif val == "#b0":
            return "0"
        else:
            return val


    def legalize_helper(self, expr , is_root = False):
        if isinstance(expr, Reg):
            return [] , f"reg_{expr.index}"

        if isinstance(expr, ConstBitVector):
            return [], self.convert_to_int(expr)

        assert isinstance(expr, Context)



        eq_class = self.get_pim_eq_class(expr)

        assert not eq_class is None, "Must belong to some known eq class"
        sample_ctx = eq_class.contexts[0]
        sample_ctx_args = sample_ctx.context_args
        idx_sym_bvs = [idx for idx in range(len(sample_ctx_args)) if isinstance(sample_ctx_args[idx], BitVector)]

        expr_size = expr.out_vectsize
        expr_bw = expr.out_precision
        expr_num_elems = expr_size // expr_bw

        stmts = []
        opnd_labels = []
        opnd_elems = []


        # Reorder according to permutation map
        reordered_idxs = [None] * len(idx_sym_bvs)
        non_zero_perms = [p for p in expr.permutation if p != -1 and  isinstance(sample_ctx_args[p], BitVector)]
        print(expr.name)
        print("expression perms", expr.permutation)
        print("Non zero perms", non_zero_perms)

        for idx ,perm_idx in enumerate(non_zero_perms):
            print("Reordered idx",reordered_idxs )
            reordered_idxs[idx] = perm_idx

        print("Before Permute", idx_sym_bvs)
        print("After Permute", reordered_idxs)

        # Swap permuted operands
        idx_sym_bvs = reordered_idxs




        for idx in idx_sym_bvs:
            sub_expr = expr.context_args[idx]
            sub_stmts , sub_expr_label = self.legalize_helper(sub_expr, is_root = False)
            stmts += sub_stmts
            opnd_labels.append(sub_expr_label)
            if isinstance(sub_expr, ConstBitVector):
                opnd_size  = sub_expr.size
                opnd_bw = sub_expr.size
            else:
                opnd_size  = sub_expr.out_vectsize
                opnd_bw = sub_expr.out_precision

            num_elems = opnd_size // opnd_bw

            opnd_elems.append(num_elems)


        var_name = "return_vec" if is_root else self.get_fresh_name()

        # TODO: Replace with actual function name
        #impl_func_name = expr.dsl_name.split("_dsl")[0] #expr.name
        impl_func_name = expr.name.split("_dsl")[0] #expr.name

        expr_return_type = self.get_halide_type(expr_size, expr_bw)
        stmts.append(f"{expr_return_type} {var_name};")

        # Final pair of values correspond to return types
        opnd_labels.append(var_name)
        opnd_elems.append(expr_num_elems)

        invoke_params = []
        for i in range(len(opnd_labels)):
            label = opnd_labels[i]
            num_elems = opnd_elems[i]
            if num_elems != 1:
                invoke_params.append(f"{label}.data()")
            else:
                invoke_params.append(f"{label}")
            invoke_params.append(str(num_elems))

        params_joined = ", ".join(invoke_params)

        # Get pre extended name
        impl_func_name = impl_func_name.split("_extended")[0]

        if impl_func_name.endswith("_m32"):
            impl_func_name = impl_func_name.split("_m32")[0]

        # Strip test_enum_* prefix
        if  "scaled" in impl_func_name:
            wrapper_name =  "test_" + impl_func_name.split("test_")[-1]
        elif "manual" in impl_func_name:
            wrapper_name = "manual_"+impl_func_name.split("manual_")[-1]
        else:
            wrapper_name = "comb"+impl_func_name.split("_comb")[-1]
        invoke_fused_op = f"{wrapper_name}({params_joined});"


        stmts.append(invoke_fused_op)

        return stmts, var_name

    def arg_max(self, ls):
        if len(ls) == 0:
            return -1

        max_idx = 0

        for idx, v in enumerate(ls):
            if ls[max_idx] < v:
                max_idx = idx

        return max_idx


    def legalize_helper_opt_data_movement(self, expr , is_root = False):
        if is_root and isinstance(expr, Reg):
            return ""

        assert isinstance(expr, Context)





        expr_return_type = self.get_halide_type(expr.out_vectsize, expr.out_precision)
        num_out_elems = expr.out_vectsize // expr.out_precision

        regs = get_unique_context_registers(expr)

        reg_sizes = [reg.size for reg in regs]
        combined_exprs = reg_sizes + [expr.out_vectsize]

        num_exprs = len(combined_exprs)

        arg_max = self.arg_max(combined_exprs)

        # Use arg max argument as root for PIM Device creation
        # Copy host to device for all values except last, and for last copy device to host

        root_name = "pim_root"

        pim_objs = [None] * num_exprs

        if arg_max == num_exprs - 1:
            root_expr = PimObj(elem_ty_to_enum[expr.out_precision], expr.out_vectsize, var_name = root_name, aligned_to = None, host_memory_reference = "return_vec", vect_size_name = f"{num_out_elems}")
            pim_objs[arg_max] = root_expr
            for idx in range(num_exprs-1):
                other_expr = PimObj(elem_ty_to_enum[regs[idx].precision], regs[idx].size, var_name = f"pim_{idx}", aligned_to = root_expr, host_memory_reference = f"reg_{regs[idx].index}.data()")
                pim_objs[idx] = other_expr


        else:
            root_expr = PimObj(elem_ty_to_enum[regs[arg_max].precision], regs[arg_max].size, var_name = root_name, aligned_to = None, host_memory_reference = f"reg_{regs[arg_max].index}.data()", vect_size_name = f"{num_out_elems}")
            pim_objs[arg_max] = root_expr
            for idx in range(num_exprs):
                if idx == arg_max:
                    continue
                if idx == num_exprs - 1:
                    other_expr = PimObj(elem_ty_to_enum[expr.out_precision], expr.out_vectsize, var_name = f"pim_{idx}", aligned_to = root_expr, host_memory_reference = f"return_vec.data()")
                else:
                    other_expr = PimObj(elem_ty_to_enum[regs[idx].precision], regs[idx].size, var_name = f"pim_{idx}", aligned_to = root_expr, host_memory_reference = f"reg_{regs[idx].index}.data()")
                pim_objs[idx] = other_expr




        stmts = []
        stmts.append(f"{expr_return_type} return_vec;")

        # Allocate root first
        stmts.append(
            root_expr.emit_pim_allocation()
        )

        for idx, pim_obj in enumerate(pim_objs):
            if idx == arg_max:
                continue

            stmts.append(
                pim_obj.emit_pim_allocation()
            )

        # Emit data movements

        for idx, pim_obj in enumerate(pim_objs):
            if idx == num_exprs - 1:
                # Emit copy device to host
                stmts.append(
                    pim_obj.emit_pim_copy_to_host(use_fused = False)
                )
            else:
                # Emit host to device
                stmts.append(
                    pim_obj.emit_pim_copy_to_device(use_fused = False)
                )



        # Free all allocations
        for idx, pim_obj in enumerate(pim_objs):
            stmts.append(
                pim_obj.emit_pim_deallocation()
            )



        return stmts























if __name__ == "__main__":
    pim_config = PIM_CONFIG(device_type = PimDeviceEnum.PIM_DEVICE_BANK_LEVEL, num_ranks = 1, num_banks_per_rank = 1, num_subarray_per_bank = 8, num_rows = 1024, num_cols = 8192)
    fused_stats_path = "/home/arnoor2/PiMCOM/codegen-generator/targets/DRAM_BitSIMD/perf_cost_model/fused_perf_results.txt"
    unfused_stats_path = "/home/arnoor2/PiMCOM/codegen-generator/targets/DRAM_BitSIMD/perf_cost_model/unfused_perf_results.txt"
    pim_config.generate_perf_csv(fused_stats_path = fused_stats_path, unfused_stats_path =  unfused_stats_path)



