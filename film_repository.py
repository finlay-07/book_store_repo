from film import Film

class FilmRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    def all(self):
        rows = self._connection.execute('SELECT * FROM films ORDER BY id')
        films = []
        for row in rows:
            item = Film(row["name"], row["release_year"], row["id"])
            films.append(item)
        return films

    def create(self, film):
        rows = self._connection.execute("INSERT INTO films (name, release_year) VALUES (%s, %s)", (film.name, film.release_year))
        return None