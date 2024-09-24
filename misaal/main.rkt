#lang rosette

(module+ test
  (require rackunit))

;; Notice
;; To install (from within the package directory):
;;   $ raco pkg install
;; To install (once uploaded to pkgs.racket-lang.org):
;;   $ raco pkg install <<name>>
;; To uninstall:
;;   $ raco pkg remove <<name>>
;; To view documentation:
;;   $ raco docs <<name>>
;;
;; For your convenience, we have included LICENSE-MIT and LICENSE-APACHE files.
;; If you would prefer to use a different license, replace those files with the
;; desired license.
;;
;; Some users like to add a `private/` directory, place auxiliary files there,
;; and require them in `main.rkt`.
;;
;; See the current version of the racket style guide here:
;; http://docs.racket-lang.org/style/index.html

;; Code here



;; Typed Halide IR:

(require misaal/ir/halide/types)
(require misaal/ir/halide/length)
(require misaal/ir/halide/prec)
(require misaal/ir/halide/printer)
(require misaal/ir/halide/visitor)
(require misaal/ir/halide/interpreter)
(require misaal/ir/halide/get_ops)
(require misaal/ir/halide/cost_model)
(require misaal/ir/halide/utils)
(require misaal/ir/halide/semantics)


;; Typed Repair IR:


(require misaal/ir/repair/binder)
(require misaal/ir/repair/const_fold)
(require misaal/ir/repair/definition)
(require misaal/ir/repair/extract)
(require misaal/ir/repair/get_name)
(require misaal/ir/repair/get_ops)
(require misaal/ir/repair/sub_expr)
(require misaal/ir/repair/get_variants)
(require misaal/ir/repair/scale)
(require misaal/ir/repair/length)
(require misaal/ir/repair/prec)
(require misaal/ir/repair/printer)
(require misaal/ir/repair/visitor)
(require misaal/ir/repair/interpreter)
(require misaal/ir/repair/cost_model)
(require misaal/ir/repair/semantics)


;; Synthesis Utilities

(require misaal/synthesis/ir_to_ir_transform)
(require misaal/synthesis/iterative_synthesis_v2)
(require misaal/synthesis/expanded_grammar_iterative_synthesis)
(require misaal/synthesis/target_desc)
(require misaal/synthesis/grammar_utils)


(provide 


(all-from-out misaal/ir/halide/types)
(all-from-out misaal/ir/halide/length)
(all-from-out misaal/ir/halide/prec)
(all-from-out misaal/ir/halide/printer)
(all-from-out misaal/ir/halide/visitor)
(all-from-out misaal/ir/halide/interpreter)
(all-from-out misaal/ir/halide/get_ops)
(all-from-out misaal/ir/halide/cost_model)
(all-from-out misaal/ir/halide/utils)
(all-from-out misaal/ir/halide/semantics)


(all-from-out  misaal/ir/repair/binder)
(all-from-out  misaal/ir/repair/const_fold)
(all-from-out  misaal/ir/repair/definition)
(all-from-out  misaal/ir/repair/extract)
(all-from-out  misaal/ir/repair/get_name)
(all-from-out  misaal/ir/repair/get_ops)
(all-from-out  misaal/ir/repair/sub_expr)
(all-from-out  misaal/ir/repair/get_variants)
(all-from-out  misaal/ir/repair/scale)
(all-from-out  misaal/ir/repair/length)
(all-from-out  misaal/ir/repair/prec)
(all-from-out  misaal/ir/repair/printer)
(all-from-out  misaal/ir/repair/visitor)
(all-from-out  misaal/ir/repair/interpreter)
(all-from-out  misaal/ir/repair/cost_model)
(all-from-out  misaal/ir/repair/semantics)




(all-from-out misaal/synthesis/expanded_grammar_iterative_synthesis)
(all-from-out misaal/synthesis/iterative_synthesis_v2)
(all-from-out misaal/synthesis/ir_to_ir_transform)
(all-from-out misaal/synthesis/target_desc)
(all-from-out misaal/synthesis/grammar_utils)

  )
