# 9. Word counter

**Level:** Medium. **You'll practise:** cleaning text, counting with a dictionary, sorting with a key.

Search engines, spam filters and word clouds all start by counting words. Write two functions:

- `word_counts(text)` returns a list of `(word, count)` pairs, the most frequent word first. Ignore case, and strip punctuation from the ends of words, so `"Data,"` and `"data"` count as the same word. When two words have the same count, keep them in the order they first appeared.
- `top_words(text, n)` returns just the `n` most frequent words, as a list.

## Examples

```python
>>> word_counts('the cat sat on the mat')
[('the', 2), ('cat', 1), ('sat', 1), ('on', 1), ('mat', 1)]
>>> word_counts('Data, data and more DATA.')
[('data', 3), ('and', 1), ('more', 1)]
>>> top_words('to be or not to be that is the question', 2)
['to', 'be']
```

## Rules

- Words are separated by spaces. Strip these characters from the ends of each word: `.,!?;:"'()`.
- Skip words that are empty after stripping, such as a lone `!`.
- An empty text gives an empty list.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 09-word-counter
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

Lowercase the text, `split()` it, and `word.strip(".,!?;:\"'()")` each word.

</details>

<details>
<summary>Hint 2</summary>

Count with a dictionary: `counts[word] = counts.get(word, 0) + 1`. A dictionary remembers the order words were first added.

</details>

<details>
<summary>Hint 3</summary>

Sort the pairs by count, biggest first: `sorted(counts.items(), key=lambda pair: pair[1], reverse=True)`. Python's sort is **stable**: items with the same count keep their original order.

</details>

## Take it further

Add a `stop_words` parameter: a set of common words like `{"the", "and", "a"}` to leave out of the counts.

A full solution is in [solutions/09-word-counter.py](../solutions/09-word-counter.py).

Next: [10. Find the max](../10-find-max/)
