#include "Halide.h"

using namespace Halide;

#define M 4096
#define N 1
#define K 4096

class Matmul : public Generator<Matmul> {
public:
    GeneratorParam<int> matrix_size{"size", K};
    Input<Buffer<int32_t>> A{ "A", 2 };
    Input<Buffer<int32_t>> B{ "B", 2 };
    Output<Buffer<int32_t>> output{ "output", 2 };

    void generate() {
        RDom k(0, K);

        output(x, y) = 0;
        output(x, y) += A(x,k) * B(k,y);
        // Schedules for BitSIMD 
        output
            .update(0)
            .specialize(A.dim(0).extent() == M)
            .specialize(A.dim(1).extent() == K)
            .specialize(B.dim(0).extent() == K)
            .specialize(B.dim(1).extent() == N)
            .specialize(output.dim(0).extent() == M)
            .specialize(output.dim(1).extent() == N)
            .fuse(x, y, x)
            .vectorize(x, M)
            .unroll(k, 64/4)
            ;


    }

    void schedule() {}

private:
    Var x{ "x" }, y{ "y" };
};

HALIDE_REGISTER_GENERATOR(Matmul, gemv_v1)
