halide_folded = {
    "typed-folded:cast-extend": {
        "target_instructions": {
            "typed-folded:cast-extend-signed-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 16,
                "in_vectsize_index": None,
                "out_vectsize_index": None,
                "lanesize_index": 1,
                "in_precision_index": 1,
                "out_precision_index": 3,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "16",
                    "1"
                ]
            },
            "typed-folded:cast-extend-signed-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 16,
                "in_vectsize_index": None,
                "out_vectsize_index": None,
                "lanesize_index": 1,
                "in_precision_index": 1,
                "out_precision_index": 3,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "16",
                    "1"
                ]
            },

            "typed-folded:cast-extend-unsigned-p8-s32": {
                "in_vectsize": 32,
                "out_vectsize": 64,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 16,
                "in_vectsize_index": None,
                "out_vectsize_index": None,
                "lanesize_index": 1,
                "in_precision_index": 1,
                "out_precision_index": 3,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_32",
                    "8",
                    "32",
                    "16",
                    "0"
                ]
            },
            "typed-folded:cast-extend-unsigned-p8-s8": {
                "in_vectsize": 8,
                "out_vectsize": 16,
                "lanesize": 8,
                "in_precision": 8,
                "out_precision": 16,
                "in_vectsize_index": None,
                "out_vectsize_index": None,
                "lanesize_index": 1,
                "in_precision_index": 1,
                "out_precision_index": 3,
                "arg_permute_map": [],
                "Signedness": 0,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_8",
                    "8",
                    "8",
                    "16",
                    "0"
                ]
            },
        },
        "semantics": [
            '" (define (typed-folded:cast-extend vec iprec isize oprec sign) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice (extract %high %iter vec)) "',
            '" (define %sext (bvsizeext slice oprec sign)) "',
            '" %sext "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:cast-truncate": {
        "target_instructions": {
            "typed-folded:cast-truncate-p16-s16": {
                "in_vectsize": 16,
                "out_vectsize": 8,
                "lanesize": 16,
                "in_precision": 16,
                "out_precision": 8,
                "in_vectsize_index": 2,
                "out_vectsize_index": None,
                "lanesize_index": 1,
                "in_precision_index": 1,
                "out_precision_index": 3,
                "arg_permute_map": [],
                "Signedness": 1,
                "Cost": "[]",
                "SIMD": "False",
                "Extensions": [
                    ""
                ],
                "args": [
                    "SYMBOLIC_BV_16",
                    "16",
                    "16",
                    "8"
                ]
            },
        },
        "semantics": [
            '" (define (typed-folded:cast-truncate vec iprec isize oprec) "',
            '" (define dst "',
            '" (apply "',
            '" concat "',
            '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
            '" (define %lastidx1 (- iprec 1)) "',
            '" (define %high (+ %lastidx1 %iter)) "',
            '" (define slice (extract %high %iter vec)) "',
            '" (define %offset (- oprec 1)) "',
            '" (define trunc (extract %offset 0 slice)) "',
            '" trunc "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },
    "typed-folded:vec-div": {
        "target_instructions": {
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

    "typed-folded:vec-max": {
        "target_instructions": {
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


    "typed-folded:vec-min": {
        "target_instructions": {
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
    "typed-folded:vec-shl": {
        "target_instructions": {
            "typed-folded:vec-shl-signed-p16-s64": {
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
        },
        "semantics": [
            '" (define (typed-folded:vec-shl v1 v2 iprec isize sign) "',
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
            '" (define %result (bvshl slice_v1 slice_v2)) "',
            '" %result "',
            '" ) "',
            '" ) "',
            '" ) "',
            '" dst "',
            '" ) "',
        ]
    },

    "typed-folded:vec-add": {
        "target_instructions": {
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


}

