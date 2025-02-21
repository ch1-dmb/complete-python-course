
import requests

from pages.quotes_page import QuotesPage
from parsers.quote import QuoteParser


web_content = requests.get('http://quotes.toscrape.com').content
extract_content = QuotesPage(web_content)

# for i in extract_content.quotes:
#     print(i)
extract_info={
    "content": QuoteParser.get_content,
    "author": QuoteParser.get_author,
    "tags": QuoteParser.get_tags
}
# print(extract_info)
