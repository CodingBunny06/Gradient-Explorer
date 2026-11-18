# Gradient Explorer
## Project Report

**Project title:** Gradient Explorer — Interactive Mathematical Visualisation of Gradient and Steepest Ascent  
**Project type:** Engineering Mathematics-I mini project  
**Implementation:** Python, SymPy, NumPy, Matplotlib, Streamlit and Pytest  
**Author:** CodingBunny06

## 1. Abstract

Gradient Explorer is an interactive application for studying gradients of scalar functions of two variables. It accepts a mathematical expression and an evaluation point, calculates symbolic partial derivatives and numerical gradient properties, and presents the function through contour, heatmap, and three-dimensional surface plots.

The application connects the analytical definition of the gradient with its geometric interpretation as the direction of steepest local increase.

## 2. Problem statement

Students may find it difficult to connect partial derivative calculations with the geometry of a function surface. Gradient Explorer provides a visual and numerical environment for exploring these relationships at selected points and over a coordinate region.

## 3. Objectives

1. Accept functions of two variables.
2. Validate supported mathematical expressions safely.
3. Calculate symbolic partial derivatives.
4. Evaluate the function and gradient at a selected point.
5. Calculate gradient magnitude and unit ascent direction.
6. Calculate directional derivatives.
7. Visualise the function using contour, heatmap, gradient-field, and 3D surface plots.
8. Handle zero-gradient and undefined/non-real cases.
9. Verify behaviour with automated tests.

## 4. Mathematical foundation

For a scalar function f(x,y), the gradient is:

\[
\\nabla f(x,y)=\\left(\\frac{\\partial f}{\\partial x},\\frac{\\partial f}{\\partial y}\\right)
\]

Its magnitude is:

\[
\\lVert\\nabla f\\rVert=\\sqrt{\\left(\\frac{\\partial f}{\\partial x}\\right)^2+\\left(\\frac{\\partial f}{\\partial y}\\right)^2}
\]

When the magnitude is non-zero, the unit gradient indicates steepest ascent:

\[
\\hat{u}=\\frac{\\nabla f}{\\lVert\\nabla f\\rVert}
\]

The directional derivative along a unit vector u is:

\[
D_{\\mathbf{u}}f=\\nabla f\\cdot\\mathbf{u}
\]

At a zero-gradient point, the unit gradient is undefined.

## 5. Technology stack

| Technology | Role |
|---|---|
| Python | Application logic |
| Streamlit | User interface |
| SymPy | Symbolic expressions and differentiation |
| NumPy | Numerical coordinate grids |
| Matplotlib | Mathematical visualisations |
| Pytest | Automated testing |
| GitHub Actions | Continuous integration |

## 6. System implementation

### 6.1 Equation parser

The parser converts user input into a SymPy expression through Python's AST module. It permits only a defined set of variables, constants, functions, and operators. It does not use eval to execute user input. Input length, syntax-tree size, nesting depth, and numeric exponent magnitude are bounded.

### 6.2 Calculation engine

The calculation module computes partial derivatives with SymPy and evaluates the function and derivative values at the selected point. It calculates gradient magnitude, unit ascent direction, and directional derivatives. Zero gradients are represented without division by zero; undefined or non-real point evaluations are reported.

### 6.3 Visualisation engine

The visualisation module evaluates the function and its derivatives over NumPy coordinate grids. It produces a contour plot with gradient arrows and a selected-point marker, a heatmap, and a three-dimensional surface. Non-finite grid values are masked.

### 6.4 Streamlit interface

The interface collects the expression, point, and plot range. It presents symbolic derivatives, numerical values, gradient direction, directional derivative controls, and plot tabs.

## 7. Verification

Automated tests cover:
- Supported and unsupported equation syntax.
- Mathematical reference cases for quadratic, linear, product, and saddle functions.
- Symbolic partial derivatives.
- Gradient magnitude and normalized direction.
- Zero-gradient behaviour.
- Undefined and non-real points.
- Non-finite coordinates.
- Directional derivatives and invalid direction vectors.
- Parser resource limits, including expression length, syntax-tree size, nesting depth, and exponent magnitude.
- Visualisation outputs, including constant functions and grids containing singular or non-finite values.

The GitHub Actions run for the implementation pull request completed successfully: **36 tests passed** on Python 3.12. The run is available at [GitHub Actions run #15](https://github.com/CodingBunny06/Gradient-Explorer/actions/runs/44284095884).

## 8. Example result

For f(x,y) = x² + y² at (1,2):

- ∂f/∂x = 2x
- ∂f/∂y = 2y
- Gradient = (2,4)
- Magnitude = √20 ≈ 4.4721
- Unit ascent direction = (1/√5, 2/√5)

## 9. Limitations

- The equation parser supports a restricted mathematical syntax and does not support arbitrary Python, implicit multiplication, or every SymPy function.
- Plots show numerical samples over a finite coordinate window.
- A mathematically defined symbolic expression may be undefined or non-real at a selected point.
- Visualisations are educational aids and use numerical approximations.

## 10. Future scope

Potential extensions include gradient-ascent path tracing, additional supported functions, configurable plot sampling, and more advanced critical-point analysis.

## 11. Conclusion

Gradient Explorer combines safe mathematical input, symbolic differentiation, numerical gradient evaluation, and graphical representations in one application. It helps users relate the gradient's analytical definition to its magnitude, direction, and geometric behaviour over a function surface.

## 12. References

1. James Stewart, *Calculus: Early Transcendentals*.
2. SymPy documentation — https://docs.sympy.org/
3. Streamlit documentation — https://docs.streamlit.io/
4. NumPy documentation — https://numpy.org/doc/
5. Matplotlib documentation — https://matplotlib.org/stable/
6. Pytest documentation — https://docs.pytest.org/
