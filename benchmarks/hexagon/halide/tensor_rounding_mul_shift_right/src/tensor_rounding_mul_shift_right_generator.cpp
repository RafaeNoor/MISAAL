#include "Halide.h"

using namespace Halide;

class TensorShr : public Generator<TensorShr> {
public:
    Input<Buffer<int32_t>> A{ "A", 2 };
    Input<Buffer<int32_t>> B{ "B", 2 };
    Output<Buffer<int32_t>> output{ "output", 2 };

    void generate() {
        output(x, y) = rounding_mul_shift_right(A(x,y),B(x,y), 31);
        output
            .compute_root()
            .reorder({y,x})
            .vectorize(x, 1024/ 32)
            ;

    }
private:
    Var x{ "x" }, y{ "y" };
};
HALIDE_REGISTER_GENERATOR(TensorShr, tensor_rounding_mul_shift_right)
