"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import UserRepository
from util import parse_params


class UserResourceByName(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/user/SEARCH_BY_NAME.yml")
    def get(first_name, last_name):
        """ Return an user key information based on his name """
        users = UserRepository.get_by_name(first_name = first_name, last_name = last_name)
        return jsonify({user.key : user.json for user in users})

