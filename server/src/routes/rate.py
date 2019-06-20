"""
Defines the blueprint for the ratingd
"""
from flask import Blueprint
from flask_restful import Api

from resources import RateResource, AllRatesResource,  RatesByMovieResource, RatesByUserResource 

RATE_BLUEPRINT = Blueprint("rate", __name__)
Api(RATE_BLUEPRINT).add_resource(
    RateResource, "/rate/<int:user_rating>/<int:movie_rated>"
)
Api(RATE_BLUEPRINT).add_resource(
    AllRatesResource, "/all_rates/"
)
Api(RATE_BLUEPRINT).add_resource(
    RatesByMovieResource, "/rates_of_movie/<int:movie_rated>"
)
Api(RATE_BLUEPRINT).add_resource(
    RatesByUserResource, "/rates_by_user/<int:user_rating>"
)
