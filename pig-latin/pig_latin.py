VOWELS = ('a', 'e', 'i', 'o', 'u', 'yt', 'xr')

CONSONANTS = ('b', 'c', 'd', 'f', 'g',
              'h', 'j', 'k', 'l', 'm',
              'n', 'p', 'q', 'r', 's',
              't', 'v', 'w', 'x', 'y',
              'z', 'sh', 'sch', 'zz', 'gh',
              'ch', 'th', 'qu', 'thr',
              'squ')


def translate(sentence):
    result = []
    for word in sentence.split(' '):
        if word[:3] in CONSONANTS:
            word = word[3:] + word[:3]
        elif word[:2] in CONSONANTS:
            word = word[2:] + word[:2]
        elif word[0] in CONSONANTS and word[:2] not in VOWELS:
            word = word[1:] + word[0]

        result.append(word + 'ay')
    return " ".join(result)
