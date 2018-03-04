import math


def primitive_triplets(b):
    trips = set()
    for x, y, z in trip(b):
        if math.gcd(x, y) == math.gcd(y, z) == 1:
            trips.add((x, y, z))
    return trips


def triplets_in_range(min_value, max_value):
    triple = set()
    for a in range(min_value, max_value + 1):
        for b in range(a, max_value + 1):
            for c in range(b, max_value + 1):
                if a ** 2 + b ** 2 == c ** 2:
                    triple.update([(a, b, c)])
    return triple


def is_triplet(triplet):
    a, b, c = sorted(triplet)
    return a * a + b * b == c * c


def trip(b):
    if b % 4:
        raise ValueError('Invalid Input')
    max_num = int(math.sqrt((b - 1) / 2))
    for n in range(1, max_num + 1):
        m, redr = divmod(b // 2, n)
        if redr == 0:
            yield (tuple(sorted((m * m - n * n, b, m * m + n * n))))
