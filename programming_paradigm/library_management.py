class Book:
    """A class representing a book with title, author, and availability."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a library managing a collection of books."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds a book by title and checks it out."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return

    def return_book(self, title):
        """Finds a book by title and returns it."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        """Lists all books that are not checked out."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
