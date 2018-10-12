from faceduck.models.user import User
from flask_jwt_extended import (
    create_access_token
)


class SessionKeeping:
    @staticmethod
    def identity(uid):
        return User.get(id=uid)

    @staticmethod
    def generate_jwt_token(uid):
        return create_access_token(uid)

