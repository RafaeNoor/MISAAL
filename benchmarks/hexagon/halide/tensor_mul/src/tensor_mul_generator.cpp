#include "Halide.h"

using namespace Halide;

class TensorMul : public Generator<TensorMul> {
public:
    Input<Buffer<int8_t>> A{ "A", 2 };
    Input<Buffer<int8_t>> B{ "B", 2 };
    Output<Buffer<int16_t>> output{ "output", 2 };

    void generate() {
        output(x, y) = cast<int16_t>(A(x,y)) * cast<int16_t>(B(x,y));
        output
            .compute_root()
            .reorder({y,x})
            .vectorize(x, 128)
            ;

    }
private:
    Var x{ "x" }, y{ "y" };
};
HALIDE_REGISTER_GENERATOR(TensorMul, tensor_mul)
