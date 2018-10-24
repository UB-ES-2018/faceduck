from flask import Blueprint

api = Blueprint("api", "faceduck.views.api")
upload = Blueprint("upload", "faceduck.views.upload")

all_blueprints = (api, upload, )  # Add each new blueprint created here

