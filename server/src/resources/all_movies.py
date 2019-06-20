"""
Define the REST verbs relative to the movies
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import MovieRepository
from util import parse_params


class AllMoviesResource(Resource):
    """ Verbs relative to the movies """

    @staticmethod
    @swag_from("../swagger/movie/GET_ALL.yml")
    def get():
        """ Return all movies """
        movies = MovieRepository.get_all()
        return [movie.json for movie in movies]

