#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require rosette/lib/destruct)
(require hydride/utils/bvops)
(require hydride/utils/debug)
(require hydride/utils/misc)
(require hydride/synthesis/synth_main)
(require hydride/synthesis/python)
(require hydride/synthesis/spec_utils)



(require misaal/synthesis/target_desc)



(provide (all-defined-out))
(define MISAAL_SRC "/home/arnoor2/MISAAL/");(getenv "MISAAL_SRC"))
(define MISAAL_LIB_PATH (if (equal? MISAAL_SRC #f) (error "MISAAL_SRC is undefined!") (string-append MISAAL_SRC "/lib/" )))
(define MISAAL-GEN-GRAMMAR-SCRIPT-NAME "generate_grammar.py")
(define MISAAL-GEN-GRAMMAR-SCRIPT (string-append MISAAL_LIB_PATH MISAAL-GEN-GRAMMAR-SCRIPT-NAME))


(define (generate-grammar-file-step-misaal grammar-spec grammar-file-name base_name VF is_shuffle step-idx depth scale-factor synth-target-desc)
  (define target-str
    "misaal"
    
    )


;  --spec_name SPEC_NAME
; --output_path OUTPUT_PATH
;  --VF VF
;  --is_shuffle IS_SHUFFLE
;  --scale_factor SCALE_FACTOR
;  --step STEP
;  --depth DEPTH
;  --target_dict TARGET_DICT
;  --dict_name DICT_NAME

  (define spec-file-name (string-append "/tmp/" base_name "_spec.JSON"))
  (write-str-to-file grammar-spec spec-file-name)
  (define gen-grammar-cmd (string-append PYTHON " " MISAAL-GEN-GRAMMAR-SCRIPT " --spec_name " spec-file-name " --output_path " (path->string grammar-file-name) " --VF  " (~s VF) " --is_shuffle " (~s is_shuffle)  " --step " (~s step-idx) " --depth " (~s depth) " --scale_factor " (~s scale-factor) " --target_dict " (~s (target-desc-sema-path synth-target-desc))  " --dict_name " (~s  (target-desc-dict-name synth-target-desc) ) " > /dev/null 2>&1" ))
  (debug-log gen-grammar-cmd)
  (system gen-grammar-cmd)
  )

(define (get-expr-grammar-step-misaal expr  base_name get-ops-functor visitor-functor 
                                       get-length-functor get-prec-functor
                                       input-precs input-sizes input-signedness VF step-idx depth scale-factor
                                       synth-target-desc)

  (debug-log (format "get-expr-grammar-misaal (step-wise synthesis) with base_name: ~a\n" base_name))

  (define spec-contents (gen-synthesis-spec-hydride expr get-ops-functor visitor-functor get-length-functor get-prec-functor input-precs input-sizes input-signedness  base_name))
  (define grammar-file-name (string-append base_name "_grammar.rkt"))
  (debug-log grammar-file-name)
  (define mod-path (build-path gen (string->path grammar-file-name)))
  (debug-log mod-path)
  (generate-grammar-file-step-misaal spec-contents mod-path base_name VF 0 step-idx depth scale-factor synth-target-desc) ;; IS_SHUFFLE = 0
  (debug-log "Generated Grammar File")
  (define (get-grammar mod name)
    (debug-log (format "Dynamically importing from ~a ... \n" name))
    (dynamic-require mod (string->symbol name))
    )

  (define grammar (get-grammar mod-path (string-append base_name "")))
  (define interpreter (get-grammar mod-path (string-append base_name ":interpret")))
  (define cost-model (get-grammar mod-path (string-append base_name ":cost")))
  (values grammar interpreter cost-model)
  )



(define (assert-non-zero-env env)
  (for/list ([i (range (vector-length env))])
            (define value (vector-ref env i))
            (cond 
              [(symbolic? value)
               (assert (not (equal? value (bv 0 (bitvector (bvlength value))))))
               ]
              )
            )
  )
