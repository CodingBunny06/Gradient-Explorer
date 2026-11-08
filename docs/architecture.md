
# System Architecture

## Gradient Explorer

## 1. Overview

Gradient Explorer is an interactive mathematical visualisation application designed to demonstrate the concept of gradients and steepest ascent on a surface.

The application accepts a mathematical function of two variables, evaluates it at a selected point and presents mathematical and graphical results.

The project uses Python, SymPy, NumPy, Matplotlib and Streamlit.

## 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive user interface |
| SymPy | Symbolic mathematics and differentiation |
| NumPy | Numerical operations and coordinate calculations |
| Matplotlib | Mathematical visualisations |
| Pytest | Automated testing |
| Git and GitHub | Version control and collaboration |
| GitHub Actions | Continuous integration and automated testing |

## 3. Project Structure

```text
Gradient-Explorer/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── tests/
│   └── test_equation_parser.py
│
├── docs/
│   ├── math_test_cases.md
│   └── architecture.md
│
├── app.py
├── equation_parser.py
├── calculations.py
├── visualizations.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

Note: `calculations.py` and `visualizations.py` represent planned modules and will be added when their implementations are ready.

## 4. Module Responsibilities

### 4.1 app.py — Application Interface

Responsible for:
- Displaying the Streamlit interface.
- Accepting mathematical function input.
- Accepting x and y coordinates.
- Triggering equation validation and calculations.
- Displaying mathematical results.
- Integrating visualisation components.

### 4.2 equation_parser.py — Equation Validation

Responsible for:
- Validating user-entered mathematical expressions.
- Restricting input to supported variables, constants and functions.
- Converting validated expressions into SymPy expressions.
- Rejecting unsupported or unsafe syntax.

### 4.3 calculations.py — Mathematical Engine

Planned responsibilities:
- Calculating partial derivatives.
- Evaluating gradient components.
- Calculating gradient magnitude.
- Calculating unit gradient vectors.
- Handling zero-gradient and undefined cases.

### 4.4 visualizations.py — Graphical Engine

Planned responsibilities:
- Generating contour plots.
- Generating heatmaps.
- Displaying gradient vectors.
- Representing the function surface and its mathematical behaviour.

### 4.5 tests/ — Automated Testing

Responsible for:
- Testing equation parsing and validation.
- Testing mathematical calculations.
- Checking expected outputs and edge cases.
- Preventing regressions during development.

### 4.6 docs/ — Project Documentation

Contains:
- Mathematical test specifications.
- System architecture.
- Project report and technical documentation.

## 5. Application Data Flow

The planned application workflow is:

1. User enters a mathematical function.
2. The application sends the input to the equation parser.
3. The parser validates the expression and converts it into a SymPy expression.
4. The mathematical engine calculates partial derivatives and gradient properties.
5. The visualisation engine generates graphical representations.
6. Streamlit displays the mathematical and graphical results.

## 6. Conceptual Architecture Diagram

```text
              USER
                |
                v
        STREAMLIT INTERFACE
              app.py
                |
                v
        EQUATION VALIDATION
          equation_parser.py
                |
                v
        MATHEMATICAL ENGINE
           calculations.py
                |
                v
        VISUALISATION ENGINE
          visualizations.py
                |
                v
        RESULTS DISPLAY
         Streamlit Interface
```

The diagram represents the intended architecture. Some modules are still under development.

## 7. Testing and Continuous Integration

The project uses Pytest for automated testing.

GitHub Actions runs the test suite when changes are pushed to the main branch or submitted through a pull request.

This helps identify errors before changes are merged into the main codebase.

## 8. Development Approach

The project follows a modular development approach.

Each major responsibility is separated into an independent Python module. This improves maintainability, testing and collaboration.

Feature branches and pull requests are used to manage contributions and protect the main branch.

## 9. Future Scope

Potential future improvements include:
- Interactive three-dimensional surface plots.
- Directional derivative calculations.
- User-controlled gradient visualisation.
- Additional mathematical functions.
- Improved graph customisation.
- Expanded automated test coverage.
