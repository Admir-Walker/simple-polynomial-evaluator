from marshmallow import Schema, fields


class PolynomialRequestSchema(Schema):
    expression = fields.Str(required=True)


class PolynomialEvaluateRequestSchema(Schema):
    x = fields.Float(required=True, default=0.0)
    y = fields.Float(required=True, default=0.0)


class PolynomialResponseSchema(Schema):
    polynomial_id = fields.Int()


class PolynomialEvaluateResponseSchema(Schema):
    value = fields.Float(required=True, default=0.0)
