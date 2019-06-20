"""
Define the REST verbs relative to the ratings
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import RateRepository
from util import parse_params


class RatesByMovieResource(Resource):
    """ Verbs relative to the ratings """

    @staticmethod
    @swag_from("../swagger/rate/GET_BY_MOVIE.yml")
    def get(movie_rated):
        """ Return a list of all ratings of the movie """
        rates = RateRepository.get_all_by_movie(key=movie_rated)
        return jsonify({rate.user_rating : rate.json for rate in rates})
