"""Where MISAAL finds egglog, the equality-saturation engine.

EggLogCompiler runs <EGG_PKG_PATH>/target/release/egglog, so EGG_PKG_PATH must be
an egglog source checkout built with `cargo build --release`.

Resolution order:
  1. the EGG_PKG_PATH environment variable
  2. an `egglog` checkout next to this MISAAL checkout (the PIM-AutoDSE layout,
     where MISAAL/ and egglog/ are sibling submodules)
  3. the checkout that contains an `egglog` binary found on PATH

If nothing is found, EGG_PKG_PATH is None and EggLogCompiler raises an error
explaining how to set it.
"""
import os
import shutil


def _is_built_checkout(path):
    return bool(path) and os.path.isfile(os.path.join(path, "target", "release", "egglog"))


def _find_egg_pkg_path():
    env = os.environ.get("EGG_PKG_PATH")
    if env:
        return os.path.abspath(os.path.expanduser(env))

    misaal_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    sibling = os.path.join(os.path.dirname(misaal_root), "egglog")
    if _is_built_checkout(sibling):
        return sibling

    exe = shutil.which("egglog")
    if exe:
        # <checkout>/target/release/egglog
        candidate = os.path.abspath(os.path.join(os.path.realpath(exe), "..", "..", ".."))
        if _is_built_checkout(candidate):
            return candidate

    return None


EGG_PKG_PATH = _find_egg_pkg_path()
