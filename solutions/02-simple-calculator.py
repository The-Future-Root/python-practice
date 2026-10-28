# Solution to 2. Simple calculator

def calculate(a, operator, b):
    """Return a <operator> b, for the operators + - * and /."""
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Unknown operator: {operator}")
