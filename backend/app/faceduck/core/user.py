from elasticsearch.exceptions import NotFoundError
from faceduck.models.user import User


def get_user(user_id):
    try:
        user = User.get(id=user_id)
    except NotFoundError:
        raise ValueError
    
    return user
