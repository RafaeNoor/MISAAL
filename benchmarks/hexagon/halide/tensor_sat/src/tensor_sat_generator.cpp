#include "Halide.h"
#include "../../hannk/common_halide.h"
#include "../../hannk/constants.h"

using namespace Halide;

class TensorAdd : public Generator<TensorAdd> {
public:
    Input<Buffer<int16_t>> A{ "A", 2 };
    Output<Buffer<int8_t>> output{ "output", 2 };

    void generate() {
        Type narrow = A.type().narrow().with_code(Type::Int);
        output(x, y) = saturating_cast(narrow , A(x,y)) ;
        output
            .compute_root()
            .reorder({y,x})
            .vectorize(x, 1024 / 8)
            ;

    }
private:
    Var x{ "x" }, y{ "y" };
};
HALIDE_REGISTER_GENERATOR(TensorAdd, tensor_sat)
