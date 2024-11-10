HALIDE_DISTRIB ?= /home/arnoor2/MISAAL/frontends/halide/distrib/
HALIDE_DIR ?=/home/arnoor2/MISAAL/frontends/halide/distrib/
LLVM_ROOT ?= $(LLVM_DIS_ROOT)

benchmarks = matmul_256_32bit_bias_add \
			 matmul_bias_relu_matmul \
			 max_pool \
			 dilate3x3 \
			 dilate5x5 \
			 dilate7x7 \
			 l2norm

bin_dirs = $(addsuffix /bin,$(benchmarks))

hannk = hannk/common_halide.cpp

ENABLE_HYDRIDE ?= 1
EXPR_DEPTH ?=2
SYNTH_BITWIDTH ?= 16 

BENCHMARK ?=1

CC=clang


clean:
	rm -rf $(bin_dirs)
	rm -rf halide_expr_*
	rm -rf /tmp/hydride_exprs.rkt
	rm -rf /tmp/base_*
	rm -rf /tmp/hydride_hash*
	rm -rf /tmp/hydride.node*
	rm -rf ./*.py ./*.egg ./*.txt ./*.rkt ./test.out ./egg*

TARGET=arm-64-osx-no_bounds_query-no_asserts
STARTING_HASH_FLAG=#HYDRIDE_INITIAL_HASH=starting_hash
HALIDE_COMPILE_LLVM?=#HALIDE_COMPILE_LLVM=1
HYDRIDE_DECOMPOSE_LET?=#0
BIN=bin

STARTING_HASH ?= "empty_hash"


.PHONY: clean all $(benchmarks)

all: $(benchmarks)

$(benchmarks): %: %/$(BIN)
# 	Compile the generator
	g++ --std=c++17 -fno-rtti -O3 -DLOG2VLEN=7    \
		-I $(HALIDE_DISTRIB)/include -I $(HALIDE_DISTRIB)/tools \
		-g $@/src/$@_generator.cpp $(HALIDE_DISTRIB)/tools/GenGen.cpp \
		$(hannk) \
		-o $@/$(BIN)/$@_generator \
		-L $(HALIDE_DISTRIB)/lib -lHalide $(shell $(LLVM_CONFIG) --system-libs --link-static) $(ADDITIONAL)

# 	Use the generator (to get a manual schedule which is the default)
#
	export LD_LIBRARY_PATH=$(HALIDE_DISTRIB)/lib; HYDRIDE_BENCHMARK=$@_arm_depth$(EXPR_DEPTH)_misaal HL_ENABLE_MISAAL=$(ENABLE_HYDRIDE)  HL_ENABLE_HYDRIDE=$(ENABLE_HYDRIDE) MISAAL_DISABLE_FRONTEND_PATTERNS=1 HYDRIDE_TARGET=arm HYDRIDE_DISTRIBUTE_LOOK_AHEAD=1   HL_SYNTH_BW=$(SYNTH_BITWIDTH) HYDRIDE_INITIAL_HASH=$(STARTING_HASH) ./$@/$(BIN)/$@_generator \
		-t 0 \
		-o $@/$(BIN) \
		-g $@ \
		-e static_library,stmt,h,llvm_assembly,assembly \
		-f $@ target=$(TARGET)
	export LD_LIBRARY_PATH=$(HALIDE_DIR)/lib; HL_EXPR_DEPTH=$(EXPR_DEPTH) HL_ENABLE_HYDRIDE=0 HL_DEBUG_CODEGEN=1  HL_SYNTH_BW=$(SYNTH_BITWIDTH) MISAAL_DISABLE_FRONTEND_PATTERNS=1 ./$@/$(BIN)/$@_generator \
		-r halide_runtime_x86 \
		-o $@/$(BIN) \
		-e object,c_header \
		target=$(TARGET)
	
	$(CC) -Dbenchmark_$@ --std=c++17 \
		-O0\
		-I $(HALIDE_DISTRIB)/include -I ./$@/$(BIN) \
		-lstdc++ -ldl -pthread \
		test/run.cpp \
		test/stubs.cpp \
		$@/$(BIN)/$@.a \
		$@/$(BIN)/halide_runtime_x86.o \
		-o $@/$(BIN)/$@_run.out

	
ifeq ($(BENCHMARK),1) 

# Benchmark the generated $(BIN)ary
	$@/$(BIN)/$@_run.out 3840 2160 ../test_vectors/football3840x2160.bin $@/out/out.bin
	$@/$(BIN)/$@_run.out 3840 2160 ../test_vectors/football3840x2160.bin $@/out/out.bin
	$@/$(BIN)/$@_run.out 3840 2160 ../test_vectors/football3840x2160.bin $@/out/out.bin
	$@/$(BIN)/$@_run.out 3840 2160 ../test_vectors/football3840x2160.bin $@/out/out.bin

endif

fully_connected: 
	g++ --std=c++17 -fno-rtti -O3 -DLOG2VLEN=7 \
		-I $(HALIDE_DISTRIB)/include -I $(HALIDE_DISTRIB)/tools \
		-g $@/src/$@_generator.cpp $(HALIDE_DISTRIB)/tools/GenGen.cpp \
		$(hannk) \
		-o $@/$(BIN)/$@_generator \
		-L $(HALIDE_DISTRIB)/lib -lHalide $(shell $(LLVM_CONFIG) --system-libs --link-static) $(ADDITIONAL)

	export LD_LIBRARY_PATH=$(HALIDE_DISTRIB)/lib; export HYDRIDE_BENCHMARK=$@_arm_depth$(EXPR_DEPTH)_misaal; time HL_ENABLE_MISAAL=$(ENABLE_HYDRIDE)  HL_ENABLE_HYDRIDE=$(ENABLE_HYDRIDE) MISAAL_DISABLE_FRONTEND_PATTERNS=1 HYDRIDE_TARGET=arm HYDRIDE_DISTRIBUTE_LOOK_AHEAD=1 HL_SYNTH_BW=$(SYNTH_BW) $(STARTING_HASH) ./$@/$(BIN)/$@_generator \
	    -t 0 \
		-o $@/$(BIN) \
		-g $@ output.type=uint8 \
		-e static_library,stmt,h,llvm_assembly,assembly \
		-f $@ target=$(TARGET)
	
	HL_EXPR_DEPTH=$(EXPR_DEPTH) HL_ENABLE_HYDRIDE=0 HL_DEBUG_CODEGEN=1  HL_SYNTH_BW=$(SYNTH_BITWIDTH) MISAAL_DISABLE_FRONTEND_PATTERNS=1 ./$@/$(BIN)/$@_generator \
		-r halide_runtime_x86 \
		-o $@/$(BIN) \
		-e object,c_header \
		target=$(TARGET)
	
	$(CC) -Dbenchmark_$@ --std=c++17 \
		-O0\
		-I $(HALIDE_DISTRIB)/include -I ./$@/$(BIN) \
		-lstdc++ -ldl -pthread \
		test/run.cpp \
		test/stubs.cpp \
		$@/$(BIN)/$@.a \
		$@/$(BIN)/halide_runtime_x86.o \
		-o $@/$(BIN)/$@_run.out

	
ifeq ($(BENCHMARK),1) 

# Benchmark the generated $(BIN)ary
	$@/$(BIN)/$@_run.out 3840 2160 ../test_vectors/football3840x2160.bin $@/out/out.bin
	$@/$(BIN)/$@_run.out 3840 2160 ../test_vectors/football3840x2160.bin $@/out/out.bin
	$@/$(BIN)/$@_run.out 3840 2160 ../test_vectors/football3840x2160.bin $@/out/out.bin
	$@/$(BIN)/$@_run.out 3840 2160 ../test_vectors/football3840x2160.bin $@/out/out.bin

endif

#-lpng -lpthread -ldl -ljpeg 
	
fully_connected/bin_ref fully_connected/bin: %:
	mkdir $@

# Make the bin dirs if needed
$(bin_dirs): %:
	mkdir $@

$(bin_ref_dirs): %:
	mkdir $@
