from flask import request
from faceduck.blueprints import testing


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@testing.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
