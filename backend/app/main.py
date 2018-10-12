from flask import Flask
from faceduck.blueprints import all_blueprints
from importlib import import_module
from faceduck import config
from flask_cors import CORS
#import logging

app = Flask(__name__)


# CORS config
#add needed IPs or regExes to origins to allow api cconnection
cors = CORS(app, resources={r"/*": {"origins": ['http://127.0.0.1', 'http://localhost' ,'http://192.168.99.100']}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

#logging.getLogger('flask_cors').level = logging.DEBUG

if __name__ == '__main__':
    for bp in all_blueprints:
        import_module(bp.import_name)
        app.register_blueprint(bp)

    app.run(debug=True, host='0.0.0.0')
