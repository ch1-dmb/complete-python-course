
import requests

from pages.page_quote import PageQuote
from parsers.all_parsers import QuoteParsers


web_content = requests.get('http://quotes.toscrape.com').content
extract_content = PageQuote(web_content)
# first_quote = extract_content.quotes[0]
info = QuoteParsers(extract_content.quotes[0])

# for i in extract_content.quotes:
#     print(i)
extract_info={
    "content": info.get_content,
    "author": info.get_author,
    "tags": info.get_tags
}
print(extract_info)

