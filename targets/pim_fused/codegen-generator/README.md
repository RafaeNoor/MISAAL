# PIM CISC ISA Enumerator

This directory consists of the `PIM-AutoDSE` utilities for enumerating CISC ISA for PIM with formal semantics using ISA building blocks.  Note we use the term fusion here to refer to the process of generating a CISC ISA from RISC (i.e. simplier) ISA building blocks.

[Ops.py](./FusedOpGen/Ops.py) describes the primitive building blocks of the ISA to combine when constructing more complex CISC ISAs. Primitives include element-wise addition, truncate, conditional select, broadcasts, etc.

[Enumerator.py](./FusedOpGen/Enumerator.py) performs the actual enumeration for stitching together primitive ISA blocks. Users provide the required element-bitwidths and vector size combinations to generate the ISA from. Note that the methodology in `PIM-AutoDSE` uses formal methods techniques developed in `MISAAL` to abstract properties of these ISA into a parameterized target agnostic IR. This means that the generated compiler is vector size agnostic (hence we don't need to explicitly enumerate the entire desired vector sizes). 

Using a [TOMLEmitter.py](./FusedOpGen/TOMLEmitter.py), we emit a toml entry with the pseudocode for the generated ISA combinations:
```toml
[test_enum_2.comb_16_fused_pim_op_70]
name = "comb_16_fused_pim_op_70"
operand_sizes = [512, 8, 512, 512]
operand_layouts = ['DRAM_VERT', 'DRAM_VERT', 'DRAM_VERT', 'DRAM_VERT']
operand_elem_bw = [8, 8, 8, 8]
result_layout = "DRAM_VERT"
result_size = 64
result_elem_bw = 1
signedness = 1
semantics = """\
DEFINE comb_16_fused_pim_op_70(a, b, c, d):
FOR idx IN RANGE(0, 64, 1):
var_0_low = idx * 8
var_1_low = 0 * 8
var_2 = a[var_0_low+7:var_0_low] >> b[var_1_low+7:var_1_low]
var_3_low = idx * 8
var_4_low = idx * 8
var_5 = c[var_3_low+7:var_3_low] - d[var_4_low+7:var_4_low]
var_6_low = idx * 1
dst[var_6_low+0:var_6_low] = (var_2 < var_5) ? 1 : 0
ENDFOR
"""
```
These files contain thousands of instructions with _similar_ but not **equivalent** semantics. `PIM-AutoDSE` later folds these similar operations into an abstracted AutoLLVM IR representation.

In addition to these pseudocode descriptions to generate the compiler artifacts with semantics, we also emit two C++ files to interface with the `PIM-AutoDSE` simulator. 

The [fused_lower.h](./dse/fused_lower.h) files generate the interface instructing the simulator to model this ISA operation with optimizations afforded by fusing the ISA micro-ops.
```c++
/*
(comb_16_fused_pim_op_70
	(LoopOp
		(LTOp
			(RightShiftOp
				(a 8 512)
 				(b 8 8)
     )
 			(SubOp
				(c 8 512)
 				(d 8 512)
)
)
)
 )
*/
void comb_16_fused_pim_op_70(void* reg_0, int64_t reg_0_num_elems, int64_t reg_1, int64_t reg_1_num_elems, void* reg_2, int64_t reg_2_num_elems, void* reg_3, int64_t reg_3_num_elems, void* ret_vec, int64_t ret_vec_num_elems){

	PimProg prog;
	// Emitting Allocations
	PimObjId fuse_root = pimAlloc(PIM_ALLOC_AUTO, reg_0_num_elems, PIM_INT8);
	PimObjId fuse_expr_0 = pimAllocAssociated(fuse_root, PIM_BOOL);
	PimObjId fuse_expr_2 = pimAllocAssociated(fuse_root, PIM_INT8);
	// Scalar operand fuse_expr_3 does not need pim allocation
	auto fuse_expr_3 = reg_1;
	PimObjId fuse_expr_4 = pimAllocAssociated(fuse_root, PIM_INT8);
	PimObjId fuse_expr_5 = pimAllocAssociated(fuse_root, PIM_INT8);
	PimObjId fuse_expr_6 = pimAllocAssociated(fuse_root, PIM_INT8);
	// Emitting Copy Host to Device
	prog.add(pimCopyHostToDevice,(void*)reg_0, fuse_expr_2, 0UL, 0UL);
	// No need to copy scalar value reg_1 to PIM memory
	prog.add(pimCopyHostToDevice,(void*)reg_2, fuse_expr_5, 0UL, 0UL);
	prog.add(pimCopyHostToDevice,(void*)reg_3, fuse_expr_6, 0UL, 0UL);
	// Creating PIM Fused Program
	prog.add(pimSub,fuse_expr_5, fuse_expr_6 , fuse_expr_4);
	prog.add(pimShiftBitsRight, fuse_expr_2, fuse_root , (unsigned) fuse_expr_3);
	prog.add(pimLT,fuse_root, fuse_expr_4 , fuse_expr_0);
	// Emitting Copy Device to Host
	prog.add(pimCopyDeviceToHost,fuse_expr_0,(void*)ret_vec, 0UL, 0UL);
	pimFuse(prog);
	// Emitting Deallocations
	pimFree(fuse_expr_0);
	pimFree(fuse_root);
	pimFree(fuse_expr_2);
	// Scalar operand fuse_expr_3 does not need pim deallocation
	pimFree(fuse_expr_4);
	pimFree(fuse_expr_5);
	pimFree(fuse_expr_6);
}
void benchmark_comb_16_fused_pim_op_70(){
printf("Benchmarking comb_16_fused_pim_op_70\n");
pimResetStats();
if(VF == 0){
int8_t arg_0[64];
int8_t arg_1;
int8_t arg_2[64];
int8_t arg_3[64];
int8_t ret_val[64];
comb_16_fused_pim_op_70(arg_0, 64, arg_1, 1, arg_2, 64, arg_3, 64, ret_val, 64);

} else {
 int8_t* arg_0 = new int8_t[VF];
int8_t arg_1;
int8_t* arg_2 = new int8_t[VF];
int8_t* arg_3 = new int8_t[VF];
int8_t* ret_val = new int8_t[VF];
comb_16_fused_pim_op_70(arg_0, VF, arg_1, VF, arg_2, VF, arg_3, VF, ret_val, VF);
delete[] arg_0;
delete[] arg_2;
delete[] arg_3;
delete[] ret_val;

};
pimShowStats();
}
```

Similarly, we generate an interface with unfused i.e. without optimizations in [unfused_lower.h](./dse/unfused_lower.h) to enable measuring the difference in performance and energy due to fusion optimizations.

To generate a performance & energy cost model to instruct the compiler to generate desired optimized code, [GenPimFusedCost](./perf_cost_model/GenPimFusedCost.py) creates the required harness to configure the PIM simulator, invokes each of the CISC ISA with fusion enabled and disabled, then records the collected metrics into a `.csv` file.

 [DRAM_PseudoCode_Parser.py](./Parser/DRAM_PseudoCode_Parser.py) defines a parser which parses the pseudocode of the constructed PIM CISC ISA into a formal semantics. These formal semantics are used to automatically identify similar semantics using [DRAMSimilarityChecker.py](./Parser/DRAMSimilarityChecker.py) which in terms creates an abstracted AutoLLVM IR. The resultant IR are shown in [semantics.py](./Parser/semantics.py).

Design Space exploration is performed using the Simulator config files in [cfg_files](./dse/cfg_files/). An example configuration is shown as:
```
num_ranks = 20
num_bank_per_rank = 128
num_subarray_per_bank = 32
num_row_per_subarray = 1024
num_col_per_subarray = 8192
simulation_target = PIM_DEVICE_BANK_LEVEL
memory_config_file = ../../../configs/asplos/DDR4_8Gb_x8_3200.ini
```


```
[dram_structure]
protocol = DDR4
bankgroups = 4
banks_per_group = 4
rows = 65536
columns = 1024
device_width = 8
BL = 8

[timing]
tCK = 0.83
AL = 0
CL = 17
CWL = 16
tRCD = 17
tRP = 17
tRAS = 52
tRFC = 560
tRFC2 = 416
tRFC4 = 256
tREFI = 12480
tRPRE = 1
tWPRE = 1
tRRD_S = 4
tRRD_L = 8
tWTR_S = 4
tWTR_L = 12
tFAW = 34
tWR = 24
tWR2 = 25
tRTP = 12
tCCD_S = 3
tCCD_L = 6
tCKE = 8
tCKESR = 9
tXS = 576
tXP = 10
tRTRS = 1

[power]
VDD = 1.2
IDD0 = 57
IPP0 = 3.0
IDD2P = 25
IDD2N = 37
IDD3P = 43
IDD3N = 52
IDD4W = 150
IDD4R = 168
IDD5AB = 250
IDD6x = 30

[system]
channel_size = 16384
channels = 1
bus_width = 64
address_mapping = rochrababgco
queue_structure = PER_BANK
refresh_policy = RANK_LEVEL_STAGGERED
row_buf_policy = OPEN_PAGE
cmd_queue_size = 8
trans_queue_size = 32

[other]
epoch_period = 1587301
output_level = 1
```

The compiler sweeps across these config files and collects the performance, energy and targeted CISC ISA across different PIM configurations across benchmarks. The results can then be summarized using [process_dse_insts.py](./dse/process_dse_insts.py) (for processing instruction distributions) and [process_dse.py](./dse/process_dse.py) for other metrics.

