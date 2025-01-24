#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require rosette/lib/destruct)
(require hydride/ir/hydride/definition)
(require rosette/solver/smt/boolector)
(require rosette/solver/smt/z3)



(provide (all-defined-out))



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
(define (param_abstract:contains-reg-leq prog index)
  (destruct prog
            [(reg id) (<= (bitvector->integer id) index)]
            [(SCALAR a) #f]
            [(ADD a b)
             (or (param_abstract:contains-reg-leq a index) (param_abstract:contains-reg-leq b index))
             ]
            [(SUB a b)
             (or (param_abstract:contains-reg-leq a index) (param_abstract:contains-reg-leq b index))
             ]
            [(MUL a b)
             (or (param_abstract:contains-reg-leq a index) (param_abstract:contains-reg-leq b index))
             ]
            [(DIV a b)
             (or (param_abstract:contains-reg-leq a index) (param_abstract:contains-reg-leq b index))
             ]
            [(MOD a b)
             (or (param_abstract:contains-reg-leq a index) (param_abstract:contains-reg-leq b index))
             ]
            [_ (error "Unrecognized term in param abstract contains-reg-leq")]
            )
  )

(define (param_abstract:exclude-reg prog index)
  (destruct prog
            [(reg id) (not (equal? (bitvector->integer id) index))]
            [(SCALAR a) #t]
            [(ADD a b)
             (and (param_abstract:exclude-reg a index) (param_abstract:exclude-reg b index))
             ]
            [(SUB a b)
             (and (param_abstract:exclude-reg a index) (param_abstract:exclude-reg b index))
             ]
            [(MUL a b)
             (and (param_abstract:exclude-reg a index) (param_abstract:exclude-reg b index))
             ]
            [(DIV a b)
             (and (param_abstract:exclude-reg a index) (param_abstract:exclude-reg b index))
             ]
            [(MOD a b)
             (and (param_abstract:exclude-reg a index) (param_abstract:exclude-reg b index))
             ]
            [_ (error "Unrecognized term in param abstract exclude-reg")]
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

(define (generate-exclude-reg-constraints expr-grammar exclude-regs)

  (define (helper i)
    (define exclude-case-i (list-ref exclude-regs i))
    (assert (param_abstract:exclude-reg expr-grammar exclude-case-i))
    )
  (define num-cex (length exclude-regs))
  ;; Build list of conditions
  (define assertions (build-list num-cex helper))
  assertions
  )

(define (synthesize-param-expression test-cases grammar-depth reg-leq exclude-regs)
  (define test-0 (list-ref test-cases 0))
  (define num-reg-inputs (vector-length (TESTS-input-values test-0)))
  (define grammar-generator (create-param-grammar num-reg-inputs))
  (define expr-grammar (grammar-generator grammar-depth))
  (define sol
    (optimize 
      #:minimize (list (param_abstract:cost expr-grammar))
      #:guarantee
      (begin
        (generate-constraints test-cases expr-grammar)
        (generate-exclude-reg-constraints expr-grammar exclude-regs)
        ;(assert (param_abstract:contains-reg-leq expr-grammar reg-leq))
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

