#include "misaal.h"
#include <stdio.h>


int main(){

    misaal::MisaalCompiler compiler (misaal::TARGET::HVX);

    compiler.compile_expression("out.ll", "driver");

    return 0;
}
