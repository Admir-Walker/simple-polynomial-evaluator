from flask import Flask, Blueprint
from flask_apispec import FlaskApiSpec
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import ConfigNames

db = SQLAlchemy()

from main.utils.register_endpoints import register_api_endpoints, register_docs, register_endpoints

def create_app(config: ConfigNames = ConfigNames.DEVELOPMENT) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config.value)

    api_bp = Blueprint('api', __name__, url_prefix='/api')
    
    db.init_app(app)

    api = Api(api_bp)
    docs = FlaskApiSpec(app)

    app.register_blueprint(api_bp)
    
    register_endpoints(api, docs, api_bp)
    return app
