import uuid
from werkzeug.security import generate_password_hash
from faceduck.models.user import User
from faceduck.utils import FaceduckError


def username_already_exists(username):
    username_response = User.search().from_dict({
        "query": {
            "match_phrase": {
                "username": username
            }
        }
    }).execute()

    return len(username_response.hits) > 0


def email_already_exists(email):
    email_response = User.search().from_dict({
        "query": {
            "match_phrase": {
                "email": email
            }
        }
    }).execute()

    return len(email_response.hits) > 0


def create_user(username, email, password, name, surname, birthday, gender):
    if username_already_exists(username):
        raise FaceduckError("002")

    if email_already_exists(email):
        raise FaceduckError("003")
    
    id = uuid.uuid4()
    password = generate_password_hash(password)
    user = User(meta={'id': id}, username=username, email=email, password=password,
                name=name, surname=surname, birthday=birthday, gender=gender)
    user.save()
    
    return user
