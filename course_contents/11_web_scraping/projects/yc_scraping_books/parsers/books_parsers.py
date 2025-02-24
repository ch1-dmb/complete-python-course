import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')

class BooksParsers:
    """
    A class to take in an HTML page or content, and find properties of an item
    in it.
    """
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, boss):
        logger.debug(f'New book parser created from `{boss}`')
        self.boss = boss

    def __repr__(self):
       return f'<Book {self.name} {self.price}, {self.rating} stars>'

    #get book name
    @property
    def name(self):
       logger.debug('Finding book name...')
       locators = BookLocators.NAME_LOCATOR
       book_name = self.boss.select_one(locators).attrs['title']
       logger.info(f'Found book name, `{item_name}`.')
       return book_name
      

   #get link
    @property
    def link(self):
       logger.debug('Finding book page link...')
       locators = BookLocators.LINK_LOCATOR
       link_name = self.boss.select_one(locators).attrs['href']
       pattern = r"catalogue/([a-zA-Z\-_]+)\d+\/index\.html"
       matcher = re.search(pattern, link_name)
       logger.info(f'Found book page link, `{link_name}`.')
       return matcher.group(1) if matcher else None

   # how much for the specific book 
    @property
    def price(self):
       logger.debug('Finding book price...')
       locators = BookLocators.PRICE_LOCATOR
       price_name = self.boss.select_one(locators).text
       logger.debug(f'Item price element found, `{price_name}`')
       pattern = r"£(\d+(?:\.\d{2})?)"
       matcher = re.search(pattern, price_name)
       logger.info(f'Found book price, `{matcher.group(1)}`.')

       return float(matcher.group(1)) if matcher else None
 

   #  whats the rating of this book?
    @property
    # use next, filter to find rating
    def rating(self):
       logger.debug('Finding book rating...')
       locators = BookLocators.RATING_LOCATOR
       rating = self.boss.select_one(locators).attrs['class']
    #    pattern = r"star-rating\s([A-Za-z)+])"
    #    matcher = re.search(r"star-rating\s([A-Za-z]+)", " ".join(rating))
       rating_word = next(filter(lambda x: x in self.RATINGS, rating), None)
       logger.info(f'Found book rating, `{rating_word}`.')
       logger.debug('Converting to integer for sorting in the return.')
       return self.RATINGS.get(rating_word) if rating_word else None
    #    if matcher:
    #      rating_word = matcher.group(1)
    #      return self.RATINGS[rating_word]
    #    return None

            