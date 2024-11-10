{
    " (vmov_n_u16_dsl ; vmovq_n_u32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t32\n\t32\n\t4\n )+128+vmovq_n_u32+typed:xBroadcast_is32_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmov_n_u16_dsl (reg (bv #x00 8)) 128 128 0 128 32)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 4)",
                "output_size": 128,
                "original_src_expr": " (vmov_n_u16_dsl ; vmovq_n_u32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t32\n\t32\n\t4\n )",
                "src_ctx": "vmovq_n_u32",
                "dst_ctx": "typed:xBroadcast_is32_os128_signed_None"
            }
        }
    ],
    " (vmov_n_u16_dsl ; vmovq_n_u32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t32\n\t32\n\t4\n )+64+vmov_n_u16+typed:xBroadcast_is16_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmov_n_u16_dsl (reg (bv #x00 8)) 64 64 0 64 16)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 4)",
                "output_size": 64,
                "original_src_expr": " (vmov_n_u16_dsl ; vmovq_n_u32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t32\n\t32\n\t4\n )",
                "src_ctx": "vmov_n_u16",
                "dst_ctx": "typed:xBroadcast_is16_os64_signed_None"
            }
        }
    ],
    " (vmov_n_u16_dsl ; vmovq_n_u32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t32\n\t32\n\t4\n )+64+vmov_n_u32+typed:xBroadcast_is32_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmov_n_u16_dsl (reg (bv #x00 8)) 64 64 0 64 32)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 32 32 2)",
                "output_size": 64,
                "original_src_expr": " (vmov_n_u16_dsl ; vmovq_n_u32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t32\n\t32\n\t4\n )",
                "src_ctx": "vmov_n_u32",
                "dst_ctx": "typed:xBroadcast_is32_os64_signed_None"
            }
        }
    ],
    " (vmov_n_u16_dsl ; vmovq_n_u32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t32\n\t32\n\t4\n )+64+vmov_n_u8+typed:xBroadcast_is8_os64_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmov_n_u16_dsl (reg (bv #x00 8)) 64 64 0 64 8)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 8)",
                "output_size": 64,
                "original_src_expr": " (vmov_n_u16_dsl ; vmovq_n_u32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t32\n\t32\n\t4\n )",
                "src_ctx": "vmov_n_u8",
                "dst_ctx": "typed:xBroadcast_is8_os64_signed_None"
            }
        }
    ],
    " (vmov_n_u16_dsl ; vmovq_n_u32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t32\n\t32\n\t4\n )+128+vmovq_n_s8+typed:xBroadcast_is8_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmov_n_u16_dsl (reg (bv #x00 8)) 128 128 0 128 8)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 8 8 16)",
                "output_size": 128,
                "original_src_expr": " (vmov_n_u16_dsl ; vmovq_n_u32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t32\n\t32\n\t4\n )",
                "src_ctx": "vmovq_n_s8",
                "dst_ctx": "typed:xBroadcast_is8_os128_signed_None"
            }
        }
    ],
    " (vmov_n_u16_dsl ; vmovq_n_u32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n )+ (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t32\n\t32\n\t4\n )+128+vmovq_n_s16+typed:xBroadcast_is16_os128_signed_None": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmov_n_u16_dsl (reg (bv #x00 8)) 128 128 0 128 16)",
                "dst": "(typed:xBroadcast (reg (bv #x00 8)) 16 16 8)",
                "output_size": 128,
                "original_src_expr": " (vmov_n_u16_dsl ; vmovq_n_u32\n\t(reg (bv 0 (bitvector 8))) ; < 4 x i8> False\n\t128\n\t128\n\t0\n\t128\n\t32\n )",
                "original_dst_expr": " (typed:xBroadcast ; typed:xBroadcast_is32_os128_signed_None\n\t(buffer-index  0 'uint8 32) ; < 4 x i8> False\n\t32\n\t32\n\t4\n )",
                "src_ctx": "vmovq_n_s16",
                "dst_ctx": "typed:xBroadcast_is16_os128_signed_None"
            }
        }
    ],
    " (vmovn_s16_dsl ; vmovn_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t2\n )+ (typed:cast-int-truncate ; typed:cast-int_1_ip64_is128_op32_os64_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t64\n\t1\n\t2\n\t32\n )+64+vmovn_s16+typed:cast-int_1_ip16_is128_op8_os64_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmovn_s16_dsl (reg (bv #x00 8)) 64 64 0 64 8 2)",
                "dst": "(typed:cast-int-truncate (reg (bv #x00 8)) 16 1 8 8)",
                "output_size": 64,
                "original_src_expr": " (vmovn_s16_dsl ; vmovn_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t2\n )",
                "original_dst_expr": " (typed:cast-int-truncate ; typed:cast-int_1_ip64_is128_op32_os64_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t64\n\t1\n\t2\n\t32\n )",
                "src_ctx": "vmovn_s16",
                "dst_ctx": "typed:cast-int_1_ip16_is128_op8_os64_signed_1"
            }
        }
    ],
    " (vmovn_s16_dsl ; vmovn_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t2\n )+ (typed:cast-int-truncate ; typed:cast-int_1_ip64_is128_op32_os64_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t64\n\t1\n\t2\n\t32\n )+64+vmovn_u32+typed:cast-int_1_ip32_is128_op16_os64_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmovn_s16_dsl (reg (bv #x00 8)) 64 64 0 64 16 2)",
                "dst": "(typed:cast-int-truncate (reg (bv #x00 8)) 32 1 4 16)",
                "output_size": 64,
                "original_src_expr": " (vmovn_s16_dsl ; vmovn_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t2\n )",
                "original_dst_expr": " (typed:cast-int-truncate ; typed:cast-int_1_ip64_is128_op32_os64_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t64\n\t1\n\t2\n\t32\n )",
                "src_ctx": "vmovn_u32",
                "dst_ctx": "typed:cast-int_1_ip32_is128_op16_os64_signed_1"
            }
        }
    ],
    " (vmovn_s16_dsl ; vmovn_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t2\n )+ (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is128_op32_os64_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t64\n\t1\n\t2\n\t32\n )+64+vmovn_s16+typed:cast-uint_1_ip16_is128_op8_os64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmovn_s16_dsl (reg (bv #x00 8)) 64 64 0 64 8 2)",
                "dst": "(typed:cast-uint-truncate (reg (bv #x00 8)) 16 1 8 8)",
                "output_size": 64,
                "original_src_expr": " (vmovn_s16_dsl ; vmovn_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t2\n )",
                "original_dst_expr": " (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is128_op32_os64_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t64\n\t1\n\t2\n\t32\n )",
                "src_ctx": "vmovn_s16",
                "dst_ctx": "typed:cast-uint_1_ip16_is128_op8_os64_signed_0"
            }
        }
    ],
    " (vmovn_s16_dsl ; vmovn_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t2\n )+ (typed:cast-int-truncate ; typed:cast-int_1_ip64_is128_op32_os64_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t64\n\t1\n\t2\n\t32\n )+64+vmovn_u64+typed:cast-int_1_ip64_is128_op32_os64_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmovn_s16_dsl (reg (bv #x00 8)) 64 64 0 64 32 2)",
                "dst": "(typed:cast-int-truncate (reg (bv #x00 8)) 64 1 2 32)",
                "output_size": 64,
                "original_src_expr": " (vmovn_s16_dsl ; vmovn_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t2\n )",
                "original_dst_expr": " (typed:cast-int-truncate ; typed:cast-int_1_ip64_is128_op32_os64_signed_1\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t64\n\t1\n\t2\n\t32\n )",
                "src_ctx": "vmovn_u64",
                "dst_ctx": "typed:cast-int_1_ip64_is128_op32_os64_signed_1"
            }
        }
    ],
    " (vmovn_s16_dsl ; vmovn_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t2\n )+ (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is128_op32_os64_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t64\n\t1\n\t2\n\t32\n )+64+vmovn_u64+typed:cast-uint_1_ip64_is128_op32_os64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmovn_s16_dsl (reg (bv #x00 8)) 64 64 0 64 32 2)",
                "dst": "(typed:cast-uint-truncate (reg (bv #x00 8)) 64 1 2 32)",
                "output_size": 64,
                "original_src_expr": " (vmovn_s16_dsl ; vmovn_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t2\n )",
                "original_dst_expr": " (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is128_op32_os64_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t64\n\t1\n\t2\n\t32\n )",
                "src_ctx": "vmovn_u64",
                "dst_ctx": "typed:cast-uint_1_ip64_is128_op32_os64_signed_0"
            }
        }
    ],
    " (vmovn_s16_dsl ; vmovn_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t2\n )+ (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is128_op32_os64_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t64\n\t1\n\t2\n\t32\n )+64+vmovn_u32+typed:cast-uint_1_ip32_is128_op16_os64_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmovn_s16_dsl (reg (bv #x00 8)) 64 64 0 64 16 2)",
                "dst": "(typed:cast-uint-truncate (reg (bv #x00 8)) 32 1 4 16)",
                "output_size": 64,
                "original_src_expr": " (vmovn_s16_dsl ; vmovn_u64\n\t(reg (bv 0 (bitvector 8))) ; < 16 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t32\n\t2\n )",
                "original_dst_expr": " (typed:cast-uint-truncate ; typed:cast-uint_1_ip64_is128_op32_os64_signed_0\n\t(buffer-index  0 'uint8 128) ; < 16 x i8> False\n\t64\n\t1\n\t2\n\t32\n )",
                "src_ctx": "vmovn_u32",
                "dst_ctx": "typed:cast-uint_1_ip32_is128_op16_os64_signed_0"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_u8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t0\n\t16\n )+ (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is64_op16_os128_signed_0\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t1\n\t8\n\t16\n )+128+vmovl_u16+typed:cast-uint_1_ip16_is64_op32_os128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 0 32)",
                "dst": "(typed:cast-uint-extend (reg (bv #x00 8)) 16 1 4 32)",
                "output_size": 128,
                "original_src_expr": " (vmovl_s32_dsl ; vmovl_u8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is64_op16_os128_signed_0\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t1\n\t8\n\t16\n )",
                "src_ctx": "vmovl_u16",
                "dst_ctx": "typed:cast-uint_1_ip16_is64_op32_os128_signed_0"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_u8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t0\n\t16\n )+ (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is64_op16_os128_signed_0\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t1\n\t8\n\t16\n )+128+vmovl_u8+typed:cast-uint_1_ip8_is64_op16_os128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 0 16)",
                "dst": "(typed:cast-uint-extend (reg (bv #x00 8)) 8 1 8 16)",
                "output_size": 128,
                "original_src_expr": " (vmovl_s32_dsl ; vmovl_u8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is64_op16_os128_signed_0\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t1\n\t8\n\t16\n )",
                "src_ctx": "vmovl_u8",
                "dst_ctx": "typed:cast-uint_1_ip8_is64_op16_os128_signed_0"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_u8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t0\n\t16\n )+ (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is64_op16_os128_signed_0\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t1\n\t8\n\t16\n )+128+vmovl_u32+typed:cast-uint_1_ip32_is64_op64_os128_signed_0": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 0 64)",
                "dst": "(typed:cast-uint-extend (reg (bv #x00 8)) 32 1 2 64)",
                "output_size": 128,
                "original_src_expr": " (vmovl_s32_dsl ; vmovl_u8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t0\n\t16\n )",
                "original_dst_expr": " (typed:cast-uint-extend ; typed:cast-uint_1_ip8_is64_op16_os128_signed_0\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t1\n\t8\n\t16\n )",
                "src_ctx": "vmovl_u32",
                "dst_ctx": "typed:cast-uint_1_ip32_is64_op64_os128_signed_0"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t16\n )+ (typed:cast-int-extend ; typed:cast-int_1_ip8_is64_op16_os128_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t1\n\t8\n\t16\n )+128+vmovl_s32+typed:cast-int_1_ip32_is64_op64_os128_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 32 64 0 2 1 64)",
                "dst": "(typed:cast-int-extend (reg (bv #x00 8)) 32 1 2 64)",
                "output_size": 128,
                "original_src_expr": " (vmovl_s32_dsl ; vmovl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t16\n )",
                "original_dst_expr": " (typed:cast-int-extend ; typed:cast-int_1_ip8_is64_op16_os128_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t1\n\t8\n\t16\n )",
                "src_ctx": "vmovl_s32",
                "dst_ctx": "typed:cast-int_1_ip32_is64_op64_os128_signed_1"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t16\n )+ (typed:cast-int-extend ; typed:cast-int_1_ip8_is64_op16_os128_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t1\n\t8\n\t16\n )+128+vmovl_s16+typed:cast-int_1_ip16_is64_op32_os128_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 16 32 0 2 1 32)",
                "dst": "(typed:cast-int-extend (reg (bv #x00 8)) 16 1 4 32)",
                "output_size": 128,
                "original_src_expr": " (vmovl_s32_dsl ; vmovl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t16\n )",
                "original_dst_expr": " (typed:cast-int-extend ; typed:cast-int_1_ip8_is64_op16_os128_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t1\n\t8\n\t16\n )",
                "src_ctx": "vmovl_s16",
                "dst_ctx": "typed:cast-int_1_ip16_is64_op32_os128_signed_1"
            }
        }
    ],
    " (vmovl_s32_dsl ; vmovl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t16\n )+ (typed:cast-int-extend ; typed:cast-int_1_ip8_is64_op16_os128_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t1\n\t8\n\t16\n )+128+vmovl_s8+typed:cast-int_1_ip8_is64_op16_os128_signed_1": [
        {
            "property_name": "EnumeratePattern_arm_extend_truncate",
            "property": {
                "src": "(vmovl_s32_dsl (reg (bv #x00 8)) 64 64 0 64 8 16 0 2 1 16)",
                "dst": "(typed:cast-int-extend (reg (bv #x00 8)) 8 1 8 16)",
                "output_size": 128,
                "original_src_expr": " (vmovl_s32_dsl ; vmovl_s8\n\t(reg (bv 0 (bitvector 8))) ; < 8 x i8> False\n\t64\n\t64\n\t0\n\t64\n\t8\n\t16\n\t0\n\t2\n\t1\n\t16\n )",
                "original_dst_expr": " (typed:cast-int-extend ; typed:cast-int_1_ip8_is64_op16_os128_signed_1\n\t(buffer-index  0 'uint8 64) ; < 8 x i8> False\n\t8\n\t1\n\t8\n\t16\n )",
                "src_ctx": "vmovl_s8",
                "dst_ctx": "typed:cast-int_1_ip8_is64_op16_os128_signed_1"
            }
        }
    ]
}