import csv
import json

ENTRY_INDEX = 0
TITLE_INDEX = 1
AUTHOR_INDEX = 2
ISBN_INDEX = 4

# Iterates over the Goodreads-books dataset, converting each entry
# into a book dictionary compatible with the existing CoffeeHouse
# architecture.
def parse_goodreads_dataset():
  with open("../data/books.csv") as goodreads_dataset:
    with open("../data/parsed_books.txt", "w") as books_file:
      goodreads_csv = csv.reader(goodreads_dataset)

      next(goodreads_csv)
      for row in goodreads_csv:
        title = row[TITLE_INDEX]
        author = row[AUTHOR_INDEX]
        isbn = row[ISBN_INDEX]
        
        book = {
          "title": title,
          "author": author,
          "isbn": isbn,
        }
        book_json = json.dumps(book)
        books_file.writelines((book_json, '\n'))

parse_goodreads_dataset()
