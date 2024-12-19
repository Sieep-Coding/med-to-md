import sys
import scraper, utils  # mine

def main():
    
    utils.Utility.arguments()
    
    url = sys.argv[1]
    print("Fetching...")
    html = scraper.Scraper.fetch_medium_article(url)
    print("Extracting...")
    title, article_content = scraper.Scraper.extract_title_and_content(html)
    print("Converting...")
    markdown_content = scraper.Scraper.convert_to_markdown(article_content)
    print("Saving...")
    file = utils.Utility.save_file(title, markdown_content)
    print("Running bash...")
    utils.Utility.run_bash(file)

if __name__ == "__main__":
    main()