from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by author:", books_by_author)


# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
library_books = library.books.all()
print("Books in library:", library_books)


# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian:", librarian)
