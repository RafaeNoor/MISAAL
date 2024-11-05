#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>

#include "hexagon_standalone.h"
#include <hexagon_sim_timer.h>

#include "HalideBuffer.h"

#if tensor_add
  #include "tensor_add_hvx128.h"
#elif tensor_mul
  #include "tensor_mul_hvx128.h"
#elif max_pool
  #include "max_pool_hvx128.h"
#elif median3x3
  #include "median3x3_hvx128.h"
#elif sobel3x3
  #include "sobel3x3_hvx128.h"
#elif dilate3x3
  #include "dilate3x3_hvx128.h"
#elif dilate5x5
  #include "dilate5x5_hvx128.h"
#elif dilate7x7
  #include "dilate7x7_hvx128.h"
#elif blur3x3
  #include "blur3x3_hvx128.h"
#elif blur5x5
  #include "blur5x5_hvx128.h"
#elif blur7x7
  #include "blur7x7_hvx128.h"
#elif average_pool
  #include "average_pool_hvx128.h"
#elif batched_matmul_256_32bit
#include "batched_matmul_256_32bit_hvx128.h"
#elif max_pool_add
  #include "max_pool_add_hvx128.h"
#elif average_pool_add
  #include "average_pool_add_hvx128.h"
#endif

#define LOG2VLEN 7
#define VLEN (1<<LOG2VLEN)

#define O_CREAT_WRONLY_TRUNC (O_CREAT | O_WRONLY | O_TRUNC)

extern "C" {
ssize_t      write(int, const void *, size_t);
}

int write_file(int fp, unsigned char *src, int height, int width, int border_width) {
  int i;
  for(i = 0; i < height; i++) {
    if(write(fp, &src[i*width], sizeof(unsigned char)*(width))!=(width)) {
      return 1;
    }
  }
  return 0;
}

template<typename F>
long long benchmark(F op) {
  long long start_time = q6sim_read_pcycles();

  op();

  long long total_cycles = q6sim_read_pcycles() - start_time;
  return total_cycles;
}

// This is a basic implementation of the Halide runtime for Hexagon.
void halide_print(void *user_context, const char *str) {
    if (str) {
        //log_printf("%s", str);
    }
}

void halide_error(void *user_context, const char *str) {
    if (!str) {
        //log_printf("Unknown error\n");
    } else if (*str == '\0' || str[strlen(str) - 1] != '\n') {
        //log_printf("Error: %s\n", str);
    } else {
        //log_printf("Error: %s", str);
    }
}

int main(int argc, char **argv) {
  int i, in_fp;
  
  constexpr int dims = 2;

  /* -----------------------------------------------------*/
  /*  Get input parameters                                */
  /* -----------------------------------------------------*/
  if (argc != 3) {
    printf("usage: %s <width> <height> \n", argv[0]);
    return 1;
  }

  int width  = atoi(argv[1]);
  int height = atoi(argv[2]);
  int stride = (width + (VLEN) - 1)&(-(VLEN));

unsigned char *input  = (unsigned char *)memalign(1 << LOG2VLEN, width*height*sizeof(unsigned char));
unsigned char *output = (unsigned char *)memalign(1 << LOG2VLEN, width*height*4*sizeof(unsigned char));

  /* -----------------------------------------------------*/
  /*  Run benchmark on the Simulator                      */
  /* -----------------------------------------------------*/
  long long cycles;

  #if tensor_add
    printf("Testing With Tensor Add!\n");
    int simple_width = width ;
    int simple_height = height;
    
    halide_dimension_t x_dim{0, simple_width, 1};
    halide_dimension_t y_dim{0, simple_height, simple_width};
    halide_dimension_t shape[2] = {x_dim, y_dim};


    int8_t* simple_input_1 = (int8_t*)memalign(1 << LOG2VLEN, simple_width * simple_height * sizeof(int8_t));
    int8_t* simple_input_2 = (int8_t*)memalign(1 << LOG2VLEN, simple_width * simple_height * sizeof(int8_t));

    for(int i =0; i < simple_width * simple_height;i++){
        simple_input_1[i] = 1;
        simple_input_2[i] = 2;
    }

    int8_t* simple_output = (int8_t*)memalign(1 << LOG2VLEN, simple_width * simple_height * sizeof(int8_t));

    Halide::Runtime::Buffer<int8_t> input_buf_1(simple_input_1, dims, shape);
    Halide::Runtime::Buffer<int8_t> input_buf_2(simple_input_2, dims, shape);
    Halide::Runtime::Buffer<int8_t> output_buf(simple_output, dims, shape);

    // Run in 128 byte mode
    SIM_ACQUIRE_HVX;
    SIM_SET_HVX_DOUBLE_MODE;
    cycles = benchmark([&]() {
        int error = tensor_add_hvx128(input_buf_1, input_buf_2, output_buf);
        if (error != 0) {
          printf("tensor_add_hvx128 pipeline failed: %d\n", error);
        }
      });
    SIM_RELEASE_HVX;

    for (int x=0; x<10; x++)
      for (int y=0; y<10; y++)
        printf("(x: %d, y: %d) ==> input-vals: %d  %d output-val: %d\n", x, y, input_buf_1(x, y), input_buf_2(x, y), output_buf(x, y));

    printf("AppReported (HVX128B-mode): Image %dx%d - simple(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles/(width*height));

  free(simple_input_1);
  free(simple_input_2);
  free(simple_output);
  #endif

  #if tensor_mul
    printf("Testing With Tensor Mul!\n");
    int simple_width = width ;
    int simple_height = height;
    
    halide_dimension_t x_dim{0, simple_width, 1};
    halide_dimension_t y_dim{0, simple_height, simple_width};
    halide_dimension_t shape[2] = {x_dim, y_dim};


    int8_t* simple_input_1 = (int8_t*)memalign(1 << LOG2VLEN, simple_width * simple_height * sizeof(int8_t));
    int8_t* simple_input_2 = (int8_t*)memalign(1 << LOG2VLEN, simple_width * simple_height * sizeof(int8_t));

    for(int i =0; i < simple_width * simple_height;i++){
        simple_input_1[i] = 1;
        simple_input_2[i] = 2;
    }

    int16_t* simple_output = (int16_t*)memalign(1 << LOG2VLEN, simple_width * simple_height * sizeof(int16_t));

    Halide::Runtime::Buffer<int8_t> input_buf_1(simple_input_1, dims, shape);
    Halide::Runtime::Buffer<int8_t> input_buf_2(simple_input_2, dims, shape);
    Halide::Runtime::Buffer<int16_t> output_buf(simple_output, dims, shape);

    // Run in 128 byte mode
    SIM_ACQUIRE_HVX;
    SIM_SET_HVX_DOUBLE_MODE;
    cycles = benchmark([&]() {
        int error = tensor_mul_hvx128(input_buf_1, input_buf_2, output_buf);
        if (error != 0) {
          printf("tensor_mul_hvx128 pipeline failed: %d\n", error);
        }
      });
    SIM_RELEASE_HVX;

    for (int x=0; x<10; x++)
      for (int y=0; y<10; y++)
        printf("(x: %d, y: %d) ==> input-vals: %d  %d output-val: %d\n", x, y, input_buf_1(x, y), input_buf_2(x, y), output_buf(x, y));

    printf("AppReported (HVX128B-mode): Image %dx%d - simple(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles/(width*height));

  free(simple_input_1);
  free(simple_input_2);
  free(simple_output);
  #endif

#if max_pool
      halide_dimension_t c_dim{ 0, 1024, 1 };
      halide_dimension_t x_dim{ 0, width / 32, 128 };
      halide_dimension_t y_dim{ 0, height / 32, 128 * (width / 32) };
      halide_dimension_t b_dim{ 0, 1, 128 * (width / 32) * (height / 32) };
      halide_dimension_t shape[4] = { c_dim, x_dim, y_dim, b_dim };



      Halide::Runtime::Buffer<uint8_t> input_buf(input, 4, shape);
      Halide::Runtime::Buffer<uint8_t> output_buf(output, 4, shape);

      // Run in 128 byte mode
      SIM_ACQUIRE_HVX;
      SIM_SET_HVX_DOUBLE_MODE;
      cycles = benchmark([&]() {
          int error = max_pool_hvx128(input_buf, 2, 2, 8, 8, 5, 225, output_buf);
          if (error != 0) {
              printf("max_pool_hvx128 pipeline failed: %d\n", error);
          }
          });
      SIM_RELEASE_HVX;

      for (int x = 0; x < 10; x++)
          for (int y = 0; y < 10; y++)
              printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y, input_buf(x, y), output_buf(x, y));

      printf("AppReported (HVX128B-mode): Image %dx%d - max_pool(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if median3x3
    halide_dimension_t x_dim{ 0, width, 1 };
    halide_dimension_t y_dim{ 0, height, width };
    halide_dimension_t shape[2] = { x_dim, y_dim };


    Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
    Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

    // Run in 128 byte mode
    SIM_ACQUIRE_HVX;
    SIM_SET_HVX_DOUBLE_MODE;
    cycles = benchmark([&]() {
        int error = median3x3_hvx128(input_buf, output_buf);
        if (error != 0) {
            printf("median3x3_hvx128 pipeline failed: %d\n", error);
        }
        });
    SIM_RELEASE_HVX;

    for (int x = 0; x < 10; x++)
        for (int y = 0; y < 10; y++)
            printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y, input_buf(x, y), output_buf(x, y));

    printf("AppReported (HVX128B-mode): Image %dx%d - median3x3(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / width / height);

#endif



  #if dilate3x3
    halide_dimension_t x_dim{ 0, width, 1 };
    halide_dimension_t y_dim{ 0, height, width };
    halide_dimension_t shape[2] = { x_dim, y_dim };



    Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
    Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

    // Run in 128 byte mode
    SIM_ACQUIRE_HVX;
    SIM_SET_HVX_DOUBLE_MODE;
    cycles = benchmark([&]() {
        int error = dilate3x3_hvx128(input_buf, output_buf);
        if (error != 0) {
            printf("dilate3x3_hvx128 pipeline failed: %d\n", error);
        }
        });
    SIM_RELEASE_HVX;

    for (int x = 0; x < 10; x++)
        for (int y = 0; y < 10; y++)
            printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y, input_buf(x, y), output_buf(x, y));

    printf("AppReported (HVX128B-mode): Image %dx%d - dilate3x3(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / (width * height));

  #endif

  #if dilate5x5
    halide_dimension_t x_dim{ 0, width, 1 };
    halide_dimension_t y_dim{ 0, height, width };
    halide_dimension_t shape[2] = { x_dim, y_dim };

    Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
    Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

    // Run in 128 byte mode
    SIM_ACQUIRE_HVX;
    SIM_SET_HVX_DOUBLE_MODE;
    cycles = benchmark([&]() {
        int error = dilate5x5_hvx128(input_buf, output_buf);
        if (error != 0) {
            printf("dilate5x5_hvx128 pipeline failed: %d\n", error);
        }
        });
    SIM_RELEASE_HVX;

    for (int x = 0; x < 10; x++)
        for (int y = 0; y < 10; y++)
            printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y, input_buf(x, y), output_buf(x, y));

    printf("AppReported (HVX128B-mode): Image %dx%d - dilate5x5(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / (width * height));
  #endif

  #if dilate7x7
    halide_dimension_t x_dim{ 0, width, 1 };
    halide_dimension_t y_dim{ 0, height, width };
    halide_dimension_t shape[2] = { x_dim, y_dim };

    Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
    Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

    // Run in 128 byte mode
    SIM_ACQUIRE_HVX;
    SIM_SET_HVX_DOUBLE_MODE;
    cycles = benchmark([&]() {
        int error = dilate7x7_hvx128(input_buf, output_buf);
        if (error != 0) {
            printf("dilate7x7_hvx128 pipeline failed: %d\n", error);
        }
        });
    SIM_RELEASE_HVX;

    for (int x = 0; x < 10; x++)
        for (int y = 0; y < 10; y++)
            printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y, input_buf(x, y), output_buf(x, y));

    printf("AppReported (HVX128B-mode): Image %dx%d - dilate7x7(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / (width * height));
  #endif

  #if sobel3x3
    halide_dimension_t x_dim{ 0, width, 1 };
    halide_dimension_t y_dim{ 0, height, width };
    halide_dimension_t shape[2] = { x_dim, y_dim };

    Halide::Runtime::Buffer<uint8_t> input_buf(input, dims, shape);
    Halide::Runtime::Buffer<uint8_t> output_buf(output, dims, shape);

    // Run in 128 byte mode
    SIM_ACQUIRE_HVX;
    SIM_SET_HVX_DOUBLE_MODE;
    cycles = benchmark([&]() {
        int error = sobel3x3_hvx128(input_buf, output_buf);
        if (error != 0) {
            printf("sobel3x3_hvx128 pipeline failed: %d\n", error);
        }
        });
    SIM_RELEASE_HVX;

    for (int x = 0; x < 10; x++)
        for (int y = 0; y < 10; y++)
            printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y, input_buf(x, y), output_buf(x, y));

    printf("AppReported (HVX128B-mode): Image %dx%d - sobel3x3(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / (width * height));
  #endif

#if average_pool
      halide_dimension_t c_dim{ 0, 1024, 1 };
      halide_dimension_t x_dim{ 0, width/32, 128 };
      halide_dimension_t y_dim{ 0, height/32, 128 * (width / 32) };
      halide_dimension_t b_dim{ 0, 1, 128 * (width / 32) * (height / 32) };
      halide_dimension_t shape[4] = { c_dim, x_dim, y_dim, b_dim };

      Halide::Runtime::Buffer<uint8_t> input_buf(input, 4, shape);
      Halide::Runtime::Buffer<uint8_t> output_buf(output, 4, shape);

      // Run in 128 byte mode
      SIM_ACQUIRE_HVX;
      SIM_SET_HVX_DOUBLE_MODE;
      cycles = benchmark([&]() {
          int error = average_pool_hvx128(input_buf, 2, 2, 8, 8, 5, 225, output_buf);
          if (error != 0) {
              printf("average_pool_hvx128 pipeline failed: %d\n", error);
          }
          });
      SIM_RELEASE_HVX;

      for (int x = 0; x < 10; x++)
          for (int y = 0; y < 10; y++)
              printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y, input_buf(x, y), output_buf(x, y));

      printf("AppReported (HVX128B-mode): Image %dx%d - average_pool(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if blur3x3
    halide_dimension_t x_dim{ 0, width/2, 1 };
    halide_dimension_t y_dim{ 0, height, width/2 };
    halide_dimension_t shape[2] = { x_dim, y_dim };

    Halide::Runtime::Buffer<int16_t> input_buf((short*)input, dims, shape);
    Halide::Runtime::Buffer<int16_t> output_buf((short*)output, dims, shape);

    // Run in 128 byte mode
    SIM_ACQUIRE_HVX;
    SIM_SET_HVX_DOUBLE_MODE;
    cycles = benchmark([&]() {
        int error = blur3x3_hvx128(input_buf, output_buf);
        if (error != 0) {
            printf("blur3x3_hvx128 pipeline failed: %d\n", error);
        }
        });
    SIM_RELEASE_HVX;

    for (int x = 0; x < 10; x++)
        for (int y = 0; y < 10; y++)
            printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y, input_buf(x, y), output_buf(x, y));

    printf("AppReported (HVX128B-mode): Image %dx%d - blur3x3(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / (width * height));
  #endif


#if blur5x5
    halide_dimension_t x_dim{ 0, width/2, 1 };
    halide_dimension_t y_dim{ 0, height, width/2 };
    halide_dimension_t shape[2] = { x_dim, y_dim };

    Halide::Runtime::Buffer<int16_t> input_buf((short*)input, dims, shape);
    Halide::Runtime::Buffer<int16_t> output_buf((short*)output, dims, shape);

    // Run in 128 byte mode
    SIM_ACQUIRE_HVX;
    SIM_SET_HVX_DOUBLE_MODE;
    cycles = benchmark([&]() {
        int error = blur5x5_hvx128(input_buf, output_buf);
        if (error != 0) {
            printf("blur5x5_hvx128 pipeline failed: %d\n", error);
        }
        });
    SIM_RELEASE_HVX;

    for (int x = 0; x < 10; x++)
        for (int y = 0; y < 10; y++)
            printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y, input_buf(x, y), output_buf(x, y));

    printf("AppReported (HVX128B-mode): Image %dx%d - blur5x5(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / (width * height));
  #endif


#if blur7x7
    halide_dimension_t x_dim{ 0, width/2, 1 };
    halide_dimension_t y_dim{ 0, height, width/2 };
    halide_dimension_t shape[2] = { x_dim, y_dim };

    Halide::Runtime::Buffer<int16_t> input_buf((short*)input, dims, shape);
    Halide::Runtime::Buffer<int16_t> output_buf((short*)output, dims, shape);

    // Run in 128 byte mode
    SIM_ACQUIRE_HVX;
    SIM_SET_HVX_DOUBLE_MODE;
    cycles = benchmark([&]() {
        int error = blur7x7_hvx128(input_buf, output_buf);
        if (error != 0) {
            printf("blur7x7_hvx128 pipeline failed: %d\n", error);
        }
        });
    SIM_RELEASE_HVX;

    for (int x = 0; x < 10; x++)
        for (int y = 0; y < 10; y++)
            printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y, input_buf(x, y), output_buf(x, y));

    printf("AppReported (HVX128B-mode): Image %dx%d - blur7x7(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / (width * height));
  #endif


#if batched_matmul_256_32bit


    constexpr int dims_3 = 3;
    int32_t matrix_size = 256;
    
    int num_batches = 4; 
    halide_dimension_t x_dim{ 0, matrix_size, 1 };
    halide_dimension_t y_dim{ 0, matrix_size, matrix_size * 1 };
    halide_dimension_t b_dim{ 0, num_batches, matrix_size * matrix_size };
    halide_dimension_t shape[3] = { x_dim, y_dim, b_dim};


    printf("Allocating memory!\n");



    int16_t* matATensor = (int16_t*) memalign(1 << LOG2VLEN,matrix_size * matrix_size * num_batches * sizeof(int16_t));
    int16_t* matBTensor = (int16_t*) memalign(1 << LOG2VLEN,matrix_size * matrix_size * num_batches *  sizeof(int16_t));
    int32_t* outputTensor = (int32_t*) memalign(1 << LOG2VLEN,matrix_size * matrix_size * num_batches * sizeof(int32_t));


    printf("Creating runtime buffers!\n");

    Halide::Runtime::Buffer<int16_t> matA((int16_t*)matATensor, dims_3, shape);
    Halide::Runtime::Buffer<int16_t> matB((int16_t*) matBTensor, dims_3, shape);



    Halide::Runtime::Buffer<int32_t> output_buf((int32_t*)outputTensor, dims_3, shape);

    printf("About to launch kernel!\n");

    // Run in 128 byte mode
    SIM_ACQUIRE_HVX;
    SIM_SET_HVX_DOUBLE_MODE;
    cycles = benchmark([&]() {
            int error = batched_matmul_256_32bit_hvx128(matA, matB, output_buf);
            if (error != 0) {
            printf("batched_matmul_256_32bit_hvx128 pipeline failed: %d\n", error);
            }
            });

    SIM_RELEASE_HVX;



    printf("AppReported (): Image %dx%d - batched(): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / (width * height));

#endif



#if average_pool_add
      halide_dimension_t c_dim{ 0, 1024, 1 };
      halide_dimension_t x_dim{ 0, width/32, 128 };
      halide_dimension_t y_dim{ 0, height/32, 128 * (width / 32) };
      halide_dimension_t b_dim{ 0, 1, 128 * (width / 32) * (height / 32) };
      halide_dimension_t shape[4] = { c_dim, x_dim, y_dim, b_dim };

      Halide::Runtime::Buffer<uint8_t> input_buf(input, 4, shape);
      Halide::Runtime::Buffer<uint8_t> output_buf(output, 4, shape);

      // Run in 128 byte mode
      SIM_ACQUIRE_HVX;
      SIM_SET_HVX_DOUBLE_MODE;
      cycles = benchmark([&]() {
          int error = average_pool_add_hvx128(input_buf, input_buf, 2, 2, 8, 8, 5, 225, output_buf);
          if (error != 0) {
              printf("average_pool_add_hvx128 pipeline failed: %d\n", error);
          }
          });
      SIM_RELEASE_HVX;

      for (int x = 0; x < 10; x++)
          for (int y = 0; y < 10; y++)
              printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y, input_buf(x, y), output_buf(x, y));

      printf("AppReported (HVX128B-mode): Image %dx%d - average_pool_add(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif

#if max_pool
      halide_dimension_t c_dim{ 0, 1024, 1 };
      halide_dimension_t x_dim{ 0, width / 32, 128 };
      halide_dimension_t y_dim{ 0, height / 32, 128 * (width / 32) };
      halide_dimension_t b_dim{ 0, 1, 128 * (width / 32) * (height / 32) };
      halide_dimension_t shape[4] = { c_dim, x_dim, y_dim, b_dim };

      Halide::Runtime::Buffer<uint8_t> input_buf(input, 4, shape);
      Halide::Runtime::Buffer<uint8_t> output_buf(output, 4, shape);

      // Run in 128 byte mode
      SIM_ACQUIRE_HVX;
      SIM_SET_HVX_DOUBLE_MODE;
      cycles = benchmark([&]() {
          int error = max_pool_hvx128(input_buf, 2, 2, 8, 8, 5, 225, output_buf);
          if (error != 0) {
              printf("max_pool_hvx128 pipeline failed: %d\n", error);
          }
          });
      SIM_RELEASE_HVX;

      for (int x = 0; x < 10; x++)
          for (int y = 0; y < 10; y++)
              printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y, input_buf(x, y), output_buf(x, y));

      printf("AppReported (HVX128B-mode): Image %dx%d - max_pool(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif


#if max_pool_add
      halide_dimension_t c_dim{ 0, 1024, 1 };
      halide_dimension_t x_dim{ 0, width / 32, 128 };
      halide_dimension_t y_dim{ 0, height / 32, 128 * (width / 32) };
      halide_dimension_t b_dim{ 0, 1, 128 * (width / 32) * (height / 32) };
      halide_dimension_t shape[4] = { c_dim, x_dim, y_dim, b_dim };

      Halide::Runtime::Buffer<uint8_t> input_buf(input, 4, shape);
      Halide::Runtime::Buffer<uint8_t> output_buf(output, 4, shape);

      // Run in 128 byte mode
      SIM_ACQUIRE_HVX;
      SIM_SET_HVX_DOUBLE_MODE;
      cycles = benchmark([&]() {
          int error = max_pool_add_hvx128(input_buf, input_buf, 2, 2, 8, 8, 5, 225, output_buf);
          if (error != 0) {
              printf("max_pool_add_hvx128 pipeline failed: %d\n", error);
          }
          });
      SIM_RELEASE_HVX;

      for (int x = 0; x < 10; x++)
          for (int y = 0; y < 10; y++)
              printf("(x: %d, y: %d) ==> input-val: %d   output-val: %d\n", x, y, input_buf(x, y), output_buf(x, y));

      printf("AppReported (HVX128B-mode): Image %dx%d - max_pool_add(128B): %lld cycles (%0.4f cycles/pixel)\n", (int)width, (int)height, cycles, (float)cycles / (width * height));
#endif


  free(input);
  free(output);



  printf("Success!\n");

  return 0;
}

