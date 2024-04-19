/home/baronia3/bin/racket -I rosette -e '
                    (require hydride/utils/bvops)
                    (require hydride/utils/misc)
                    (require hydride/ir/hvx/semantics)
                    (vec_d (integer->bitvector 1 (bitvector 1024)) 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0)'