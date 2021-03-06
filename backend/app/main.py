import os
from flask import Flask
from faceduck.blueprints import all_blueprints, testing
from importlib import import_module
from flask_cors import CORS
from faceduck.core.sessionkeeping import SessionKeeping
from flask_jwt_extended import (
    JWTManager
)
from faceduck import config # Needed for autoconfiguration

app = Flask(__name__, template_folder="faceduck/templates")

is_testing = os.environ.get("CI")
app.config['TESTING'] = True
app.config['JWT_SECRET_KEY'] = '1234567'
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False

jwt = JWTManager(app)


@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    return SessionKeeping.identity(identity)


# CORS config
# add needed IPs or regExes to origins to allow api cconnection
cors = CORS(app, resources={r"/*": {"origins": ['http://127.0.0.1:8080', 'http://localhost:8080' ,'http://192.168.99.100:8080', 'http://faceduck.xyz', 'https://faceduck.xyz']}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == '__main__':
    for bp in all_blueprints:
        import_module(bp.import_name)
        app.register_blueprint(bp)
    
    if is_testing:
        import_module(testing.import_name)
        app.register_blueprint(testing)
        
        debug = False
    else:
        debug = True
    
    app.run(host='0.0.0.0', debug=debug)

