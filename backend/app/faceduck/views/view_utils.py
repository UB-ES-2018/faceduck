from flask import make_response, jsonify
from .mappers import ERRORS


def client_error(error_id):
    return make_response(jsonify(**ERRORS[error_id]), 400)
