from faceduck.blueprints import api
from faceduck.core import login
import json
from werkzeug.security import generate_password_hash

@api.route('/user', methods=["POST"])
def login():
    req = request.get_json()
    try:
        username = req['username']
        password = req['password']
    except KeyError:
        return json.dumps({'error-id': '400', 'error-message': 'Invalid data submitted'})
    try:
        login.loginUser(username, generate_password_hash(password))
    except ValueError:
        return json.dumps({'error-id': '400', 'error-message': "Invalid username/email or password"})
