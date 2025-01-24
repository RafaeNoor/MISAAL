#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require rosette/lib/destruct)
(require hydride)
(require misaal)
(require rosette/solver/smt/boolector)
(require rosette/solver/smt/z3)

;; Uncomment the line below to enable verbose logging
(enable-debug)
(custodian-limit-memory (current-custodian) (* 10000 1024 1024))


;; Since you are synthesizing with integers in mind, I would keep the bitwidth
;; Atleast 32. 
(current-bitwidth 32)



;; Struct Defs

(struct SCALAR (a) #:transparent #:mutable)
(struct ADD (a b) #:transparent #:mutable)
(struct SUB (a b) #:transparent #:mutable)
(struct MUL (a b) #:transparent #:mutable)
(struct DIV (a b) #:transparent #:mutable)
(struct MOD (a b) #:transparent #:mutable)

;; Struct to represent test case for input and output values
(struct TESTS (output-value input-values)  #:transparent)

;; Cost Model
(define (param_abstract:cost prog)
  (destruct prog
            [(reg id) 1]
            [(SCALAR a) 1]
            [(ADD a b)
             (+ 1 (param_abstract:cost a) (param_abstract:cost b))
             ]
            [(SUB a b)
             (+ 1 (param_abstract:cost a) (param_abstract:cost b))
             ]
            [(MUL a b)
             (+ 1 (param_abstract:cost a) (param_abstract:cost b))
             ]
            [(DIV a b)
             (+ 1 (param_abstract:cost a) (param_abstract:cost b))
             ]
            [(MOD a b)
             (+ 1 (param_abstract:cost a) (param_abstract:cost b))
             ]
            [_ (error "Unrecognized term in param abstract cost")]
            )
  )

;; Interpreter
(define (param_abstract:interpret prog env)
  (destruct prog
            [(reg id) (vector-ref-bv env id)]
            [(SCALAR a) a]
            [(ADD a b)
             (+ (param_abstract:interpret a env) (param_abstract:interpret b env))
             ]
            [(SUB a b)
             (- (param_abstract:interpret a env) (param_abstract:interpret b env))
             ]
            [(MUL a b)
             (* (param_abstract:interpret a env) (param_abstract:interpret b env))
             ]
            [(DIV a b)
             (/ (param_abstract:interpret a env) (param_abstract:interpret b env))
             ]
            [(MOD a b)
             (remainder (param_abstract:interpret a env) (param_abstract:interpret b env))
             ]
            [_ (error "Unrecognized term in param abstract interpreter")]
            )
  )

;; Convert to String
(define (param_abstract:to-string prog)
  (destruct prog
            [(reg id) (format "reg_~a" (bitvector->natural id))]
            [(SCALAR a) (~s a)]
            [(ADD a b)
             (format "(+ ~a ~a)"   (param_abstract:to-string a) (param_abstract:to-string b) )
             ]
            [(SUB a b)
             (format "(- ~a ~a)"   (param_abstract:to-string a) (param_abstract:to-string b) )
             ]
            [(MUL a b)
             (format "(* ~a ~a)"   (param_abstract:to-string a) (param_abstract:to-string b) )
             ]
            [(DIV a b)
             (format "(/ ~a ~a)"   (param_abstract:to-string a) (param_abstract:to-string b) )
             ]
            [(MOD a b)
             (format "(% ~a ~a)"   (param_abstract:to-string a) (param_abstract:to-string b) )
             ]
            [_ (error "Unrecognized term in param abstract to string")]
            )
  )


(define (create-param-grammar num-regs)
  (define regs (build-list num-regs (lambda (x)   (reg (bv x 8)))))


  ;; Extend the grammar as needed
  (define-grammar  (param-grammar)
                   [expr_start (choose 
                                 (apply choose* regs)
                                 (SCALAR 1)
                                 (SCALAR 2)
                                 (ADD (expr_start) (expr_start))
                                 (MUL (expr_start) (expr_start))
                                 (SUB (expr_start) (expr_start))
                                 (DIV (expr_start) (expr_start))
                                 (MOD (expr_start) (expr_start))
                                 )
                               ]
                   )

  (define (grammar-fn k)
    (param-grammar #:depth k #:start expr_start)
    )
  grammar-fn
  )



(define (generate-constraints test-cases expr-grammar)

  (define (helper i)
    (define test-case-i (list-ref test-cases i))
    (define output-value-i (TESTS-output-value test-case-i))
    (define input-values-i (TESTS-input-values test-case-i))
    (assert (equal? (param_abstract:interpret  expr-grammar input-values-i) output-value-i))
    )
  (define num-cex (length test-cases))
  ;; Build list of conditions
  (define assertions (build-list num-cex helper))
  assertions
  )

(define (synthesize-param-expression test-cases grammar-depth)
  (define test-0 (list-ref test-cases 0))
  (define num-reg-inputs (vector-length (TESTS-input-values test-0)))
  (define grammar-generator (create-param-grammar num-reg-inputs))
  (define expr-grammar (grammar-generator grammar-depth))
  (define sol
    (optimize 
      #:minimize (list (param_abstract:cost expr-grammar))
      #:guarantee
      (begin
        (generate-constraints tests expr-grammar)
        )
      )
    )

  (cond 
    [(sat? sol)
     (values #t (evaluate expr-grammar sol))
     ]
    [else
      (values #f '())
      ]
    )
  )

;; Simple test 
(define test-0-inputs (vector 2 3))
(define test-0-output 7)
(define test-case-0 (TESTS test-0-output test-0-inputs))

(define test-1-inputs (vector 3 4))
(define test-1-output 9)
(define test-case-1 (TESTS test-1-output test-1-inputs))

;; Test cases is a list of TEST
(define tests (list test-case-0  test-case-1))


(define-values (satisfiable? expr)
  (synthesize-param-expression tests 2)
  )

(cond
  [satisfiable?
    (displayln "Expression exists")
    (pretty-print expr)
    (displayln (param_abstract:to-string expr))
    ]
  [else
    (displayln "No expression exists")
    ]

  )
