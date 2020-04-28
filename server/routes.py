# routes.py attaches the views to the routes. It is invoked during server configuration
# (eg at server startup time)

import flask
import server.views as views


def setup_routes(app: flask.Flask) -> flask.Flask:
    """
    setup_routes attaches our views to our routes

    docs => https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing
    """
    app.route("/user", methods=["POST"])(views.create_user)
    app.route("/user", methods=["GET"])(views.get_users)
    return app