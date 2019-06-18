""" Defines the Rate repository """

from models import Rate


class RateRepository:
    """ The repository for the rate model """

    @staticmethod
    def get(user_rating, movie_rated):
        """ Query a rating by user and movie """
        return Rate.query.filter_by(user_rating=user_rating, movie_rated=movie_rated).one()

    def update(self, user_rating, movie_rated, rating):
        """ Update a movie's rating """
        rate = self.get(user_rating, movie_rated)
        rate.rating = rating

        return rate.save()

    @staticmethod
    def create(user_rating, movie_rated, rating):
        """ Create a new rating """
        rate = Rate(user_rating=user_rating, movie_rated=movie_rated, rating=rating)

        return rate.save()
