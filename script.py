import requests
from bs4 import BeautifulSoup
import html2text
import sys
import subprocess
import os

def fetch_medium_article(url):
    """Fetches a medium article."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching article: {e}")
        sys.exit(1)

def extract_title_and_content(html):
    """Extracts the title and content from Medium article HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    title_tag = soup.find("title")
    title = title_tag.text if title_tag else "Untitled"
    article_content = soup.find("article")
    if not article_content:
        print("Could not find content.")
        sys.exit(1)
    return title, article_content

def convert_to_markdown(html_content):
    markdown_converter = html2text.HTML2Text()
    markdown_converter.ignore_links = False
    markdown_converter.ignore_images = False
    return markdown_converter.handle(str(html_content))

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

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <url to Medium article>")
        sys.exit(1)
    
    url = sys.argv[1]
    print("Fetching...")
    html = fetch_medium_article(url)
    print("Extracting...")
    title, article_content = extract_title_and_content(html)
    print("Converting...")
    markdown_content = convert_to_markdown(article_content)
    print("Saving...")
    file = save_file(title, markdown_content)
    print("Running bash...")
    run_bash(file)

if __name__ == "__main__":
    main()