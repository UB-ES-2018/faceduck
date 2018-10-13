from flask import make_response, request, jsonify
from faceduck.blueprints import api
from faceduck import core
from faceduck.utils import FaceduckError
from .mappers import ERRORS, post_mapper


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


@api.route("/post", methods=["POST"])
def create_post():
    if not request.is_json:
        return client_error("001")
    
    try:
        text = request.json["text"]
        author_id = request.json["author-id"]
    except ValueError:
        return client_error("001")

    try:
        post = core.create_post(text, author_id)
        response = post_mapper(post)
    except FaceduckError as e:
        return client_error(e.id)
    
    return jsonify(response)


@api.route("/post/<post_id>")
def get_post(post_id):
    try:
        post = core.get_post(post_id)
        response = post_mapper(post)
    except FaceduckError as e:
        return client_error(e.id)
    
    return jsonify(response)
