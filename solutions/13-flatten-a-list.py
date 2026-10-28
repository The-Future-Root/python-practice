# Solution to 13. Flatten a list

def flatten(nested):
    """Return one list with the items of every inner list, in order (one level deep)."""
    result = []
    for inner in nested:
        for item in inner:
            result.append(item)
    return result


def flatten_deep(nested):
    """Return one list with every value, however deeply the lists are nested."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_deep(item))
        else:
            result.append(item)
    return result
