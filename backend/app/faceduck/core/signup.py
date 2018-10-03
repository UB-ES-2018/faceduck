from faceduck.models.user import User
from faceduck import blueprints.py
from flask import Response

def validateSignup(user, email, password, name, surname, birthday, gender):
	if User.get(username = user):
		return Response({'error-message':'Username used'}, status=400)
	if User.get(email=email):
		return Response({'error-message':'Email used'}, status=400)
	
	newUser = User(username=user, email=email, password=password, name=name, surname=surname, birthday=birthday, gender=gender)
	newUser.save()
	
	return Response(status=204)