#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)
(require rosette/solver/smt/boolector)

(require hydride/utils/bvops)
(require hydride/utils/misc)


(provide (all-defined-out))

(define (hexagon_V6_vshuffvdd_128B  Vu Vv Rt %vectsize %outerlanesize %laneoffset %innerlanesize %arg0 %arg1)
  (define Rt_int (bitvector->integer Rt))
  (define %elem_size (* (- 0 Rt_int) %arg0))
  (define Vdd
    (apply
      concat
      (for/list ([%outer.it (reverse (range 0 %vectsize %outerlanesize))])
                (apply
                  concat
                  (for/list ([%inner.it (reverse (range %laneoffset %innerlanesize %elem_size))])
                            (define %low %inner.it)
                            (define %high (+ %inner.it (- %elem_size 1)))
                            (define %a (extract  %high %low Vu))
                            (define %b (extract  %high %low Vv))
                            (concat %b %a)
                            )
                  )
                )
      )
    )
  (bvpadhighbits  Vdd %arg1)
  )

(define (hexagon_V6_vdealvdd_128B  Vu Vv Rt %vectsize %outerlanesize %laneoffset0 %innerlanesize0 %laneoffset1 %innerlanesize1 %laneoffset2 %innerlanesize2 %laneoffset3 %innerlanesize3 %arg0 %arg1 %arg2 %arg3 %arg4 %arg5)
  (define Rt_int (bitvector->integer Rt))
  (define %elem_size (* (- 0 Rt_int) %arg0))
  (define Vdd
    (apply
      concat
      (for/list ([%outer.it (reverse (range 0 %vectsize %outerlanesize))])
                (concat
                  (apply
                    concat
                    (for/list ([%inner.it.0 (reverse (range %laneoffset0 %innerlanesize0 %elem_size))])
                              (define %low.0 (+ %elem_size (* %arg1 %inner.it.0)))
                              (define %high.0 (+ %low.0 (- %elem_size 1)))
                              (define %ext.Vu.0 (extract  %high.0 %low.0 Vu))
                              %ext.Vu.0
                              )
                    )
                  (apply
                    concat
                    (for/list ([%inner.it.1 (reverse (range %laneoffset1 %innerlanesize1 %elem_size))])
                              (define %low.1 (+ %elem_size (* %arg2 %inner.it.1)))
                              (define %high.1 (+ %low.1 (- %elem_size 1)))
                              (define %ext.Vv.0 (extract  %high.1 %low.1 Vv))
                              %ext.Vv.0
                              )
                    )
                  (apply
                    concat
                    (for/list ([%inner.it.2 (reverse (range %laneoffset2 %innerlanesize2 %elem_size))])
                              (define %low.2 (* %arg3 %inner.it.2))
                              (define %high.2 (+ %low.2 (- %elem_size 1)))
                              (define %ext.Vu.1 (extract  %high.2 %low.2 Vu))
                              %ext.Vu.1
                              )
                    )
                  (apply
                    concat
                    (for/list ([%inner.it.3 (reverse (range %laneoffset3 %innerlanesize3 %elem_size))])
                              (define %low.3 (* %arg4 %inner.it.3))
                              (define %high.3 (+ %low.3 (- %elem_size 1)))
                              (define %ext.Vv.1 (extract  %high.3 %low.3 Vv))
                              %ext.Vv.1
                              )
                    )
                  )
                )
      )
    )
  (bvpadhighbits  Vdd %arg5)
  )