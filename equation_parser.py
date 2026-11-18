"""Safe allowlist-based parser for two-variable mathematical expressions."""
import ast
import math
import sympy as sp

x, y = sp.symbols("x y")
ALLOWED_FUNCTIONS = {"sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "exp": sp.exp, "log": sp.log, "sqrt": sp.sqrt, "abs": sp.Abs}
ALLOWED_CONSTANTS = {"pi": sp.pi, "E": sp.E}
ALLOWED_VARIABLES = {"x": x, "y": y}
MAX_EQUATION_LENGTH = 200
MAX_AST_NODES = 100
MAX_AST_DEPTH = 20
MAX_EXPONENT_MAGNITUDE = 100


class EquationValidationError(ValueError):
    """Raised when an equation contains unsupported or unsafe input."""


def _convert_node(node, depth=0):
    """Convert an allowlisted AST node into a SymPy expression."""
    if depth > MAX_AST_DEPTH:
        raise EquationValidationError("Equation is too deeply nested.")
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool):
            raise EquationValidationError("Boolean values are not supported.")
        if isinstance(node.value, (int, float)):
            if isinstance(node.value, float) and not math.isfinite(node.value):
                raise EquationValidationError("Numeric constants must be finite.")
            return sp.sympify(node.value)
        raise EquationValidationError("Only numeric constants are allowed.")
    if isinstance(node, ast.Name):
        if node.id in ALLOWED_VARIABLES:
            return ALLOWED_VARIABLES[node.id]
        if node.id in ALLOWED_CONSTANTS:
            return ALLOWED_CONSTANTS[node.id]
        raise EquationValidationError(f"'{node.id}' is not an allowed variable or constant.")
    if isinstance(node, ast.BinOp):
        if not isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow)):
            raise EquationValidationError("This mathematical operator is not supported.")
        left, right = _convert_node(node.left, depth + 1), _convert_node(node.right, depth + 1)
        if isinstance(node.op, ast.Pow) and right.is_number:
            try:
                exponent = complex(sp.N(right))
            except (TypeError, ValueError, OverflowError) as error:
                raise EquationValidationError("Exponent must be a finite real number.") from error
            if not math.isfinite(exponent.real) or not math.isfinite(exponent.imag) or abs(exponent.imag) > 1e-12:
                raise EquationValidationError("Exponent must be a finite real number.")
            if abs(exponent.real) > MAX_EXPONENT_MAGNITUDE:
                raise EquationValidationError("Exponent magnitude cannot exceed 100.")
        operations = {ast.Add: lambda a, b: a + b, ast.Sub: lambda a, b: a - b, ast.Mult: lambda a, b: a * b, ast.Div: lambda a, b: a / b, ast.Pow: lambda a, b: a ** b}
        return operations[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp):
        value = _convert_node(node.operand, depth + 1)
        if isinstance(node.op, ast.UAdd):
            return value
        if isinstance(node.op, ast.USub):
            return -value
        raise EquationValidationError("This unary operator is not supported.")
    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise EquationValidationError("Only direct mathematical function calls are allowed.")
        function = ALLOWED_FUNCTIONS.get(node.func.id)
        if function is None:
            raise EquationValidationError(f"Function '{node.func.id}' is not supported.")
        if node.keywords or len(node.args) != 1:
            raise EquationValidationError("Mathematical functions must have exactly one argument.")
        return function(_convert_node(node.args[0], depth + 1))
    raise EquationValidationError("The equation contains unsupported syntax.")


def parse_equation(equation: str):
    """Validate user input and return a SymPy expression in x and y."""
    if not isinstance(equation, str) or not equation.strip():
        raise EquationValidationError("Please enter a mathematical function.")
    equation = equation.strip()
    if len(equation) > MAX_EQUATION_LENGTH:
        raise EquationValidationError("Equation is too long. Maximum: 200 characters.")
    try:
        syntax_tree = ast.parse(equation.replace("^", "**"), mode="eval")
        if sum(1 for _ in ast.walk(syntax_tree)) > MAX_AST_NODES:
            raise EquationValidationError("Equation is too complex.")
        expression = _convert_node(syntax_tree.body)
        if not expression.free_symbols.issubset({x, y}):
            raise EquationValidationError("Only x and y are supported.")
        return expression
    except EquationValidationError:
        raise
    except (SyntaxError, TypeError, ValueError, ZeroDivisionError, OverflowError, RecursionError) as error:
        raise EquationValidationError("Invalid equation. Check the mathematical syntax.") from error
