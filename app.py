import streamlit as st
import sympy as sp

from equation_parser import parse_equation, EquationValidationError

# Page configuration
st.set_page_config(
    page_title="Gradient Explorer",
    page_icon="📈",
    layout="wide"
)

# Application heading
st.title("Gradient Explorer")

st.subheader(
    "Interactive Mathematical Visualisation "
    "of Gradient and Steepest Ascent"
)

st.write(
    "Explore mathematical functions, calculate gradients, "
    "and visualise the direction of steepest ascent."
)

st.divider()

# Equation input
st.header("1. Enter Mathematical Function")

equation = st.text_input(
    "Enter your function f(x, y):",
    value="x**2 + y**2",
    help="Example: x**2 + y**2"
)

# Coordinate selection
st.header("2. Select a Point")

col1, col2 = st.columns(2)

with col1:
    x_value = st.number_input(
        "X coordinate",
        value=1.0,
        step=0.5
    )

with col2:
    y_value = st.number_input(
        "Y coordinate",
        value=2.0,
        step=0.5
    )

st.divider()

# Calculate button
if st.button("Calculate Gradient", type="primary"):

    try:
        # Validate and convert the equation into a SymPy expression
        expression = parse_equation(equation)

        # Display successful validation
        st.success("Equation validated successfully!")

        # Display the validated mathematical function
        st.write("### Validated Function")
        st.latex(f"f(x,y) = {sp.latex(expression)}")

        # Display selected coordinates
        st.write("### Selected Point")
        st.write(f"x = {x_value}, y = {y_value}")

        st.info(
            "Equation validation is complete. "
            "Gradient calculations will be connected in the next stage."
        )

    except EquationValidationError as error:
        st.error(str(error))

st.divider()

st.caption(
    "Gradient Explorer | Engineering Mathematics-I Project"
)
