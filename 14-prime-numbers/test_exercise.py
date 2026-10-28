import time
import unittest

from exercise import is_prime, primes_up_to


class TestPrimes(unittest.TestCase):
    def test_small_primes(self):
        for n in (2, 3, 5, 7, 11, 13, 97):
            self.assertIs(is_prime(n), True, f"{n} is prime")

    def test_not_prime(self):
        for n in (4, 9, 15, 21, 25, 100):
            self.assertIs(is_prime(n), False, f"{n} isn't prime")

    def test_below_two(self):
        for n in (1, 0, -7):
            self.assertIs(is_prime(n), False)

    def test_primes_up_to(self):
        self.assertEqual(primes_up_to(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(primes_up_to(2), [2])
        self.assertEqual(primes_up_to(1), [])

    def test_fast_enough(self):
        start = time.perf_counter()
        self.assertIs(is_prime(1_000_003), True)
        self.assertIs(is_prime(999_999_937), True)
        self.assertLess(time.perf_counter() - start, 2, "Only try divisors up to the square root of n")


if __name__ == "__main__":
    unittest.main()
