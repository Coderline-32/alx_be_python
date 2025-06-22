class Book:
    """
    A class to represent a book with a title, author, and publication year.
    """

    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The year the book was published.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        Used by print() and str().
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns a developer-friendly string representation of the book.
        Used in debugging and interactive sessions.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Called when the object is about to be destroyed.
        Typically used to free resources or confirm deletion.
        """
        print(f"Deleting book: {self.title}")
