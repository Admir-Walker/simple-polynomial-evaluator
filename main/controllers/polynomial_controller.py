from flask_apispec import marshal_with, use_kwargs, doc
from flask_apispec.views import MethodResource
from flask_restful import Resource
from http import HTTPStatus

from main.schemas.default import BaseResponseSchema
from main.schemas.polynomial import PolynomialEvaluateRequestSchema, PolynomialEvaluateResponseSchema, PolynomialRequestSchema, PolynomialResponseSchema
from main.services.polynomial_service import PolynomialService


@doc(tags=['Polynomial'])
class PolynomialListResource(MethodResource, Resource):
    @use_kwargs(PolynomialRequestSchema)
    @marshal_with(PolynomialResponseSchema, code=HTTPStatus.CREATED)
    @marshal_with(BaseResponseSchema, code=HTTPStatus.INTERNAL_SERVER_ERROR)
    def post(self, **kwargs):
        return PolynomialService.create(kwargs)


@doc(tags=['Polynomial'])
@use_kwargs(PolynomialEvaluateRequestSchema, location=('query'))
@marshal_with(PolynomialEvaluateResponseSchema, code=HTTPStatus.OK)
@marshal_with(BaseResponseSchema, code=HTTPStatus.NOT_FOUND)
@marshal_with(BaseResponseSchema, code=HTTPStatus.INTERNAL_SERVER_ERROR)
class PolynomialResource(MethodResource, Resource):
    def get(self, polynomial_id, **kwargs):
        return PolynomialService.evaluate(polynomial_id, kwargs)
