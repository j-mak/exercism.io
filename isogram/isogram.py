def is_isogram(word):
    """This method check if given word is isogram."""
    chars = set()
    if len(word) == 0:
        return True
    for letter in word:
        letter = letter.lower()
        if letter.isalpha() and letter in chars:
            return False
        chars.add(letter)

    return True
