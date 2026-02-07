from django.db import models


class Author(models.Model):
    """
    Author model represents a book writer.

    Fields:
        name — stores the author's full name.

    Relationship:
        One Author can have many Books (one-to-many).
        Related books are accessed using author.books.all()
        because of related_name in Book model.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a published book.

    Fields:
        title — name of the book
        publication_year — year book was published
        author — ForeignKey linking to Author

    Relationship:
        Many books belong to one Author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )

    def __str__(self):
        return self.title
