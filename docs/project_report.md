
# Gradient Explorer
## Project Report

**Project Title:** Gradient Explorer – Interactive Mathematical Visualisation of Gradient and Steepest Ascent

**Project Type:** Engineering Mathematics Mini Project

**Technology:** Python, SymPy, NumPy, Matplotlib and Streamlit

---

# 1. Abstract

Gradient Explorer is an interactive mathematical visualisation project designed to demonstrate the concept of gradients and steepest ascent for functions of two variables.

The project aims to help students understand how partial derivatives are used to calculate the gradient vector at a given point on a surface. It also aims to demonstrate gradient magnitude, direction and the relationship between gradients and contour lines.

The application is being developed using Python and its mathematical libraries, with Streamlit providing the user interface.

The current implementation includes a Streamlit interface and a safe mathematical equation parser. The mathematical calculation and visualisation modules are planned components of the project.

# 2. Introduction

Calculus plays an important role in engineering, mathematics and scientific applications.

For functions of two variables, partial derivatives describe how a function changes with respect to one variable while keeping the other variable constant.

The gradient combines these partial derivatives into a vector that indicates the direction of the greatest rate of increase of a function.

Gradient Explorer aims to make this mathematical concept easier to understand through an interactive software application.

# 3. Problem Statement

Students often find it difficult to visualise how partial derivatives, gradient vectors and steepest ascent relate to a mathematical surface.

Traditional mathematical calculations provide numerical answers but may not always make the geometric interpretation clear.

The project aims to develop an interactive application that accepts mathematical functions and coordinates, calculates gradient properties and presents their graphical interpretation.

# 4. Objectives

The main objectives are:

1. Develop an interactive mathematical application.
2. Accept functions of two variables, x and y.
3. Validate mathematical expressions safely.
4. Calculate partial derivatives.
5. Determine gradient vectors at selected points.
6. Calculate gradient magnitude and unit gradient vectors.
7. Visualise functions using heatmaps and contour plots.
8. Demonstrate the direction of steepest ascent.

# 5. Mathematical Foundation

## 5.1 Functions of Two Variables

A function of two variables is represented as:

f(x, y)

It assigns a numerical value to each valid pair of input coordinates.

## 5.2 Partial Derivatives

The partial derivative with respect to x measures the rate of change of the function with respect to x while y remains constant.

Similarly, the partial derivative with respect to y measures the rate of change with respect to y while x remains constant.

## 5.3 Gradient Vector

The gradient of a function is defined as:

∇f(x,y) = (∂f/∂x, ∂f/∂y)

It points in the direction of the steepest increase of the function.

## 5.4 Gradient Magnitude

The magnitude of the gradient is:

|∇f| = √((∂f/∂x)² + (∂f/∂y)²)

It represents the maximum rate of increase of the function at a point.

## 5.5 Unit Gradient Vector

The unit gradient vector is:

u = ∇f / |∇f|

It represents the direction of steepest ascent.

This vector is undefined when the gradient magnitude is zero.

# 6. Technology Stack

| Technology | Application |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive user interface |
| SymPy | Symbolic mathematics |
| NumPy | Numerical calculations |
| Matplotlib | Mathematical visualisation |
| Pytest | Automated testing |
| Git and GitHub | Version control and collaboration |
| GitHub Actions | Continuous integration |

# 7. System Architecture

The application follows a modular architecture.

The planned modules include:

- app.py: Main Streamlit application.
- equation_parser.py: Mathematical expression validation.
- calculations.py: Partial derivatives and gradient calculations.
- visualizations.py: Heatmaps, contour plots and gradient vectors.
- tests/: Automated testing.
- docs/: Technical and mathematical documentation.

The intended workflow begins with user input, followed by equation validation, mathematical calculations and graphical visualisation.

# 8. Implementation

## 8.1 Streamlit Interface

A basic Streamlit interface has been implemented to accept mathematical expressions and coordinate values.

The interface includes:
- Mathematical equation input.
- X-coordinate input.
- Y-coordinate input.
- Calculate Gradient button.
- Equation validation feedback.

## 8.2 Equation Parser

A mathematical equation parser has been implemented using Python's Abstract Syntax Tree (AST) module and SymPy.

It supports approved mathematical variables, constants, functions and operators.

The parser uses an allowlist-based validation approach instead of directly evaluating arbitrary user input.

## 8.3 Automated Testing

Pytest is used to verify equation parsing and validation.

The current parser test suite contains 14 tests covering:
- Basic mathematical expressions.
- Exponent notation.
- Supported mathematical functions.
- Mathematical constants.
- Invalid variables.
- Unsupported functions and operators.
- Invalid syntax.
- Unsafe input handling.
- Exponent restrictions.

All 14 parser tests passed locally during development.

## 8.4 Planned Implementation

The following components remain under development:

- Partial derivative calculations.
- Gradient magnitude and unit vector calculations.
- Heatmap and contour visualisations.
- Gradient arrow visualisation.
- Complete integration of mathematical and graphical modules.

# 9. Testing and Validation

The project uses automated tests to verify the correctness of its equation parser.

A separate mathematical test specification has also been prepared to define expected results for the future gradient calculation engine.

These mathematical test cases cover:
- Partial derivatives.
- Gradient components.
- Gradient magnitude.
- Unit gradient vectors.
- Zero-gradient conditions.
- Undefined and non-real results.

The calculation engine will be tested against these expected mathematical results once implemented.

# 10. Results and Discussion

The current implementation demonstrates successful equation input and validation through the Streamlit interface.

The parser has passed all 14 locally executed automated tests.

The mathematical calculation and graphical visualisation stages are still under development. Therefore, final gradient calculation results and visualisation outputs are not yet available for evaluation.

# 11. Limitations

The current development stage has the following limitations:

1. Gradient calculations are not yet integrated.
2. Heatmap and contour visualisations are pending.
3. Gradient vector arrows are pending.
4. Complete end-to-end application testing remains pending.

# 12. Future Scope

Potential improvements include:

- Interactive three-dimensional surface visualisation.
- Directional derivative calculations.
- Interactive gradient vector controls.
- Additional mathematical functions.
- Improved graph customisation.
- Expanded mathematical test coverage.

# 13. Conclusion

Gradient Explorer is being developed as an interactive educational application to demonstrate gradients and steepest ascent for functions of two variables.

The project has established its initial Streamlit interface, safe equation parsing system, automated parser tests and technical documentation.

The remaining development work focuses on implementing the mathematical calculation engine, graphical visualisations and complete application integration.

The project aims to provide students with a practical way to connect mathematical calculations with their geometric interpretation.

# 14. References

1. James Stewart, Calculus: Early Transcendentals.
2. SymPy Documentation – https://docs.sympy.org/
3. Streamlit Documentation – https://docs.streamlit.io/
4. NumPy Documentation – https://numpy.org/doc/
5. Matplotlib Documentation – https://matplotlib.org/stable/
6. Pytest Documentation – https://docs.pytest.org/
