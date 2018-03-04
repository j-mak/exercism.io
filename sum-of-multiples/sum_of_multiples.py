def sum_of_multiples(below, multiples):
    """Returns sum of multiples below given maximum."""
    sums = set()
    for number in multiples:
        for i in range(number, below, number):
            sums.add(i)
    return sum(sums)
