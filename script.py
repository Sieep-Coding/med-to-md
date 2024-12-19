import html2text
import sys

import scraper, utils

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

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <url to Medium article>")
        sys.exit(1)
    
    url = sys.argv[1]
    print("Fetching...")
    html = scraper.Scraper.fetch_medium_article(url)
    print("Extracting...")
    title, article_content = scraper.Scraper.extract_title_and_content(html)
    print("Converting...")
    markdown_content = convert_to_markdown(article_content)
    print("Saving...")
    file = save_file(title, markdown_content)
    print("Running bash...")
    utils.Utility.run_bash(file)

if __name__ == "__main__":
    main()