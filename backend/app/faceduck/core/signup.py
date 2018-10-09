from faceduck.models.user import User
import uuid

def createUser(user, email, password, name, surname, birthday, gender):

    if User.get(email = email, ignore="404") is not None:
        raise ValueError
    if User.get(username=user, ignore="404") is not None:
        raise ValueError

    newUser = User(meta={'id': uuid.uuid4()}, username=user, email=email, password=password, name=name, surname=surname,
                   birthday=birthday, gender=gender)
    newUser.save()

    return newUser
