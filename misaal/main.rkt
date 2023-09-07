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



(provide 


(all-from-out misaal/ir/halide/types)
(all-from-out misaal/ir/halide/length)
(all-from-out misaal/ir/halide/prec)
(all-from-out misaal/ir/halide/printer)
(all-from-out misaal/ir/halide/visitor)
(all-from-out misaal/ir/halide/interpreter)
(all-from-out misaal/ir/halide/get_ops)
(all-from-out misaal/ir/halide/cost_model)

  )
