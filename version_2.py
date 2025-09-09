
import subprocess

files = [
    r"C:\Users\pc\OneDrive\Desktop\subprocess\script1.py",
    r"C:\Users\pc\OneDrive\Desktop\subprocess\script2.py"
]

python_path = "python"

for file in files:
    print(f"Running {file}..\n{'='*30}")

    process = subprocess.Popen(
        ["python", "-u", file],  # Real-time output using -u
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    for line in process.stdout:
        print(line, end='')
    process.wait()
    print(f"\n{'='*30}\nDone running {file}\n")
    
