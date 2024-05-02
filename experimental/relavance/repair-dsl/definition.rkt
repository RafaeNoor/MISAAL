#lang rosette/safe

(require
  (only-in racket/struct make-constructor-style-printer)
  (only-in racket/base error)
  rosette/lib/destruct)


(provide (all-defined-out))

(struct repair-add_dsl (v1 v2 prec size) #:transparent #:mutable)
(struct repair-reduce-add_dsl (reduce-factor v1  prec size) #:transparent #:mutable)
(struct repair-sub_dsl (v1 v2 prec size) #:transparent #:mutable)
(struct repair-sat-add_dsl (v1 v2 prec size) #:transparent #:mutable)
(struct repair-sat-sub_dsl (v1 v2 prec size) #:transparent #:mutable)
(struct repair-mul_dsl (v1 v2 prec size) #:transparent #:mutable)
(struct repair-widen-mul_dsl (v1 v2 iprec oprec size) #:transparent #:mutable)
(struct repair-sext_dsl (v1  iprec oprec size) #:transparent #:mutable)
(struct repair-extract-index_dsl (v1  prec size index) #:transparent #:mutable)
(struct repair-build-vector_dsl (num-ele indices) #:transparent #:mutable)
(struct repair-max_dsl (v1 v2 prec size) #:transparent #:mutable)
(struct repair-min_dsl (v1 v2 prec size) #:transparent #:mutable)
         
