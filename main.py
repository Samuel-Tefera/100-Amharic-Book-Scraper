import json
import os

import books, book_description

data = {}

for i in range(len(books.books_title)):
    data[i+1] = {
        'title' : books.books_title[i],
        'author' : books.books_author[i],
        'cover_page' : book_description.books_cover[i],
        'rating' : book_description.books_rating[i],
    }

json_file_path = 'data/amharic_books.json'

os.makedirs(os.path.dirname(json_file_path), exist_ok=True)

with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
