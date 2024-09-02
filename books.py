import requests
from bs4 import BeautifulSoup

books_url = 'https://www.goodreads.com/list/show/89548.Best_Amharic_Books'

headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
   }

def books_detail_url(book_link):
    return f'https://www.goodreads.com{book_link}'

book_res = requests.get(url=books_url, headers=headers)
web_page = book_res.text
soup = BeautifulSoup(web_page, 'html.parser')

books_title = []
books_link = []
for title in soup.find_all('a', {'class' : 'bookTitle'}):
    books_title.append(title.find('span', recursive=False).get_text())
    books_link.append(books_detail_url(title['href']))

books_author = []
for author in soup.find_all('a', {'class' : 'authorName'}):
    books_author.append(author.find('span', recursive=False).get_text())
