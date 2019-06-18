"""
Define the Rate model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Rate(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Rate model """

    __tablename__ = "rate"

    user_rating = db.Column(db.Integer, primary_key=True)
    movie_rated = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Float, nullable=True)

    def __init__(self, user_rating, movie_rated, rating=None):
        """ Create a new Rate """
        self.user_rating = user_rating
        self.movie_rated = movie_rated
        self.rating = rating
