#include "Halide.h"

using namespace Halide;

class FilterByKey : public Generator<FilterByKey> {
public:
    Input<Buffer<int32_t>> Input{ "Input", 1 };
    Output<Buffer<int32_t>> Output{ "Output", 1 };

    void generate() {
        int32_t key = 56;
        Output(x) =  select(key > Input(x), (int32_t) 1, (int32_t) 0);

        // Schedules for BitSIMD 
        Output
            .compute_root()
            .vectorize(x, 4)
            ;

    }
private:
    Var x{ "x" }, y{ "y" };
};
HALIDE_REGISTER_GENERATOR(FilterByKey, filter_by_key)
