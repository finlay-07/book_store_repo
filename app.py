from flask import Flask, render_template, request, redirect
from database_connection import DatabaseConnection
from book_repository import BookRepository
from book import Book
from film import Film
from film_repository import FilmRepository
from user import User
from user_repository import UserRepository

# instantiate a Flask app object
app = Flask(__name__)



# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

@app.route('/books', methods=['GET'])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    print(books)
    return render_template("books.html", books=books)

@app.route("/", methods=["GET"])
def index():
    #connection = DatabaseConnection()
    #book_repository = BookRepository(connection)
    #connection.connect()
    #books = book_repository.all()
    return render_template("index.html") #, books=books)

@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)


@app.route('/authors', methods=['GET'])
def authors():
    authors = [
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
    return authors

@app.route('/books', methods=['POST'])
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(title=book_details["title"], author=book_details["author"])
    book_repository.create(book)
    return redirect("/books")

@app.route('/films', methods=['GET'])
def get_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    return render_template("films.html", films=films)

@app.route('/films', methods=['POST'])
def create_film():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    film_name = request.form['name']
    film_year = request.form['release_year']
    film_repository.create(Film(film_name, film_year))
    return redirect("/films")

@app.route('/users/new', methods=['GET'])
def get_signup_form():
    return render_template("signup_form.html")

@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    user = User(username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect("/books")

# make the server run in response to `python app.py`
# on port 5001
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)