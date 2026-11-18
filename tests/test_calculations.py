import math

import pytest
import sympy as sp

from calculations import (
    CalculationError,
    calculate_directional_derivative,
    calculate_gradient,
)
from equation_parser import parse_equation


@pytest.mark.parametrize(
    "equation, point, expected_gradient, expected_magnitude",
    [
        ("x**2 + y**2", (1, 2), (2, 4), math.sqrt(20)),
        ("3*x + 4*y", (1, 1), (3, 4), 5.0),
        ("x*y", (3, 2), (2, 3), math.sqrt(13)),
        ("x**2 - y**2", (2, 1), (4, -2), math.sqrt(20)),
        ("x**2 + y**2", (0, 0), (0, 0), 0.0),
    ],
)
def test_reference_gradient_cases(equation, point, expected_gradient, expected_magnitude):
    result = calculate_gradient(parse_equation(equation), *point)
    assert (result.gradient_x, result.gradient_y) == pytest.approx(expected_gradient)
    assert result.magnitude == pytest.approx(expected_magnitude)


def test_symbolic_partial_derivatives():
    result = calculate_gradient(parse_equation("x**2*y + sin(y)"), 2, 0)
    assert result.derivative_x == 2 * sp.Symbol("x") * sp.Symbol("y")
    assert result.derivative_y == sp.Symbol("x")**2 + sp.cos(sp.Symbol("y"))


def test_unit_gradient_is_normalized():
    result = calculate_gradient(parse_equation("3*x + 4*y"), 0, 0)
    assert result.unit_gradient == pytest.approx((0.6, 0.8))
    assert math.hypot(*result.unit_gradient) == pytest.approx(1.0)


def test_zero_gradient_has_no_unit_direction():
    result = calculate_gradient(parse_equation("x**2 + y**2"), 0, 0)
    assert result.is_stationary
    assert result.unit_gradient is None


@pytest.mark.parametrize("equation, point", [("1/x", (0, 1)), ("log(x)", (-1, 0)), ("sqrt(x)", (-1, 0))])
def test_undefined_or_non_real_points_are_rejected(equation, point):
    with pytest.raises(CalculationError):
        calculate_gradient(parse_equation(equation), *point)


def test_non_finite_coordinates_are_rejected():
    with pytest.raises(CalculationError):
        calculate_gradient(parse_equation("x+y"), float("inf"), 0)


def test_directional_derivative():
    value = calculate_directional_derivative(parse_equation("3*x + 4*y"), 0, 0, (1, 1))
    assert value == pytest.approx(7 / math.sqrt(2))


def test_directional_derivative_rejects_zero_direction():
    with pytest.raises(CalculationError):
        calculate_directional_derivative(parse_equation("x+y"), 0, 0, (0, 0))
