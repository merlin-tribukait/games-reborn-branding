import sys
import subprocess
print("Executable:", sys.executable)
print("Version:", sys.version)

subprocess.run([sys.executable, "-m", "pip", "install", "vtracer"])
try:
    import vtracer
    print("vtracer loaded successfully!")
    print(dir(vtracer))
except Exception as e:
    print("Error:", e)
