from faceduck.blueprints import upload
from faceduck.views.view_utils import client_error
from flask import request, jsonify, current_app, send_from_directory
from faceduck import core
from flask_jwt_extended import jwt_required
import sys

@upload.route('/media', methods=["POST"])
@jwt_required
def upload_media():
    file = None
    if 'file' in request.files:
        file = request.files['file']

    if file is None:
        return client_error("001")

    if file.filename == '':
        return client_error("001")

    media = core.upload_media(file, current_app.config['UPLOAD_FOLDER'], request.host_url)

    return jsonify(media)


@upload.route('/media/<media_filename>')
def serve_media(media_filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], media_filename)
