plain = "abcdefghijklmnopqrstuvwxyz"


def rotate(string_to_encode, rot_size):
    """Return encoded string in rotational cipher."""
    rotated = plain[rot_size:] + plain[:rot_size]

    response = ""
    for char in string_to_encode:
        needed_upper = char.isupper()
        if char.lower() in plain:
            char_rotated = rotated[plain.index(char.lower())]
            response += char_rotated.upper() if needed_upper else char_rotated
        else:
            response += char
    return response
