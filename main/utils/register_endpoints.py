from flask_restful import Api
from flask_apispec import FlaskApiSpec


def register_api_endpoints(api: Api):
    pass


def register_docs(docs: FlaskApiSpec):
    pass


def register_endpoints(api: Api, docs: FlaskApiSpec):
    register_api_endpoints(api)
    register_docs(docs)
