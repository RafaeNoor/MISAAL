tvm_folded = {
    "typed-folded:vec-add": {
        "target_instructions": {
            # VF = 1
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
            # VF = 2
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
            # VF = 4
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
            # VF = 8
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
            # VF = 16
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
            # VF = 32
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
            # VF = 64
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
    }
}