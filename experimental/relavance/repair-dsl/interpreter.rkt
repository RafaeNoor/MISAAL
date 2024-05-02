#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require rosette/lib/destruct)
(require hydride)
(require misaal)

(require "./semantics.rkt")
(require "./definition.rkt")

(provide  (all-defined-out))

(define (repair:interpret expr env)
  (destruct expr
            [(repair-build-vector_dsl num-ele indices)
             (repair-build-vector num-ele indices env)
             ]
            [(repair-add_dsl v1 v2 prec size)
             (repair-add 
               (repair:interpret v1 env)  
               (repair:interpret v2 env)  
               prec size)
             ]
            [(repair-sat-add_dsl v1 v2 prec size)
             (repair-sat-add 
               (repair:interpret v1 env)  
               (repair:interpret v2 env)  
               prec size)
             ]
            [(repair-reduce-add_dsl reduce-factor v1 prec size)
             (repair-reduce-add 
               reduce-factor
               (repair:interpret v1 env)  
               prec size)
             ]

            [(repair-max_dsl v1 v2 prec size)
             (repair-max 
               (repair:interpret v1 env)  
               (repair:interpret v2 env)  
               prec size)
             ]

            [(repair-min_dsl v1 v2 prec size)
             (repair-min 
               (repair:interpret v1 env)  
               (repair:interpret v2 env)  
               prec size)
             ]
            [(repair-sub_dsl v1 v2 prec size)
             (repair-sub 
               (repair:interpret v1 env)  
               (repair:interpret v2 env)  
               prec size)
             ]

            [(repair-sat-sub_dsl v1 v2 prec size)
             (repair-sat-sub 
               (repair:interpret v1 env)  
               (repair:interpret v2 env)  
               prec size)
             ]

            [(repair-mul_dsl v1 v2 prec size)
             (repair-mul 
               (repair:interpret v1 env)  
               (repair:interpret v2 env)  
               prec size)
             ]
            [(repair-sext_dsl v1  iprec oprec size)
             (repair-sext 
               (repair:interpret v1 env)  
               iprec oprec size)
             ]
            [(repair-extract-index_dsl v1  prec size index)
              (repair-extract-index 
               (repair:interpret v1 env)  
                prec size index)
             ]
            [(repair-widen-mul_dsl v1 v2 iprec oprec size)
             (repair-widen-mul 
               (repair:interpret v1 env)  
               (repair:interpret v2 env)  
               iprec oprec size)
             ]
            [_
              (println expr)
              (error "Unsupported op")
              ]
    )
  )
