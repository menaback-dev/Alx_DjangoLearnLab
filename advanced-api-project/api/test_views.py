from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book


class BookAPITest(APITestCase):

    def setUp(self):
        # create user
        self.user = User.objects.create_user(
            username="tester",
            password="pass123"
        )

        # create author + books
        self.author = Author.objects.create(name="Author A")

        self.book1 = Book.objects.create(
            title="Alpha",
            publication_year=2020,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Beta",
            publication_year=2022,
            author=self.author
        )

        self.list_url = "/api/books/"
        self.create_url = "/api/books/create/"

    #LIST
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    #DETAIL
    def test_get_book_detail(self):
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Alpha")

    #CREATE requires auth
    def test_create_book_requires_auth(self):
        data = {
            "title": "New",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        self.client.login(username="tester", password="pass123")

        data = {
            "title": "New",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #UPDATE
    def test_update_book(self):
        self.client.login(username="tester", password="pass123")

        response = self.client.put(
            f"/api/books/update/{self.book1.id}/",
            {
                "title": "Alpha Updated",
                "publication_year": 2020,
                "author": self.author.id
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #DELETE
    def test_delete_book(self):
        self.client.login(username="tester", password="pass123")

        response = self.client.delete(
            f"/api/books/delete/{self.book1.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #FILTER
    def test_filter_books(self):
        response = self.client.get(self.list_url + "?title=Alpha")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    #SEARCH
    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Beta")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    #ORDERING
    def test_order_books(self):
        response = self.client.get(self.list_url + "?ordering=publication_year")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["publication_year"], 2020)
