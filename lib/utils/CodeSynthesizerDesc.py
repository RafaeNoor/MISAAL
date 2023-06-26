

class CodeSynthesizerDesc:
    """Class to capture the names of the various components of Hydride's automatically
    generated code-synthesizer components
    """
    def __init__(self, interpreter_name = "",
    cost_name = "", bind_name = "", printer_name = "",
    get_prec_name = "", get_length_name = "" ):
        """Constructor

        Args:
            interpreter_name (str, optional): _description_. Defaults to "".
            cost_name (str, optional): _description_. Defaults to "".
            bind_name (str, optional): _description_. Defaults to "".
            printer_name (str, optional): _description_. Defaults to "".
            get_prec_name (str, optional): _description_. Defaults to "".
            get_length_name (str, optional): _description_. Defaults to "".
        """

        self.interpreter_name = interpreter_name
        self.cost_name = cost_name
        self.bind_name = bind_name
        self.printer_name = printer_name
        self.get_prec_name = get_prec_name
        self.get_length_name = get_length_name

    def interpret_expr(self, expr, env_name):
        return "({} {} {})".format(self.interpreter_name, str(expr), env_name)
    
        




X86_SYNTH_DESC = CodeSynthesizerDesc(interpreter_name="hydride:interpret", cost_name= "hydride:cost",
bind_name="bind-expr", printer_name="hydride:print-expr", get_prec_name="hydride:get-prec",
get_length_name="hydride:get-length")