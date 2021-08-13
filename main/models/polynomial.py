import re

from .. import db
from main.utils.mixins import CrudMixin


class Polynomial(CrudMixin, db.Model):

    allowed_variables = ['x', 'y']
    calculated_values_dict = {}

    expression = db.Column(db.String(), nullable=False)
    parsed_expression = db.Column(db.String(), nullable=False)

    def parse_expression(self):
        expression = ' ' + self.expression
        for replacement in self.make_replacements():
            expression = expression.replace(*replacement)
        return expression

    def make_replacements(self):
        replacements = []
        for variable in self.allowed_variables:
            replacements.append((f'+{variable}', f'+1{variable}'))
            replacements.append((f'-{variable}', f'-1{variable}'))
            replacements.append((f' {variable}', f'1{variable}'))
            replacements.append((variable, f'*{variable}'))
        return replacements

    def calculate_expression(self, values):
        self.init_memo(values)

        result = 0.0
        expression_length = len(self.parsed_expression)
        # starting index of monomial
        starting_index = 0
        breaks = ['+', '-']

        # Break polynomial into monomials
        for i in range(expression_length):
            if self.parsed_expression[i] in breaks and i > 1 and self.parsed_expression[i-1] != '^':
                result += self.evaluate_monomial(
                    self.parsed_expression[starting_index:i])
                starting_index = i
            elif i == expression_length - 1:
                result += self.evaluate_monomial(
                    self.parsed_expression[starting_index:i+1])
                starting_index = i

        return result

    # Value gets stored so it can be reused again
    def init_memo(self, values):
        for variable in self.allowed_variables:
            self.calculated_values_dict[variable] = {}
            self.calculated_values_dict[variable]['1'] = values[variable]
            if values[variable] != 0.0:
                self.calculated_values_dict[variable]['-1'] = 1 / \
                    values[variable]

    # We get monomial in const * x * y form
    def evaluate_monomial(self, monomial):
        monomial = monomial.split('*')
        evaluation = float(monomial[0].replace(' ', ''))
        for i in range(1, len(monomial)):
            evaluation *= self.evaluate_variable(monomial[i].strip())
        return evaluation

    # We get monomial parts in 'variable^exponent' form
    def evaluate_variable(self, variable):
        variable = variable.split('^')
        if len(variable) > 1:
            return self.power(variable[0], int(variable[1]))
        return self.power(variable[0])

    def power(self, symbol, exponent=1):
        if exponent == 0.0:
            return 1.0

        calculated = self.is_calculated(symbol, exponent)

        if calculated is not None:
            return calculated

        if exponent > 0:
            return self.power_positive(symbol, exponent)
        return self.power_negative(symbol, exponent)

    def is_calculated(self, symbol, exponent):
        return self.calculated_values_dict[symbol].get(str(exponent))

    def save_calculated_value(self, symbol, exponent, incrementor):
        if (exponent % 2) == 0:
            self.calculated_values_dict[symbol][str(exponent)] = self.power(
                symbol, exponent // 2) ** 2
        else:
            self.calculated_values_dict[symbol][str(exponent)] = self.power(
                symbol, incrementor) * self.power(symbol, exponent - incrementor)

        return self.calculated_values_dict[symbol][str(exponent)]

    def power_positive(self, symbol, exponent=1):
        return self.save_calculated_value(symbol, exponent, 1)

    def power_negative(self, symbol, exponent=-1):
        return self.save_calculated_value(symbol, exponent, -1)
