#include "Halide.h"

using namespace Halide;

class TensorAdd : public Generator<TensorAdd> {
public:
    Input<Buffer<int8_t>> A{ "A", 2 };
    Input<Buffer<int8_t>> B{ "B", 2 };
    Output<Buffer<int8_t>> output{ "output", 2 };

    void generate() {
        output(x, y) = rounding_halving_add(A(x,y), B(x,y));
        output
            .compute_root()
            .reorder({y,x})
            .vectorize(x, 128)
            ;

    }
private:
    Var x{ "x" }, y{ "y" };
};
HALIDE_REGISTER_GENERATOR(TensorAdd, tensor_rounding_halving_add)
