class Book:
    """Represents a book with title, author, and checkout status."""

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
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """Manages a collection of Book instances."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        print(f"'{title}' is not available or does not exist.")
        return False

    def return_book(self, title):
        """Returns a book by title if it was checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        print(f"'{title}' was not checked out or does not exist.")
        return False

    def list_available_books(self):
        """Prints all books that are currently available."""
        available = False
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available = True
        if not available:
            print("No books available at the moment.")
