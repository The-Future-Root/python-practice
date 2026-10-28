# Solution to 12. Second largest

def second_largest(numbers):
    """Return the second largest distinct value, or None if there isn't one."""
    largest = None
    second = None
    for n in numbers:
        if largest is None or n > largest:
            second = largest
            largest = n
        elif n != largest and (second is None or n > second):
            second = n
    return second
