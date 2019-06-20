"""
Defines the blueprint for the movies
"""
from flask import Blueprint
from flask_restful import Api

from resources import MovieResource, AllMoviesResource, MovieResourceByTitle, MovieRatingResource, MovieGenreResource, MoviesSimilarResource

MOVIE_BLUEPRINT = Blueprint("movie", __name__)
Api(MOVIE_BLUEPRINT).add_resource(
    MovieResource, "/movie/<int:key>"
)
Api(MOVIE_BLUEPRINT).add_resource(
    MovieResourceByTitle, "/movie/<string:title>"
)
Api(MOVIE_BLUEPRINT).add_resource(
    AllMoviesResource, "/movie/all"
)
Api(MOVIE_BLUEPRINT).add_resource(
    MovieRatingResource, "/movie_rating/<int:key>"
)
Api(MOVIE_BLUEPRINT).add_resource(
    MovieGenreResource, "/genre/<string:genre>"
)
Api(MOVIE_BLUEPRINT).add_resource(
    MoviesSimilarResource, "/similar/<int:key>"
)
