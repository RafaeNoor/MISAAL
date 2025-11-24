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
#elif benchmark_axpy 
#include "axpy.h"
#elif benchmark_relu
#include "relu.h"
#elif benchmark_gemv_v1
#include "gemv_v1.h"
#elif benchmark_gemv_v2
#include "gemv_v2.h"
#elif benchmark_gemv_v3
#include "gemv_v3.h"
#elif benchmark_gemm_medium
#include "gemm_medium.h"
#elif benchmark_gemm_small
#include "gemm_small.h"
#elif benchmark_gemm_large
#include "gemm_large.h"
#elif benchmark_convolution
#include "convolution.h"
#elif benchmark_histogram
#include "histogram.h"
#elif benchmark_filter_by_key
#include "filter_by_key.h"
#elif benchmark_radix_sort
#include "radix_sort.h"
#endif

#define LOG2VLEN 7
#define VLEN (1 << LOG2VLEN)

#define O_CREAT_WRONLY_TRUNC (O_CREAT | O_WRONLY | O_TRUNC)

#define NUM_ITERATIONS 1
#define WARMUP 0

// #define IMG_8BIT

// Macro to stringify an argument
#define STRINGIFY(x) #x


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


    pimCreateDeviceFromConfig(PIM_FUNCTIONAL, argv[1]); // Replace by Macro preprocessing

    printf("DEVICE CREATED!!\n");

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

#if benchmark_axpy
    printf("Testing With AXPY!\n");
    int simple_width = 65536;
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
            int error = axpy(input_buf_1, input_buf_2, output_buf);
            if (error != 0) {
            printf("axpy pipeline failed: %d\n", error);
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

#if benchmark_filter_by_key
    printf("Testing With filter_by_key!\n");
    int simple_width = 524288;
    int simple_height = 1;

    halide_dimension_t x_dim{0, simple_width, 1};
    halide_dimension_t shape[1] = {x_dim};

    int16_t *simple_input_1 =
        (int16_t *)malloc(simple_width * simple_height * sizeof(int16_t));

    for (int i = 0; i < simple_width * simple_height; i++) {
        simple_input_1[i] = i;
    }

    int16_t *simple_output =
        (int16_t *)malloc(simple_width * simple_height * sizeof(int16_t));

    Halide::Runtime::Buffer<int16_t> input_buf_1(simple_input_1, 1, shape);
    Halide::Runtime::Buffer<int16_t> output_buf(simple_output, 1, shape);

    benchmark([&]() {
            int error = filter_by_key(input_buf_1, output_buf);
            if (error != 0) {
            printf("filter_by_key pipeline failed: %d\n", error);
            }
            });


    free(simple_input_1);
    free(simple_output);
#endif

#if benchmark_gemv_v1

  int M = 4096;
  int N = 1;
  int K = 4096;

  halide_dimension_t x_dim_A{0, M, 1};
  halide_dimension_t y_dim_A{0, K, M};
  halide_dimension_t shape_A[2] = {x_dim_A, y_dim_A};
  int32_t* matAptr = (int32_t*) malloc(sizeof(int32_t) * M * K);
  Halide::Runtime::Buffer<int32_t> matA((int32_t *)matAptr, 2, shape_A);


  halide_dimension_t x_dim_B{0, K, 1};
  halide_dimension_t y_dim_B{0, N, K};
  halide_dimension_t shape_B[2] = {x_dim_B, y_dim_B};
  int32_t* matBptr = (int32_t*) malloc(sizeof(int32_t) * N * K);
  Halide::Runtime::Buffer<int32_t> matB((int32_t *)matBptr, 2, shape_B);



  halide_dimension_t x_dim_O{0, M, 1};
  halide_dimension_t y_dim_O{0, N, M};
  halide_dimension_t shape_O[2] = {x_dim_O, y_dim_O};
  int32_t* matOptr = (int32_t*) malloc(sizeof(int32_t) * N * M);
  Halide::Runtime::Buffer<int32_t> output_buf((int32_t *)matOptr, 2, shape_O);

   benchmark([&]() {
    printf("Launching bitsimd gemv!\n");
    int error = gemv_v1(matA, matB, output_buf);
    if (error != 0) {
      printf("gemv_v1 pipeline failed: %d\n", error);
    }
  });

  free(matAptr);
  free(matBptr);
  free(matOptr);
#endif


#if benchmark_gemv_v2

  int M = 16384;
  int N = 1;
  int K = 4096;

  halide_dimension_t x_dim_A{0, M, 1};
  halide_dimension_t y_dim_A{0, K, M};
  halide_dimension_t shape_A[2] = {x_dim_A, y_dim_A};
  int32_t* matAptr = (int32_t*) malloc(sizeof(int32_t) * M * K);
  Halide::Runtime::Buffer<int32_t> matA((int32_t *)matAptr, 2, shape_A);


  halide_dimension_t x_dim_B{0, K, 1};
  halide_dimension_t y_dim_B{0, N, K};
  halide_dimension_t shape_B[2] = {x_dim_B, y_dim_B};
  int32_t* matBptr = (int32_t*) malloc(sizeof(int32_t) * N * K);
  Halide::Runtime::Buffer<int32_t> matB((int32_t *)matBptr, 2, shape_B);



  halide_dimension_t x_dim_O{0, M, 1};
  halide_dimension_t y_dim_O{0, N, M};
  halide_dimension_t shape_O[2] = {x_dim_O, y_dim_O};
  int32_t* matOptr = (int32_t*) malloc(sizeof(int32_t) * N * M);
  Halide::Runtime::Buffer<int32_t> output_buf((int32_t *)matOptr, 2, shape_O);

   benchmark([&]() {
    printf("Launching bitsimd gemv!\n");
    int error = gemv_v2(matA, matB, output_buf);
    if (error != 0) {
      printf("gemv_v2 pipeline failed: %d\n", error);
    }
  });

  free(matAptr);
  free(matBptr);
  free(matOptr);
#endif

#if benchmark_gemv_v3

  int M = 8192;
  int N = 1;
  int K = 16384;

  halide_dimension_t x_dim_A{0, M, 1};
  halide_dimension_t y_dim_A{0, K, M};
  halide_dimension_t shape_A[2] = {x_dim_A, y_dim_A};
  int32_t* matAptr = (int32_t*) malloc(sizeof(int32_t) * M * K);
  Halide::Runtime::Buffer<int32_t> matA((int32_t *)matAptr, 2, shape_A);


  halide_dimension_t x_dim_B{0, K, 1};
  halide_dimension_t y_dim_B{0, N, K};
  halide_dimension_t shape_B[2] = {x_dim_B, y_dim_B};
  int32_t* matBptr = (int32_t*) malloc(sizeof(int32_t) * N * K);
  Halide::Runtime::Buffer<int32_t> matB((int32_t *)matBptr, 2, shape_B);



  halide_dimension_t x_dim_O{0, M, 1};
  halide_dimension_t y_dim_O{0, N, M};
  halide_dimension_t shape_O[2] = {x_dim_O, y_dim_O};
  int32_t* matOptr = (int32_t*) malloc(sizeof(int32_t) * N * M);
  Halide::Runtime::Buffer<int32_t> output_buf((int32_t *)matOptr, 2, shape_O);

   benchmark([&]() {
    printf("Launching bitsimd gemv!\n");
    int error = gemv_v3(matA, matB, output_buf);
    if (error != 0) {
      printf("gemv_v3 pipeline failed: %d\n", error);
    }
  });

  free(matAptr);
  free(matBptr);
  free(matOptr);
#endif

#if benchmark_convolution
  printf("\t*** Convolution\n");

  int image_row = 256;
  int image_col = 256;
  int image_depth = 3;


  int filter_row = 3;
  int filter_col = 3;
  int filter_depth = 64;

  int output_row = image_row;
  int output_col = image_col;
  int output_depth = filter_depth;


  int32_t *input_image = (int32_t*) aligned_malloc(
      image_depth * image_row * image_col * sizeof(int32_t) ,
      1 << LOG2VLEN); 

  int32_t *filter = (int32_t*) aligned_malloc(
      filter_row * filter_col * filter_depth * sizeof(int32_t),
      1 << LOG2VLEN); 


  int32_t *conv_output = (int32_t*) aligned_malloc(
      output_row * output_col * output_depth * sizeof(int32_t),
      1 << LOG2VLEN); 

  
  for(int i =0 ; i < image_row; i++){
      for(int j =0; j < image_col; j++){
          int offset = (i * image_col) + j;
          *(input_image + offset) = offset;
      }
  }

  for(int i =0 ; i < filter_row; i++){
      for(int j =0; j < filter_col; j++){
          int offset = (i * filter_col) + j;
          *(filter + offset) = 1;
      }
  }


  halide_dimension_t image_x_dim{0, image_row, 1};
  halide_dimension_t image_y_dim{0, image_col, image_row};
  halide_dimension_t image_channel_dim{0, image_depth, image_row * image_depth};
  halide_dimension_t image_shape[3] = { image_x_dim, image_y_dim, image_channel_dim};

  halide_dimension_t filter_x{0, filter_row, 1};
  halide_dimension_t filter_y{0, filter_col, filter_row};
  halide_dimension_t filter_channel_dim{0, filter_depth, filter_row * filter_col};
  halide_dimension_t filter_shape[3] = {filter_x, filter_y, filter_channel_dim};


  halide_dimension_t output_x{0, output_row, 1};
  halide_dimension_t output_y{0, output_col, output_row};
  halide_dimension_t output_channel_dim{0, filter_depth, output_row * output_col};
  halide_dimension_t output_shape[3] = {output_x, output_y, output_channel_dim};

  Halide::Runtime::Buffer<int32_t> IMG(input_image, 3, image_shape);
  Halide::Runtime::Buffer<int32_t> Filter(filter, 3, filter_shape);
  Halide::Runtime::Buffer<int32_t> Output(conv_output, 3, output_shape);

  benchmark([&]() {
    int error = convolution(IMG, Filter, Output);
    if (error != 0) {
      printf("Convolution pipeline failed: %d\n", error);
    }
  });


  free(input_image);
  free(filter);
  free(conv_output);


#endif

#if benchmark_relu
  printf("Testing With Relu!\n");
  int simple_width = 256 * 256 * 256;
  int simple_height = 1;

  halide_dimension_t x_dim{0, simple_width, 1};
  halide_dimension_t y_dim{0, simple_height, simple_width};
  halide_dimension_t shape[2] = {x_dim, y_dim};

  int32_t *simple_input_1 =
      (int32_t *)malloc(simple_width * simple_height * sizeof(int32_t));

  for (int i = 0; i < simple_width * simple_height; i++) {
    simple_input_1[i] = 2;
  }

  int32_t *simple_output =
      (int32_t *)malloc(simple_width * simple_height * sizeof(int32_t));

  Halide::Runtime::Buffer<int32_t> input_buf_1(simple_input_1, 2, shape);
  Halide::Runtime::Buffer<int32_t> output_buf(simple_output, 2, shape);

  benchmark([&]() {
    int error = relu(input_buf_1,  output_buf);
    if (error != 0) {
      printf("relu pipeline failed: %d\n", error);
    }
  });

  printf("Completed executing relu!\n");

  free(simple_input_1);
  free(simple_output);
#endif

#if benchmark_gemm_small

  int M = 4096;
  int N = 4096;
  int K = 4096;

  halide_dimension_t x_dim_A{0, M, 1};
  halide_dimension_t y_dim_A{0, K, M};
  halide_dimension_t shape_A[2] = {x_dim_A, y_dim_A};
  int32_t* matAptr = (int32_t*) malloc(sizeof(int32_t) * M * K);
  Halide::Runtime::Buffer<int32_t> matA((int32_t *)matAptr, 2, shape_A);


  halide_dimension_t x_dim_B{0, K, 1};
  halide_dimension_t y_dim_B{0, N, K};
  halide_dimension_t shape_B[2] = {x_dim_B, y_dim_B};
  int32_t* matBptr = (int32_t*) malloc(sizeof(int32_t) * N * K);
  Halide::Runtime::Buffer<int32_t> matB((int32_t *)matBptr, 2, shape_B);



  halide_dimension_t x_dim_O{0, M, 1};
  halide_dimension_t y_dim_O{0, N, M};
  halide_dimension_t shape_O[2] = {x_dim_O, y_dim_O};
  int32_t* matOptr = (int32_t*) malloc(sizeof(int32_t) * N * M);
  Halide::Runtime::Buffer<int32_t> output_buf((int32_t *)matOptr, 2, shape_O);

  benchmark([&]() {
    printf("Launching gemm_small!\n");
    int error = gemm_small(matA, matB, output_buf);
    if (error != 0) {
      printf("gemm_small pipeline failed: %d\n", error);
    }
  });

  free(matAptr);
  free(matBptr);
  free(matOptr);
#endif

#if benchmark_gemm_medium

  int M = 8192;
  int N = 4096;
  int K = 16384;

  halide_dimension_t x_dim_A{0, M, 1};
  halide_dimension_t y_dim_A{0, K, M};
  halide_dimension_t shape_A[2] = {x_dim_A, y_dim_A};
  int32_t* matAptr = (int32_t*) malloc(sizeof(int32_t) * M * K);
  Halide::Runtime::Buffer<int32_t> matA((int32_t *)matAptr, 2, shape_A);


  halide_dimension_t x_dim_B{0, K, 1};
  halide_dimension_t y_dim_B{0, N, K};
  halide_dimension_t shape_B[2] = {x_dim_B, y_dim_B};
  int32_t* matBptr = (int32_t*) malloc(sizeof(int32_t) * N * K);
  Halide::Runtime::Buffer<int32_t> matB((int32_t *)matBptr, 2, shape_B);



  halide_dimension_t x_dim_O{0, M, 1};
  halide_dimension_t y_dim_O{0, N, M};
  halide_dimension_t shape_O[2] = {x_dim_O, y_dim_O};
  int32_t* matOptr = (int32_t*) malloc(sizeof(int32_t) * N * M);
  Halide::Runtime::Buffer<int32_t> output_buf((int32_t *)matOptr, 2, shape_O);

  benchmark([&]() {
    printf("Launching gemm_medium\n");
    int error = gemm_medium(matA, matB, output_buf);
    if (error != 0) {
      printf("gemm_medium pipeline failed: %d\n", error);
    }
  });

  free(matAptr);
  free(matBptr);
  free(matOptr);
#endif

#if benchmark_gemm_large

  int M = 16384;
  int N = 4096;
  int K = 4096;

  halide_dimension_t x_dim_A{0, M, 1};
  halide_dimension_t y_dim_A{0, K, M};
  halide_dimension_t shape_A[2] = {x_dim_A, y_dim_A};
  int32_t* matAptr = (int32_t*) malloc(sizeof(int32_t) * M * K);
  Halide::Runtime::Buffer<int32_t> matA((int32_t *)matAptr, 2, shape_A);


  halide_dimension_t x_dim_B{0, K, 1};
  halide_dimension_t y_dim_B{0, N, K};
  halide_dimension_t shape_B[2] = {x_dim_B, y_dim_B};
  int32_t* matBptr = (int32_t*) malloc(sizeof(int32_t) * N * K);
  Halide::Runtime::Buffer<int32_t> matB((int32_t *)matBptr, 2, shape_B);



  halide_dimension_t x_dim_O{0, M, 1};
  halide_dimension_t y_dim_O{0, N, M};
  halide_dimension_t shape_O[2] = {x_dim_O, y_dim_O};
  int32_t* matOptr = (int32_t*) malloc(sizeof(int32_t) * N * M);
  Halide::Runtime::Buffer<int32_t> output_buf((int32_t *)matOptr, 2, shape_O);

  benchmark([&]() {
    printf("Launching gemm_large!\n");
    int error = gemm_large(matA, matB, output_buf);
    if (error != 0) {
      printf("gemm_large pipeline failed: %d\n", error);
    }
  });

  free(matAptr);
  free(matBptr);
  free(matOptr);
#endif

#if benchmark_histogram
  int width = 8192;
  int height = 34;
  printf("\t*** Histogram\n");

#ifdef IMG_8BIT
  int8_t *input_image = (int8_t*) aligned_malloc(
      width * height * sizeof(int8_t) * 3,
      1 << LOG2VLEN); 
#else

  int32_t *input_image = (int32_t*) aligned_malloc(
      width * height * sizeof(int32_t) * 3,
      1 << LOG2VLEN); 
#endif

  int32_t *bins = (int32_t*) aligned_malloc(
      256 * sizeof(int32_t) * 3,
      1 << LOG2VLEN); 

  assert(input_image && "Unable to allocate input image");
  assert(bins && "Unable to allocate bins");

#ifndef IMG_8BIT
  // Initialize image
  for(int c = 0; c < 3; c++){
      int32_t* channel_offset = input_image + (c * height * width);
      int32_t value = 0;
      switch(c){
          case 0:
              value = 0;
              break;
          case 1:
              value = 1;
              break;
          case 3:
              value = 2;
              break;

      };
      for(int w = 0; w < width; w++){
          for(int h = 0; h < height; h++){
              value = (value + 2) % 256;
              int32_t* pixel_offset = channel_offset + (h * width) + w;
              *pixel_offset = value;
          }
      }
  }
#endif


  halide_dimension_t x_dim{0, width, 1};
  halide_dimension_t y_dim{0, height, width};
  halide_dimension_t channel_dim{0, 3, height * width};
  halide_dimension_t shape[3] = { x_dim, y_dim, channel_dim};

  halide_dimension_t x_bin_dim{0, 256, 1};
  halide_dimension_t y_bin_dim{0, 3, 256};
  halide_dimension_t bin_shape[2] = {x_bin_dim, y_bin_dim};


#ifdef IMG_8BIT
  Halide::Runtime::Buffer<int8_t> IMG(input_image, 3, shape);
#else
  Halide::Runtime::Buffer<int32_t> IMG(input_image, 3, shape);
#endif
  Halide::Runtime::Buffer<int32_t> Bins(bins, 2, bin_shape);

  benchmark([&]() {
    int error = histogram(IMG, Bins);
    if (error != 0) {
      printf("histogram pipeline failed: %d\n", error);
    }
  });

  printf("Red Bins\n");
  for(int i =0; i < 8; i ++){
      printf("[%d]:\t%d\n", i, Bins(i, 0));
  }

  printf("Blue Bins\n");
  for(int i =0; i < 8; i ++){
      printf("[%d]:\t%d\n", i, Bins(i, 1));
  }

  printf("Green Bins\n");
  for(int i =0; i < 8; i ++){
      printf("[%d]:\t%d\n", i, Bins(i, 2));
  }

  free(input_image);
  free(bins);

#endif

#if benchmark_radix_sort
  printf("Testing With Radix_Sort!\n");
  int simple_width = 262144;

  halide_dimension_t x_dim{0, simple_width, 1};
  halide_dimension_t shape[1] = {x_dim};

  int32_t *simple_input_1 =
      (int32_t *)malloc(simple_width  * sizeof(int32_t));


  int32_t *simple_output =
      (int32_t *)malloc(simple_width  * sizeof(int32_t));

  for (int i = 0; i < simple_width ; i++) {
    simple_input_1[i] = simple_width - i;
    simple_output[i] = -1;
  }

  Halide::Runtime::Buffer<int32_t> input_buf_1(simple_input_1, 1, shape);

  Halide::Runtime::Buffer<int32_t> output_buf(simple_output, 1, shape);

  benchmark([&]() {
    int error = radix_sort(input_buf_1, output_buf);
    if (error != 0) {
      printf("radix_sort pipeline failed: %d\n", error);
      exit(-1);
    }
  });

  printf("Completed executing radix_sort!\n");



  free(simple_input_1);
  free(simple_output);
#endif

    printf("Success!\n");
    pimShowStats();

    return 0;
}
