import re


class Luhn(object):
    def __init__(self, validate_number):
        self.validate_number = validate_number

    def is_valid(self):
        checksum = 0

        if re.search(r'[^\d ]', self.validate_number):
            return False

        only_numbers = re.findall(r'\d', self.validate_number)

        if len(only_numbers) < 2:
            return False

        for index, number in enumerate(reversed(only_numbers)):
            number = int(number)
            if index % 2:
                number *= 2
                if number > 9:
                    number -= 9
            checksum += number
        return checksum % 10 == 0
