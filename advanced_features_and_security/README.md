# Permissions and Groups Setup

## Custom Permissions

The Book model defines the following custom permissions:

- can_view
- can_create
- can_edit
- can_delete

These permissions are declared in the Book model Meta class.

## Groups Configuration

Three groups were created using the Django admin interface:

1. Viewers
   - Assigned permission: can_view

2. Editors
   - Assigned permissions: can_create, can_edit

3. Admins
   - Assigned permissions: can_view, can_create, can_edit, can_delete

## Views Protection

The following views are protected using the permission_required decorator:

- add_book → requires can_create
- edit_book → requires can_edit
- delete_book → requires can_delete
- list_books → requires can_view

Example:

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    ...

## Usage

Users are assigned to groups via the Django admin interface.  
Access to views is automatically restricted based on group permissions.
