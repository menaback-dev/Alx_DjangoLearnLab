from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print("Books by author:", books_by_author)


# List all books in a library
library = Library.objects.get(name="Central Library")
library_books = library.books.all()
print("Books in library:", library_books)


# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian:", librarian)
