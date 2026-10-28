# Solution to 11. Remove duplicates

def remove_duplicates(items):
    """Return a new list with each item once, in its original order."""
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen
