from models import Movie


class MovieRepository:
    """ The repository for the movie model """

    @staticmethod
    def get_all():

        return Movie.query.all()

    def get(title, director):

        return Movie.query.filter_by(title = title, director=director).one()

    def update(self, title, director, date, rating):

        movie = self.get(title, director)
        movie.date = date
        movie.director= director
        movie.rating = rating

        return movie.save()

    @staticmethod
    def create(title, director, date, rating):

        movie = Movie(title=title, director=director, date=date, rating=rating)
        return movie.save()
