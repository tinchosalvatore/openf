import subprocess
import sys

def uninstall():
    print("Uninstalling openf command...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "openf"])
        print("\nopenf has been uninstalled.")
    except Exception as e:
        print(f"\nUninstallation failed: {str(e)}")

if __name__ == "__main__":
    uninstall()
