#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require rosette/lib/destruct)
(require rosette/solver/smt/boolector)
(require rosette/solver/smt/z3)






(require hydride/halide)


(provide (all-defined-out))

(struct target-desc (interpreter cost-fn visitor length-fn prec-fn get-ops-fn sema-path dict-name) #:transparent)


