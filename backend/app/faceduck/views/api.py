from faceduck.blueprints import api
from faceduck.core import signup
import json
import uuid

@api.route('/user', methods=["POST"])
def signup():
	req = request.get_json()
	try:
		id = uuid.uuid4()
		username = req['username']
		email = req['email']
		password = req['password']
		name = req['name']
		surname = req['surname']
		birthday = req['birthday']
		gender = req['gender']
	except KeyError:
		return json.dumps({'error-id': '400', 'error-message': 'Invalid data submitted'})
	
	try:
		signup.createUser(id, username, email, password, name, surname, birthday, gender)
	except ValueError:
		return json.dumps({'error-id': '400', 'error-message': "Username or Email already used"})