import unittest
from unittest.mock import patch
import scraper

class TestScraperMethods(unittest.TestCase):
    @patch('scraper.requests.get')
    def test_fetch(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "<html><title>Test Article</title><article>Test content</article></html>"
        
        url = "https://medium.com/@nick-stambaugh/dynamic-arrays-in-c-fdc8a2f66b53"
        
        result = scraper.Scraper.fetch_medium_article(url)
        
        self.assertEqual(mock_get.call_count, 1) 
        mock_get.assert_called_with(url, headers={'User-Agent': unittest.mock.ANY})
        self.assertIn("<title>Test Article</title>", result)

if __name__ == "__main__":
    unittest.main()
