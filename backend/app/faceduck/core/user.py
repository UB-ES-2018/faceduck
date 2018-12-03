from elasticsearch.exceptions import NotFoundError
from faceduck.models.user import User
from faceduck.utils import FaceduckError
from .signup import email_already_exists


def get_user(user_id):
    try:
        user = User.get(id=user_id)
    except NotFoundError:
        raise FaceduckError("001")
    
    return user


def get_all_users():
    return User.search().query("match_all").scan()

def get_login_logs(user_id):
    user = get_user(user_id)
    return user.get_login_logs()

def edit_user(user_id, newData):
    user = get_user(user_id)
    for key in newData.keys():
        if key == "username":
            user.username = newData[key]
        elif key == "email":
            if email_already_exists(newData[key]):
                raise FaceduckError("003") 
            user.email = newData[key]
        elif key == "name":
            user.name = newData[key]
        elif key == "surname":
            user.surname = newData[key]
        elif key == "birthday":
            user.birthday = newData[key]
        elif key == "gender":
            user.gender = newData[key]
        elif key == "image-url":
            user.image_url = newData[key]
    user.save()
    return user