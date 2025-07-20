// Automatically generated file
#include "libpimeval.h"
#include <cstdio>



/*
(comb_2_fused_pim_op_7
	(LoopOp
		(AddOp
			(a 16 64)
 			(b 16 64)
)
)
 )
*/
#if 1
void comb_2_fused_pim_op_7(void* reg_0, int64_t reg_0_num_elems, void* reg_1, int64_t reg_1_num_elems, void* ret_vec, int64_t ret_vec_num_elems){

	PimProg prog;
	// Emitting Allocations
	PimObjId fuse_root = pimAlloc(PIM_ALLOC_AUTO, ret_vec_num_elems, PIM_INT16);
	PimObjId fuse_expr_0 = pimAllocAssociated(fuse_root, PIM_INT16);
	PimObjId fuse_expr_1 = pimAllocAssociated(fuse_root, PIM_INT16);
	// Emitting Copy Host to Device
	prog.add(pimCopyHostToDevice,(void*)reg_0, fuse_expr_0, 0UL, 0UL);
	prog.add(pimCopyHostToDevice,(void*)reg_1, fuse_expr_1, 0UL, 0UL);
	// Creating PIM Fused Program
	prog.add(pimAdd,fuse_expr_0, fuse_expr_1 , fuse_root);
	// Emitting Copy Device to Host
	prog.add(pimCopyDeviceToHost,fuse_root,(void*)ret_vec, 0UL, 0UL);
	pimFuse(prog);
	// Emitting Deallocations
	pimFree(fuse_root);
	pimFree(fuse_expr_0);
	pimFree(fuse_expr_1);
}

#else

void comb_2_fused_pim_op_7(void* reg_0, int64_t reg_0_num_elems, void* reg_1, int64_t reg_1_num_elems, void* ret_vec, int64_t ret_vec_num_elems){

	// Emitting Allocations
	PimObjId fuse_root = pimAlloc(PIM_ALLOC_AUTO, ret_vec_num_elems, PIM_INT16);
	PimObjId fuse_expr_0 = pimAllocAssociated(fuse_root, PIM_INT16);
	PimObjId fuse_expr_1 = pimAllocAssociated(fuse_root, PIM_INT16);
	// Emitting Copy Host to Device
	pimCopyHostToDevice((void*)reg_0, fuse_expr_0, 0UL, 0UL);
	pimCopyHostToDevice((void*)reg_1, fuse_expr_1, 0UL, 0UL);
	// Creating PIM Fused Program
	pimAdd(fuse_expr_0, fuse_expr_1 , fuse_root);
	// Emitting Copy Device to Host
	pimCopyDeviceToHost(fuse_root,(void*)ret_vec, 0UL, 0UL);
	// Emitting Deallocations
	pimFree(fuse_root);
	pimFree(fuse_expr_0);
	pimFree(fuse_expr_1);
}
#endif
