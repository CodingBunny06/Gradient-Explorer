
from equation_parser import parse_equation, EquationValidationError
import sympy as sp


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
    try:
        parse_equation("x**2 + z**2")
        assert False, "Expected validation error"
    except EquationValidationError:
        pass


def test_unsafe_input():
    try:
        parse_equation("print(x)")
        assert False, "Expected validation error"
    except EquationValidationError:
        pass


def test_empty_input():
    try:
        parse_equation("")
        assert False, "Expected validation error"
    except EquationValidationError:
        pass
