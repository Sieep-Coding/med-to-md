import subprocess, os

class Utility:
    def run_bash(filename):
        """Moves the file to the 'test' folder in the project root."""
        test_dir = "./output"
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)
        try:
            result = subprocess.run(["mv", filename, test_dir], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Moved '{filename}' to '{test_dir}/'")
            else:
                print(f"Error moving file: {result.stderr}")
        except Exception as e:
            print(f"Error running bash command: {e}")