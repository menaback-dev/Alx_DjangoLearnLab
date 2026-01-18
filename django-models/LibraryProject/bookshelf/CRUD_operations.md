# Django CRUD Operations

This document contains all CRUD operations performed on the Book model using Django ORM.

## Create
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

## Retrieve
Book.objects.all()

## Update
book.title = "Nineteen Eighty-Four"
book.save()

## Delete
book.delete()
