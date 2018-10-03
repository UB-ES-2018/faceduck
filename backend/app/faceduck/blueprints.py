from flask import Blueprint

api = Blueprint("api", "faceduck.views.api")

all_blueprints = (api, )  # Add each new blueprint created here

