"""
Define the Movies model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Movie(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Movie model """

    __tablename__ = "movie"

    title = db.Column(db.String(300), primary_key=True)
    director = db.Column(db.String(300), primary_key=True)
    date = db.Column(db.Integer, nullable=True)
    

    def __init__(self, title, director, date=None):
        """ Create a new Movie """
        self.title = title
        self.director = director
        self.date = date
