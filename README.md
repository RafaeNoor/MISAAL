# MISAAL

# Install

```bash
git clone --recurse-submodules git@github.com:RafaeNoor/MISAAL.git
```

``` Build legalizers (have LLVM 12 available on system for now)
cd Hydride/codegen-generator/tools/low-level-codegen
mkdir build && cd build
cmake ..
make
```

# Build from script

```bash
source install_misaal.sh
```

# Build Instructions (Manual)

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
```
