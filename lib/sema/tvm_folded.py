tvm_folded = {
    "typed-folded:vec-add": {
        "target_instructions": {
            "typed-folded:vec-add-signed-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "-1"
                ]
            },
            "typed-folded:vec-add-signed-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "1"
                ]
            },
            "typed-folded:vec-add-unsigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "0"
                ]
            },
            "typed-folded:vec-add-nosigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "-1"
                ]
            }
        },
        "semantics": [
            '" (define (typed-folded:vec-add v1 v2 iprec isize sign) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %result (bvaddnw slice_v1 slice_v2 iprec sign)) "',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:vec-sub": {
        "target_instructions": {
            "typed-folded:vec-sub-signed-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "-1"
                ]
            },
            "typed-folded:vec-sub-signed-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "1"
                ]
            },
            "typed-folded:vec-sub-unsigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "0"
                ]
            },
            "typed-folded:vec-sub-nosigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "-1"
                ]
}
        },
        "semantics": [
            '" (define (typed-folded:vec-sub v1 v2 iprec isize sign) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %result (bvsubnw slice_v1 slice_v2 iprec sign)) "',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:vec-mul": {
        "target_instructions": {
            "typed-folded:vec-mul-signed-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-mul-signed-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "1"
                ]
            },
            "typed-folded:vec-mul-unsigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "0"
                ]
            }

        },
        "semantics": [
            '" (define (typed-folded:vec-mul v1 v2 iprec isize widenprec sign) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %widen_slice_v1 (bvsizeext slice_v1 widenprec sign)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %widen_slice_v2 (bvsizeext slice_v2 widenprec sign)) "',
            '" (define prod (bvmul %widen_slice_v1 %widen_slice_v1)) "',
            '" (define %narrow (extract %lastidx1 0 prod)) "',
            '" %narrow "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:vec-div": {
        "target_instructions": {
            "typed-folded:vec-div-signed-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-div-signed-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "1"
                ]
            },
            "typed-folded:vec-div-unsigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "0"
                ]
            }
        },
        "semantics": [
            '" (define (typed-folded:vec-div v1 v2 iprec isize sign) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %result (bvdiv slice_v1 slice_v2 sign)) "',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:vec-mod": {
        "target_instructions": {
            "typed-folded:vec-mod-signed-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-mod-signed-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "1"
                ]
            },
            "typed-folded:vec-mod-unsigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "0"
                ]
            }
        },
        "semantics": [
            '" (define (typed-folded:vec-mod v1 v2 iprec isize sign) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %result (bvrem slice_v1 slice_v2 sign)) "',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:vec-min": {
        "target_instructions": {
            "typed-folded:vec-min-signed-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-min-signed-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "1"
                ]
            },
            "typed-folded:vec-min-unsigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "0"
                ]
            }
        },
        "semantics": [
            '" (define (typed-folded:vec-min v1 v2 iprec isize sign) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %result (bvmin slice_v1 slice_v2 sign)) "',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:vec-max": {
        "target_instructions": {
            "typed-folded:vec-max-signed-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-max-signed-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "1"
                ]
            },
            "typed-folded:vec-max-unsigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "0"
                ]
            }
        },
        "semantics": [
            '" (define (typed-folded:vec-max v1 v2 iprec isize sign) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %result (bvmax slice_v1 slice_v2 sign)) "',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:vec-lt": {
        "target_instructions": {
            "typed-folded:vec-lt-signed-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 1,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 1,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 2,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 2,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 4,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 4,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 1,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 1,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 2,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 2,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 4,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 4,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 8,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 8,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 1,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 1,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 2,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 2,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 4,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 4,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 8,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 8,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 16,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 16,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 1,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 1,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 2,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 2,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 4,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 4,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 8,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 8,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 16,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 16,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 32,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 32,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-lt-signed-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "1"
                ]
            },
            "typed-folded:vec-lt-unsigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "0"
                ]
            }
        },
        "semantics": [
            '" (define (typed-folded:vec-lt v1 v2 iprec isize sign) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %bool (bvlt slice_v1 slice_v2 sign)) "',
            '" (define %result (bool-to-bv %bool))"',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:vec-le": {
        "target_instructions": {
            "typed-folded:vec-le-signed-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 1,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 1,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 2,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 2,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 4,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 4,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 1,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 1,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 2,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 2,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 4,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 4,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 8,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 8,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 1,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 1,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 2,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 2,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 4,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 4,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 8,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 8,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 16,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 16,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 1,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 1,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 2,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 2,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 4,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 4,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 8,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 8,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 16,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 16,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 32,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 32,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-le-signed-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "1"
                ]
            },
            "typed-folded:vec-le-unsigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "0"
                ]
            }

        },
        "semantics": [
            '" (define (typed-folded:vec-le v1 v2 iprec isize sign) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %bool (bvle slice_v1 slice_v2 sign)) "',
            '" (define %result (bool-to-bv %bool))"',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:vec-gt": {
        "target_instructions": {
            "typed-folded:vec-gt-signed-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 1,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 1,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 2,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 2,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 4,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 4,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 1,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 1,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 2,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 2,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 4,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 4,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 8,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 8,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 1,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 1,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 2,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 2,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 4,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 4,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 8,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 8,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 16,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 16,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 1,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 1,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 2,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 2,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 4,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 4,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 8,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 8,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 16,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 16,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 32,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 32,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-gt-signed-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "1"
                ]
            },
            "typed-folded:vec-gt-unsigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "0"
                ]
            }

        },
        "semantics": [
            '" (define (typed-folded:vec-gt v1 v2 iprec isize sign) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %bool (bvgt slice_v1 slice_v2 sign)) "',
            '" (define %result (bool-to-bv %bool))"',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:vec-ge": {
        "target_instructions": {
            "typed-folded:vec-ge-signed-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 1,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 1,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 2,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 2,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 4,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 4,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 1,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 1,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 2,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 2,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 4,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 4,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 8,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 8,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 1,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 1,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 2,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 2,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 4,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 4,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 8,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 8,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 16,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 16,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 1,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 1,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 2,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 2,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 4,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 4,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 8,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 8,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 16,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 16,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 32,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 32,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "0"
                ]
            },
            "typed-folded:vec-ge-signed-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "1"
                ]
            },
            "typed-folded:vec-ge-unsigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "0"
                ]
            }

        },
        "semantics": [
            '" (define (typed-folded:vec-ge v1 v2 iprec isize sign) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %bool (bvge slice_v1 slice_v2 sign)) "',
            '" (define %result (bool-to-bv %bool))"',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:vec-eq": {
        "target_instructions": {
            "typed-folded:vec-eq-nosigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 1,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 2,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 4,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 1,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 2,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 4,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 8,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 1,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 2,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 4,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 8,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 16,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 1,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 2,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 4,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 8,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 16,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 32,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048",
                    "-1"
                ]
            },
            "typed-folded:vec-eq-nosigned-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 1,
                "in_vectsize_index": 3,
                "out_vectsize_index": None,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096",
                    "-1"
                ]
            }
        },
        "semantics": [
            '" (define (typed-folded:vec-eq v1 v2 iprec isize) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %bool (bveq slice_v1 slice_v2)) "',
            '" (define %result (bool-to-bv %bool))"',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    # CORRECT ENTRIES BELOW HERE, FIX/CHECK ABOVE
    
    "typed-folded:vec-bwor": {
        "target_instructions": {
            "typed-folded:vec-bwor-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8"
                ]
            },
            "typed-folded:vec-bwor-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16"
                ]
            },
            "typed-folded:vec-bwor-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32"
                ]
            },
            "typed-folded:vec-bwor-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64"
                ]
            },
            "typed-folded:vec-bwor-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128"
                ]
            },
            "typed-folded:vec-bwor-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256"
                ]
            },
            "typed-folded:vec-bwor-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512"
                ]
            },
            "typed-folded:vec-bwor-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16"
                ]
            },
            "typed-folded:vec-bwor-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32"
                ]
            },
            "typed-folded:vec-bwor-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64"
                ]
            },
            "typed-folded:vec-bwor-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128"
                ]
            },
            "typed-folded:vec-bwor-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256"
                ]
            },
            "typed-folded:vec-bwor-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512"
                ]
            },
            "typed-folded:vec-bwor-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024"
                ]
            },
            "typed-folded:vec-bwor-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32"
                ]
            },
            "typed-folded:vec-bwor-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64"
                ]
            },
            "typed-folded:vec-bwor-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128"
                ]
            },
            "typed-folded:vec-bwor-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256"
                ]
            },
            "typed-folded:vec-bwor-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512"
                ]
            },
            "typed-folded:vec-bwor-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024"
                ]
            },
            "typed-folded:vec-bwor-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048"
                ]
            },
            "typed-folded:vec-bwor-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64"
                ]
            },
            "typed-folded:vec-bwor-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128"
                ]
            },
            "typed-folded:vec-bwor-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256"
                ]
            },
            "typed-folded:vec-bwor-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512"
                ]
            },
            "typed-folded:vec-bwor-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024"
                ]
            },
            "typed-folded:vec-bwor-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048"
                ]
            },
            "typed-folded:vec-bwor-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096"
                ]
            }
        },
        "semantics": [
            '" (define (typed-folded:vec-bwor v1 v2 iprec isize) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %result (bvor slice_v1 slice_v2)) "',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:vec:bwand": {
        "target_instructions": {
            "typed-folded:vec-bwand-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 8,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "SYMBOLIC_BV_8",
                    "8",
                    "8"
                ]
            },
            "typed-folded:vec-bwand-p8-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "8",
                    "16"
                ]
            },
            "typed-folded:vec-bwand-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "8",
                    "32"
                ]
            },
            "typed-folded:vec-bwand-p8-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "8",
                    "64"
                ]
            },
            "typed-folded:vec-bwand-p8-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "8",
                    "128"
                ]
            },
            "typed-folded:vec-bwand-p8-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "8",
                    "256"
                ]
            },
            "typed-folded:vec-bwand-p8-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 8,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "8",
                    "512"
                ]
            },
            "typed-folded:vec-bwand-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 16,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "SYMBOLIC_BV_16",
                    "16",
                    "16"
                ]
            },
            "typed-folded:vec-bwand-p16-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "16",
                    "32"
                ]
            },
            "typed-folded:vec-bwand-p16-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "16",
                    "64"
                ]
            },
            "typed-folded:vec-bwand-p16-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "16",
                    "128"
                ]
            },
            "typed-folded:vec-bwand-p16-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "16",
                    "256"
                ]
            },
            "typed-folded:vec-bwand-p16-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "16",
                    "512"
                ]
            },
            "typed-folded:vec-bwand-p16-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 16,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "16",
                    "1024"
                ]
            },
            "typed-folded:vec-bwand-p32-s32": {
                "in_vectsize": 32,
                "out_vectsize": 32,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "SYMBOLIC_BV_32",
                    "32",
                    "32"
                ]
            },
            "typed-folded:vec-bwand-p32-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "32",
                    "64"
                ]
            },
            "typed-folded:vec-bwand-p32-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "32",
                    "128"
                ]
            },
            "typed-folded:vec-bwand-p32-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "32",
                    "256"
                ]
            },
            "typed-folded:vec-bwand-p32-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "32",
                    "512"
                ]
            },
            "typed-folded:vec-bwand-p32-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "32",
                    "1024"
                ]
            },
            "typed-folded:vec-bwand-p32-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 32,
                "in_precision": 32,
                "out_precision": 32,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "32",
                    "2048"
                ]
            },
            "typed-folded:vec-bwand-p64-s64": {
                "in_vectsize": 64,
                "out_vectsize": 64,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_64",
                    "SYMBOLIC_BV_64",
                    "64",
                    "64"
                ]
            },
            "typed-folded:vec-bwand-p64-s128": {
                "in_vectsize": 128,
                "out_vectsize": 128,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_128",
                    "SYMBOLIC_BV_128",
                    "64",
                    "128"
                ]
            },
            "typed-folded:vec-bwand-p64-s256": {
                "in_vectsize": 256,
                "out_vectsize": 256,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_256",
                    "SYMBOLIC_BV_256",
                    "64",
                    "256"
                ]
            },
            "typed-folded:vec-bwand-p64-s512": {
                "in_vectsize": 512,
                "out_vectsize": 512,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_512",
                    "SYMBOLIC_BV_512",
                    "64",
                    "512"
                ]
            },
            "typed-folded:vec-bwand-p64-s1024": {
                "in_vectsize": 1024,
                "out_vectsize": 1024,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_1024",
                    "SYMBOLIC_BV_1024",
                    "64",
                    "1024"
                ]
            },
            "typed-folded:vec-bwand-p64-s2048": {
                "in_vectsize": 2048,
                "out_vectsize": 2048,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_2048",
                    "SYMBOLIC_BV_2048",
                    "64",
                    "2048"
                ]
            },
            "typed-folded:vec-bwand-p64-s4096": {
                "in_vectsize": 4096,
                "out_vectsize": 4096,
                "lanesize": 64,
                "in_precision": 64,
                "out_precision": 64,
                "in_vectsize_index": 3,
                "out_vectsize_index": 3,
                "lanesize_index": 2,
                "in_precision_index": 2,
                "out_precision_index": 2,
                "arg_permute_map": [],
                "Signedness": None,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_4096",
                    "SYMBOLIC_BV_4096",
                    "64",
                    "4096"
                ]
            }
        },
        "semantics": [
            '" (define (typed-folded:vec-bwand v1 v2 iprec isize) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice_v1 (extract %high %iter v1)) "',
            '" (define %lastidx2 (- iprec 1)) "',
            '" (define %high2 (+ %lastidx2 %iter)) "',
            '" (define slice_v2 (extract %high2 %iter v2)) "',
            '" (define %result (bvand slice_v1 slice_v2)) "',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    }
}
