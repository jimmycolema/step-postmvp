import csv
import json

# Constants for corresponding indexes 
ENTRY_INDEX = 0
TITLE_INDEX = 1
AUTHOR_INDEX = 2
ISBN_INDEX = 4

DATASET_PWD = "../data/books.csv"
OUTPUT_FILE_PWD = "../data/parsed_books.txt"

# Iterates over the Goodreads-books dataset, converting each entry
# into a book dictionary compatible with the existing CoffeeHouse
# architecture.
def parse_goodreads_dataset(dataset_pwd, output_file_pwd):
  with open(DATASET_PWD) as goodreads_dataset:
    with open(OUTPUT_FILE_PWD, "w") as books_file:
      goodreads_csv = csv.reader(goodreads_dataset)

      next(goodreads_csv) # Skip CSV file column headers.
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

if __name__ == "__main__":
  parse_goodreads_dataset(DATASET_PWD, OUTPUT_FILE_PWD)
