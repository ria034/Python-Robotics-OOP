class Library: 
    def __init__(self,name_lib):
        self.name_lib = name_lib 
        self.books= []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

    
class Book:
    def __init__(self, title, author):
        self.title= title 
        self.author = author 


library = Library("Boston Common Public Library")

book1= Book("Harry Potter", "J.K Rowling")
book2= Book("2 states", "Chetan Bhagat")

library.add_book(book1)
library.add_book(book2)
print(library.name_lib)

for book in library.list_books():
    print(book)


