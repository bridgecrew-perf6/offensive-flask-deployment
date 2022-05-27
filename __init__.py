"""
Flask-Cors example
===================
This is a tiny Flask Application demonstrating Flask-Cors, making it simple
to add cross origin support to your flask app!

:copyright: (c) 2016 by Cory Dolphin.
:license:   MIT/X11, see LICENSE for more details.
"""
import imp
from flask import Flask, jsonify, Blueprint, request
import logging
from .models import Model
from .models import Add

try:
    from flask_cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    import os

    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask_cors import CORS


api_v1 = Blueprint("API_v1", __name__)

CORS(api_v1)  # enable CORS on the API_v1 blue print


@api_v1.route("/api/v1/users/")
def list_users():

    return jsonify(user="listening")


@api_v1.route("/api/v1/users/create", methods=["POST"])
def create_user():
    movie_data = request.get_json()
    result = Model(movie_data["description"])
    # print(result)
    return {"result": result}


public_routes = Blueprint("public", __name__)


@public_routes.route("/")
def helloWorld():
    """
    Since the path '/' does not match the regular expression r'/api/*',
    this route does not have CORS headers set.
    """
    return """<h1>Hello CORS!</h1> Read about my spec at the
<a href="http://www.w3.org/TR/cors/">W3</a> Or, checkout my documentation
on <a href="https://github.com/corydolphin/flask-cors">Github</a>"""


logging.basicConfig(level=logging.INFO)
app = Flask("FlaskCorsBlueprintBasedExample")
app.register_blueprint(api_v1)
app.register_blueprint(public_routes)


if __name__ == "__main__":
    app.run(debug=True)

"""
from flask import Flask, jsonify
from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin


def create_app():
    app = Flask(__name__)

    @app.route("/api")
    @cross_origin()
    def api():
        return jsonify({"data": "It is working"})

    @app.route("/add_movie", methods=["POST"])
    @cross_origin()
    def add_movie():
        movie_data = request.get_json()
        return "Done"

    return app
"""
