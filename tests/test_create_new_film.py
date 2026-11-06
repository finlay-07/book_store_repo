from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

def test_create_film(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/films.sql")
    page.goto("http://127.0.0.1:5001/films")
    page.get_by_placeholder("Name").fill("Arrival")
    page.get_by_placeholder("Release Year").fill("2016")
    page.get_by_role("button", name="Submit").click()
    films = page.locator("li")
    new_film = films.all_inner_texts()[-1]
    assert new_film == "Arrival by 2016"