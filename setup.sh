CUR_DIR=$(pwd)

export MISAAL_SRC=$CUR_DIR
export PYTHONPATH=${CUR_DIR}/lib/:$PYTHONPATH
export EXPR_DIR=${CUR_DIR}/ruler/tests/misaal_exprs/
export HALIDE_SRC=$CUR_DIR/frontends/halide
export HALIDE_DISTRIB=$HALIDE_SRC/distrib

