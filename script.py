import sys
import scraper, utils  # mine

def main():
    
    aScraper = scraper.Scraper
    aUtil = utils.Utility
    aUtil.arguments()

    url = sys.argv[1]
    print("Fetching...")
    html = aScraper.fetch_medium_article(url)
    print("Extracting...")
    title, article_content = aScraper.extract_title_and_content(html)
    print("Converting...")
    markdown_content = aScraper.convert_to_markdown(article_content)
    print("Saving...")
    file = aUtil.save_file(title, markdown_content)
    print("Running bash...")
    aUtil.run_bash(file)

if __name__ == "__main__":
    main()