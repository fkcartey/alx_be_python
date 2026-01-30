class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Triggers when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String Representation: For end-users."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official Representation: To recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
