from playwright.sync_api import Page, expect

def test_creating_a_new_book(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder("title").fill("The Chroicles of Geronimo (the cat)")
    page.get_by_placeholder("author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_role("cell", name="The Chroicles of Geronimo (the cat) by Geronimo").first).to_be_visible()
    # assert new_book == "The Chroicles of Geronimo (the cat) by Geronimo"