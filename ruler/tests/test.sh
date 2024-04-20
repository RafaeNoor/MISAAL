/home/baronia3/bin/racket -I rosette -e '
                (require hydride/utils/bvops)
                (require hydride/utils/misc)
                (require hydride/ir/hvx/semantics)

                (for/list ([%i (range 0 8 1)]) 
                    (bitvector->integer (extract (* (+ %i 1) 127) (* %i 128) (hexagon_V6_vdealb_128B (bv #x00ff00ff67ff00ff00ff00ff00ff00ff45ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff43ff00ff 1024) 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0)))
                )
'