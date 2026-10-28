# Solution to 3. Even or odd

def is_even(n):
    """Return True if n is even, False if it's odd."""
    return n % 2 == 0


def describe(n):
    """Return "7 is odd" or "10 is even"."""
    if is_even(n):
        return f"{n} is even"
    return f"{n} is odd"
