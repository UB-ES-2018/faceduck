from datetime import datetime
import uuid
from elasticsearch.exceptions import NotFoundError
from faceduck.models.post import Post
from faceduck.models.user import User


def create_user(user, email, password, name, surname, birthday, gender):
    id = uuid.uuid4()
    user = User(meta={'id': id}, username=user, email=email, password=password, name=name,
                surname=surname, birthday=birthday, gender=gender)
    user.save()
    
    return user


def get_user(user_id):
    try:
        user = User.get(id=user_id)
    except NotFoundError:
        raise ValueError
    
    return user
        
