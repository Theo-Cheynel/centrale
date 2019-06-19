"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import UserRepository
from util import parse_params


class UserResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/user/GET.yml")
    def get(key):
        """ Return an user key information based on his name """
        user = UserRepository.getbykey(key=key)
        return jsonify({"user": user.json})

    @staticmethod
    @parse_params(
        Argument("age", location="json", required=True, help="The age of the user."),
        Argument("first_name", location="json", required=True, help="The first name of the user."),
	Argument("last_name", location="json", required=True, help="The last name of the user.")
    )
    @swag_from("../swagger/user/POST.yml")
    def post(key, last_name, first_name, age):
        print(key, last_name, first_name)
        """ Create an user based on the sent information """
        user = UserRepository.create(
            key=key, last_name=last_name, first_name=first_name, age=age
        )
        return jsonify({"user": user.json})

    @staticmethod
    @parse_params(
        Argument("age", location="json", required=True, help="The age of the user."),
        Argument("first_name", location="json", required=True, help="The first name of the user."),
	Argument("last_name", location="json", required=True, help="The last name of the user.")
    )
    @swag_from("../swagger/user/PUT.yml")
    def put(key, last_name, first_name, age):
        """ Update an user based on the sent information """
        repository = UserRepository()
        user = repository.update(key=key, last_name=last_name, first_name=first_name, age=age)
        return jsonify({"user": user.json})
