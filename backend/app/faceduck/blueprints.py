from flask import Blueprint

api = Blueprint("api", "faceduck.views.api")
upload = Blueprint("upload", "faceduck.views.upload")
sitemap = Blueprint("sitemap", "faceduck.views.sitemap")

all_blueprints = (api, upload, sitemap, )  # Add each new blueprint created here

