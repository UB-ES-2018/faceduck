from faceduck.models.user import User

def createUser(user, email, password, name, surname, birthday, gender):

	newUser = None
	
	try{
		User.get(username = user):
		User.get(email=email):
	except ValueError:
		return newUser
	
	newUser = User(username=user, email=email, password=password, name=name, surname=surname, birthday=birthday, gender=gender)
	newUser.save()
	
	return newUser