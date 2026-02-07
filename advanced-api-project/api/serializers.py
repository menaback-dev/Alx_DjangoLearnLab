from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer converts Book model instances to/from JSON.

    Includes all model fields.

    Custom Validation:
        Ensures publication_year is not in the future.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Field-level validation.
        Rejects years greater than current year.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer serializes Author model.

    Nested Representation:
        Includes related books using BookSerializer.
        Uses related_name='books' from the Book model.
        many=True → one author has many books.
        read_only=True → nested books are not created here.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
