# Solution to 17. Temperature converter

def convert(value, from_unit, to_unit):
    """Convert a temperature between "C", "F" and "K", rounded to 2 decimal places."""
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()
    for unit in (from_unit, to_unit):
        if unit not in ("C", "F", "K"):
            raise ValueError(f"Unknown unit: {unit}")

    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if celsius < -273.15:
        raise ValueError("Below absolute zero")

    if to_unit == "C":
        result = celsius
    elif to_unit == "F":
        result = celsius * 9 / 5 + 32
    else:
        result = celsius + 273.15
    return round(result, 2)
