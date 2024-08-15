import os

from flask import Flask
from .api import bp as api_bp

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(api_bp)
    app.add_url_rule('/', endpoint='api')

    return app