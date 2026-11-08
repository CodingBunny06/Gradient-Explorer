from equation_parser import x, y
import pytest
import sympy as sp

from equation_parser import parse_equation, EquationValidationError


def test_basic_equation():
    expression = parse_equation("x**2 + y**2")
    assert expression == sp.Symbol("x")**2 + sp.Symbol("y")**2


def test_caret_notation():
    expression = parse_equation("x^2 + y^2")
    assert expression == sp.Symbol("x")**2 + sp.Symbol("y")**2


def test_math_function():
    expression = parse_equation("sin(x) + cos(y)")
    assert expression == sp.sin(sp.Symbol("x")) + sp.cos(sp.Symbol("y"))


def test_invalid_variable():
    with pytest.raises(EquationValidationError):
        parse_equation("x**2 + z**2")


def test_unsafe_input():
    with pytest.raises(EquationValidationError):
        parse_equation("print(x)")


def test_empty_input():
    with pytest.raises(EquationValidationError):
        parse_equation("")


def test_allowed_constants():
    expression = parse_equation("x + pi + E")
    assert expression == x + sp.pi + sp.E


def test_all_supported_functions():
    expression = parse_equation(
        "tan(x) + exp(y) + log(x) + sqrt(y) + abs(x)"
    )

    assert expression == (
        sp.tan(x) + sp.exp(y) + sp.log(x)
        + sp.sqrt(y) + sp.Abs(x)
    )


def test_unsupported_function():
    with pytest.raises(EquationValidationError):
        parse_equation("factorial(x)")


def test_unsupported_operator():
    with pytest.raises(EquationValidationError):
        parse_equation("x // y")


def test_multiple_function_arguments():
    with pytest.raises(EquationValidationError):
        parse_equation("sin(x, y)")


def test_exponent_limit():
    with pytest.raises(EquationValidationError):
        parse_equation("x**101")


def test_boolean_input():
    with pytest.raises(EquationValidationError):
        parse_equation("True + x")


def test_invalid_syntax():
    with pytest.raises(EquationValidationError):
        parse_equation("x + * y")
