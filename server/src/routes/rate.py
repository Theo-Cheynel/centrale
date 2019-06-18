"""
Defines the blueprint for the ratingd
"""
from flask import Blueprint
from flask_restful import Api

from resources import RateResource

RATE_BLUEPRINT = Blueprint("rate", __name__)
Api(RATE_BLUEPRINT).add_resource(
    RateResource, "/rate/<int:user_rating>/<int:movie_rated>"
)
