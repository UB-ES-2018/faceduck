from faceduck.models.user import User
from werkzeug.security import check_password_hash

def loginUser(user, password):
	
	if User.get(username = user, password = check_password_hash(password)):
        myUser = User.get(username = user, password = check_password_hash(password))
    else if User.get(email = user, password = check_password_hash(password)):
        myUser = User.get(email=user, password=check_password_hash(password))
    if myUser is None:
        raise ValueError

	return newUser