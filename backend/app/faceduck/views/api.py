from flask import make_response, request
from flask import jsonify
from faceduck.blueprints import api
from faceduck import core
from .mappers import ERRORS
from faceduck.utils import FaceduckError
from faceduck.core import login
import json
from werkzeug.security import generate_password_hash


def client_error(error_id):
    return make_response(jsonify(**ERRORS[error_id]), 400)


@api.route('/user', methods=["POST"])
def signup():
    if not request.is_json:
        return client_error("001")
    
    try:
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        name = request.json['name']
        surname = request.json['surname']
        birthday = request.json['birthday']
        gender = request.json['gender']
    except KeyError:
        return client_error("001")

    try:
        user = core.create_user(username, email, password, name,
                                surname, birthday, gender)
    except FaceduckError as e:
        return client_error(e.id)
    
    return ("", 204)


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
