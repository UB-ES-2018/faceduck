from faceduck.blueprints import api

@api.route('/')
def index():
    return "hellow"
