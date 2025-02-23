import re

from locators.book_locators import BookLocators

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
        self.boss = boss

    def __repr__(self):
       return f'<Book {self.name} {self.price}, {self.rating} stars>'

    #get book name
    @property
    def name(self):
       locators = BookLocators.NAME_LOCATOR
       book_name = self.boss.select_one(locators).attrs['title']
       return book_name
      

   #get link
    @property
    def link(self):
       locators = BookLocators.LINK_LOCATOR
       link_name = self.boss.select_one(locators).attrs['href']
       pattern = r"catalogue/([a-zA-Z\-_]+)\d+\/index\.html"
       matcher = re.search(pattern, link_name)
       return matcher.group(1) if matcher else None

   # how much for the specific book 
    @property
    def price(self):
       locators = BookLocators.PRICE_LOCATOR
       price_name = self.boss.select_one(locators).text
       pattern = r"£(\d+(?:\.\d{2})?)"
       matcher = re.search(pattern, price_name)

       return float(matcher.group(1)) if matcher else None
 

   #  whats the rating of this book?
    @property
    # use next, filter to find rating
    def rating(self):
      
       locators = BookLocators.RATING_LOCATOR
       rating = self.boss.select_one(locators).attrs['class']
       pattern = r"star-rating\s([A-Za-z)+])"
       matcher = re.search(r"star-rating\s([A-Za-z]+)", " ".join(rating))
       rating_word = next(filter(lambda x: x in self.RATINGS, rating), None)
       return self.RATINGS.get(rating_word) if rating_word else None
    #    if matcher:
    #      rating_word = matcher.group(1)
    #      return self.RATINGS[rating_word]
    #    return None

            