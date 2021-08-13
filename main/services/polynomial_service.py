from http import HTTPStatus

from main.models.polynomial import Polynomial


class PolynomialService():
    @staticmethod
    def create(kwargs):
        try:
            polynomial = Polynomial(**kwargs)
            polynomial.parsed_expression = polynomial.parse_expression()
            polynomial.save()

            return {"polynomial_id": polynomial.id}, HTTPStatus.CREATED
        except Exception:
            return {"message": "Something went wrong, try again."}, HTTPStatus.INTERNAL_SERVER_ERROR

    @staticmethod
    def evaluate(polynomial_id, kwargs):
        try:
            polynomial: Polynomial = Polynomial.get_by_id(polynomial_id)

            if polynomial is None:
                return {"message": "Polynomial doesn't exist"}, HTTPStatus.NOT_FOUND

            return {"value": polynomial.calculate_expression(kwargs)}
        except Exception:
            return {"message": "Something went wrong, try again."}, HTTPStatus.INTERNAL_SERVER_ERROR
