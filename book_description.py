import books

from bs4 import BeautifulSoup
import requests

num = 1

books_detail_pages = []
print(len(books.books_link))
for book_link in books.books_link:
    res = requests.get(url=book_link, headers=books.headers)
    books_detail_pages.append(BeautifulSoup(res.text, 'html.parser'))
    print(num)
    num = num + 1

print(f'length of book detail page: {len(books_detail_pages)}')

books_cover = []
for detail_pages in books_detail_pages:
    for detail_page in detail_pages.findAll('img', {'role' : 'presentation'}):
        # append 2 book cover pic link
        books_cover.append(detail_page['src'])
    books_cover.pop() # remove duplicate link

print(f'length of book detail cover: {len(books_cover)}')

books_rating = []
for detail_pages in books_detail_pages:
    for detail_page in detail_pages.find('div', {'class' : 'RatingStatistics__rating'}):
        books_rating.append(float(detail_page.get_text()))

print(f'length of books rating: {len(books_rating)}')
