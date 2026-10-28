# Solution to 7. Count vowels

def count_vowels(text):
    """Return the number of vowels in text, in upper or lower case."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count


def vowel_counts(text):
    """Return a dictionary with a count for each of a, e, i, o, u."""
    counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
    return counts
