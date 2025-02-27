import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from typing import List
from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser, AspxParser





class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def aspx_quotes(self) -> List[AspxParser]:
        return [
            AspxParser(e)
            for e in self.browser.find_elements(
                By.CSS_SELECTOR, QuotesPageLocators.QUOTE
            )]
    @property
    def quotes(self) -> List[QuoteParser]:
        return [
            QuoteParser(e)
            for e in self.browser.find_elements(
                By.CSS_SELECTOR, QuotesPageLocators.QUOTE
            )]
    @property
    def authors_drop_down(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotesPageLocators.AUTHOR_DROPDOWN
            )
        return Select(element)
    
    @property
    def search_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, QuotesPageLocators.SEARCH)
    

    @property
    def tags_drop_down(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotesPageLocators.TAG_DROPDOWN
            )
        return Select(element)

    def get_author(self, author_name: str):
        self.authors_drop_down.select_by_visible_text(author_name)

    def get_tag(self, tag: str):
        self.tags_drop_down.select_by_visible_text(tag)
    
    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tags_drop_down.options]
    
    # def click_search(self):
    #     self.search_button.click()

    def search_results(self, author_name: str, tag_name: str) -> List[AspxParser]:
        self.get_author(author_name)
        # Wait for tag dropdown options to load
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, QuotesPageLocators.TAG_DROPDOWN_OPTION))
        )
        # ... rest of the method
        try:
            # Check if tag is valid for author
            available_tags = self.get_available_tags()
            if tag_name not in available_tags:
                raise InvalidTagForAuthorError(f"Author '{author_name}' does not have any quotes tagged with '{tag_name}'.")
            self.get_tag(tag_name)
            self.search_button.click()
            # Wait for results to load (adjust locator as needed)
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, QuotesPageLocators.SEARCH))
            )
            return self.aspx_quotes
        except InvalidTagForAuthorError as e:
            print(e)
            return []
        except Exception as e:
            print(f"Error during search: {e}")
            return []

class InvalidTagForAuthorError(ValueError):
    pass
'''
BeautifulSoup tries to parse it, but chrome isn’t HTML—it’s a browser controller. Hence the TypeError.
'''

'''
try:
    # Code that might fail
    result = some_operation()
except Exception as e:
    # Raise a new error
    raise RuntimeError(f"Failed because: {e}")
'''