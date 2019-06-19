"""
Define the REST verbs relative to the movies
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import RateRepository
from util import parse_params


class MovieRatingResource(Resource):
    """ Verbs relative to the movies """

    @staticmethod
    @swag_from("../swagger/movie/GET_AVERAGE_RATING.yml")
    def get(key):
        """ Return all movies """
        rating = RateRepository.average_rating(key = key)
        return jsonify({"average_rating" : rating})

