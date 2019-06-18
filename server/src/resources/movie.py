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
    def get(title, director):
        """ Return a movie key information based on its title """
        movie = MovieRepository.get(title = title, director=director)
        return jsonify({"movie": movie.json})

    @staticmethod
    @parse_params(
        Argument("date", location="json", required=True, help="The date of the movie.")
    )
    @swag_from("../swagger/movie/POST.yml")
    def post(title, director, date):
        """ Create a movie based on the sent information """
        movie = MovieRepository.create(
            title = title, director = director, date = date
        )
        return jsonify({"movie": movie.json})

    @staticmethod
    @parse_params(
        Argument("date", location="json", required=True, help="The date of the movie.")
    )
    @swag_from("../swagger/movie/PUT.yml")
    def put(title, director, date):
        """ Update a movie based on the sent information """
        repository = MovieRepository()
        movie = repository.update(title = title, director = director, date=date)
        return jsonify({"movie": movie.json})
