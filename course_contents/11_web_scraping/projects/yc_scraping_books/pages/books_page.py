
import re
import logging
from bs4 import BeautifulSoup
from locators.all_books_page import AllBooksPageLocators
from parsers.books_parsers import BooksParsers

logger = logging.getLogger('scraping.books_page')

class BooksPage:
    # connect the page which has all book per page
    def __init__(self, soup):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(soup, 'html.parser')

    @property
    def get_books(self):
        logger.debug(f'Finding all books in the page using `{AllBooksPageLocators.BOOKS}`')
        # return self.soup.select(AllBooksPageLocators.BOOKS)
        return [BooksParsers(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    
    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages available...')
        # get text and make sure there is no space
        content = self.soup.select_one(AllBooksPageLocators.PAGE).text.strip()
        # print(content)
        # current_page_element.get_text(strip=True)
        pattern = re.search('Page [0-9]+ of ([0-9]+)', content)
        # pattern = re.search(r'Page (\d+) of (\d+)', content)
        # # print(pattern.group(1))
        # if pattern:
        #     page_num = pattern.group(2)
        #     return int(page_num)

        pages = int(pattern.group(1))
        logger.info(f'Extracted number of pages as integer: `{pages}`.')

        return pages
        
