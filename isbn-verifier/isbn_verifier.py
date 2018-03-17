import re


def is_valid(isbn):
    result = re.match(r'\d\-?\d{3}\-?\d{5}\-?(?:\d|X)', isbn)
    return result is not None


def verify(isbn):
    if isbn and is_valid(isbn):
        isbn = isbn.replace('-', '')
        length = len(isbn)

        isbn_sum = 0
        for i in range(length):
            if isbn[i].lower() == "x":
                isbn_sum += 10 * (length - i)
            else:
                isbn_sum += int(isbn[i]) * (length - i)

        return isbn_sum % 11 == 0
    return False

