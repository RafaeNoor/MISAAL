#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require rosette/lib/destruct)
(require hydride)
(require misaal)

(require "./definition.rkt")

(provide  (all-defined-out))

(define (repair:cost expr)
  (destruct expr
            [(repair-build-vector_dsl num-ele indices)
             1
             ]
            [(repair-add_dsl v1 v2 prec size)
             (+ 1 
               (repair:cost v1)  
               (repair:cost v2)  
               )
             ]
            [(repair-sat-add_dsl v1 v2 prec size)
             (+ 1 
               (repair:cost v1)  
               (repair:cost v2)  
               )
             ]
            [(repair-reduce-add_dsl reduce-factor v1 prec size)
             (+ 1
               (repair:cost v1)  
               )
             ]

            [(repair-max_dsl v1 v2 prec size)
             (+ 1
               (repair:cost v1)  
               (repair:cost v2)  
               )
             ]

            [(repair-min_dsl v1 v2 prec size)
             (+ 1
               (repair:cost v1)  
               (repair:cost v2)  
               )
             ]
            [(repair-sub_dsl v1 v2 prec size)
             (+ 1
               (repair:cost v1)  
               (repair:cost v2)  
               )
             ]

            [(repair-sat-sub_dsl v1 v2 prec size)
             (+ 1
               (repair:cost v1)  
               (repair:cost v2)  
               )
             ]

            [(repair-mul_dsl v1 v2 prec size)
             (+ 1
               (repair:cost v1)  
               (repair:cost v2)  
               )
             ]
            [(repair-sext_dsl v1  iprec oprec size)
             (+ 1 
               (repair:cost v1)  
               )
             ]
            [(repair-extract-index_dsl v1  prec size index)
              (+ 1 
               (repair:cost v1)  
                )
             ]
            [(repair-widen-mul_dsl v1 v2 iprec oprec size)
             (+ 1
               (repair:cost v1)  
               (repair:cost v2)  
               )
             ]

            [(repair-sdiv_dsl v1 v2 prec size)
             (+ 1
               (repair:cost v1)  
               (repair:cost v2)  
               )
             ]

            [(repair-udiv_dsl v1 v2 prec size)
             (+ 1
               (repair:cost v1)  
               (repair:cost v2)  
               )
             ]

            [(repair-bvor_dsl v1 v2 prec size)
             (+ 1
               (repair:cost v1)  
               (repair:cost v2)  
               )
             ]

            [(repair-bvand_dsl v1 v2 prec size)
             (+ 1
               (repair:cost v1)  
               (repair:cost v2)  
               )
             ]

            [(repair-bvmod_dsl v1 v2 prec size)
             (+ 1
               (repair:cost v1)  
               (repair:cost v2)  
               )
             ]
            [_
              (println expr)
              (error "Unsupported op")
              ]
    )
  )
