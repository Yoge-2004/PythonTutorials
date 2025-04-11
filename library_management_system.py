class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = {}  # key: title, value: LibraryBook object
        self.borrowers = {}  # key: borrower name, value: list of titles

    def __str__(self):
        book_list = "\n".join([str(book) for book in self.books.values()])
        return f"Library Name: {self.library_name}\nBooks:\n{book_list}"

    def __repr__(self):
        return f"<Library: {self.library_name}, Total Books: {len(self)}>"

    def __len__(self):
        return len(self.books)

    def __getitem__(self, title):
        return self.books[title]

    def __setitem__(self, title, book):
        self.books[title] = book

    def __contains__(self, title):
        return title in self.books

    def add_book(self, book):
        if book.title in self.books:
            self.books[book.title] = self.books[book.title] + book.copies_available
        else:
            self.books[book.title] = book

    def borrow_book(self, title, user):
        if title in self.books and self.books[title].copies_available > 0:
            self.books[title] = self.books[title] - 1
            self.borrowers.setdefault(user, []).append(title)
        else:
            print("Not Available.")
            return None

    def return_book(self, title, borrower):
        if title in self.books and borrower in self.borrowers and title in self.borrowers[borrower]:
            self.books[title] = self.books[title] + 1
            self.borrowers[borrower].remove(title)
            if not self.borrowers[borrower]:
                del self.borrowers[borrower]
        else:
            print("Book is not available or Invalid Borrower Name.")

    def search_by_author(self, author_name):
        return [book for book in self.books.values() if book.author.lower() == author_name.lower()]


class LibraryBook:
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def __call__(self):
        return {
            "title": self.title,
            "author": self.author,
            "copies available": self.copies_available
        }

    def __str__(self):
        return f"title = '{self.title}', author = '{self.author}', copies_available = {self.copies_available}"

    def __repr__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nCopies Available: {self.copies_available}"

    def __eq__(self, other):
        return isinstance(other, LibraryBook) and self.title == other.title and self.author == other.author

    def __len__(self):
        return self.copies_available

    def __add__(self, x):
        return LibraryBook(self.title, self.author, self.copies_available + x)

    def __sub__(self, x):
        result = self.copies_available - x
        return LibraryBook(self.title, self.author, max(result, 0))


# Demonstration
if __name__ == '__main__':
    book1 = LibraryBook("The Alchemist", "Paulo Coelho", 5)
    book2 = LibraryBook("1984", "George Orwell", 2)

    print(book1)                    # Display book1 details
    print(book1 == book2)          # False
    book1 = book1 + 3              # Add 3 copies
    book1 = book1 - 1              # Borrow 1 copy
    print(len(book1))              # Number of copies available
    print(book1())                 # Dictionary format
    print()

    lib = Library("City Central Library")
    lib.add_book(book1)
    lib.add_book(book2)

    print(lib)                     # Library details
    print(len(lib))                # Total number of books
    print("The Alchemist" in lib)  # True

    results = lib.search_by_author("George Orwell")
    for book in results:
        print(book)

    lib.borrow_book("1984", "Alice")
    print(lib.borrowers)           # {'Alice': ['1984']}

    lib.return_book("1984", "Alice")
    print(lib.borrowers)           # {}
