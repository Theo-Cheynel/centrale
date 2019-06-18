from models import Movie


class MovieRepository:
    """ The repository for the movie model """

    @staticmethod
    def get(title, director):

        return Movie.query.filter_by(title = title, director=director).one()

    def update(self, title, director, date):

        movie = self.get(title, director)
        movie.date = date
        movie.director= director

        return movie.save()

    @staticmethod
    def create(title, director, date):

        movie = Movie(title=title, director=director, date=date)
        return movie.save()
