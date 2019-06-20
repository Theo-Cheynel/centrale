"""
Define the REST verbs relative to the movies
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import MovieRepository, RateRepository, UserRepository
from util import parse_params

from functools import reduce
import operator
import math

def prod(factors):
    return reduce(operator.mul, factors, 1)



class MoviesSimilarResource(Resource):
    """ Verbs relative to the movies """

    @staticmethod
    @swag_from("../swagger/movie/GET_SIMILAR.yml")
    def get(key):
        """ Return a list of similar movies """
        movie = MovieRepository.getbykey(key)
        #return jsonify({"test":movie.json})
        
        users_who_rated = RateRepository.get_all_by_movie(key)
        keys_of_users_who_rated = [u.user_rating for u in users_who_rated]
        movies_were_rated = {}
        for user in users_who_rated :
            for m in RateRepository.get_all_by_user(user.user_rating) :
                if m.movie_rated in movies_were_rated :
                    movies_were_rated[m.movie_rated].append(user.user_rating)
                else :
                    movies_were_rated[m.movie_rated] = [user.user_rating]
        sim = {}
        
        #return jsonify({movie:movie for movie in movies_were_rated})
        for m in movies_were_rated.keys() :
            users = [u for u in movies_were_rated[m] if u in keys_of_users_who_rated]
            sim[m] = sum((RateRepository.get(user, movie.key).rating - RateRepository.average_rating(movie.key)) * (RateRepository.get(user, m).rating - RateRepository.average_rating(m)) for user in users) / prod([math.sqrt(0.00001 + (RateRepository.get(user, movie.key).rating - RateRepository.average_rating(movie.key))**2 + (RateRepository.get(user, m).rating - RateRepository.average_rating(m))**2) for user in users])
            print(sim[m])
            
        movies_to_be_returned = [MovieRepository.getbykey(m) for m in sim.keys() if sim[m] > .8]
        
        return jsonify({movie.key: movie.json for movie in movies_to_be_returned})


