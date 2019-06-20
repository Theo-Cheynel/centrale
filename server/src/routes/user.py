"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import UserResource, UserResourceByName, AllUsersResource

USER_BLUEPRINT = Blueprint("user", __name__)
Api(USER_BLUEPRINT).add_resource(
    UserResource, "/user/<int:key>"
)
Api(USER_BLUEPRINT).add_resource(
    UserResourceByName, "/user/<string:last_name>/<string:first_name>"
)
Api(USER_BLUEPRINT).add_resource(
    AllUsersResource, "/all_users/"
)
