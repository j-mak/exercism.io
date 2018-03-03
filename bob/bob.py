def hey(sentence):
    """Return bob's answer on sentence."""
    sentence = sentence.strip()
    if sentence.isupper():
        return "Whoa, chill out!"
    elif not sentence:
        return "Fine. Be that way!"
    elif sentence.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
