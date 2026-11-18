# System Architecture

## Gradient Explorer

## 1. Overview

Gradient Explorer is a Streamlit application for exploring scalar functions of two variables. It validates mathematical input, calculates symbolic and numerical gradient properties, and visualises the function over a selected coordinate window.

## 2. Technology stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| Streamlit | User interface |
| SymPy | Parsing output, symbolic differentiation, and evaluation |
| NumPy | Numerical coordinate grids |
| Matplotlib | Contour, heatmap, vector-field, and surface plots |
| Pytest | Automated testing |
| GitHub Actions | Continuous integration |

## 3. Project structure

```text
Gradient-Explorer/
├── .github/workflows/tests.yml
├── tests/
│   ├── test_calculations.py
│   └── test_equation_parser.py
├── docs/
│   ├── architecture.md
│   ├── math_test_cases.md
│   └── project_report.md
├── app.py
├── calculations.py
├── equation_parser.py
├── visualizations.py
├── requirements.txt
└── README.md
```

## 4. Module responsibilities

### app.py — Presentation layer
- Collects the function, coordinates, and plot range.
- Invokes validation and calculation services.
- Displays symbolic and numerical results.
- Renders contour, heatmap, and 3D surface tabs.
- Presents domain and zero-gradient feedback.

### equation_parser.py — Input boundary
- Parses Python expression syntax into an AST.
- Allows only explicitly supported variables, constants, functions, and operators.
- Enforces input length, AST node count, nesting depth, and exponent bounds.
- Converts the approved syntax into SymPy expressions without eval.

### calculations.py — Mathematical engine
- Computes symbolic partial derivatives.
- Evaluates the function and gradient at a finite real coordinate pair.
- Calculates gradient magnitude and unit ascent direction.
- Represents a zero-gradient direction as None rather than dividing by zero.
- Calculates directional derivatives along normalized user-supplied vectors.
- Raises CalculationError for undefined, non-finite, or non-real point evaluations.

### visualizations.py — Graphical engine
- Builds coordinate grids with NumPy.
- Evaluates expressions and derivatives through SymPy lambdify.
- Masks non-finite values in plots.
- Generates a contour map with sampled gradient arrows and selected point.
- Generates a heatmap and a 3D surface plot.

### tests/ — Quality checks
- Verifies parser allowlisting and rejected syntax.
- Checks reference gradient cases, derivatives, magnitude, unit direction, directional derivatives, and invalid domains.

## 5. Data flow

```text
User inputs
    |
    v
Streamlit interface (app.py)
    |
    v
Equation parser (equation_parser.py)
    |
    v
SymPy expression
    |
    +------------------------------+
    |                              |
    v                              v
Calculation engine             Visualization engine
(calculations.py)               (visualizations.py)
    |                              |
    +---------------+--------------+
                    |
                    v
             Streamlit results
```

## 6. Numerical behaviour and errors

Point calculations require finite real coordinates and finite real outputs. Singularities and non-real values at the selected point are reported as calculation errors. A zero gradient is a valid result: its magnitude is zero, while its normalized direction is undefined.

Plots use a numerical grid and mask invalid values so singular regions do not contaminate the entire figure. Plotting is an approximation over a finite window, while symbolic derivatives are computed by SymPy.

## 7. Testing and continuous integration

Pytest validates parser and mathematical behaviour. GitHub Actions installs the declared dependencies and runs the test suite on pushes to main and pull requests targeting main.

## 8. Design decisions

- Keep parsing, calculations, visualisation, and presentation in separate modules.
- Do not evaluate arbitrary user-supplied Python code.
- Use symbolic differentiation for exact derivative expressions.
- Use numerical evaluation only at selected points and across plotting grids.
- Keep main protected by pull-request review and CI.
