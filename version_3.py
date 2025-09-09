
import subprocess

files = [
    r"C:\Users\pc\OneDrive\Desktop\subprocess\script1.py",
    r"C:\Users\pc\OneDrive\Desktop\subprocess\script2.py"
]

python_path = "python"

for file in files:
    print(f"Running {file}..\n{'='*30}")
    
    try:
        process = subprocess.Popen(
            ["python", "-u", file],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        for line in process.stdout:
            print(line, end='')

        exit_code = process.wait()

        if exit_code != 0:
            print(f"\n❌ Script failed with exit code {exit_code}: {file}\n")
        else:
            print(f"\n✅ Done running {file}\n")

    except Exception as e:
        print(f"\n❗ Exception while running {file}: {e}\n")

    print("="*30 + "\n")
    
