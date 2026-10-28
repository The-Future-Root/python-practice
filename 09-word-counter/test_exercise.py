import unittest

from exercise import top_words, word_counts


class TestWordCounts(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(word_counts("the cat sat on the mat"),
                         [("the", 2), ("cat", 1), ("sat", 1), ("on", 1), ("mat", 1)])

    def test_case_and_punctuation(self):
        self.assertEqual(word_counts("Data, data and more DATA."), [("data", 3), ("and", 1), ("more", 1)])

    def test_ties_keep_first_appearance(self):
        self.assertEqual(word_counts("b a b a c"), [("b", 2), ("a", 2), ("c", 1)])

    def test_quotes_and_brackets(self):
        self.assertEqual(word_counts('"Hello" (hello) hello!'), [("hello", 3)])

    def test_empty(self):
        self.assertEqual(word_counts(""), [])
        self.assertEqual(word_counts("... !!"), [])


class TestTopWords(unittest.TestCase):
    def test_top_two(self):
        self.assertEqual(top_words("to be or not to be that is the question", 2), ["to", "be"])

    def test_more_than_there_are(self):
        self.assertEqual(top_words("one two", 5), ["one", "two"])


if __name__ == "__main__":
    unittest.main()
