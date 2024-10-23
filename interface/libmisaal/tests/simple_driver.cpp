#include "misaal.h"
#include <stdio.h>


int main(){

    std::vector<std::string> expressions;
    expressions.push_back("(typed:vec-add (reg (bv 0 4)) (reg (bv 1 4)) 32 2048 )");

    misaal::MisaalCompiler compiler (misaal::TARGET::HVX);

    for(int i =0; i < expressions.size(); i++){
        std::string test_name = "hydride.node."+std::to_string(i);
        std::string expr = expressions[i];
        compiler.add_expression_to_compile(expr, test_name);
    }


    compiler.compile_expression("misaal.driver.out", "driver");

    return 0;
}
