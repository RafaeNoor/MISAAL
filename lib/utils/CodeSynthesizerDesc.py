import sys
import os
import time
import subprocess as sb
from common.DSLParser import parse_dict
from x86SemanticsAllArgs import semantcs
from common.PredefinedDSL import *
from common.StructDef import StructDef
from interpreter.InterpreterDef import InterpreterDef
from utils.CostDef import CostDef
from utils.GetLengthDef import GetLengthDef
from utils.GetOutPrecDef import GetOutPrecDef
from utils.IRPrinter import IRPrinter
from utils.BindDef import BindDef
from utils.GetBVOps import GetBVOps
from Specification import Specification, parse_spec
from utils.VisitorDef import VisitorDef
from utils.ScaleDef import ScaleDef
from utils.GetTargetSpecificNames import GetTargetNames
from utils.GetSubExpressions import GetSubExpressions
from utils.ExtractExprDepth import ExtractExprDepth
from utils.ConstFold import ConstFold
from utils.GetVariants import GetVariants

class CodeSynthesizerDesc:
    """Class to capture the names of the various components of Hydride's automatically
    generated code-synthesizer components
    """
    def __init__(self, target_name = "" ,interpreter_name = "",
    cost_name = "", bind_name = "", printer_name = "",
    get_prec_name = "", get_length_name = "" , target_vector_sizes = [], visitor_name = "", get_ops_name = "", const_fold_name = "", emit_interpreter = False, sema_path = None, dict_name = None):
        """Constructor

        Args:
            interpreter_name (str, optional): _description_. Defaults to "".
            cost_name (str, optional): _description_. Defaults to "".
            bind_name (str, optional): _description_. Defaults to "".
            printer_name (str, optional): _description_. Defaults to "".
            get_prec_name (str, optional): _description_. Defaults to "".
            get_length_name (str, optional): _description_. Defaults to "".
        """
        self.target_name = target_name
        self.interpreter_name = interpreter_name
        self.cost_name = cost_name
        self.bind_name = bind_name
        self.printer_name = printer_name
        self.get_prec_name = get_prec_name
        self.get_length_name = get_length_name
        self.target_vector_sizes = target_vector_sizes
        self.visitor_name = visitor_name
        self.const_fold_name = const_fold_name
        self.get_ops_name = get_ops_name
        self.set_target_name = "(set-target-{})".format(self.target_name)
        self.emit_interpreter = emit_interpreter
        self.sema_path = sema_path
        self.dict_name = dict_name
        self.emit_sema = True

    def interpret_expr(self, expr, env_name):
        return "({} {} {})".format(self.interpreter_name, str(expr), env_name)

    def get_target_vector_sizes(self):
        return self.target_vector_sizes


    def emit_interpreter_framework(self, dsl_list):
        sd = StructDef(emit_default = False)
        idd = InterpreterDef()
        cd = CostDef()
#sp = parse_spec(specification)
        gl = GetLengthDef(get_len_name = self.get_length_name)
        gp = GetOutPrecDef(get_prec_name = self.get_prec_name)
        ip = IRPrinter(printer_name = self.printer_name, get_length_name = self.get_length_name, get_prec_name = self.get_prec_name)
        bd = BindDef(bind_name = self.bind_name)
        vd = VisitorDef()
        gbo = GetBVOps(get_ops_name = self.get_ops_name)
        const_fold = ConstFold(aggressive = False)
        agg_const_fold = ConstFold(aggressive = True)

        statements = []

        if self.emit_sema:
            for dsl_inst in dsl_list:
                statements.append(dsl_inst.get_semantics())

            statements.append(sd.emit_struct_defs(dsl_list))
        statements.append(cd.emit_cost_model(dsl_list, sd, cost_name = self.cost_name, use_label = self.emit_sema))

        statements.append(idd.emit_interpreter(dsl_list, sd, add_assertions = False, interpret_name = self.interpreter_name))

        statements.append(gl.emit_get_length(dsl_list, sd))

        statements.append(gp.emit_get_prec(dsl_list, sd))

        statements.append(ip.emit_dsl_printer(dsl_list, sd, prog_name = "prog"))

        statements.append(bd.emit_binder(dsl_list ,sd))

        statements.append(vd.emit_visitor(dsl_list, sd, visitor_name = self.visitor_name))

        statements.append(gbo.emit_get_bv_ops(dsl_list, sd))
        statements.append(const_fold.emit_const_fold(dsl_list, sd, const_fold_name = self.const_fold_name, interpret_name = self.interpreter_name))
        statements.append(agg_const_fold.emit_const_fold(dsl_list, sd, const_fold_name = "aggressive-"+self.const_fold_name, interpret_name = self.interpreter_name))


        return "\n".join(statements)


    def emit_struct_def(self, dsl_list):
        sd = StructDef(emit_default = False)
        return sd.emit_struct_defs(dsl_list)

    def emit_interpreter_def(self, dsl_list):
        sd = StructDef(emit_default = False)
        idd = InterpreterDef()
        return idd.emit_interpreter(dsl_list, sd, add_assertions = False, interpret_name = self.interpreter_name)

    def emit_cost_def(self, dsl_list):
        sd = StructDef(emit_default = False)
        cd = CostDef()
        return cd.emit_cost_model(dsl_list, sd, cost_name = self.cost_name, use_label = self.emit_sema)






def create_synth_desc(base_prefix, emit_interpreter, target_sizes, sema_path, dict_name):
    def join(string):
        return base_prefix +":"+string

    return CodeSynthesizerDesc(target_name = base_prefix, interpreter_name = join("interpret"), cost_name = join("cost"),
                               bind_name = join("bind-expr"), printer_name = join("hydride-printer"), get_prec_name = join("get-prec"), get_length_name = join("get-length"), target_vector_sizes = target_sizes, visitor_name = join("visitor"), get_ops_name = join("get-bv-ops"), const_fold_name = join("const-fold") , emit_interpreter = emit_interpreter, sema_path = sema_path, dict_name = dict_name)

MISAAL_SRC =  "/home/arnoor2/MISAAL/"#os.getenv('MISAAL_SRC',default = "/home/arnoor2/MISAAL/")



X86_SYNTH_DESC = CodeSynthesizerDesc(target_name= "x86",interpreter_name="hydride:interpret", cost_name= "hydride:cost",
bind_name="bind-expr", printer_name="hydride:hydride-printer", get_prec_name="hydride:get-prec",
                                     get_length_name="hydride:get-length", target_vector_sizes = [32, 64,128, 256, 512], visitor_name = "hydride:visitor", get_ops_name = "hydride:get-bv-ops", sema_path = os.path.join(MISAAL_SRC, "/lib/sema/x86SemanticsAllArgs.py"), dict_name = "semantcs")

HVX_SYNTH_DESC = CodeSynthesizerDesc(target_name= "hvx",interpreter_name="hvx:interpret", cost_name= "hvx:cost",
bind_name="hvx:bind-expr", printer_name="hvx:hydride-printer", get_prec_name="hvx:get-prec",
get_length_name="hvx:get-length", target_vector_sizes = [1024, 2048], visitor_name = "hvx:visitor", get_ops_name = "hvx:get-bv-ops", sema_path = os.path.join(MISAAL_SRC, "/lib/sema/hexsemantics_new.py"), dict_name = "semantics")


ARM_SYNTH_DESC = CodeSynthesizerDesc(target_name= "arm",interpreter_name="arm:interpret", cost_name= "arm:cost",
bind_name="arm:bind-expr", printer_name="arm:hydride-printer", get_prec_name="arm:get-prec",
get_length_name="arm:get-length", target_vector_sizes = [32, 64, 128], visitor_name = "arm:visitor", get_ops_name = "arm:get-bv-ops" , sema_path = os.path.join(MISAAL_SRC, "/lib/sema/ARMSema.py"), dict_name = "arm_semantics" )

HALIDE_X86_SYNTH_DESC = CodeSynthesizerDesc(target_name= "halide",interpreter_name="typed:halide:interpret-hydride", cost_name= "typed:halide:cost", bind_name="halide:bind-expr", printer_name="typed:halide:hydride-printer", get_prec_name="typed:halide:get-prec", get_length_name="typed:halide:get-length", target_vector_sizes = [32, 64,128, 256, 512], visitor_name = "typed:halide:visitor", get_ops_name = "typed:halide:get-bv-ops" , sema_path = os.path.join(MISAAL_SRC,"/lib/sema/halide_sema.py"), dict_name = "halide_semantics")


HALIDE_HVX_SYNTH_DESC = CodeSynthesizerDesc(target_name= "halide",interpreter_name="typed:halide:interpret-hydride", cost_name= "typed:halide:cost", bind_name="halide:bind-expr", printer_name="typed:halide:hydride-printer", get_prec_name="typed:halide:get-prec", get_length_name="typed:halide:get-length", target_vector_sizes = [1024, 2048] , visitor_name = "typed:halide:visitor", get_ops_name = "typed:halide:get-bv-ops" , sema_path = os.path.join(MISAAL_SRC,"/lib/sema/halide_sema.py"), dict_name = "halide_semantics" )

