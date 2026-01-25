from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm


# =========================
# SECURITY NOTES:
# - Django ORM is used to prevent SQL injection.
# - User input is validated using Django forms.
# - CSP headers are added to mitigate XSS attacks.
# - permission_required is used to enforce access control.
# =========================


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    """
    Securely list all books.
    Uses Django ORM to prevent SQL injection.
    """
    books = Book.objects.all()  # ORM prevents SQL injection
    return render(request, "bookshelf/book_list.html", {"books": books})


def search_books(request):
    """
    Secure search view using Django ORM (prevents SQL injection).
    User input is parameterized automatically.
    """
    query = request.GET.get("q", "")
    books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"books": books})


@permission_required("bookshelf.can_create", raise_exception=True)
def add_book_secure(request):
    """
    Secure book creation view.
    Uses Django forms for validation and sanitization.
    """
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():  # Input validation
            form.save()
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})


@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book_secure(request, book_id):
    """
    Secure book edit view.
    Protected with custom permissions.
    """
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():  # Input validation
            form.save()
    else:
        form = ExampleForm(instance=book)

    return render(request, "bookshelf/form_example.html", {"form": form})


@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book_secure(request, book_id):
    """
    Secure book delete view.
    Uses ORM and permission checks.
    """
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()

    return render(request, "bookshelf/book_list.html", {"books": Book.objects.all()})


def csp_protected_view(request):
    """
    View with Content Security Policy (CSP) header
    to mitigate XSS attacks.
    """
    response = HttpResponse("CSP protected response")

    # Content Security Policy header
    response["Content-Security-Policy"] = (
        "default-src 'self'; script-src 'self'; style-src 'self'"
    )

    return response
