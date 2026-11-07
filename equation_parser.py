import ast
import sympy as sp


# Variables supported by Gradient Explorer
x, y = sp.symbols("x y")

# Mathematical functions users are allowed to enter
ALLOWED_FUNCTIONS = {
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "exp": sp.exp,
    "log": sp.log,
    "sqrt": sp.sqrt,
    "abs": sp.Abs,
}

# Mathematical constants
ALLOWED_CONSTANTS = {
    "pi": sp.pi,
    "E": sp.E,
}

ALLOWED_VARIABLES = {
    "x": x,
    "y": y,
}


class EquationValidationError(ValueError):
    """Raised when an equation contains unsupported input."""


def _convert_node(node, depth=0):
    """Convert an allowlisted Python syntax tree into a SymPy expression."""

    if depth > 20:
        raise EquationValidationError("Equation is too deeply nested.")

    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool):
            raise EquationValidationError("Boolean values are not supported.")

        if isinstance(node.value, (int, float)):
            return sp.sympify(node.value)

        raise EquationValidationError("Only numeric constants are allowed.")

    if isinstance(node, ast.Name):
        if node.id in ALLOWED_VARIABLES:
            return ALLOWED_VARIABLES[node.id]

        if node.id in ALLOWED_CONSTANTS:
            return ALLOWED_CONSTANTS[node.id]

        raise EquationValidationError(
            f"'{node.id}' is not an allowed variable or constant."
        )

    if isinstance(node, ast.BinOp):
        left = _convert_node(node.left, depth + 1)
        right = _convert_node(node.right, depth + 1)

        operations = {
            ast.Add: lambda a, b: a + b,
            ast.Sub: lambda a, b: a - b,
            ast.Mult: lambda a, b: a * b,
            ast.Div: lambda a, b: a / b,
            ast.Pow: lambda a, b: a ** b,
        }

        operation = operations.get(type(node.op))

        if operation is None:
            raise EquationValidationError("This mathematical operator is not supported.")

        if isinstance(node.op, ast.Pow):
            if right.is_number and abs(float(right)) > 100:
                raise EquationValidationError("Exponent magnitude cannot exceed 100.")

        return operation(left, right)

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
            raise EquationValidationError(
                f"Function '{node.func.id}' is not supported."
            )

        if node.keywords or len(node.args) != 1:
            raise EquationValidationError(
                "Mathematical functions must have exactly one argument."
            )

        argument = _convert_node(node.args[0], depth + 1)
        return function(argument)

    raise EquationValidationError("The equation contains unsupported syntax.")


def parse_equation(equation: str):
    """Validate user input and return a SymPy expression in x and y."""

    if not isinstance(equation, str) or not equation.strip():
        raise EquationValidationError("Please enter a mathematical function.")

    equation = equation.strip()

    if len(equation) > 200:
        raise EquationValidationError("Equation is too long. Maximum: 200 characters.")

    # Accept ^ as a user-friendly alternative for **
    equation = equation.replace("^", "**")

    try:
        syntax_tree = ast.parse(equation, mode="eval")
        expression = _convert_node(syntax_tree.body)

        if len(list(ast.walk(syntax_tree))) > 100:
            raise EquationValidationError("Equation is too complex.")

        if not expression.free_symbols.issubset({x, y}):
            raise EquationValidationError("Only x and y are supported.")

        return expression

    except EquationValidationError:
        raise

    except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as error:
        raise EquationValidationError(
            "Invalid equation. Check the mathematical syntax."
        ) from error
