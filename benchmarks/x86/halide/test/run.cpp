#include <chrono>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#include "HalideBuffer.h"
#include <vector>

#if benchmark_dilate3x3
#include "dilate3x3.h"
#elif benchmark_dilate5x5
#include "dilate5x5.h"
#elif benchmark_dilate7x7
#include "dilate7x7.h"
#elif benchmark_max_pool
#include "max_pool.h"
#elif benchmark_sobel3x3
#include "sobel3x3.h"
#elif benchmark_sobel5x5
#include "sobel5x5.h"
#elif benchmark_blur3x3
#include "blur3x3.h"
#elif benchmark_blur5x5
#include "blur5x5.h"
#elif benchmark_blur7x7
#include "blur7x7.h"
#elif benchmark_median3x3
#include "median3x3.h"
#elif benchmark_gaussian3x3
#include "gaussian3x3.h"
#elif benchmark_gaussian5x5
#include "gaussian5x5.h"
#elif benchmark_gaussian7x7
#include "gaussian7x7.h"
#elif benchmark_batched_matmul_256_32bit
#include "batched_matmul_256_32bit.h"
#elif benchmark_max_pool_add
#include "max_pool_add.h"
#elif benchmark_matmul_256_32bit_bias_add
#include "matmul_256_32bit_bias_add.h"
#endif

#define LOG2VLEN 7
#define VLEN (1 << LOG2VLEN)

#define O_CREAT_WRONLY_TRUNC (O_CREAT | O_WRONLY | O_TRUNC)

#define NUM_ITERATIONS 1000
#define WARMUP 50

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
  // long long start_time = q6sim_read_pcycles();

  // clock_t start_cycle = clock();

  // Run for WARMUP iterations to warm up
  for (int i = 0; i < WARMUP; i++) {
    op();
  }

  auto start_time = std::chrono::high_resolution_clock::now();

  for (int i = 0; i < NUM_ITERATIONS; i++) {
    op();
  }

  auto end_time = std::chrono::high_resolution_clock::now();

  // clock_t end_cycle = clock();

  std::chrono::duration<double> duration = end_time - start_time;

  printf("Execution took %0.4f s\n", duration.count());

  // long long total_cycles =  (long long) (end_cycle - start_cycle);

  // long long total_cycles = q6sim_read_pcycles() - start_time;
  return duration.count(); /// total_cycles;
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
  int i, in_fp;

  constexpr int dims = 2;

  /* -----------------------------------------------------*/
  /*  Get input parameters                                */
  /* -----------------------------------------------------*/
  if (argc != 3) {
    printf("usage: %s <width> <height> \n", argv[0]);
    return 1;
  }

  int width = atoi(argv[1]);
  int height = atoi(argv[2]);
  int stride = (width + (VLEN)-1) & (-(VLEN));

  /* -----------------------------------------------------*/
  /*  Allocate memory for input/output                    */
  /* -----------------------------------------------------*/

  unsigned char *input = (unsigned char *)aligned_malloc(
      width * height * sizeof(unsigned char),
      1 << LOG2VLEN); // memalign(1 << LOG2VLEN, width*height*sizeof(unsigned
                      // char));
  unsigned char *output = (unsigned char *)aligned_malloc(
      width * height * 4 * sizeof(unsigned char),
      1 << LOG2VLEN); // memalign(1 << LOG2VLEN, width*height*4*sizeof(unsigned
                      // char));

  if (input == NULL || output == NULL) {
    printf("Error: Could not allocate Memory for image\n");
    return 1;
  }


  /* -----------------------------------------------------*/
  /*  Run benchmark on the Simulator                      */
  /* -----------------------------------------------------*/
  long long cycles;

#if benchmark_dilate3x3
  halide_dimension_t x_dim{0, width, 1};
  halide_dimension_t y_dim{0, height, width};
  halide_dimension_t shape[2] = {x_dim, y_dim};

  Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
  Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

  benchmark([&]() {
    int error = dilate3x3(input_buf, output_buf);
    if (error != 0) {
      printf("dilate3x3 pipeline failed: %d\n", error);
    }
  });

#if DEBUG
  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y,
             input_buf(x, y), output_buf(x, y));
#endif

  printf("AppReported (): Image %dx%d - dilate3x3(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if benchmark_dilate5x5
  halide_dimension_t x_dim{0, width, 1};
  halide_dimension_t y_dim{0, height, width};
  halide_dimension_t shape[2] = {x_dim, y_dim};

  Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
  Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

  benchmark([&]() {
    int error = dilate5x5(input_buf, output_buf);
    if (error != 0) {
      printf("dilate5x5 pipeline failed: %d\n", error);
    }
  });

#if DEBUG
  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y,
             input_buf(x, y), output_buf(x, y));
#endif

  printf("AppReported (): Image %dx%d - dilate5x5(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if benchmark_dilate7x7
  halide_dimension_t x_dim{0, width, 1};
  halide_dimension_t y_dim{0, height, width};
  halide_dimension_t shape[2] = {x_dim, y_dim};

  Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
  Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

  benchmark([&]() {
    int error = dilate7x7(input_buf, output_buf);
    if (error != 0) {
      printf("dilate7x7 pipeline failed: %d\n", error);
    }
  });

#if DEBUG
  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y,
             input_buf(x, y), output_buf(x, y));
#endif

  printf("AppReported (): Image %dx%d - dilate7x7(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif


#if benchmark_max_pool
  halide_dimension_t c_dim{0, 1024, 1};
  halide_dimension_t x_dim{0, width / 32, 128};
  halide_dimension_t y_dim{0, height / 32, 128 * (width / 32)};
  halide_dimension_t b_dim{0, 1, 128 * (width / 32) * (height / 32)};
  halide_dimension_t shape[4] = {c_dim, x_dim, y_dim, b_dim};

  Halide::Runtime::Buffer<uint8_t> input_buf(input, 4, shape);
  Halide::Runtime::Buffer<uint8_t> output_buf(output, 4, shape);

  benchmark([&]() {
    int error = max_pool(input_buf, 2, 2, 8, 8, 5, 225, output_buf);
    if (error != 0) {
      printf("max_pool pipeline failed: %d\n", error);
    }
  });

#if DEBUG
  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y,
             input_buf(x, y), output_buf(x, y));
#endif

  printf("AppReported (): Image %dx%d - max_pool(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if benchmark_sobel3x3
  halide_dimension_t x_dim{0, width, 1};
  halide_dimension_t y_dim{0, height, width};
  halide_dimension_t shape[2] = {x_dim, y_dim};

  Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
  Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

  float exec_time = benchmark([&]() {
    int error = sobel3x3(input_buf, output_buf);
    if (error != 0) {
      printf("sobel3x3 pipeline failed: %d\n", error);
    }
  });

  printf("Execution took %0.4f s\n", exec_time);
#if DEBUG
  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y,
             input_buf(x, y), output_buf(x, y));
#endif

  printf("AppReported (): Image %dx%d - sobel3x3(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if benchmark_sobel5x5
  halide_dimension_t x_dim{0, width, 1};
  halide_dimension_t y_dim{0, height, width};
  halide_dimension_t shape[2] = {x_dim, y_dim};

  Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
  Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

  float exec_time = benchmark([&]() {
    int error = sobel5x5(input_buf, output_buf);
    if (error != 0) {
      printf("sobel5x5 pipeline failed: %d\n", error);
    }
  });

  printf("Execution took %0.4f s\n", exec_time);
#if DEBUG
  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y,
             input_buf(x, y), output_buf(x, y));
#endif

  printf("AppReported (): Image %dx%d - sobel3x3(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if benchmark_blur3x3
  halide_dimension_t x_dim{0, width / 2, 1};
  halide_dimension_t y_dim{0, height, width / 2};
  halide_dimension_t shape[2] = {x_dim, y_dim};

  Halide::Runtime::Buffer<uint16_t> input_buf((uint16_t *)input, dims, shape);
  Halide::Runtime::Buffer<uint16_t> output_buf((uint16_t *)output, dims, shape);

  cycles = benchmark([&]() {
    int error = blur3x3(input_buf, output_buf);
    if (error != 0) {
      printf("blur3x3 pipeline failed: %d\n", error);
    }
  });

#if DEBUG
  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y,
             input_buf(x, y), output_buf(x, y));

#endif

  printf("AppReported (): Image %dx%d - blur3x3(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if benchmark_blur5x5
  halide_dimension_t x_dim{0, width / 2, 1};
  halide_dimension_t y_dim{0, height, width / 2};
  halide_dimension_t shape[2] = {x_dim, y_dim};

  Halide::Runtime::Buffer<uint16_t> input_buf((uint16_t *)input, dims, shape);
  Halide::Runtime::Buffer<uint16_t> output_buf((uint16_t *)output, dims, shape);

  cycles = benchmark([&]() {
    int error = blur5x5(input_buf, output_buf);
    if (error != 0) {
      printf("blur5x5 pipeline failed: %d\n", error);
    }
  });

#if DEBUG
  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y,
             input_buf(x, y), output_buf(x, y));

#endif

  printf("AppReported (): Image %dx%d - blur5x5(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if benchmark_blur7x7
  halide_dimension_t x_dim{0, width / 2, 1};
  halide_dimension_t y_dim{0, height, width / 2};
  halide_dimension_t shape[2] = {x_dim, y_dim};

  Halide::Runtime::Buffer<uint16_t> input_buf((uint16_t *)input, dims, shape);
  Halide::Runtime::Buffer<uint16_t> output_buf((uint16_t *)output, dims, shape);

  cycles = benchmark([&]() {
    int error = blur7x7(input_buf, output_buf);
    if (error != 0) {
      printf("blur7x7 pipeline failed: %d\n", error);
    }
  });

#if DEBUG
  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y,
             input_buf(x, y), output_buf(x, y));

#endif

  printf("AppReported (): Image %dx%d - blur7x7(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif


#if benchmark_gaussian3x3
  halide_dimension_t x_dim{0, width, 1};
  // halide_dimension_t y_dim{ 1, height-1, width };
  halide_dimension_t y_dim{1, height, width};
  halide_dimension_t shape[2] = {x_dim, y_dim};

  Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
  Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

  // Run in 128 byte mode
  benchmark([&]() {
    int error = gaussian3x3(input_buf, output_buf);
    if (error != 0) {
      printf("gaussian3x3 pipeline failed: %d\n", error);
    }
  });

#if DEBUG
  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf(
          "(x: %d, y: %d) ==> input-val: %d   output-val: %d, true-val: %d\n",
          x, y, input_buf(x, y), output_buf(x, y),

          ((static_cast<int16_t>(input_buf(x - 1, y - 1)) * 1 +
            static_cast<int16_t>(input_buf(x, y - 1)) * 2 +
            static_cast<int16_t>(input_buf(x + 1, y - 1)) * 1 +
            static_cast<int16_t>(input_buf(x - 1, y)) * 2 +
            static_cast<int16_t>(input_buf(x, y)) * 4 +
            static_cast<int16_t>(input_buf(x + 1, y)) * 2 +
            static_cast<int16_t>(input_buf(x - 1, y + 1)) * 1 +
            static_cast<int16_t>(input_buf(x, y + 1)) * 2 +
            static_cast<int16_t>(input_buf(x + 1, y + 1) * 1)) +
           8) >>
              4

      );
#endif

  printf("AppReported (): Image %dx%d - gaussian3x3(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if benchmark_gaussian5x5
  halide_dimension_t x_dim{0, width, 1};
  halide_dimension_t y_dim{0, height, width};
  halide_dimension_t shape[2] = {x_dim, y_dim};

  Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
  Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

  // Run in 128 byte mode
  cycles = benchmark([&]() {
    int error = gaussian5x5(input_buf, output_buf);
    if (error != 0) {
      printf("gaussian5x5 pipeline failed: %d\n", error);
    }
  });

#if DEBUG
  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y,
             input_buf(x, y), output_buf(x, y));
#endif

  printf("AppReported (): Image %dx%d - gaussian5x5(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if benchmark_gaussian7x7
  halide_dimension_t x_dim{0, width, 1};
  halide_dimension_t y_dim{0, height, width};
  halide_dimension_t shape[2] = {x_dim, y_dim};

  Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
  Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

  // Run in 128 byte mode
  cycles = benchmark([&]() {
    int error = gaussian7x7(input_buf, output_buf);
    if (error != 0) {
      printf("gaussian7x7 pipeline failed: %d\n", error);
    }
  });

#if DEBUG
  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y,
             input_buf(x, y), output_buf(x, y));
#endif

  printf("AppReported (): Image %dx%d - gaussian7x7(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if benchmark_median3x3
  printf("\t*** median3x3\n");
  halide_dimension_t x_dim{0, width, 1};
  halide_dimension_t y_dim{0, height, width};
  halide_dimension_t shape[2] = {x_dim, y_dim};

  Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
  Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

  benchmark([&]() {
    int error = median3x3(input_buf, output_buf);
    if (error != 0) {
      printf("median3x3 pipeline failed: %d\n", error);
    }
  });
#if DEBUG

  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y,
             input_buf(x, y), output_buf(x, y));
#endif

  printf("AppReported (): Image %dx%d - median3x3(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / width / height);
#endif

#if benchmark_batched_matmul_256_32bit

  constexpr int dims_3 = 3;
  int32_t matrix_size = 256;

  int num_batches = 4;
  halide_dimension_t x_dim{0, matrix_size, 1};
  halide_dimension_t y_dim{0, matrix_size, matrix_size};
  halide_dimension_t b_dim{0, num_batches, matrix_size * matrix_size};
  halide_dimension_t shape[3] = {x_dim, y_dim, b_dim};

  int16_t matATensor[matrix_size * matrix_size * num_batches];
  int16_t matBTensor[matrix_size * matrix_size * num_batches];
  int32_t outputTensor[matrix_size * matrix_size * num_batches];

  Halide::Runtime::Buffer<int16_t> matA((int16_t *)matATensor, dims_3, shape);
  Halide::Runtime::Buffer<int16_t> matB((int16_t *)matBTensor, dims_3, shape);
  Halide::Runtime::Buffer<int32_t> output_buf((int32_t *)outputTensor, dims_3,
                                              shape);

  cycles = benchmark([&]() {
    int error = batched_matmul_256_32bit(matA, matB, output_buf);
    if (error != 0) {
      printf("batched_matmul_256_32bit pipeline failed: %d\n", error);
    }
  });

  printf("AppReported (): Image %dx%d - batched_matmul_256_32bit(): %lld "
         "cycles (%0.4f cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if benchmark_max_pool_add
  halide_dimension_t c_dim{0, 1024, 1};
  halide_dimension_t x_dim{0, width / 32, 128};
  halide_dimension_t y_dim{0, height / 32, 128 * (width / 32)};
  halide_dimension_t b_dim{0, 1, 128 * (width / 32) * (height / 32)};
  halide_dimension_t shape[4] = {c_dim, x_dim, y_dim, b_dim};

  Halide::Runtime::Buffer<uint8_t> input_buf(input, 4, shape);
  Halide::Runtime::Buffer<uint8_t> output_buf(output, 4, shape);

  benchmark([&]() {
    int error =
        max_pool_add(input_buf, input_buf, 2, 2, 8, 8, 5, 225, output_buf);
    if (error != 0) {
      printf("max_pool_add pipeline failed: %d\n", error);
    }
  });

#if DEBUG
  for (int x = 0; x < 10; x++)
    for (int y = 0; y < 10; y++)
      printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y,
             input_buf(x, y), output_buf(x, y));
#endif

  printf("AppReported (): Image %dx%d - max_pool(128B): %lld cycles (%0.4f "
         "cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if benchmark_matmul_256_32bit_bias_add

  printf("benchmark matmul_256_32bit_bias_add!\n");

  constexpr int dims_3 = 3;
  int32_t matrix_size = 256;

  int bias_size = 64;
  halide_dimension_t x_dim{0, matrix_size, 1};
  halide_dimension_t y_dim{0, matrix_size, matrix_size * 1};
  halide_dimension_t b_dim{0, bias_size, matrix_size * matrix_size};
  halide_dimension_t shape[3] = {b_dim, x_dim, y_dim};

  printf("Allocating memory!\n");

  /*
  int16_t matATensor[matrix_size * matrix_size * bias_size ];
  int16_t matBTensor[matrix_size * matrix_size * bias_size ];
  int32_t bias_[bias_size];
  int32_t outputTensor[matrix_size * matrix_size * bias_size ];
  */

  /*
  int16_t* matATensor = (int16_t*) aligned_malloc(matrix_size * matrix_size *
  bias_size * sizeof(int16_t), 1 << LOG2VLEN); int16_t* matBTensor = (int16_t*)
  aligned_malloc(matrix_size * matrix_size * bias_size *  sizeof(int16_t), 1 <<
  LOG2VLEN); int32_t* outputTensor = (int32_t*) aligned_malloc(matrix_size *
  matrix_size * bias_size * sizeof(int32_t), 1 << LOG2VLEN); int32_t* bias_ =
  (int32_t*) aligned_malloc(bias_size * sizeof(int32_t), 1 << LOG2VLEN);
  */

  int16_t *matATensor = (int16_t *)malloc(matrix_size * matrix_size *
                                          bias_size * sizeof(int16_t));
  int16_t *matBTensor = (int16_t *)malloc(matrix_size * matrix_size *
                                          bias_size * sizeof(int16_t));
  int32_t *outputTensor = (int32_t *)malloc(matrix_size * matrix_size *
                                            bias_size * sizeof(int32_t));
  int32_t *bias_ = (int32_t *)malloc(bias_size * sizeof(int32_t));

  printf("Creating runtime buffers!\n");

  Halide::Runtime::Buffer<int16_t> matA((int16_t *)matATensor, dims_3, shape);
  Halide::Runtime::Buffer<int16_t> matB((int16_t *)matBTensor, dims_3, shape);

  halide_dimension_t bias_dim{0, bias_size, 1};
  halide_dimension_t bias_shape[1] = {bias_dim};

  Halide::Runtime::Buffer<int32_t> bias_buf((int32_t *)bias_, 1, bias_shape);
  Halide::Runtime::Buffer<int32_t> output_buf((int32_t *)outputTensor, dims_3,
                                              shape);

  printf("About to launch kernel!\n");
  cycles = benchmark([&]() {
    int error = matmul_256_32bit_bias_add(matA, matB, bias_buf, output_buf);
    if (error != 0) {
      printf("matmul_256_32bit_bias_add pipeline failed: %d\n", error);
    }
  });

  free(matATensor);
  free(matBTensor);
  free(outputTensor);
  free(bias_);

  printf("AppReported (): Image %dx%d - matmul_256_32bit_bias_add(): %lld "
         "cycles (%0.4f cycles/pixel)\n",
         (int)width, (int)height, cycles, (float)cycles / (width * height));

#endif

  free(input);
  free(output);
  printf("Success!\n");

  return 0;
}
