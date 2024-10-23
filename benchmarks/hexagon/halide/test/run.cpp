#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>

#include "hexagon_standalone.h"
#include <hexagon_sim_timer.h>

#include "HalideBuffer.h"

#if tensor_add
  #include "tensor_add_hvx128.h"
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





  printf("Success!\n");

  return 0;
}

