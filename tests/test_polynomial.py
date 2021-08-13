from flask import json
from flask.testing import FlaskClient
from http import HTTPStatus


def create(client: FlaskClient, expression):
    return client.post('/api/poly', json=dict(expression=expression))


def get(client: FlaskClient, polynomial_id, x, y):
    return client.get(f'/api/poly/eval/{polynomial_id}', query_string=dict(x=x, y=y))


# Generate sum(x^i * y^j)
def generate_sum_expression(i_range, j_range):
    expression = ''
    for i in range(i_range):
        for j in range(j_range):
            expression += f'x^{i}y^{j} + '

    def sum_evaluation(x, y):
        result = 0.0
        for i in range(i_range):
            for j in range(j_range):
                result += x**i * y**j
        return result

    return expression[:len(expression)-2], sum_evaluation


def test_post_poly_created(client: FlaskClient):
    res = create(client, 'x+y')
    assert res.status_code == HTTPStatus.CREATED


def test_get_poly_not_found(client: FlaskClient):
    res = get(client, 0, 0, 0)
    assert res.status_code == HTTPStatus.NOT_FOUND


def post_and_evaluation(client: FlaskClient, expression, x, y, expectedResult):
    post_response = create(client, expression)

    assert post_response.status_code == HTTPStatus.CREATED

    post_data = json.loads(post_response.data)
    polynomial_id = post_data['polynomial_id']

    get_response = get(client, polynomial_id, x, y)

    assert get_response.status_code == HTTPStatus.OK

    get_data = json.loads(get_response.data)
    value = get_data['value']

    assert value == expectedResult


def test_simple_expression(client: FlaskClient):
    post_and_evaluation(client, '1 + x + y', 0, 0, 1.0)


def test_constant_expression(client: FlaskClient):
    post_and_evaluation(client, '55', 100, 100, 55.0)


def test_complex_expression(client: FlaskClient):
    post_and_evaluation(client, '1 + x^5y^3 - 5x + 11y + 33yx', 1, 1, 41.0)


def test_big_exponents_expression(client: FlaskClient):
    post_and_evaluation(client, '0.1x^222 - 0.5x^100y^100',
                        10, 10, 1.0000000000000006e+221)


def test_zero_expression(client: FlaskClient):
    post_and_evaluation(client, 'x + y - x - y', 50, 50, 0.0)


def test_first_negative_expression(client: FlaskClient):
    post_and_evaluation(client, '-x+y-1', 0.1, 0.1, -1)


def test_negative_exponents_expression(client: FlaskClient):
    post_and_evaluation(client, '-x+y^-5-1', 0.1, 0.1, 99998.9)


def test_large_expression(client: FlaskClient):
    x, y = 5, 5
    expression, sum_eval = generate_sum_expression(10, 10)
    post_and_evaluation(client, expression, x, y, sum_eval(x, y))
