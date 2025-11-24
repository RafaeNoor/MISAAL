#include "Halide.h"

using namespace Halide;

// To understanding rfactor scheduling directive for factoring reductions, 
// please see https://halide-lang.org/tutorials/tutorial_lesson_18_parallel_associative_reductions.html
//
#define IMAGE_ROW 8192
#define iMAGE_COL 34

// #define IMG_8BIT

class Histogram : public Generator<Histogram> {
public:
#ifdef IMG_8BIT
    Input<Buffer<uint8_t>> IMG{ "IMG", 3 };
#else
    Input<Buffer<int32_t>> IMG{ "IMG", 3 };
#endif
    Output<Buffer<int32_t>> BINS{ "BINS", 2 };


    void generate() {
        RDom k(0, IMG.dim(0).extent(), 0, IMG.dim(1).extent());
        const int32_t vectorization_factor = 8192;

        // Histogram Algorithm
        Func color_hist("color_hist");
        color_hist(i,c) = 0;
#ifdef IMG_8BIT
        color_hist(clamp(IMG(k.x, k.y, c), cast<uint8_t>(0), cast<uint8_t>(255)), c) += 1;
#else
        color_hist(clamp(IMG(k.x, k.y, c), 0, 255), c) += 1;
#endif

        // Histogram Schedule
        //
        Func intermediate_color = color_hist.update().rfactor({{k.x, u}});
        intermediate_color.compute_root().update().vectorize(u, vectorization_factor);

        intermediate_color
            .vectorize(i, vectorization_factor)
            ;
        color_hist
             .vectorize(i, vectorization_factor)
            ;


        // Final definition of output bins
        BINS(x, c) = color_hist(x,c);
        


    }

    void schedule() {}

private:
    Var x{ "x" }, y{ "y" }, i{ "i" }, u { "u" }, v { "v" }, c {"c"};
};

HALIDE_REGISTER_GENERATOR(Histogram, histogram)
