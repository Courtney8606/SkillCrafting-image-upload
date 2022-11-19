from playwright.sync_api import Page, expect

"""
We can list out all the books
"""
def test_get_books(db_connection, page, test_web_address):
    # We seed our database with the book store seed file
    db_connection.seed("seeds/book_store.sql")

    # We load a virtual browser and navigate to the /books page
    page.goto(f"http://{test_web_address}/books")

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
def test_get_book(db_connection, page, test_web_address):
    db_connection.seed("seeds/book_store.sql")

    # We visit the books page
    page.goto(f"http://{test_web_address}/books")

    # Click the link with the text 'Emma by Jane Austen'
    page.click("text=Emma by Jane Austen")

    # The virtual browser acts just like a normal browser and goes to the next
    # page without us having to tell it to.

    # Then we look for specific test classes that we have put into the HTML
    # as targets for our tests to look for. This one is called `t-title`.
    # You can see it in `templates/books/show.html`
    title_element = page.locator(".t-title")
    expect(title_element).to_have_text("Emma")

    # We do the same for the author name
    author_element = page.locator(".t-author-name")
    expect(author_element).to_have_text("Jane Austen")


"""
When we create a new book
We see it in the books index
"""
def test_create_book(db_connection, page, test_web_address):
    db_connection.seed("seeds/book_store.sql")
    page.goto(f"http://{test_web_address}/books")

    # This time we click the link with the text 'Add a new book'
    page.click("text=Add a new book")

    # Then we fill out the field with the name attribute 'title'
    page.fill("input[name='title']", "The Hobbit")

    # And the field with the name attribute 'author_name'
    page.fill("input[name='author_name']", "J.R.R. Tolkien")

    # Finally we click the button with the text 'Create Book'
    page.click("text=Create Book")

    # Just as before, the virtual browser acts just like a normal browser and
    # goes to the next page without us having to tell it to.

    title_element = page.locator(".t-title")
    expect(title_element).to_have_text("The Hobbit")

    author_element = page.locator(".t-author-name")
    expect(author_element).to_have_text("J.R.R. Tolkien")


"""
When we delete a book
We no longer see it in the books index
"""
def test_delete_book(db_connection, page, test_web_address):
    db_connection.seed("seeds/book_store.sql")
    page.goto(f"http://{test_web_address}/books")
    page.click("text=Nineteen Eighty-Four by George Orwell")
    page.click("text=Delete Book")
    list_items = page.locator("li")
    expect(list_items).to_have_text([
        "Mrs Dalloway by Virginia Woolf",
        "Emma by Jane Austen",
        "Dracula by Bram Stoker",
        "The Age of Innocence by Edith Wharton",
    ])

