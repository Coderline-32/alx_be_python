class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
   

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.fileSize = file_size
    def __str__(self):
        return f"{super().__str__()} [EBook, {self.fileSize}MB]"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.pageCount = page_count
    def __str__(self):
        return f"{super().__str__()} [PrintBook, {self.pageCount} pages]"



class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print('Only add instances!')
    def __str__(self):
        print(f"{self.books}")
    def list_books(self):
     
       for book in self.books:
           print(f"- {book}")


        