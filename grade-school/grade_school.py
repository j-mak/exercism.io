from collections import defaultdict


class School(object):
    def __init__(self, school_name):
        self.name = school_name
        self.grades = defaultdict(set)

    def add(self, student_name, student_grade):
        """Add student with given grade to school."""
        self.grades[student_grade].add(student_name)

    def grade(self, find_grade):
        """Returns students which have given grade."""
        return self.grades[find_grade]

    def sort(self):
        """Sorts students in group."""
        grades = sorted(self.grades.keys())
        return tuple(map(lambda x: (x, tuple(sorted(self.grades[x]))), grades))
