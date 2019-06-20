"""
Define the REST verbs relative to the movies
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import UserRepository
from util import parse_params


class AllUsersResource(Resource):
    """ Verbs relative to the user """

    @staticmethod
    @swag_from("../swagger/user/GET_ALL.yml")
    def get():
        """ Return all users """
        users = UserRepository.get_all()
        return jsonify({user.key: user.json for user in users})

    @staticmethod
    @swag_from("../swagger/user/LOAD_DB.yml")
    def post():
        """ Post the full user database """
        users = UserRepository.post_all_db()
        return jsonify({"data":"The user database was loaded correctfully"})
