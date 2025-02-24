from selenium.webdriver.common.by import By
from locators.quote_locators import QuoteLocators

class QuoteParser:
    def __init__(self, element):
        self.element = element  # WebElement from Selenium
    
    @property
    def content(self):
        return self.element.find_element(By.CSS_SELECTOR, QuoteLocators.CONTENT_LOCATOR).text
    
    @property
    def author(self):
        return self.element.find_element(By.CSS_SELECTOR, QuoteLocators.AUTHOR_LOCATOR).text
    
    @property
    def tags(self):
        return [t.text for t in self.element.find_elements(By.CSS_SELECTOR, QuoteLocators.TAGS_LOCATOR)]
    
    def __repr__(self):
        return f'"{self.content}" by {self.author} (Tags: {", ".join(self.tags)})'
    
class AspxParser:
    def __init__(self, element):
        self.element = element

        
    @property
    def aspx_content(self):
        return self.element.find_element(By.CSS_SELECTOR, QuoteLocators.QUOTE_CONTENT).text
    
    @property
    def aspx_author(self):
        return self.element.find_element(By.CSS_SELECTOR, QuoteLocators.QUOTE_AUTHOR).text
    
    @property
    def aspx_tags(self):
        return [t.text for t in self.element.find_elements(By.CSS_SELECTOR, QuoteLocators.QUOTE_TAG)]
    
    def __repr__(self):
        return f"<Quote {self.aspx_content}, by {self.aspx_author}>"
    
    
    