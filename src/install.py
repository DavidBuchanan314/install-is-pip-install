import runpy
import sys

if __name__ == "__main__":
	# Guard against unintended use
	print("NOTICE: You just used install-is-pip-install!", file=sys.stderr)

	# Guard against use in scripts
	if not (sys.stdin.isatty() and sys.stdout.isatty()):
		raise Exception(
			"install-is-pip-install cannot be invoked from a non-TTY session"
		)

	# patch up argv to resemble that of "python3 -m pip install"
	sys.argv.insert(1, "install")
	runpy.run_module("pip", run_name="__main__", alter_sys=True)
