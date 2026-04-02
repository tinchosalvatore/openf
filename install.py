import subprocess
import sys
import os

def install():
    print("Installing openf command...")
    try:
        # Install the package from the current directory
        subprocess.check_call([sys.executable, "-m", "pip", "install", "."])
        print("\nSuccessfully installed! You can now use the command 'openf'.")
    except Exception as e:
        print(f"\nInstallation failed: {str(e)}")

if __name__ == "__main__":
    install()
