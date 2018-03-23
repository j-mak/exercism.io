def is_armstrong(number):
    """
    Verifies if given number is armstrong number or not.
    Args:
        number: number which we want to test

    Returns:
        true if given number is armstrong number.

    """
    total_sum = 0
    str_number = str(number)
    length = len(str_number)

    for num in str_number:
        total_sum += pow(int(num), length)

    return total_sum == number
