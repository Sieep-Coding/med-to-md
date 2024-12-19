import requests
from bs4 import BeautifulSoup
import html2text
import sys
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
