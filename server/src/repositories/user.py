""" Defines the User repository """

from models import User


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def getbykey(key):
        """ Query a user by last and first name """
        return User.query.filter_by(key=key).one()

    def update(self, key, last_name, first_name, age):
        """ Update a user's age """
        user = self.get(last_name, first_name)
        user.age = age

        return user.save()

    @staticmethod
    def create(key, last_name, first_name, age):
        """ Create a new user """
        user = User(key=key, last_name=last_name, first_name=first_name, age=age)

        return user.save()
