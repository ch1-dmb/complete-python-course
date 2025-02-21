from locators.quote_locators import QuoteLocators

class QuoteParsers:
    def __init__(self, boss):
        self.boss = boss

    def __repr__(self):
        return f'<Quote {self.get_content}, by {self.get_author}>'

    @property
    def get_content(self):
        return self.boss.select_one(QuoteLocators.CONTENT_LOCATOR).text

    @property
    def get_author(self):
        return self.boss.select_one(QuoteLocators.AUTHOR_LOCATOR).text

    # get_tags Needs a Loop Because of string Extraction
    @property
    def get_tags(self):
        return [i.text for i in self.boss.select(QuoteLocators.TAGS_LOCATOR)]


'''
When to use .text over .string:
If the HTML structure has nested tags and you want to get all the text, use .text. It's more reliable.
If the HTML structure is simple and you only want the direct text inside a tag (without nested tags), you can use .string.
'''