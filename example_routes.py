from lib.database_connection import get_flask_database_connection
from lib.book_repository import BookRepository
from lib.book import Book
from flask import request, render_template, redirect, url_for

# You won't need to nest your routes in app.py in a method like this
def apply_example_routes(app):
    # GET /books
    # Returns a list of books
    @app.route('/books', methods=['GET'])
    def get_books():
        connection = get_flask_database_connection()
        repository = BookRepository(connection)
        books = repository.all()
        return render_template('books/index.html', books=books)


    # GET /books/<id>
    # Returns a single book
    @app.route('/books/<int:id>', methods=['GET'])
    def get_book(id):
        connection = get_flask_database_connection()
        repository = BookRepository(connection)
        book = repository.find(id)
        return render_template('books/show.html', book=book)

    # GET /books/new
    # Returns a form to create a new book
    @app.route('/books/new', methods=['GET'])
    def get_new_book():
        return render_template('books/new.html')


    # POST /books
    # Creates a new book
    @app.route('/books', methods=['POST'])
    def create_book():
        connection = get_flask_database_connection()
        repository = BookRepository(connection)
        book = Book(None, request.form['title'], request.form['author_name'])
        book = repository.create(book)
        return redirect(url_for('get_book', id=book.id))


    # POST /books/<id>/delete
    # Deletes a book
    @app.route('/books/<int:id>/delete', methods=['POST'])
    def delete_book(id):
        connection = get_flask_database_connection()
        repository = BookRepository(connection)
        repository.delete(id)
        return redirect(url_for('get_books'))
