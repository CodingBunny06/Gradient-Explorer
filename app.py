
import streamlit as st
import sympy as sp

from equation_parser import parse_equation, EquationValidationError


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Gradient Explorer",
    page_icon="📈",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📈 Gradient Explorer")

st.markdown(
    "### Interactive Mathematical Visualisation of Gradient and Steepest Ascent"
)

st.write(
    "Explore mathematical functions, evaluate selected points, "
    "and understand the direction of steepest ascent."
)

st.divider()


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.header("1. Function and Coordinates")

with st.container(border=True):

    equation = st.text_input(
        "Mathematical function  f(x, y)",
        value="x**2 + y**2",
        help="Examples: x**2 + y**2, sin(x) + cos(y), x*y"
    )

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

    calculate = st.button(
        "Calculate Gradient",
        type="primary",
        use_container_width=True
    )


# --------------------------------------------------
# RESULTS SECTION
# --------------------------------------------------

if calculate:

    st.divider()
    st.header("2. Mathematical Results")

    try:
        expression = parse_equation(equation)

        st.success("Equation validated successfully!")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Validated Function")
            st.latex(
                rf"f(x,y) = {sp.latex(expression)}"
            )

        with col2:
            st.markdown("#### Evaluation Point")
            st.latex(
                rf"P = ({x_value}, {y_value})"
            )

        st.info(
            "Equation validation is complete. "
            "Gradient calculations will be integrated next."
        )

    except EquationValidationError as error:
        st.error(str(error))


# --------------------------------------------------
# VISUALISATION PLACEHOLDER
# --------------------------------------------------

st.divider()
st.header("3. Visualisation")

st.caption(
    "The graphical visualisation engine will be integrated "
    "in a later development stage."
)

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("Contour Plot")
        st.caption("Contour lines and gradient directions will appear here.")

with col2:
    with st.container(border=True):
        st.subheader("Surface / Heatmap")
        st.caption("The function surface and heatmap will appear here.")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Gradient Explorer | Engineering Mathematics-I Project"
)
