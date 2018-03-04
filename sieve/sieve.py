def sieve(limit):
    """Returns list of prime numbers to given limit."""
    numbers = [x for x in range(2, limit + 1)]
    primes = []

    while numbers:
        primes.append(numbers.pop(0))
        for item in numbers:
            if not item % primes[-1]:
                numbers.remove(item)
    return primes
