# Solution to 8. Palindrome check

def is_palindrome(text):
    """Return True if text reads the same backwards, ignoring case and anything that isn't a letter or digit."""
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char.lower()
    return cleaned == cleaned[::-1]
