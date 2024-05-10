;#============================== Hydride File =================================
;#
;# Part of the Hydride Compiler Infrastructure.
;# <Placeholder for license information>
;#
;#=============================================================================
;#
;# Do NOT modify this file. It is automatically generated.
;#
;#=============================================================================

#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require rosette/lib/destruct)

(require hydride/utils/bvops)
(require hydride/utils/misc)


(provide (all-defined-out))
;; ================================================================================
;;                                Struct Definitions
;; ================================================================================
(struct repair-add_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-bwand_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-bwnot_dsl (v0 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-bwor_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-cast-int_dsl (v0 prec_i prec_o size_i) #:transparent #:mutable)
(struct repair-cast-uint_dsl (v0 prec_i prec_o size_i) #:transparent #:mutable)
(struct repair-sabsd_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-saturate_dsl (v0 prec_i prec_o size_i bool_4) #:transparent #:mutable)
(struct repair-sdiv_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-shl_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-smax_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-smin_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-smod_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-smul_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-ssat-add_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-ssat-sub_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-sshr_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-sub_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-uabsd_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-udiv_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-umax_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-umin_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-umod_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-umul_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-usat-add_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-usat-sub_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-ushr_dsl (v0 v1 prec_i_o size_i_o) #:transparent #:mutable)
(struct repair-vector-reduce-add_dsl (num_0 v1 size_o size_i) #:transparent #:mutable)
;; ================================================================================

