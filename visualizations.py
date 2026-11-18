"""Matplotlib visualisations for Gradient Explorer."""
from __future__ import annotations

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

from equation_parser import x, y


def _real_array(values, shape):
    """Convert numeric output to a real array, masking complex/non-finite values."""
    array = np.asarray(values)
    if np.iscomplexobj(array):
        real = np.real(array)
        imaginary = np.imag(array)
        array = np.where(np.abs(imaginary) <= 1e-10, real, np.nan)
    array = np.asarray(array, dtype=float)
    if array.ndim == 0:
        array = np.full(shape, float(array), dtype=float)
    else:
        array = np.broadcast_to(array, shape)
    return np.where(np.isfinite(array), array, np.nan)


def _evaluate_grid(expression: sp.Expr, x_grid: np.ndarray, y_grid: np.ndarray) -> np.ndarray:
    function = sp.lambdify((x, y), expression, modules=["numpy"])
    with np.errstate(all="ignore"):
        values = function(x_grid, y_grid)
    return _real_array(values, x_grid.shape)


def create_contour_plot(expression: sp.Expr, x_value: float, y_value: float,
                        x_range: tuple[float, float] = (-5.0, 5.0),
                        y_range: tuple[float, float] = (-5.0, 5.0),
                        resolution: int = 120):
    """Return a contour figure with a sampled gradient vector field."""
    x_axis = np.linspace(*x_range, resolution)
    y_axis = np.linspace(*y_range, resolution)
    x_grid, y_grid = np.meshgrid(x_axis, y_axis)
    values = _evaluate_grid(expression, x_grid, y_grid)

    derivative_x = sp.lambdify((x, y), sp.diff(expression, x), modules=["numpy"])
    derivative_y = sp.lambdify((x, y), sp.diff(expression, y), modules=["numpy"])
    sample = slice(None, None, max(1, resolution // 18))
    sx, sy = x_grid[sample, sample], y_grid[sample, sample]
    with np.errstate(all="ignore"):
        gx = _real_array(derivative_x(sx, sy), sx.shape)
        gy = _real_array(derivative_y(sx, sy), sy.shape)

    figure, axis = plt.subplots(figsize=(9, 6))
    if np.isfinite(values).any():
        filled = axis.contourf(x_grid, y_grid, values, levels=24, cmap="viridis")
        figure.colorbar(filled, ax=axis, label="f(x, y)")
        finite_values = values[np.isfinite(values)]
        if finite_values.size > 1 and np.ptp(finite_values) > 0:
            axis.contour(x_grid, y_grid, values, levels=12, colors="white", linewidths=0.55, alpha=0.65)
    else:
        axis.text(0.5, 0.5, "No finite values in this plot window", transform=axis.transAxes, ha="center")
    axis.quiver(sx, sy, gx, gy, color="white", alpha=0.85, pivot="mid")
    axis.scatter([x_value], [y_value], color="red", edgecolors="white", s=85, label="Selected point", zorder=5)
    axis.set(xlabel="x", ylabel="y", title="Contour map and gradient field")
    axis.legend(loc="upper right")
    axis.set_aspect("equal", adjustable="box")
    figure.tight_layout()
    return figure


def create_heatmap(expression: sp.Expr, x_range: tuple[float, float] = (-5.0, 5.0),
                   y_range: tuple[float, float] = (-5.0, 5.0), resolution: int = 160):
    """Return a heatmap of the function over the selected coordinate window."""
    x_axis = np.linspace(*x_range, resolution)
    y_axis = np.linspace(*y_range, resolution)
    x_grid, y_grid = np.meshgrid(x_axis, y_axis)
    values = _evaluate_grid(expression, x_grid, y_grid)
    figure, axis = plt.subplots(figsize=(8, 5))
    image = axis.imshow(values, extent=(x_range[0], x_range[1], y_range[0], y_range[1]),
                        origin="lower", aspect="auto", cmap="magma")
    figure.colorbar(image, ax=axis, label="f(x, y)")
    axis.set(xlabel="x", ylabel="y", title="Function heatmap")
    figure.tight_layout()
    return figure


def create_surface_plot(expression: sp.Expr, x_range: tuple[float, float] = (-5.0, 5.0),
                        y_range: tuple[float, float] = (-5.0, 5.0), resolution: int = 70):
    """Return a 3D surface figure; undefined values are masked."""
    x_axis = np.linspace(*x_range, resolution)
    y_axis = np.linspace(*y_range, resolution)
    x_grid, y_grid = np.meshgrid(x_axis, y_axis)
    values = np.ma.masked_invalid(_evaluate_grid(expression, x_grid, y_grid))
    figure = plt.figure(figsize=(9, 6))
    axis = figure.add_subplot(111, projection="3d")
    surface = axis.plot_surface(x_grid, y_grid, values, cmap="viridis", linewidth=0, antialiased=True)
    figure.colorbar(surface, ax=axis, shrink=0.65, label="f(x, y)")
    axis.set(xlabel="x", ylabel="y", zlabel="f(x, y)", title="3D function surface")
    figure.tight_layout()
    return figure
