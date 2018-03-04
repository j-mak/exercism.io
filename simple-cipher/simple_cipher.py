import random
import string


class Cipher:
    random_key_length = 100

    def __init__(self, key=None):
        self.key = key if key is not None else self.generate_random_key()
        if not self.valid_key():
            raise ValueError()

    def encode(self, phrase):
        return ''.join([chr(self.wrap(ord(c) + self.offset(i))) for i, c in
                        enumerate(self.clean(phrase))])

    def decode(self, phrase):
        return ''.join([chr(self.wrap(ord(c) - self.offset(i))) for i, c in
                        enumerate(self.clean(phrase))])

    @staticmethod
    def clean(phrase):
        return filter(str.isalpha, phrase.lower())

    def generate_random_key(self):
        return ''.join(random.SystemRandom().choice(string.ascii_lowercase)
                       for _ in range(self.random_key_length))

    def valid_key(self):
        return self.key.isalpha() and self.key.islower()

    def offset(self, index):
        return self.wrap(ord(self.key[index % len(self.key)]) - 97)

    @staticmethod
    def wrap(val):
        while val > 122:
            val -= 26
        while val < 97:
            val += 26
        return val


class Caesar:
    def __init__(self):
        self.cipher = Cipher('d')

    def encode(self, phrase):
        return self.cipher.encode(phrase)

    def decode(self, phrase):
        return self.cipher.decode(phrase)
