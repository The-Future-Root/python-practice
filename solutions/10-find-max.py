# Solution to 10. Find the max

def find_max(numbers):
    """Return the largest number, or None for an empty list. Don't use max()."""
    if not numbers:
        return None
    biggest = numbers[0]
    for n in numbers[1:]:
        if n > biggest:
            biggest = n
    return biggest


def find_min(numbers):
    """Return the smallest number, or None for an empty list. Don't use min()."""
    if not numbers:
        return None
    smallest = numbers[0]
    for n in numbers[1:]:
        if n < smallest:
            smallest = n
    return smallest


def find_average(numbers):
    """Return the average rounded to 2 decimal places, or None for an empty list."""
    if not numbers:
        return None
    return round(sum(numbers) / len(numbers), 2)
