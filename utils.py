import subprocess, os, sys

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

    def save_file(title, markdown_content):
        """Saves the Markdown content to a .md file and returns the file path."""
        safe_title = "".join(c for c in title if c.isalnum() or c in " -_").rstrip()
        filename = f"{safe_title}.md"
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(markdown_content)
            print(f"Article saved as '{filename}'")
            return filename
        except Exception as e:
            print(f"Error saving file: {e}")
            return None
        
    def arguments():
        if len(sys.argv) != 2:
            print("Usage: python3 script.py <url to Medium article>")
            sys.exit(1)