class Book:
    def __init__(self, title, author):
        """Initialize base book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook attributes using inheritance."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook attributes using inheritance."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Composition: Library manages a collection of Book instances."""
        self.books = []

    def add_book(self, book):
        """Adds a book instance to the library collection."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library."""
        for book in self.books:
            print(book)
