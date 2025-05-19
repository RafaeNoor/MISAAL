#!/bin/bash

export MISAAL_ROOT_DIR=$(pwd)

# --- Build Hydride ---
export HYDRIDE_DIR="${MISAAL_ROOT_DIR}/Hydride"

if [ ! -d "$HYDRIDE_DIR" ]; then
  echo "Cloning Hydride repository..."
  #git clone -b bitserial https://github.com/akothen/Hydride.git
  git submodule update Hydride
else
  echo "Hydride directory exists."
fi
cd $HYDRIDE_DIR
if [ -f setup.sh ]; then
  source ./setup.sh
else
  echo "Error: setup.sh not found in Hydride directory."
  exit 1
fi

echo "Installing Rosette ..."
echo cd $HYDRIDE_DIR/rosette
cd $HYDRIDE_DIR/rosette
echo raco pkg install
raco pkg install
echo "Rosette installed successfully."

### Install Hydride code synthesizer
echo "Installing Hydride code synthesizer ..."
echo cd $HYDRIDE_DIR/code-synthesizer
cd $HYDRIDE_DIR/code-synthesizer
echo raco pkg install hydride/
raco pkg install hydride/
echo "Hydride code synthesizer installed successfully."

echo "Hydride build complete."
echo ""

echo "Installing Halide frontend for MISAAL ..."
echo cd $MISAAL_ROOT_DIR/frontends/halide
cd $MISAAL_ROOT_DIR/frontends/halide
bash install.sh
echo "Halide frontend installed successfully."

# --- Build MISAAL ---
echo "Building MISAAL..."

if [ -z "${MISAAL_ROOT_DIR}" ]; then
  echo "Error: MISAAL_ROOT_DIR environment variable not set."
  echo "Please set MISAAL_ROOT_DIR to the location of the MISAAL repository."
  exit 1
fi

cd "${MISAAL_ROOT_DIR}"
if [ -f setup.sh ]; then
  source setup.sh
else
  echo "Error: setup.sh not found in MISAAL directory."
  exit 1
fi

echo "Installing Racket package for MISAAL..."
raco pkg install misaal/

echo "MISAAL build complete."
echo ""

# --- Build Other Dependencies ---
echo "Building Other Dependencies..."

# Egglog
export EGGLOG_DIR="${MISAAL_ROOT_DIR}/egglog"
echo "Building Egglog..."
if [ ! -d "$EGGLOG_DIR" ]; then
  echo "Cloning egglog repository..."
  git submodule update egglog
else
  echo "Egglog directory exists."
fi
cd egglog/
cargo install --locked cargo-nextest@0.9.85
cargo build
make test nits docs

echo "Egglog build complete."
echo ""

echo "All dependencies built successfully."