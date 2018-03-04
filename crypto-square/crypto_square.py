import math


def encode(sentence):
    if not sentence:
        return ''

    normalized = __normalize(sentence)
    return make_square(normalized)


def __normalize(sentence):
    result = []
    for char in sentence:
        if char.isalnum():
            result.append(char.lower())

    return ''.join(result)


def __square_size(normalized_sentence):
    return int(math.ceil(math.sqrt(len(normalized_sentence))))


def make_square(sentence):
    size = __square_size(sentence)
    array = [sentence[i:i + size] for i in range(0, len(sentence), size)]

    result = []
    for index in range(size):
        word = []
        for item in array:
            try:
                word.append(item[index])
            except IndexError:
                word.append('')
        result.append(''.join(word))

    return ' '.join(result).strip()
