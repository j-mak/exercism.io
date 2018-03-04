def on_square(square):
    """Calculate quantity on square."""
    return __calculate(square) / 2


def total_after(total):
    """Calculate total to given square."""
    return __calculate(total) - 1


def __calculate(x):
    if x > 64 or x < 1:
        raise ValueError
    else:
        return 1 << x
