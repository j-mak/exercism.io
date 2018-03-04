def prime_factors(number):
    """Returns prime factors for given number."""
    result = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            number /= divisor
            result.append(divisor)
        else:
            divisor += 1

    return result
