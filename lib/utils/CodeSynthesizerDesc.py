

class CodeSynthesizerDesc:
    """Class to capture the names of the various components of Hydride's automatically
    generated code-synthesizer components
    """
    def __init__(self, target_name = "" ,interpreter_name = "",
    cost_name = "", bind_name = "", printer_name = "",
    get_prec_name = "", get_length_name = "" , target_vector_sizes = []):
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

    def interpret_expr(self, expr, env_name):
        return "({} {} {})".format(self.interpreter_name, str(expr), env_name)

    def get_target_vector_sizes(self):
        return self.target_vector_sizes






X86_SYNTH_DESC = CodeSynthesizerDesc(target_name= "x86",interpreter_name="hydride:interpret", cost_name= "hydride:cost",
bind_name="bind-expr", printer_name="hydride:hydride-printer", get_prec_name="hydride:get-prec",
get_length_name="hydride:get-length", target_vector_sizes = [32, 64,128, 256, 512])

HVX_SYNTH_DESC = CodeSynthesizerDesc(target_name= "hvx",interpreter_name="hvx:interpret", cost_name= "hvx:cost",
bind_name="hvx:bind-expr", printer_name="hvx:hydride-printer", get_prec_name="hvx:get-prec",
get_length_name="hvx:get-length", target_vector_sizes = [1024, 2048])
