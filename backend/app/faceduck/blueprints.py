from flask import Blueprint

api = Blueprint("api", "faceduck.views.api")
upload = Blueprint("upload", "faceduck.views.upload")
sitemap = Blueprint("sitemap", "faceduck.views.sitemap")
testing = Blueprint("testing", "faceduck.views.testing")

all_blueprints = (api, upload, sitemap, )  # Add each new blueprint created here

