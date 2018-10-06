from faceduck.models.user import User


class SessionKeeping:
    @staticmethod
    def identity(uid):
        return User.get(id=uid)

