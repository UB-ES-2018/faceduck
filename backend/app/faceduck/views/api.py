import json
from flask import make_response, request
from faceduck.blueprints import api
from faceduck import core
from flask import jsonify
from .mappers import post_mapper, ERRORS


def client_error(error_id):
    return make_response(jsonify(**ERRORS["001"]), 400)


@api.route("/post", methods=["POST"])
def create_post():
    if not request.is_json:
        return client_error("001")
    
    try:
        text = request.json["text"]
        author_id = request.json["author-id"]
    except KeyError:
        return client_error("001")

    try:
        post = core.create_post(text, author_id)
        response = post_mapper(post)
    except ValueError:
        return client_error("001")
    
    return jsonify(response)


@api.route("/post/<post_id>")
def get_post(post_id):
    try:
        post = core.get_post(post_id)
        response = post_mapper(post)
    except ValueError:
        return client_error("001")
    
    return jsonify(response)

