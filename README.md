# MISAAL

# Dependencies

## Prerequisites

### Clang 12+

### Python
- Install [Python](https://www.python.org/downloads/) > 3.0.

### Z3
- Install [z3](https://github.com/Z3Prover/z3):
    - MacOS: `brew install z3`
    - Linux example: `sudo apt-get install -y z3`

### Racket 
- Install [Racket](https://download.racket-lang.org/)
    - Linux example (works for all versions of Racket): 
    ```bash
    wget https://download.racket-lang.org/installers/8.17/racket-8.17-x86_64-linux-cs.sh
    sh racket-8.17-x86_64-linux-cs.sh
    ```
### Rust + Cargo

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

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

# Build from script and setup paths

```bash
chmod +x install_misaal.sh
./install_misaal.sh
source setup.sh
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
