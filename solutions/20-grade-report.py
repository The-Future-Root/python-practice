# Solution to 20. Grade report

def letter_grade(average):
    """Return "A", "B", "C", "D" or "F" for an average score."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"


def average(scores):
    """Return the average of the scores rounded to 1 decimal place, or None for an empty list."""
    if not scores:
        return None
    return round(sum(scores) / len(scores), 1)


def report(students):
    """Return a list of (name, average, grade) tuples, highest average first, then by name."""
    results = []
    for name, scores in students.items():
        avg = average(scores)
        if avg is not None:
            results.append((name, avg, letter_grade(avg)))
    results.sort(key=lambda r: (-r[1], r[0]))
    return results
