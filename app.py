"""Streamlit interface for exploring gradients of two-variable functions."""
import matplotlib.pyplot as plt
import streamlit as st
import sympy as sp

from calculations import CalculationError, calculate_directional_derivative, calculate_gradient
from equation_parser import EquationValidationError, parse_equation
from visualizations import create_contour_plot, create_heatmap, create_surface_plot

st.set_page_config(page_title="Gradient Explorer", page_icon="📈", layout="wide")
st.title("📈 Gradient Explorer")
st.markdown("### Interactive mathematical visualisation of gradients and steepest ascent")
st.write("Explore a function of two variables, inspect its partial derivatives, evaluate the gradient at a point, and see how the function changes across a region.")

with st.container(border=True):
    st.subheader("1 · Define your function")
    examples = {
        "Quadratic bowl": "x**2 + y**2",
        "Linear plane": "3*x + 4*y",
        "Saddle surface": "x**2 - y**2",
        "Product surface": "x*y",
        "Trigonometric surface": "sin(x) + cos(y)",
        "Exponential surface": "exp(-x**2 - y**2)",
    }
    if "equation_input" not in st.session_state:
        st.session_state["equation_input"] = "x**2 + y**2"

    def load_example():
        choice = st.session_state["selected_example"]
        if choice in examples:
            st.session_state["equation_input"] = examples[choice]

    selected_example = st.selectbox("Example functions", ["Custom"] + list(examples),
                                    key="selected_example", on_change=load_example)
    equation = st.text_input("Function  f(x, y)", key="equation_input",
        help="Use x and y, numeric constants, pi, E, +, -, *, /, ** and supported functions.")
    with st.expander("Equation syntax guide"):
        st.markdown("**Variables:** x, y  ·  **Constants:** pi, E  ·  **Functions:** sin, cos, tan, exp, log, sqrt, abs")
        st.code("x**2 + y**2\n3*x + 4*y\nsin(x) + cos(y)\nx*y")
        st.caption("Use ** or ^ for powers. Multiplication must be explicit, e.g. 2*x.")

with st.container(border=True):
    st.subheader("2 · Choose an evaluation point")
    left, right = st.columns(2)
    with left:
        x_value = st.number_input("x coordinate", value=1.0, step=0.5, format="%.4f")
    with right:
        y_value = st.number_input("y coordinate", value=2.0, step=0.5, format="%.4f")
    span = st.slider("Plot range (±)", min_value=2, max_value=12, value=5)

calculate = st.button("Calculate gradient", type="primary", use_container_width=True)
if calculate:
    try:
        expression = parse_equation(equation)
        result = calculate_gradient(expression, x_value, y_value)
        st.divider()
        st.header("3 · Mathematical results")
        st.success("Function validated and evaluated successfully.")
        st.latex(r"f(x,y) = " + sp.latex(expression))
        st.latex(r"P = (" + f"{x_value:g}, {y_value:g}" + r")")
        metric1, metric2, metric3 = st.columns(3)
        metric1.metric("Function value", f"{result.function_value:.6g}")
        metric2.metric("Gradient magnitude", f"{result.magnitude:.6g}")
        metric3.metric("Gradient status", "Stationary point" if result.is_stationary else "Non-zero gradient")
        st.subheader("Partial derivatives")
        derivative1, derivative2 = st.columns(2)
        with derivative1:
            st.latex(r"\frac{\partial f}{\partial x} = " + sp.latex(result.derivative_x))
            st.metric("At selected point", f"{result.gradient_x:.6g}")
        with derivative2:
            st.latex(r"\frac{\partial f}{\partial y} = " + sp.latex(result.derivative_y))
            st.metric("At selected point", f"{result.gradient_y:.6g}")
        st.subheader("Gradient vector")
        st.latex(r"\nabla f(" + f"{x_value:g},{y_value:g}" + r") = " + rf"({result.gradient_x:.6g}, {result.gradient_y:.6g})")
        st.latex(r"\left|\nabla f\right| = " + f"{result.magnitude:.6g}")
        if result.unit_gradient is None:
            st.warning("The gradient is zero at this point. The unit gradient and steepest-ascent direction are undefined here.")
        else:
            ux, uy = result.unit_gradient
            st.latex(r"\hat{u}_{\mathrm{ascent}} = " + rf"({ux:.6g}, {uy:.6g})")
            st.latex(r"\hat{u}_{\mathrm{descent}} = " + rf"({-ux:.6g}, {-uy:.6g})")
        with st.expander("Directional derivative"):
            st.write("Enter a direction vector. It is normalized before evaluation.")
            direction_x, direction_y = st.columns(2)
            with direction_x:
                dx = st.number_input("Direction x component", value=1.0, key="direction_x")
            with direction_y:
                dy = st.number_input("Direction y component", value=0.0, key="direction_y")
            if dx == 0 and dy == 0:
                st.info("Enter a non-zero direction vector.")
            else:
                directional = calculate_directional_derivative(expression, x_value, y_value, (dx, dy))
                st.metric("Directional derivative", f"{directional:.6g}")
        st.divider()
        st.header("4 · Visualise the function")
        x_window, y_window = (-float(span), float(span)), (-float(span), float(span))
        tab_contour, tab_heatmap, tab_surface = st.tabs(["Contour + gradient field", "Heatmap", "3D surface"])
        with tab_contour:
            figure = create_contour_plot(expression, x_value, y_value, x_window, y_window)
            st.pyplot(figure, use_container_width=True)
            plt.close(figure)
            st.caption("White arrows show sampled gradient directions; the red marker is your evaluation point.")
        with tab_heatmap:
            figure = create_heatmap(expression, x_window, y_window)
            st.pyplot(figure, use_container_width=True)
            plt.close(figure)
        with tab_surface:
            figure = create_surface_plot(expression, x_window, y_window)
            st.pyplot(figure, use_container_width=True)
            plt.close(figure)
    except (EquationValidationError, CalculationError, ValueError, TypeError) as error:
        st.error("Unable to calculate this function at the selected point.")
        st.warning(str(error))
        with st.expander("Check the equation"):
            st.markdown("Use only x, y, pi, E, supported functions, and +, -, *, /, **. Check that the selected point is inside the real-valued domain.")

with st.expander("How to interpret the gradient"):
    st.markdown("- Partial derivatives measure change along one coordinate direction while the other is fixed.\n- The gradient points in the direction of steepest local increase.\n- Its magnitude is the maximum directional rate of increase.\n- The unit gradient gives direction only and is undefined when the gradient is zero.\n- At regular points, the gradient is perpendicular to a contour line.")
    st.latex(r"\nabla f = \left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\right)")
    st.latex(r"D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}")
st.divider()
st.caption("Gradient Explorer · Engineering Mathematics-I · Python, SymPy, NumPy, Matplotlib and Streamlit")
