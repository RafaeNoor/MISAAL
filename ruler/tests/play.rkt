#lang rosette
(require hydride/utils/bvops)
(require hydride/utils/misc)
(require hydride/ir/hvx/semantics)

;; (for/list ([%i (range 0 8 1)]) 
;;     (bitvector->integer (extract (* (+ %i 1) 127) (* %i 128) (hexagon_V6_vdealb_128B (integer->bitvector -170141183460469231731687303715884105727 (bitvector 1024)) 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0)))
;; )

(define-symbolic i (bitvector 1024))

(assert (bveq (hexagon_V6_vshuffh_128B (hexagon_V6_vdealb_128B i 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0) 1024 16 0 16 8 16 8 0)
i ) )
(vc-asserts (vc))

;; (hexagon_V6_vdealb_128B (hexagon_V6_vshuffh_128B (concat (integer->bitvector 0 (bitvector 128)) (integer->bitvector 0 (bitvector 128)) (integer->bitvector 0 (bitvector 128)) (integer->bitvector 0 (bitvector 128)) (integer->bitvector 0 (bitvector 128)) (integer->bitvector 0 (bitvector 128)) (integer->bitvector 0 (bitvector 128)) (integer->bitvector 0 (bitvector 128)) ) 1024 16 0 16 8 16 8 0) 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0)
;; (for/list ([%i (range 0 8 1)]) 
;;     (bitvector->integer (extract (* (+ %i 1) 127) (* %i 128) (hexagon_V6_vdealb_128B (bv #x00ff00ff67ff00ff00ff00ff00ff00ff45ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff43ff00ff 1024) 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0)))
;; ) 