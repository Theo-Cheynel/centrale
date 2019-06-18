"""
Defines the blueprint for the ratingd
"""
from flask import Blueprint
from flask_restful import Api

from resources import UserResource

RATE_BLUEPRINT = Blueprint("rate", __name__)
Api(RATE_BLUEPRINT).add_resource(
    RateResource, "/user/<integer:user_rating>/<integer:movie_rated>"
)
