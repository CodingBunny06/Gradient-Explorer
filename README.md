# Gradient Explorer

### Interactive Mathematical Visualisation of Gradient and Steepest Ascent

<p align="center">
  An Engineering Mathematics-I working model demonstrating partial differentiation, gradient vectors, and the direction of steepest ascent through interactive visualisations.
</p>

---

## 1. About the Project

Gradient Explorer is an interactive mathematical application designed to demonstrate how a function of two variables changes across a surface.

Users will be able to enter mathematical functions, calculate their partial derivatives, determine gradient vectors and gradient magnitudes, and visualise the results through heatmaps, contour lines, and gradient arrows.

**Main objective:** To demonstrate the mathematical concept of gradients and identify the direction in which a function increases most rapidly.

## 2. Mathematical Concepts

The project focuses on the following Engineering Mathematics-I concepts:

- Functions of two variables
- Partial differentiation
- Gradient of a scalar function
- Gradient vector and magnitude
- Directional derivatives
- Direction of steepest ascent and descent
- Contour lines and their relationship with gradients

## 3. Planned Features

| Feature | Description |
|---|---|
| Custom Equation Input | Enter mathematical functions of two variables |
| Partial Derivatives | Calculate derivatives with respect to x and y |
| Gradient Calculation | Calculate the gradient vector |
| Gradient Magnitude | Determine the maximum rate of increase |
| Heatmap | Visualise function values using colours |
| Contour Plot | Display curves of constant function values |
| Gradient Arrows | Visualise the direction of steepest ascent |
| Point Selection | Evaluate the gradient at a selected point |
| Steepest-Ascent Path | Illustrate movement in the uphill direction |

*Features will be implemented progressively.*

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| SymPy | Symbolic differentiation and mathematical expressions |
| NumPy | Numerical calculations and coordinate grids |
| Matplotlib | Heatmaps, contour plots and vector visualisations |
| Streamlit | Interactive web application |
| pytest | Testing mathematical calculations |
| Git & GitHub | Version control and collaboration |

## 5. Development Environment

Our development tools will include:

- **Visual Studio Code:** Writing and managing project code.
- **Terminal:** Installing dependencies and running commands.
- **Web Browser:** Accessing the application through localhost.
- **GitHub:** Hosting source code and tracking development.
- **Google Colab (optional):** Experimenting with Python calculations.

## 6. How the Application Works

The proposed application follows this workflow:

1. The user enters a mathematical function of two variables.
2. SymPy calculates the partial derivatives.
3. The application constructs the gradient vector.
4. NumPy performs numerical calculations over a coordinate grid.
5. Matplotlib generates heatmaps, contour plots and gradient arrows.
6. Streamlit presents the calculations and visualisations through an interactive interface.

## 7. Role of AI

AI tools such as ChatGPT and Google Gemini will be used as development assistants for:

- Understanding mathematical concepts.
- Assistance with Python programming.
- Debugging and troubleshooting.
- Reviewing mathematical calculations.
- Generating test cases.
- Improving documentation and presentation material.

**Important:** AI will assist the development process. The actual mathematical calculations and visualisations will be performed by our Python application.

## 8. Team Responsibilities

| Member | Responsibility |
|---|---|
| Member 1 | Mathematical concepts, formulas and verification |
| Member 2 | Python backend and SymPy calculations |
| Member 3 | Heatmaps, contour plots and gradient visualisation |
| Member 4 | Streamlit interface, integration and testing |

All members will participate in understanding the mathematical concepts and final project demonstration.

## 9. Development Roadmap

| Stage | Task |
|---|---|
| 1 | Understand the mathematics and finalise requirements |
| 2 | Set up Python environment and dependencies |
| 3 | Implement partial derivatives and gradient calculations |
| 4 | Develop mathematical visualisations |
| 5 | Build the interactive Streamlit interface |
| 6 | Integrate components and test different functions |
| 7 | Prepare documentation, report and presentation |

## 10. Project Structure

Planned folder structure:

```text
Gradient-Explorer/
│
├── app.py
├── calculations.py
├── visualizations.py
├── requirements.txt
├── README.md
│
├── tests/
│   └── test_calculations.py
│
├── screenshots/
│
└── docs/
    └── project_report.md
```

## 11. Example Mathematical Function

Consider the function:

\[
f(x,y)=x^2+y^2
\]

Its gradient is:

\[
\nabla f(x,y)=(2x,2y)
\]

At the point \((1,2)\):

\[
\nabla f(1,2)=(2,4)
\]

The gradient indicates the direction of steepest increase, while its magnitude represents the maximum rate of increase.

The application will allow users to explore such mathematical relationships interactively.

---

## 12. Project Information

- **Project Name:** Gradient Explorer
- **Subject:** Engineering Mathematics-I
- **Project Type:** Interactive Mathematical Working Model
- **Programming Language:** Python
- **Team Size:** 4 Members
- **Development Status:** Planning

---

*Built as an academic project to explore and visualise the mathematics of gradients.*
