class Matrix(object):
    def __init__(self, matrix_string):
        """
        Matrix class.

        Args:
            matrix_string: string representation of Matrix.
        """
        self.data = [
            [
                int(column) for column in row.split(' ')
            ] for row in matrix_string.split('\n')]

    def row(self, index):
        """
        Return row from Matrix at specific index.

        Args:
            index:
                index of row in Matrix

        Returns:
            List of numbers in specific row.
        """
        return self.data[index]

    def column(self, index):
        """
        Return column from Matrix at specific index.

        Args:
            index:
                index of wanted column in Matrix
        Returns:
            List of numbers in specific column
        """
        result = []
        for col in self.data:
            result.append(col[index])
        return result