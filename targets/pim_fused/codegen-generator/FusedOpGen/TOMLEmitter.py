from Ops import *



def emit_toml_str(expr, collection_name):
    assert isinstance(expr, FunctionOp)
    context = {"loop_index_var": "idx"}
    defns, context = expr.emit_semantics_pseudocode(context)

    func_name = expr.name
    regs = expr.get_registers()
    operand_sizes = [reg.output_size for reg in regs]
    operand_layouts = ["DRAM_VERT"] * len(regs)
    operand_elem_bw = [reg.bitwidth for reg in regs]
    signedness = int(expr.signedness)
    semantics = defns[0]
    result_size = expr.output_size
    result_bitwidth = expr.bitwidth

    tomls_stmts = []

    class_decl = f"[{collection_name}.{func_name}]"
    tomls_stmts.append(class_decl)

    name_decl = f"name = \"{func_name}\""
    tomls_stmts.append(name_decl)

    opnd_size_decl = f"operand_sizes = {operand_sizes}"
    tomls_stmts.append(opnd_size_decl)

    opnd_layout_decl = f"operand_layouts = {operand_layouts}"
    tomls_stmts.append(opnd_layout_decl)

    opnd_bw_decl = f"operand_elem_bw = {operand_elem_bw}"
    tomls_stmts.append(opnd_bw_decl)

    result_layout_decl = "result_layout = \"DRAM_VERT\""
    tomls_stmts.append(result_layout_decl)

    result_size_decl = f"result_size = {result_size}"
    tomls_stmts.append(result_size_decl)

    result_bw_decl = f"result_elem_bw = {result_bitwidth}"
    tomls_stmts.append(result_bw_decl)

    result_signedness_decl = f"signedness = {signedness}"
    tomls_stmts.append(result_signedness_decl)

    semantics_decl = "semantics = \"\"\"\\\n" + semantics + "\n\"\"\"\n"
    tomls_stmts.append(semantics_decl)



    return "\n".join(tomls_stmts)
