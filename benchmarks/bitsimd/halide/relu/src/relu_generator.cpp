#include "Halide.h"

using namespace Halide;

class ReLU : public Generator<ReLU> {
public:
    Input<Buffer<int32_t>> A{ "A", 2 };
    Output<Buffer<int32_t>> output{ "output", 2 };

    void generate() {
        output(x, y) = max(A(x,y) , 0);
        // Schedules for BitSIMD 
        output
            .compute_root()
            .reorder({y,x})
            .vectorize(x, 4)
            ;

    }
private:
    Var x{ "x" }, y{ "y" }, yi{"yi"}, xi{"xi"};
};

HALIDE_REGISTER_GENERATOR(ReLU, relu)
