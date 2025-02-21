from bs4 import BeautifulSoup

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')
# this wont work due to the QuoteParser will not have instance for it, so please refer to folder: yc_scraping to find better solutions
    @property
    def quotes(self):
        return [QuoteParser(e) for e in self.soup.select(QuotesPageLocators.QUOTE)]
