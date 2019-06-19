"""
Define the REST verbs relative to the movies
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import MovieRepository
from util import parse_params


class MovieResource(Resource):
    """ Verbs relative to the movies """

    @staticmethod
    @swag_from("../swagger/movie/GET.yml")
    def get(key):
        """ Return a movie key information based on its title """
        movie = MovieRepository.getbykey(key=key)
        return jsonify({"movie": movie.json})

    @staticmethod
    @parse_params(
        Argument("date", location="json", required=True, help="The date of the movie."),
        Argument("title", location="json", required=True, help="The title of the movie."),
        Argument("director", location="json", required=True, help="The name of the movie director.")
    )
    @swag_from("../swagger/movie/POST.yml")
    def post(key, title, director, date):
        """ Create a movie based on the sent information """
        movie = MovieRepository.create(
            key = key, title = title, director = director, date = date
        )
        return jsonify({"movie": movie.json})

    @staticmethod
    @parse_params(
        Argument("date", location="json", required=True, help="The date of the movie."),
        Argument("title", location="json", required=True, help="The title of the movie."),
        Argument("director", location="json", required=True, help="The name of the movie director.")
    )
    @swag_from("../swagger/movie/PUT.yml")
    def put(key, title, director, date):
        """ Update a movie based on the sent information """
        repository = MovieRepository()
        movie = repository.update(key = key, title = title, director = director, date=date)
        return jsonify({"movie": movie.json})
