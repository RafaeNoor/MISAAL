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


  free(input);
  free(output);
  printf("Success!\n");

  return 0;
}
