"""
Define the Movies model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Movie(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Movie model """

    __tablename__ = "movie"
    key = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), primary_key=False)
    director = db.Column(db.String(300), primary_key=False)
    genre = db.Column(db.String(300), primary_key=False)
    date = db.Column(db.Integer, nullable=True)
    

    def __init__(self, key, title, director, genre, date=None):
        """ Create a new Movie """
        self.key = key
        self.title = title
        self.director = director
        self.date = date
        self.genre = genre

