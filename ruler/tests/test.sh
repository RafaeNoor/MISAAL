#/home/baronia3/bin/racket -I rosette -e '
#                (require hydride/utils/bvops)
#                (require hydride/utils/misc)
#                (require hydride/ir/hvx/semantics)
#
#                (for/list ([%i (range 0 8 1)]) 
#                    (bitvector->integer (extract (* (+ %i 1) 127) (* %i 128) (hexagon_V6_vdealb_128B (bv #x00ff00ff67ff00ff00ff00ff00ff00ff45ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff43ff00ff 1024) 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0)))
#                )
#'
#
#
#rm -f hvx_out.txt && cargo test --package ruler --test hvx -- test::compare --exact --show-output &> hvx_out.txt
#
#
#
#rm -rf /home/baronia3/new-MISAAL/MISAAL/ruler/tests/misaal_exprs/* && time cargo test --package ruler --test misaal_gen_test -- test::run --exact --show-output
#
#/home/baronia3/bin/racket -I rosette -e '
#                        (require hydride/utils/bvops)
#                        (require hydride/utils/misc)
#                        (require hydride/ir/hvx/semantics)
#                        (define-symbolic i (bitvector 1024))
#                        (verify (assert (bveq i (bvnot (hexagon_V6_vshuffh_128B (hexagon_V6_vdealb_128B i 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0) 1024 16 0 16 8 16 8 0)))))'
#
#
#/home/baronia3/bin/racket -I rosette -e '
#                        (require hydride/utils/bvops)
#                        (require hydride/utils/misc)
#                        (require hydride/ir/hvx/semantics)
#                        (define-symbolic i (bitvector 1024))
#                        (verify (assert (bveq i (hexagon_V6_vshuffh_128B (hexagon_V6_vdealb_128B i 1024 1024 0 512 8 0 512 8 2 64 8 2 8 0) 1024 16 0 16 8 16 8 0))))'                        
#

rm -f misaal_out.txt tests/misaal_exprs/misaal_log.expr nohup.out && nohup time cargo run --package ruler misaal_test_gen &> misaal_out.txt