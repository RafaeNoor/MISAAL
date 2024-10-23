CUR_DIR=$(pwd)

export MISAAL_SRC=$CUR_DIR
export PYTHONPATH=${CUR_DIR}/lib/:$PYTHONPATH
export HALIDE_SRC=$CUR_DIR/frontends/halide
export HALIDE_DISTRIB=$HALIDE_SRC/distrib

