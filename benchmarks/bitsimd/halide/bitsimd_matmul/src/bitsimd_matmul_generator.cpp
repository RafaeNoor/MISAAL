#include "Halide.h"

using namespace Halide;

class Matmul : public Generator<Matmul> {
public:
    GeneratorParam<int> matrix_size{"size", 1024};
    Input<Buffer<int32_t>> A{ "A", 2 };
    Input<Buffer<int32_t>> B{ "B", 2 };
    Output<Buffer<int32_t>> output{ "output", 2 };

    void generate() {
        RDom k(0, matrix_size);

        output(x, y) = 0;
        output(x, y) += A(x,k) * B(k,y);
        // Schedules for BitSIMD 
        output
            .update(0)
            .specialize(A.dim(0).extent() == 1024)
            .specialize(A.dim(1).extent() == 1024)
            .specialize(B.dim(0).extent() == 1024)
            .specialize(B.dim(1).extent() == 1024)
            .specialize(output.dim(0).extent() == 1024)
            .specialize(output.dim(1).extent() == 1024)
            .fuse(x, y, x)
            .vectorize(x,1024 * 1024)
            .unroll(k, 64)
            ;

    }

    void schedule() {}

private:
    Var x{ "x" }, y{ "y" };
};

HALIDE_REGISTER_GENERATOR(Matmul, bitsimd_matmul)
