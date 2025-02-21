import requests
from bs4 import BeautifulSoup


CONTENT_LOCATOR = 'div.quote span.text'
AUTHOR_LOCATOR = 'small.author'
TAGS_LOCATOR = 'div.tags a.tag'
QUOTE = 'div.quote'



# get the first quote
def fetch_page():
    page = requests.get("https://quotes.toscrape.com/").content
    return BeautifulSoup(page, 'html.parser')
#get the first quote    
def first_quote():
    soup = fetch_page()
    
    return soup.select_one(QUOTE)


# get content
def get_content():
    first_soup = first_quote()
    return first_soup.select_one(CONTENT_LOCATOR).text

# # get author

def get_author():
    first_soup = first_quote()
    return first_soup.select_one(AUTHOR_LOCATOR).text

# # get tags
def get_tags():
    first_soup = first_quote()
    return [i.text for i in first_soup.select(TAGS_LOCATOR)]


# print(first_quote())
print(get_content())
print(get_author())
print(get_tags())



'''
import requests
from bs4 import BeautifulSoup

# CSS Selectors
CONTENT_LOCATOR = 'div.quote span.text'
AUTHOR_LOCATOR = 'small.author'
TAGS_LOCATOR = 'div.tags a.tag'

# Function to fetch and parse the page
def fetch_page():
    page = requests.get("https://quotes.toscrape.com/").content
    return BeautifulSoup(page, 'html.parser')  # ✅ Return parsed soup

# Function to get the first quote
def first_quote():
    soup = fetch_page()  # ✅ Now returns BeautifulSoup object
    return soup.select_one("div.quote")  # ✅ Selecting the first quote div

# Get content from a quote
def get_content(quote):
    return quote.select_one(CONTENT_LOCATOR).text.strip()  # ✅ Extract text properly

# Get author from a quote
def get_author(quote):
    return quote.select_one(AUTHOR_LOCATOR).text.strip()

# Get tags from a quote
def get_tags(quote):
    return [tag.text for tag in quote.select(TAGS_LOCATOR)]  # ✅ Extract all tags as a list

# Fetch and process the first quote
quote = first_quote()
print("Quote:", get_content(quote))
print("Author:", get_author(quote))
print("Tags:", get_tags(quote))

'''


