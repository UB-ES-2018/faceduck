from faceduck.blueprints import api
from faceduck.core import signup
from flask import Response
import json

@api.route('/user', methods=["POST"])
def signup():
	req = request.get_json()
	try:
		username = req['username']
		email = req['email']
		password = req['passowrd']
		name = req['name']
		surname = req['surname']
		birthday = req['birthday']
		gender = req['gender']
	except KeyError:
		resp = {'error-id': '400', 'error-message': 'Invalid data submitted'}
		return Response('error-message': 'Invalid data submitted', status=400)
			
	
	return signup.validateSignup(username, email, password, name, surname, birthday, gender)
	
