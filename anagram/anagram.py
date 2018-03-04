def detect_anagrams(word, candidates):
    """Return list of anagrams to given word from list of candidates."""
    response = []
    word = word.lower()
    word_list = sorted(word)

    for c in candidates:
        c_lower = c.lower()
        if word != c_lower and sorted(list(c_lower)) == word_list:
            response.append(c)

    return response
