class BookShelf:
    def __init__(self, *books) -> None:
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."
    
class Book:
        def __init__(self, name) -> None:
            self.name = name

        def __str__(self) -> str:
            return f"Book {self.name}."
        
""" we use a Book class to creat more book objects and than we use Bookshelf Class using book objects as attributes"""
""" This is COMPOSITION """
book1 = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book1, book2)
print(book1)

print(shelf)
for book in shelf.books: # hre we are getting objects in loop
     print(book) 
