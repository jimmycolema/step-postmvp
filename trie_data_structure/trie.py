import json
from trie_node import Node

class Trie:

  def __init__(self):
    self.root = Node("root")
    self.load_books()

  def load_books(self):
    goodreads_books_file = open("../utils/data/parsed_books.txt", "r")
    goodreads_books = goodreads_books_file.readlines()

    for book_json in goodreads_books:
      book = json.loads(book_json)
      self.insert_book(book)
    goodreads_books_file.close()

  def insert_book(self, book):
    insert_key = book.get("title").lower().strip().replace(" ", "")
    child_node_key = insert_key[0]

    if self.root.children_dict.get(child_node_key):
      self.root.children_dict.get(child_node_key).insert_book(insert_key, book)
    else:
      self.root.children_dict.update({child_node_key: Node(child_node_key)})
      self.root.children_dict.get(child_node_key).insert_book(insert_key, book)

  def search_book(self, title):
    search_key = title.lower().strip().replace(" ", "")
    child_node_key = search_key[0]

    if self.root.children_dict.get(child_node_key):
      found_book = self.root.children_dict.get(child_node_key).search_book_by_title(search_key, title)
      print(found_book) if found_book else print("Book not found.")
    else:
      print("Book not found.")


def main():
  trie = Trie()
  trie.search_book("The Iliad")
  trie.search_book("Quimby the Mouse")
  trie.search_book("Even Cowgirls Get the Blues")

main()
