# Gradient Explorer

![CI](https://github.com/CodingBunny06/Gradient-Explorer/actions/workflows/tests.yml/badge.svg)

**Interactive mathematical visualisation of gradients and steepest ascent**

Gradient Explorer is a Python application for exploring scalar functions of two variables. Enter a function, select a point, calculate its gradient, and inspect the result using contour, heatmap, and 3D surface visualisations.

## Features

- Allowlist-based equation parser for safe mathematical input
- Symbolic partial derivatives with respect to x and y
- Numerical function and gradient evaluation at a selected point
- Gradient vector, magnitude, unit ascent direction, and descent direction
- Directional derivative along a user-selected direction
- Contour plot with sampled gradient vector field and selected point
- Function heatmap and 3D surface plot
- Explicit handling of zero gradients and undefined/non-real evaluations
- Automated tests and GitHub Actions CI

## Mathematical foundation

For a scalar function f(x, y), the gradient is:

\[
\\nabla f(x,y)=\\left(\\frac{\\partial f}{\\partial x},\\frac{\\partial f}{\\partial y}\\right)
\]

Its magnitude gives the maximum local rate of increase. When the magnitude is non-zero, the normalized gradient gives the direction of steepest ascent:

\[
\\hat{u}_{\\mathrm{ascent}}=\\frac{\\nabla f}{\\lVert\\nabla f\\rVert}
\]

The directional derivative along a unit vector u is:

\[
D_{\\mathbf{u}}f=\\nabla f\\cdot\\mathbf{u}
\]

At a zero-gradient point, the unit gradient is undefined.

## Supported equation syntax

| Category | Supported input |
|---|---|
| Variables | x, y |
| Constants | pi, E |
| Functions | sin, cos, tan, exp, log, sqrt, abs |
| Operators | +, -, *, /, ** |
| Power alias | ^ |

Multiplication must be explicit (write 2*x, not 2x). Functions accept one argument. Expressions are limited in length, syntax-tree size, nesting depth, and numeric exponent magnitude.

## Technology stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| SymPy | Symbolic mathematics |
| NumPy | Numerical grids and array operations |
| Matplotlib | Contour, heatmap, vector-field, and surface plots |
| Streamlit | Interactive web interface |
| Pytest | Automated testing |
| GitHub Actions | Continuous integration |

## Deployment

Gradient Explorer is prepared for deployment on **Streamlit Community Cloud**.

- Deployment guide: [docs/deployment.md](docs/deployment.md)
- Repository: [GitHub](https://github.com/CodingBunny06/Gradient-Explorer)

The public app URL will be added here after deployment and smoke testing are complete.

## Run locally

Python 3.12 is used by the CI workflow.

```bash
git clone https://github.com/CodingBunny06/Gradient-Explorer.git
cd Gradient-Explorer

python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\\Scripts\\activate       # Windows

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit (usually http://localhost:8501).

## Run tests

```bash
python -m pytest -v
```

## Project structure

```text
Gradient-Explorer/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── config.yml
│   │   └── feature_request.yml
│   ├── workflows/
│   │   └── tests.yml
│   ├── dependabot.yml
│   └── pull_request_template.md
├── docs/
│   ├── architecture.md
│   ├── deployment.md
│   ├── math_test_cases.md
│   └── project_report.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── SUPPORT.md
├── tests/
│   ├── test_calculations.py
│   ├── test_equation_parser.py
│   ├── test_parser_limits.py
│   └── test_visualizations.py
├── app.py
├── calculations.py
├── equation_parser.py
├── visualizations.py
├── requirements.txt
└── README.md
```

## Architecture

1. Streamlit collects the function, point, and plot range.
2. equation_parser.py validates the expression using an allowlist and converts it to SymPy.
3. calculations.py differentiates the expression symbolically and evaluates function/gradient values.
4. visualizations.py samples the function and derivatives over a NumPy grid and creates Matplotlib figures.
5. app.py presents numerical results and interactive plot tabs.

See [docs/architecture.md](docs/architecture.md) for module responsibilities and data flow.

## Example

For f(x,y) = x² + y² at (1,2):

- Partial derivatives: ∂f/∂x = 2x and ∂f/∂y = 2y
- Gradient: (2,4)
- Magnitude: √20 ≈ 4.4721
- Unit ascent direction: (1/√5, 2/√5)

## Limitations

- The parser intentionally supports a restricted mathematical language; arbitrary Python and implicit multiplication are not supported.
- Numerical plots mask undefined or non-finite regions.
- Symbolic expressions that are valid mathematically may still be outside the real-valued domain at a selected point.
- The application is an educational visualisation tool, not a computer algebra system replacement.

## Development

This is an individual academic project. Changes are developed on feature branches, tested, and reviewed through pull requests before being merged into main.

## Project information

- **Project:** Gradient Explorer
- **Subject context:** Engineering Mathematics-I
- **Type:** Interactive mathematical working model
- **Author:** CodingBunny06

---
