from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    api = swagger.docs(Api(app), apiVersion="0.1", api_spec_url="/api/spec")

    from app.api import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api")

    from app import views, models

    return app