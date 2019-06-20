"""
Define the REST verbs relative to the ratings
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import RateRepository
from util import parse_params


class RatesByUserResource(Resource):
    """ Verbs relative to the ratings """

    @staticmethod
    @swag_from("../swagger/rate/GET_BY_USER.yml")
    def get(user_rating):
        """ Return a list of all ratings done by the user """
        rates = RateRepository.get_all_by_user(key=user_rating)
        return jsonify({rate.movie_rated : rate.json for rate in rates})
