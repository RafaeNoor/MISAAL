(define (output_hexagon_V6_vshuffeb_128B_layer_0_1024) 
(choose* 
(hexagon_V6_vshuffeb_128B_dsl
(output_hexagon_V6_vshuffeb_128B_layer_0_1024_arg_0_hexagon_V6_vdmpybus_128B_layer_1_1024)
(output_hexagon_V6_vshuffeb_128B_layer_0_1024_arg_1_hexagon_V6_vmpyihb_128B_layer_1_1024)
1024				;; Integer Operand 
1024				;; Integer Operand 
0				;; Integer Operand 
512				;; Integer Operand 
8				;; Precision Operand 
8				;; Integer Operand 
2				;; Integer Operand 
0				;; Integer Operand 
)
(hexagon_V6_vshuffeb_128B_dsl
(output_hexagon_V6_vshuffeb_128B_layer_0_1024_arg_0_hexagon_V6_vdmpybus_128B_layer_1_1024)
(output_hexagon_V6_vshuffeb_128B_layer_0_1024_arg_1_hexagon_V6_vmpyihb_128B_layer_1_1024)
1024				;; Integer Operand 
1024				;; Integer Operand 
0				;; Integer Operand 
512				;; Integer Operand 
16				;; Precision Operand 
16				;; Integer Operand 
2				;; Integer Operand 
0				;; Integer Operand 
)
))
(define (output_hexagon_V6_vshuffeb_128B_layer_0_1024_arg_0_hexagon_V6_vdmpybus_128B_layer_1_1024) 
(choose* 
(hexagon_V6_vdmpybus_128B_dsl
(reg (bv 0 (bitvector 8)))
(reg (bv 1 (bitvector 8)))
(reg (bv 2 (bitvector 8)))
1024				;; Integer Operand 
16				;; Precision Operand 
0				;; Integer Operand 
16				;; Integer Operand 
8				;; Precision Operand 
-1				;; Integer Operand 
1				;; Integer Operand 
0				;; Integer Operand 
4				;; Integer Operand 
8				;; Integer Operand 
8				;; Integer Operand 
0				;; Integer Operand 
)
))
(define (output_hexagon_V6_vshuffeb_128B_layer_0_1024_arg_1_hexagon_V6_vmpyihb_128B_layer_1_1024) 
(choose* 
(hexagon_V6_vmpyihb_128B_dsl
(reg (bv 3 (bitvector 8)))
(reg (bv 4 (bitvector 8)))
32				;; Integer Operand 
32				;; Integer Operand 
0				;; Integer Operand 
512				;; Integer Operand 
8				;; Integer Operand 
16				;; Precision Operand 
1				;; Integer Operand 
1				;; Integer Operand 
32				;; Integer Operand 
1				;; Integer Operand 
4				;; Integer Operand 
8				;; Integer Operand 
0				;; Integer Operand 
)
(hexagon_V6_vmpyihb_128B_dsl
(reg (bv 3 (bitvector 8)))
(reg (bv 4 (bitvector 8)))
32				;; Integer Operand 
32				;; Integer Operand 
0				;; Integer Operand 
512				;; Integer Operand 
16				;; Integer Operand 
32				;; Precision Operand 
1				;; Integer Operand 
1				;; Integer Operand 
64				;; Integer Operand 
1				;; Integer Operand 
2				;; Integer Operand 
16				;; Integer Operand 
0				;; Integer Operand 
)
(hexagon_V6_vmpyihb_128B_dsl
(reg (bv 3 (bitvector 8)))
(reg (bv 4 (bitvector 8)))
32				;; Integer Operand 
32				;; Integer Operand 
0				;; Integer Operand 
256				;; Integer Operand 
8				;; Integer Operand 
32				;; Precision Operand 
1				;; Integer Operand 
0				;; Integer Operand 
64				;; Integer Operand 
1				;; Integer Operand 
4				;; Integer Operand 
8				;; Integer Operand 
0				;; Integer Operand 
)
(hexagon_V6_vmpyihb_128B_dsl
(reg (bv 3 (bitvector 8)))
(reg (bv 4 (bitvector 8)))
32				;; Integer Operand 
32				;; Integer Operand 
0				;; Integer Operand 
256				;; Integer Operand 
8				;; Integer Operand 
32				;; Precision Operand 
1				;; Integer Operand 
1				;; Integer Operand 
64				;; Integer Operand 
1				;; Integer Operand 
4				;; Integer Operand 
8				;; Integer Operand 
0				;; Integer Operand 
)
))