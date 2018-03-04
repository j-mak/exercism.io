import random
import string


class Robot(object):
    def __init__(self):
        self.__name = self.__generate()

    @property
    def name(self):
        return self.__name

    def reset(self):
        self.__name = self.__generate()

    @staticmethod
    def __generate():
        rand_char = random.SystemRandom().choice(string.ascii_uppercase)
        rand_num = random.SystemRandom().choice(string.digits)
        result = rand_char + rand_char + rand_num + rand_num + rand_num
        return result
