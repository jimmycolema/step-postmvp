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
  goodreads_dataset = open("../data/books.csv")
  goodreads_csv = csv.reader(goodreads_dataset)

  book_list = []
  for index, row in enumerate(goodreads_csv):
    # Skip CSV file column headers.
    if index == 0: continue

    title = row[TITLE_INDEX]
    author = row[AUTHOR_INDEX]
    isbn = row[ISBN_INDEX]
    
    book = {
      "title": title,
      "author": author,
      "isbn": isbn,
    }
    book_json = json.dumps(book)
    book_list.append(book_json + "\n")
  
  booksFile = open("../data/parsed_books.txt", "w")
  booksFile.writelines(book_list)
  booksFile.close()

parse_goodreads_dataset()
