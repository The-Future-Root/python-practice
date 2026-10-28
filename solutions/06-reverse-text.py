# Solution to 6. Reverse text

def reverse(text):
    """Return the text backwards."""
    result = ""
    for char in text:
        result = char + result
    return result


def reverse_words(sentence):
    """Return the words of the sentence in reverse order, separated by single spaces."""
    words = sentence.split()
    return " ".join(words[::-1])
