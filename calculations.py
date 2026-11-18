"""Symbolic and numerical gradient calculations for two-variable functions."""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable

import sympy as sp

from equation_parser import x, y


class CalculationError(ValueError):
    """Raised when a function cannot be evaluated at the requested point."""


@dataclass(frozen=True)
class GradientResult:
    """Symbolic and numerical gradient information at one point."""

    expression: sp.Expr
    derivative_x: sp.Expr
    derivative_y: sp.Expr
    function_value: float
    gradient_x: float
    gradient_y: float
    magnitude: float
    unit_gradient: tuple[float, float] | None

    @property
    def is_stationary(self) -> bool:
        return self.magnitude == 0.0


def _finite_real(value: object, label: str) -> float:
    """Convert a SymPy/numeric value to a finite real float."""
    try:
        evaluated = complex(sp.N(value))
    except (TypeError, ValueError, OverflowError) as error:
        raise CalculationError(f"{label} could not be evaluated as a real number.") from error

    if not (math.isfinite(evaluated.real) and math.isfinite(evaluated.imag)):
        raise CalculationError(f"{label} is undefined or non-finite at this point.")
    if abs(evaluated.imag) > 1e-10:
        raise CalculationError(f"{label} is not real at this point.")
    return float(evaluated.real)


def calculate_gradient(
    expression: sp.Expr,
    x_value: float,
    y_value: float,
) -> GradientResult:
    """Differentiate expression symbolically and evaluate its gradient at (x, y)."""
    if not isinstance(expression, sp.Expr):
        raise TypeError("expression must be a SymPy expression.")
    try:
        coordinates = {x: float(x_value), y: float(y_value)}
    except (TypeError, ValueError, OverflowError) as error:
        raise CalculationError("Coordinates must be finite real numbers.") from error

    if not all(math.isfinite(value) for value in coordinates.values()):
        raise CalculationError("Coordinates must be finite real numbers.")

    derivative_x = sp.diff(expression, x)
    derivative_y = sp.diff(expression, y)
    try:
        function_value = _finite_real(expression.subs(coordinates), "Function value")
        gradient_x = _finite_real(derivative_x.subs(coordinates), "Partial derivative ∂f/∂x")
        gradient_y = _finite_real(derivative_y.subs(coordinates), "Partial derivative ∂f/∂y")
    except (ZeroDivisionError, OverflowError) as error:
        raise CalculationError("The function is undefined at the selected point.") from error

    magnitude = math.hypot(gradient_x, gradient_y)
    unit_gradient = (
        (gradient_x / magnitude, gradient_y / magnitude)
        if magnitude > 0.0
        else None
    )

    return GradientResult(
        expression=expression,
        derivative_x=derivative_x,
        derivative_y=derivative_y,
        function_value=function_value,
        gradient_x=gradient_x,
        gradient_y=gradient_y,
        magnitude=magnitude,
        unit_gradient=unit_gradient,
    )


def calculate_directional_derivative(
    expression: sp.Expr,
    x_value: float,
    y_value: float,
    direction: Iterable[float],
) -> float:
    """Evaluate the directional derivative along a supplied non-zero direction."""
    try:
        components = tuple(float(component) for component in direction)
    except (TypeError, ValueError, OverflowError) as error:
        raise CalculationError("Direction must contain two finite real numbers.") from error
    if len(components) != 2 or not all(math.isfinite(value) for value in components):
        raise CalculationError("Direction must contain two finite real numbers.")

    length = math.hypot(*components)
    if length == 0.0:
        raise CalculationError("Direction vector must be non-zero.")

    result = calculate_gradient(expression, x_value, y_value)
    return result.gradient_x * components[0] / length + result.gradient_y * components[1] / length
