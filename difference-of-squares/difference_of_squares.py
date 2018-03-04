import math


def square_of_sum(num):
    """Returns square of sum of N integers."""
    squares = 0
    for i in range(1, num + 1):
        squares += i
    return math.pow(squares, 2)


def sum_of_squares(num):
    """Returns sum of square of N integers."""
    sums = 0
    for i in range(1, num + 1):
        sums += math.pow(i, 2)
    return sums


def difference(num):
    """Returns difference between square_of_sum and sum_of_square
    for first N integers."""
    return square_of_sum(num) - sum_of_squares(num)
