import requests
import logging
import time
# from bs4 import BeautifulSoup
# from locators.all_books_page import AllBooksPageLocators
from pages.books_page import BooksPage
# from parsers.books_parsers import BooksParsers


# implementing logging system

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='yc_logs.txt')
logger = logging.getLogger('scraping')

logger.info('lets start load it')

logger.info('request the website and load the content')
web_link = requests.get("http://books.toscrape.com/").content


logger.debug('Creating AllBooksPage from page content.')
web = BooksPage(web_link)

# this will get book on the first page(main page)
# books = web.get_books
# print(f"Found {len(books)} books")
# print(books[0])

# use the variable to collect those books
_book_list = []
# get the toal of pages(int), and try to get all books info from each page

start = time.time()
logger.info(f'lets go through those {web.page_count} pages now at {start}')
for i in range(web.page_count):
    page_start = time.time()
    url = f'http://books.toscrape.com/catalogue/page-{i+1}.html'
    logger.info(f'Requesting {url}')

    logger.debug('Receive from page content.')
    page_link = requests.get(url).content
    page_content = BooksPage(page_link)
    print(f'{url} took {time.time() - page_start}')
    _book_list.extend(page_content.get_books)
print(f'Total took {time.time9-start}')
logger.info(f'Total took {time.time9-start}')

books = _book_list

    





