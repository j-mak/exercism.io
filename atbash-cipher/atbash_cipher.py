from string import ascii_lowercase

cipher = ascii_lowercase[::-1]


def encode(raw):
    """Encode plain text with atbash cipher method."""
    response = ''
    raw = raw.replace(' ', '')
    tab_index = 0
    for char in raw.lower():
        if char in ascii_lowercase:
            index = ascii_lowercase.index(char)
            response += cipher[index]
            tab_index += 1
        elif char.isdigit():
            response += char
            tab_index += 1
        if tab_index == 5:
            response += ' '
            tab_index = 0
    return response.strip()


def decode(encoded):
    """decode encoded text with atbash cipher method."""
    response = ''
    encoded = encoded.replace(' ', '')
    for char in encoded:

        if char in cipher:
            index = cipher.index(char)
            response += ascii_lowercase[index]
        else:
            response += char
    return response
