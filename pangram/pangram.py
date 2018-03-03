def is_pangram(sentence):
    """Check if given sentence is a pangram or not."""
    length = (ord('z') - ord('a')) + 1
    used = set()

    if not len(sentence):
        return False

    for char in sentence.lower():
        if char.isalpha():
            if char not in used:
                used.add(char)

    return len(used) == length
