from elasticsearch.exceptions import NotFoundError
from faceduck.models.user import User
from faceduck.utils import FaceduckError


def get_user(user_id):
    try:
        user = User.get(id=user_id)
    except NotFoundError:
        raise FaceduckError("001")
    
    return user


def get_all_users():
    return User.search().query("match_all").scan()
