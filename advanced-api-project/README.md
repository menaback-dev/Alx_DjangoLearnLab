# Advanced API Project — Generic Views

This project demonstrates Django REST Framework generic views
for CRUD operations on the Book model.

## Views Implemented

BookListView — list all books (public)
BookDetailView — retrieve one book (public)
BookCreateView — create book (authenticated only)
BookUpdateView — update book (authenticated only)
BookDeleteView — delete book (authenticated only)

## Permissions

Read endpoints are open.
Write endpoints require authentication.

## Validation

BookSerializer prevents publication_year from being in the future.

## Endpoints

GET /api/books/
GET /api/books/<id>/
POST /api/books/create/
PUT /api/books/<id>/update/
DELETE /api/books/<id>/delete/


## Tests cover:
- CRUD operations
- permissions (auth required for write)
- filtering, search, ordering
- response status codes

Run with:
python manage.py test api
