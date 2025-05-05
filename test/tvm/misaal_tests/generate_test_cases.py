import os

test_case_dir = "/u/is16/526/MISAAL/test/tvm/misaal_tests/test_cases"
test_template = "/u/is16/526/MISAAL/test/tvm/misaal_tests/test_case_template.txt"

class Test:
    def __init__(self, test_name, dtype, buffer_size, vector_size, numpy_op, tir_func):
        self.test_name = test_name
        self.dtype = dtype
        self.buffer_size = buffer_size
        self.vector_size = vector_size
        self.numpy_op = numpy_op
        self.tir_func =tir_func

    def generate_test(self):
        test_file_name = test_case_dir + f"/test_{self.test_name}.py"
        with open(test_template, 'r') as file:
            test_text = file.read()
            test_text = test_text.replace("TEST_NAME", self.test_name) 
            test_text = test_text.replace("DTYPE", self.dtype) 
            test_text = test_text.replace("BUFFER_SIZE", str(self.buffer_size)) 
            test_text = test_text.replace("VECTOR_SIZE", str(self.vector_size)) 
            test_text = test_text.replace("NUMPY_OP", self.numpy_op) 
            test_text = test_text.replace("TIR_FUNC", self.tir_func) 
        with open(test_file_name, 'w') as file:
            file.write(test_text)
        
tests = [
    Test("vec_add", 
         "int16",
         128,
         4,
         "lambda x,y : x + y",
         "T.Add",
         ),
    Test("vec_sub", 
         "int32",
         128,
         8,
         "lambda x,y : x - y",
         "T.Sub",
         ),
    Test("vec_mod", 
         "int32",
         128,
         8,
         "lambda x,y : np.mod(x,y)",
         "T.Sub",
         ),
    Test("vec_max", 
         "int32",
         128,
         8,
         "lambda x,y : np.max([x, y], axis=0)",
         "T.Max",
         ),
    Test("vec_min", 
         "int32",
         128,
         8,
         "lambda x,y : np.min([x, y], axis=0)",
         "T.Min",
         ),
    Test("vec_bwor", 
         "int32",
         128,
         16,
         "lambda x,y : np.bitwise_or(x,y)",
         "T.bitwise_or",
         ),
    Test("vec_bwand", 
         "int16",
         128,
         32,
         "lambda x,y : np.bitwise_and(x,y)",
         "T.bitwise_and",
         ),
]

for test in tests:
    test.generate_test()