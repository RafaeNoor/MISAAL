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
            '" (define %trunc (extract %offset 0 slice)) "',
            '" %trunc "',
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
    "typed-folded:vec-ge": {
        "target_instructions": {
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
    "typed-folded:vec-le": {
        "target_instructions": {
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
    "typed-folded:vec-lt": {
        "target_instructions": {
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

    "typed-folded:vec-mul": {
        "target_instructions": {
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
                    "32",
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
                    "32",
                    "0"
                ]
            },
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


"typed-folded:vec-widen-mul": {
    "target_instructions": {
        "typed-folded:vec-widen-mul-signed-p16-s64": {
            "in_vectsize": 64,
            "out_vectsize": 128,
            "lanesize": 16,
            "in_precision": 16,
            "out_precision": 32,
            "in_vectsize_index": 3,
            "out_vectsize_index": None,
            "lanesize_index": 2,
            "in_precision_index": 2,
            "out_precision_index": 4,
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
                "32",
                "1"
            ]
        },

        "typed-folded:vec-widen-mul-unsigned-p16-s64": {
            "in_vectsize": 64,
            "out_vectsize": 128,
            "lanesize": 16,
            "in_precision": 16,
            "out_precision": 32,
            "in_vectsize_index": 3,
            "out_vectsize_index": None,
            "lanesize_index": 2,
            "in_precision_index": 2,
            "out_precision_index": 4,
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
                "32",
                "0"
            ]
        },
    },
    "semantics": [
        '" (define (typed-folded:vec-widen-mul v1 v2 iprec isize widenprec sign) "',
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
        '" (define %prod (bvmul %widen_slice_v1 %widen_slice_v1)) "',
        '" %prod "',
        '" ) "',
        '" ) "',
        '" ) "',
        '" dst "',
        '" ) "',
    ]
},

"typed-folded:vec-absd": {
    "target_instructions": {
        "typed-folded:vec-absd-signed-p16-s64": {
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

        "typed-folded:vec-absd-unsigned-p16-s64": {
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
        '" (define (typed-folded:vec-absd v1 v2 iprec isize sign) "',
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
        '" (define max-v1-v2 (bvmax slice_v1 slice_v2 sign)) "',
        '" (define min-v1-v2 (bvmin slice_v1 slice_v2 sign)) "',
        '" (define %diff (bvsub max-v1-v2 min-v1-v2)) "',
        '" %diff "',
        '" ) "',
        '" ) "',
        '" ) "',
        '" dst "',
        '" ) "',
    ]
},

"typed-folded:vec-shr": {
    "target_instructions": {
        "typed-folded:vec-shr-signed-p16-s64": {
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

        "typed-folded:vec-shr-unsigned-p16-s64": {
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
        '" (define (typed-folded:vec-shr v1 v2 iprec isize sign) "',
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
        '" (define %result (bvshr slice_v1 slice_v2 sign)) "',
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

"typed-folded:vec-saturate": {
    "target_instructions": {
        "typed-folded:vec-saturate-signed-p16-s64": {
            "in_vectsize": 64,
            "out_vectsize": 32,
            "lanesize": 16,
            "in_precision": 16,
            "out_precision": 8,
            "in_vectsize_index": 2,
            "out_vectsize_index": None,
            "lanesize_index": 1,
            "in_precision_index": 1,
            "out_precision_index": None,
            "arg_permute_map": [],
            "Signedness": 1,
            "Cost": "[]",
            "SIMD": "False",
            "Extensions": [
                ""
            ],
            "args": [
                "SYMBOLIC_BV_64",
                "16",
                "64",
                "8",
                "1"
            ]
        },

        "typed-folded:vec-saturate-unsigned-p16-s64": {
            "in_vectsize": 64,
            "out_vectsize": 32,
            "lanesize": 16,
            "in_precision": 16,
            "out_precision": 8,
            "in_vectsize_index": 2,
            "out_vectsize_index": None,
            "lanesize_index": 1,
            "in_precision_index": 1,
            "out_precision_index": None,
            "arg_permute_map": [],
            "Signedness": 0,
            "Cost": "[]",
            "SIMD": "False",
            "Extensions": [
                ""
            ],
            "args": [
                "SYMBOLIC_BV_64",
                "16",
                "64",
                "8",
                "0"
            ]
        },
    },
    "semantics": [
        '" (define (typed-folded:vec-saturate vec iprec isize oprec sign) "',
        '" (define dst "',
        '" (apply "',
        '" concat "',
        '" (for/list ([%iter (reverse (range 0 isize iprec))]) "',
        '" (define %lastidx1 (- iprec 1)) "',
        '" (define %high (+ %lastidx1 %iter)) "',
        '" (define slice (extract %high %iter vec)) "',
        '" (define %trunc (bvsaturate slice iprec oprec sign)) "',
        '" %trunc "',
        '" ) "',
        '" ) "',
        '" ) "',
        '" dst "',
        '" ) "',
    ]
},



"typed-folded:vec-bwand": {
    "target_instructions": {
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
                "16",
            ]
        },
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
},

"typed-folded:vec-bwor": {
    "target_instructions": {
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
                "16",
            ]
        },
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

"typed-folded:vec-eq": {
    "target_instructions": {

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
                "64"
            ]
        },

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
"typed-folded:vec-rounding_halving_add": {
    "target_instructions": {
        "typed-folded:vec-rounding_halving_add-signed-p16-s64": {
            "in_vectsize": 64,
            "out_vectsize": 64,
            "lanesize": 16,
            "in_precision": 16,
            "out_precision": 16,
            "in_vectsize_index": 4,
            "out_vectsize_index": 4,
            "lanesize_index": 2,
            "in_precision_index": 2,
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
                "32",
                "64",
                "1"
            ]
        },

        "typed-folded:vec-rounding_halving_add-unsigned-p16-s64": {
            "in_vectsize": 64,
            "out_vectsize": 64,
            "lanesize": 16,
            "in_precision": 16,
            "out_precision": 16,
            "in_vectsize_index": 4,
            "out_vectsize_index": 4,
            "lanesize_index": 2,
            "in_precision_index": 2,
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
                "32",
                "64",
                "0"
            ]
        },
    },
    "semantics": [
        '" (define (typed-folded:vec-rounding_halving_add v1 v2 iprec widenprec isize sign) "',
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
        '" (define sum (bvadd %widen_slice_v1 %widen_slice_v1)) "',
        '" (define rounded_sum (bvadd sum (bv 1 (bitvector widenprec)))) "',
        '" (define avg (bvdiv rounded_sum (bv 2 (bitvector widenprec))  sign)) "',
        '" (define %narrow (extract %lastidx1 0 avg)) "',
        '" %narrow "',
        '" ) "',
        '" ) "',
        '" ) "',
        '" dst "',
        '" ) "',



    ]
},

"typed-folded:vec-halving_add": {
    "target_instructions": {
        "typed-folded:vec-halving_add-signed-p16-s64": {
            "in_vectsize": 64,
            "out_vectsize": 64,
            "lanesize": 16,
            "in_precision": 16,
            "out_precision": 16,
            "in_vectsize_index": 4,
            "out_vectsize_index": 4,
            "lanesize_index": 2,
            "in_precision_index": 2,
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
                "32",
                "64",
                "1"
            ]
        },

        "typed-folded:vec-halving_add-unsigned-p16-s64": {
            "in_vectsize": 64,
            "out_vectsize": 64,
            "lanesize": 16,
            "in_precision": 16,
            "out_precision": 16,
            "in_vectsize_index": 4,
            "out_vectsize_index": 4,
            "lanesize_index": 2,
            "in_precision_index": 2,
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
                "32",
                "64",
                "0"
            ]
        },
    },
    "semantics": [
        '" (define (typed-folded:vec-halving_add v1 v2 iprec widenprec isize sign) "',
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
        '" (define sum (bvadd %widen_slice_v1 %widen_slice_v1)) "',
        '" (define avg (bvdiv sum (bv 2 (bitvector widenprec))  sign)) "',
        '" (define %narrow (extract %lastidx1 0 avg)) "',
        '" %narrow "',
        '" ) "',
        '" ) "',
        '" ) "',
        '" dst "',
        '" ) "',



    ]
},
"typed-folded:vec-rounding_shift_right": {
    "target_instructions": {
        "typed-folded:vec-rounding_shift_right-signed-p16-s64": {
            "in_vectsize": 64,
            "out_vectsize": 64,
            "lanesize": 16,
            "in_precision": 16,
            "out_precision": 16,
            "in_vectsize_index": 4,
            "out_vectsize_index": 4,
            "lanesize_index": 2,
            "in_precision_index": 2,
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
                "32",
                "64",
                "1"
            ]
        },

        "typed-folded:vec-rounding_shift_right-unsigned-p16-s64": {
            "in_vectsize": 64,
            "out_vectsize": 64,
            "lanesize": 16,
            "in_precision": 16,
            "out_precision": 16,
            "in_vectsize_index": 4,
            "out_vectsize_index": 4,
            "lanesize_index": 2,
            "in_precision_index": 2,
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
                "32",
                "64",
                "0"
            ]
        },
    },
    "semantics": [
        '" (define (typed-folded:vec-rounding_shift_right v1 v2 iprec widenprec isize sign) "',
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
        '" (define %max-b-0 (bvmax slice_v2 (bv 0 (bitvector iprec)) sign)) "',
        '" (define %lshift (bvshl (bv 1 (bitvector iprec)) %max-b-0 )) "',
        '" (define %half (bvdiv %lshift (bv 2 (bitvector iprec)) sign)) "',
        '" (define %widen_half_v2 (bvsizeext %half widenprec sign)) "',
        '" (define %sum (bvadd %widen_slice_v1 %widen_half_v2)) "',
        '" (define %rshift (bvshr %sum %widen_slice_v2 sign)) "',
        '" (define %narrow (bvsaturate %rshift widenprec iprec sign)) "',
        '" %narrow "',
        '"  "',
        '" ) "',
        '" ) "',
        '" ) "',
        '" dst "',
        '" ) "',
    ]
},

"typed-folded:vec-rounding_mul_shift_right": {
    "target_instructions": {
        "typed-folded:vec-rounding_mul_shift_right-signed-p16-s64": {
            "in_vectsize": 64,
            "out_vectsize": 64,
            "lanesize": 16,
            "in_precision": 16,
            "out_precision": 16,
            "in_vectsize_index": 5,
            "out_vectsize_index": 5,
            "lanesize_index": 3,
            "in_precision_index": 3,
            "out_precision_index": 3,
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
                "SYMBOLIC_BV_64",
                "16",
                "32",
                "64",
                "1"
            ]
        },

        "typed-folded:vec-rounding_mul_shift_right-unsigned-p16-s64": {
            "in_vectsize": 64,
            "out_vectsize": 64,
            "lanesize": 16,
            "in_precision": 16,
            "out_precision": 16,
            "in_vectsize_index": 5,
            "out_vectsize_index": 5,
            "lanesize_index": 3,
            "in_precision_index": 3,
            "out_precision_index": 3,
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
                "SYMBOLIC_BV_64",
                "16",
                "32",
                "64",
                "0"
            ]
        },
    },
    "semantics": [
        '" (define (typed-folded:vec-rounding_mul_shift_right v1 v2 v3 iprec widenprec isize sign) "',
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
        '" (define %lastidx3 (- iprec 1)) "',
        '" (define %high3 (+ %lastidx3 %iter)) "',
        '" (define slice_v3 (extract %high3 %iter v3)) "',
        '" (define %widen_slice_v3 (bvsizeext slice_v3 widenprec sign)) "',
        '" (define %widen-mul-a-b (bvmul %widen_slice_v1 %widen_slice_v2)) "',
        '" (define %max-q-0 (bvmax %widen_slice_v3 (bv 0 (bitvector widenprec)) sign)) "',
        '" (define %lshift (bvshl (bv 1 (bitvector widenprec)) %max-q-0 )) "',
        '" (define %half (bvdiv %lshift (bv 2 (bitvector widenprec)) sign)) "',
        '" (define %widen_half_v3 (bvsizeext %half (* widenprec 2) sign)) "',
        '" (define %double-widen-mul-a-b (bvsizeext %widen-mul-a-b (* widenprec 2) sign)) "',
        '" (define %sum (bvadd %double-widen-mul-a-b %widen_half_v3)) "',
        '" (define %double-widen-v3 (bvsizeext %widen_slice_v3 (* widenprec 2) sign)) "',
        '" (define %rshift (bvshr %sum %double-widen-v3 sign)) "',
        '" (define %narrow (bvsaturate %rshift (* widenprec 2) widenprec sign)) "',
        '" (define %double-narrow (bvsaturate %narrow widenprec iprec sign)) "',
        '" %double-narrow "',
        '" ) "',
        '" ) "',
        '" ) "',
        '" dst "',
        '" ) "',
    ]
},
"typed-folded:vec-reduce_add": {
    "target_instructions": {
        "typed-folded:vec-reduce_add-p8-s16": {
            "in_vectsize": 16,
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
                "2",
                "SYMBOLIC_BV_16",
                "8",
                "16"
            ]
        },
    },
    "semantics": [
        '" (define (typed-folded:vec-reduce_add reduce-factor v1 iprec isize ) "',
        '" (define dst "',
        '" (apply "',
        '" concat "',
        '" (for/list ([%outer (reverse (range 0 isize (* iprec reduce-factor)))]) "',
        '" (apply "',
        '" bvadd "',
        '" (for/list ([%iter (reverse (range 0 reduce-factor 1))]) "',
        '" (define %step (* iprec %iter)) "',
        '" (define %low-offset (+ %outer %step)) "',
        '" (define %lastidx (- iprec 1)) "',
        '" (define %high-idx (+ %low-offset %lastidx)) "',
        '" (define %slice (extract %high-idx %low-offset v1)) "',
        '" %slice "',
        '" ) "',
        '" ) "',
        '" ) "',
        '" ) "',
        '" ) "',
        '" dst "',
        '" ) "',
    ]
},



"typed-folded:broadcast": {
    "target_instructions": {
        "typed-folded:broadcast-p16-s1024": {
            "in_vectsize": 16,
            "out_vectsize": 1024,
            "lanesize": 16,
            "in_precision": 16,
            "out_precision": 16,
            "in_vectsize_index": 1 ,
            "out_vectsize_index": None,
            "lanesize_index": 1,
            "in_precision_index": 1,
            "out_precision_index": 1,
            "arg_permute_map": [],
            "Signedness": None,
            "Cost": "[]",
            "SIMD": "False",
            "Extensions": [
                ""
            ],
            "args": [
                "SYMBOLIC_BV_16",
                "16",
                "64"
            ]
        },
    },
    "semantics": [
        '" (define (typed-folded:broadcast %v1 iprec factor) "',
        '" (define dst "',
        '" (apply "',
        '" concat "',
        '" (for/list ([%iter (reverse (range 0 factor 1))]) "',
        '" %v1 "',
        '" ) "',
        '" ) "',
        '" ) "',
        '" dst "',
        '" ) "',
    ]
},


"typed-folded:slice_vector": {
    "target_instructions": {
        "typed-folded:slice_vector-p8-s1024_b0_s1_l64": {
            "in_vectsize": 1024,
            "out_vectsize": 512,
            "lanesize": 8,
            "in_precision": 8,
            "out_precision": 8,
            "in_vectsize_index": 2 ,
            "out_vectsize_index": None,
            "lanesize_index": 1,
            "in_precision_index": 1,
            "out_precision_index": 1,
            "arg_permute_map": [],
            "Signedness": None,
            "Cost": "[]",
            "SIMD": "False",
            "Extensions": [
                ""
            ],
            "args": [
                "SYMBOLIC_BV_1024",
                "8",
                "1024",
                "0",
                "1",
                "64"
            ]
        },
    },
    "semantics": [
        '" (define (typed-folded:slice_vectors %v1 iprec %isize base stride len) "',
        '" (define dst "',
        '" (apply "',
        '" concat "',
        '" (for/list ([%iter (reverse (range 0 len 1))]) "',
        '" (define %offset-from-base (* iprec stride)) "',
        '" (define %elem-idx (+ base %iter)) "',
        '" (define %offset-to-base (* %elem-idx iprec)) "',
        '" (define %offset (+ %offset-to-base %offset-from-base)) "',
        '" (define %lastidx (- iprec 1)) "',
        '" (define %high (+ %offset %lastidx)) "',
        '" (define %slice (extract %high %offset %v1)) "',
        '" %slice "',
        '" ) "',
        '" ) "',
        '" ) "',
        '" dst "',
        '" ) "',
    ]
},
}

