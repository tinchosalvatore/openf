import os
import sys
import subprocess

def open_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    if sys.platform == "win32":
        # Windows
        os.startfile(file_path)
    elif sys.platform == "darwin":
        # macOS
        subprocess.call(["open", file_path])
    else:
        # Linux (and others)
        subprocess.call(["xdg-open", file_path])

def main():
    if len(sys.argv) < 2:
        print("Usage: openf <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    open_file(file_path)

if __name__ == "__main__":
    main()
