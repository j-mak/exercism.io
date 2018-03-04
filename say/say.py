from num2words import num2words


def say(number):
    """Translate given number to words."""
    if number < 0 or number >= 10**12:
        raise AttributeError
    return num2words(number).replace(",", "")
