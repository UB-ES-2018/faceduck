import logging
import uuid
from elasticsearch.exceptions import NotFoundError
from faceduck.models.user import User
from faceduck.utils import FaceduckError


def create_user(username, email, password, name, surname, birthday, gender):
    username_response = User.search().from_dict({
        "query": {
            "term": {
                "username": username
            }
        }
    }).execute()

    if len(username_response) != 0:
        raise FaceduckError("002")
    
    email_response = User.search().from_dict({
        "query": {
            "term": {
                "email": email
            }
        }
    }).execute()
    
    if len(email_response) != 0:
        raise FaceduckError("003")
    
    id = uuid.uuid4()
    user = User(meta={'id': id}, username=username, email=email, password=password,
                name=name, surname=surname, birthday=birthday, gender=gender)
    user.save()
    
    return user

