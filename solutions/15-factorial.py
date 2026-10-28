# Solution to 15. Factorial

def factorial(n):
    """Return n! using a loop. Raise ValueError for negative n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result


def factorial_recursive(n):
    """Return n! using recursion. Raise ValueError for negative n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
