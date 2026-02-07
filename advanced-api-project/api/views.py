from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.

    Permissions:
        - Accessible to anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    Returns a single book by ID.

    Permissions:
        - Accessible to anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    Creates a new Book.

    Custom Behavior:
        - Only authenticated users can create books.
        - Serializer validation enforces publication_year rule.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook method to customize save behavior.
        Can be extended later for audit logging or owner tracking.
        """
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing Book.

    Permissions:
        - Only authenticated users allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom update hook.
        """
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a Book instance.

    Permissions:
        - Only authenticated users allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

