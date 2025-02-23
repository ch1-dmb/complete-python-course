import requests
from bs4 import BeautifulSoup
from locators.all_books_page import AllBooksPageLocators

from pages.books_page import BooksPage
from parsers.books_parsers import BooksParsers

web_link = requests.get("http://books.toscrape.com/").content
web = BooksPage(web_link)

# this will get book on the first page(main page)
# books = web.get_books
# print(f"Found {len(books)} books")
# print(books[0])

# use the variable to collect those books
_book_list = []
# get the toal of pages(int), and try to get all books info from each page


for i in range(web.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{i+1}.html'
    page_link = requests.get(url).content
    page_content = BooksPage(page_link)

    _book_list.extend(page_content.get_books)

books = _book_list

    





