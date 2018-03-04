class Garden(object):
    seed = {
        "R": "Radishes",
        "C": "Clover",
        "G": "Grass",
        "V": "Violets"
    }

    def __init__(self, seeds, students=("Alice", "Bob", "Charlie", "David",
                                        "Eve", "Fred", "Ginny", "Harriet",
                                        "Ileana", "Joseph", "Kincaid",
                                        "Larry")):
        self.students = sorted(students)
        self.seeds = seeds.split('\n')

    def plants(self, name):
        """Returns plants owned for given name."""
        result = []
        if name in self.students:
            index = self.students.index(name)
            for group in self.seeds:
                for i in range(index * 2, index * 2 + 2):
                    result.append(self.seed.get(group[i]))
        return result
