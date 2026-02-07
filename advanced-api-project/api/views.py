from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    List books with filtering, searching, and ordering.

    Examples:
    /api/books/?title=1984
    /api/books/?search=orwell
    /api/books/?ordering=publication_year
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Filtering
    filterset_fields = ['title', 'publication_year', 'author']

    # Searching
    search_fields = ['title', 'author__name']

    # Ordering
    ordering_fields = ['title', 'publication_year']



class BookDetailView(generics.RetrieveAPIView):
    """
    Returns a single book by ID.

    Permissions:
        - Accessible to anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Creates a new Book.

    Custom Behavior:
        - Only authenticated users can create books.
        - Serializer validation enforces publication_year rule.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

