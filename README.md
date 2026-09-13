# MISAAL

# Build Instructions

### Build Hydride
Note that Hydride needs to be built before building MISAAL repository
```
git clone -b bitserial https://github.com/akothen/Hydride.git
cd Hydride/
source setup.sh
cd code-synthesizer/
# Install racket package for Hydride, Note the backslash is necessary
raco pkg install hydride/
```

### Build MISAAL
```
cd ${MISAAL_ROOT_DIR}
source setup.sh
# Install racket package for MISAAL, Note the backslash is necessary
raco pkg install misaal/
```

### Build  Other Dependencies

#### Egglog
```
git clone https://github.com/egraphs-good/egglog.git
cd egglog/
apt-get install make cargo
cargo install cargo-nextest
make all
cargo build --release
export EGG_PKG_PATH=$(pwd)   # MISAAL runs $EGG_PKG_PATH/target/release/egglog
```

MISAAL looks for egglog in `$EGG_PKG_PATH`, then in an `egglog` checkout next to
this repository, then via an `egglog` binary on `PATH` (see `lib/utils/egg_config.py`).
