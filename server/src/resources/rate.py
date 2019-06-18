"""
Define the REST verbs relative to the ratings
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import UserRepository
from util import parse_params


class RateResource(Resource):
    """ Verbs relative to the ratings """

    @staticmethod
    @swag_from("../swagger/user/GET.yml")
    def get(user_rating, movie_rated):
        """ Return an rate key information based on his user """
        rate = RateRepository.get(user_rating=user_rating, movie_rated=movie_rated)
        return jsonify({"rate": rate.json})

    @staticmethod
    @parse_params(
        Argument("ratings", location="json", required=True, help="The ratings of the movie by the user")
    )
    @swag_from("../swagger/user/POST.yml")
    def post(user_rating, movie_rated, rating):
        """ Create a rating based on the sent information """
        rate = RateRepository.create(
            user_rating=user_rating, movie_rated=movie_rated, rating=rating
        )
        return jsonify({"rate": rate.json})

    @staticmethod
    @parse_params(
        Argument("ratings", location="json", required=True, help="The ratings of the movie by the user")
    )
    @swag_from("../swagger/user/PUT.yml")
    def put(user_rating, movie_rated, rating):
        """ Update a rating based on the sent information """
        repository = RateRepository()
        rate = repository.update(user_rating=user_rating, movie_rated=movie_rated, rating=rating)
        return jsonify({"rate": rate.json})
