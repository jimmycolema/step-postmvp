class Node:

  def __init__(self, key):
    self.key = key
    self.children_dict = {}
    self.book_list = []

  #   Recursively inserts book based on it's title.
  #   Assumptions:
  #   1.) String will have all spaces & whitespace removed.
  #   2.) String will be lowercase, all ascii characters acceptable.
  def insert_book(self, insert_key, book):
    if len(insert_key) == 1:
      self.book_list.append(book)
      return

    child_node_key = insert_key[0]
    insert_key = insert_key[1:]

    if self.children_dict.get(child_node_key):
      self.children_dict.get(child_node_key).insert_book(insert_key, book)
    else:
      self.children_dict.update({child_node_key: Node(child_node_key)})
      self.children_dict.get(child_node_key).insert_book(insert_key, book)

  #   Recursivley searches for book based on it's title.
  def search_book_by_title(self, search_key, title):
    if len(search_key) == 1:
      for book in self.book_list:
        if book.get("title").lower().strip().replace(" ", "") == title.lower().strip().replace(" ", ""): 
          return book

    child_node_key = search_key[0]
    search_key = search_key[1:]

    if self.children_dict.get(child_node_key):
      return self.children_dict.get(child_node_key).search_book_by_title(search_key, title)
    else:
      return None
