import requests
from bs4 import BeautifulSoup
import sys
import html2text

class Scraper():
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
        """Uses html2text to convert html to markdown."""
        markdown_converter = html2text.HTML2Text()
        markdown_converter.ignore_links = False
        markdown_converter.ignore_images = False
        return markdown_converter.handle(str(html_content))