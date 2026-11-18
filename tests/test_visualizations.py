import matplotlib.pyplot as plt
import pytest

from equation_parser import parse_equation
from visualizations import create_contour_plot, create_heatmap, create_surface_plot


@pytest.mark.parametrize("factory", [create_contour_plot, create_heatmap, create_surface_plot])
def test_visualizations_return_figures(factory):
    expression = parse_equation("x**2 + y**2")
    if factory is create_contour_plot:
        figure = factory(expression, 1.0, 2.0, resolution=30)
    else:
        figure = factory(expression, resolution=30)
    try:
        assert figure.axes
    finally:
        plt.close(figure)


def test_visualizations_handle_singular_grid_regions():
    expression = parse_equation("1/x")
    figure = create_heatmap(expression, resolution=30)
    try:
        assert figure.axes
    finally:
        plt.close(figure)


def test_constant_function_can_be_plotted():
    expression = parse_equation("5")
    figure = create_contour_plot(expression, 0.0, 0.0, resolution=30)
    try:
        assert figure.axes
    finally:
        plt.close(figure)
