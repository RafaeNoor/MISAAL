#!/usr/bin/env python3
import os, glob, sys

test_case_dir = "/u/is16/526/MISAAL/test/tvm/misaal_tests/test_cases"
test_template = "/u/is16/526/MISAAL/test/tvm/misaal_tests/test_case_template.txt"
test_template_cast = "/u/is16/526/MISAAL/test/tvm/misaal_tests/test_case_template_cast.txt"

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

class CastTest:
    def __init__(self, test_name, input_dtype, output_dtype, buffer_size, vector_size):
        self.test_name = test_name
        self.input_dtype = input_dtype
        self.output_dtype = output_dtype
        self.buffer_size = buffer_size
        self.vector_size = vector_size

    def generate_test(self):
        test_file_name = test_case_dir + f"/test_{self.test_name}.py"
        with open(test_template_cast, 'r') as file:
            test_text = file.read()
            test_text = test_text.replace("TEST_NAME", self.test_name) 
            test_text = test_text.replace("INPUT_DTYPE", self.input_dtype) 
            test_text = test_text.replace("OUTPUT_DTYPE", self.output_dtype) 
            test_text = test_text.replace("BUFFER_SIZE", str(self.buffer_size)) 
            test_text = test_text.replace("VECTOR_SIZE", str(self.vector_size)) 
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
    Test("vec_mul", 
         "uint32",
         128,
         16,
         "lambda x,y : x * y",
         "T.Mul",
         ),
    ## Not supported by MISAAL but it still compiles correctly.
    Test("vec_div", 
         "uint32",
         128,
         16,
         "lambda x,y : x // y",
         "T.Div",
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
    CastTest("cast_extend", 
         "int16",
         "int32",
         128,
         8,
         ),
    CastTest("cast_truncate", 
         "int32",
         "int16",
         128,
         8,
         ),
]

if len(sys.argv) > 1 and str(sys.argv[1]) == "clean":
    for file in glob.glob(test_case_dir + "/*"):
        if not os.path.isdir(file):
            os.remove(file)

for test in tests:
    test.generate_test()