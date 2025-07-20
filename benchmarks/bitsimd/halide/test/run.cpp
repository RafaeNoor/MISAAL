#include <chrono>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#include "HalideBuffer.h"
#include "libpimeval.h"
#include <vector>

#if benchmark_tensor_add
#include "tensor_add.h"
#elif benchmark_relu
#include "relu.h"
#endif

#define LOG2VLEN 7
#define VLEN (1 << LOG2VLEN)

#define O_CREAT_WRONLY_TRUNC (O_CREAT | O_WRONLY | O_TRUNC)

#define NUM_ITERATIONS 1
#define WARMUP 0

extern "C" {
    ssize_t write(int, const void *, size_t);
}

void *aligned_malloc(size_t size, unsigned alignment) {
    void *result = NULL;
    int rc;
    rc = posix_memalign(&result, alignment, size);
    return result;
}

int write_file(int fp, unsigned char *src, int height, int width,
        int border_width) {
    int i;
    for (i = 0; i < height; i++) {
        if (write(fp, &src[i * width], sizeof(unsigned char) * (width)) !=
                (width)) {
            return 1;
        }
    }
    return 0;
}

template <typename F> float benchmark(F op) {

    // Run for WARMUP iterations to warm up
    for (int i = 0; i < WARMUP; i++) {
        op();
    }


    for (int i = 0; i < NUM_ITERATIONS; i++) {
        op();
    }

    return 0.0;
}

// This is a basic implementation of the Halide runtime for Hexagon.
void halide_print(void *user_context, const char *str) {
    if (str) {
        // log_printf("%s", str);
    }
}

void halide_error(void *user_context, const char *str) {
    if (!str) {
        // log_printf("Unknown error\n");
    } else if (*str == '\0' || str[strlen(str) - 1] != '\n') {
        // log_printf("Error: %s\n", str);
    } else {
        // log_printf("Error: %s", str);
    }
}

int main(int argc, char **argv) {



    printf("Invoked Benchmarking script!\n");


    // 1GB capacity
    unsigned numRanks = 1;
    unsigned numBankPerRank = 1;
    unsigned numSubarrayPerBank = 8;
    unsigned numRows = 1024;
    unsigned numCols = 8192;
    PimStatus status = pimCreateDevice(PIM_DEVICE_BANK_LEVEL, numRanks, numBankPerRank, numSubarrayPerBank, numRows, numCols);
    //PimStatus status = pimCreateDevice(PIM_FUNCTIONAL, numRanks, numBankPerRank, numSubarrayPerBank, numRows, numCols);

#if benchmark_tensor_add
    printf("Testing With Tensor Add!\n");
    int simple_width = 1024;
    int simple_height = 1;

    halide_dimension_t x_dim{0, simple_width, 1};
    halide_dimension_t y_dim{0, simple_height, simple_width};
    halide_dimension_t shape[2] = {x_dim, y_dim};

    int32_t *simple_input_1 =
        (int32_t *)malloc(simple_width * simple_height * sizeof(int32_t));
    int32_t *simple_input_2 =
        (int32_t *)malloc(simple_width * simple_height * sizeof(int32_t));

    for (int i = 0; i < simple_width * simple_height; i++) {
        simple_input_1[i] = 2;
        simple_input_2[i] = 1;
    }

    int32_t *simple_output =
        (int32_t *)malloc(simple_width * simple_height * sizeof(int32_t));

    Halide::Runtime::Buffer<int32_t> input_buf_1(simple_input_1, 2, shape);
    Halide::Runtime::Buffer<int32_t> input_buf_2(simple_input_2, 2, shape);
    Halide::Runtime::Buffer<int32_t> output_buf(simple_output, 2, shape);

    benchmark([&]() {
            int error = tensor_add(input_buf_1, input_buf_2, output_buf);
            if (error != 0) {
            printf("tensor_add pipeline failed: %d\n", error);
            }
            });

    printf("Completed executing tensor_add!\n");
    for (int x = 0; x < std::min(10, simple_width); x++)
        for (int y = 0; y < std::min(10, simple_height); y++)
            printf("(x: %d, y: %d) ==> input-vals: (%d,%d),   output-val: %d\n", x, y,
                    input_buf_1(x, y), input_buf_2(x, y),output_buf(x, y));


    free(simple_input_1);
    free(simple_input_2);
    free(simple_output);
#endif

    printf("Success!\n");
    pimShowStats();

    return 0;
}
