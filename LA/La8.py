print("LA:8")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("Daniel's book", "Daniel")
print(f"Title: {book.title}, Author: {book.author}")

del book.author

try:
    print(book.author)
except AttributeError as e:
    print(e)

book1 = Book("Old book", "Aeron")
print(f"Title: {book1.title}, Author: {book1.author}")