HALIDE_DISTRIB ?= /home/arnoor2/MISAAL/frontends/halide/distrib/
HALIDE_DIR ?=/home/arnoor2/MISAAL/frontends/halide/distrib/
LLVM_ROOT ?= $(LLVM_DIS_ROOT)

benchmarks = tensor_add \
			 bitsimd_gemv \
			 bitsimd_matmul \
			 histogram \
			 relu \
			 filter_by_key \
			 convolution \
			 max_pool \
			 radix_sort

bin_dirs = $(addsuffix /bin,$(benchmarks))

hannk = hannk/common_halide.cpp

ENABLE_HYDRIDE ?= 1
EXPR_DEPTH ?=2
SYNTH_BITWIDTH ?= 16 

BENCHMARK ?=1

CC=g++#clang
#TARGET=host-x86-64 #host-noos-no_bounds_query-no_asserts
TARGET=host-x86-64-no_bounds_query-no_asserts #host-noos-no_bounds_query-no_asserts
STARTING_HASH_FLAG= #HYDRIDE_INITIAL_HASH=x86_hash

#STARTING_HASH ?= "hash_v3" #"empty_hash" 

STARTING_HASH ?= "empty_hash" 


.PHONY: clean all $(benchmarks)

all: $(benchmarks)

$(benchmarks): %: %/bin
# 	Compile the generator
	g++ --std=c++17 -fno-rtti -O3 -DLOG2VLEN=7 \
		-I $(HALIDE_DISTRIB)/include -I $(HALIDE_DISTRIB)/tools \
		-g $@/src/$@_generator.cpp $(HALIDE_DISTRIB)/tools/GenGen.cpp \
		$(hannk) \
		-o $@/bin/$@_generator \
		-L $(HALIDE_DISTRIB)/lib -lHalide $(shell $(LLVM_ROOT)/bin/llvm-config --system-libs --link-static)

# 	Use the generator (to get a manual schedule which is the default)
#
	 export LD_LIBRARY_PATH=$(HALIDE_DIR)/lib;HL_EXPR_DEPTH=$(EXPR_DEPTH) $(STARTING_HASH_FLAG) HYDRIDE_BENCHMARK=$@_x86_depth$(EXPR_DEPTH)_misaal  HL_ENABLE_MISAAL=$(ENABLE_HYDRIDE)  HL_ENABLE_HYDRIDE=$(ENABLE_HYDRIDE) HL_SYNTH_BW=$(SYNTH_BITWIDTH) HYDRIDE_INITIAL_HASH=$(STARTING_HASH) MISAAL_DISABLE_FRONTEND_PATTERNS=1 ./$@/bin/$@_generator \
		-t 0 \
		-o $@/bin \
		-g $@ \
		-e cpp,h,stmt \
		-f $@ target=$(TARGET)
	export LD_LIBRARY_PATH=$(HALIDE_DIR)/lib;HL_EXPR_DEPTH=$(EXPR_DEPTH) HL_ENABLE_HYDRIDE=0 HL_DEBUG_CODEGEN=1  HL_SYNTH_BW=$(SYNTH_BITWIDTH) MISAAL_DISABLE_FRONTEND_PATTERNS=1 ./$@/bin/$@_generator \
		-r halide_runtime_x86 \
		-o $@/bin \
		-e object,c_header \
		target=$(TARGET)
ifeq ($(ENABLE_HYDRIDE),1)
	python3 inline.py $@
endif

	$(CC) -DHALIDE_CPP_ALWAYS_USE_CPP_VECTORS -DFUSED -Dbenchmark_$@ --std=c++17 \
		-O0 -march=native -mavx512vl -mavx512ifma \
		-I $(HALIDE_DISTRIB)/include -I ./$@/bin -I ./libpimsim/ \
		-lstdc++ -ldl -pthread \
		test/run.cpp \
		test/stubs.cpp \
		$@/bin/$@.halide_generated.cpp \
		-L ./libpimsim/ \
		-lpimeval \
		$@/bin/halide_runtime_x86.o \
		-o $@/bin/$@_run.out
	
ifeq ($(BENCHMARK),1) 

# Benchmark the generated binary
	$@/bin/$@_run.out 

endif

#-lpng -lpthread -ldl -ljpeg 
	


# Make the bin dirs if needed
$(bin_dirs): %:
	mkdir $@

clean:
	rm -rf $(bin_dirs)
	rm -rf halide_expr_*
	rm -rf /tmp/hydride_exprs.rkt
	rm -rf /tmp/base_*
	rm -rf /tmp/hydride_hash*
	rm -rf /tmp/hydride.node*
	rm -rf ./*misaal.py ./*.egg ./*.txt ./*.rkt ./test.out ./egg*
	rm -rf ./pim_fused_lowering.h

