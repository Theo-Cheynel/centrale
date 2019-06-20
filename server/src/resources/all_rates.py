"""
Define the REST verbs relative to the ratings
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import RateRepository
from util import parse_params


class AllRatesResource(Resource):
    """ Verbs relative to the ratings """

    @staticmethod
    @swag_from("../swagger/rate/LOAD_DB.yml")
    def put():
        """ Load the full rating database """
        rate = RateRepository.post_db()
        return jsonify({"success": "the database was loaded successfully"})
