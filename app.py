import os
import sys
import subprocess

current_file = os.path.basename(__file__)

for file in os.listdir("."):
    if file.endswith(".py") and file != current_file:
        print(f"Running {file}...")
        subprocess.run([sys.executable, file], check=True)