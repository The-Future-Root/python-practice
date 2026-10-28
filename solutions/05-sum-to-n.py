# Solution to 5. Sum of 1 to n

def sum_to(n):
    """Return 1 + 2 + ... + n, using a loop."""
    total = 0
    for number in range(1, n + 1):
        total += number
    return total


def sum_formula(n):
    """Return 1 + 2 + ... + n, using n * (n + 1) // 2."""
    if n < 1:
        return 0
    return n * (n + 1) // 2
