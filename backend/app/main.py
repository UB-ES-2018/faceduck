from flask import Flask
from faceduck.blueprints import all_blueprints
from importlib import import_module
from faceduck import config

app = Flask(__name__)

if __name__ == '__main__':
    for bp in all_blueprints:
        import_module(bp.import_name)
        app.register_blueprint(bp)

    app.run(debug=True, host='0.0.0.0')
