import re
from playwright.sync_api import Page, expect

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page): # Note `page` parameter
    # We load a virtual browser and navigate to the /emoji page
    page.goto("http://localhost:5000/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")


"""
We can list out all the books
"""
def test_get_books(db_connection, page):
    # We seed our database with the book store seed file
    db_connection.seed("seeds/book_store.sql")

    # We load a virtual browser and navigate to the /books page
    page.goto("http://localhost:5000/books")

    # We look at all the <li> tags
    list_items = page.locator("li")

    # We assert that it has the books in it
    expect(list_items).to_have_text([
        "Nineteen Eighty-Four by George Orwell",
        "Mrs Dalloway by Virginia Woolf",
        "Emma by Jane Austen",
        "Dracula by Bram Stoker",
        "The Age of Innocence by Edith Wharton",
    ])


"""
We can retrieve a single book
"""
def test_get_book(db_connection, page):
    db_connection.seed("seeds/book_store.sql")
    page.goto("http://localhost:5000/books")
    page.click("text=Emma by Jane Austen")
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Title: Emma",
        "Author: Jane Austen",
    ])


"""
When we create a new book
We see it in the books index
"""
def test_create_book(db_connection, page):
    db_connection.seed("seeds/book_store.sql")
    page.goto("http://localhost:5000/books")
    page.click("text=Add a new book")
    page.fill("input[name='title']", "The Hobbit")
    page.fill("input[name='author_name']", "J.R.R. Tolkien")
    page.click("text=Create Book")
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Title: The Hobbit",
        "Author: J.R.R. Tolkien",
    ])


"""
When we delete a book
We no longer see it in the books index
"""
def test_delete_book(db_connection, page):
    db_connection.seed("seeds/book_store.sql")
    page.goto("http://localhost:5000/books")
    page.click("text=Nineteen Eighty-Four by George Orwell")
    page.click("text=Delete Book")
    list_items = page.locator("li")
    expect(list_items).to_have_text([
        "Mrs Dalloway by Virginia Woolf",
        "Emma by Jane Austen",
        "Dracula by Bram Stoker",
        "The Age of Innocence by Edith Wharton",
    ])

