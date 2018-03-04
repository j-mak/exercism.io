allergies = {
    1: 'eggs',
    2: 'peanuts',
    4: 'shellfish',
    8: 'strawberries',
    16: 'tomatoes',
    32: 'chocolate',
    64: 'pollen',
    128: 'cats'
}


class Allergies(object):
    def __init__(self, score):
        """Calculates allergies for given score."""
        self.score = score
        self.lst = []
        self.__calculate_allergies()

    def __calculate_allergies(self):
        """Pseudo private method for generating list of allergies."""
        for i, allergy in allergies.items():
            if i & self.score:
                self.lst.append(allergy)

    def is_allergic_to(self, food):
        """Check if person is allergic on given food."""
        return food in self.lst
