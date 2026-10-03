class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False


class Library:
    def __init__(self):
        self.books = []

    # Add a book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    # Remove a book
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.issued:
                    print("Book is currently issued. Cannot remove it.")
                else:
                    self.books.remove(book)
                    print("Book removed successfully!")
                return

        print("Book not found!")

    # Issue a book
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.issued:
                    print("Book is already issued!")
                else:
                    book.issued = True
                    print("Book issued successfully!")
                return

        print("Book not found!")

    # Return a book
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.issued:
                    book.issued = False
                    print("Book returned successfully!")
                else:
                    print("Book was not issued!")
                return

        print("Book not found!")

    # Display all books
    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nLibrary Books:")
        for book in self.books:
            status = "Issued" if book.issued else "Available"

            print("ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Status:", status)
            print("----------------------")



library = Library()

library.add_book(Book(1, "Python Programming", "John Smith"))
library.add_book(Book(2, "Java Programming", "James Gosling"))
library.add_book(Book(3, "Data Structures", "Mark Allen"))


library.display_books()


library.issue_book(1)


library.display_books()


library.return_book(1)


library.remove_book(2)


library.display_books()