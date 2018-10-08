from faceduck.models.user import User
import uuid

def createUser(user, email, password, name, surname, birthday, gender):
		newUser = User({meta='id': uuid.uuid4()},  username=user, email=email, password=password, name=name, surname=surname, birthday=birthday, gender=gender)
		newUser.save()
	
	return newUser