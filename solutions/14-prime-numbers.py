# Solution to 14. Prime numbers

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def primes_up_to(limit):
    """Return a list of the primes from 2 up to and including limit."""
    return [n for n in range(2, limit + 1) if is_prime(n)]
