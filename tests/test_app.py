import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#this allows to import app without changing anything
from app import app
from database_connection import DatabaseConnection

from playwright.sync_api import Page, expect

def test_get_books_returns_a_200():
    client = app.test_client() #making the test client
    response = client.get("/books") #making the request
    assert response.status_code == 200


def test_book_list_contains_all_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    
    page.goto("http://127.0.0.1:5001/books")

    books = page.locator('table td').filter(has_text=" by ")

    expected_books = [
    'The Gruffalo by Julia Donaldson',
    'Ada Twist, Scientist by Andrea Beaty',
    'The Girl Who Drank the Moon by Kelly Barnhill',
    'Dragons in a Bag by Zetta Elliott'
    ]

    # here's the neat part which saves you from iterating over the `li` elements
    actual_books = books.all_inner_texts()

    assert actual_books == expected_books


def test_get_authors_returns_a_200():
    client = app.test_client() #making the test client
    response = client.get("/authors") #making the request
    assert response.status_code == 200

def test_get_authors_returns_all_authors():
    client = app.test_client()
    response = client.get("/authors")
    assert response.json == [
        {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
    },
    {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
    },
    {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
    },
    {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
    }
    ]