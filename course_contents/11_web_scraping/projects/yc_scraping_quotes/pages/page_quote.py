from bs4 import BeautifulSoup
from locators.page_locators import PageLocators



class PageQuote:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')


    # get all quotes
    @property
    def quotes(self):
        return self.soup.select(PageLocators.QUOTE) # Returns a list of quote elements


'''
    @property
    def quotes(self):
        return [QuoteParser(e) for e in self.soup.select(QuotesPageLocators.QUOTE)]
'''