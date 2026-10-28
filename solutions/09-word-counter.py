# Solution to 9. Word counter

PUNCTUATION = ".,!?;:\"'()"


def word_counts(text):
    """Return a list of (word, count) pairs, most frequent first."""
    counts = {}
    for word in text.lower().split():
        word = word.strip(PUNCTUATION)
        if word:
            counts[word] = counts.get(word, 0) + 1
    return sorted(counts.items(), key=lambda pair: pair[1], reverse=True)


def top_words(text, n):
    """Return the n most frequent words, as a list."""
    return [word for word, count in word_counts(text)[:n]]
