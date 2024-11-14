#include "Halide.h"
#include "../../hannk/common_halide.h"
#include "../../hannk/constants.h"
using namespace Halide;

class TensorShr : public Generator<TensorShr> {
public:
    Input<Buffer<int16_t>> A{ "A", 2 };
    Input<Buffer<uint16_t>> B{ "B", 2 };
    Output<Buffer<uint8_t>> output{ "output", 2 };

    void generate() {
        Type narrow = A.type().narrow().with_code(Type::UInt);
        output(x, y) = saturating_cast(narrow,(A(x,y) >> B(x,y)));
        output
            .compute_root()
            .reorder({y,x})
            .vectorize(x, 64)
            ;

    }
private:
    Var x{ "x" }, y{ "y" };
};
HALIDE_REGISTER_GENERATOR(TensorShr, tensor_shr_sat)
