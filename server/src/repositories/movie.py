from models import Movie


class MovieRepository:
    """ The repository for the movie model """

    @staticmethod
    def get_all():

        return Movie.query.all()

    def get_by_title(title):
        return Movie.query.filter_by(title=title)

    def getbykey(key):

        return Movie.query.filter_by(key=key).one()

    def update(self, key, title, director, date):

        movie = self.get(title, director)
        movie.date = date
        movie.director= director
        movie.key=key

        return movie.save()

    @staticmethod
    def create(key, title, director, date):

        movie = Movie(key=key, title=title, director=director, date=date)
        return movie.save()

