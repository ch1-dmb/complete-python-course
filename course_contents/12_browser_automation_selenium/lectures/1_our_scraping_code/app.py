# app.py
import logging
from selenium import webdriver
from pages.quotes_page import QuotesPage

logging.basicConfig(level=logging.DEBUG, filename='logs.txt', filemode='w')


logger = logging.getLogger(__name__)
chrome = webdriver.Chrome()
website = 'http://quotes.toscrape.com'
def scrape_the_main_pages():

    chrome.get(website)
    page = QuotesPage(chrome)  # Pass WebDriver

    for quote in page.quotes:
        print(quote)

def interact_with_dropdown():
   
    # page.get_author(author)
    chrome.get(website + '/search.aspx')
    page = QuotesPage(chrome)
    author = str(input('Enter the author u like to quote from: '))
    selected_tag = input("Enter your tag: ")
    print(page.search_results(author, selected_tag))
    
    # tags = page.get_available_tags()
    # print("Select one of these tags: [{}]".format(" | ".join(tags)))
    # page.get_tag(selected_tag)
    # page.click_search()
    # print(page.aspx_quotes)


    # logger.debug(f"Attempting to select author: {author}")
    # try:
    #     page.get_author(author)
    #     logger.info("Author selected successfully")
    # except Exception as e:
    #     logger.error(f"Failed to select author: {e}")
    # for quote in page.quotes:
    #     print(quote)

interact_with_dropdown()
