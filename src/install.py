import runpy
import sys

# Guard against "import install" (nonsense, but would annoying to debug otherwise)
if __name__ != "__main__": raise Exception("install-is-pip-install is not a library")

# Try to avoid inadvertant propagation of incorrect commands into docs, etc.
print("NOTICE: You just used install-is-pip-install!", file=sys.stderr)

# patch up argv to resemble that of "python3 -m pip install"
sys.argv.insert(1, "install")
runpy.run_module("pip", run_name="__main__", alter_sys=True)
