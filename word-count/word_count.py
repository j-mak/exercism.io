def word_count(sentence):
    """Return JSON with words from sentence and count of they."""
    result = {}
    word = ""
    for char in sentence.lower():
        if char.isalnum():
            word += char
        else:
            if len(word):
                if result.get(word):
                    result[word] += 1
                else:
                    result.update({word: 1})
                word = ""
    # to process last word
    if result.get(word) and len(word):
        result[word] += 1
    elif len(word):
        result.update({word: 1})
    return result
