from models import Movie


class MovieRepository:
    """ The repository for the movie model """

    @staticmethod
    def get_all():

        return Movie.query.all()

    def get_by_title(title):
        return Movie.query.filter_by(title=title)

    def get_by_genre(genre):
        return Movie.query.filter_by(genre=genre)

    def getbykey(key):

        return Movie.query.filter_by(key=key).one()

    def update(self, key, title, director, date, genre):

        movie = self.get(title, director)
        movie.date = date
        movie.director= director
        movie.key=key
        movie.genre=genre

        return movie.save()

    @staticmethod
    def create(key, title, director, date, genre):

        movie = Movie(key=key, title=title, director=director, date=date, genre=genre)
        return movie.save()

