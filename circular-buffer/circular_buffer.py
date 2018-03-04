class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, size):
        self.__read = 0
        self.__write = 0
        self.__size = size
        self.buff = [None for _ in range(size)]

    def write(self, item):
        if all(self.buff):
            raise BufferFullException
        self.buff[self.__write] = item
        self.__write = (self.__write + 1) % self.__size

    def read(self):
        if not any(self.buff):
            raise BufferEmptyException
        value = self.buff[self.__read]
        self.buff[self.__read] = None
        self.__read = (self.__read + 1) % self.__size
        return value

    def overwrite(self, item):
        self.buff[self.__write] = item
        self.__read = (self.__read + 1) % self.__size
        self.__write = (self.__write + 1) % self.__size

    def clear(self):
        self.buff = [None for _ in range(self.__size)]
        self.__read = 0
        self.__write = 0
