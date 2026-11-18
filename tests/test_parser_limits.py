import pytest

from equation_parser import EquationValidationError, parse_equation


def test_rejects_oversized_exponent():
    with pytest.raises(EquationValidationError):
        parse_equation("x**1000")


def test_rejects_excessive_expression_length():
    with pytest.raises(EquationValidationError):
        parse_equation("x+" + "1+" * 100 + "y")


def test_rejects_non_finite_numeric_literal():
    with pytest.raises(EquationValidationError):
        parse_equation("1e999 + x")
