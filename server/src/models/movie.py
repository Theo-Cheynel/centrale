"""
Define the Movies model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Movies(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Movie model """

    __tablename__ = "user"

    title = db.Column(db.String(300), primary_key=True)
    director = db.Column(db.String(300), primary_key=False)
    date = db.Column(db.Integer, nullable=True)
    

    def __init__(self, first_name, last_name, age=None):
        """ Create a new Movie """
        self.title = first_name
        self.director = director
        self.date = date
