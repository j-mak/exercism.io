def numeral(arabic_number):
    """Convert Arabic number to Roman."""
    roman_number = ''
    convert_array = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
                     [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'],
                     [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]

    for arabic, roman in convert_array:
        roman_number += roman * (arabic_number // arabic)
        arabic_number %= arabic

    return roman_number
