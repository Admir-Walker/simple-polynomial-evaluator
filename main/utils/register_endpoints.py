from flask.blueprints import Blueprint
from flask_restful import Api
from flask_apispec import FlaskApiSpec

from main.controllers.polynomial_controller import PolynomialListResource, PolynomialResource


def register_api_endpoints(api: Api):
    api.add_resource(PolynomialListResource, '/poly')
    api.add_resource(PolynomialResource, '/poly/eval/<int:polynomial_id>')


def register_docs(docs: FlaskApiSpec, blueprint_name: str):
    docs.register(PolynomialListResource, blueprint=blueprint_name)
    docs.register(PolynomialResource, blueprint=blueprint_name)


def register_endpoints(api: Api, docs: FlaskApiSpec, blueprint: Blueprint):
    register_api_endpoints(api)
    register_docs(docs, blueprint.name)
