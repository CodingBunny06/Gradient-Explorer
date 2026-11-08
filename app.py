
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

st.info(
    "If the gradient magnitude is zero, the direction of steepest "
    "ascent cannot be determined using the unit gradient formula."
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
        key="equation_input",
        help="Enter a function using the supported mathematical syntax."
    )
    
    examples = {
        "Quadratic surface": "x**2 + y**2",
        "Linear function": "3*x + 4*y",
        "Product function": "x*y",
        "Difference of squares": "x**2 - y**2",
        "Trigonometric function": "sin(x) + cos(y)"
    }
    def load_example():
        st.session_state["equation_input"] = examples[
            st.session_state["selected_example"]
        ]

    selected_example = st.selectbox(
        "Try an example function",
        options=list(examples.keys()),
        key="selected_example"
    )

    st.button(
        "Load Example",
        on_click=load_example
    )

    with st.expander("📘 Equation input guide"):

        st.markdown("**Supported variables:**")
        st.code("x, y")

        st.markdown("**Supported constants:**")
        st.code("pi, E")

        st.markdown("**Supported mathematical functions:**")
        st.code("sin, cos, tan, exp, log, sqrt, abs")

        st.markdown("**Supported operators:**")
        st.code("+  -  *  /  **")

        st.markdown("**Example equations:**")

        st.code(
            "x**2 + y**2\n"
            "3*x + 4*y\n"
            "sin(x) + cos(y)\n"
            "x*y"
        )

        st.caption(
            "You can use ^ as an alternative to ** for exponents."
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

        st.error("Equation validation failed!")

        st.warning(f"**What went wrong:** {error}")

        with st.expander("How to fix this equation"):
            st.markdown("""
            **Supported variables:** `x`, `y`

            **Supported constants:** `pi`, `E`

            **Supported functions:**
            `sin`, `cos`, `tan`, `exp`, `log`, `sqrt`, `abs`

            **Supported operators:**
            `+`, `-`, `*`, `/`, `**`

            **Examples of valid equations:**

            - `x**2 + y**2`
            - `3*x + 4*y`
            - `sin(x) + cos(y)`
            - `x*y`

            **Remember:** Use `**` or `^` for exponents.
            """)
    st.divider()

st.subheader("3. Understanding the Gradient")

with st.expander("How does gradient work?", expanded=True):

    st.markdown("### 1. Partial Derivatives")

    st.latex(r"\frac{\partial f}{\partial x}")
    st.write(
        "Measures how the function changes with respect to x, "
        "while keeping y constant."
    )

    st.latex(r"\frac{\partial f}{\partial y}")
    st.write(
        "Measures how the function changes with respect to y, "
        "while keeping x constant."
    )

    st.markdown("### 2. Gradient Vector")

    st.latex(
        r"\nabla f(x,y) = "
        r"\left("
        r"\frac{\partial f}{\partial x}, "
        r"\frac{\partial f}{\partial y}"
        r"\right)"
    )

    st.write(
        "The gradient combines both partial derivatives into a vector. "
        "It points in the direction of the steepest increase of the function."
    )

    st.markdown("### 3. Magnitude of the Gradient")

    st.latex(
        r"|\nabla f| = "
        r"\sqrt{\left(\frac{\partial f}{\partial x}\right)^2"
        r"+\left(\frac{\partial f}{\partial y}\right)^2}"
    )

    st.write(
        "The magnitude represents the maximum rate of increase "
        "of the function at a given point."
    )

    st.markdown("### 4. Direction of Steepest Ascent")

    st.latex(
        r"\hat{u} = \frac{\nabla f}{|\nabla f|}"
    )

    st.write(
        "The unit gradient vector gives the direction of steepest ascent. "
        "The opposite direction gives the direction of steepest descent."
    )



# --------------------------------------------------
# VISUALISATION PLACEHOLDER
# --------------------------------------------------

st.divider()
st.header("4. Visualisation")

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
